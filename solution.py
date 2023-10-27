import json
import csv

def update_users(file):
    res = []
    with open(file) as users:
        templates = json.load(users)
    for temp in templates:
        newitem = [temp['name'], temp['gender'], temp['address'], temp['age']]
        res.append(newitem)
    return res

def update_books(file):
    books = []
    with open(file, 'r') as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            newbook = {'title': row[0], 'author': row[1], 'pages': row[3], 'genre': row[2]}
            books.append(newbook)
    return books

def make_json(users, books, file):
    m_books, extra_books = len(books) // len(users), len(books) % len(users)
    to_json = []
    i_b = 0

    for user in users:
        new_user = {'name': user[0], 'gender': user[1], 'address': user[2], 'age': user[3], 'books': []}
        for i in range(i_b, i_b + m_books):
            new_user['books'].append(books[i])
        i_b += m_books
        if extra_books != 0:
            new_user['books'].append(books[i_b])
            extra_books -= 1
            i_b += 1
        to_json.append(new_user)
    with open(file, 'w') as f:
        json.dump(to_json, f, indent = 2)

users_file = 'users.json'
books_file = 'books.csv'
users = update_users(users_file)
books = update_books(books_file)
make_json(users, books, 'books_n_users.json')



