# app.py - Aplicación principal de Flask para Tandem Metrix
from flask import Flask, render_template, request, flash, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = 'tandem_metrix_secret_key_2024'  # Cambiar en producción

@app.route('/')
def index():
    print("=" * 50)
    print("DEBUG INDEX - INFORMACIÓN COMPLETA")
    print("=" * 50)
    
    # Información básica
    print(f"Directorio actual: {os.getcwd()}")
    print(f"Template folder: {app.template_folder}")
    
    # Verificar archivos
    base_path = os.path.join(app.template_folder, 'base.html')
    index_path = os.path.join(app.template_folder, 'index.html')
    
    print(f"Base.html exists: {os.path.exists(base_path)}")
    print(f"Index.html exists: {os.path.exists(index_path)}")
    
    # Listar archivos en templates
    print("Archivos en templates/:")
    try:
        for file in os.listdir(app.template_folder):
            print(f"  - {file}")
    except Exception as e:
        print(f"Error listando templates: {e}")
    
    # Intentar renderizar
    print("Intentando renderizar template...")
    try:
        result = render_template('index.html')
        print(f"✅ Template renderizado exitosamente!")
        print(f"Longitud del resultado: {len(result)}")
        print(f"Primeros 100 chars: {repr(result[:100])}")
        
        # Verificar si contiene CSS en lugar de HTML
        if result.strip().startswith('/*'):
            print("🚨 PROBLEMA: El resultado contiene CSS, no HTML!")
        elif result.strip().startswith('<!DOCTYPE html>'):
            print("✅ El resultado es HTML válido")
        else:
            print(f"⚠️ Resultado inesperado")
            
        return result
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return f"<h1>Error renderizando template</h1><pre>{e}</pre>", 500

@app.route('/quienes-somos')
def quienes_somos():
    """Página Quiénes Somos"""
    return render_template('quienes_somos.html')

@app.route('/metodologia')
def metodologia():
    """Página de Servicios/Metodología"""
    return render_template('metodologia.html')

@app.route('/casos-exito')
def casos_exito():
    """Página de Casos de Éxito"""
    return render_template('casos_exito.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    """Página de Contacto"""
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        telefono = request.form.get('telefono')
        mensaje = request.form.get('mensaje')
        
        # Aquí puedes agregar lógica para enviar email, guardar en BD, etc.
        # Por ahora solo mostramos un mensaje de confirmación
        flash(f'Gracias {nombre}! Hemos recibido tu mensaje y te contactaremos pronto.', 'success')
        return redirect(url_for('contacto'))
    
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)