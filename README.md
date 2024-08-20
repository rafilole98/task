# task
-- create database task ;\
-- use task;\
-- 1 Step ONE Create Tables \
CREATE TABLE Person (
    person_id INT PRIMARY KEY,
    first_name varchar(150),
    last_name varchar(150),
    address varchar(150),
    mobile varchar(15) UNIQUE
    ); \
 CREATE TABLE Job (
    job_id INT PRIMARY KEY,
    title_ar VARCHAR(150),
    title_en VARCHAR(150),
    min_salary DECIMAL(10, 2)
); \

  CREATE TABLE PersonJobDetail (
    jobdetail_id INT PRIMARY KEY,
    person_id INT,
    job_id INT,
    salary DECIMAL(10, 2),
    years_of_experience INT unsigned,
    FOREIGN KEY (person_id) REFERENCES Person(person_id),
    FOREIGN KEY (job_id) REFERENCES Job(job_id)
); \
 
 
 -- 2 INSERT DATA \
 
INSERT INTO Person  (person_id, first_name, last_name, address, mobile) VALUES (1,'mark','miller','usa','+1587681247');\
INSERT INTO Person  (person_id, first_name, last_name, address, mobile) VALUES (2,'karim','karm','syria','+963947254368');\
INSERT INTO Person  (person_id, first_name, last_name, address, mobile) VALUES (3,'maria','hanna','syria','+963947254361');\



INSERT INTO Job (job_id,title_ar,title_en,min_salary) VALUES (1,'مهندس مدني','civil eng',5000.00);\
INSERT INTO Job (job_id,title_ar,title_en,min_salary) VALUES (2,'مهندس تقني','tech eng',4500.00);\
INSERT INTO Job (job_id,title_ar,title_en,min_salary) VALUES (3,'حلاقة رجالية','Barber',2500.00);\
INSERT INTO Job (job_id,title_ar,title_en,min_salary) VALUES (4,'فني كهرباء','Electrician',2800.00);\
INSERT INTO Job (job_id,title_ar,title_en,min_salary) VALUES (5,'خياطة','sewing',1500.00);\


INSERT INTO PersonJobDetail (jobdetail_id,salary,years_of_experience,job_id,person_id) VALUES (1,6500.00,5,2,1); \
INSERT INTO PersonJobDetail (jobdetail_id,salary,years_of_experience,job_id,person_id) VALUES (2,1700.00,2,3,1); \
INSERT INTO PersonJobDetail (jobdetail_id,salary,years_of_experience,job_id,person_id) VALUES (3,4500.00,2,1,2); \
INSERT INTO PersonJobDetail (jobdetail_id,salary,years_of_experience,job_id,person_id) VALUES (4,2000.00,4,4,2); \
INSERT INTO PersonJobDetail (jobdetail_id,salary,years_of_experience,job_id,person_id) VALUES (5,1200.00,3,5,3); \
INSERT INTO PersonJobDetail (jobdetail_id,salary,years_of_experience,job_id,person_id) VALUES (6,5000.00,6,1,3); \



-- 3 Show Persons who are working with salaries are more than the min_salary

SELECT Person.first_name, Person.last_name, Job.title_en,Job.title_ar, PersonJobDetail.salary
FROM Person 
JOIN PersonJobDetail  ON Person.person_id = PersonJobDetail.person_id
JOIN Job  ON PersonJobDetail.job_id = Job.job_id
WHERE PersonJobDetail.salary > Job.min_salary;


-- 4 

SELECT Job.title_en AS JobTitle, COUNT(*) AS NumberOfEmployees, GROUP_CONCAT(Person.first_name, ' ', Person.last_name) AS EmployeeNames
FROM PersonJobDetail 
JOIN Job  ON PersonJobDetail.job_id = Job.job_id
JOIN Person  ON PersonJobDetail.person_id = Person.person_id
GROUP BY Job.title_en;
