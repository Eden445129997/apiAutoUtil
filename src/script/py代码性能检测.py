import cProfile

def loop(count):
    result = []
    for i in range(count):
        result.append(i)

'''
ncalls 执行次
tot time 总执行时间 排除子函数的执行时间
percall ：平均每次执行时间 tottime ／ncalls
cumtime 累计执行时间（包含子函数的执行时间）
percall ：平均每次执行时间 cumtime/ncalls ，递归调用只记一次）
filename:lineno(function)：具体执行内容说明，比如上面的哪行代码
'''

if __name__ == '__main__':
    cProfile.run('loop(10000)')

    print(33717+4606)