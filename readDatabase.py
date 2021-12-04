import sqlite3

invalid = {"message": "Invalid Format Received"}

def is_repeatd(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated

def read_halls(file='halls.txt'):
    halls = []
    file = open(file, 'r')
    lines = file.readlines()
    for line in lines:
        cls = line.split('\t', )
        try:
            cls[-1], a = cls[-1].split('\n')
            halls.append(cls)
        except ValueError:
            halls.append(cls)
    return halls


def check_halls(path):
    # try:
    halls = []
    file = open(path, 'r')
    lines = file.readlines()
    for line in lines:
        cls = line.split('\t', )
        try:
            cls[-1], a = cls[-1].split('\n')
            halls.append(cls)
        except ValueError:
            halls.append(cls)

    # for validation
    for hall in halls:
        a = hall[0].split(" ")
        b = hall[1].split(" ")
        if len(a)<=1:
            if (a[0].isdigit() and int(a[1]) >= 1) or len(halls)>1:
                pass
            else:
                return invalid
        else:
            if ((a[0].isdigit() or a[1].isdigit()) and int(a[1]) >= 1) and (
                    (b[0].isdigit() or b[1].isdigit()) and int(b[1]) >= 1):
                pass
            else:
                return invalid

    return halls

    # except:
    #     print("problem")
    #     return invalid


def get_classes(file='students.db'):
    try:
        conn = sqlite3.connect(file)
        stu = conn.cursor()
        get = "SELECT DISTINCT class FROM student ORDER BY rollno ASC "
        stu.execute(get)
        temp = stu.fetchall()
        print(temp)
        if len(temp) >=1:
            return temp
        else:
            return invalid
    except:
        return invalid


def read_classes(file=0):
    conn = sqlite3.connect('students.db')
    stu = conn.cursor()
    print("class File", file)
    file = open(file, 'r')
    lines = file.readlines()
    print(lines)
    classes = []
    for line in lines:
        cls = line.split('\n')
        get = ("SELECT rollno FROM student WHERE class=? ORDER BY rollno ASC ")
        stu.execute(get, [cls[0]])
        temp = stu.fetchall()
        siz = len(temp)
        clas = [cls[0], siz]
        classes.append(clas)
    return classes


def fetch_rollnos(classes):
    conn = sqlite3.connect('students.db')
    stu = conn.cursor()
    rollnos = []
    for cls in classes:
        get = ("SELECT rollno, class FROM student WHERE class=? ORDER BY rollno ASC ")
        stu.execute(get, [cls[0]])
        temp = stu.fetchall()
        for t in temp:
            rno = t[0], t[1]
            rollnos.append(rno)
    return rollnos


def devide_rollnos(rollnos, sizes):
    class_limit = 172
    # sizes = [sizes[0],sizes[1],sizes[2],sizes[3],]
    class_limit = sizes[0]
    r1, r2, r3, r4, r5, r6 = [], [], [], [], [], []

    start = 0
    end = start + class_limit
    # for1
    for i in range(start, end):
        r1.append(rollnos[i])
        start += 1



    class_limit = sizes[2]
    end = start + class_limit

    # for3
    for i in range(start, end):
        r3.append(rollnos[i])
        start += 1

    class_limit = sizes[1]
    end = start + class_limit

    # for2
    for i in range(start, end):
        r2.append(rollnos[i])
        start += 1
    class_limit = sizes[3]
    end = start + class_limit

    # for4
    for i in range(start, end):
        r4.append(rollnos[i])
        start += 1

    class_limit = sizes[4]
    end = start + class_limit

    # for5
    for i in range(start, end):
        r5.append(rollnos[i])
        start += 1

    class_limit = sizes[5]
    end = start + class_limit

    # for6
    r6 = []

    for i in range(start, end):
        try:
            r6.append(rollnos[i])
            start += 1
        except:
            pass

    i = 0
    out_nos = [r1, r2, r3, r4, r5, r6]

    file = open('test.txt', 'w')
    wr = str(r1), '\n', str(r2), '\n', str(r3), '\n', str(r4), '\n', str(r5), '\n', str(r6)
    file.writelines(wr)
    return out_nos
