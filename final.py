from readDatabase import fetch_rollnos, devide_rollnos
from get_size import main_split
from allotement import main_call


def finalCall(classes, halls,outFileLoc):
    rollnos = fetch_rollnos(classes)
    sizes = main_split(halls=halls, rollno=rollnos)
    divided = devide_rollnos(rollnos, sizes)



    main_call(halls=halls, rollnos=divided,outFileLoc=outFileLoc)

