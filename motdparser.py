def nospace(sstring):
    return sstring.strip()

def create_task(command):
    """
    first argument name
    -de - description non required
    -cd - create_date defeault now
    -ttd - time to do
    -v - value
    """
    command = nospace(command)

    if not command[0].isalpha():
        error_command(2)
    print('Create Task')
    
def update_task():
    print('Again Task')
    
def done_task():
    print('OK Task')
    
def delete_task():
    print('Bye Task')

def error_command(error_code):
    if error_code == 1:
        print('command need -c or -u or -do or -d')
    if error_code == 2:
        print('invalid task\'s name')
    
def command_parse(command):
    """
    -c - create
    -u - update
    -d - delete
    -do - done
    """
    command = nospace(command)
    
    if command.startswith('-c '):
        create_task(command[2:])
    elif command.startswith('-u '):
        update_task()
    elif command.startswith('-do '):
        done_task()
    elif command.startswith('-d '):
        delete_task()
    else:
        error_command(1)

