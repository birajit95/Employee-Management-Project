from datetime import datetime
import sqlite3
from pathlib import Path
from django.core.exceptions import ValidationError

def get_current_financial_year():
    current_year = datetime.now().year
    month = datetime.now().month

    if int(month) >= 7:
        return f"{current_year}-{int(current_year)+1}"
    else:
        return f"{int(current_year)-1}-{current_year}"
    

def generic_file_type_allowance_validation(file, file_type):
    path = Path(file.name)
    file_extension = path.suffix.lower()
    if file_extension != f".{file_type.lower()}":
        raise ValidationError(f"Only {file_type} file is allowed")
    return sqlite3.Binary(file.read())

