from db import *
from bottle import route, run, template, request, response


@route('/')
def index():
    return '''
        <form action="/shortify" method="post">
            URL to shorten: <input name="url" type="text" />
            <input value="Shorten" type="submit" />
        </form>
    '''


@route('/shortify', method='POST')
def shortify():
    url = request.forms.get('url')
    shortUrl = db.add_url(url)
    return template('<b>Short URL: {{scheme}}://{{host}}/{{shortUrl}}</b>', scheme=request.urlparts.scheme, host=request.urlparts.netloc, shortUrl=shortUrl)


@route('/<shortUrl>')
def redirect(shortUrl):
    url = db.get_url(shortUrl)
    print(url)
    response.status = 303
    response.set_header('Location', '{url}'.format(url=url))
    return response

if __name__ == '__main__':
    db = Database()
    db.create_table()
    run(host='0.0.0.0', port=8080)
