import logging

logging.basicConfig(level=logging.INFO,
                    filename="app.log",
                    format="%(asctime)s-%(levelname)s-(message)s")

logging.info("Program started")
logging.warning("This is warning")
logging.error("Something went wrong")