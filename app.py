from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route("/", methods=["GET", "POST"])
def index():
    AzkaNilai1 = AzkaNilai2 = Azka1 = Azka2 = Azka3 = Azka4 = Azka5 = Azka6 = Azka7 = Azka8 = Azka9 = None  # Inisialisasi awal agar aman saat GET
    if request.method == 'POST':
        AzkaNilai1 = int(request.form["AzkaNilai1"])
        AzkaNilai2 = int(request.form["AzkaNilai2"])

        Azka1 = AzkaNilai1 + AzkaNilai2
        Azka2 = AzkaNilai1 - AzkaNilai2
        Azka3 = int(AzkaNilai1 / AzkaNilai2)
        Azka4 = AzkaNilai1 * AzkaNilai2

        Azka5 = AzkaNilai1 == AzkaNilai2
        Azka6 = AzkaNilai1 > AzkaNilai2
        Azka7 = AzkaNilai1 < AzkaNilai2
        Azka8 = AzkaNilai1 <= AzkaNilai2
        Azka9 = AzkaNilai1 >= AzkaNilai2


    return render_template('index.html', AzkaNilai1=AzkaNilai1, 
                                        AzkaNilai2=AzkaNilai2, 
                                        Azka1=Azka1,
                                        Azka2=Azka2,
                                        Azka3=Azka3,
                                        Azka4=Azka4,
                                        Azka5=Azka5,
                                        Azka6=Azka6,
                                        Azka7=Azka7,
                                        Azka8=Azka8,
                                        Azka9=Azka9)

if __name__ == '__main__':
    app.run(debug=True)
