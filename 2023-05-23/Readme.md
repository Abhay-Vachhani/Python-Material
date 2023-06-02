# Random, Accessing of binary files using mmap

- The full form of mmap is 'MemoryMappedFile'

- Once a binary file is created with some data, that data is viewed as strings and it can be manipulated using mmap module

- The mmap can be used as

```python
    mm = mmap.mmap(fp.fileno(), 0)
```

- This will map the currently opened file 'fp' with the file object 'mm'

- The 'fp' represents the actual binary file that is being mapped

- The second argument is zero(0), it means the whole file should be considered for mapping

# Zipping the contents of files
