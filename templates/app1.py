from flask import Flask
from flask import render_template

app = Flask(__name__)

items = {
    'clothes': {
        1:{
            'href': "/clothes/item/1",
            'foto': "/static/image/clothes/foto1.jpeg",
            'title1': "ELLERY X M'O CAPSULE",
            'description': "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
            'price': 52.00
        },
        2:{
            'href': "/clothes/item/2",
            'foto': "/static/image/clothes/foto2.jpg",
            'title1': "Красный костюм",
            'description': "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
            'price': 105.00
        },
        3:{
            'href': "/clothes/item/3",
            'foto': "/static/image/clothes/foto3.jpg",
            'title1': "ELLERY X M'O CAPSULE",
            'description': "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
            'price': 52.00
        }
    },
    'shoes': {
        1: {
            'href': "/shoes/item/1",
            'foto': "/static/image/shoes/foto1.jpeg",
            'title1': "ELLERY X M'O CAPSULE",
            'description': "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
            'price': 52.00
        },
        2: {
            'href': "/shoes/item/2",
            'foto': "/static/image/shoes/foto2.jpg",
            'title1': "Красный костюм",
            'description': "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
            'price': 105.00
        },
        3: {
            'href': "/shoes/item/3",
            'foto': "/static/image/shoes/foto3.jpg",
            'title1': "ELLERY X M'O CAPSULE",
            'description': "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
            'price': 52.00
        }
    },
    'jackets': {
        1: {
            'href': "/jackets/item/1",
            'foto': "/static/image/jackets/foto1.jpg",
            'title1': "ELLERY X M'O CAPSULE",
            'description': "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
            'price': 52.00
        },
        2: {
            'href': "/jackets/item/2",
            'foto': "/static/image/jackets/foto2.jpg",
            'title1': "Красный костюм",
            'description': "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
            'price': 105.00
        },
        3: {
            'href': "/jackets/item/3",
            'foto': "/static/image/jackets/foto3.jpg",
            'title1': "ELLERY X M'O CAPSULE",
            'description': "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
            'price': 52.00
        },
        4: {
            'href': "/jackets/item/4",
            'foto': "/static/image/jackets/foto4.jpg",
            'title1': "ELLERY X M'O CAPSULE",
            'description': "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
            'price': 52.00
        },
        5: {
            'href': "/jackets/item/5",
            'foto': "/static/image/jackets/foto5.jpg",
            'title1': "ELLERY X M'O CAPSULE",
            'description': "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
            'price': 52.00
        },
        6: {
            'href': "/jackets/item/6",
            'foto': "/static/image/jackets/foto6.jpg",
            'title1': "ELLERY X M'O CAPSULE",
            'description': "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
            'price': 52.00
        }
    }
}

@app.route('/')
@app.route('/clothes/item/index')
@app.route('/shoes/item/index')
@app.route('/jackets/item/index')
@app.route('/index')
def hello_world():
    context = {
        'title': 'Главная',
    }
    return render_template("index.html", **context)

@app.route('/clothes')
def clothes():
    context = {
        'title': 'Одежда',
        'items': [
            {
                'href': "/clothes/item/1",
                'foto': "/static/image/clothes/foto1.jpeg",
                'title1': "ELLERY X M'O CAPSULE",
                'description': "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
                'price': 52.00
            },
            {
                'href': "/clothes/item/2",
                'foto': "/static/image/clothes/foto2.jpg",
                'title1': "Красный костюм",
                'description': "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
                'price': 105.00
            },
            {
                'href': "/clothes/item/3",
                'foto': "/static/image/clothes/foto3.jpg",
                'title1': "ELLERY X M'O CAPSULE",
                'description': "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
                'price': 52.00
            },
        ]
    }
    return render_template("clothes.html", **context)

@app.route('/shoes')
def shoes():
    context = {
        'title': 'Обувь',
        'items': [
            {
                'href': "/shoes/item/1",
                'foto': "/static/image/shoes/foto1.jpeg",
                'title1': "ELLERY X M'O CAPSULE",
                'description': "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
                'price': 52.00
            },
            {
                'href': "/shoes/item/2",
                'foto': "/static/image/shoes/foto2.jpg",
                'title1': "Красный костюм",
                'description': "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
                'price': 105.00
            },
            {
                'href': "/shoes/item/3",
                'foto': "/static/image/shoes/foto3.jpg",
                'title1': "ELLERY X M'O CAPSULE",
                'description': "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
                'price': 52.00
            },
        ]
    }
    return render_template("shoes.html", **context)

@app.route('/jackets')
def jackets():
    context = {
        'title': 'Куртки',
        'items': [
            {
                'href': "/jackets/item/1",
                'foto': "/static/image/jackets/foto1.jpg",
                'title1': "ELLERY X M'O CAPSULE",
                'description': "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
                'price': 52.00
            },
            {
                'href': "/jackets/item/2",
                'foto': "/static/image/jackets/foto2.jpg",
                'title1': "Красный костюм",
                'description': "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
                'price': 105.00
            },
            {
                'href': "/jackets/item/3",
                'foto': "/static/image/jackets/foto3.jpg",
                'title1': "ELLERY X M'O CAPSULE",
                'description': "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
                'price': 52.00
            },
            {
                'href': "/jackets/item/4",
                'foto': "/static/image/jackets/foto4.jpg",
                'title1': "ELLERY X M'O CAPSULE",
                'description': "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
                'price': 52.00
            },
            {
                'href': "/jackets/item/5",
                'foto': "/static/image/jackets/foto5.jpg",
                'title1': "ELLERY X M'O CAPSULE",
                'description': "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
                'price': 52.00
            },
            {
                'href': "/jackets/item/6",
                'foto': "/static/image/jackets/foto6.jpg",
                'title1': "ELLERY X M'O CAPSULE",
                'description': "Known for her sculptural takes on traditional tailoring, Australian arbiter of cool Kym Ellery teams up with Moda Operandi.",
                'price': 52.00
            }
        ]
    }
    return render_template("jackets.html", **context)

@app.route('/<category>/item/<int:num>')
def itemPrint(category, num):
    context = {
        'title': 'Одежда',
        'item' : items['clothes'][num]
    }
    return render_template("item.html", **context)

if __name__ == '__main__':
    app.run(debug=True)