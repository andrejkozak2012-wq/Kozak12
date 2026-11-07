import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="logs_p81.log",
                    filemode="w",
                    format="WE have logging message:%(asctime)s:%(levelname)S - %(message)s")



logging.debug("debug")
logging.info("warning")
logging.error("error")
logging.critical("critical")
logging.info("info")

