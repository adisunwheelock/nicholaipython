import os
import json
from mysql import connector

vcap = json.loads(os.getenv("VCAP_SERVICES"))
creds = vcap['mysql'][0]['credentials']

conn = connector.connect(host=creds['host'],
                         port=creds['port'],
                         user=creds['user'],
                         password=creds['password'])
cursor = conn.cursor()
cursor.execute("SHOW DATABASES")
cursor.fetchall()
cursor.execute("USE d4b34d227c2484ba6afcd7a02f3d7d977")
cursor.execute("SHOW TABLES")
cursor.fetchall()
