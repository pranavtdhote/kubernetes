from flask import Flask, request, render_template_string

app = Flask(__name__)

content_list = []

template = """
<!DOCTYPE html>
<html>
<head>
    <title>Content Management</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: #333;
            margin: 0;
            padding: 0;
        }

        .container {
            width: 400px;
            margin: 50px auto;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        }

        h2 {
            text-align: center;
            color: #4a4a4a;
        }

        input[type="text"] {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        input[type="submit"] {
            width: 100%;
            padding: 10px;
            background: #667eea;
            border: none;
            color: white;
            font-weight: bold;
            border-radius: 5px;
            cursor: pointer;
            transition: 0.3s;
        }

        input[type="submit"]:hover {
            background: #5a67d8;
        }

        ul {
            list-style: none;
            padding: 0;
            margin-top: 20px;
        }

        li {
            background: #f1f1f1;
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 5px;
        }

        b {
            color: #333;
        }
    </style>
</head>

<body>
    <div class="container">
        <h2>📋 Content Management</h2>

        <form method="POST">
            Title:
            <input type="text" name="title" required>

            Description:
            <input type="text" name="desc" required>

            <input type="submit" value="Add Content">
        </form>

        <ul>
        {% for c in contents %}
            <li><b>{{c.title}}</b>: {{c.desc}}</li>
        {% endfor %}
        </ul>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        content_list.append({
            'title': request.form['title'],
            'desc': request.form['desc']
        })
    return render_template_string(template, contents=content_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)