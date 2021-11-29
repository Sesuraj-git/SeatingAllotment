r1, r2, r3, r4, r5, r6 = [], [], [], [], [], []
ind1, ind2, ind3, ind4, ind5, ind6 = 0, 0, 0, 0, 0, 0
global outfile, stu_count


def odd_write(hall):
    global ind1, ind2, ind3
    if int(hall[2]) >= 1:
        if len(r1) > ind1:

            write = ',' + str(r1[ind1][0])
            stu_count.append(r1[ind1])
            outfile.write(write)
            ind1 += 1
        else:
            outfile.write(',')

    if int(hall[2]) >= 2:
        if len(r2) > ind2:
            write = ',' + str(r2[ind2][0])
            stu_count.append(r2[ind2])
            outfile.write(write)
            ind2 += 1
        else:
            outfile.write(',')

    if int(hall[2]) >= 3:
        if len(r3) > ind3:
            write = ',' + str(r3[ind3][0])
            stu_count.append(r3[ind3])
            outfile.write(write)
            ind3 += 1
        else:
            outfile.write(',')

    if int(hall[2]) >= 4:
        if len(r1) > ind1:
            write = ',,' + str(r1[ind1][0])
            stu_count.append(r1[ind1])
            outfile.write(write)
            ind1 += 1
        else:
            outfile.write(',')

    if int(hall[2]) >= 5:
        if len(r2) > ind2:
            write = ',' + str(r2[ind2][0])
            stu_count.append(r2[ind2])
            outfile.write(write)
            ind2 += 1
        else:
            outfile.write(',')

    if int(hall[2]) >= 6:
        if len(r3) > ind3:
            write = ',' + str(r3[ind3][0])
            stu_count.append(r3[ind3])
            outfile.write(write)
            ind3 += 1
        else:
            outfile.write(',')

    if int(hall[2]) >= 7:
        if len(r1) > ind1:
            write = ',,' + str(r1[ind1][0])
            stu_count.append(r1[ind1])
            outfile.write(write)
            ind1 += 1
        else:
            outfile.write(',')

    if int(hall[2]) >= 8:
        if len(r2) > ind2:
            write = ',' + str(r2[ind2][0])
            stu_count.append(r2[ind2])
            outfile.write(write)
            ind2 += 1
        else:
            outfile.write(',')

    if int(hall[2]) >= 9:
        if len(r3) > ind3:
            write = ',' + str(r3[ind3][0])
            stu_count.append(r3[ind3])
            outfile.write(write)
            ind3 += 1
        else:
            outfile.write(',')
    outfile.write('\n')


def even_write(hall):
    global ind4, ind5, ind6
    if int(hall[2]) >= 1:
        if len(r4) > ind4:

            write = ',' + str(r4[ind4][0])
            stu_count.append(r4[ind4])
            outfile.write(write)
            ind4 += 1
        else:
            outfile.write(',')

    if int(hall[2]) >= 2:
        if len(r5) > ind5:
            write = ',' + str(r5[ind5][0])
            stu_count.append(r5[ind5])
            outfile.write(write)
            ind5 += 1
        else:
            outfile.write(',')

    if int(hall[2]) >= 3:
        if len(r6) > ind6:
            write = ',' + str(r6[ind6][0])
            stu_count.append(r6[ind6])
            outfile.write(write)
            ind6 += 1
        else:
            outfile.write(',')

    if int(hall[2]) >= 4:
        if len(r4) > ind4:
            write = ',,' + str(r4[ind4][0])
            stu_count.append(r4[ind4])
            outfile.write(write)
            ind4 += 1
        else:
            outfile.write(',')

    if int(hall[2]) >= 5:
        global ind2
        if len(r5) > ind5:
            write = ',' + str(r5[ind5][0])
            stu_count.append(r5[ind5])
            outfile.write(write)
            ind5 += 1
        else:
            outfile.write(',')

    if int(hall[2]) >= 6:
        if len(r6) > ind6:
            write = ',' + str(r6[ind6][0])
            stu_count.append(r6[ind6])
            outfile.write(write)
            ind6 += 1
        else:
            outfile.write(',')

    if int(hall[2]) >= 7:
        if len(r4) > ind4:
            write = ',,' + str(r4[ind4][0])
            stu_count.append(r4[ind4])
            outfile.write(write)
            ind4 += 1
        else:
            outfile.write(',')

    if int(hall[2]) >= 8:
        if len(r5) > ind5:
            write = ',' + str(r5[ind5][0])
            stu_count.append(r5[ind5])
            outfile.write(write)
            ind5 += 1
        else:
            outfile.write(',')

    if int(hall[2]) >= 9:
        if len(r6) > ind6:
            write = ',' + str(r6[ind6][0])
            stu_count.append(r6[ind6])
            outfile.write(write)
            ind6 += 1
        else:
            outfile.write(',')
    outfile.write('\n')


def colls_3(hall):
    write = ',' * int(float(hall[2]) * 0.5), hall[0], '\n'
    outfile.writelines(write)
    i = 0
    # for i in range(0, int(hall[1])):
    while True:
        if i == int(hall[1]):
            return
        else:
            odd_write(hall)
            i += 1
        if i == int(hall[1]):
            return
        else:
            even_write(hall)
            i += 1


def stud_count(stu_count, coll):
    # print(stu_count)
    classes = []
    unique = {}
    write = str(',' * (int(coll)-1)), "Students Count : \n"
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
        stu_count = []
        colls_3(hall)
        stud_count(stu_count, hall[2])
