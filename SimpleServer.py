import json
import tornado.ioloop
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
#https://stackoverflow.com/questions/35254742/tornado-server-enable-cors-requests

    def set_default_headers(self):
        print("Setting headers.")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def post(self):
        print("POST operation.")
        self.write('whatever')

    def get(self):
        print("GET operation.")
        j = open('response.json').read()
        self.write(j)
        #print('Sent: {}'.format(j))

    def options(self):
        # no body
        self.set_status(204)
        self.finish()

class SimpleServer(tornado.web.Application):

    def __init__(self):

        super().__init__([
            (r'/json', BaseHandler)
            ])

def main():
    print('Server started.')
    server = SimpleServer()
    server.listen(8888, xheaders = True)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()

