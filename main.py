from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

process = None
process_unfollow = None

@app.route('/')
def index():
    return render_template('interfazBot.html')

@app.route('/guardar_lista', methods=['POST'])
def guardar_lista():
    lista = request.json['lista']
    
    with open('hashtagfile', 'w', encoding='utf-8') as file:
        for item in lista:
            file.write(f"{item}\n")
    return 'Lista guardada en hashtagfile'

@app.route('/run')
def run():
    global process
    process = subprocess.Popen(['python', 'followerPost.py'])
    #output = subprocess.check_output(['python', 'followerPost.py'], shell=True)
    return "Bot Follower"

@app.route('/stop')
def stop():
    try:
        # Guardar el ID del proceso
        process_id = process.pid
        output = subprocess.run(['taskkill', '/F', '/T', '/PID', str(process_id)])
        return 'Proceso de Python terminado exitosamente.'
    except subprocess.CalledProcessError as e:
        return 'Error al intentar terminar el proceso de Python: ' + str(e)

@app.route('/unfollow')
def unfollow():
    global process_unfollow
    process_unfollow = subprocess.Popen(['python', 'unfollow.py'])
    return "sucess"

@app.route('/stopunfollow')
def stop_unfollow():
    try:
        process_id = process_unfollow.pid
        output = subprocess.run(['taskkill', '/F', '/T', '/PID', str(process_id)])
        return 'Proceso de Python terminado exitosamente.'
    except subprocess.CalledProcessError as e:
        return 'Error al intentar terminar el proceso de Python: ' + str(e)


if __name__ == '__main__':
    app.run(debug=True)