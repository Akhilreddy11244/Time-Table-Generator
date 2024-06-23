import tkinter as tk
from tkinter import messagebox
import webbrowser
import auth_data


def download_timetable():
    import shutil
    shutil.copy('timetable.html', 'downloaded_timetable.html')
    messagebox.showinfo("Download Successful", "Timetable has been downloaded as 'downloaded_timetable.html'")


def student_interface():
    def login():
        username = username_entry.get()
        password = password_entry.get()
        if auth_data.student_credentials.get(username) == password:
            messagebox.showinfo("Login Successful", "Login Successful")
            logged_in_frame.pack()
        else:
            messagebox.showerror("Login Failed", "Invalid Credentials")

    root = tk.Tk()
    root.title("Student Login")

    login_frame = tk.Frame(root)
    login_frame.pack()

    tk.Label(login_frame, text="Student Login").grid(row=0, column=1)
    tk.Label(login_frame, text="Username").grid(row=1, column=0)
    tk.Label(login_frame, text="Password").grid(row=2, column=0)

    username_entry = tk.Entry(login_frame)
    password_entry = tk.Entry(login_frame, show="*")

    username_entry.grid(row=1, column=1)
    password_entry.grid(row=2, column=1)

    tk.Button(login_frame, text="Login", command=login).grid(row=3, column=1)

    logged_in_frame = tk.Frame(root)

    tk.Button(logged_in_frame, text="View Timetable", command=lambda: webbrowser.open('timetable.html')).grid(row=0, column=0)
    tk.Button(logged_in_frame, text="Download Timetable", command=download_timetable).grid(row=0, column=1)

    root.mainloop()


if __name__ == "__main__":
    student_interface()
