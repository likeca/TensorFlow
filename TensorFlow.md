# TensorFlow
https://web.stanford.edu/class/cs20si/  
https://github.com/chiphuyen/stanford-tensorflow-tutorials

# CPU Warning
The TensorFlow library wasn't compiled to use SSE4.2 instructions, but these are available on your machine and could speed up CPU computations.  
```
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
```
