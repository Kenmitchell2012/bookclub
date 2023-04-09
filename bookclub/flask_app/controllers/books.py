from flask_app import app
from flask import render_template, redirect, url_for, request, flash, session
from flask_app.models.user import User
from flask_app.models.book import Book


@app.route('/createbook', methods=['POST'])
def create_book():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    print(session['user_id'])
    if not Book.validate_book(request.form):
        alert = 'Please fill all the fields'
        return redirect(url_for('dashboard', alert=alert))
    new_book = {
        'user_id': session['user_id'],
        'title': request.form['title'],
        'description': request.form['description']
    }
    print(new_book)
    Book.save_book(new_book)
    return redirect(url_for('dashboard'))

# edit book
@app.route('/edit/<int:book_id>')
def edit_book(book_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user = User.get_by_id(session['user_id'])
    print("Printing user", user)
    book = Book.get_book_by_id(book_id)
    print("Book from edit request", book)
    return render_template('edit_book.html', book=book, user=user)

# add book to favorites
@app.route('/add_to_favorites', methods=['POST'])
def add_to_favorites():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    print(session['user_id'])
    Book.add_to_favorites
    return redirect(url_for('dashboard'))

# update book
@app.route('/update/<int:book_id>', methods=['POST'])
def update(book_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    print("From update route", session['user_id'])
    if not Book.validate_book(request.form):
        alert = 'Please fill all the fields'
        return redirect(url_for('dashboard', alert=alert))
    data = {
        'user_id': session['user_id'],
        'title': request.form['title'],
        'description': request.form['description']
    }
    Book.update_book(book_id, data)
    return redirect(url_for('dashboard'))

# delete a book
@app.route('/delete/<int:book_id>')
def delete_book(book_id):
    if 'user_id' not in session:
        return redirect('/login')

    book = Book.get_book_by_id(book_id)
    book.delete_book(book_id)
    return redirect('/dashboard')