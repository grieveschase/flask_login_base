import sqlite3
import io
from io import BytesIO
from PIL import Image
import datetime
from datetime import timedelta

conn = sqlite3.connect('SQLite.db', detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
cur = conn.cursor()
t1 = datetime.datetime.now() - datetime.timedelta(hours = 5)
lot = '4938192RS8'
sql_in = '''select
            Slot,
            FOV,
            Iprobe,
            Lot,
            Vhar,
            Recipe,
            Site,
            Field,
            ToolId,
            LocationX,
            LocationY,
            Date,
            Port,
            Cycle,
            Image
            from PatternFov
            where Lot= '%s'
            and Recipe like '%s' ''' %(lot, 'DWRV6A_FCESME')
cur.execute(sql_in)
data = [list(row) for row in cur]
cur.close()
conn.close()

print('Rows returned: ', len(data))
for tic in data:
    print(tic[:-1])

    img_blob =tic[-1]
    image = Image.open(io.BytesIO(img_blob))
    #save_string = "/home/ccag/test_scripts/django_ccag/project1/app1/static/app1/"+ image_name
    save_string = 'test_image%s.JPG' %tic[-2]
    image.save(save_string, quality=80)
    image.close()
