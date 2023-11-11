import sqlite3
from hashlib import sha256
from urllib.parse import urlparse
from random import randint

class Database:
    def __init__(self):
        self.con = sqlite3.connect('urls.db')
        self.cur = self.con.cursor()

    def create_table(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS urls (shortUrl TEXT, longUrl TEXT)')

    def add_url(self, url):
        parsed_url = urlparse(url, scheme="https").geturl()
        hashed_url = sha256(str.encode(parsed_url+str(randint(0,9999)))).hexdigest()
        linked_url = (hashed_url[:5], parsed_url)
        self.cur.execute('INSERT INTO urls VALUES (?, ?)', linked_url)
        self.con.commit()
        return hashed_url[:5]

    def get_url(self, shortUrl):
        self.cur.execute('SELECT longUrl FROM urls WHERE shortUrl = ?', (shortUrl,))
        return self.cur.fetchone()[0]
