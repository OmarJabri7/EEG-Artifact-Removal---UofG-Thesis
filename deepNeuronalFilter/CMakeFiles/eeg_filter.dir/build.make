# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.20

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
CMAKE_COMMAND = /usr/local/Cellar/cmake/3.20.4/bin/cmake

# The command to remove a file.
RM = /usr/local/Cellar/cmake/3.20.4/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/Users/omar/Desktop/UofG/Master's Project/Thesis/EEG-Artifact-Removal---UofG-Thesis/deepNeuronalFilter"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/Users/omar/Desktop/UofG/Master's Project/Thesis/EEG-Artifact-Removal---UofG-Thesis/deepNeuronalFilter"

# Include any dependencies generated for this target.
include CMakeFiles/eeg_filter.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/eeg_filter.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/eeg_filter.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/eeg_filter.dir/flags.make

CMakeFiles/eeg_filter.dir/dnf_test.cpp.o: CMakeFiles/eeg_filter.dir/flags.make
CMakeFiles/eeg_filter.dir/dnf_test.cpp.o: dnf_test.cpp
CMakeFiles/eeg_filter.dir/dnf_test.cpp.o: CMakeFiles/eeg_filter.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/Users/omar/Desktop/UofG/Master's Project/Thesis/EEG-Artifact-Removal---UofG-Thesis/deepNeuronalFilter/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/eeg_filter.dir/dnf_test.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/eeg_filter.dir/dnf_test.cpp.o -MF CMakeFiles/eeg_filter.dir/dnf_test.cpp.o.d -o CMakeFiles/eeg_filter.dir/dnf_test.cpp.o -c "/Users/omar/Desktop/UofG/Master's Project/Thesis/EEG-Artifact-Removal---UofG-Thesis/deepNeuronalFilter/dnf_test.cpp"

CMakeFiles/eeg_filter.dir/dnf_test.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/eeg_filter.dir/dnf_test.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/Users/omar/Desktop/UofG/Master's Project/Thesis/EEG-Artifact-Removal---UofG-Thesis/deepNeuronalFilter/dnf_test.cpp" > CMakeFiles/eeg_filter.dir/dnf_test.cpp.i

CMakeFiles/eeg_filter.dir/dnf_test.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/eeg_filter.dir/dnf_test.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/Users/omar/Desktop/UofG/Master's Project/Thesis/EEG-Artifact-Removal---UofG-Thesis/deepNeuronalFilter/dnf_test.cpp" -o CMakeFiles/eeg_filter.dir/dnf_test.cpp.s

# Object files for target eeg_filter
eeg_filter_OBJECTS = \
"CMakeFiles/eeg_filter.dir/dnf_test.cpp.o"

# External object files for target eeg_filter
eeg_filter_EXTERNAL_OBJECTS =

eeg_filter: CMakeFiles/eeg_filter.dir/dnf_test.cpp.o
eeg_filter: CMakeFiles/eeg_filter.dir/build.make
eeg_filter: DNF/libCLDL.a
eeg_filter: /usr/local/lib/libiir.1.9.0.dylib
eeg_filter: /usr/local/lib/libiir_static.a
eeg_filter: /usr/local/lib/libfir.1.5.0.dylib
eeg_filter: /usr/local/opt/opencv@2/lib/libopencv_videostab.2.4.13.dylib
eeg_filter: /usr/local/opt/opencv@2/lib/libopencv_ts.a
eeg_filter: /usr/local/opt/opencv@2/lib/libopencv_superres.2.4.13.dylib
eeg_filter: /usr/local/opt/opencv@2/lib/libopencv_stitching.2.4.13.dylib
eeg_filter: /usr/local/opt/opencv@2/lib/libopencv_contrib.2.4.13.dylib
eeg_filter: /usr/local/opt/opencv@2/lib/libopencv_nonfree.2.4.13.dylib
eeg_filter: /usr/local/opt/opencv@2/lib/libopencv_ocl.2.4.13.dylib
eeg_filter: /usr/local/opt/opencv@2/lib/libopencv_gpu.2.4.13.dylib
eeg_filter: /usr/local/opt/opencv@2/lib/libopencv_photo.2.4.13.dylib
eeg_filter: /usr/local/opt/opencv@2/lib/libopencv_objdetect.2.4.13.dylib
eeg_filter: /usr/local/opt/opencv@2/lib/libopencv_legacy.2.4.13.dylib
eeg_filter: /usr/local/opt/opencv@2/lib/libopencv_video.2.4.13.dylib
eeg_filter: /usr/local/opt/opencv@2/lib/libopencv_ml.2.4.13.dylib
eeg_filter: /usr/local/opt/opencv@2/lib/libopencv_calib3d.2.4.13.dylib
eeg_filter: /usr/local/opt/opencv@2/lib/libopencv_features2d.2.4.13.dylib
eeg_filter: /usr/local/opt/opencv@2/lib/libopencv_highgui.2.4.13.dylib
eeg_filter: /usr/local/opt/opencv@2/lib/libopencv_imgproc.2.4.13.dylib
eeg_filter: /usr/local/opt/opencv@2/lib/libopencv_flann.2.4.13.dylib
eeg_filter: /usr/local/opt/opencv@2/lib/libopencv_core.2.4.13.dylib
eeg_filter: CMakeFiles/eeg_filter.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/Users/omar/Desktop/UofG/Master's Project/Thesis/EEG-Artifact-Removal---UofG-Thesis/deepNeuronalFilter/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable eeg_filter"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/eeg_filter.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/eeg_filter.dir/build: eeg_filter
.PHONY : CMakeFiles/eeg_filter.dir/build

CMakeFiles/eeg_filter.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/eeg_filter.dir/cmake_clean.cmake
.PHONY : CMakeFiles/eeg_filter.dir/clean

CMakeFiles/eeg_filter.dir/depend:
	cd "/Users/omar/Desktop/UofG/Master's Project/Thesis/EEG-Artifact-Removal---UofG-Thesis/deepNeuronalFilter" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/Users/omar/Desktop/UofG/Master's Project/Thesis/EEG-Artifact-Removal---UofG-Thesis/deepNeuronalFilter" "/Users/omar/Desktop/UofG/Master's Project/Thesis/EEG-Artifact-Removal---UofG-Thesis/deepNeuronalFilter" "/Users/omar/Desktop/UofG/Master's Project/Thesis/EEG-Artifact-Removal---UofG-Thesis/deepNeuronalFilter" "/Users/omar/Desktop/UofG/Master's Project/Thesis/EEG-Artifact-Removal---UofG-Thesis/deepNeuronalFilter" "/Users/omar/Desktop/UofG/Master's Project/Thesis/EEG-Artifact-Removal---UofG-Thesis/deepNeuronalFilter/CMakeFiles/eeg_filter.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/eeg_filter.dir/depend

