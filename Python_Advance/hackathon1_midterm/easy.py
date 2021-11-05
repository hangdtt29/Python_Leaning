# 1
import re
from datetime import datetime

def day_diff(release_date, code_complete_day):
    date_release = datetime.strptime(release_date, '%d/%m/%Y').date()
    date_code_complete = datetime.strptime(code_complete_day, '%Y-%d-%m').date()
    day_diff = date_release - date_code_complete
    return day_diff.days

# 2
def alpha_num(sentence):
    pattern = '[a-zA-Z]+[0-9]+'
    match = re.findall(pattern, sentence) 
    return match
    