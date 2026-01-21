# Generated from /home/shon/PersonalWorkspace/Uni/PPL/assignment1/tyc-compiler/src/grammar/TyC.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3*")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7\2\2\3\5\3\3\2\2\2\2")
        return buf.getvalue()


class TyCParser ( Parser ):

    grammarFileName = "TyC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'struct'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "','", "'('", 
                     "')'", "'{'", "'}'", "';'", "'['", "']'", "<INVALID>", 
                     "'='", "'=='", "'!='", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'<'", "'>'", "'<='", "'>='", "'&&'", "'||'", 
                     "'!'", "'++'", "'--'", "'.'" ]

    symbolicNames = [ "<INVALID>", "WS", "STRUCT", "RESERVED_WORDS", "TYPE", 
                      "BLOCK_COMMENT", "LINE_COMMENT", "COMMA", "LEFT_PAREN", 
                      "RIGHT_PAREN", "LEFT_BRACE", "RIGHT_BRACE", "SEMICOLON", 
                      "LEFT_SQUARE_BRACKET", "RIGHT_SQUARE_BRACKET", "ID", 
                      "ASSIGN", "EQUAL", "NOT_EQUAL", "PLUS", "MINUS", "MULTIPLY", 
                      "DIVIDE", "MODULUS", "LESS_THAN", "GREATER_THAN", 
                      "LESS_THAN_OR_EQUAL", "GREATER_THAN_OR_EQUAL", "LOGICAL_AND", 
                      "LOGICAL_OR", "LOGICAL_NOT", "INCREMENT", "DECREMENT", 
                      "MEMBER_ACCESS", "INTEGER_LITERAL", "FLOAT_LITERAL", 
                      "STRING_LITERAL", "CHAR_LITERAL", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    WS=1
    STRUCT=2
    RESERVED_WORDS=3
    TYPE=4
    BLOCK_COMMENT=5
    LINE_COMMENT=6
    COMMA=7
    LEFT_PAREN=8
    RIGHT_PAREN=9
    LEFT_BRACE=10
    RIGHT_BRACE=11
    SEMICOLON=12
    LEFT_SQUARE_BRACKET=13
    RIGHT_SQUARE_BRACKET=14
    ID=15
    ASSIGN=16
    EQUAL=17
    NOT_EQUAL=18
    PLUS=19
    MINUS=20
    MULTIPLY=21
    DIVIDE=22
    MODULUS=23
    LESS_THAN=24
    GREATER_THAN=25
    LESS_THAN_OR_EQUAL=26
    GREATER_THAN_OR_EQUAL=27
    LOGICAL_AND=28
    LOGICAL_OR=29
    LOGICAL_NOT=30
    INCREMENT=31
    DECREMENT=32
    MEMBER_ACCESS=33
    INTEGER_LITERAL=34
    FLOAT_LITERAL=35
    STRING_LITERAL=36
    CHAR_LITERAL=37
    ERROR_CHAR=38
    ILLEGAL_ESCAPE=39
    UNCLOSE_STRING=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TyCParser.EOF, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_program




    def program(self):

        localctx = TyCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(TyCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





