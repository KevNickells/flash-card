from json import load
from random import randrange
from logging import warning
from subprocess import Popen, PIPE
from shlex import split
from time import sleep

def send_message(message):
  try:
    command = split(f"""
      notify-send "{message}\n\n\n\n"
        --icon /home/kev/flash-card/poland.jpg
        --expire-time=5000
      """)

    response = Popen(command, stdout=PIPE, stderr=PIPE)
    response_code = response.wait()
    out, error = response.communicate()

  except Exception as ex:
    warning('fuckry here')
    warning(ex)

with open('/home/kev/flash-card/terms.json') as f:
  terms = load(f)
  random_number = randrange(len(terms))
  term = list(terms.keys())[random_number]
  response = terms[term]

  send_message(term)
  sleep(5)
  send_message(response)


