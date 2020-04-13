from os import system, name

def hang_graphics():
    """Graphs from https://gist.github.com/DevDarren/4199441"""
    yield """
    ________      
    |           
    |             
    |             
    |             
    |"""
    yield """
	________      
	|      |      
	|             
	|             
	|             
	|"""
    yield """
	________      
	|      |      
	|      0      
	|             
	|            
	|"""
    yield """
	________      
	|      |      
	|      0     
	|     /       
	|             
	|"""
    yield """
	________      
	|      |      
	|      0     
	|     /|       
	|             
	|"""
    yield """
	________      
	|      |      
	|      0      
	|     /|\     
	|             
	|"""
    yield """
	________      
	|      |      
	|      0      
	|     /|\     
	|     /       
	|"""
    yield """
	________      
	|      |      
	|      0      
	|     /|\     
	|     / \     
	|"""


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


if __name__ == '__main__':
    graphics = list(hang_graphics())
    print(len(graphics))