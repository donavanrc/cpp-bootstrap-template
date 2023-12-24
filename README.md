# C++ Bootstrap template

This template serves as the base to create C++ projects.

## Project build - Visual Studio:

```
mkdir build
cd build
cmake .. -G "Visual Studio 17 2022" -A x64
```

## Project build - Visual Studio Code:

Right-click on `CMakeLists.txt` in the root directory and select the <strong>Configure All Projects</strong> option.

Ensure that the <strong>C++ Extension Pack</strong> is installed to complete this task.

## Dependencies download

Dependencies are downloaded when building the project automatically using CMake, but you can do this task individually by running the `python setup.py` command.