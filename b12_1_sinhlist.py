import random
import numpy as np
n=random.randrange(50,1001)
print(n,' Là giải độc đắc của chương trình xổ số hôm nay!','\n')
a=list(np.random.randint(-1000,1000, size=n))
print('Chúc mừng các giải khuyến khích!')
print(a,'\n')
b=list(np.random.uniform(-1000,1000, size=n))
print('Chúc các bạn may mắn lần sau!')
print(b)
print('end')
