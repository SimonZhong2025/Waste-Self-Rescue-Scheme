#coding:utf-8
class FError(Exception):
    print('异常')
try:
    raise FError('自定义异常')
except FError as e:
    print(e)
    raise   