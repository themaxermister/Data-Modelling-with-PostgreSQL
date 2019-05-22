# SUCCESSFUL

import psycopg2
from sql_queries import create_table_queries, drop_table_queries

def create_database():
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=udacity user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # grant permission to tables
    cur.execute("GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO student;")
   
    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    conn.set_session(autocommit=True)

    return cur, conn

def drop_tables(cur, conn):
    for query in drop_table_queries:
        try:
                cur.execute(query)
        except psycopg2.Error as e: 
                print("Error: Dropping table")
                print (e)

        #conn.commit()


def create_tables(cur, conn):
    for query in create_table_queries:
        try:
                cur.execute(query)
        except psycopg2.Error as e: 
                print("Error: Issue creating table")
                print (e)
                
        #conn.commit()

def main():
    cur, conn = create_database()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()
    print ("DISCONNECT")


if __name__ == "__main__":
    main()
    