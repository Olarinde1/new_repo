import os
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory
  cwd = os.getcwd()
  above = os.chdir("..")
  new_cd = os.getcwd() 
  relative_parent = os.path.join(cwd, new_cd)

  # Return the absolute path of the parent directory
  return relative_parent

print(parent_directory())
print(os.getcwd())