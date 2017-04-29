import csv
import datetime
from db_classes import db_session, Place, User, Book


def load_data_from_csv(csv_filepath, db_class, do_commit=False, fields=[]):
    with open(csv_filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, fields, delimiter=',')
        for row in reader:
            db_session.add(db_class(**row))
    if do_commit:
        db_session.commit()


def load_users_from_csv(csv_filepath, do_commit=False):
    load_data_from_csv(
        csv_filepath=csv_filepath,
        do_commit=do_commit,
        fields=['name', 'email', 'image'],
        db_class=User
    )


def load_places_from_csv(csv_filepath, do_commit=False):
    load_data_from_csv(
        csv_filepath=csv_filepath,
        do_commit=do_commit,
        fields=['name', 'address', 'latitude', 'longitude', 'description'],
        db_class=Place
    )

def load_books_from_csv(csv_filepath, do_commit=False):
    with open('booklist.csv', 'r', encoding='utf-8') as f:
        fields = ['booked_at', 'user_id', 'place_id']
        reader = csv.DictReader(f, fields, delimiter=',')
        for row in reader:
            row['booked_at'] = datetime.datetime.strptime(row['booked_at'], '%d.%m.%Y')
            row['place_id'] = Place.query.filter(Place.name == row['place_id']).first().id
            row['user_id'] = User.query.filter(User.email == row['user_id']).first().id
            db_session.add(Book(**row))
    if do_commit:
        db_session.commit()


def load_data_from_all_csv():
    load_users_from_csv(csv_filepath='userlist.csv', do_commit=True)
    load_places_from_csv(csv_filepath='placelist.csv', do_commit=True)
    load_books_from_csv(csv_filepath='booklist.csv', do_commit=True)


if __name__ == '__main__':
    load_data_from_all_csv()
