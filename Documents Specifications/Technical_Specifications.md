# Technical Specifications


<details><summary><b>Table of Contents</b></summary>

- [Technical Specifications](#technical-specifications)
- [1. Introduction](#1-introduction)
  - [a. Context](#a-context)
  - [b. Goal](#b-goal)
  - [c. General Description](#c-general-description)
  - [d. Team Members](#d-team-members)
- [2. Solutions](#2-solutions)
  - [a. Existing Solutions](#a-existing-solutions)
  - [b. Current Solution](#b-current-solution)
  - [c. Proposed Solution](#c-proposed-solution)
- [3. Folder Structure](#3-folder-structure)
  - [a. Before the project](#a-before-the-project)
  - [b. After the project](#b-after-the-project)
- [4. Implementation](#4-implementation)
- [5. Considerations](#5-considerations)
- [6. Ressources](#6-ressources)
  - [a. References](#a-references)
  - [b. Glossary](#b-glossary)
  
</details>

# 1. Introduction

[HARFANG](https://www.harfang3d.com/en_US/framework) is a real-time 3D engine open-source and available on GitHub, developed by [HARFANG3D](https://www.harfang3d.com/en_US/). It is written in C++ and is based on the open-source [bgfx](https://github.com/bkaradzic/bgfx) library supporting Vulkan, Metal, DirectX, OpenGL and OpenGL ES.
## a. Context

[FABGen](https://github.com/ejulien/FABGen/) (a set of Python scripts to generate C++ binding code to different languages) is used to generate binding for HARFANG and currently supports the following target languages: CPython 3.2+, Lua and Go 1.11+. 

For more details, please take a look at the [Functional Specifications](https://github.com/algosup/2022-2023-project-3-harfang3d-binding-Project-1-group/blob/main/Documents%20Specifications/Functional_Specifications.md).
## b. Goal

The goal of the project is to provide a F# binding for HARFANG.

 ## c. General Description
| Project | Client | Author | Created on | Last update |
|:---|:---|:---|:---|:---|
| 2023 Project 3 - Harfang3D Binding Group 1 | [HARFANG3D](https://github.com/harfang3d/harfang3d)  | [Nicolas MIDA](https://github.com/Nicolas-Mida) | 2022-01-03 | 2022-01-17 |

&nbsp;
## d. Team Members

| Role | Name |  
|:---|:---|
| Project Manager | [Élise GAUTIER](https://github.com/elisegtr) |
| Tech Lead | [Nicolas MIDA](https://github.com/Nicolas-Mida) |
| Quality Assurance (QA) | [Théo TROUVÉ](https://github.com/TheoTr/) |
| Software Engineer | [Grégory PAGNOUX](https://github.com/Gregory-Pagnoux) |
| Program Manager | [Rémy CHARLES](https://github.com/RemyCHARLES) |


&nbsp;

# 2. Solutions

## a. Existing Solutions

SWIG (Simplified Wrapper and Interface Generator) is a software development tool that connects programs written in C and C++ with a variety of high-level programming languages.

However SWIG has different issues 

  - It is a very old and complex codebase. Language support is written partially in C and SWIG interface files 
which are almost a language by themselves. The C codebase does everything through a single 
Object struct hiding the real type of variables making it extremely difficult to debug and extend the 
SWIG core. 
  
  - Uneven feature support between languages with missing features although the target language 
could support them

## b. Current Solution 

FABGen is a set of Python scripts to generate C++ binding code to different languages. It is used to generate binding for HARFANG and currently supports the following target languages: CPython 3.2+, Lua and Go 1.11+.

FABgen tries to solve the issues of SWIG by:

 - Using Python to implement Fabgen and the binding definitions themselves.
 - Implementing as much as possible of the features in a common part of the program (gen.py).

## c. Proposed Solution

As mentioned above, the main goal of the project is to provide a F# binding for HARFANG.

What is F# ? 
  - JIT (Just-In-Time) from IL (Intermediate Language) to native code
  - Statically typed
  - Link to C library (C++ has to be wrapped with C first)

# 3. Folder Structure

## a. Before the project

Here is what the FABGen folder structure currently looks like:

```
├───FABGen-master
│   ├─── .travis
│   ├─── .vscode
│   ├─── examples
│   ├─── lang
│   │     ├─── __init__.py
│   │     ├─── cpython.py
│   │     ├─── go.py
│   │     ├─── lua.py
│   │     └─── xml.py
│   ├─── lib
│   │     ├── cpython
│   │     │     ├── __init__.py
│   │     │     ├── std.py
│   │     │     └─── stl.py
│   │     ├─── go
│   │     │     ├── WrapperConverter.go_
│   │     │     ├── __init__.py 
│   │     │     ├── std.py
│   │     │     └─── stl.py
│   │     ├─── lua
│   │     │     ├── __init__.py
│   │     │     ├── std.py
│   │     │     └─── stl.py
│   │     ├─── xml
│   │     │      └─── stl.py
│   │     │
│   │     ├─── __init__.py
│   │     ├─── std.py
│   │     └─── stl.py
│   ├─── tests
│   │     └─── All the tests.py
│   ├─── bind.py
│   ├─── gen.py
│   ├─── requirements.txt
│   ├─── test.py

```

As you can see, not all the folders are used for the project. The main folders that will be used are:

  - lang
  - lib
  - tests

To provide a F# binding for HARFANG, we will have to create a new folder in the lang and lib folders.

We also need to implement the F# binding in several files such as: bind.py, gen.py and test.py.

## b. After the project

Here is what the FABGen folder structure will look like:

```
├───FABGen-master
│   ├─── .travis
│   ├─── .vscode
│   ├─── examples
│   ├─── lang
│   │     ├─── __init__.py
│   │     ├─── cpython.py
│   │     ├─── go.py
│   │     ├─── lua.py
│   │     ├─── **fsharp.py (New File) **
│   │     └─── xml.py
│   ├─── lib
│   │     ├── cpython
│   │     │     ├── __init__.py
│   │     │     ├── std.py
│   │     │     └─── stl.py
│   │     ├─── go
│   │     │     ├── WrapperConverter.go_
│   │     │     ├── __init__.py 
│   │     │     ├── std.py
│   │     │     └─── stl.py
│   │     ├─── lua
│   │     │     ├── __init__.py
│   │     │     ├── std.py
│   │     │     └─── stl.py
│   │     ├── **fsharp (New Folder)**
│   │     │     ├── __init__.py
│   │     │     ├── std.py
│   │     │     └─── stl.py **
│   │     ├─── xml
│   │     │      └─── stl.py
│   │     │
│   │     ├─── __init__.py
│   │     ├─── std.py
│   │     └─── stl.py
│   ├─── tests
│   │     └─── All the tests.py
│   ├─── **bind.py ** (Edited)
│   ├─── **gen.py ** (Edited)
│   ├─── requirements.txt
│   ├─── **test.py ** (Edited)

```

# 4. Implementation
 WIP
# 5. Considerations
WIP
# 6. Ressources
## a. References

[1] [Harfang3D Website](https://www.harfang3d.com/en_US/)  
[2] [FABGen](https://github.com/ejulien/FABGen/)  
[3] [Harfang API Documentation](https://dev.harfang3d.com/docs/2.0.111/man.overview/)  
[4] [Harfang GitHub](https://github.com/harfang3d/harfang3d)

## b. Glossary

| Term | Acronym | Definition |
|:---|:---:|:---|
| HARFANG3D | - | HARFANG3D is a company that develops HARFANG |
| HARFANG | - | HARFANG is a real-time 3D engine |
| FABGen | - | FABGen is a set of Python scripts to generate C++ binding code to different languages. |
| F# | F Sharp | F# is a functional programming language |
| C++ | C Plus Plus | C++ is a programming language |
| Lua | - | Lua is a programming language |
| Go | - | Go is a programming language |
| CPython | - | CPython is an open-source, cross-platform, high-level programming language. |
| API | Application Programming Interface | An API is a set of functions and procedures allowing the creation of applications that access the features or data of an operating system, application, or other service. |
| Binding | - | A binding is a link between two things. |
| bgfx | - | bgfx is a cross-platform, graphics API agnostic, "Bring Your Own Engine/Framework" style rendering library. |
| Vulkan | - | Vulkan is a low-overhead, cross-platform 3D graphics and compute API. |
| Metal | - | Metal is a low-overhead, cross-platform 3D graphics and compute API. |
| DirectX | - | DirectX is a set of APIs for handling tasks related to multimedia, especially game programming and video, on Microsoft platforms. |
| OpenGL | - | OpenGL is a cross-language, cross-platform application programming interface for rendering 2D and 3D vector graphics. |
| OpenGL ES | - | OpenGL ES is a cross-platform, royalty-free, standard API for rendering 2D and 3D graphics. |
| SWIG | Simplified Wrapper and Interface Generator | SWIG is a software development tool that connects programs written in C and C++ with a variety of high-level programming languages. |
| JIT | Just-In-Time | JIT is a compilation technique in which the source code is compiled into machine code at run time. |
| IL | Intermediate Language | IL is a stack-based instruction set that is used by the Common Language Infrastructure (CLI). |
| CLI | Common Language Infrastructure | CLI is a specification that describes the runtime environment in which .NET Framework applications execute. |
| Wrapper | - | A wrapper is a software component that encapsulates the interactions with an operating system or library. |
