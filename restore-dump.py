import subprocess
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def restore_postgres_db(db_host, db, port, user, password, backup_file):
    """
    Restore postgres db from a file.
    """

    print(user,password,db_host,port, db)
    process = subprocess.Popen(
        ['pg_restore',
            '--no-owner',
            '--dbname=postgresql://{}:{}@{}:{}/{}'.format(user,
                                                        password,
                                                        db_host,
                                                        port, db),
            '-v',
            backup_file],
        stdout=subprocess.PIPE
    )
    output = process.communicate()[0]
    if int(process.returncode) != 0:
        print('Command failed. Return code : {}'.format(process.returncode))

    return output

host = "localhost"
database_name = "test"
port="5432"
user="postgres"
password="postgres"
dest_file="dump.sql"

restore_postgres_db(host, database_name, port, user, password, dest_file)
