import psycopg2
def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        
        conn = psycopg2.connect(
                database="att", user='postgres', password='bhargav1', host='localhost', port= '5432')
		
        return conn
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)



if __name__ == '__main__':
    connect()