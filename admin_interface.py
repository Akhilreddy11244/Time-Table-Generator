import tkinter as tk
from tkinter import messagebox
import webbrowser
import auth_data


def generate_timetable_html(college, classname, year, day, timetable, faculty, room):
    with open('timetable.html', 'w') as f:
        code = f"""
        <!DOCTYPE html>
        <html>
        <head><title>Timetable</title></head>
        <body>
            <p><br></p>
            <font face='Arial'>
                <p><b>{college} - {classname} ({year})</b></p>
                <table border="1">
                    <thead>
                        <tr>
                            <th>Day</th>
                            <th>9:20 - 10:20</th>
                            <th>10:20 - 11:20</th>
                            <th>11:20 - 12:20</th>
                            <th>12:20 - 1:20</th>
                            <th>1:20 - 2:00</th>
                            <th>2:00 - 3:00</th>
                            <th>3:00 - 4:00</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>{day}</td>
                            <td>{timetable[0]}</td>
                            <td>{timetable[1]}</td>
                            <td>{timetable[2]}</td>
                            <td>{timetable[3]}</td>
                            <td>{timetable[4]}</td>
                            <td>{timetable[5]}</td>
                            <td>{timetable[6]}</td>
                        </tr>
                        <tr>
                            <td>Faculty</td>
                            <td>{faculty[0]}</td>
                            <td>{faculty[1]}</td>
                            <td>{faculty[2]}</td>
                            <td>{faculty[3]}</td>
                            <td>{faculty[4]}</td>
                            <td>{faculty[5]}</td>
                            <td>{faculty[6]}</td>
                        </tr>
                        <tr>
                            <td>Room</td>
                            <td>{room[0]}</td>
                            <td>{room[1]}</td>
                            <td>{room[2]}</td>
                            <td>{room[3]}</td>
                            <td>{room[4]}</td>
                            <td>{room[5]}</td>
                            <td>{room[6]}</td>
                        </tr>
                    </tbody>
                </table>
            </font>
        </body>
        </html>
        """
        f.write(code)
    webbrowser.open('timetable.html')


