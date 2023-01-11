# Harfang - The Fabulous binding Generator for CPython and FSharp

import os

import gen

import lib

class FSharpGenerator(gen.Generator):
    def __init__(self, module, output_dir, output_file, output_namespace):
        gen.Generator.__init__(self, module, output_dir, output_file, output_namespace)

        self.output_dir = output_dir
        self.output_file = output_file
        self.output_namespace = output_namespace

        self.output_file = os.path.join(self.output_dir, self.output_file)

        self.output = open(self.output_file, "w")
