-- creating database
create database goodreads_db;

use goodreads_db;

-- creating books table
create table if not exists books (
    book_id int,
    title varchar(255),
    authors text,
    average_rating float,
    isbn varchar(20),
    isbn13 varchar(20),    
    language_code varchar(15),
    num_pages int,
    ratings_count int,
    text_reviews_count int,       
    publication_date date,
    publisher varchar(255)
    )
    
-- Data loaded using etl used over here

-- Q1: What is the highest reviewed book of all time?
select book_id, title, authors
from books 
order by text_reviews_count desc 
limit 1;

-- Q2: List all the non-english books
select book_id, title, authors
from books
where language_code not in ('eng', 'en-US', 'en-GB');

-- Q3: Group number of books per publisher
select publisher, count(*) as No_of_books
from books
group by publisher;

-- Q4: Highest rated book of 2001
select book_id, title, authors, text_reviews_count
from books
where year(publication_date) = 2001
order by text_reviews_count desc
limit 1;
-- sql is strict for date format so, different results than pandas

-- Q5: List english author with highest rated book (average_rating)
select book_id, title, authors
from books
where language_code in ('eng', 'en-US', 'en-GB')
order by average_rating desc
limit 1;

-- Q6: Which publisher has the highest rating count?
with highest_ratings as (
		select publisher, ratings_count,
			row_number() over (
			order by ratings_count desc
			) as row_num
		from books
		)

select publisher, ratings_count
from highest_ratings
where row_num = 1;

-- Q7: Which book is the most popular for each publisher? (ratings_count)
with highest_ratings as (
		select publisher, ratings_count,
			row_number() over (
            partition by publisher
			order by ratings_count desc
			) as row_num
		from books
		)

select publisher, ratings_count
from highest_ratings
where row_num = 1;

-- Q8: What are the average text reviews count for publisher?
select publisher, avg(text_reviews_count) as 'Average review count'
from books
group by publisher
order by publisher;

-- Q9: Get all Spanish books
select book_id, title, authors, publisher
from books
where language_code = 'spa';

-- Q10: Categorise based on average_rating
select book_id, title, authors,
		case
			when average_rating <= 3 then 'Not recomended'
            when average_rating <= 4 and average_rating > 3 then 'Okay'
            else 'Must read'
		end as Recommendation
from books;
