from multiprocessing import Process, Lock,Semaphore

class Overview:
    def __init__(self, model, describe):
        self.model = model
        self.describe = describe
   
   
if "__name__" == "__main__":
        on: Overview = Overview('start',('overviewing system'))
        off: Overview = Overview('stop', ('script stoped'))
        
def func(p_lock, identifier):
    with p_lock:
        sleep(1)
        print(f'process {identifier} is running')
        
        
def main():
    lock = lcok()
    sem = Semaphore(3)
    
    prccoesses = [Process(target=func, args=(lock,i))  for i in range(5)]
    
    for process in prccoesses:
        process.start()
        
    for process in prccoesses:
        process.join()
def descripe(self):
        print(f'describe server status {self.model} ({self.describe})')

def turn_on(self):
       
        print( 'script started')
        if self == 'start':
            print('start scipt')
def turn_off(self):
        print('script stop')
    
def go_to(_select:int):
        print('go to {self._select}')



def start_overview(self):
   
   
    while textInput := input('start to start and stop to stop script: '):
        if textInput == 'start':
            turn_on("START Overview")
     
        elif textInput == 'stop':
            turn_off("stop script")
        elif textInput == '0':
            print('circle back')
        else:
            print('exit')
            break
        

print('print start to start and stop to stop: ')

start_overview('f{self.model}')