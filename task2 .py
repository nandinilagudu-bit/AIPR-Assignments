def read_file(filename):
    try:
        with open(filename, "r") as f:
            data = f.read()
        return data
    except FileNotFoundError:
        return "Error: File not found."
    except IOError:
        return "Error: Unable to read file."
