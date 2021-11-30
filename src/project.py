def hello():
  """ Returns "Hello, world!" """
  print('Hello, world!')
  return

def add_2(a):
  """ 
  Add 2 to a number 
  
  >>> add_2(3)
  5
  >>> add_2(5)
  7
  
  Parameters
  --------------
    a : int
      Number to add
      
  Returns
  ------------
    int, value a+2
  """
  return a+2

def is_even(val):
  """ 
  Returns True if the input number is even, False if it's odd 
  
  >>> is_even(4)
  True
  >>> is_even(17)
  False
  
  Parameters
  -------------
    val : int
      Number to evaluate
      
  Returns
  -------------
    boolean, True if val is even, False if val is odd
  """
  return val % 2 == 0
