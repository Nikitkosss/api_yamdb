import csv
import sqlite3

connection = sqlite3.connect('db.sqlite3')

cursor = connection.cursor()

file_category = open('static/data/category.csv')
file_comments = open('static/data/comments.csv')
file_genre_title = open('static/data/genre_title.csv')
file_genre = open('static/data/genre.csv')
file_review = open('static/data/review.csv')
file_titles = open('static/data/titles.csv')
file_users = open('static/data/users.csv')

contents = csv.reader(file_category)
contents1 = csv.reader(file_comments)
contents2 = csv.reader(file_genre_title)
contents3 = csv.reader(file_genre)
contents4 = csv.reader(file_review)
contents5 = csv.reader(file_titles)

insert_records = """ INSERT INTO
                    reviews_сategory (id, slug, name)
                    VALUES(?, ?, ?) """
insert_records1 = """ INSERT INTO reviews_comment
                    (id,review_id,text,author_id,pub_date)
                    VALUES(?, ?, ?, ?, ?) """
insert_records2 = """ INSERT INTO reviews_title_genre
                    (id, title_id, genre_id)
                    VALUES(?, ?, ?) """
insert_records3 = """ INSERT INTO reviews_genre
                    (id, name, slug)
                    VALUES(?, ?, ?) """
insert_records4 = """ INSERT INTO reviews_review
                    (id, title_id, text, author_id, score, pub_date)
                    VALUES(?, ?, ?, ?, ?, ?) """
insert_records5 = """ INSERT INTO reviews_title
                    (id, name, year, category_id)
                    VALUES(?, ?, ?, ?) """

cursor.executemany(insert_records, contents)
cursor.executemany(insert_records1, contents1)
cursor.executemany(insert_records2, contents2)
cursor.executemany(insert_records3, contents3)
cursor.executemany(insert_records4, contents4)
cursor.executemany(insert_records5, contents5)

select_all = "SELECT * FROM reviews_сategory"
select_all1 = "SELECT * FROM reviews_comment"
select_all2 = "SELECT * FROM reviews_title_genre"
select_all3 = "SELECT * FROM reviews_genre"
select_all4 = "SELECT * FROM reviews_review"
select_all5 = "SELECT * FROM reviews_title"

rows = cursor.execute(select_all).fetchall()
rows1 = cursor.execute(select_all1).fetchall()
rows2 = cursor.execute(select_all2).fetchall()
rows3 = cursor.execute(select_all3).fetchall()
rows4 = cursor.execute(select_all4).fetchall()
rows5 = cursor.execute(select_all5).fetchall()

connection.commit()

connection.close()
