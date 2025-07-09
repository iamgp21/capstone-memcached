from pymemcache.client.base import Client


def main():
    client = Client(('127.0.0.1', 11211))
    client.set('Environment', 'wsl2', expire=60) ## expire is in seconds
    client.set('database', 'memcached', expire=60) ## expire is in seconds
    result = client.get_many(['Environment', 'database'])
    #print(type(result))
    #print(result)
    for key, value in result.items():
        if key is None or value is None:
            continue
        else:
            print(f"Key: {key}", end="\n")
            print(f"Value: {str(value.decode('utf-8'))}", end="\n")
    #client.flush_all()
    client.close()

if __name__ == "__main__":
    main()
