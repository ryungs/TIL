--1. users 에서 age 가 30 이상인 사람?
SELECT * FROM users WHERE age >= 30;

--2. users 에서 age 가 30 이상인 사람의 이름만
SELECT first_name FROM users WHERE age >= 30;

--3. users 에서 age 가 30 이상이고 성이 '김'씨인 사람의 성과 나이만,
SELECT last_name FROM users WHERE age >= 30 and last_name="김";

--4. 