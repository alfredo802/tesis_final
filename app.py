from flask import Flask, render_template, jsonify, request
import pandas as pd
import json
from datetime import datetime, timedelta
import os
from config import GOOGLE_MAPS_API_KEY

app = Flask(__name__)

# Cargar datos de pronóstico
def cargar_pronostico_marea():
    try:
        df = pd.read_csv('resultados/pronostico_keller_futuro.csv')
        df['fecha'] = pd.to_datetime(df['fecha'])
        return df
    except Exception as e:
        print(f"Error al cargar datos: {str(e)}")
        return None

@app.route('/')
def index():
    return render_template('index.html', google_maps_api_key=GOOGLE_MAPS_API_KEY)

@app.route('/api/pronostico')
def get_pronostico():
    fecha_inicio = request.args.get('fecha_inicio')
    fecha_fin = request.args.get('fecha_fin')
    
    df = cargar_pronostico_marea()
    if df is None:
        return jsonify({'error': 'No se pudieron cargar los datos'}), 500
    
    if fecha_inicio and fecha_fin:
        fecha_inicio = pd.to_datetime(fecha_inicio)
        fecha_fin = pd.to_datetime(fecha_fin)
        df = df[(df['fecha'] >= fecha_inicio) & (df['fecha'] <= fecha_fin)]
    
    # Convertir a formato para el gráfico
    datos = {
        'fechas': df['fecha'].dt.strftime('%Y-%m-%d %H:%M:%S').tolist(),
        'valores': df['keller_pronostico'].tolist()
    }
    
    return jsonify(datos)

@app.route('/api/pronostico/hoy')
def get_pronostico_hoy():
    df = cargar_pronostico_marea()
    if df is None:
        return jsonify({'error': 'No se pudieron cargar los datos'}), 500
    
    hoy = datetime.now().date()
    df_hoy = df[df['fecha'].dt.date == hoy]
    
    datos = {
        'fechas': df_hoy['fecha'].dt.strftime('%H:%M').tolist(),
        'valores': df_hoy['keller_pronostico'].tolist()
    }
    
    return jsonify(datos)

if __name__ == '__main__':
    app.run(debug=True) 