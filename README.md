# C++ Bootstrap template

This template serves as the base to create projects using C++ programming language.

## Software List

| Software | Operational System |
| -------- | --------------------- |
| GCC 13.x | Windows |
| MS Visual Studio Code* | Windows |
| Python 3.x | Windows |
| CMake 3.20+ | Windows |

<sub>\* To use <strong>Visual Studio Code</strong>, it is essential to have the <strong>C/C++ Extension Pack</strong> installed, along with a <strong>C++ compiler</strong> configured and added to the operating system's <strong>environment variables.</strong></sub>

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

## Custom dependencies

Through the `External/dependencies.json` file, it is possible to register dependencies that will be automatically cloned during the configuration process. This file offers a convenient way to manage and incorporate external libraries required for your project development.

```
"dependencies": [
    {
        "name": "...",
        "source": {
            "type": "git",
            "url": "...",
            "version": "..."
        }
    },
]
```
