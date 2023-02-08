from flask import Flask, render_template, request, redirect, url_for
from database import add_message, get_all_messages, delete_all_messages

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/delete')
def delete():
    # delete all messages
    delete_all_messages()
    return redirect(url_for('home'))


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        # getting info from form
        username = request.form['username']
        text = request.form['text']
        
        # add it to database
        add_message(username, text)

    return render_template('chat.html', messages=get_all_messages())

if __name__ == '__main__':
    app.run(debug=True)