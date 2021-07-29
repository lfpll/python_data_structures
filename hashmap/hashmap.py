from sympy import nextprime

class Item:
    
    def __init__(self, key, value) -> None:
        self.key   = key
        self.value = value

class HashTable:

    def __init__(self) -> None:
        self.map = []
        self.size = 0

    # modulos of hash
    def __hash_func(self,key: str,mod:int = 1039) -> int:    
        return sum([(ord(w) % mod) for w in key])

    def __is_in(self,index: int, in_list):
        try:

            return in_list[index]
        except IndexError:
            return False

    def __get_index(self,key:str):
        hash1 = self.__hash_func(key,mod=1039)
        hash2 = self.__hash_func(key,mod=27)
        return hash1+hash2,hash2 

    def __grow_array(self,new_min_size:int):
        tmp = [None] * nextprime(new_min_size)
        for x in range(self.size):
            tmp[x] = self.map[x]
        self.map = tmp
        
    def search(self,key:str):
        index,hash2 = self.__get_index(key)
        value = None
        while self.__is_in(index,self.map):
            if self.map[index][0] == key:
                value = self.map[index][1]
                break
            index = index * hash2    

        return value

    def insert(self,key:str,value):
        index,hash2 = self.__get_index(key)

        # Gettig not used index
        while self.__is_in(index,self.map):
            index = index * hash2
        
        # Growing array if index bigger then size
        if self.size < index:
            self.__grow_array(new_min_size=index)
            self.size = index

        self.map[index] = (key,value)

    def delete(self,key:str):
        index,hash2 = self.__get_index(key)

        while self.__is_in(index,self.map) and  self.map[index][0] != key:
            index = index * hash2  

        self.map[index] = None