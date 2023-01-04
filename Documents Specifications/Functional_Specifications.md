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
    - [2.2 System Actors](#22-system-actors)
    - [2.3 Dependencies and Change Impacts](#23-dependencies-and-change-impacts)
  - [3. Functional Specifications](#3-functional-specifications)
    - [3.1 Binding F# for HARFANG® 3D](#31-binding-f-for-harfang-3d)
  - [4. System Configurations](#4-system-configurations)
  - [5. Other System Requirements/ Non Functional Requirements](#5-other-system-requirements-non-functional-requirements)
  - [6. Reporting Requirements](#6-reporting-requirements)
  - [7. Integration Requirements](#7-integration-requirements)
    - [7.1 Exception Handling/ Error Reporting](#71-exception-handling-error-reporting)
  - [8. References](#8-references)
  - [9. Open Issues](#9-open-issues)
  - [10. Glossary](#10-glossary)
  
</details>

___
<img id="image" src="img/harfang3d-logo.png" >
<br>

## 1. Introduction 

<br>

### 1.1 Purpose 

[HARFANG® 3D](https://www.harfang3d.com/en_US/) is a 3D engine that allows you to create 3D games and applications. It is a cross-platform engine that can be used on Windows, Linux, macOS, iOS, Android, and HTML5. It is written in **C++** and uses OpenGL for rendering. It is also compatible with Vulkan and DirectX 11.

Based on the information provided, it appears that the purpose of developing another 3D engine, **HARFANG® 3D** is to meet the specific technical, sovereignty, and long-term requirements of the civil and defense industries. These industries have strong technical requirements such as safety certification and custom hardware, as well as a need for confidentiality and the ability to run offline.

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
| **HARFANG® 3D** | 3D engine that allows you to create 3D games and applications. |
| **F#** | Functional programming language. |
| **C++** | Object-oriented programming language. |
| **OpenGL** | Cross-platform API for rendering 2D and 3D graphics. |
| **Vulkan** | Cross-platform API for rendering 2D and 3D graphics. |
| **DirectX 11** | Cross-platform API for rendering 2D and 3D graphics. |
| **HTML5** | Markup language for web pages. |

<br>

### 1.5 Risk and Assumptions

- If we forget to create a binding for a function, it will not be possible to use it in F#.

<br>

## 2. System/ Solution Overview



<br>

### 2.1 Context Diagram 

### 2.2 System Actors

### 2.3 Dependencies and Change Impacts

## 3. Functional Specifications

### 3.1 Binding F# for HARFANG® 3D

  - #### 3.1.1 Purpose/ Description

  - #### 3.1.2 Uses Cases

  - #### 3.1.3 Mock-up

  - #### 3.1.4 Functional Requirements

  - #### 3.1.5 Field level Specifications

## 4. System Configurations

## 5. Other System Requirements/ Non Functional Requirements

## 6. Reporting Requirements

## 7. Integration Requirements

### 7.1 Exception Handling/ Error Reporting

## 8. References

## 9. Open Issues

## 10. Glossary


<style>
  img {
    width: 100px;
    height: 100px;
    margin-left: 450px;
    position: absolute;
  }
</style>

