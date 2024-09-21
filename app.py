from flask import Flask
from flask import Flask, request
from flask_cors import CORS
import sqlite3
from datetime import datetime
app = Flask(__name__)

con = sqlite3.connect('abcall.db', check_same_thread=False)


@app.route('/notification', methods=['POST'])
def create_notification():
    insert_notification = """
    INSERT INTO notification (priority,incident_id,creation_date)
    VALUES(?,?,?);"""
    cur = con.cursor()
    data = request.get_json()
    parameters = (
        data.get('priority'), data.get('incident_id'), datetime.now()
        )
    cur.execute(insert_notification, parameters)
    con.commit()
    return {'statut': 'ok'}

@app.route('/incident', methods=['POST'])
def create_incident():
    insert_notification = """
    INSERT INTO incident (description,state,priority,client,agent,creation_date,update_date)
    VALUES(?,?,?,?,?,?,?);"""
    cur = con.cursor()
    data = request.get_json()
    parameters = (
        data.get('description'), data.get('state'), data.get('priority'),
        data.get('client'), data.get('agent'), datetime.now(),
        datetime.now()
        )
    cur.execute(insert_notification, parameters)
    con.commit()
    return {'statut': 'ok'}

if __name__ == '__main__':
    app.run(debug=True)
    