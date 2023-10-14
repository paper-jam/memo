import random 
import logging 


logging.basicConfig(level=logging.DEBUG)

# setting logger handler and formatter
logger = logging.getLogger(__name__)

# format
FORMAT = '%(name)s:%(levelname)s:%(asctime)s -> %(message)s'
formatter = logging.Formatter(FORMAT)

# handler
handler = logging.FileHandler('prod_lab.log', mode='a')
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

logger.addHandler(handler )


print ('*****************************')



print(logger.handlers)


for _ in range(0,30) :

    # generate temp 
    temperature = random.randrange(0,40)
    print(f'generated temperature is {temperature}')

    match temperature:
        case _ if temperature < 20 :
            logger.debug('temperature is < 20 --> ' + str(temperature) )
        case _ if 30 <= temperature <= 35 :
            logger.warning('temperature is between 30 and 35 --> ' + str(temperature) )



# DEBUG = TEMPERATURE_IN_CELSIUS < 20
# WARNING = TEMPERATURE_IN_CELSIUS >= 30 AND TEMPERATURE_IN_CELSIUS <= 35
# CRITICAL = TEMPERATURE_IN_CELSIUS > 35
