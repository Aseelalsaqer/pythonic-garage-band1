class Musician:
    members = []

    def __init__(self, name):
        self.name = name
        Musician.members.append(self.name)

"""
    A class to represent a musician.
    Attributes
    ----------
    name : str
    members : list
   
    """
class Band(Musician):
    
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)
    def play_solos(self):
        solos_list = []
        solos_list.append(Guitarist.play_solo(self))
        solos_list.append(Bassist.play_solo(self))
        solos_list.append(Drummer.play_solo(self))
        return solos_list
    def __str__(self):
        return f'We are {self.name} and we are music band'
    def __repr__(self):
        return f'Band inctance. Name = {self.name}'
    @classmethod
    def to_list(cls):
        return cls.instances

"""
    A class to represent a Guitarist.
    Attributes
    ----------
    name : str
       
    INSTRUMENT : str
     
    """
class Guitarist(Musician):
    def __str__(self):
        return f'My name is {self.name} and I play guitar'
    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'
    def get_instrument(self):
        return 'guitar'
    def play_solo(self):
        return 'face melting guitar solo'

"""
    A class to represent a Bassist.
    Attributes
    ----------
    name : str
       
    INSTRUMENT : str
 
    """
class Bassist(Musician):
    def __str__(self):
        return f'My name is {self.name} and I play bass'
    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'
    def get_instrument(self):
        return 'bass'
    def play_solo(self):
        return 'bom bom buh bom'

"""
    A class to represent a Drummer.
    Attributes
    ----------
    name : str
      
    INSTRUMENT : str
      
    """

class Drummer(Musician):
    def __str__(self):
        return f'My name is {self.name} and I play drums'
    def __repr__(self):
       return f'Drummer instance. Name = {self.name}'
    def get_instrument(self):
        return 'drums'
    def play_solo(self):
        return 'rattle boom crash'        

 

