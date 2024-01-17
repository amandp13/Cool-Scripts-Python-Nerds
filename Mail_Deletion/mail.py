#python script to delete mail with certain keywords in subject
import win32com.client
import re
import os, sys, logging
from datetime import datetime, timedelta

#timestr = time.strftime("%Y%m%d-%H%M%S")
#logFileName = 'C:\dev\Mail_deleter_log_' + timestr + '.log'
#logFileName = 'C:\dev\Mail_deleter_log.log'

"""Set of keywords to look for in the subject
--------------------------- Input goes here ---------------------------"""
keywords = { }

from_IDs = { }

keywords_string = '|'.join(keywords)

# Create a regular expression pattern for keywords
pattern = re.compile(rf'{keywords_string}', re.IGNORECASE)

def setup_outlook_instance(logger_type):
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)
    messages = inbox.Items
    logger_type.info("Connected to and created a outlook instance, all mails have been retrived!")
    return messages

def setup_logger(filename):
    print(f"Setting up logger for {str(filename)}")
    logger = logging.getLogger(filename)
    logger.setLevel(logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d in function %(funcName)s] %(message)s')
    
    file_handler = logging.FileHandler(filename)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger

def just_delete(mails, logger_type):
    print(f"Started execution of just_delete")
    for mail in mails:
        logger_type.info(f"Deleting : {str(mail.ReceivedTime)} {str(mail.Subject)}")
        mail.Delete()

def sender_delete():
    try:
        print(f"Started execution of sender_delete")
        sender_logger = setup_logger('C:\dev\sender_log.log')
        messages = setup_outlook_instance(sender_logger)

        for from_id in from_IDs:
            filter = "[SenderEmailAddress] = " + str(from_id)
            truncated_mails = messages.Restrict(filter)
            n = len(truncated_mails)
            if n > 0:
                sender_logger.info(f"Deleting mails from {str(from_id)}, around {str(n)} mails are there")
                just_delete(truncated_mails, sender_logger)
            else:
                sender_logger.info(f"NO mails from {str(from_id)}")
        sender_logger.info("Completed checking and deleting mails from specified senders!")
        sender_logger.info('--------------------------------- END of sender_delete ---------------------------------\n')
    except Exception as e:
        exception_type, exception_object, exception_traceback = sys.exc_info()
        filename = os.path.split(exception_traceback.tb_frame.f_code.co_filename)[1]
        sender_logger.info(f"{str(e)} {exception_type} {filename}, Line {exception_traceback.tb_lineno}")
        sender_logger.info('--------------------------------- END of sender_delete ---------------------------------\n')
        exit()

def process_mails():
    try:
        print(f"Started execution of process_mails")
        process_mails_logger = setup_logger('C:\dev\process_mails_log.log')
        messages = setup_outlook_instance(process_mails_logger)
        filterStr = "@SQL=""urn:schemas:httpmail:subject"" like '% " & keywords_string & " %'"
        messages = messages.Restrict(filterStr)
        n = len(messages)
        process_mails_logger.info(f"number of mails to be deleted are {str(n)}")
        just_delete(messages, process_mails_logger)
        process_mails_logger.info(f"DELETED {str(n)} mails")

        process_mails_logger.info(f"Completed Deleting mails with subject having {str(keywords_string)} !")
        process_mails_logger.info('--------------------------------- END of process_mails ---------------------------------\n')
    
    except Exception as e:
        exception_type, exception_object, exception_traceback = sys.exc_info()
        filename = os.path.split(exception_traceback.tb_frame.f_code.co_filename)[1]
        process_mails_logger.info(f"{str(e)} {exception_type} {filename}, Line {exception_traceback.tb_lineno}")
        process_mails_logger.info('--------------------------------- END of process_mails ---------------------------------\n')

if __name__ == "__main__":
    try:
        main_logger = setup_logger('C:\dev\main_log.log')
        main_logger.info("Starting the mail deletion process")

        # Start the processes
        main_logger.info('Started sender_process')
        sender_delete()
        main_logger.info('Completed sender_process!')

        main_logger.info('Started process_mails_process')
        process_mails()
        main_logger.info('Completed process_mails_process!')

        main_logger.info("All functions have completed")
    except KeyboardInterrupt:
        main_logger.info('Script terminated by user')
        main_logger.info('--------------------------------- END ---------------------------------\n')
    except Exception as e:
        exception_type, exception_object, exception_traceback = sys.exc_info()
        filename = os.path.split(exception_traceback.tb_frame.f_code.co_filename)[1]
        main_logger.info(f"{str(e)} {exception_type} {filename}, Line {exception_traceback.tb_lineno}")
        main_logger.info('--------------------------------- END ---------------------------------\n')