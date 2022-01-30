import logging
import logging.config
from pathlib import Path
from os import path
from helloworld import helloworld

LOGGING_CONF = "logging.conf"

if __name__ == "__main__":
    conf_dir = path.join(Path(__file__).parent.absolute().parent.absolute(), "conf")
    logging_conf = path.join(conf_dir, LOGGING_CONF)
    logging.config.fileConfig(logging_conf, disable_existing_loggers=False)
    helloworld.main()