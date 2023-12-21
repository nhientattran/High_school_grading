def grading(time, perc, multi, tf):
    grade = 0
    correct_multi = ['C', 'C', 'A', 'C', 'B', 'B', 'B', 'B', 'C', 'A', 'B', 'D', 'D', 'A', 'A']
    correct_tf = ['T', 'T', 'F', 'F', 'F', 'T', 'T', 'T', 'F', 'F', 'T', 'F', 'F', 'F', 'T']

    for i in range(len(multi)):
        if multi[i] == correct_multi[i]:
            grade += 2
        if multi[i] != correct_multi[i]:
            print(f"Question {i+1}'s correct answer is {correct_multi[i]}")

        if tf[i] == correct_tf[i]:
            grade += 2
        if tf[i] != correct_tf[i]:
            print(f"Question TF {i+1}'s correct answer is {correct_tf[i]}")


    if time <= 17:
        grade += 20
    elif time > 17 and time <= 37:
        grade += (20-(time-17))

    if perc >= 95:
        grade += 20
    elif perc < 95:
        grade += (20-(95-perc))
    
    return grade

print(grading(12, 96, ['A', 'C', 'A', 'C', 'A', 'B', 'A', 'B', 'B', 'A', 'B', 'D', 'D', 'A', 'A'],  ['T', 'F', 'F', 'T', 'F', 'F', 'T', 'T', 'T', 'F', 'T', 'F', 'F', 'F', 'T']))
