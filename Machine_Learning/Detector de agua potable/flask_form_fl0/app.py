from flask import Flask, request, jsonify, render_template
import pandas as pd
from datetime import datetime
import pickle
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, text
import io
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

#engine= create_engine("sqlite:///./base_datos/predictions.db")
#engine = create_engine("postgresql://postgres:password@database-1.ciesmwidx3x0.eu-north-1.rds.amazonaws.com:5432/postgres")

# with open("modelo.pkl",  "rb") as f:
#     loaded_model = pickle.load(f)


app = Flask(__name__)

@app.route("/", methods=["GET"])
def inicio():
    return """<h1>Flask app para predecir si el agua es potable o no segun una serie de parametros:</h1>

    La predicción se realiza desde la ruta "/predict_form" y se tienen que poner los valores con las abreviaturas indicadas: <br>
    <br>
    <br>
    'Valor del PH' -> ph <br>
    'Dureza' -> dur <br>
    'Sólidos totales disueltos - TDS' -> tds <br>
    'Cloraminas' -> clo <br>
    'Sulfatos' -> sulf <br>
    'Conductividad' -> cond <br>
    'Carbono orgánico' -> co <br>
    'Trihalometanos' -> thm <br>
    'Turbidez' -> turb <br>
    <br>
    <br>
    Para compobar el registro de predicciones realizadas se realiza desde la ruta "/check_logs"

    """
    
@app.route("/check_logs", methods=["GET"])
def check_logs():
    
    filter = False
    start = request.args.get("start")
    end = request.args.get("end")
    filter = request.args.get("filter")

    if filter == True:

        query = f"""

            select * from predictions
            where fecha < "{end}"
            and fecha > "{start}";

        """
    else:
        query = f"""

            select * from predictions """
            
    return pd.read_sql(query, con=engine).to_html()


@app.route("/predict_form", methods=["GET", "POST"])
def predict_form():
    if request.method == "POST":
        ph = request.form.get("ph", None)
        dureza = request.form.get("dur", None)
        tds = request.form.get("tds", None)
        cloraminas = request.form.get("clo", None)
        sulfatos = request.form.get("sulf", None)
        conductividad = request.form.get("cond", None)
        carbono_o = request.form.get("co", None)
        trihalometanos = request.form.get("thm", None)
        turbidez = request.form.get("turb", None)
        
        data2pred = [ph, dureza, tds, cloraminas, sulfatos, conductividad, carbono_o, trihalometanos, turbidez]
        
        # IF ARGS MISSING, ERROR 0
        if None in data2pred:
            return {"results": 0}

        # IF ANY VALUE NOT FLOAT, ERROR 1
        if len(data2pred) != len([float(s) for s in data2pred if not s.isalpha()]):
            return {"results": 1}
        

        inputs = str(data2pred)
        output = loaded_model.predict([data2pred])[0]
        fecha = str(datetime.now())[0:19]
        
        def clasificar_agua(output):
            if output == 0:
                return 'Agua no potable'
            elif output == 1:
                return 'Agua potable'
            else:
                return 'Valor de predicción no válido'


        output2 = clasificar_agua(output)


        df = pd.DataFrame({
            "fecha": [fecha],
            "inputs": [inputs],
            "prediction": [output2]
        })
        
        
        df.to_sql("predictions", con=engine, if_exists="append", index=None)
    
        return render_template("form.html", prediction = output2)
    
    
    return render_template("form.html", prediction = "N/A")

if __name__ == "__main__":
    engine= create_engine("sqlite:///./predictions.db")
    #engine= create_engine("postgresql://fl0user:WQoFRVutI1K4@ep-steep-dew-56828010.eu-central-1.aws.neon.fl0.io:5432/database?sslmode=require")
    with open("modelo.pkl",  "rb") as f:
        loaded_model = pickle.load(f)
    app.run(debug=True, port=8080)