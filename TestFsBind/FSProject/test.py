import importlib
import tempfile
import subprocess
import argparse
import shutil
import lib
import sys
import os

start_path = os.path.dirname(__file__)

parser = argparse.ArgumentParser(description='Run generator unit tests.')
parser.add_argument('--pybase', dest='python_base_path', help='Path to the Python interpreter')
parser.add_argument('--debug', dest='debug_test', help='Generate a working solution to debug a test')
parser.add_argument('--x64', dest='x64', help='Build for 64 bit architecture', action='store_true', default=False)
parser.add_argument('--linux', dest='linux', help='Build on Linux', action='store_true', default=False)
parser.add_argument('--fsharp', dest='fsharp_build', help='Build FSharp', action='store_true', default=False)

args = parser.parse_args()

# -- interpreter settings
if args.python_base_path:
	python_include_dir = args.python_base_path + '/' + 'include'
	python_library = args.python_base_path + '/' + 'libs/python3.lib'
	python_site_package = args.python_base_path + '/' + 'Lib/site-packages'
	python_interpreter = args.python_base_path + '/' + 'python.exe'

# -- CMake generator
if not args.linux:
	if args.x64:
		cmake_generator = 'Visual Studio 17 2022'
	else:
		cmake_generator = 'Visual Studio 17 2022'

	print("Using CMake generator: %s" % cmake_generator)

	msvc_arch = 'x64' if args.x64 else 'Win32'

# --
run_test_list = []
failed_test_list = []

def run_test(gen, name, testbed):
	work_path = tempfile.mkdtemp()
	print('Working directory is ' + work_path)

	test_module = importlib.import_module(name)

	# generate the interface file
	files = test_module.bind_test(gen)
	sources = []

	for path, src in files.items():
		if path[-2:] != '.h':
			sources.append(path)
		with open(os.path.join(work_path, path), 'w') as file:
			file.write(src)

	# with open(os.path.join(work_path, 'fabgen.h'), 'w') as file:
	# 	import gen as gen_module
	# 	file.write(gen_module.get_fabgen_api())

	run_test_list.append(name)
	result = testbed.build_and_test_extension(work_path, test_module, sources)

	if result:
		print("[OK]")
	else:
		print("[FAILED]")
		failed_test_list.append(name)

	if args.debug_test:
		if args.linux:
			subprocess.Popen('xdg-open "%s"' % work_path, shell=True)
		else:
			subprocess.Popen('explorer "%s"' % work_path)
	else:
		shutil.rmtree(work_path, ignore_errors=True)

def run_tests(names, testbed):
	# print("Starting tests with generator %s" % gen.get_language())

	test_count = len(names)
	print("Running %d tests\n" % test_count)

	for i, name in enumerate(names):
		# print('[%d/%d] Running test "%s" (%s)' % (i+1, test_count, name, gen.get_language()))
		cwd = os.getcwd()
		run_test(name, testbed)
		os.chdir(cwd)
		print('')

	run_test_count = len(run_test_list)
	failed_test_count = len(failed_test_list)

	print("[Test summary: %d run, %d failed]" % (run_test_count, failed_test_count))
	# print("Done with fabgen generator %s\n" % gen.get_language())

# Fsharp test bed
def create_fsharp_cmake_file(module, work_path, sources):
	cmake_path = os.path.join(work_path, 'CMakeLists.txt')

	with open(cmake_path, 'w') as file:
		quoted_sources = ['"%s"' % source for source in sources if ".fs" not in source]

		work_place_ = work_path.replace('\\', '/')

		file.write(f"""
cmake_minimum_required(VERSION 3.1)

set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)

set(CMAKE_MODULE_PATH ${{CMAKE_MODULE_PATH}} "${{CMAKE_SOURCE_DIR}}/")

project({module})
enable_language(C CXX)
set(CMAKE_CXX_STANDARD 14)

add_library(my_test SHARED {' '.join(quoted_sources)})
set_target_properties(my_test PROPERTIES RUNTIME_OUTPUT_DIRECTORY_RELEASE "{work_place_}")

install(TARGETS my_test DESTINATION "${{CMAKE_SOURCE_DIR}}/" COMPONENT my_test)
""")

class TestBed:
    def build_and_test_extension(self, work_path, module, sources):
        if not hasattr(module, "test_fsharp"):
            print("Can't find test_fsharp")
            return False
        
        # copy test file
        test_path = os.path.join(work_path, 'test.fs')
        with open(test_path, 'w') as file:
            file.write(module.test_fsharp)
       
        # Build the F# project
        os.chdir(work_path)
        try:
            subprocess.check_output("dotnet new console -lang F# -n test", shell=True, stderr=subprocess.STDOUT)
            subprocess.check_output("dotnet add test.fsproj reference sources", shell=True, stderr=subprocess.STDOUT)
            subprocess.check_output("dotnet build test.fsproj", shell=True, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            print(e.output.decode('utf-8'))
            return False
        
        success = True
        try:
            subprocess.check_output("dotnet test test.fsproj", shell=True, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            print(e.output.decode('utf-8'))
            success = False
        
        return success

# Clang format
def create_clang_format_file(work_path):
	with open(os.path.join(work_path, '_clang-format'), 'w') as file:
		file.write('''ColumnLimit: 0
UseTab: Always
TabWidth: 4
IndentWidth: 4
IndentCaseLabels: true
AccessModifierOffset: -4
AlignAfterOpenBracket: DontAlign
AlwaysBreakTemplateDeclarations: false
AlignTrailingComments: false''')

sys.path.append(os.path.join(start_path, 'tests'))

if args.debug_test:
	test_names = [args.debug_test]
else:
	test_names = [file[:-3] for file in os.listdir('./tests') if file.endswith('.py')]

if args.fsharp_build:
	run_tests(test_names, TestBed())



print("[Final summary]")

if len(failed_test_list) == 0:
	print("All tests passed!")
else:
	print("The following tests failed:")
	for test in failed_test_list:
		print(" - " + test)
	sys.exit(1)
