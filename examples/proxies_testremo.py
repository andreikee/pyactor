"""
Testing proxy comparison.
Run after proxies_test.py, concurrently.
"""
from pyactor.context import set_context, create_host, sleep, shutdown, Host


class Echo(object):
    _tell = {'echo'}

    def echo(self, msg):
        print(msg)


def main():
    set_context()
    host = create_host("http://127.0.0.1:12666")

    remote = host.lookup_url("http://127.0.0.1:12777", Host)
    print(remote)

    p1 = host.lookup_url("http://127.0.0.1:12777/1", Echo)
    p2 = remote.lookup('1')

    print("p1 =", id(p1))
    print("p2 =", id(p2))

    print(p1 == p2)
    print(p1 != p2)
    print(p1 is p2)

    s = set()
    s.add(p1)
    s.add(p2)
    print(len(s))

    print(p1)
    print(repr(p1))

    shutdown()


if __name__ == '__main__':
    main()
