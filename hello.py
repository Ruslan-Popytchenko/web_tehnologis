
def app(environ, start_responce):
    start_responce('200 OK', [('Content-Type', 'text/plain')])
    resp = environ['QUERY_STRING'].split("&")
    resp = [item + "\r\n" for item in resp]
    return resp
