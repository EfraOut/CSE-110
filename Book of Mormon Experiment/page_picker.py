import random, os
import webbrowser
basedir = "C:\\book_of_mormon"

file = random.choice([x for x in os.listdir(basedir) if os.path.isfile(os.path.join(basedir, x))])

print(f"Playing file {file}...")
webbrowser.open(os.path.join(basedir, file))