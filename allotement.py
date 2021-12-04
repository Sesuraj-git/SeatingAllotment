r1, r2, r3, r4, r5, r6 = [], [], [], [], [], []
ind1, ind2, ind3, ind4, ind5, ind6 = 0, 0, 0, 0, 0, 0
global outfile, stu_count, even_addup, odd_addup
global one, two, three, four, five, six


def odd_write(hall, loop, addups):
    global one, two, three, four, five, six
    global ind1, ind2, ind3

    # no : 1
    if int(hall[2]) >= 1:
        addup = loop
        if len(r1) > ind1 + addup:

            try:
                write = ',' + str(r1[ind1 + addup][0])
                stu_count.append(r1[ind1 + addup])
            except IndexError:
                write = ',,' + ','

            outfile.write(write)
            one += 1
        else:
            outfile.write(',')

# no : 4
    if int(hall[2]) >= 2:
        if len(r2) > ind2 + addup:

            try:
                write = ',' + str(r2[ind2 + addup][0])
                stu_count.append(r2[ind2 + addup])
            except IndexError:
                write = ',,' + ','

            outfile.write(write)
            two += 1
        else:
            outfile.write(',')

# no : 2
    if int(hall[2]) >= 3:
        if len(r3) > ind3 + addup:

            try:
                write = ',' + str(r3[ind3 + addup][0])
                stu_count.append(r3[ind3 + addup])
            except IndexError:
                write = ',,' + ','

            outfile.write(write)
            three += 1
        else:
            outfile.write(',')

# no : 1
    if int(hall[2]) >= 4:
        addup = loop + addups
        if len(r1) > ind1 + addup:

            try:
                write = ',,' + str(r1[ind1 + addup][0])
                stu_count.append(r1[ind1 + addup])
            except IndexError:
                write = ',,' + ','

            outfile.write(write)
            one += 1
        else:
            outfile.write(',')

# no : 4
    if int(hall[2]) >= 5:
        if len(r2) > ind2 + addup:

            try:
                write = ',' + str(r2[ind2 + addup][0])
                stu_count.append(r2[ind2 + addup])
            except IndexError:
                write = ',,' + ','

            outfile.write(write)
            two += 1
        else:
            outfile.write(',')

# no : 2
    if int(hall[2]) >= 6:
        if len(r3) > ind3 + addup:

            try:
                write = ',' + str(r3[ind3 + addup][0])
                stu_count.append(r3[ind3 + addup])
            except IndexError:
                write = ',,' + ','

            outfile.write(write)
            three += 1
        else:
            outfile.write(',')

# no : 1
    if int(hall[2]) >= 7:
        addup = loop + addups + addups
        if len(r1) > ind1 + addup:

            try:
                write = ',,' + str(r1[ind1 + addup][0])
                stu_count.append(r1[ind1 + addup])
            except IndexError:
                write = ',,' + ','

            outfile.write(write)
            one += 1
        else:
            outfile.write(',')

# no : 4
    if int(hall[2]) >= 8:
        if len(r2) > ind2 + addup:

            try:
                write = ',' + str(r2[ind2 + addup][0])
                stu_count.append(r2[ind2 + addup])
            except IndexError:
                write = ',,' + ','

            outfile.write(write)
            two += 1
        else:
            outfile.write(',')

# no : 2
    if int(hall[2]) >= 9:
        if len(r3) > ind3 + addup:

            try:
                write = ',' + str(r3[ind3 + addup][0])
                stu_count.append(r3[ind3 + addup])
            except IndexError:
                write = ',,' + ','

            outfile.write(write)
            three += 1
        else:
            outfile.write(',')
    outfile.write('\n')


def even_write(hall, loop, addups):
    global one, two, three, four, five, six
    global ind4, ind5, ind6
    print(loop, addups)
    
# no :3
    # c = input()
    if int(hall[2]) >= 1:
        addup = loop
        if len(r4) > ind4 + addup:

            try:
                write = ',' + str(r4[ind4 + addup][0])
                stu_count.append(r4[ind4 + addup])
            except IndexError:
                write = ',,' + ','

            outfile.write(write)
            four += 1
        else:
            outfile.write(',')

# no : 6
    if int(hall[2]) >= 2:
        if len(r5) > ind5 + addup:

            try:
                write = ',' + str(r5[ind5 + addup][0])
                stu_count.append(r5[ind5 + addup])
            except IndexError:
                write = ',,' + ','

            outfile.write(write)
            five += 1
        else:
            outfile.write(',')

# no : 5
    if int(hall[2]) >= 3:
        if len(r6) > ind6 + addup:

            try:
                write = ',' + str(r6[ind6 + addup][0])
                stu_count.append(r6[ind6 + addup])
            except IndexError:
                write = ',,' + ','

            outfile.write(write)
            six += 1
        else:
            outfile.write(',')

