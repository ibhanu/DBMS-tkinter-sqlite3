import os
import sqlite3
import tkinter
from os import path

# Designing Main(first) window

def main_account_screen():
	global main_screen
	main_screen = tkinter.Tk()
	main_screen.geometry("1920x1080")
	#main_screen.configure(background='white')
	main_screen.title("Account Login")
	tkinter.Label(main_screen , text="HOMEPAGE", fg="black", font=("times", 40, "bold")).pack()
	tkinter.Label(main_screen , text="").pack()
	#newl = "\n\n\n\n\n\n\n\n\n" * 2
	tkinter.Label(text=" ").pack()
	tkinter.Button(text="Login", height="3", width="35", bg="green", font=("calibri", 25, "bold"), command=login).pack()
	tkinter.Label(text="").pack()
	tkinter.Button(text="Register", height="3", width="35", bg="yellow", font=("calibri", 25, "bold"), command=register).pack()
	main_screen.mainloop()



# Designing window for login

def login():
	global login_screen
	login_screen = tkinter.Toplevel(main_screen)
	login_screen.title("Login")
	login_screen.geometry("1920x1080")
	tkinter.Label(login_screen, text="Please enter details below to login", font=("times", 40, "bold")).pack()
	tkinter.Label(login_screen, text="").pack()

	global username_verify
	global password_verify

	username_verify = tkinter.StringVar()
	password_verify = tkinter.StringVar()

	global username_login_entry
	global password_login_entry

	tkinter.Label(login_screen, text="Username * ", font=("calibre", 30, "bold")).pack()
	username_login_entry = tkinter.Entry(login_screen, textvariable=username_verify, width=30, font=("calibre"))
	username_login_entry.pack(ipady=10)
	tkinter.Label(login_screen, text="").pack()
	tkinter.Label(login_screen, text="Password * ", font=("calibre", 30, "bold")).pack()
	password_login_entry = tkinter.Entry(login_screen, textvariable=password_verify, show='*', width=30, font=("calibre"))
	password_login_entry.pack(ipady=10)
	tkinter.Label(login_screen, text="").pack()
	tkinter.Button(login_screen, text="Login", width=20, height=2, font=("calibri", 30, "bold"), command=login_verify).pack()


# Implementing event on login button

def login_verify():
	username1 = username_verify.get()
	password1 = password_verify.get()
	username_login_entry.delete(0, tkinter.END)
	password_login_entry.delete(0, tkinter.END)

	list_of_files = os.listdir()
	if username1 in list_of_files:
		file1 = open(username1, "r")
		verify = file1.read().splitlines()
		if password1 in verify:
			login_sucess()

		else:
			password_not_recognised()

	else:
		user_not_found()



def register():
	global register_screen
	register_screen = tkinter.Toplevel(main_screen)
	register_screen.title("Register")
	register_screen.geometry("1920x1080")

	global username
	global password
	global username_entry
	global password_entry
	username = tkinter.StringVar()
	password = tkinter.StringVar()

	tkinter.Label(register_screen, text="Please enter details below", font=("times", 40, "bold")).pack()
	tkinter.Label(register_screen, text="").pack()
	username_lable = tkinter.Label(register_screen, text="Username * ", font=("calibre", 30, "bold"))
	username_lable.pack()
	username_entry = tkinter.Entry(register_screen, textvariable=username, width=30, font=("calibre"))
	username_entry.pack(ipady=10)
	password_lable = tkinter.Label(register_screen, text="Password * ", font=("calibre", 30, "bold"))
	password_lable.pack()
	password_entry = tkinter.Entry(register_screen, textvariable=password, show='*', width=30, font=("calibre"))
	password_entry.pack(ipady=10)
	tkinter.Label(register_screen, text="").pack()
	tkinter.Button(register_screen, text="Register", width=20, height=2, font=("times", 30, "bold"), command=register_user).pack()

# Implementing event on register button

def register_user():
	username_info = username.get()
	password_info = password.get()
	if path.exists(username_info):
		tkinter.Label(register_screen, text="USERNAME ALREADY EXISTS !", fg="red", font=("calibri", 20)).pack()
	else:
		file = open(username_info, "w")
		file.write(username_info + "\n")
		file.write(password_info)
		file.close()

		username_entry.delete(0, tkinter.END)
		password_entry.delete(0, tkinter.END)

		tkinter.Label(register_screen, text="REGISTRATION SUCCESSFUL !", fg="green", font=("calibri", 20)).pack()



# Designing popup for login success

def login_sucess():
	global login_success_screen
	login_success_screen = tkinter.Toplevel(login_screen)
	login_success_screen.title("Success")
	login_success_screen.geometry("1920x1080")
	tkinter.Label(login_success_screen, text="WELCOME TO MUSIC DB BROWSER", font=("times",40, "bold")).pack()
	tkinter.Button(login_success_screen, text="OK", font=("times",30), command=delete_login_success).pack()


# Designing popup for login invalid password

