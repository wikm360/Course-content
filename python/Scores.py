num_students = int(input("تعداد دانش‌آموزان را وارد کنید: "))

students = []
grades = []

for i in range(num_students):
    name = input(f"نام دانش‌آموز {i+1}: ")
    grade = float(input(f"نمره {name}: "))
    students.append(name)
    grades.append(grade)

average = sum(grades) / len(grades)

max_grade = max(grades)
min_grade = min(grades)

max_index = grades.index(max_grade)
min_index = grades.index(min_grade)

print("\n📚 لیست نمرات:")
for i in range(len(students)):
    print(f"{students[i]}: {grades[i]}")

print("\n📊 آمار کلی:")
print(f"میانگین نمرات کلاس: {average:.2f}")
print(f"بیشترین نمره: {students[max_index]} با نمره {max_grade}")
print(f"کمترین نمره: {students[min_index]} با نمره {min_grade}")