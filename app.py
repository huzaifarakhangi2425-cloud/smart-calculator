from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Smart Calculator</h1>
    <input id='input' placeholder='Type 2+2 or 5*10'/>
    <button onclick='calc()'>Calculate</button>
    <h2 id='result'></h2>

    <script>
    async function calc() {
        let val = document.getElementById("input").value;

        let res = await fetch("/calc", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({input: val})
        });

        let data = await res.json();
        document.getElementById("result").innerText = data.result;
    }
    </script>
    """

@app.route("/calc", methods=["POST"])
def calc():
    data = request.get_json()
    try:
        result = eval(data["input"])
    except Exception:
        result = "Error"
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
