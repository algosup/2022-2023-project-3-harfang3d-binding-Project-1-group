# Technical Specifications


<details><summary><b>Table of Contents</b></summary>

- [Technical Specifications](#technical-specifications)
- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [General Description](#general-description)
  - [Team Members](#team-members)
- [Sources](#sources)
  - [References](#references)
  - [Glossary](#glossary)
  

</details>
&nbsp;

# Introduction


## Purpose

Currently, the Harfang3D library is written in C++ and can be used in CPython, Lua and Go. The goal of this project is to create a binding to the Harfang3D library in F# so that the user can use the Harfang3D API in F#.

The binding will be done using [FABGen](https://github.com/ejulien/FABGen/), a tool to generate F# bindings from C++ headers. The binding will be done in a way that the user can use the Harfang3D API as if it was written in F#.

For more details, please look at the [Functional Specifications](functional_specifications.md).

&nbsp;
 ## General Description
| Project | Client | Author | Created on | Last update |
|:---|:---|:---|:---|:---|
| 2023 Project 3 - Harfang3D Binding Group 1 | [HARFANG3D](https://github.com/harfang3d/harfang3d)  | [Nicolas MIDA](https://github.com/Nicolas-Mida) | 2022-01-03 | 2022-01-04 |
&nbsp;
## Team Members

| Role | Name |  
|:---|:---|
| Project Manager | [Élise GAUTIER](https://github.com/elisegtr) |
| Tech Lead | [Nicolas MIDA](https://github.com/Nicolas-Mida) |
| Quality Assurance (QA) | [Théo TROUVÉ](https://github.com/TheoTr/) |
| Software Engineer | [Grégory PAGNOUX](https://github.com/Gregory-Pagnoux) |
| Program Manager | [Rémy CHARLES](https://github.com/RemyCHARLES) |


&nbsp;
# Sources
## References

[1] [Harfang3D Website](https://www.harfang3d.com/en_US/)  
[2] [FABGen](https://github.com/ejulien/FABGen/)  
[3] [Harfang3D API Documentation](https://dev.harfang3d.com/docs/2.0.111/man.overview/)  
[4] [Harfang3D GitHub](https://github.com/harfang3d/harfang3d)

## Glossary

| Term | Acronym | Definition |
|:---|:---:|:---|
| Harfang3D | - | Harfang3D is a real-time 3D engine |
| FABGen | - | FABGen is a set of Python scripts to generate C++ binding code to different languages. |
| F# | F Sharp | F# is a functional programming language |
| C++ | C Plus Plus | C++ is a programming language |
| Lua | - | Lua is a programming language |
| Go | - | Go is a programming language |
| API | Application Programming Interface | An API is a set of functions and procedures allowing the creation of applications that access the features or data of an operating system, application, or other service. |
| Binding | - | A binding is a link between two things. |

