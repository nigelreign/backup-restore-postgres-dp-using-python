import argparse
import logging
import subprocess
import os
import tempfile
from tempfile import mkstemp

import configparser
import gzip
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def backup_postgres_db(host, database_name, port, user, password, dest_file):
    """
    Backup postgres db to a file.
    """
    process = subprocess.Popen(
        ['pg_dump',
            '--dbname=postgresql://{}:{}@{}:{}/{}'.format(user, password, host, port, database_name),
            '-Fc',
            '-f', dest_file,
            '-v'],
        stdout=subprocess.PIPE
    )
    output = process.communicate()[0]
    if int(process.returncode) != 0:
        print('Command failed. Return code : {}'.format(process.returncode))
        exit(1)
    return output

host = "localhost"
database_name = "test"
port="5432"
user="postgres"
password="postgres"
dest_file="dump.sql"

backup_postgres_db(host, database_name, port, user, password, dest_file)
