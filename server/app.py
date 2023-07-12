#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    # animal = Animal.query.get(id)
    # animal = Animal.query.filter_by(id=id).first_or_404()
    # animal = Animal.query.filter_by(species='Monkey').all()
    # animal = Animal.query.filter(Animal.id==id).first_or_404()
    # if animal:= Animal.query.get(id):
    if animal:= Animal.query.get(id):
        response_body = f"""
            <ul>ID: {animal.id}</ul>
            <ul>Name: {animal.name}</ul>
            <ul>Species: {animal.species}</ul> 
            <ul>Zookeeper: {animal.zookeeper.name}</ul>
            <ul>Enclosure: {animal.enclosure.environment}</ul>
        """
        return make_response(response_body, 200)
    else:
        response_body = f"""
            <ul>404 Not Found any animals with id {id}</ul>
        """
        return make_response(response_body, 404)

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    if zk:= db.session.get(Zookeeper, id):
        response_body = f"""
            <ul>ID: {zk.id}</ul>
            <ul>Name: {zk.name}</ul>
            <ul>Birthday: {zk.birthday}</ul> 
        """
        animal_names = [animal.name for animal in zk.animals]
        
        for name in animal_names:
            response_body += f"<ul>Animal: {name}</ul>"       

        return make_response(response_body, 200)
    else:
        response_body = f"""
            <ul>404 Not Found any zookeeper with id {id}</ul>
        """
        return make_response(response_body, 404)

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    if enc:= db.session.get(Enclosure, id):
        response_body = f"""
            <ul>ID: {enc.id}</ul>
            <ul>Environment: {enc.environment}</ul>
            <ul>Open to Visitors: {enc.open_to_visitors}</ul>
        """
        animal_names = [animal.name for animal in enc.animals]
        for name in animal_names:
            response_body += f"<ul>Animal: {name}</ul>"
            
        return make_response(response_body, 200)
    else:
        response_body = f"""
            <ul>404 Not Found any zookeepers with id {id}</ul>
        """
        return make_response(response_body, 404)


if __name__ == '__main__':
    app.run(port=5555, debug=True)