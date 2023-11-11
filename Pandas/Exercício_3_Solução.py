import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    inicio = employees.head(3)
    return inicio