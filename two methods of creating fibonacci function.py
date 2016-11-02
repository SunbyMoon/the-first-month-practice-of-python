#!/usr/bin/python

def fibo(n):
    if n <=1:
        return n
    else:
        return (fibo(n-1) + fibo(n-2))
    
if __name__ == '__main__':
    for i in range(10):
        print fibo(i) 

	
#!/usr/bin/python

def fibs(n):
    result=[0,1]
    for i in range(n-2):
        result.append(result[-2] + result[-1])
    return result
if __name__ == '__main__':
    print fibs(10)
