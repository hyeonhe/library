from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 데이터를 저장할 dictionary 초기화
members = {}
books = {}

@app.route('/')
def index():
    return render_template('index.html', members=members, books=books)

@app.route('/add_member', methods=['POST'])
def add_member():
    member_name = request.form.get('member_name')
    members[member_name] = []
    return redirect(url_for('index'))

@app.route('/delete_member', methods=['POST'])
def delete_member():
    member_name = request.form.get('member_name')
    if member_name in members:
        del members[member_name]
    return redirect(url_for('index'))

@app.route('/add_book', methods=['POST'])
def add_book():
    book_title = request.form.get('book_title')
    books[book_title] = 'available'
    return redirect(url_for('index'))

@app.route('/delete_book', methods=['POST'])
def delete_book():
    book_title = request.form.get('book_title')
    if book_title in books:
        del books[book_title]
    return redirect(url_for('index'))

@app.route('/borrow_book', methods=['POST'])
def borrow_book():
    member_name = request.form.get('member_name')
    book_title = request.form.get('book_title')
    if member_name in members and book_title in books and books[book_title] == 'available':
        members[member_name].append(book_title)
        books[book_title] = 'borrowed'
    return redirect(url_for('index'))

@app.route('/return_book', methods=['POST'])
def return_book():
    member_name = request.form.get('member_name')
    book_title = request.form.get('book_title')
    if member_name in members and book_title in members[member_name]:
        members[member_name].remove(book_title)
        books[book_title] = 'available'
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
