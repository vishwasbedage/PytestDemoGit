import inspect
import logging

class LogGenerator:
    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]  # Get the name of the function that called loggen()
        logger = logging.getLogger(name)  # Create a logger object with the caller's name
        logfile = logging.FileHandler(".\\Logs\\OrangeHRM_Log.log")  # Create a file handler to write logs to a file
        logformat = logging.Formatter("%(asctime)s : %(levelname)s :  %(name)s : %(funcName)s : %(lineno)d : %(message)s")  # Define the format for the log messages
        logfile.setFormatter(logformat)  # Set the defined format to the file handler
        logger.addHandler(logfile)  # Add the file handler to the logger
        logger.setLevel(logging.INFO)  # Set the logging level to INFO
        return logger  # Return the configured logger object


    ## debug Info Warnings error critical


