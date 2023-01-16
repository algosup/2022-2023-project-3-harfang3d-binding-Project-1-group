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
  - [d. Development of the solution](#d-development-of-the-solution)
- [Ressources](#ressources)
  - [References](#references)
  - [Glossary](#glossary)
  
</details>

# 1. Introduction

[HARFANG](https://www.harfang3d.com/en_US/framework) is a real-time 3D engine open-source and available on GitHub, developed by [HARFANG3D](https://www.harfang3d.com/en_US/). It is written in C++ and is based on the open-source [bgfx](https://github.com/bkaradzic/bgfx) library supporting Vulkan, Metal, DirectX, OpenGL and OpenGL ES.
## a. Context

[FABGen](https://github.com/ejulien/FABGen/) (a set of Python scripts to generate C++ binding code to different languages) is used to generate binding for HARFANG and currently supports the following target languages: CPython 3.2+, Lua and Go 1.11+. 

For more details, please take a look at the [Functional Specifications](functional_specifications.md).
## b. Goal

The goal of the project is to provide a F# binding for HARFANG using FABGen.

 ## c. General Description
| Project | Client | Author | Created on | Last update |
|:---|:---|:---|:---|:---|
| 2023 Project 3 - Harfang3D Binding Group 1 | [HARFANG3D](https://github.com/harfang3d/harfang3d)  | [Nicolas MIDA](https://github.com/Nicolas-Mida) | 2022-01-03 | 2022-01-09 |

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

## b. Current Solution 

FABGen is a set of Python scripts to generate C++ binding code to different languages. It is used to generate binding for HARFANG and currently supports the following target languages: CPython 3.2+, Lua and Go 1.11+.

## c. Proposed Solution

As mentioned above, our goal is to provide a F# binding for HARFANG using FABGen.

## d. Development of the solution

The development of the solution will be done in 3 steps:

1. **Generate the F# binding** 


2. **Test the F# binding**.


3. **Improve the F# binding**.


WIP


# Ressources
## References

[1] [Harfang3D Website](https://www.harfang3d.com/en_US/)  
[2] [FABGen](https://github.com/ejulien/FABGen/)  
[3] [Harfang API Documentation](https://dev.harfang3d.com/docs/2.0.111/man.overview/)  
[4] [Harfang GitHub](https://github.com/harfang3d/harfang3d)

## Glossary

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