# no : 
    if int(hall[2]) >= 4:
        addup = loop + addups
        if len(r4) > ind4 + addup:

            try:
                write = ',,' + str(r4[ind4 + addup][0])
                stu_count.append(r4[ind4 + addup])
            except IndexError:
                write = ',,' + ','

            outfile.write(write)
            four += 1
        else:
            outfile.write(',')

# no : 
    if int(hall[2]) >= 5:
        global ind2
        if len(r5) > ind5 + addup:

            try:
                write = ',' + str(r5[ind5 + addup][0])
                stu_count.append(r5[ind5 + addup])
            except IndexError:
                write = ',,' + ','

            outfile.write(write)
            five += 1
        else:
            outfile.write(',')

# no : 
    if int(hall[2]) >= 6:
        if len(r6) > ind6 + addup:

            try:
                write = ',' + str(r6[ind6 + addup][0])
                stu_count.append(r6[ind6 + addup])
            except IndexError:
                write = ',,' + ','

            outfile.write(write)
            six += 1
        else:
            outfile.write(',')

# no : 
    if int(hall[2]) >= 7:
        addup = loop + addups + addups
        if len(r4) > ind4 + addup:

            try:
                write = ',,' + str(r4[ind4 + addup][0])
                stu_count.append(r4[ind4 + addup])
            except IndexError:
                write = ',,' + ','

            outfile.write(write)
            four += 1
        else:
            outfile.write(',')

# no : 
    if int(hall[2]) >= 8:
        if len(r5) > ind5 + addup:

            try:
                write = ',' + str(r5[ind5 + addup][0])
                stu_count.append(r5[ind5 + addup])
            except IndexError:
                write = ',,' + ','

            outfile.write(write)
            five += 1
        else:
            outfile.write(',')

# no : 
    if int(hall[2]) >= 9:
        if len(r6) > ind6 + addup:

            try:
                write = ',' + str(r6[ind6 + addup][0])
                stu_count.append(r6[ind6 + addup])
            except IndexError:
                write = ',,' + ','

            outfile.write(write)
            six += 1
        else:
            outfile.write(',')
    outfile.write('\n')


def arrange_column(row_count, col_count):
    global odd_addup, even_addup
    col_count = int(col_count)
    row_count = int(row_count)
    print(row_count, "R \nC", col_count)
    # c = input()
    even_addup = int(col_count * 0.5)
    if col_count % 2 == 1:
        odd_addup = even_addup + 1
    else:
        odd_addup = even_addup
    print(even_addup, odd_addup)


def colls_3(hall):
    try:
        write = ',,,,', hall[0], '\n'
    except IndexError:
        write = ',,' + ','
    outfile.writelines(write)
    i = 0
    j = 0
    arrange_column(hall[2], hall[1])
    # for i in range(0, int(hall[1])):
    while True:

        if i == int(hall[1]):
            return
        else:

            print("j ", j, "i", i)
            odd_write(hall, j, odd_addup)
            i += 1
        #     cover here
        if i == int(hall[1]):
            return
        else:

            even_write(hall, j, even_addup)
            i += 1
        j = j + 1


def stud_count(stu_count, coll):
    # print(stu_count)
    classes = []
    unique = {}
    write = ",,,,Students Count : \n"
    outfile.writelines(write)
    for stu in stu_count:
        classes.append(stu[1])
    if len(classes) > 1:
        classes.sort()

        for clas in classes:
            if clas not in unique:
                unique[clas] = 1
            else:
                unique[clas] = unique[clas] + 1
    u = []
    for uni in unique:
        ev = str(',' * int(coll)), str(uni), ',', str(unique[uni]), "\n"
        outfile.writelines(ev)
        u.append(ev)

    outfile.write("\n\n")
    print(u, len(u))


def main_call(halls, rollnos, outFileLoc):
    global outfile, stu_count
    global ind1, ind2, ind3, ind4, ind5, ind6
    loc = str(outFileLoc) + '/outfile.csv'
    outfile = open(loc, 'w')

    global r1
    r1 = rollnos[0]
    global r2
    r2 = rollnos[1]
    global r3
    r3 = rollnos[2]
    global r4
    r4 = rollnos[3]
    global r5
    r5 = rollnos[4]
    global r6
    r6 = rollnos[5]

    for hall in halls:
        global one, two, three, four, five, six
        one, two, three, four, five, six = 0, 0, 0, 0, 0, 0
        stu_count = []
        colls_3(hall)
        stud_count(stu_count, hall[2])
        ind1, ind2, ind3, ind4, ind5, ind6 = ind1+one, ind2+two, ind3+three, ind4+four, ind5+five, ind6+six

    outfile.close()
