def fn1(a,b=1,f=3,*c,k,n,**l):
    print(c)
    print(l)
def count():
        fs = []
        for i in range(1, 4):
            def r(i):
                def f():
                    return i*i
                return  f
            fs.append(r(i))
        return fs
def test(fun):
    return fun


def decorator_a(func):
    print ('Get in decorator_a')
    def inner_a(*args, **kwargs):
        print ('Get in inner_a')
        return func(*args, **kwargs)
    return inner_a

def decorator_b(func):
    print ('Get in decorator_b')
    def inner_b(*args, **kwargs):
        print ('Get in inner_b')
        return func(*args, **kwargs)
    return inner_b

@decorator_b
@decorator_a
def f(x):
    print ('Get in f')
    return x * 2

if __name__ == '__main__':
    # fn1(1,6,4,3,7,n=4) # fn1() missing 1 required keyword-only argument: 'k'   k和n缺少一个都不行
    # fn1(1,6,4,3,7,k=5) # fn1() missing 1 required keyword-only argument: 'n'   k和n缺少一个都不行
    # fn1(1,6,4,3,7,k=5,n=4)  # c=(3,7) 并且  l={}
    # fn1(1,6,4,3,7,f=3,k=5,n=4)  #  fn1() got multiple values for argument 'f'   将字典作为参数传入时，字典中的key与函数参数列表命名发生重复
    # fn1(1,6,4,3,7,a=3,k=5,n=4) #  fn1() got multiple values for argument 'a'
    # fn1(1,6,4,3,7,k=5,n=4,g=3)  #通过
    # fn1(1,6,4,3,7,h=6,n=4,k=5,g=3) # c=(3,7) 并且  l={'h': 6, 'g': 3}
    # fn1(1,6,4,3,7,h=6,n=8,g=3)  #  fn1() missing 1 required keyword-only argument: 'k'
    # fn1(1,6,4,3,7,h=6,n=8,k=5,g=3)# c=(3,7) 并且  l={'h': 6, 'g': 3}
    # fn1(1,6,4,3,7,h=6,n=8,g=3,k=5)# c=(3,7) 并且  l={'h': 6, 'g': 3}
    # fn1(1,6,f=4,r=3,v=7,k=5,g=3)# fn1() missing 1 required keyword-only argument: 'n'
    # fn1(1,k=5,n=4)   ## c=() 并且  l={}
    # fn1(k=5,g=3,a=4,n=2)

    # f1, f2, f3 = count()
    # print(f1())
    # print(f2())
    # print(f3())

    print(test.__name__)