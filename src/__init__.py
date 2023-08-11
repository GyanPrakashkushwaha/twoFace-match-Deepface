import os
import sys
import logging
from datetime import datetime

class NonEmptyLogFilter(logging.Filter):
    def filter(self, record):
        return bool(record.getMessage().strip())  # Check if the log message is non-empty

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir, f"{datetime.now():%d_%m_%H_%M_%S}.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("ProjectLogger")

# Add a custom filter to prevent empty log messages from being saved
non_empty_filter = NonEmptyLogFilter()
logger.addFilter(non_empty_filter)



class CustomException(Exception):

    def msg_detail(self,error,error_details:sys):
        _,_,exc_tb = error_details.exc_info()

        file_name = exc_tb.tb_frame.f_code.co_filename
        error_msg = f"Error occured in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{str(error)}]"

        return error_msg 
    
    def __init__(self, error_msg,error_detail:sys):
        super().__init__(error_msg)
        self.error_msg = self.msg_detail(error=error_msg,error_details=error_detail)

    def __str__(self):
        return self.error_msg
