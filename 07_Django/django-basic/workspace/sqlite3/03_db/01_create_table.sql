CREATE TABLE "movies"(
    영화코드 INT PRIMARY KEY,
    영화이름 TEXT,
    관람등급 TEXT,
    감독 TEXT,    
    개봉연도 NUMBER, 
    누적관객수 INT, 
    상영시간 INT, 
    제작국가 TEXT, 
    장르 TEXT
);

.headers on
.mode csv

.import boxoffice.csv movies

select count(*) from movies;

