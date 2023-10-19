## 使用conda搭建python环境
```shell
conda create --name fairness python=3.11.4 pip
conda activate fairness
pip install ray
pip install pandas
pip install torch
pip install tqdm
pip install scipy
pip install pyarrow
```

## 编写main程序
main.py:
```python
import sys, os
working_dir = '.'
sys.path.insert(1, os.path.join(working_dir, 'FedFB'))
os.environ["PYTHONPATH"] = os.path.join(working_dir, 'FedFB')

from DP_run import *

sim_dp('fedavg', 'logistic regression', 'synthetic')
```
## 将main.py放到README.md同级目录中，运行即可