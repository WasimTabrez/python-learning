# Logging Utility

from datetime import datetime


LOG_FILE = "application.log"


def write_log(message):

    with open(LOG_FILE, "a") as file:

        current_time = datetime.now()

        file.write(

            f"[{current_time}] {message}\n"

        )


def info(message):

    write_log(f"INFO : {message}")


def warning(message):

    write_log(f"WARNING : {message}")


def error(message):

    write_log(f"ERROR : {message}")
