from unittest import result
import decisions

print('Please Rate Faculty 0.0-10')
    options = float(input('Enter Faculty Rating:'))
    total = int(input('Enter 10 for TOTAL'))

    result = decisions.get_options_ratio(options, total)
    if(options < 0.0 or options > 10.0):
            print('Invalid Entry')