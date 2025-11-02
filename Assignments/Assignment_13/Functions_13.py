from Assignment_13_Solved import read_students, add_student, average_marks_by_subject, update_student_mark

while True:
    print("\n=== სტუდენტების მენიუ ===")
    print("1. დაამატე სტუდენტი")
    print("2. წაიკითხე სტუდენტები")
    print("3. გამოთვალე საშუალო ქულა")
    print("4. განაახლე ქულა")
    print("5. გასვლა")

    choice = input("აირჩიე მოქმედება: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        read_students()
    elif choice == "3":
        average_marks_by_subject()
    elif choice == "4":
        update_student_mark()
    elif choice == "5":
        print("პროგრამა დასრულდა.")
        break
    else:
        print("არასწორი არჩევანი!")

