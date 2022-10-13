#%%
import re
text = '.system.name    "n8fib01"'
print(re.search('"(.*)"', text).group(1))
# %%
import os, re

eth = os.popen("ipconfig").read()
print(eth)
print("Ethernet" in eth)
# %%
