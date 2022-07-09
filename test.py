import logging
logging.basicConfig(filename="test1.log" ,level = logging.INFO)
logging.info("thsi is my very first code for logging ")
logging.warning("thsi will try to load a warning message")
logging.error("this is a error message form system ")
l = [1,2,3,4,5,6,7,7]
for i in l :
    if i == 2 :
        logging.info(l)
        logging.warning("this is a wartning for a user that they have found out 2 in list ")

logging.shutdown()

