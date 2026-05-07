
from flask import Flask, request
app = Flask(__name__)
@app.route('/alkuluku')
def alkuluku():
    args = request.args
    luku = int(args.get("luku"))
    lista = list(range(2, (luku)))
    n = luku
    check = 0
    isprime = False
    for luku in lista:
        if n % luku == 0:
            check += 1
            break
    if check == 0:
        isprime = True
    else:
        isprime = False
    vastaus = {
        "luku": luku,
        "isPrime": isprime
    }
    return vastaus

app.run(use_reloader=True, host='127.0.0.1', port=3000)