# Sample REST WebApp using Tornado framework
from tornado.ioloop import IOLoop
import sqlite3 as sqlite
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello World!')


class CarHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('GET - Welcome to the CarHandler!')

    def post(self):
        self.write('POST - Welcome to the CarHandler!')


def verify_database():
    conn = sqlite.connect('cars.db')
    c = conn.cursor()
    try:
        c.execute('SELECT * FROM cars')
        print('Table already exists')
    except:
        print('Creating table \'cars\'')
        c.execute('CREATE TABLE cars (\
            id text,\
            make text,\
            model text,\
            year text,\
            trans text,\
            color text)')
        print('Successfully created table \'cars\'')
    conn.commit()
    conn.close()


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
                (r"/?", MainHandler),
                (r"/api/v1/cars/?", CarHandler),
                (r"/api/v1/cars/[0-9][0-9][0-9][0-9]/?", CarHandler)
        ]
        tornado.web.Application.__init__(self, handlers)


def main():
    verify_database()
    app = Application()
    app.listen(8888)
    IOLoop.current().start()


if __name__ == '__main__':
    main()