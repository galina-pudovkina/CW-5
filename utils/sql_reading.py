from config import QUERIES_PATH


def sql_reading():
    """
    Метод для чтения sql запросов.
    """
    sql_quries_dict = {}
    current_query_name = None
    curernt_query = ""
    with open(QUERIES_PATH, encoding='UTF-8') as fp:
        for line in fp:
            if line.startswith("--"):
                if current_query_name and curernt_query:
                    sql_quries_dict[current_query_name] = curernt_query
                current_query_name = line.lstrip("--").strip()
                curernt_query = ''
            else:
                curernt_query += line

    if current_query_name and curernt_query:
        sql_quries_dict[current_query_name] = curernt_query.strip()

    return sql_quries_dict

