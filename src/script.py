from browser import document
import time

title = 'Python'
document['header'].html = f"Hello, {title}!"

counter = 0

def increment(ev):
    global counter
    counter += 1
    document['counter'].html = str(counter)

document["counter-button"].bind("click", increment)

# check console
current_time = int(time.strftime('%H'))
if current_time < 12 :
      print('Good morning')
      document['cumprimento'].html = 'Good morning'
elif 12 <= current_time < 18:
      print('Good afternoon')
      document['cumprimento'].html = 'Good afternoon'
else:
      print('Good evening')
      document['cumprimento'].html = 'Good evening'
