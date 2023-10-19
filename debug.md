## 出现原因
应该是原代码需要的依赖的版本与实际安装的版本不符（原代码应该较老），有些数据格式变了，函数也被弃用了，因此需要修改代码以适应新的依赖版本。

## 修改方式

- `utils.py`：在`process_csv`函数中的return前一行加上`df = df.astype('float64')`:
```py
   df = df.drop(columns = sensitive_attributes)
   df = df.astype('float64')
   return df
```
- `DP_run.py`:在`sim_dp`函数中做如下修改：
```python
# 修改前
# trained_model.load_state_dict(torch.load(os.path.join(best_trial.checkpoint.value, 'checkpoint')))
# 修改后
trained_model.load_state_dict(torch.load(os.path.join(best_trial.checkpoint.dir_or_data, 'checkpoint')))
# ...
# 修改前
# df = df.append(pd.DataFrame([result]))
# 修改后
df = pd.concat([df, pd.DataFrame([result])], ignore_index=True)
```