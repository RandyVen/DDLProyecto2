#file to test

import collections
EPSILON = 'ε'
class Automata:
     def __init__(self, exp):
        self.id = exp 
        self.states = []

class State: 
   def __init__(self,num):
     self.id = num
     self.transitions = []
     self.accept = False 

class Transition: 
  def __init__(self,sym,to):
        self.symbol = sym
        self.to = to

def is_in_language(automata, expresion):
  if expresion == ' ' or expresion == '':
      expresion = EPSILON
  actual = [0]
  actual = cerradura(automata, actual)
  i = 0
  while True:
      temp = []
      for num in actual:
          for transition in automata.states[num].transitions:
              if transition.symbol == expresion[i] and transition.to not in temp:
                  temp.append(transition.to)
      i += 1
      temp = cerradura(automata, temp)
      if not temp and expresion == EPSILON:
          break
      actual = temp.copy()
      if i > len(expresion)-1:
          break
  for id in actual:
      if automata.states[id].accept:
          return True
  return False

def cerradura(automata, actual):
  for num in actual:
      for transition in automata.states[num].transitions:
          if transition.symbol == EPSILON and transition.to not in actual:
              actual.append(transition.to)
  return actual

def read_word(file, actual):
  temp_word = ''
  while actual < len(file):
      if(file[actual] == ' ' or file[actual] == '\n') and (len(temp_word)>0):
          break
      elif file[actual] == ' ' or file[actual] == '\n':
          actual += 1
      else:
          temp_word += file[actual]
          actual += 1
  return temp_word, actual

def word_break(file, automata0, actual = 0):
  temp = ''
  validos = []
  while actual < len(file):
      temp += file[actual]
      if is_in_language(automata0, temp):
          validos.append(temp)
      actual += 1
  if validos:
      return max(validos, key = len)
  return False
def main():
  automatas = []
  automata0 = Automata("completo")
  temp_node= State(0)
  temp_transition = Transition('i', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('f', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('a', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('b', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('c', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('d', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('e', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('g', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('h', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('0', 3)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('1', 3)
  temp_node.transitions.append(temp_transition)
  automata0.states.append(temp_node)
  temp_node= State(1)
  temp_node.accept = True
  temp_transition = Transition('i', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('f', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('a', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('b', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('c', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('d', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('e', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('g', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('h', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('0', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('1', 2)
  temp_node.transitions.append(temp_transition)
  automata0.states.append(temp_node)
  temp_node= State(2)
  temp_node.accept = True
  temp_transition = Transition('i', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('f', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('a', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('b', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('c', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('d', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('e', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('g', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('h', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('0', 2)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('1', 2)
  temp_node.transitions.append(temp_transition)
  automata0.states.append(temp_node)
  temp_node= State(3)
  temp_node.accept = True
  temp_transition = Transition('0', 3)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('1', 3)
  temp_node.transitions.append(temp_transition)
  automata0.states.append(temp_node)
  automatas.append(automata0)

  automata1 = Automata("if")
  temp_node= State(0)
  temp_transition = Transition('i', 1)
  temp_node.transitions.append(temp_transition)
  automata1.states.append(temp_node)
  temp_node= State(1)
  temp_transition = Transition('f', 2)
  temp_node.transitions.append(temp_transition)
  automata1.states.append(temp_node)
  temp_node= State(2)
  temp_node.accept = True
  automata1.states.append(temp_node)
  automatas.append(automata1)

  automata2 = Automata("id")
  temp_node= State(0)
  temp_transition = Transition('a', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('b', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('c', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('d', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('e', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('f', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('g', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('h', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('i', 1)
  temp_node.transitions.append(temp_transition)
  automata2.states.append(temp_node)
  temp_node= State(1)
  temp_node.accept = True
  temp_transition = Transition('a', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('b', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('c', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('d', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('e', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('f', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('g', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('h', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('i', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('0', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('1', 1)
  temp_node.transitions.append(temp_transition)
  automata2.states.append(temp_node)
  automatas.append(automata2)

  automata3 = Automata("numero")
  temp_node= State(0)
  temp_transition = Transition('0', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('1', 1)
  temp_node.transitions.append(temp_transition)
  automata3.states.append(temp_node)
  temp_node= State(1)
  temp_node.accept = True
  temp_transition = Transition('0', 1)
  temp_node.transitions.append(temp_transition)
  temp_transition = Transition('1', 1)
  temp_node.transitions.append(temp_transition)
  automata3.states.append(temp_node)
  automatas.append(automata3)

  print('archivo a revisar?')
  archivo = input()
  prueba = open('./test/'+archivo)
  data = prueba.read()
  prueba.close()
  i = 0
  last = 0
  while i < len(data):
      valid = word_break(data, automata0, i)
      if valid:
          if last != 0 and (i - last > 0):
              while last < i:
                  print(data[last], end='')
                  last += 1
              print(': False')
          last += len(valid)
          aut = 1
          while aut<len(automatas):
              if (is_in_language(automatas[aut], valid)):
                  if 'í' in valid:
                    valid = valid.replace('í', 'CHR(')
                  elif 'ó' in valid:
                    valid = valid.replace('ó', '(.')
                  elif 'ú' in valid:
                    valid = valid.replace('ú', '.)')
                  print(valid, ': ', automatas[aut].id)
                  break
              aut += 1
          i += len(valid)
      else:
          i+=1
if __name__ == "__main__":
   main()