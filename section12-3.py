# 파이썬 데이터베이스 연동(SQLite)
# 테이블 데이터 수정 및 삭제

import sqlite3

# DB 생성
conn = sqlite3.connect("C:/python_workspace/resource/database.db")

# Curser 연결
c = conn.cursor()



# 데이터 수정 1
# c.execute("update users set username = ? where id = ?", ("niceman", 2))

# 데이터 수정 2
# c.execute("update users set username = :name where id = :id", {"name" : "goodman", "id" : 5})

# 데이터 수정 3
# c.execute("update users set username = '%s' where id = '%d'" %("badboy", 3))



# 중간 데이터 확인 1
# for user in c.execute("select * from users") :
#     print(user)




# Row Delete 1
# c.execute("delete from users where id = ?", (2, ))

# Row Delete 2
# c.execute("delete from users where id = :id", {"id" : 5})

# Row Delete 3
# c.execute("delete from users where id = '%s'" %(4, ))



# 중간 데이터 확인 2
# for user in c.execute("select * from users") :
#     print(user)



# 테이블 전체 데이터 삭제
# print("users db deleted : ", conn.execute("delete from users").rowcount, " rows")



# 커밋
# conn.commit()

# 접속 해제
# conn.close()