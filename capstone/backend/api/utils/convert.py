from sqlalchemy import text
from sqlalchemy.orm import Session
from typing import List, Dict

def convert_to_table(
        session: Session,
        sql: str
    ) -> List[Dict[str, any]]:

    result = session.execute(text(sql))
    column_names = result.keys()

    # Directly create the list of dictionaries from the fetched rows
    return [dict(zip(column_names, row)) for row in result]

