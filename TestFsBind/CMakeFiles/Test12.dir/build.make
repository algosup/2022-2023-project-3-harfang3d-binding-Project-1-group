# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.25

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /opt/homebrew/lib/python3.10/site-packages/cmake/data/bin/cmake

# The command to remove a file.
RM = /opt/homebrew/lib/python3.10/site-packages/cmake/data/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/Users/remycharles/Desktop/Github Desktop/2022-2023-project-3-harfang3d-binding-Project-1-group/TestFsBind"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/Users/remycharles/Desktop/Github Desktop/2022-2023-project-3-harfang3d-binding-Project-1-group/TestFsBind"

# Include any dependencies generated for this target.
include CMakeFiles/Test12.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/Test12.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/Test12.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Test12.dir/flags.make

CMakeFiles/Test12.dir/vectors.cpp.o: CMakeFiles/Test12.dir/flags.make
CMakeFiles/Test12.dir/vectors.cpp.o: vectors.cpp
CMakeFiles/Test12.dir/vectors.cpp.o: CMakeFiles/Test12.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/Users/remycharles/Desktop/Github Desktop/2022-2023-project-3-harfang3d-binding-Project-1-group/TestFsBind/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/Test12.dir/vectors.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/Test12.dir/vectors.cpp.o -MF CMakeFiles/Test12.dir/vectors.cpp.o.d -o CMakeFiles/Test12.dir/vectors.cpp.o -c "/Users/remycharles/Desktop/Github Desktop/2022-2023-project-3-harfang3d-binding-Project-1-group/TestFsBind/vectors.cpp"

CMakeFiles/Test12.dir/vectors.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Test12.dir/vectors.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/Users/remycharles/Desktop/Github Desktop/2022-2023-project-3-harfang3d-binding-Project-1-group/TestFsBind/vectors.cpp" > CMakeFiles/Test12.dir/vectors.cpp.i

CMakeFiles/Test12.dir/vectors.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Test12.dir/vectors.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/Users/remycharles/Desktop/Github Desktop/2022-2023-project-3-harfang3d-binding-Project-1-group/TestFsBind/vectors.cpp" -o CMakeFiles/Test12.dir/vectors.cpp.s

# Object files for target Test12
Test12_OBJECTS = \
"CMakeFiles/Test12.dir/vectors.cpp.o"

# External object files for target Test12
Test12_EXTERNAL_OBJECTS =

lib/libTest12.dylib: CMakeFiles/Test12.dir/vectors.cpp.o
lib/libTest12.dylib: CMakeFiles/Test12.dir/build.make
lib/libTest12.dylib: CMakeFiles/Test12.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/Users/remycharles/Desktop/Github Desktop/2022-2023-project-3-harfang3d-binding-Project-1-group/TestFsBind/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library lib/libTest12.dylib"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/Test12.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Test12.dir/build: lib/libTest12.dylib
.PHONY : CMakeFiles/Test12.dir/build

CMakeFiles/Test12.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/Test12.dir/cmake_clean.cmake
.PHONY : CMakeFiles/Test12.dir/clean

CMakeFiles/Test12.dir/depend:
	cd "/Users/remycharles/Desktop/Github Desktop/2022-2023-project-3-harfang3d-binding-Project-1-group/TestFsBind" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/Users/remycharles/Desktop/Github Desktop/2022-2023-project-3-harfang3d-binding-Project-1-group/TestFsBind" "/Users/remycharles/Desktop/Github Desktop/2022-2023-project-3-harfang3d-binding-Project-1-group/TestFsBind" "/Users/remycharles/Desktop/Github Desktop/2022-2023-project-3-harfang3d-binding-Project-1-group/TestFsBind" "/Users/remycharles/Desktop/Github Desktop/2022-2023-project-3-harfang3d-binding-Project-1-group/TestFsBind" "/Users/remycharles/Desktop/Github Desktop/2022-2023-project-3-harfang3d-binding-Project-1-group/TestFsBind/CMakeFiles/Test12.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/Test12.dir/depend

