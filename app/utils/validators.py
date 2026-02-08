import re

def validate_financial_data(data: list, valid_categories: list, valid_sources: list):
    """
    Validates financial data input.
    Expected format: ["date", "category","sub_category", "description","amount","source"]
    - date: YYYY-MM-DD
    - category: non-empty string ["Pemasukan", "Pengeluaran"]
    - sub_category: non-empty string ["ce","co"] if Pemasukan, else ["Top up","Groceries","Galon", "Food","Laundry","Parkir","Kos","Bensin","SkinBody Care","Lainnya"]
    - description: non-empty string
    - amount: numeric (positive)
    - source: non-empty string ["Cash","etc"]
    """
    # Check number of fields
    if not data or len(data) != 6:
        return False, None, "Invalid number of data fields. Expected 6 fields. Make sure to separate each field with a comma."
    date, category, sub_category, description, amount, source = data

    # Validate date
    date_pattern = r"^\d{4}-\d{2}-\d{2}$"
    if not re.match(date_pattern, date):
        return False, None, "Invalid date format. Expected YYYY-MM-DD."
    
    # Validate category
    if category not in ["pemasukan", "pengeluaran"]:
        return False, None, "Invalid category. Must be either 'pemasukan' or 'pengeluaran'."
    # Validate sub_category
    if category == "pemasukan":
        if sub_category.lower() not in ["ce", "co"]:
            return False, None, "Invalid sub-category for 'pemasukan'. Must be either 'ce' or 'co'."
    else:
        if sub_category.lower() not in [cat.lower() for cat in valid_categories]:
            return False, None, f"Invalid sub-category for 'pengeluaran'. Must be one of {valid_categories}."
    # validate numeric amount
    try:
        amount_value = float(amount)
        if amount_value <= 0:
            return False, None, "Amount must be a positive number."
    except ValueError:
        return False, None, "Invalid amount. Must be a numeric value."
    # Validate source
    if source.lower() not in [src.lower() for src in valid_sources]:
        return False, None, f"Invalid source. Must be one of {valid_sources}."

    return True, [date, category, sub_category, description, amount_value, source], None