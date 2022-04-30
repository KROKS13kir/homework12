import logging

#файл с логированием

logger = logging.getLogger()
logger.setLevel(logging.INFO)
LOG_FOLDER = "./log"
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler(f"{LOG_FOLDER}/log.log", "w", "utf-8")
file_formatter = logging.Formatter("%(levelname)s : %(asctime)s : %(message)s")
file_handler.setFormatter(file_formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)
