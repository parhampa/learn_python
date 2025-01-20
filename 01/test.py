import numpy as np
import matplotlib.pyplot as plt

# ایجاد یک آرایه از اعداد
x = np.linspace(0, 10, 100)
y = np.sin(x)

# رسم نمودار
plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("X")
plt.ylabel("sin(X)")
plt.show()