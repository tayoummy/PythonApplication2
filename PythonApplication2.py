a = input("�������� ��������: +, -, /, *, ^, k�����, f, sin, cos, tg  ")
if a == '+':
        b = float(input('b ='))
        c = float(input('c ='))
        print(b + c)
elif a == '-':
        b1 = float(input('b1 ='))
        c1 = float(input('c1 ='))
        print(b1 - c1)
elif a == '/':
        b2 = float(input('b2 ='))
        c2 = float(input('c2 ='))
        print(b2 / c2)
elif a == '*':
        b3 = float(input('b3 ='))
        c3 = float(input('c3 ='))
        print(b3 * c3)
elif a == '^':
        b4 = float(input('b4 ='))
        c4 = float(input('c4 ='))
        print(b4 ** c4)
elif a == '������':
        b5 = float(input('b5 ='))
        l = b5 ** 0.5
        print(l)
elif a == 'f':
        x = int(input('x ='))
        y = 1
        while x > 1 :
            y = y * x
            x = x -1
        print(y)
elif a =='sin':
        h = int(input(' ������� �������� ��������������� ������:'))
        e = int(input(' ������� �������� ����������:'))
        print(h / e)
elif a =='cos':
        g = int(input('������� �������� ����������� ������:'))
        r = int(input('������� �������� ����������:'))
        print(g / r)
elif a == 'tg':
        k = int(input('������� �������������� �����:'))
        u = int(input('������� ���������� �����:'))
        print(k / u)