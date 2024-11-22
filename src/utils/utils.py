import time, pyautogui , random, re
from pathlib import Path
def Sleeping(timer):
    return time.sleep(timer)

def CreateFolder(name):
    folder = Path(f"C:/{name}")
    if not folder.exists():
        folder.mkdir(parents=True) 
        print(f"Folder '{folder}' created successfully!")
    else:
        return
    
def PressKeyTimes(x):
    count = 0
    while True:
        if count < x:
            pyautogui.hotkey('tab')
            count +=1
            Sleeping(2)
            continue
        break

def GenerateNumber():
    return random.randint(100000, 999999)

def ValidateCpf(cpf):
    
    format_cpf = re.sub(r'[^0-9]', '', str(cpf))
    
    if not len(format_cpf) == 11:
        return

    
    nums_cpf = []
    
    for num in format_cpf:
        nums_cpf.append(num)

    nums_cpf.pop()
    nums_cpf.pop()
    
    #primeiro digito    
    teen_digits_cpf = []
    first_digit = 0
    count = 10
    for num in nums_cpf:
        teen_digits_cpf.append(int(num)*count)
        count-=1

    for num in teen_digits_cpf:
        first_digit += num
        
    if 11 - (first_digit % 11) >= 10:
        first_digit = 0
    first_digit = 11 - (first_digit % 11)
    
    nums_cpf.append(first_digit)
    
    #segundo digito
    second_digit = 0
    count = 11
    eleven_digits_cpf = []
    for num in nums_cpf:
        eleven_digits_cpf.append(int(num) * count)
        count -= 1
    
    for num in eleven_digits_cpf:
        second_digit += num
    
            
    if 11 - (second_digit % 11) >= 10:
        second_digit = 0
    second_digit = 11 - (second_digit % 11)
    
    nums_cpf.append(second_digit)
    
    is_cpf = ''.join(map(str,nums_cpf)) == format_cpf

    return is_cpf
    

def ValidateDate(date):
    DATE = re.sub(r'[^0-9]', '', str(date))
    if len(DATE) > 8 or len(DATE) < 8:
        return False
    return True