# utils
Compares two Directories

Installation: pip install git+https://github.com/adaikalaraj/utils.git

Usage:

  Commandline: dircompare </path/to/source> </path/to/destination>

  Module:

  from dircompare import FileCompare

  result = FileCompare('/path/to/source', '/path/to/destination')

  print(result.matched) # returns True if matched and False if not matched

  print(result.get_report()) # returns a detailed report
