create table books (
    bookID int primary key,
    title varchar(100),
    authors varchar(100),
    average_rating float,
    isbn float,
    isbn13 float,
    language_code varchar(20),
	num_pages int,
	ratings_count int,
	text_reviews_count int,
    publication_date date,
    publisher varchar(50)
);