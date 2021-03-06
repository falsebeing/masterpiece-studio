import logging
import datetime

# I assume decorators or something would improve this module


def timestamp():
	now = datetime.datetime.now()
	return f"{now.month}/{now.day}-{now.hour}:{now.minute}:{now.second}"

def filename_timestamp():
	now = datetime.datetime.now()
	return f"{now.month}-{now.day}-{now.hour}-{now.minute}"

def log_debug(message, source='', display=True):
	print(f"(DEBUG){timestamp()}{source} -- {message}")
	logging.debug(message)

def config_log():
	logging.basicConfig(filename=f"logs/studio-{filename_timestamp()}.log", level=logging.DEBUG,
		format='%(asctime)s - %(message)s')

def log_info(message, source='', display=True):
	print(f"(INFO){timestamp()}{source} -- {message}")
	logging.info(message)

def log_warning(message, source='', display=True):
	if display:
		print(f"(WARNING){timestamp()}{source} -- {message}")
	logging.warning(message)

def log_durations(message, source='', display=True):
	print(f"(DURATIONS){timestamp()}{source} -- {message}")
	logging.info(f"DURATIONS: {message}")

def log_pitches(message, source='', display=True):
	print(f"(PITCHES){timestamp()}{source} -- {message}")
	logging.info(f"PITCHES: {message}")
	
def log_studio(message, source='', display=True):
	print(f"(STUDIO){timestamp()}{source} -- {message}")
	logging.info(f"STUDIO: {message}")
	

config_log()
