def grading(time, perc, multi, tf):
    grade = 0
    correct_multi = ['C', 'B', 'D', 'D', 'B', 'A', 'A', 'B', 'D', 'B', 'A', 'B', 'A', 'B', 'A']
    correct_tf = ['F', 'T', 'F', 'F', 'F', 'T', 'F', 'T', 'F', 'T', 'F', 'F', 'F', 'T', 'T']

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
    elif perc < 95 and perc >= 75:
        grade += (20-(95-perc))
   
    return grade

print(grading(13, 97, ['C', 'B', 'D', 'D', 'B', 'A', 'A', 'B', 'D', 'B', 'D', 'B', 'A', 'B','A'],  ['T', 'F', 'F', 'F', 'T', 'T', 'F', 'T', 'F', 'T', 'T', 'F', 'F', 'T', 'T']))