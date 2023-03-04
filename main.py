from flask import Flask, render_template, request, redirect, url_for
from collections import namedtuple

app = Flask(__name__)
# Create a named tuple
Message = namedtuple('Message', 'amount')
messages = []


def make_result(deposit_amount, deposit_term, interest_rate):
    try:
        # Input validation
        if deposit_amount < 100000000 and deposit_term < 50 and interest_rate < 100:
            # Performing Calculations
            for i in range(1, deposit_term + 1):
                temporary_variable = (deposit_amount * interest_rate) / 100
                deposit_amount = round(deposit_amount + temporary_variable, 2)
                messages.append(Message(deposit_amount))
        return deposit_amount
    except (ValueError, TypeError):
        return 0


@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", messages=messages)


# Create add_number route
@app.route('/add_number', methods=['POST'])
def add_message():
    # Cleaning list
    messages.clear()
    try:
        # Get variables from form
        deposit_amount = int(request.form['deposit_amount'])
        deposit_term = int(request.form['deposit_term'])
        interest_rate = float(request.form['interest_rate'])
        make_result(deposit_amount, deposit_term, interest_rate)
    except ValueError:
        pass
    return redirect(url_for('index'))


# Start
if __name__ == "__main__":
    app.run(debug=True)
