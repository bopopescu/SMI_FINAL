
from DBconnection import connection2
import codecs

cur, db, engine = connection2()

cur.execute('SELECT key_word FROM SMI_DB.KeyWord')

data = cur.fetchall()

db_word= []
for each in data:
    db_word.append(each[0])

user_word = []


#user_word = codecs.open("keywords.txt", mode="r", encoding='utf-8')
f = open("keywords.txt", mode="r", encoding='utf-8')
for line in f:
    #print(line)
    user_word.append(line.rstrip('\n'))
    '''if line in db_word:
        print(line,"In database")
        print('*********')
    else:
        print(line,"New word")
        print('*********')'''



'''for each in user_word:
    print(each)'''

new_words= set(user_word) - set(db_word)
print(new_words)

#print(db_word)
#print(user_word)

for each in new_words:
    #print(each)
    '''query = "INSERT INTO SMI_DB.KeyWord (word) VALUES(%s)"
    val = (each)
    cur.execute(query, val)'''
    '''SQLInsertCmd = "INSERT INTO SMI_DB.KeyWord (key_word) VALUES (%s)" % (each)
    print(SQLInsertCmd)
    cur.execute(SQLInsertCmd)'''

    cur.execute("""INSERT INTO  SMI_DB.KeyWord (key_word) VALUES (%s)""", (each,))

    #db.close()
