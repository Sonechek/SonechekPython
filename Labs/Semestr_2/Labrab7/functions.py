import pymysql.cursors
# from functions import get_connection

connection = pymysql.connect(
        host='pgsha.ru',
        user='soft0049',
        password='tWpds59l',
        db='soft0049_labrab',
        port=35006,
        cursorclass=pymysql.cursors.DictCursor)


def students_kunger():
    try:
        with connection.cursor() as cur:
            sql = f"SELECT `nameStud` FROM 'students' WHERE `city` = 'Кунгур'"
            names_from_sql = list(cur)
    finally:
        connection.close()
        return names_from_sql


def mans_Kungur():
  
    try:
        with connection.cursor() as cur:
            sql = f"SELECT `nameStud` FROM 'students' WHERE `city` = 'Кунгур' AND `gender` = 1"
            names_from_sql = list(cur)
    finally:
        connection.close()
        return names_from_sql


def mans_rating_Kungur():
    try:
        with connection.cursor() as cur:        
            sql = f"SELECT `nameStud`,`rating` FROM 'students' WHERE `city` = 'Кунгур' AND `gender` = 1 ORDER BY `rating` DESC"
            names_from_sql = list(cur)
    finally:
        connection.close()
        return names_from_sql


def names_not_from_Perm():
    try:
        with connection.cursor() as cur:
            sql = f"SELECT `nameStud`,`rating` FROM 'students' WHERE `city` <> 'Пермь' ORDER BY `date` ASC"
            names_from_sql = list(cur)
    finally:
        connection.close()
        return names_from_sql
    

def select_all_sorted():
    try:
        with connection.cursor() as cur:
            sql = f"SELECT `nameStud` FROM 'students' ORDER BY `city` ASC, `rating` DESC"
            names_from_sql = list(cur)
    finally:
        connection.close()
        return names_from_sql
