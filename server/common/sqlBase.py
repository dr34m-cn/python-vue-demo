import sqlite3

from common.config import CONFIG


def connect_sql(func):
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect(CONFIG['db']['dbname'])
        result = func(conn, *args, **kwargs)
        conn.close()
        return result

    return wrapper


@connect_sql
def fetchall(conn, query, params=()):
    cursor = conn.cursor()
    cursor.execute(query, params)
    rst = cursor.fetchall()
    cursor.close()
    return rst


@connect_sql
def fetch_first_val(conn, query, params=()):
    cursor = conn.cursor()
    cursor.execute(query, params)
    rst = cursor.fetchone()
    cursor.close()
    return rst[0]


@connect_sql
def fetchall_to_table(conn, query, params=()):
    cursor = conn.cursor()
    cursor.execute(query, params)
    rst = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    cursor.close()
    results = []
    for row in rst:
        results.append(dict(zip(columns, row)))
    return results


@connect_sql
def execute_insert(conn, query, params=()):
    cursor = conn.cursor()
    cursor.execute(query, params)
    lastId = cursor.lastrowid
    conn.commit()
    cursor.close()
    return lastId


@connect_sql
def execute_manny(conn, query, params=()):
    cursor = conn.cursor()
    cursor.executemany(query, params)
    conn.commit()
    cursor.close()


@connect_sql
def execute_update(conn, query, params=()):
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    cursor.close()
