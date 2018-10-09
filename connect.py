import MySQLdb
import keys as k
import datetime


def get_ruts():
    try:
        db = MySQLdb.connect(host=k.host, user=k.user, passwd=k.passwd, db=k.db)    
        cur = db.cursor()
        # Se hace el replace en este caso porque la BD que estoy usando no está normalizada. 
        # Luego se agregan los puntos con format_rut.py
        cur.execute('SELECT REPLACE(' + k.column + ', ".","") ' + k.column + ' FROM ' + k.tableSelect)
        listaRuts = []
        for row in cur.fetchall():
            listaRuts.append(row[0])

        db.close()
        return listaRuts
    except:
        raise Exception

def insert_data(datos, rut_consulta):
    try:
        db = MySQLdb.connect(host=k.host, user=k.user, passwd=k.passwd, db=k.db)    
        cur = db.cursor()
        now = datetime.datetime.now()
        for data in datos:
            query = 'INSERT INTO ' + k.tableInsert + '(periodo, origen, cuenta, rut_empleador, razon_social, estado, AFP_AFC, rut_consulta, fecha_consulta) VALUES("' + data[0] + '","' + data[1] + '","' + data[2] + '","' + data[3] + '","' + data[4] + '","' + data[5] + '","' + data[6] + '","' + rut_consulta + '","' + str(now) + '")'
            cur.execute(query)
        db.commit()
        db.close()
        print("Datos Insertados.")
        return True
    except:
        raise Exception
        
    