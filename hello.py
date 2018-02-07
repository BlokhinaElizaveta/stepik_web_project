from urllib.parse import parse_qsl

def wsgi_application(environ, start_response):
    data = ''
    if environ['REQUEST_METHOD'] == 'GET':
        params = parse_qsl(environ['QUERY_STRING'])
        for item in params:
           data += '{}={}\n'.format(item[0], item[1])
    headers = [
        ('Content-Type','text/plain'),
        ('Content-Length', str(len(data)))]
    start_response('200 OK', headers)
    return [data.encode('utf-8')]