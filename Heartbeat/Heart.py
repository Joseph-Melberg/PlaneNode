import os
import time
import subprocess
import pika
import json
import time
import sys
def system_call(command):
    p = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
    return p.stdout.read()

credentials = pika.PlainCredentials('life','conway')
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit.centurionx.net',5672,'/',credentials))
channel = connection.channel()
channel.exchange_declare(exchange='Inter',exchange_type='direct',durable=True)
channel.queue_declare(queue='Reader')
messa = {}
messa["Name"] = sys.argv[1] 
def getMAC(interface='eth0'):
  # Return the MAC address of the specified interface
  try:
    str = open('/sys/class/net/%s/address' %interface).read()
  except:
    str = "00:00:00:00:00:00"
  return str[0:17]

messa["Mac"] = getMAC()
channel.queue_bind(exchange='Inter',queue='Reader',routing_key='/life')
channel.basic_publish(exchange='Inter',
                      routing_key='/life',
                      body=str(messa))
connection.close()
