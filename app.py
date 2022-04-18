from flask import Flask, render_template, request
import pickle

model_be = pickle.load(open('model_be.pkl','rb'))
model_em = pickle.load(open('model_em.pkl','rb'))

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/result', methods = ['POST'])
def result():
    Your_Health = request.form['Your_Health']
    Your_School = request.form['Your_School']
    Your_Appearance = request.form['Your_Appearance']
    Your_Friends = request.form['Your_Friends']
    Your_Life = request.form['Your_Life']
    feel_safe_in_area = request.form['feel_safe_in_area']
    feel_tired_in_7days = request.form['feel_tired_in_7days']
    concentration_on_school_work = request.form['concentration_on_school_work']
    have_space_to_relax_at_home_no = request.form['have_space_to_relax_at_home_no']
    lots_of_things_i_am_good_at = request.form['lots_of_things_i_am_good_at']
    in_touch_with_friends_No = request.form['in_touch_with_friends_No']

    output1 = model_em.predict([[Your_School,Your_Appearance,Your_Friends,Your_Life,feel_safe_in_area,feel_tired_in_7days,have_space_to_relax_at_home_no]])
    output2 = model_be.predict([[Your_School,concentration_on_school_work,feel_tired_in_7days,Your_Appearance,Your_Friends,in_touch_with_friends_No,Your_Life,feel_safe_in_area,Your_Health,lots_of_things_i_am_good_at]])

    if output1==['Expected']:
        output1="Expected difficulties"
    elif output1==['Borderline difficulties']:
        output1="Borderline difficulties"
    else:
        output1 = "Clinical significant difficulties"

    if output2==['Expected']:
        output2 = "Expected difficulties"
    elif output2==['Borderline difficulties']:
        output2 ="Borderline difficulties"
    else:
        output2 = "Clinical significant difficulties"

    print(output1)
    print(output2)
    return render_template('home.html', output1=output1 ,output2=output2)


if __name__=="__main__":
    app.run(debug=True)
