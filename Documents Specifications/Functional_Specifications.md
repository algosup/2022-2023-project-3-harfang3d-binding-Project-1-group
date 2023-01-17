# Functional Specifications 

2023 Project Harfang3D Binding Group 1 <br>
Created on: 2023-04-01 <br>
Author: [Rémy Charles](https://github.com/RemyCHARLES)

| Role | Name | 
| :--- | :--- |
| Project Manager | [Elise Gautier](https://github.com/elisegtr) |
| Program Manager | [Rémy Charles](https://github.com/RemyCHARLES) |
| Tech Lead | [Nicolas Mida](https://github.com/Nicolas-Mida) | 
| Software Engineer | [Grégory Pagnoux](https://github.com/Gregory-Pagnoux) |  
| Quality Assurance | [Théo Trouvé](https://github.com/TheoTr) | 

<br>

___

<details><summary>Table of Contents</summary>

- [Functional Specifications](#functional-specifications)
  - [1. Introduction](#1-introduction)
    - [1.1 Purpose](#11-purpose)
    - [1.2 Project Scope](#12-project-scope)
    - [1.3 Related documents](#13-related-documents)
    - [1.4 Terms/ Acronyms and Definitions](#14-terms-acronyms-and-definitions)
    - [1.5 Risk and Assumptions](#15-risk-and-assumptions)
  - [2. System/ Solution Overview](#2-system-solution-overview)
    - [2.1 Context Diagram](#21-context-diagram)
    - [2.2 Dependencies and Change Impacts](#22-dependencies-and-change-impacts)
  - [3. Functional Specifications](#3-functional-specifications)
    - [3.1 Binding F# for HARFANG® 3D](#31-binding-f-for-harfang-3d)
  - [4. Other System Requirements/ Non Functional Requirements](#4-other-system-requirements-non-functional-requirements)
  - [6. Integration Requirements](#6-integration-requirements)
    - [6.1 Exception Handling/ Error Reporting](#61-exception-handling-error-reporting)
  - [7. References](#7-references)
  - [8. Open Issues](#8-open-issues)
  
</details>

___

<img src="https://github.com/harfang3d/image-storage/raw/main/brand/logo_harfang3d_owl_only.png" width="150px" heigth="150px" align="right" >

<br>

## 1. Introduction 

<br>

### 1.1 Purpose 

[HARFANG® 3D](https://www.harfang3d.com/en_US/) is a 3D engine that allows you to create 3D games and applications. It is a cross-platform engine that can be used on Win32, Win64 Intel, Linux 64 Intel and Aarch 64 ARM . It is written in **C++** and uses OpenGL for rendering. It is also compatible with Vulkan and DirectX 11.

Based on the information provided, it appears that the purpose of developing another 3D engine, **HARFANG® 3D** is to meet the specific technical, sovereignty, and long-term requirements of the civil and defense industries. These industries have strong technical requirements such as safety certification and custom hardware, as well as a need for confidentiality and the ability to run offline.



<br>

**Company distribution**

| Person | Company role | Contact |
| :-: | :-: | :-: |
| [François Gutherz](https://www.linkedin.com/in/astrofra/) | CTO & Project leader | francois.gutherz@harfang3d.com|
| [Emmanuel Julien](https://www.linkedin.com/in/ejulien/) | Lead developer | emmanuel.julien@harfang3d.com|

<br>

### 1.2 Project Scope

   - Create Bindings for the **HARFANG® 3D** engine  
   - Provide a **set of tools** and **documentation** that make it easy for **F#** developers to incorporate **HARFANG® 3D** into their projects.

<br>

### 1.3 Related documents

| Document | Description |
| :--- | :--- |
| [Critical Path](/Critical%20Path/Critical_Path.md) | Project schedule |
| [Test Plan](/Test%20Plan/Test_Plan.md) | Test plan |
| [Technical Specifications](/Documents%20Specifications/Technical_Specification.md) | Technical specifications |
| [Trello](https://trello.com/b/B7eB7vfa/f) | Trello board |

<br>

### 1.4 Terms/ Acronyms and Definitions

| Term | Definition |
| :--- | :--- |
| **HARFANG® 3D** | HARFANG® 3D is a proprietary, cross-platform 3D engine and toolset for creating interactive 3D applications and games, developed by "SNEAKY GAMES" and supports Windows, MacOS, Linux. |
| **FABgen** | Generator of bindings for the C++ engine HARFANG® 3D. |
| **SWIG** | SWIG is a tool for connecting C/C++ code with other high-level programming languages like Python, Java, and C#. It generates interfaces, also known as wrappers, to allow high-level languages to access C/C++ code, enabling developers to use the performance of C/C++ while still taking advantage of the ease of use of high-level languages. |
| **F#** | F# is a functional-first, multi-paradigm programming language for the .NET platform, developed by Microsoft, open-source and often used for functional programming and data science, as well as for high-performance and concurrent applications. |
| **lua** | Lua is a lightweight, high-performance programming language designed for extending applications. It's commonly used in video games and other applications, is open-source, cross-platform and has a small footprint, making it well-suited for embedded systems and mobile devices. |
| **C++** | C++ is a high-performance, general-purpose programming language widely used for developing operating systems, video games, browsers and other high-performance applications. It allows low-level memory manipulation and provides a lot of control over the hardware. |
| **Python** | Python is a high-level, interpreted programming language known for its simple and easy-to-learn syntax, widely used for scientific computing, data analysis, artificial intelligence, and web development. It has a large number of libraries and frameworks that can be used for a variety of tasks. |
| **OpenGL** | OpenGL is a cross-platform, industry-standard graphics API for 2D and 3D applications, widely used for video games and other 3D applications, supported on various platforms such as Windows, MacOS, Linux and mobile devices. |
| **Vulkan** |Vulkan is a low-overhead, cross-platform 3D graphics API that provides improved performance and power efficiency, used for video games and other demanding applications. Developed by the Khronos Group and works on multiple platforms.|
| **DirectX 11** | DirectX 11 is a set of APIs for programming graphics and video on Windows, commonly used for developing video games and other multimedia applications with improved 3D graphics and support for new features like tessellation and multi-core processors. |

<br>

### 1.5 Risk and Assumptions

- If we forget to create a binding for a function, it will not be possible to use it in F#.

<br>

___

## 2. System/ Solution Overview

<br>

### 2.1 Context Diagram 

<img src="img/Schema.png" >

<br>


### 2.2 Dependencies and Change Impacts

  - #### 2.2.1 System Dependencies
      
       The proposed solution will not depend on any other system because it is   not mandatory for the proper functioning of Harfang3D or other systems.

<br>

  - #### 2.2.2 Change Impacts

    - **HARFANG® 3D** : 3D engine that allows you to create 3D games and applications.
    - **FABgen** : Generator of bindings for the C++ engine HARFANG® 3D.
     - **OpenGL** : Cross-platform API for rendering 2D and 3D graphics.
     - **Vulkan** : Cross-platform API for rendering 2D and 3D graphics.
     - **DirectX 11** : Cross-platform API for rendering 2D and 3D graphics.

<br>

___

## 3. Functional Specifications

### 3.1 Binding F# for HARFANG® 3D

  - #### 3.1.1 Purpose/ Description

    The purpose of this section is to create the binding of the **HARFANG® 3D** engine in **F#**. For that we will use **FABgen** generator this is a depedency of **HARFANG® 3D** project to bring C++ engine to languages such as Python, Lua and GO. FABGen allows to replace **SWIG**, a another bindings generator supporting a lot of language. But SWIG have a some issues and that's why **HARFANG® 3D** create FABGen, and our goal is to use it to create bindings for **F#**.

    The goals of this project is to implement **F#** in FABGen to allow access for everyone who want to use this software in **F#**. In fact, C++ are not very accessible for non-coding experts person so they want to make it easier and thanks to FABGen who implements Python, Lua, GO and soon F# and Rust. Incorporating F# into FABGen would be beneficial for those who utilize F# and require a 3D engine. It may also appeal to those seeking an alternative to SWIG when connecting a C++ library to F#. F# is a concise and user-friendly language that allows for faster code development and fewer errors. Additionally, F# utilizes the .NET "int" data type which is optimized for mathematical operations and bit manipulation, resulting in faster performance compared to other languages.

  <br>

  - #### 3.1.2 Mock-up

<img src="img/Mock-Up.png" >
 
F# are not mentioned in the schema but that will work the same way as the other languages.

<br>

  - #### 3.1.4 Functional Requirements

| ID | Description | Priority | Status |
| :--- | :--- | :--- | :--- |
| FR-1 | Generate binding layers to Cpython and Lua using FABgen. | 1 | To do |
| FR-2 | Run unit tests and examine how the Go bindings work. | 2 | To do |
| FR-3 | Map types and implement features required by tests, starting with easy ones from the specified repository. | 2 | To do |
| FR-4 | Improve integration with the target language. | 2 | To do |


  - #### 3.1.5 Field level Specifications

| ID | Description | Priority | Status |
| :--- | :--- | :--- | :--- |
| FLS-1 | FABGen: The bindings should be generated using FABGen, which is a code generator designed to create bindings for various languages. | 1 | To do |
| FLS-2 | Error handling: The bindings should handle errors and exceptions from the Harfang3D API gracefully, and provide appropriate error messages. | 2 | To do |
| FLS-3 | Documentation: The bindings should be well-documented, with clear explanations of how to use the various classes, methods, and properties. | 6 | To do |
| FLS-4 | Unit tests: The bindings should be accompanied by a set of unit tests to ensure that they are working correctly. | 3 | To do | 
| FLS-5 | Compatibility: The bindings should be compatible with the latest version of Harfang3D and should be updated as new versions are released. | 5 | To do |   
| FLS-6 | Performance: The bindings should not introduce a significant performance overhead when compared to using the C++ Harfang3D API directly. | 4 | To do |
| FLS-7 | Support: The project should provide support for developers who are using the F# bindings, and should be actively maintained to fix any issues that are discovered. | 7 | To do | 

  - #### 3.1.6 Personas

| Name | Age | Role |Description | 
| :--- | :--- | :--- | :--- |
| Mathias Durant | 38 |F# developer | The F# developer wants to use the HARFANG® 3D engine in F# to create a simulation 3D in Virtual Reality (VR) to know which is most likely to attract the attention of a passer-by on the street. | 
| Pierre-Étienne Morency | 23 | Computer Science Student | He is a students who need to use the HARFRANG® 3D engine in F# to create a reproduction of his school in VR. |
| Jean-Philippe Lavoie | 48 | Software Engineer | He is a software engineer who needs to use the HARFRANG® 3D engine in F# to create a AR system for this car company. | 
| Marie-Ève Lavoie | 25 | Entrepreneur | She is a young entrepreneur who wants to have a 3D visualization of her final product and thanks to some knowledge in F#, she uses HARFRANG® 3D. |

___

## 4. Other System Requirements/ Non Functional Requirements

<!-- Todo -->
| Requirements | Description |
| :--- | :--- |
| **Performance** | TF# bindings should be efficient, with minimal overhead and latency, utilizing optimized data structures, minimizing unnecessary calculations, parallel processing and thread-safe, able to handle high concurrency. |
| **Security** | F# bindings should have strong security, implementing secure coding, input validation, error handling, authentication, authorization, encryption of sensitive data, and regular security testing. |
| **Usability** | F# bindings should have a clear, intuitive interface with good documentation, consistent naming and organization, flexibility and configurability, and compatibility with a wide range of platforms and frameworks. |
| **Maintainability** | F# bindings should have clear and well-organized code, following best practices for coding style, documentation, design patterns, abstractions and Testable, easy to add new features or make changes without introducing bugs. |
| **Scalability** | F# bindings should be able to handle increasing data and traffic using optimized data structures, algorithms, caching, load balancing,horizontally scalable, handle varying levels of concurrency and different types of workloads. |


___

## 6. Integration Requirements

### 6.1 Exception Handling/ Error Reporting

See the [Test Plan](/Test%20Plan/Test_Plan.md) and the [Critical Path](/Critical%20Path/Critical_Path.md)

___

## 7. References

| ID | Description | URL |
| :--- | :--- | :--- |
| 1 | HARFANG® 3D | [Link](https://www.harfang3d.com/en_US/) |
| 2 | FABgen | [Link](https://github.com/ejulien/FABGen) |


___

## 8. Open Issues

<!-- Todo -->
