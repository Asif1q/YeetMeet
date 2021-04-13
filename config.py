import os
class Config(object):
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    GUSERNAME = os.environ.get('GUSER_NAME')
    GPASSWORD = os.environ.get('GPASSWORD')
    SCHEDULE = os.environ.get('SCHEDULE', True)
    USERID = os.environ.get('USERID')
# If you're not familiar with how to set Environment Variables you can do like this instead
# of  setting Environment Variables

# BOT_TOKEN = os.environ.get('BOT_TOKEN', '1065989390:AAHzDBaNFujgq6f-sUPyqF0ZBZrX8mKlY9g')
# GUSERNAME = os.environ.get('GUSER_NAME', 'b17ee092@mace.ac.in ')
# GPASSWORD = os.environ.get('GPASSWORD', 'ma171@eee')

#NOTE: Putting sensitive information in files is considered unsafe. Try to use ENVIRONMENT VARIABLES 
