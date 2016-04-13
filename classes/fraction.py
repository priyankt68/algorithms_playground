class Fraction():

    def __init__(self, numerator, denominator):
	self.numerator = numerator
	self.denominator = denominator


    def show(self):
        print(str(self.numerator) + "/" + str(self.denominator))

if __name__ == "__main__":

    # Here it's the fraction class' instance
    f = Fraction(2,3)
    print f

    f.show()

