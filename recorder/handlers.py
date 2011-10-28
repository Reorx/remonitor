with open('/var/log/nginx/access.log.1', 'r') as f:
    for n, line in enumerate(f):
        if 5 > n:
            print line
        else:
            break