def password_not_recognised():
	global password_not_recog_screen
	password_not_recog_screen = tkinter.Toplevel(login_screen)
	password_not_recog_screen.title("Unsuccessful")
	password_not_recog_screen.geometry("1920x1080")
	tkinter.Label(password_not_recog_screen, text="Invalid Password ", fg="red", font=("times", 40, "bold")).pack()
	tkinter.Button(password_not_recog_screen, text="OK", font=("times", 30), command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
	global user_not_found_screen
	user_not_found_screen = tkinter.Toplevel(login_screen)
	user_not_found_screen.title("Unsuccessful")
	user_not_found_screen.geometry("1920x1080")
	tkinter.Label(user_not_found_screen, text="User Not Found", fg="red", font=("times", 40,"bold")).pack()
	tkinter.Button(user_not_found_screen, text="OK", font=("times",30), command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
	login_success_screen.destroy()
	conn = sqlite3.connect('music.sqlite')

	mainWindow = tkinter.Tk()
	mainWindow.title('Music DB Browser')
	mainWindow.geometry('1920x1080')

	mainWindow.columnconfigure(0, weight=2)
	mainWindow.columnconfigure(1, weight=2)
	mainWindow.columnconfigure(2, weight=2)
	mainWindow.columnconfigure(3, weight=1)  # spacer column on right

	mainWindow.rowconfigure(0, weight=1)
	mainWindow.rowconfigure(1, weight=5)
	mainWindow.rowconfigure(2, weight=5)
	mainWindow.rowconfigure(3, weight=1)

	# ===== labels =====
	tkinter.Label(mainWindow, text="Artists", bg="#86c232").grid(row=0, column=0)
	tkinter.Label(mainWindow, text="Albums", bg="#86c232").grid(row=0, column=1)
	tkinter.Label(mainWindow, text="Songs", bg="#86c232").grid(row=0, column=2)  # columntextcolor
	# tkinter.Label(mainwindow1)

	# ===== Artists Listbox =====
	artistList = DataListBox(mainWindow, conn, "artists", "name")
	artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
	artistList.config(border=2, relief='sunken', bg="white")  # columncolor

	artistList.requery()

	# ===== Albums Listbox =====
	albumLV = tkinter.Variable(mainWindow)
	albumLV.set(("Choose an artist",))
	albumList = DataListBox(mainWindow, conn, "albums", "name", sort_order=("name",))
	# albumList.requery(12)
	albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
	albumList.config(border=2, relief='sunken', bg="white")

	# albumList.bind('<<ListboxSelect>>', get_songs)
	artistList.link(albumList, "artist")

	# ===== Songs Listbox =====
	songLV = tkinter.Variable(mainWindow)
	songLV.set(("Choose an album",))
	songList = DataListBox(mainWindow, conn, "songs", "title", ("track", "title"))
	# songList.requery()
	songList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
	songList.config(border=2, relief='sunken', bg="white")

	albumList.link(songList, "album")

	# ===== Main loop =====
	# testList = range(0, 100)
	# albumLV.set(tuple(testList))
	mainWindow.mainloop()
	print("closing database connection")
	conn.close()


def delete_password_not_recognised():
	password_not_recog_screen.destroy()


def delete_user_not_found_screen():
	user_not_found_screen.destroy()



class Scrollbox(tkinter.Listbox):

	def __init__(self, window, **kwargs):
		# tkinter.Listbox.__init__(self, window, **kwargs)  # Python 2
		super().__init__(window, **kwargs)

		self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

	def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):
		# tkinter.Listbox.grid(self, row=row, column=column, sticky=sticky, rowspan=rowspan,
		#  **kwargs)  # Python 2
		super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
		self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
		self['yscrollcommand'] = self.scrollbar.set


class DataListBox(Scrollbox):

	def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
		# Scrollbox.__init__(self, window, **kwargs)  # Python 2
		super().__init__(window, **kwargs)

		self.linked_box = None
		self.link_field = None
		self.link_value = None

		self.cursor = connection.cursor()
		self.table = table
		self.field = field

		self.bind('<<ListboxSelect>>', self.on_select)

		self.sql_select = "SELECT " + self.field + ", _id" + " FROM " + self.table
		if sort_order:
			self.sql_sort = " ORDER BY " + ','.join(sort_order)
		else:
			self.sql_sort = " ORDER BY " + self.field

	def clear(self):
		self.delete(0, tkinter.END)

	def link(self, widget, link_field):
		self.linked_box = widget
		widget.link_field = link_field

	def requery(self, link_value=None):
		self.link_value = link_value  # store the id, so we know the "master" record we're populated from
		if link_value and self.link_field:
			sql = self.sql_select + " WHERE " + self.link_field + "=?" + self.sql_sort
			print(sql)  # TODO delete this line
			self.cursor.execute(sql, (link_value,))
		else:
			print(self.sql_select + self.sql_sort)  # TODO delete this line
			self.cursor.execute(self.sql_select + self.sql_sort)

		# clear the listbox contents before re-loading
		self.clear()
		for value in self.cursor:
			self.insert(tkinter.END, value[0])

		if self.linked_box:
			self.linked_box.clear()

	def on_select(self, event):
		if self.linked_box:
			print(self is event.widget)  # TODO delete this line
			index = self.curselection()[0]
			value = self.get(index),

			# get the ID from the database row
			# Make sure we're getting the correct one, by including the link_value if appropriate
			if self.link_value:
				value = value[0], self.link_value
				sql_where = " WHERE " + self.field + "=? AND " + self.link_field + "=?"
			else:
				sql_where = " WHERE " + self.field + "=?"

			link_id = self.cursor.execute(self.sql_select + sql_where, value).fetchone()[1]
			self.linked_box.requery(link_id)


if __name__ == '__main__':
	main_account_screen()
