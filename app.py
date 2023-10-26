total = int(input("Enter Total Numbers of Hours Conducted: "))
absent = int(input("Enter Total Numbers of Hours Absent: "))
present = total - absent

print("conducted = ", total)
print("absent = ", absent)
print("present = ", present)

presentPercent = (present / total) * 100

print("Total percent of attendance: ", presentPercent)

if presentPercent >= 75:
    print("\nMadlad, you're saved!")
else:
    print("\nIndram says, Dekhlo kuch ho sakta hai to")
    safe = (3 / 4) * total
    print("\nTo be on a safe side: ", safe)
    numberOfMl = safe - present
    print("\nNumber of ML Hours required: ", numberOfMl)
