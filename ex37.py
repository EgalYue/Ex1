# try:
#     a=1
#     b=c
# except Exception,e:
#     print Exception,":",e
#
#

def func1():
    try:
        print 'in func1 try: try statement, will return 1'
        return 1
    finally:
        print 'in func1 finally: try statement, will return 2'
        return 2


def func2():
    try:
        print 'in func2 try: raise error'
        raise ValueError()
    except:
        print 'in func2 except: caught error, will return 1!'
        return 1
    finally:
        print 'in func2 finally: will return 3'
        return 3


print func1()
print func2()