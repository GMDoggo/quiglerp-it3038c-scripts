# Numpy
This is how you can run a Python script that I created, which uses a plugin called Numpy. 
First let's create a Virtual ENV called scripts. You can call it whatever you want
```python
C:\>python -m venv /venv/numpy
```
```Powershell
Powershell
PS C:\>  /venv/numpy/Scripts/activate.ps1
(numpy) PS C:\>
```
Once Activated goto Python
```python
python
import numpy as np
```
Basic Array
```python
>>> a = np.array([1, 2, 3, 4, 5, 6])
>>> print(a[0])
1
```
Sorting Elements
```python
>>> arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
>>> np.sort(arr)
array([1, 2, 3, 4, 5, 6, 7, 8])
```
Combining Arrays
```python
>>> a = np.array([1, 2, 3, 4])
>>> b = np.array([5, 6, 7, 8])
>>> np.concatenate((a, b))
array([1, 2, 3, 4, 5, 6, 7, 8])
```
Once done you can exit. Don't forget to deactivate your virtualenv when you're done.
```python
CTRL+Z (To Exit)
```
```powershell
(numpy) PS C:\> deactivate
PS C:\>
```
