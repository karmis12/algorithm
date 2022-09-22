n = int(input())

cases = [list(map(int, input().split())) for i in range(n)]
for students in cases:
    avg = sum(students[1:]) / students[0]
    bigger = 0
    for student in students[1:]:
        if student > avg:
            bigger += 1
    print(f"{(bigger/students[0]*100):.3f}%")