def wsgi_application(environ, start_response):
    # бизнес-логика
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    body =''
    for line in environ["QUERY_STRING"].split("&"):
        body = body + line + '\n'

    start_response(status, headers)
    return [body]
