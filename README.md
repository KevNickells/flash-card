# flash-card
Wee flash card app - shows me words I'm trying to learn every minute.

# Why?

I'm learning Polish. I'm at my computer all the time. Why not have a word show
up once a minute to help with learning?

# Note

Tested in Manjaro - have no idea about other Linux flavours, I'm sorry to say.

# How do I?

Cron setup is below; it randomly selects a term (JSON key) from `terms.json` and displays
it for 5 seconds; it then displays the English translation (JSON value).


## This needs...

Linux, cron, python.

## Setup

`crontab -e` --> opens the crontable
Add `* * * * * sh /home/kev/flash-card/flash-card.sh`

## possible problems

Try `chmod +x flash-card.sh`

## Will it work in...
### Mac OS

Dunno, but it should

### Windows

Probably not, sorry. There's probably an easier, Powershell way to do it rather
than using the Linux subsystem but I don't use Windows to know I'm afraid.


