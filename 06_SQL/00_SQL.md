# SQL

- Structured Query Language : 구조화된 질의문을 쓰는 언어



## 데이터베이스

- 데이터가 모여있다



## RDBMS(관계형데이터베이스 관리시스템)

- 관계형 모델을 기반으로 하는 데이버 베이스 관리 시스템이다

- 대표적인 오픈소스 MySQL, ,SQLite, PostgreSQL(무료) 오라클, MSSQL(유료) 이 있다

  |      | SQLite                   | MySQL(2위)                                   | PostgreSQL | 오라클(1위) | MSSQL    |
  | ---- | ------------------------ | -------------------------------------------- | ---------- | ----------- | -------- |
  |      | 파일                     | 프로그램                                     | 프로그램   | 프로그램    | 프로그램 |
  |      | 데이터가 파일에 저장된다 | 데이터 서비스 본격적으로 하면 이거 많이 사용 |            |             |          |



## SQLite (무료, 경량화가 포인트) 마지막에 세미콜론 꼭 적기!

- SQLite은 **서버가 아닌 응용프로그램에 넣어 사용하는 비교적 가벼운 데이터베이스**이다.
- 구글 안드로이드 운영 체제에 기본적으로 탑재된 데이터베이스이다.
- 임베디드 소프트웨어에도 많이 활용이 되고 있다
- 로컬에서 간단한 DB 구성을 할 수 있으며, 오픈 소스 프로젝트이기 때문에 자유롭게 사용할 수 있다
- 우리는 빨리 SQL을 만져보는게 포인트라서 SQLite 사용한다. 나머지 4개의 프로그램은 까는데만 2시간 걸리기 때문이다.



## 기본용어 정리

### 스키마(scheme)

- 데이터베이스에서 자료의 구조, 표현방법, 관계들을 정의한 구조
- 데이터베이스의 구조와 제약조건에 대해서 자세히 명세한 것
- colunm, datatype는 항상 같이 다닌다
- 스키마를 지정해서 테이블을 만들어 놓고 거기 맞는 값을 지정해서 넣는거

| colunm | datatype |
| ------ | -------- |
|        |          |



#### 예제)

- 처음 데이터베이스트를 키면 흰 바탕화면

- 스키마를 id(INT), feeling(STRING), timestamp(DATETIME) 정하고 (데이터 모델링 과정)
- 결정!을 누르면
- 테이블을 생성한다 
- 하나의 데이터베이스 안에 여러가지 테이블 가능!
- 스키마를 id(INT), meun1(STRING), meun2(STRING) 정하고
- 결정!을 누르면
- 테이블을 생성한다 

| id(INT) | meun1(STRING) | meun2(STRING) |
| ------- | ------------- | ------------- |
|         |               |               |

- 한줄 한줄을 data record = row  라고 부른다
- data record가 쓰여지고 나서 id값이 생성 됨



## SQLite3 전용 명령어

| 명령어                             | 설명                                        |
| ---------------------------------- | ------------------------------------------- |
| `.mode  Mcsv`                      | csv 모드                                    |
| `.mode column`                     | 컬럼 모드                                   |
| `.headers on`                      | 헤더(컬럼이름) 같이 출력                    |
| `.read <file.sql>`                 | 해당 sql 스크립트 실행                      |
| `.import <file.name> <tabel_name>` | 해당 파일의 데이터를 지정한 테이블에 import |
| `.schema`                          | 스키마 전체 보기                            |



## SQL 명령어

- 명령어 예약어는 무조건 대문자
- table name은 소문자
- . 찍고 나서 명령어는 sql에 묻는게 아니라 sqlite프로그램 조작 의미이기 때문에 소문자로 적어도 됨!
- salite3 my_db.sqlite3
- `.import 파일명.csv 테이블이름`



### TABLE 조작 관련

#### Table 생성

```sql
CREATE TABLE <table_name> (
	<col> DATA_TYPE PRIMARY KEY AUTOINCREMENT,
    <col> DATA_TYPE NOT NULL,
    <col> DATA_TYPE DEFAULT <value>,
    ...
);
```



