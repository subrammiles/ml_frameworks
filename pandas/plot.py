import pandas as pd
import matplotlib.pyplot as plt
data = {
  'marks': [30, 42, 32,20,10,22,49]
}
df = pd.DataFrame(data)
df.plot()
plt.show() 

