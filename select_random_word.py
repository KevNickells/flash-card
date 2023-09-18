"""
  Opens terms.json; picks a term; displays term - definition using notify-send
  CRON calls this once per minute - see `crontab -l`
"""

from json import load
from random import randrange
from subprocess import Popen, PIPE
from shlex import split
from time import sleep

def send_message(message) -> None:
  command: list[str] = split(f"""
    notify-send "{message}\n\n"
      --icon /home/kev/flash-card/poland.jpg
      --expire-time=5000
    """)

  with Popen(command, stdout=PIPE, stderr=PIPE):
    pass


with open('/home/kev/flash-card/terms.json', 'r') as f:
  terms = load(f)
  random_number : int = randrange(len(terms))
  term = list(terms.keys())[random_number]
  response = terms[term]

  send_message(term)
  sleep(5)
  send_message(response)


