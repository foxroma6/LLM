## package imports
import os
import sys
import time
import pandas as pd
import numpy as np
from gpt4all import GPT4All

## model imports
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")
model.open()

with model.chat_session():
    print(model.generate("How can I run LLMs efficiently on my laptop?", max_tokens=1024))