from doktor_logging import logging

@doktor_logging
def test():
    """ 正常系 """
    print("Hello")


if __name__ == '__main__':
    test()
