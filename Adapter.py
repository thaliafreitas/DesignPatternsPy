
class Bird:
    def fly(self): pass
    def makeSound(self): pass

class Sparrow(Bird):
    def fly(self):
      return 1

	def makeSound(self):
      return print("This is a sparrow bird")


class ToyDuck:
    def squeak(self): pass


class PlasticToyDuck(ToyDuck):
    def squeak(self):
      return 0

class BirdAdapter:
   __bird = None

   def __init__(self, bird):
	    self.__bird = bird
   
   def isSqueak(self):
      if self.__bird.fly() < 1:
          print ("This bird doesn't fly")
      else:
          if self.__bird.makeSound() == 1
            print ("This is a sparrow bird")
          else:
            print ("No bird.")

def main():
   # Plug in
   bird = Bird()
   
	
if __name__ == "__main__":
   main()