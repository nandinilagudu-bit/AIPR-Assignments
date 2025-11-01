def calculate_energy_charges(units, customer_type):
    """Calculate energy charges based on TGNPDCL domestic tariff slabs"""
    if customer_type.upper() == 'D':  # Domestic
        total = 0
        remaining = units

        # TGNPDCL realistic slab rates
        if remaining > 0:
            u = min(50, remaining)
            total += u * 1.90
            remaining -= u
        if remaining > 0:
            u = min(50, remaining)
            total += u * 3.00
            remaining -= u
        if remaining > 0:
            total += remaining * 4.80
        return round(total, 2)

    elif customer_type.upper() == 'C':  # Commercial
        if units <= 100:
            return round(units * 6.15, 2)
        elif units <= 200:
            return round((100 * 6.15) + ((units - 100) * 7.15), 2)
        else:
            return round((100 * 6.15) + (100 * 7.15) + ((units - 200) * 8.50), 2)

    elif customer_type.upper() == 'I':  # Industrial
        if units <= 500:
            return round(units * 7.45, 2)
        else:
            return round((500 * 7.45) + ((units - 500) * 8.50), 2)

    return 0


def calculate_fixed_charges(customer_type, load_kw=1):
    """Fixed charge Rs.10 per kW"""
    return round(10 * load_kw, 2)


def calculate_customer_charges(customer_type):
    """Customer charge — fixed ₹70 for domestic"""
    if customer_type.upper() == 'D':
        return 70.00
    elif customer_type.upper() == 'C':
        return 120.00
    elif customer_type.upper() == 'I':
        return 200.00
    return 0.0


def calculate_electricity_duty(ec):
    """Electricity duty ~2.4% of EC"""
    return round(0.024 * ec, 2)


def print_bill(previous_reading, current_reading, customer_type, load_kw):
    """Generate and print full bill"""
    units = current_reading - previous_reading

    ec = calculate_energy_charges(units, customer_type)
    fc = calculate_fixed_charges(customer_type, load_kw)
    cc = calculate_customer_charges(customer_type)
    ed = calculate_electricity_duty(ec)
    total_bill = round(ec + fc + cc + ed, 2)

    print("\n" + "=" * 60)
    print("        TELANGANA STATE NORTHERN POWER DISTRIBUTION COMPANY")
    print("=" * 60)
    print(f"Customer Type     : {'Domestic' if customer_type.upper()=='D' else customer_type}")
    print(f"Contracted Load   : {load_kw:.2f} kW")
    print(f"Previous Reading  : {previous_reading}")
    print(f"Current Reading   : {current_reading}")
    print(f"Units Consumed    : {units}")
    print("-" * 60)
    print(f"Energy Charges (EC)     : ₹{ec:.2f}")
    print(f"Fixed Charges (FC)      : ₹{fc:.2f}")
    print(f"Customer Charges (CC)   : ₹{cc:.2f}")
    print(f"Electricity Duty (ED)   : ₹{ed:.2f}")
    print("-" * 60)
    print(f"Total Bill Amount       : ₹{total_bill:.2f}")
    print("=" * 60)
    return total_bill


def main():
    print("TGNPDCL ELECTRICITY BILL GENERATOR")
    print("Customer Types: Domestic (D), Commercial (C), Industrial (I)")
    print("-" * 50)

    try:
        prev = float(input("Enter Previous Reading (PU): "))
        curr = float(input("Enter Current Reading (CU): "))
        if curr < prev:
            print("Error: Current reading cannot be less than previous reading!")
            return

        cust_type = input("Enter Customer Type (D/C/I): ").strip().upper()
        if cust_type not in ['D', 'C', 'I']:
            print("Error: Invalid customer type! Enter D, C, or I.")
            return

        load = float(input("Enter Sanctioned Load (in kW): "))
        if load <= 0:
            print("Error: Load must be greater than 0.")
            return

        print_bill(prev, curr, cust_type, load)

    except ValueError:
        print("Error: Please enter valid numbers!")


if __name__ == "__main__":
    main()
