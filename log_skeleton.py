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
	logging.basicConfig(filename=f"dojo_server{filename_timestamp()}.log", level=logging.DEBUG,
		format='%(asctime)s - %(message)s')

def log_info(message, source='', display=True):
	print(f"(INFO){timestamp()}{source} -- {message}")
	logging.info(message)

def log_warning(message, source='', display=True):
	if display:
		print(f"(WARNING){timestamp()}{source} -- {message}")
	logging.warning(message)

def log_network(message, source='', display=True):
	print(f"(NETWORK){timestamp()}{source} -- {message}")
	logging.info(f"NETWORK: {message}")

def log_server(message, source='', display=True):
	print(f"(SERVER-MESSAGE){timestamp()}{source}")
	logging.info(message)

def log_cards(message, source='', display=True):
	print(f"(CARDS){timestamp()}{source} -- {message}")
	logging.info("(CARDS)"+message)

def log_dojo(message, source='', display=True):
	print(f"(DOJO){timestamp()}{source} -- {message}")
	logging.info("(DOJO)"+message)



config_log()
