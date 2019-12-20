# 파이썬 데이터베이스 연동(SQLite)
# 테이블 조회

import sqlite3

# DB 파일 연결(없으면 새로 생성)
conn = sqlite3.connect("C:/python_workspace/resource/database.db")

# 커서 바인딩
c = conn.cursor()

# 데이터 조회(전체)
c.execute("select * from users")

# 커서 위치가 변경
# 1개 로우 선택
# print("One -> \n", c.fetchone())

# 지정 로우 선택
# print("Three -> \n", c.fetchmany(size = 3))

# 전체 로우 선택
# print("All -> \n", c.fetchall())
# 커서가 가리키는게 없으면 빈 리스트
# print("All -> \n", c.fetchall())


# 순회 1
# rows = c.fetchall()
# for row in rows :
#     print("retrieve1 > ", row)

# 순회 2, 선호
# for row in c.fetchall() : 
#     print("retrieve2 > ", row)

# 순회 3
# desc : 역순으로
# for row in c.execute("select * from users order by id desc") :
#     print("retrieve3 > ", row)


# where : ?, %, dict

# where retrieve1
# 튜플 바인딩
param1 = (3, )
c.execute("select * from users where id = ?", param1)
print("param1 > ", c.fetchone())
print("param1 > ", c.fetchall()) # 커서가 가리키는 데이터가 이제 없으므로 빈리스트

# where retrieve2
# 정수 바인딩
param2 = 4
c.execute("select * from users where id = '%s'" %(param2))
print("param2 > ", c.fetchone())
print("param2 > ", c.fetchall())

# where retrieve3
# 딕셔너리 바인딩
c.execute("select * from users where id = :Id", {"Id" : 5})
print("param3 > ", c.fetchone())
print("param3 > ", c.fetchall())

# where retrieve4
param4 = (3, 5)
c.execute("select * from users where id in(?, ?)", param4)
print("param4 > ", c.fetchall())

# where retrieve5
c.execute("select * from users where id in('%d', '%d')" %(3, 4))
print("param5 > ", c.fetchall())

# where retrieve6
c.execute("select * from users where id = :id1 or id = :id2", {"id1" : 2, "id2" : 5})
print("param6 > ", c.fetchall())



# Dump 출력
# with : 자동 close() 호출
with conn :
    with open("C:/python_workspace/resource/dump.sql", "w") as f :
        for line in conn.iterdump() :
            f.write("%s\n" % line)
        print("Dump Print Complete")