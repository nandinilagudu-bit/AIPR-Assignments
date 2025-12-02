-- Library Management Schema (PostgreSQL)
-- Tables: books, members, loans
-- Includes integrity constraints, indexes and a trigger to keep available_copies consistent.

CREATE TABLE books (
    book_id       SERIAL PRIMARY KEY,
    isbn          VARCHAR(20) UNIQUE,
    title         TEXT NOT NULL,
    author        VARCHAR(255),
    publisher     VARCHAR(255),
    published_year SMALLINT,
    category      VARCHAR(100),
    total_copies  INT NOT NULL DEFAULT 1 CHECK (total_copies >= 0),
    available_copies INT NOT NULL DEFAULT 1 CHECK (available_copies >= 0 AND available_copies <= total_copies),
    created_at    TIMESTAMP WITH TIME ZONE DEFAULT now()
);

CREATE TABLE members (
    member_id     SERIAL PRIMARY KEY,
    first_name    VARCHAR(100) NOT NULL,
    last_name     VARCHAR(100),
    email         VARCHAR(255) UNIQUE,
    phone         VARCHAR(30),
    address       TEXT,
    joined_date   DATE DEFAULT CURRENT_DATE,
    is_active     BOOLEAN DEFAULT TRUE
);

CREATE TABLE loans (
    loan_id       SERIAL PRIMARY KEY,
    book_id       INT NOT NULL REFERENCES books(book_id) ON DELETE RESTRICT,
    member_id     INT NOT NULL REFERENCES members(member_id) ON DELETE CASCADE,
    loan_date     DATE NOT NULL DEFAULT CURRENT_DATE,
    due_date      DATE NOT NULL,
    return_date   DATE,
    status        VARCHAR(20) NOT NULL DEFAULT 'on_loan' CHECK (status IN ('on_loan','returned','overdue')),
    fine          NUMERIC(8,2) DEFAULT 0 CHECK (fine >= 0),
    CONSTRAINT chk_dates CHECK (due_date >= loan_date AND (return_date IS NULL OR return_date >= loan_date))
);

-- Useful indexes
CREATE INDEX idx_loans_member ON loans(member_id);
CREATE INDEX idx_loans_book ON loans(book_id);
CREATE INDEX idx_books_isbn ON books(isbn);

-- Trigger function to adjust books.available_copies when loans are inserted/updated/deleted
CREATE OR REPLACE FUNCTION trg_loans_adjust_inventory()
RETURNS trigger LANGUAGE plpgsql AS $$
DECLARE
    avail INT;
BEGIN
    IF TG_OP = 'INSERT' THEN
        IF NEW.status = 'on_loan' THEN
            SELECT available_copies INTO avail FROM books WHERE book_id = NEW.book_id FOR UPDATE;
            IF avail IS NULL OR avail <= 0 THEN
                RAISE EXCEPTION 'No available copies for book %', NEW.book_id;
            END IF;
            UPDATE books SET available_copies = available_copies - 1 WHERE book_id = NEW.book_id;
        END IF;

    ELSIF TG_OP = 'UPDATE' THEN
        -- Book changed
        IF OLD.book_id <> NEW.book_id THEN
            IF OLD.status = 'on_loan' THEN
                UPDATE books SET available_copies = available_copies + 1 WHERE book_id = OLD.book_id;
            END IF;
            IF NEW.status = 'on_loan' THEN
                SELECT available_copies INTO avail FROM books WHERE book_id = NEW.book_id FOR UPDATE;
                IF avail IS NULL OR avail <= 0 THEN
                    RAISE EXCEPTION 'No available copies for book %', NEW.book_id;
                END IF;
                UPDATE books SET available_copies = available_copies - 1 WHERE book_id = NEW.book_id;
            END IF;

        ELSE
            -- Same book, status changed
            IF OLD.status <> NEW.status THEN
                IF OLD.status = 'on_loan' AND NEW.status = 'returned' THEN
                    UPDATE books SET available_copies = available_copies + 1 WHERE book_id = NEW.book_id;
                ELSIF OLD.status = 'returned' AND NEW.status = 'on_loan' THEN
                    SELECT available_copies INTO avail FROM books WHERE book_id = NEW.book_id FOR UPDATE;
                    IF avail IS NULL OR avail <= 0 THEN
                        RAISE EXCEPTION 'No available copies for book %', NEW.book_id;
                    END IF;
                    UPDATE books SET available_copies = available_copies - 1 WHERE book_id = NEW.book_id;
                END IF;
            END IF;
        END IF;

    ELSIF TG_OP = 'DELETE' THEN
        IF OLD.status = 'on_loan' THEN
            UPDATE books SET available_copies = available_copies + 1 WHERE book_id = OLD.book_id;
        END IF;
    END IF;

    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_loans_inventory
    AFTER INSERT OR UPDATE OR DELETE ON loans
    FOR EACH ROW EXECUTE FUNCTION trg_loans_adjust_inventory();

-- Optional: view for active loans
CREATE VIEW active_loans AS
SELECT l.loan_id, l.book_id, b.title, l.member_id, m.first_name || ' ' || m.last_name AS member_name,
             l.loan_date, l.due_date, l.status
FROM loans l
JOIN books b ON b.book_id = l.book_id
JOIN members m ON m.member_id = l.member_id
WHERE l.status = 'on_loan';