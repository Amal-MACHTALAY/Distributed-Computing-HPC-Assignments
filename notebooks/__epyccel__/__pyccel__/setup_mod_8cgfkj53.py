from setuptools import Extension, setup
import numpy

extension_mod = Extension("mod_8cgfkj53",
		[ r'mod_8cgfkj53_wrapper.c' ],
		extra_objects = [r'/home/amal/Distributed-Computing-HPC/TP/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__/bind_c_mod_8cgfkj53.o',
				r'/home/amal/Distributed-Computing-HPC/TP/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__/mod_8cgfkj53.o'],
		include_dirs = [r'/home/amal/Distributed-Computing-HPC/TP/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__', numpy.get_include()],
		libraries = [r'gfortran'],
		library_dirs = [r'/usr/lib/gcc/x86_64-linux-gnu/9'],
		extra_link_args = [r'-O3',
				r'-fPIC',
				r'-I"/home/amal/Distributed-Computing-HPC/TP/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__"'])

setup(name = "mod_8cgfkj53", ext_modules=[extension_mod])