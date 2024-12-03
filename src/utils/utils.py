import time, pyautogui , random, re, shutil, os, stat, platform, json
from pathlib import Path


def Sleeping(timer):
    return time.sleep(timer)

def CreateFolder(name):
    if os.name == 'nt':  # Windows
        folder = Path("C:/") / name
    else:  # Linux ou Mac
        folder = Path.home() / "Downloads" / name
    if not folder.exists():
        folder.mkdir(parents=True)
        print(f"Folder '{folder}' pasta download criada com sucesso!")
    else:
        print(f"a pasta '{folder}' já existe.")
    
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

def DeleteDriverFolder():
    full_path = os.path.join(os.path.expanduser("~"), ".wdm")

    def HandleRemoveReadonly(exc_type, exc_value, exc_traceback):
        if isinstance(exc_value, PermissionError):
            path = exc_value.filename
            os.chmod(path, stat.S_IWRITE)
            os.remove(path)
        else:
            raise exc_value

    try:
        shutil.rmtree(full_path, onexc=HandleRemoveReadonly)
        print(f"Pasta '{full_path}' removida com sucesso!")
    except FileNotFoundError:
        print(f"A pasta '{full_path}' não existe.")
    except PermissionError:
        print(f"Permissão negada para remover a pasta '{full_path}'.")
    except Exception as e:
        print(f"Ocorreu um erro ao tentar remover a pasta: {e}")

def ModifyChromedriverPath():
    user_home = os.path.expanduser("~")
    wdm_dir = os.path.join(user_home, ".wdm")

    drivers_json_path = os.path.join(wdm_dir, "drivers.json")

    if not os.path.exists(drivers_json_path):
        print(f"Arquivo {drivers_json_path} não encontrado.")
        return

    with open(drivers_json_path, "r", encoding="utf-8") as file:
        drivers_data = json.load(file)

    modified = False
    for driver in drivers_data.get('drivers', []):
        if driver.get('name') == 'chromedriver':
            old_path = driver.get('binary_path', '')
            new_path = old_path.replace('THIRD_PARTY_NOTICES.chromedriver', 'chromedriver')
            driver['binary_path'] = new_path
            print(f"Caminho do driver modificado de {old_path} para {new_path}")
            modified = True

    if modified:
        with open(drivers_json_path, "w", encoding="utf-8") as file:
            json.dump(drivers_data, file, indent=4)

        if platform.system() != 'Windows':
            try:
                if os.path.exists(new_path):
                    os.chmod(new_path, 0o755)
                    print(f"Permissões de execução definidas para {new_path}")
                else:
                    print(f"Caminho {new_path} não encontrado para ajustar permissões.")
            except Exception as e:
                print(f"Erro ao definir permissões: {e}")
    else:
        print("Nenhuma modificação foi necessária no arquivo JSON.")