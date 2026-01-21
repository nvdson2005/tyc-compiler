# Generated from /home/shon/PersonalWorkspace/Uni/PPL/assignment1/tyc-compiler/src/grammar/TyC.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TyCParser import TyCParser
else:
    from TyCParser import TyCParser

# This class defines a complete listener for a parse tree produced by TyCParser.
class TyCListener(ParseTreeListener):

    # Enter a parse tree produced by TyCParser#program.
    def enterProgram(self, ctx:TyCParser.ProgramContext):
        pass

    # Exit a parse tree produced by TyCParser#program.
    def exitProgram(self, ctx:TyCParser.ProgramContext):
        pass



del TyCParser