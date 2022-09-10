from sqlalchemy.sql import text


def truncate_tables(client):
    conn = client.application.engine.connect()
    sql = """
        truncate table "user" cascade;
        truncate table post cascade;
        truncate table post_like cascade;
        truncate table post_comment cascade;
    """
    conn.execute(text(sql))
    return
