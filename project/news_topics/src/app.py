import os
from flask import Flask, render_template, request
import time
import prediction as pre

max_length = 1000

app = Flask(__name__,  static_url_path='', static_folder='static')

# Hiển thị trang để nhập thông tin
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/evaluate")
def evaluate():
    return render_template("evaluate.html")

@app.route("/svm", methods=["POST"])
def svm_predict():
    try:
        news = request.json["news"][:max_length]

        start = time.time_ns()

        result = pre.svm_predict(news)

        print(result)

        end = time.time_ns()

        # to ms
        exec_time = f"{str((end-start)/pow(10, 6))} ms"

        return {
            "time": str(exec_time),
            "result": result
        }
    except Exception as e:
        print(e)

        return "Error happen", 500

@app.route("/knn", methods=["POST"])
def knn_predict():
    try:
        news = request.json["news"][:max_length]

        start = time.time_ns()

        result = pre.knn_predict(news)

        print(result)

        end = time.time_ns()

        # to ms
        exec_time = f"{str((end-start)/pow(10, 6))} ms"

        return {
            "time": str(exec_time),
            "result": result
        }
    except Exception as e:
        print(e)

        return "Error happen", 500

@app.route("/bayes", methods=["POST"])
def bayes_predict():
    try:
        news = request.json["news"][:max_length]

        start = time.time_ns()

        result = pre.bayes_predict(news)

        print(result)

        end = time.time_ns()

        # to ms
        exec_time = f"{str((end-start)/pow(10, 6))} ms"

        return {
            "time": str(exec_time),
            "result": result
        }
    except Exception as e:
        print(e)

        return "Error happen", 500

@app.route("/phoBert", methods=["POST"])
def phoBERT():
    print(request.json)
    return {}

if os.environ.get("PORT") is None:
 os.environ["PORT"] = "80"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=os.environ.get("PORT"))
