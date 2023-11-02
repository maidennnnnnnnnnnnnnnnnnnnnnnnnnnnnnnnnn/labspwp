from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'asdasd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedbacks.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    comment = db.Column(db.Text, nullable=False)

class FeedbackForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    comment = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm()

    if form.validate_on_submit():
        feedback = Feedback(name=form.name.data, comment=form.comment.data)
        db.session.add(feedback)
        db.session.commit()
        flash('Feedback submitted successfully', 'success')
        return redirect(url_for('feedback'))

    feedbacks = Feedback.query.all()
    return render_template('feedback.html', form=form, feedbacks=feedbacks)

asd = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)