def admin_interface():
    def login():
        username = username_entry.get()
        password = password_entry.get()
        if auth_data.admin_credentials.get(username) == password:
            messagebox.showinfo("Login Successful", "Login Successful")
            login_frame.pack_forget()
            input_frame.pack()
        else:
            messagebox.showerror("Login Failed", "Invalid Credentials")

    def submit():
        college = college_entry.get()
        classname = class_entry.get()
        year = year_entry.get()
        day = day_entry.get()
        timetable = [
            period1_entry.get(),
            period2_entry.get(),
            period3_entry.get(),
            period4_entry.get(),
            period5_entry.get(),
            period6_entry.get(),
            period7_entry.get()
        ]
        faculty = [
            faculty1_entry.get(),
            faculty2_entry.get(),
            faculty3_entry.get(),
            faculty4_entry.get(),
            faculty5_entry.get(),
            faculty6_entry.get(),
            faculty7_entry.get()
        ]
        room = [
            room1_entry.get(),
            room2_entry.get(),
            room3_entry.get(),
            room4_entry.get(),
            room5_entry.get(),
            room6_entry.get(),
            room7_entry.get()
        ]
        generate_timetable_html(college, classname, year, day, timetable, faculty, room)
        messagebox.showinfo("Timetable Generated", "Timetable has been generated and opened in your browser")

    root = tk.Tk()
    root.title("Admin Login")

    login_frame = tk.Frame(root)
    login_frame.pack()

    tk.Label(login_frame, text="Admin Login").grid(row=0, column=1)
    tk.Label(login_frame, text="Username").grid(row=1, column=0)
    tk.Label(login_frame, text="Password").grid(row=2, column=0)

    username_entry = tk.Entry(login_frame)
    password_entry = tk.Entry(login_frame, show="*")

    username_entry.grid(row=1, column=1)
    password_entry.grid(row=2, column=1)

    tk.Button(login_frame, text="Login", command=login).grid(row=3, column=1)

    input_frame = tk.Frame(root)
    tk.Label(input_frame, text="Enter College/School Name").grid(row=0, column=0)
    college_entry = tk.Entry(input_frame)
    college_entry.grid(row=0, column=1)

    tk.Label(input_frame, text="Enter Class").grid(row=1, column=0)
    class_entry = tk.Entry(input_frame)
    class_entry.grid(row=1, column=1)

    tk.Label(input_frame, text="Enter Academic Year").grid(row=2, column=0)
    year_entry = tk.Entry(input_frame)
    year_entry.grid(row=2, column=1)

    tk.Label(input_frame, text="Enter Day").grid(row=3, column=0)
    day_entry = tk.Entry(input_frame)
    day_entry.grid(row=3, column=1)

    tk.Label(input_frame, text="Enter Period 1").grid(row=4, column=0)
    period1_entry = tk.Entry(input_frame)
    period1_entry.grid(row=4, column=1)

    tk.Label(input_frame, text="Enter Period 2").grid(row=5, column=0)
    period2_entry = tk.Entry(input_frame)
    period2_entry.grid(row=5, column=1)

    tk.Label(input_frame, text="Enter Period 3").grid(row=6, column=0)
    period3_entry = tk.Entry(input_frame)
    period3_entry.grid(row=6, column=1)

    tk.Label(input_frame, text="Enter Period 4").grid(row=7, column=0)
    period4_entry = tk.Entry(input_frame)
    period4_entry.grid(row=7, column=1)

    tk.Label(input_frame, text="Enter Period 5").grid(row=8, column=0)
    period5_entry = tk.Entry(input_frame)
    period5_entry.grid(row=8, column=1)

    tk.Label(input_frame, text="Enter Period 6").grid(row=9, column=0)
    period6_entry = tk.Entry(input_frame)
    period6_entry.grid(row=9, column=1)

    tk.Label(input_frame, text="Enter Period 7").grid(row=10, column=0)
    period7_entry = tk.Entry(input_frame)
    period7_entry.grid(row=10, column=1)

    tk.Label(input_frame, text="Enter Faculty Name 1").grid(row=11, column=0)
    faculty1_entry = tk.Entry(input_frame)
    faculty1_entry.grid(row=11, column=1)

    tk.Label(input_frame, text="Enter Faculty Name 2").grid(row=12, column=0)
    faculty2_entry = tk.Entry(input_frame)
    faculty2_entry.grid(row=12, column=1)

    tk.Label(input_frame, text="Enter Faculty Name 3").grid(row=13, column=0)
    faculty3_entry = tk.Entry(input_frame)
    faculty3_entry.grid(row=13, column=1)

    tk.Label(input_frame, text="Enter Faculty Name 4").grid(row=14, column=0)
    faculty4_entry = tk.Entry(input_frame)
    faculty4_entry.grid(row=14, column=1)

    tk.Label(input_frame, text="Enter Faculty Name 5").grid(row=15, column=0)
    faculty5_entry = tk.Entry(input_frame)
    faculty5_entry.grid(row=15, column=1)

    tk.Label(input_frame, text="Enter Faculty Name 6").grid(row=16, column=0)
    faculty6_entry = tk.Entry(input_frame)
    faculty6_entry.grid(row=16, column=1)

    tk.Label(input_frame, text="Enter Faculty Name 7").grid(row=17, column=0)
    faculty7_entry = tk.Entry(input_frame)
    faculty7_entry.grid(row=17, column=1)

    tk.Label(input_frame, text="Enter Room Number 1").grid(row=18, column=0)
    room1_entry = tk.Entry(input_frame)
    room1_entry.grid(row=18, column=1)

    tk.Label(input_frame, text="Enter Room Number 2").grid(row=19, column=0)
    room2_entry = tk.Entry(input_frame)
    room2_entry.grid(row=19, column=1)

    tk.Label(input_frame, text="Enter Room Number 3").grid(row=20, column=0)
    room3_entry = tk.Entry(input_frame)
    room3_entry.grid(row=20, column=1)

    tk.Label(input_frame, text="Enter Room Number 4").grid(row=21, column=0)
    room4_entry = tk.Entry(input_frame)
    room4_entry.grid(row=21, column=1)

    tk.Label(input_frame, text="Enter Room Number 5").grid(row=22, column=0)
    room5_entry = tk.Entry(input_frame)
    room5_entry.grid(row=22, column=1)

    tk.Label(input_frame, text="Enter Room Number 6").grid(row=23, column=0)
    room6_entry = tk.Entry(input_frame)
    room6_entry.grid(row=23, column=1)

    tk.Label(input_frame, text="Enter Room Number 7").grid(row=24, column=0)
    room7_entry = tk.Entry(input_frame)
    room7_entry.grid(row=24, column=1)

    tk.Button(input_frame, text="Generate Timetable", command=submit).grid(row=25, column=1)

    root.mainloop()


if __name__ == "__main__":
    admin_interface()
