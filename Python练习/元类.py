#!/usr/bin/env python3
# -*- coding:utf-8 -*-
def echo_bar(self):
    print('each_bar')
FooChild = type('FooChild', (), {'echo_bar': echo_bar,'a':1})
print(hasattr(FooChild, 'echo_bar'))
my_foo = FooChild()
print(my_foo.echo_bar())
print(my_foo.a)
print(FooChild.__class__)
print(my_foo.__class__)