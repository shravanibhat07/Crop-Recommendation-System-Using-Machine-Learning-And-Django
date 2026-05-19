from django.shortcuts import render
import joblib
import numpy as np

model = joblib.load("best_model.pkl")

scaler = joblib.load("scaler.pkl")


def crop(request):

    if request.method == "POST":

        N = float(request.POST["N"])
        P = float(request.POST["P"])
        K = float(request.POST["K"])
        temperature = float(request.POST["temperature"])
        humidity = float(request.POST["humidity"])
        ph = float(request.POST["ph"])
        rainfall = float(request.POST["rainfall"])

        data = np.array([[

            N,
            P,
            K,
            temperature,
            humidity,
            ph,
            rainfall

        ]])

        scaled_data = scaler.transform(data)

        prediction = model.predict(scaled_data)[0]

        result = prediction

        accuracies = {

            "Logistic Regression": "96.36%",
            "Decision Tree": "98.64%",
            "Random Forest": "99.32%",
            "KNN": "95.68%",
            "SVM": "96.82%",
            "Naive Bayes": "99.55%"
        }

        best_algorithm = max(accuracies, key=accuracies.get)

        return render(request, "cropapp/result.html", {

            "result": result,
            "accuracies": accuracies,
            "best_algorithm": best_algorithm

        })

    return render(request, "cropapp/index.html")