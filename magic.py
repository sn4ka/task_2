try:
    n=int(input('Размер матрицы\n'))
    if 4<=n<=1000:
        num=1
        i,u=0,0
        s=n
        end=n**2
        matrix=[[0]*n for x in range(n)]
        while (num<=end):
            for u in range(u,n):
                    matrix[i][u]=num
                    num+=1
            for i in range (i+1,n):
                    matrix[i][u]=num
                    num+=1
            for u in range (u-1,s-n-1,-1):
                    matrix[i][u]=num
                    num+=1
            for i in range (i-1, s-n, -1):
                    matrix[i][u]=num
                    num+=1
            n-=1
            u+=1
        for row in range(0,s):
            for column in range (0,s):
                print (f'{matrix[row][column]:<3} ', end='')
            print()
    else:
        print('Число не входит в диапазон от 4 до 1000')
except SyntaxError:
        print('Ошибка синтаксиса')
except ValueError:
    print ('Введите целое число')
