from app import app
from flask import render_template
from flask import request
from flask import redirect
from models.book_class import Book
from models.user_class import User
from models.book_list import book_list
from models.book_list import available_books
from models.user_list import user_by_name
from models.user_list import user_by_id
from models.user_list import add_user

@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "GET":
        return render_template("index.html", page_title = "Page title", page_h1 = "Page h1", book_list = book_list) 
    elif request.method == "POST":
        book_list.append(Book(**request.form))
        return redirect("/")

# Log in page
@app.route("/login")
def log_in():
    return render_template("login.html")

# Check login and password and change authentication status
@app.route("/validate_login", methods=["POST"])
def validate_login():
    login_details = request.form
    if (username := login_details["name"]) in user_by_name.keys():
        user = user_by_name[username]
        print(user)
        if login_details["password"] == user.password:
            user.login()
            return redirect(f"/{user.userid}/homepage")
    return redirect("/login")

# Log user out changing auth status
@app.route("/log_out/<user_id>")
def log_out(user_id):
    user = user_by_id[user_id]
    user.log_out()
    return redirect("/")

# User homepage
@app.route("/<user_id>/homepage")
def user_homepage(user_id):
    user = user_by_id[user_id]
    available_book_list = available_books(book_list)
    return render_template("user_homepage.html", user=user, available_books=available_book_list, book_list=book_list)

# Add new book object to list
@app.route("/<user_id>/new_book", methods=["POST"])
def add_book(user_id):
    book_list.append(Book(**request.form))
    return redirect(f"/{user_id}/all_books")

# Show book details
@app.route("/<user_id>/book/<int:index>")
def show_book_info(user_id, index):
    user = user_by_id[user_id]
    return render_template("book_info.html", book=book_list[index], user=user)

# User rent selected books
@app.route("/<user_id>/rent/", methods=["POST"])
def user_rent_item(user_id):
    user = user_by_id[user_id]
    for book_name in request.form.keys():
        for book_object in book_list:
            if book_name == book_object.title:
                book_object.check_out()
                user.rent_a_book(book_object)
                break                
    return redirect(f"/{user_id}/homepage")

# User return selected books
@app.route("/<user_id>/return/", methods=["POST"])
def user_return_item(user_id):
    user = user_by_id[user_id]
    for book_name in request.form.keys():
        for book_object in user.books:
            if book_name == book_object.title:
                book_object.check_in()
                user.return_a_book(book_object)
                break
    return redirect(f"/{user_id}/homepage")

# Show all books (privilege buttons for admin users)
@app.route("/<user_id>/all_books")
def user_view_all(user_id):
    user = user_by_id[user_id]
    return render_template("user_view_all.html", user=user, book_list=book_list)
    
# Delete selected books if admin user
@app.route("/<user_id>/delete", methods=["POST"])
def admin_delete_books(user_id):
    for book_name in request.form.keys():
        for book_object in book_list:
            if book_object.title == book_name:
                book_list.remove(book_object)
                break
    return redirect(f"/{user_id}/all_books")
        
        
    
    
    
@app.route("/test")
def test_page():
    add_user(user_by_name, user_by_id, User("a", "1"))
    print(user_by_name)
    return render_template("test_page.html")
    