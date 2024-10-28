class ChooseInMenu:
    
    __instance = ['sdfs'  , 'sdsds','sds']
    

       
    

    def __init__(self,selectedInMenu:int):
        """
        Initializer for ChooseInMenu class

        Args:
            selectedInMenu (int): number of menu to be opened

        Raises:
            ValueError: if selectedInMenu is None or negative
            TypeError: if selectedInMenu is not an integer
        """

        if selectedInMenu is None:
            raise ValueError("selectedInMenu cannot be None")
        if not isinstance(selectedInMenu, int):
            raise TypeError("selectedInMenu should be an integer")
        if selectedInMenu < 0:
            raise ValueError("selectedInMenu should be a positive integer")
        try:
            if not isinstance(selectedInMenu, int):
                raise TypeError("selectedInMenu should be an integer")
            if selectedInMenu < 0:
                raise ValueError("selectedInMenu should be a positive integer")
            self.selectedInMenu = selectedInMenu
            print(f'opening menu {selectedInMenu}')
        except Exception as e:
            print(f"An error occurred: {e}")
            raise
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)
        self.selectedInMenu = selectedInMenu
        print(f'opening menu {selectedInMenu}')
        
        def name(self):
       
            if self == 1: 
                print('selected tab menu')
            elif self == 2:
                print('selected someting')
            pass
       
        return print('2AS')      

        
        
        name(selectedInMenu)

  
class OverViewTab: 
    def __init__(self):
       return  print('opening Overview tab')
class SomethingSomethingTab:
       def __init__(self):
           
        print('opening something tab')
        
        
        
        
        
