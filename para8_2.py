import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="logs_p81.log",
                    filemode="w",
                    format="WE have logging message:%(asctime)s:%(levelname)S - %(message)s")



try:
    print(10/0)
except Exception:
    logging.exception("Exception")