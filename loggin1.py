import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Program started")
logging.warning("Low memory")
logging.error("File not found")