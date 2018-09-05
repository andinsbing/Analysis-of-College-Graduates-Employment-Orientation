from redis import Redis


def get_task_urls(txt_path):
    f = open(txt_path)
    for url in f.readlines():
        url = url.strip()
        # this different
        yield url[1:-2]
    f.close()
    print('closed')


def push_redis_tasks(urls):
    r = Redis(host='47.100.11.75', port=6388, db=0, password='password')
    for url in urls:
        r.rpush('type_queue', url)
        # r.sadd('type_set',url)


if __name__ == '__main__':
    push_redis_tasks(get_task_urls('target.txt'))
