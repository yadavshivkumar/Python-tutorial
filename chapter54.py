class A: 
    label = "A : Base class"
    
class B(A):
    label = "B : Masala Blend"
    
class C(A):
    label = "C : Herbal Blend"
    
class D(B, C):
    pass

cup = D()
print(cup.label)  # Output: B : Masala Blend
print(D.__mro__)  # Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>       )

