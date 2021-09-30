import datetime
import sys


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform


def get_choose(go):
    result = ''
    for i in range(1,101):
        if i%2==0 and go:
            result += str(i) + ' '
        elif i%2!=0 and go==False:
            result += str(i) + ' '
    return result

def get_mistake():
    x = random.randint(1,30)
    y = random.randint(0,1)
    print(f"Trying operation {x}/{y}...")
    try:
        result = x/y
    except ZeroDivisionError:
        return 0
    else:
        return  1