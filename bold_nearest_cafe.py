from flask import Flask
from flask import request, render_template, redirect
from test_nearest_cafe import get_cafes_from_file, find_nearest_cafe

app = Flask(__name__)

@app.route('/nearest_cafe', methods=['GET', 'POST'])
def show_nearest_cafe():
    nearest_cafe = False
    error = False

    if request.method == 'POST':
        ltd = request.form.get('latitude')
        lng = request.form.get('longitude')

        try:
            ltd = float(ltd)
            lng = float(lng)
            cafes_list = get_cafes_from_file('csv/placelist.csv')
            nearest_cafe = find_nearest_cafe(cafes_list, ltd, lng)
            print(nearest_cafe)
        except ValueError:
            error = "Заполни форму правильно"
            
    return render_template('nearest_cafe.html', cafes=cafes_list, nearest_cafe=nearest_cafe, error=error)


if __name__ == "__main__":
    app.run(debug=True)
