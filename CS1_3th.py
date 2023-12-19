def grading(time, perc, multi, tf):
    grade = 0
    correct_multi = ['A', 'C', 'A', 'D', 'B', 'B', 'B', 'A', 'B', 'B', 'B', 'B', 'A', 'D', 'B']
    correct_tf = ['T', 'F', 'F', 'F', 'T', 'T', 'T', 'F', 'T', 'T', 'F', 'T', 'T', 'F', 'F']

    for i in range(len(multi)):
        if multi[i] == correct_multi[i]:
            grade += 2
        if multi[i] != correct_multi[i]:
            print(f"Question {i+1}'s correct answer is {correct_multi[i]}")

        if tf[i] == correct_tf[i]:
            grade += 2
        if tf[i] != correct_tf[i]:
            print(f"Question TF {i+1}'s correct answer is {correct_tf[i]}")


    if time <= 9:
        grade += 20
    elif time > 9:
        grade += (20-(time-10))

    if perc >= 95:
        grade += 20
    elif perc < 95:
        grade += (20-(95-perc))
    
    return grade

print(grading(8, 96, ['B', 'C', 'C', 'D', 'A', 'B', 'B', 'D', 'B', 'B', 'B', 'B', 'A', 'D', 'B'], ['T', 'F', 'F', 'T', 'T', 'T', 'T', 'F', 'T', 'T', 'F', 'T', 'T', 'F', 'F']))