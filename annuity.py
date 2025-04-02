def nyu(i):
    return 1 / (1+i)

class Annuity:

    '''An annuity is a financial product or arrangement where a series of payments are made at regular intervals over a specified period of time.'''

    def __init__(self, i, n):
        self.i = i
        self.n = n

    def a_post(self):
        return (1-nyu(self.i)**self.n)/self.i
    
    def s_post(self):
        return self.a_post() * (1+self.i)**self.n

    def a_pre(self):
        return self.a_post() * (1+self.i)
    
    def s_pre(self):
        return self.a_pre() * (1+self.i)**self.n

    def Ia_unit_post(self):
        return (self.a_pre() - self.n*nyu(self.i)**self.n)/self.i
    
    def Ia_post(self, a, b):
        if self.n == 1:
            return a*nyu(self.i)
        return a*self.a_post() + b*Annuity(self.i, self.n - 1).Ia_unit_post()*nyu(self.i)
    
    def Is_unit_post(self):
        return (self.s_pre() - self.n)/self.i
    
    def Is_post(self, a, b):
        return self.Ia_post(a, b) * (1+self.i)**self.n 

    def Ia_unit_pre(self):
        return self.Ia_unit_post() * (1+self.i)

    def Ia_pre(self, a, b):
        if self.n == 1:
            return a
        return a*self.a_pre() + b*Annuity(self.i, self.n - 1).Ia_unit_pre()*nyu(self.i)
    
    def Is_unit_pre(self):
        return self.Is_unit_post() * (1+self.i)
        
    def Is_pre(self, a, b):
        return self.Ia_pre(self, a, b) * (1+self.i)**self.n 
    
    
    def __repr__(self):
        return f"Annuity(i={self.i}, n={self.n})"
    
    def __str__(self):
        interest_rate = int(self.i*100) if (self.i*100).is_integer() else self.i*100
        duration = int(self.n) if self.n.is_integer() else self.n
        return f"Annuity with an interest rate of {interest_rate}% and duration of {duration} years"

# examples
if __name__ == '__main__':
    # i = 0.12; n = 15. calculate the future value of a unit annuity (postnumerando)
    ann = Annuity(0.12, 15)
    print(f"Future value of {ann}: {ann.s_post()} \n")
    # i1 = 0.05, n1 = 12; i2 = 0.07, n2 = 8. calculate the present value of an arithmetically increasing (500, 550, 600, ...) annuity (prenumerando)
    x = Annuity(0.05, 12).Ia_pre(500, 50) + Annuity(0.07, 8).Ia_pre(500+50*12, 50)*nyu(0.05)**12
    print(x, '\n')
    # future value of an arithmetically increasing annuity
    print(Annuity(0.1, 2).Is_unit_post(), Annuity(0.1, 2).Is_post(1, 1))
