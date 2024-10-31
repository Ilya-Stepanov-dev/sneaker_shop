from abc import ABC, abstractmethod

class ABCRepository(ABC):

    @abstractmethod
    async def create_one():
        raise NotImplementedError
    
    @abstractmethod
    async def find():
        raise NotImplementedError
    

