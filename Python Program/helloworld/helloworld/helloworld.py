import logging

name = "PINEAPPLEBUN"

def main():
    logger = logging.getLogger("dev")
    logger_root = logging.getLogger()
    logger.info("hello")
    logger.info("NAME IS %s", name)
    logger_root.info("DAMN NAME IS %s", name)