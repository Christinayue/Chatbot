# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, make_response,jsonify
import requests
from . import Resource
from .. import schemas
from wit import Wit



class AskMessage(Resource):

    def post(self, message):
    	#print(g.json)
        expression = message
        access_token = "4WQHCEYF22X2G7DBEEFPFFAD7CWMM37Z"
        client = Wit(access_token=access_token)
        resp = client.message(expression)
        print(resp )
        if resp['entities']['entity'][0]['value'] == 'timefinddentist':
            time = resp['entities']['datetime'][0]['value'][:10]
            print(time)
            url = "http://0.0.0.0:5003/v1/timeslotsdentist/" + time
            res = requests.get(url)
            data = res.json()['message']
            print(data)
        elif resp['entities']['entity'][0]['value'] == 'greeting':
            data = "hello, Nice to see you!"
        elif resp['entities']['entity'][0]['value'] == 'appointment':
            url = "http://0.0.0.0:5003/v1/timelots"
            res = requests.get(url)
            data = res.json()
            print(data)
        elif resp['entities']['entity'][0]['value'] == 'selectdentist':
            url = "http://0.0.0.0:5008/v1/dentists"
            res = requests.get(url)
            data = res.json()['message']
            print(data)
        elif resp['entities']['entity'][0]['value'] == 'information':
            print(resp)
            #name = resp['entities']['local_search_query'][0]['value']
            url = "http://0.0.0.0:5008/v1/dentists/Joshson" 
            res = requests.get(url)
            print(res)
            data = res.json()['message']
            
            print(data)
        elif resp['entities']['entity'][0]['value'] == 'dentisttime':
            print(resp)
            name = resp['entities']['contact'][0]['value']
            url = "http://0.0.0.0:5003/v1/dentist/" + name
            res = requests.get(url)
            data = res.json()['message']
            print(data)
        elif resp['entities']['entity'][0]['value'] == 'cancel':
            #print(resp)
            appointmentid= resp['entities']['number'][0]['value']
            url = "http://0.0.0.0:5003/v1/timeslots/" + str(appointmentid) 
            res = requests.delete(url)

            data = res.json()['message']
            print(data)
        elif resp['entities']['entity'][0]['value'] == 'searchappointment':
            print(resp)
            appointmentid = resp['entities']['local_search_query'][0]['value'][0]
            
            url = "http://0.0.0.0:5003/v1/timeslots/" +  str(appointmentid)
            res = requests.get(url)
            data = res.json()['message']
            print(data)
        elif resp['entities']['entity'][0]['value'] == 'bookappointment':
            appointmentid = resp['entities']['number'][0]['value']
            print(appointmentid)
            #name = resp['entities']['contact'][0]['value']
            url = "http://0.0.0.0:5003/v1/timeslots/"+ str(appointmentid)
            res = requests.post(url)
            data = res.json()['message']
            print(data)
        elif resp['entities']['entity'][0]['value'] == 'timefinddentist':
            time = resp['entities']['datetime'][0]['value']
            url = "http://0.0.0.0:5003/v1/timeslotsdentist/Monday%2012%3A00-13%3A00"
            res = requests.get(url)
            data = res.json()['message']
            print(data)
        return make_response(jsonify(data),200)