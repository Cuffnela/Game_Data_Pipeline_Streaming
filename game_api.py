#!/usr/bin/env python
import json
from kafka import KafkaProducer
from flask import Flask, request

app = Flask(__name__)
producer = KafkaProducer(bootstrap_servers='kafka:29092')


def log_to_kafka(topic, event):
    event.update(request.headers)
    producer.send(topic, json.dumps(event).encode())


@app.route("/")
def default_response():
    default_event = {'event_type': 'default'}
    log_to_kafka('events', default_event)
    return "This is the default response!\n"


@app.route("/buy_sword/<swordtype>")
def buy_sword(swordtype):
    buy_sword_event = {'event_type': 'buy_sword',
                       'sword_type': swordtype }
    log_to_kafka('events', buy_sword_event)
    return "Sword Purchased!\n"

@app.route("/join_guild/<guildname>")
def join_guild(guildname):
    join_guild_event = {'event_type': 'join_guild',
                        'guild_name': guildname}
    log_to_kafka('events', join_guild_event)
    return "Guild Joined!\n"
