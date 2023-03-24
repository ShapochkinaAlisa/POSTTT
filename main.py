from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():

    return render_template("index1.html")


@app.route('/cartoons')
def cartoons():
    import sqlite3
    con_user = sqlite3.connect("users.db")
    cur_user = con_user.cursor()
    all_rating = cur_user.execute(f"SELECT Users_name, first_all, Phone_number FROM Users").fetchall()
    all_rating.sort(key=lambda x: x[0], reverse=True)
    if len(all_rating) >= 3:
        for i in range(3):
            print(all_rating[i])
    else:
        for i in all_rating:
            print(i)

    return render_template("cartoons.html", data=all_rating)


@app.route('/movies_of_all_time')
def movies_of_all_time():
    import sqlite3
    con_user = sqlite3.connect("users.db")
    cur_user = con_user.cursor()
    all_rating = cur_user.execute(f"SELECT Users_name, second_all, Phone_number FROM Users").fetchall()
    all_rating.sort(key=lambda x: x[0], reverse=True)
    if len(all_rating) >= 3:
        for i in range(3):
            print(all_rating[i])
    else:
        for i in all_rating:
            print(i)

    return render_template("movies_of_all_time.html", data=all_rating)


@app.route('/news')
def news():
    import sqlite3
    con_user = sqlite3.connect("users.db")
    cur_user = con_user.cursor()
    all_rating = cur_user.execute(f"SELECT Users_name, third_all, Phone_number FROM Users").fetchall()
    all_rating.sort(key=lambda x: x[0], reverse=True)
    if len(all_rating) >= 3:
        for i in range(3):
            print(all_rating[i])
    else:
        for i in all_rating:
            print(i)

    return render_template("news.html", data=all_rating)


@app.route('/soviet')
def soviet():
    import sqlite3
    con_user = sqlite3.connect("users.db")
    cur_user = con_user.cursor()
    all_rating = cur_user.execute(f"SELECT Users_name, fourth_all, Phone_number FROM Users").fetchall()
    all_rating.sort(key=lambda x: x[0], reverse=True)
    if len(all_rating) >= 3:
        for i in range(3):
            print(all_rating[i])
    else:
        for i in all_rating:
            print(i)


    return render_template("soviet.html", data=all_rating)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