#### Table ( + 레코드 모두) 삭제

```sql
DROP TABLE <table_name>;
```



#### Table 이름 수정

```plsql
ALTER TABLE <table_name>
RENAME TO <new_table_name>;
```



#### Table 컬럼 추가

```sql
ALTER TABLE <table_name>
ADD COLUMN <new_col_name> DATATYPE;
```



### Data 조작 관련

#### Data 생성 (Create)

```sql
INSERT INTO <table_name> (<col_name_1>, <col_name_2>, ...)
VALUES
(<value_1>, <value_2>, ...),
(<value_1>, <value_2>, ...),
...
(<value_1>, <value_2>, ...);

```



#### Data 조회 (Read, Retrieve)

##### 테이블에서 데이터 전체를 모든 col 에 대하여 조회

```sql
SELECT * FROM <table_name>;
```

##### 테이블에서 특정 컬럼만 조회

```sql
SELECT <col_1>, <col_2>, ... FROM <table_name>;
```

##### 특정 조건으로 전체 컬럼 조회

```sql
SELECT * FROM <table_name> WHERE [condition];
```



#### Data 수정 (Update)

```sql
UPDATE <table_name>
SET <col_1>=<val_1>, <col_2>=<val_2>, ...
WHERE [condition]; -- 보통 primary key (id) 로 선택
```



#### Data 삭제 (Delete, Destroy)

```sql
DELETE FROM <table_name>
WHERE [condtion]; -- 보통 primary key (id) 로 선택
```



### Expression

#### 해당 컬럼의 갯수

```sql
SELECT COUNT(<col>) FROM <table_name>;
```



#### 해당 컬럼의 

```sql
-- 평균
SELECT AVG(<col>) FROM <table_name>;
-- 총합
SELECT SUM(<col>) FROM <table_name>
-- 최소
SELECT MIN(<col>) FROM <table_name>
-- 최대
SELECT MAX(<col>) FROM <table_name>
```



### 정렬(order)

```sql
SELECT <col> FROM <table_name>
ORDER BY <col_1>, <col_2> [ASC | DESC]; -- 오름차순, 내림차순
```



### 제한(Limit)

```sql
SELECT <col> FROM <table_name>
LIMIT <num>
```



### 패턴(Pattern)

```sql
SELECT * FROM <table_name>
WHERE <col> LIKE '<pattern>'
```

<pattern>에 들어가는 말들

| 시작 | 예시    | 설명                                 |
| ---- | ------- | ------------------------------------ |
| `%`  | `2%`    | 2로 시작하는 값                      |
|      | `%2`    | 2로 끝나는 값                        |
|      | `%2%`   | 2가 들어가는 값                      |
| `_`  | `_2`    | 두번쨰 글자가 2 인 값                |
|      | `1___`  | 1로 시작하며 4자리                   |
|      | `_2%`   | 한글자 뒤에 2가오고 뒤에 이어지는 값 |
|      | `2_%_%` | 2로 시작하는데 최소 3자리인 값       |



### Article : Comments = 1 : n

| Column Name | DATATYPE |
| ----------- | -------- |
| Kisoo       | INTEGER  |
| REGION      | TEXT     |
| CLASS_NO    | INTEGER  |
| NAME        | TEXT     |
| AGE         | INTEGER  |
| MAJOR       | TEXT     |
| ACTIVATE    | INTEGER  |
| PHONE       | TEXT     |

REGION_TABLE

| ID   | REGION |
| ---- | ------ |
| 1    | 서울   |
| 2    | 대전   |
| 3    | 광주   |
| 4    | 구미   |



| ID   | REGION_ID | CLASS_NAME |
| ---- | --------- | ---------- |
| 1    | 1         | 1반        |
| 2    | 1         | 2반        |
| 3    | 1         | 3반        |

예제 ) 

로그인 하기

수강신청

