def attendance_report():
    total = int(input("Total Working Days: "))
    present = int(input("Days Present: "))

    percentage = (present / total) * 100

    print(f"\nAttendance = {percentage:.2f}%")

    if percentage >= 75:
        print("Status : Eligible\n")
    else:
        print("Status : Short Attendance\n")
