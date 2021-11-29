rollnos = []
total_size = 0
ind1, ind2, ind3, ind4, ind5, ind6 = 0, 0, 0, 0, 0, 0
# outfile = open('outfile.csv', 'w')
total_flag = True


def odd_write(hall):
    global ind1, ind2, ind3, total_flag
    
    
    if int(hall[2]) >= 1:
        total = ind1 + ind2 + ind3 + ind4 + ind5 + ind6
        if total <= total_size:
            
            ind1 += 1
        else:
            total_flag = True
            return

    if int(hall[2]) >= 2:
        total = ind1 + ind2 + ind3 + ind4 + ind5 + ind6
        if total <= total_size:
            
            ind2 += 1
        else:
            total_flag = True
            return

    if int(hall[2]) >= 3:
        total = ind1 + ind2 + ind3 + ind4 + ind5 + ind6
        if total <= total_size:
            
            ind3 += 1
        else:
            total_flag = True
            return

    if int(hall[2]) >= 4:
        total = ind1 + ind2 + ind3 + ind4 + ind5 + ind6
        if total <= total_size:
            
            ind1 += 1
        else:
            total_flag = True
            return

    if int(hall[2]) >= 5:
        total = ind1 + ind2 + ind3 + ind4 + ind5 + ind6
        if total <= total_size:
            
            ind2 += 1
        else:
            total_flag = True
            return

    if int(hall[2]) >= 6:
        total = ind1 + ind2 + ind3 + ind4 + ind5 + ind6
        if total <= total_size:
            
            ind3 += 1
        else:
            total_flag = True
            return

    if int(hall[2]) >= 7:
        total = ind1 + ind2 + ind3 + ind4 + ind5 + ind6
        if total <= total_size:
            
            ind1 += 1
        else:
            total_flag = True
            return

    if int(hall[2]) >= 8:
        total = ind1 + ind2 + ind3 + ind4 + ind5 + ind6
        if total <= total_size:
            
            ind2 += 1
        else:
            total_flag = True
            return

    if int(hall[2]) >= 9:
        total = ind1 + ind2 + ind3 + ind4 + ind5 + ind6
        if total <= total_size:
            
            ind3 += 1
        else:
            total_flag = True
            return


def even_write(hall):
    global ind4, ind5, ind6, total_flag
    
    if int(hall[2]) >= 1:
        total = ind1 + ind2 + ind3 + ind4 + ind5 + ind6
        if total <= total_size:
            
            ind4 += 1
        else:
            total_flag = True
            return

    if int(hall[2]) >= 2:
        total = ind1 + ind2 + ind3 + ind4 + ind5 + ind6
        if total <= total_size:
            
            ind5 += 1
        else:
            total_flag = True
            return

    if int(hall[2]) >= 3:
        total = ind1 + ind2 + ind3 + ind4 + ind5 + ind6
        if total <= total_size:
            
            ind6 += 1
        else:
            total_flag = True
            return

    if int(hall[2]) >= 4:
        total = ind1 + ind2 + ind3 + ind4 + ind5 + ind6
        if total <= total_size:
            
            ind4 += 1
        else:
            total_flag = True
            return

    if int(hall[2]) >= 5:
        total = ind1 + ind2 + ind3 + ind4 + ind5 + ind6
        if total <= total_size:
            
            ind5 += 1
        else:
            total_flag = True
            return

    if int(hall[2]) >= 6:
        total = ind1 + ind2 + ind3 + ind4 + ind5 + ind6
        if total <= total_size:
            
            ind6 += 1
        else:
            total_flag = True
            return

    if int(hall[2]) >= 7:
        total = ind1 + ind2 + ind3 + ind4 + ind5 + ind6
        if total <= total_size:
            
            ind4 += 1
        else:
            total_flag = True
            return

    if int(hall[2]) >= 8:
        total = ind1 + ind2 + ind3 + ind4 + ind5 + ind6
        if total <= total_size:
            
            ind5 += 1
        else:
            total_flag = True
            return

    if int(hall[2]) >= 9:
        total = ind1 + ind2 + ind3 + ind4 + ind5 + ind6
        if total <= total_size:
            
            ind6 += 1
        else:
            total_flag = True
            return


def colls_3(hall):
    # write = ',' * int(float(hall[2]) * 0.5), hall[0], '\n'
    # outfile.writelines(write)

    i = 0
    ttl = True
    while True:
        # for i in range(0, int(hall[1])):

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


def main_split(halls, rollno):
    global rollnos
    global total_size, total_flag
    total_flag = True
    rollnos = rollno
    total_size = len(rollnos)
    sizes = 0
    for hall in halls:
        

        if total_flag:

            colls_3(hall)
            sizes = [ind1, ind2, ind3, ind4, ind5, ind6]
        else:
            c = input(total_flag)
            return sizes
    return sizes