# Generated from /Users/codeleap/Uni/PPL/assignment/assignment1/tyc-compiler/src/grammar/TyC.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,52,447,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,1,0,3,0,86,8,0,1,0,1,0,5,0,90,8,0,10,0,12,0,
        93,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,116,8,2,1,3,1,3,1,4,1,4,1,4,5,4,123,
        8,4,10,4,12,4,126,9,4,3,4,128,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,3,5,138,8,5,1,6,1,6,1,6,5,6,143,8,6,10,6,12,6,146,9,6,3,6,148,
        8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,5,8,160,8,8,10,8,12,
        8,163,9,8,1,8,1,8,3,8,167,8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,
        9,177,8,9,1,10,1,10,1,10,1,10,5,10,183,8,10,10,10,12,10,186,9,10,
        3,10,188,8,10,1,10,1,10,1,11,1,11,1,11,1,11,3,11,196,8,11,1,11,1,
        11,1,11,1,11,3,11,202,8,11,1,11,1,11,1,11,1,11,3,11,208,8,11,1,11,
        1,11,1,11,1,11,3,11,214,8,11,1,11,1,11,1,11,1,11,1,11,3,11,221,8,
        11,3,11,223,8,11,3,11,225,8,11,1,12,1,12,1,13,1,13,1,13,1,13,1,13,
        3,13,234,8,13,1,14,1,14,1,14,5,14,239,8,14,10,14,12,14,242,9,14,
        1,15,1,15,1,15,5,15,247,8,15,10,15,12,15,250,9,15,1,16,1,16,1,16,
        5,16,255,8,16,10,16,12,16,258,9,16,1,17,1,17,1,17,5,17,263,8,17,
        10,17,12,17,266,9,17,1,18,1,18,1,18,5,18,271,8,18,10,18,12,18,274,
        9,18,1,19,1,19,1,19,5,19,279,8,19,10,19,12,19,282,9,19,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,295,8,20,1,21,
        1,21,5,21,299,8,21,10,21,12,21,302,9,21,1,22,1,22,5,22,306,8,22,
        10,22,12,22,309,9,22,1,23,1,23,1,23,1,23,1,23,1,23,3,23,317,8,23,
        1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,25,3,25,329,8,25,
        1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,
        1,26,3,26,345,8,26,1,27,1,27,1,27,5,27,350,8,27,10,27,12,27,353,
        9,27,1,28,1,28,1,29,1,29,5,29,359,8,29,10,29,12,29,362,9,29,1,29,
        1,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,3,30,373,8,30,1,31,1,31,
        1,31,1,31,1,31,1,31,1,32,1,32,1,32,3,32,384,8,32,1,32,1,32,3,32,
        388,8,32,1,32,1,32,3,32,392,8,32,1,32,1,32,1,32,1,33,1,33,1,34,1,
        34,1,35,1,35,1,35,1,35,1,35,1,35,5,35,407,8,35,10,35,12,35,410,9,
        35,1,35,1,35,1,36,1,36,3,36,416,8,36,1,37,1,37,1,37,1,37,5,37,422,
        8,37,10,37,12,37,425,9,37,1,38,1,38,1,38,5,38,430,8,38,10,38,12,
        38,433,9,38,1,39,1,39,3,39,437,8,39,1,39,1,39,1,40,1,40,1,40,1,41,
        1,41,1,41,1,41,0,0,42,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,
        76,78,80,82,0,6,5,0,11,11,14,14,16,16,19,19,46,46,1,0,32,33,2,0,
        30,31,42,43,1,0,37,38,1,0,39,41,1,0,28,29,471,0,85,1,0,0,0,2,96,
        1,0,0,0,4,115,1,0,0,0,6,117,1,0,0,0,8,127,1,0,0,0,10,137,1,0,0,0,
        12,147,1,0,0,0,14,149,1,0,0,0,16,166,1,0,0,0,18,176,1,0,0,0,20,178,
        1,0,0,0,22,224,1,0,0,0,24,226,1,0,0,0,26,233,1,0,0,0,28,235,1,0,
        0,0,30,243,1,0,0,0,32,251,1,0,0,0,34,259,1,0,0,0,36,267,1,0,0,0,
        38,275,1,0,0,0,40,294,1,0,0,0,42,296,1,0,0,0,44,303,1,0,0,0,46,316,
        1,0,0,0,48,318,1,0,0,0,50,328,1,0,0,0,52,344,1,0,0,0,54,346,1,0,
        0,0,56,354,1,0,0,0,58,356,1,0,0,0,60,365,1,0,0,0,62,374,1,0,0,0,
        64,380,1,0,0,0,66,396,1,0,0,0,68,398,1,0,0,0,70,400,1,0,0,0,72,415,
        1,0,0,0,74,417,1,0,0,0,76,426,1,0,0,0,78,434,1,0,0,0,80,440,1,0,
        0,0,82,443,1,0,0,0,84,86,3,2,1,0,85,84,1,0,0,0,85,86,1,0,0,0,86,
        91,1,0,0,0,87,90,3,14,7,0,88,90,3,4,2,0,89,87,1,0,0,0,89,88,1,0,
        0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,92,1,0,0,0,92,94,1,0,0,0,93,91,
        1,0,0,0,94,95,5,0,0,1,95,1,1,0,0,0,96,97,5,19,0,0,97,98,5,1,0,0,
        98,99,5,22,0,0,99,100,5,23,0,0,100,101,3,58,29,0,101,3,1,0,0,0,102,
        103,3,6,3,0,103,104,5,46,0,0,104,105,5,22,0,0,105,106,3,8,4,0,106,
        107,5,23,0,0,107,108,3,58,29,0,108,116,1,0,0,0,109,110,5,46,0,0,
        110,111,5,22,0,0,111,112,3,8,4,0,112,113,5,23,0,0,113,114,3,58,29,
        0,114,116,1,0,0,0,115,102,1,0,0,0,115,109,1,0,0,0,116,5,1,0,0,0,
        117,118,7,0,0,0,118,7,1,0,0,0,119,124,3,10,5,0,120,121,5,21,0,0,
        121,123,3,10,5,0,122,120,1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,
        124,125,1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,127,119,1,0,0,0,
        127,128,1,0,0,0,128,9,1,0,0,0,129,130,5,14,0,0,130,138,5,46,0,0,
        131,132,5,11,0,0,132,138,5,46,0,0,133,134,5,16,0,0,134,138,5,46,
        0,0,135,136,5,46,0,0,136,138,5,46,0,0,137,129,1,0,0,0,137,131,1,
        0,0,0,137,133,1,0,0,0,137,135,1,0,0,0,138,11,1,0,0,0,139,144,3,24,
        12,0,140,141,5,21,0,0,141,143,3,24,12,0,142,140,1,0,0,0,143,146,
        1,0,0,0,144,142,1,0,0,0,144,145,1,0,0,0,145,148,1,0,0,0,146,144,
        1,0,0,0,147,139,1,0,0,0,147,148,1,0,0,0,148,13,1,0,0,0,149,150,5,
        17,0,0,150,151,5,46,0,0,151,152,5,24,0,0,152,153,3,16,8,0,153,154,
        5,25,0,0,154,155,5,26,0,0,155,15,1,0,0,0,156,161,3,18,9,0,157,158,
        5,26,0,0,158,160,3,18,9,0,159,157,1,0,0,0,160,163,1,0,0,0,161,159,
        1,0,0,0,161,162,1,0,0,0,162,164,1,0,0,0,163,161,1,0,0,0,164,165,
        5,26,0,0,165,167,1,0,0,0,166,156,1,0,0,0,166,167,1,0,0,0,167,17,
        1,0,0,0,168,169,5,14,0,0,169,177,5,46,0,0,170,171,5,11,0,0,171,177,
        5,46,0,0,172,173,5,16,0,0,173,177,5,46,0,0,174,175,5,46,0,0,175,
        177,5,46,0,0,176,168,1,0,0,0,176,170,1,0,0,0,176,172,1,0,0,0,176,
        174,1,0,0,0,177,19,1,0,0,0,178,187,5,24,0,0,179,184,3,24,12,0,180,
        181,5,21,0,0,181,183,3,24,12,0,182,180,1,0,0,0,183,186,1,0,0,0,184,
        182,1,0,0,0,184,185,1,0,0,0,185,188,1,0,0,0,186,184,1,0,0,0,187,
        179,1,0,0,0,187,188,1,0,0,0,188,189,1,0,0,0,189,190,5,25,0,0,190,
        21,1,0,0,0,191,192,5,5,0,0,192,195,5,46,0,0,193,194,5,36,0,0,194,
        196,3,24,12,0,195,193,1,0,0,0,195,196,1,0,0,0,196,225,1,0,0,0,197,
        198,5,14,0,0,198,201,5,46,0,0,199,200,5,36,0,0,200,202,3,24,12,0,
        201,199,1,0,0,0,201,202,1,0,0,0,202,225,1,0,0,0,203,204,5,11,0,0,
        204,207,5,46,0,0,205,206,5,36,0,0,206,208,3,24,12,0,207,205,1,0,
        0,0,207,208,1,0,0,0,208,225,1,0,0,0,209,210,5,16,0,0,210,213,5,46,
        0,0,211,212,5,36,0,0,212,214,3,24,12,0,213,211,1,0,0,0,213,214,1,
        0,0,0,214,225,1,0,0,0,215,216,5,46,0,0,216,222,5,46,0,0,217,220,
        5,36,0,0,218,221,3,24,12,0,219,221,3,20,10,0,220,218,1,0,0,0,220,
        219,1,0,0,0,221,223,1,0,0,0,222,217,1,0,0,0,222,223,1,0,0,0,223,
        225,1,0,0,0,224,191,1,0,0,0,224,197,1,0,0,0,224,203,1,0,0,0,224,
        209,1,0,0,0,224,215,1,0,0,0,225,23,1,0,0,0,226,227,3,26,13,0,227,
        25,1,0,0,0,228,229,3,54,27,0,229,230,5,36,0,0,230,231,3,26,13,0,
        231,234,1,0,0,0,232,234,3,28,14,0,233,228,1,0,0,0,233,232,1,0,0,
        0,234,27,1,0,0,0,235,240,3,30,15,0,236,237,5,35,0,0,237,239,3,30,
        15,0,238,236,1,0,0,0,239,242,1,0,0,0,240,238,1,0,0,0,240,241,1,0,
        0,0,241,29,1,0,0,0,242,240,1,0,0,0,243,248,3,32,16,0,244,245,5,34,
        0,0,245,247,3,32,16,0,246,244,1,0,0,0,247,250,1,0,0,0,248,246,1,
        0,0,0,248,249,1,0,0,0,249,31,1,0,0,0,250,248,1,0,0,0,251,256,3,34,
        17,0,252,253,7,1,0,0,253,255,3,34,17,0,254,252,1,0,0,0,255,258,1,
        0,0,0,256,254,1,0,0,0,256,257,1,0,0,0,257,33,1,0,0,0,258,256,1,0,
        0,0,259,264,3,36,18,0,260,261,7,2,0,0,261,263,3,36,18,0,262,260,
        1,0,0,0,263,266,1,0,0,0,264,262,1,0,0,0,264,265,1,0,0,0,265,35,1,
        0,0,0,266,264,1,0,0,0,267,272,3,38,19,0,268,269,7,3,0,0,269,271,
        3,38,19,0,270,268,1,0,0,0,271,274,1,0,0,0,272,270,1,0,0,0,272,273,
        1,0,0,0,273,37,1,0,0,0,274,272,1,0,0,0,275,280,3,40,20,0,276,277,
        7,4,0,0,277,279,3,40,20,0,278,276,1,0,0,0,279,282,1,0,0,0,280,278,
        1,0,0,0,280,281,1,0,0,0,281,39,1,0,0,0,282,280,1,0,0,0,283,284,5,
        28,0,0,284,295,3,40,20,0,285,286,5,29,0,0,286,295,3,40,20,0,287,
        288,5,38,0,0,288,295,3,40,20,0,289,290,5,37,0,0,290,295,3,40,20,
        0,291,292,5,44,0,0,292,295,3,40,20,0,293,295,3,42,21,0,294,283,1,
        0,0,0,294,285,1,0,0,0,294,287,1,0,0,0,294,289,1,0,0,0,294,291,1,
        0,0,0,294,293,1,0,0,0,295,41,1,0,0,0,296,300,3,44,22,0,297,299,3,
        48,24,0,298,297,1,0,0,0,299,302,1,0,0,0,300,298,1,0,0,0,300,301,
        1,0,0,0,301,43,1,0,0,0,302,300,1,0,0,0,303,307,3,50,25,0,304,306,
        3,46,23,0,305,304,1,0,0,0,306,309,1,0,0,0,307,305,1,0,0,0,307,308,
        1,0,0,0,308,45,1,0,0,0,309,307,1,0,0,0,310,311,5,45,0,0,311,317,
        5,46,0,0,312,313,5,22,0,0,313,314,3,12,6,0,314,315,5,23,0,0,315,
        317,1,0,0,0,316,310,1,0,0,0,316,312,1,0,0,0,317,47,1,0,0,0,318,319,
        7,5,0,0,319,49,1,0,0,0,320,329,5,46,0,0,321,329,5,47,0,0,322,329,
        5,48,0,0,323,329,5,49,0,0,324,325,5,22,0,0,325,326,3,24,12,0,326,
        327,5,23,0,0,327,329,1,0,0,0,328,320,1,0,0,0,328,321,1,0,0,0,328,
        322,1,0,0,0,328,323,1,0,0,0,328,324,1,0,0,0,329,51,1,0,0,0,330,331,
        3,22,11,0,331,332,5,26,0,0,332,345,1,0,0,0,333,334,3,56,28,0,334,
        335,5,26,0,0,335,345,1,0,0,0,336,345,3,60,30,0,337,345,3,62,31,0,
        338,345,3,64,32,0,339,345,3,70,35,0,340,345,3,78,39,0,341,345,3,
        80,40,0,342,345,3,82,41,0,343,345,3,58,29,0,344,330,1,0,0,0,344,
        333,1,0,0,0,344,336,1,0,0,0,344,337,1,0,0,0,344,338,1,0,0,0,344,
        339,1,0,0,0,344,340,1,0,0,0,344,341,1,0,0,0,344,342,1,0,0,0,344,
        343,1,0,0,0,345,53,1,0,0,0,346,351,5,46,0,0,347,348,5,45,0,0,348,
        350,5,46,0,0,349,347,1,0,0,0,350,353,1,0,0,0,351,349,1,0,0,0,351,
        352,1,0,0,0,352,55,1,0,0,0,353,351,1,0,0,0,354,355,3,24,12,0,355,
        57,1,0,0,0,356,360,5,24,0,0,357,359,3,52,26,0,358,357,1,0,0,0,359,
        362,1,0,0,0,360,358,1,0,0,0,360,361,1,0,0,0,361,363,1,0,0,0,362,
        360,1,0,0,0,363,364,5,25,0,0,364,59,1,0,0,0,365,366,5,13,0,0,366,
        367,5,22,0,0,367,368,3,24,12,0,368,369,5,23,0,0,369,372,3,52,26,
        0,370,371,5,10,0,0,371,373,3,52,26,0,372,370,1,0,0,0,372,373,1,0,
        0,0,373,61,1,0,0,0,374,375,5,20,0,0,375,376,5,22,0,0,376,377,3,24,
        12,0,377,378,5,23,0,0,378,379,3,52,26,0,379,63,1,0,0,0,380,381,5,
        12,0,0,381,383,5,22,0,0,382,384,3,66,33,0,383,382,1,0,0,0,383,384,
        1,0,0,0,384,385,1,0,0,0,385,387,5,26,0,0,386,388,3,24,12,0,387,386,
        1,0,0,0,387,388,1,0,0,0,388,389,1,0,0,0,389,391,5,26,0,0,390,392,
        3,68,34,0,391,390,1,0,0,0,391,392,1,0,0,0,392,393,1,0,0,0,393,394,
        5,23,0,0,394,395,3,52,26,0,395,65,1,0,0,0,396,397,3,22,11,0,397,
        67,1,0,0,0,398,399,3,24,12,0,399,69,1,0,0,0,400,401,5,18,0,0,401,
        402,5,22,0,0,402,403,3,24,12,0,403,404,5,23,0,0,404,408,5,24,0,0,
        405,407,3,72,36,0,406,405,1,0,0,0,407,410,1,0,0,0,408,406,1,0,0,
        0,408,409,1,0,0,0,409,411,1,0,0,0,410,408,1,0,0,0,411,412,5,25,0,
        0,412,71,1,0,0,0,413,416,3,74,37,0,414,416,3,76,38,0,415,413,1,0,
        0,0,415,414,1,0,0,0,416,73,1,0,0,0,417,418,5,7,0,0,418,419,3,24,
        12,0,419,423,5,27,0,0,420,422,3,52,26,0,421,420,1,0,0,0,422,425,
        1,0,0,0,423,421,1,0,0,0,423,424,1,0,0,0,424,75,1,0,0,0,425,423,1,
        0,0,0,426,427,5,9,0,0,427,431,5,27,0,0,428,430,3,52,26,0,429,428,
        1,0,0,0,430,433,1,0,0,0,431,429,1,0,0,0,431,432,1,0,0,0,432,77,1,
        0,0,0,433,431,1,0,0,0,434,436,5,15,0,0,435,437,3,24,12,0,436,435,
        1,0,0,0,436,437,1,0,0,0,437,438,1,0,0,0,438,439,5,26,0,0,439,79,
        1,0,0,0,440,441,5,6,0,0,441,442,5,26,0,0,442,81,1,0,0,0,443,444,
        5,8,0,0,444,445,5,26,0,0,445,83,1,0,0,0,45,85,89,91,115,124,127,
        137,144,147,161,166,176,184,187,195,201,207,213,220,222,224,233,
        240,248,256,264,272,280,294,300,307,316,328,344,351,360,372,383,
        387,391,408,415,423,431,436
    ]

class TyCParser ( Parser ):

    grammarFileName = "TyC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'auto'", "'break'", "'case'", "'continue'", "'default'", 
                     "'else'", "'float'", "'for'", "'if'", "'int'", "'return'", 
                     "'string'", "'struct'", "'switch'", "'void'", "'while'", 
                     "','", "'('", "')'", "'{'", "'}'", "';'", "':'", "'++'", 
                     "'--'", "'<='", "'>='", "'=='", "'!='", "'&&'", "'||'", 
                     "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'<'", "'>'", 
                     "'!'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "WS", "BLOCK_COMMENT", "LINE_COMMENT", 
                      "AUTO", "BREAK", "CASE", "CONTINUE", "DEFAULT", "ELSE", 
                      "FLOAT", "FOR", "IF", "INT", "RETURN", "STRING", "STRUCT", 
                      "SWITCH", "VOID", "WHILE", "COMMA", "LEFT_PAREN", 
                      "RIGHT_PAREN", "LEFT_BRACE", "RIGHT_BRACE", "SEMICOLON", 
                      "COLON", "INCREMENT", "DECREMENT", "LESS_THAN_OR_EQUAL", 
                      "GREATER_THAN_OR_EQUAL", "EQUAL", "NOT_EQUAL", "LOGICAL_AND", 
                      "LOGICAL_OR", "ASSIGN", "PLUS", "MINUS", "MULTIPLY", 
                      "DIVIDE", "MODULUS", "LESS_THAN", "GREATER_THAN", 
                      "LOGICAL_NOT", "MEMBER_ACCESS", "ID", "INTEGER_LITERAL", 
                      "FLOAT_LITERAL", "STRING_LITERAL", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "ERROR_TOKEN" ]

    RULE_program = 0
    RULE_mainFunction = 1
    RULE_functionDeclaration = 2
    RULE_returnType = 3
    RULE_parameterList = 4
    RULE_parameter = 5
    RULE_argumentList = 6
    RULE_structDeclaration = 7
    RULE_structMemberList = 8
    RULE_structMember = 9
    RULE_structInit = 10
    RULE_variableDeclaration = 11
    RULE_expression = 12
    RULE_assignmentExpression = 13
    RULE_orExpression = 14
    RULE_andExpression = 15
    RULE_equalityExpression = 16
    RULE_relationalExpression = 17
    RULE_additiveExpression = 18
    RULE_multiplicativeExpression = 19
    RULE_unaryExpression = 20
    RULE_postfixExpression = 21
    RULE_memberExpression = 22
    RULE_memberOrCall = 23
    RULE_postfixIncDec = 24
    RULE_primaryExpression = 25
    RULE_statement = 26
    RULE_lvalue = 27
    RULE_expressionStatement = 28
    RULE_block = 29
    RULE_ifStatement = 30
    RULE_whileStatement = 31
    RULE_forStatement = 32
    RULE_forInit = 33
    RULE_forUpdate = 34
    RULE_switchStatement = 35
    RULE_switchClause = 36
    RULE_caseClause = 37
    RULE_defaultClause = 38
    RULE_returnStatement = 39
    RULE_breakStatement = 40
    RULE_continueStatement = 41

    ruleNames =  [ "program", "mainFunction", "functionDeclaration", "returnType", 
                   "parameterList", "parameter", "argumentList", "structDeclaration", 
                   "structMemberList", "structMember", "structInit", "variableDeclaration", 
                   "expression", "assignmentExpression", "orExpression", 
                   "andExpression", "equalityExpression", "relationalExpression", 
                   "additiveExpression", "multiplicativeExpression", "unaryExpression", 
                   "postfixExpression", "memberExpression", "memberOrCall", 
                   "postfixIncDec", "primaryExpression", "statement", "lvalue", 
                   "expressionStatement", "block", "ifStatement", "whileStatement", 
                   "forStatement", "forInit", "forUpdate", "switchStatement", 
                   "switchClause", "caseClause", "defaultClause", "returnStatement", 
                   "breakStatement", "continueStatement" ]

    EOF = Token.EOF
    T__0=1
    WS=2
    BLOCK_COMMENT=3
    LINE_COMMENT=4
    AUTO=5
    BREAK=6
    CASE=7
    CONTINUE=8
    DEFAULT=9
    ELSE=10
    FLOAT=11
    FOR=12
    IF=13
    INT=14
    RETURN=15
    STRING=16
    STRUCT=17
    SWITCH=18
    VOID=19
    WHILE=20
    COMMA=21
    LEFT_PAREN=22
    RIGHT_PAREN=23
    LEFT_BRACE=24
    RIGHT_BRACE=25
    SEMICOLON=26
    COLON=27
    INCREMENT=28
    DECREMENT=29
    LESS_THAN_OR_EQUAL=30
    GREATER_THAN_OR_EQUAL=31
    EQUAL=32
    NOT_EQUAL=33
    LOGICAL_AND=34
    LOGICAL_OR=35
    ASSIGN=36
    PLUS=37
    MINUS=38
    MULTIPLY=39
    DIVIDE=40
    MODULUS=41
    LESS_THAN=42
    GREATER_THAN=43
    LOGICAL_NOT=44
    MEMBER_ACCESS=45
    ID=46
    INTEGER_LITERAL=47
    FLOAT_LITERAL=48
    STRING_LITERAL=49
    ILLEGAL_ESCAPE=50
    UNCLOSE_STRING=51
    ERROR_TOKEN=52

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TyCParser.EOF, 0)

        def mainFunction(self):
            return self.getTypedRuleContext(TyCParser.MainFunctionContext,0)


        def structDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StructDeclarationContext)
            else:
                return self.getTypedRuleContext(TyCParser.StructDeclarationContext,i)


        def functionDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.FunctionDeclarationContext)
            else:
                return self.getTypedRuleContext(TyCParser.FunctionDeclarationContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_program




    def program(self):

        localctx = TyCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 84
                self.mainFunction()


            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 70368744916992) != 0):
                self.state = 89
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [17]:
                    self.state = 87
                    self.structDeclaration()
                    pass
                elif token in [11, 14, 16, 19, 46]:
                    self.state = 88
                    self.functionDeclaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 94
            self.match(TyCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(TyCParser.VOID, 0)

        def LEFT_PAREN(self):
            return self.getToken(TyCParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(TyCParser.RIGHT_PAREN, 0)

        def block(self):
            return self.getTypedRuleContext(TyCParser.BlockContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_mainFunction




    def mainFunction(self):

        localctx = TyCParser.MainFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mainFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(TyCParser.VOID)
            self.state = 97
            self.match(TyCParser.T__0)
            self.state = 98
            self.match(TyCParser.LEFT_PAREN)
            self.state = 99
            self.match(TyCParser.RIGHT_PAREN)
            self.state = 100
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def returnType(self):
            return self.getTypedRuleContext(TyCParser.ReturnTypeContext,0)


        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LEFT_PAREN(self):
            return self.getToken(TyCParser.LEFT_PAREN, 0)

        def parameterList(self):
            return self.getTypedRuleContext(TyCParser.ParameterListContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(TyCParser.RIGHT_PAREN, 0)

        def block(self):
            return self.getTypedRuleContext(TyCParser.BlockContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_functionDeclaration




    def functionDeclaration(self):

        localctx = TyCParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_functionDeclaration)
        try:
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.returnType()
                self.state = 103
                self.match(TyCParser.ID)
                self.state = 104
                self.match(TyCParser.LEFT_PAREN)
                self.state = 105
                self.parameterList()
                self.state = 106
                self.match(TyCParser.RIGHT_PAREN)
                self.state = 107
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.match(TyCParser.ID)
                self.state = 110
                self.match(TyCParser.LEFT_PAREN)
                self.state = 111
                self.parameterList()
                self.state = 112
                self.match(TyCParser.RIGHT_PAREN)
                self.state = 113
                self.block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TyCParser.INT, 0)

        def FLOAT(self):
            return self.getToken(TyCParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(TyCParser.STRING, 0)

        def VOID(self):
            return self.getToken(TyCParser.VOID, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_returnType




    def returnType(self):

        localctx = TyCParser.ReturnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_returnType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 70368744785920) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ParameterContext)
            else:
                return self.getTypedRuleContext(TyCParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.COMMA)
            else:
                return self.getToken(TyCParser.COMMA, i)

        def getRuleIndex(self):
            return TyCParser.RULE_parameterList




    def parameterList(self):

        localctx = TyCParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 70368744261632) != 0):
                self.state = 119
                self.parameter()
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==21:
                    self.state = 120
                    self.match(TyCParser.COMMA)
                    self.state = 121
                    self.parameter()
                    self.state = 126
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TyCParser.INT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.ID)
            else:
                return self.getToken(TyCParser.ID, i)

        def FLOAT(self):
            return self.getToken(TyCParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(TyCParser.STRING, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_parameter




    def parameter(self):

        localctx = TyCParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_parameter)
        try:
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.match(TyCParser.INT)
                self.state = 130
                self.match(TyCParser.ID)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.match(TyCParser.FLOAT)
                self.state = 132
                self.match(TyCParser.ID)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 133
                self.match(TyCParser.STRING)
                self.state = 134
                self.match(TyCParser.ID)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 4)
                self.state = 135
                self.match(TyCParser.ID)
                self.state = 136
                self.match(TyCParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(TyCParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.COMMA)
            else:
                return self.getToken(TyCParser.COMMA, i)

        def getRuleIndex(self):
            return TyCParser.RULE_argumentList




    def argumentList(self):

        localctx = TyCParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073536475070464) != 0):
                self.state = 139
                self.expression()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==21:
                    self.state = 140
                    self.match(TyCParser.COMMA)
                    self.state = 141
                    self.expression()
                    self.state = 146
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(TyCParser.STRUCT, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LEFT_BRACE(self):
            return self.getToken(TyCParser.LEFT_BRACE, 0)

        def structMemberList(self):
            return self.getTypedRuleContext(TyCParser.StructMemberListContext,0)


        def RIGHT_BRACE(self):
            return self.getToken(TyCParser.RIGHT_BRACE, 0)

        def SEMICOLON(self):
            return self.getToken(TyCParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_structDeclaration




    def structDeclaration(self):

        localctx = TyCParser.StructDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_structDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(TyCParser.STRUCT)
            self.state = 150
            self.match(TyCParser.ID)
            self.state = 151
            self.match(TyCParser.LEFT_BRACE)
            self.state = 152
            self.structMemberList()
            self.state = 153
            self.match(TyCParser.RIGHT_BRACE)
            self.state = 154
            self.match(TyCParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructMemberListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structMember(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StructMemberContext)
            else:
                return self.getTypedRuleContext(TyCParser.StructMemberContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.SEMICOLON)
            else:
                return self.getToken(TyCParser.SEMICOLON, i)

        def getRuleIndex(self):
            return TyCParser.RULE_structMemberList




    def structMemberList(self):

        localctx = TyCParser.StructMemberListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_structMemberList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 70368744261632) != 0):
                self.state = 156
                self.structMember()
                self.state = 161
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 157
                        self.match(TyCParser.SEMICOLON)
                        self.state = 158
                        self.structMember() 
                    self.state = 163
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                self.state = 164
                self.match(TyCParser.SEMICOLON)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructMemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(TyCParser.INT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.ID)
            else:
                return self.getToken(TyCParser.ID, i)

        def FLOAT(self):
            return self.getToken(TyCParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(TyCParser.STRING, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_structMember




    def structMember(self):

        localctx = TyCParser.StructMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_structMember)
        try:
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.match(TyCParser.INT)
                self.state = 169
                self.match(TyCParser.ID)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.match(TyCParser.FLOAT)
                self.state = 171
                self.match(TyCParser.ID)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 172
                self.match(TyCParser.STRING)
                self.state = 173
                self.match(TyCParser.ID)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 4)
                self.state = 174
                self.match(TyCParser.ID)
                self.state = 175
                self.match(TyCParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACE(self):
            return self.getToken(TyCParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(TyCParser.RIGHT_BRACE, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(TyCParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.COMMA)
            else:
                return self.getToken(TyCParser.COMMA, i)

        def getRuleIndex(self):
            return TyCParser.RULE_structInit




    def structInit(self):

        localctx = TyCParser.StructInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_structInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(TyCParser.LEFT_BRACE)
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073536475070464) != 0):
                self.state = 179
                self.expression()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==21:
                    self.state = 180
                    self.match(TyCParser.COMMA)
                    self.state = 181
                    self.expression()
                    self.state = 186
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 189
            self.match(TyCParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AUTO(self):
            return self.getToken(TyCParser.AUTO, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.ID)
            else:
                return self.getToken(TyCParser.ID, i)

        def ASSIGN(self):
            return self.getToken(TyCParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(TyCParser.ExpressionContext,0)


        def INT(self):
            return self.getToken(TyCParser.INT, 0)

        def FLOAT(self):
            return self.getToken(TyCParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(TyCParser.STRING, 0)

        def structInit(self):
            return self.getTypedRuleContext(TyCParser.StructInitContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_variableDeclaration




    def variableDeclaration(self):

        localctx = TyCParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.match(TyCParser.AUTO)
                self.state = 192
                self.match(TyCParser.ID)
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36:
                    self.state = 193
                    self.match(TyCParser.ASSIGN)
                    self.state = 194
                    self.expression()


                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.match(TyCParser.INT)
                self.state = 198
                self.match(TyCParser.ID)
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36:
                    self.state = 199
                    self.match(TyCParser.ASSIGN)
                    self.state = 200
                    self.expression()


                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 203
                self.match(TyCParser.FLOAT)
                self.state = 204
                self.match(TyCParser.ID)
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36:
                    self.state = 205
                    self.match(TyCParser.ASSIGN)
                    self.state = 206
                    self.expression()


                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 209
                self.match(TyCParser.STRING)
                self.state = 210
                self.match(TyCParser.ID)
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36:
                    self.state = 211
                    self.match(TyCParser.ASSIGN)
                    self.state = 212
                    self.expression()


                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 5)
                self.state = 215
                self.match(TyCParser.ID)
                self.state = 216
                self.match(TyCParser.ID)
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36:
                    self.state = 217
                    self.match(TyCParser.ASSIGN)
                    self.state = 220
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [22, 28, 29, 37, 38, 44, 46, 47, 48, 49]:
                        self.state = 218
                        self.expression()
                        pass
                    elif token in [24]:
                        self.state = 219
                        self.structInit()
                        pass
                    else:
                        raise NoViableAltException(self)



                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentExpression(self):
            return self.getTypedRuleContext(TyCParser.AssignmentExpressionContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_expression




    def expression(self):

        localctx = TyCParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.assignmentExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvalue(self):
            return self.getTypedRuleContext(TyCParser.LvalueContext,0)


        def ASSIGN(self):
            return self.getToken(TyCParser.ASSIGN, 0)

        def assignmentExpression(self):
            return self.getTypedRuleContext(TyCParser.AssignmentExpressionContext,0)


        def orExpression(self):
            return self.getTypedRuleContext(TyCParser.OrExpressionContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_assignmentExpression




    def assignmentExpression(self):

        localctx = TyCParser.AssignmentExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_assignmentExpression)
        try:
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.lvalue()
                self.state = 229
                self.match(TyCParser.ASSIGN)
                self.state = 230
                self.assignmentExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.orExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.AndExpressionContext)
            else:
                return self.getTypedRuleContext(TyCParser.AndExpressionContext,i)


        def LOGICAL_OR(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.LOGICAL_OR)
            else:
                return self.getToken(TyCParser.LOGICAL_OR, i)

        def getRuleIndex(self):
            return TyCParser.RULE_orExpression




    def orExpression(self):

        localctx = TyCParser.OrExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_orExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.andExpression()
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==35:
                self.state = 236
                self.match(TyCParser.LOGICAL_OR)
                self.state = 237
                self.andExpression()
                self.state = 242
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.EqualityExpressionContext)
            else:
                return self.getTypedRuleContext(TyCParser.EqualityExpressionContext,i)


        def LOGICAL_AND(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.LOGICAL_AND)
            else:
                return self.getToken(TyCParser.LOGICAL_AND, i)

        def getRuleIndex(self):
            return TyCParser.RULE_andExpression




    def andExpression(self):

        localctx = TyCParser.AndExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_andExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.equalityExpression()
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 244
                self.match(TyCParser.LOGICAL_AND)
                self.state = 245
                self.equalityExpression()
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.RelationalExpressionContext)
            else:
                return self.getTypedRuleContext(TyCParser.RelationalExpressionContext,i)


        def EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.EQUAL)
            else:
                return self.getToken(TyCParser.EQUAL, i)

        def NOT_EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.NOT_EQUAL)
            else:
                return self.getToken(TyCParser.NOT_EQUAL, i)

        def getRuleIndex(self):
            return TyCParser.RULE_equalityExpression




    def equalityExpression(self):

        localctx = TyCParser.EqualityExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_equalityExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.relationalExpression()
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32 or _la==33:
                self.state = 252
                _la = self._input.LA(1)
                if not(_la==32 or _la==33):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 253
                self.relationalExpression()
                self.state = 258
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.AdditiveExpressionContext)
            else:
                return self.getTypedRuleContext(TyCParser.AdditiveExpressionContext,i)


        def LESS_THAN(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.LESS_THAN)
            else:
                return self.getToken(TyCParser.LESS_THAN, i)

        def LESS_THAN_OR_EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.LESS_THAN_OR_EQUAL)
            else:
                return self.getToken(TyCParser.LESS_THAN_OR_EQUAL, i)

        def GREATER_THAN(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.GREATER_THAN)
            else:
                return self.getToken(TyCParser.GREATER_THAN, i)

        def GREATER_THAN_OR_EQUAL(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.GREATER_THAN_OR_EQUAL)
            else:
                return self.getToken(TyCParser.GREATER_THAN_OR_EQUAL, i)

        def getRuleIndex(self):
            return TyCParser.RULE_relationalExpression




    def relationalExpression(self):

        localctx = TyCParser.RelationalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_relationalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.additiveExpression()
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 13197360758784) != 0):
                self.state = 260
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 13197360758784) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 261
                self.additiveExpression()
                self.state = 266
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(TyCParser.MultiplicativeExpressionContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.PLUS)
            else:
                return self.getToken(TyCParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.MINUS)
            else:
                return self.getToken(TyCParser.MINUS, i)

        def getRuleIndex(self):
            return TyCParser.RULE_additiveExpression




    def additiveExpression(self):

        localctx = TyCParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.multiplicativeExpression()
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37 or _la==38:
                self.state = 268
                _la = self._input.LA(1)
                if not(_la==37 or _la==38):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 269
                self.multiplicativeExpression()
                self.state = 274
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.UnaryExpressionContext)
            else:
                return self.getTypedRuleContext(TyCParser.UnaryExpressionContext,i)


        def MULTIPLY(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.MULTIPLY)
            else:
                return self.getToken(TyCParser.MULTIPLY, i)

        def DIVIDE(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.DIVIDE)
            else:
                return self.getToken(TyCParser.DIVIDE, i)

        def MODULUS(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.MODULUS)
            else:
                return self.getToken(TyCParser.MODULUS, i)

        def getRuleIndex(self):
            return TyCParser.RULE_multiplicativeExpression




    def multiplicativeExpression(self):

        localctx = TyCParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.unaryExpression()
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3848290697216) != 0):
                self.state = 276
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3848290697216) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 277
                self.unaryExpression()
                self.state = 282
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INCREMENT(self):
            return self.getToken(TyCParser.INCREMENT, 0)

        def unaryExpression(self):
            return self.getTypedRuleContext(TyCParser.UnaryExpressionContext,0)


        def DECREMENT(self):
            return self.getToken(TyCParser.DECREMENT, 0)

        def MINUS(self):
            return self.getToken(TyCParser.MINUS, 0)

        def PLUS(self):
            return self.getToken(TyCParser.PLUS, 0)

        def LOGICAL_NOT(self):
            return self.getToken(TyCParser.LOGICAL_NOT, 0)

        def postfixExpression(self):
            return self.getTypedRuleContext(TyCParser.PostfixExpressionContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_unaryExpression




    def unaryExpression(self):

        localctx = TyCParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_unaryExpression)
        try:
            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.match(TyCParser.INCREMENT)
                self.state = 284
                self.unaryExpression()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
                self.match(TyCParser.DECREMENT)
                self.state = 286
                self.unaryExpression()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 3)
                self.state = 287
                self.match(TyCParser.MINUS)
                self.state = 288
                self.unaryExpression()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 4)
                self.state = 289
                self.match(TyCParser.PLUS)
                self.state = 290
                self.unaryExpression()
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 5)
                self.state = 291
                self.match(TyCParser.LOGICAL_NOT)
                self.state = 292
                self.unaryExpression()
                pass
            elif token in [22, 46, 47, 48, 49]:
                self.enterOuterAlt(localctx, 6)
                self.state = 293
                self.postfixExpression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def memberExpression(self):
            return self.getTypedRuleContext(TyCParser.MemberExpressionContext,0)


        def postfixIncDec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.PostfixIncDecContext)
            else:
                return self.getTypedRuleContext(TyCParser.PostfixIncDecContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_postfixExpression




    def postfixExpression(self):

        localctx = TyCParser.PostfixExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_postfixExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.memberExpression()
            self.state = 300
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28 or _la==29:
                self.state = 297
                self.postfixIncDec()
                self.state = 302
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpression(self):
            return self.getTypedRuleContext(TyCParser.PrimaryExpressionContext,0)


        def memberOrCall(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.MemberOrCallContext)
            else:
                return self.getTypedRuleContext(TyCParser.MemberOrCallContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_memberExpression




    def memberExpression(self):

        localctx = TyCParser.MemberExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_memberExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.primaryExpression()
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22 or _la==45:
                self.state = 304
                self.memberOrCall()
                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberOrCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MEMBER_ACCESS(self):
            return self.getToken(TyCParser.MEMBER_ACCESS, 0)

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def LEFT_PAREN(self):
            return self.getToken(TyCParser.LEFT_PAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(TyCParser.ArgumentListContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(TyCParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_memberOrCall




    def memberOrCall(self):

        localctx = TyCParser.MemberOrCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_memberOrCall)
        try:
            self.state = 316
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.match(TyCParser.MEMBER_ACCESS)
                self.state = 311
                self.match(TyCParser.ID)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
                self.match(TyCParser.LEFT_PAREN)
                self.state = 313
                self.argumentList()
                self.state = 314
                self.match(TyCParser.RIGHT_PAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixIncDecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INCREMENT(self):
            return self.getToken(TyCParser.INCREMENT, 0)

        def DECREMENT(self):
            return self.getToken(TyCParser.DECREMENT, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_postfixIncDec




    def postfixIncDec(self):

        localctx = TyCParser.PostfixIncDecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_postfixIncDec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TyCParser.ID, 0)

        def INTEGER_LITERAL(self):
            return self.getToken(TyCParser.INTEGER_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(TyCParser.FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(TyCParser.STRING_LITERAL, 0)

        def LEFT_PAREN(self):
            return self.getToken(TyCParser.LEFT_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(TyCParser.ExpressionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(TyCParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_primaryExpression




    def primaryExpression(self):

        localctx = TyCParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_primaryExpression)
        try:
            self.state = 328
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.match(TyCParser.ID)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.match(TyCParser.INTEGER_LITERAL)
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 3)
                self.state = 322
                self.match(TyCParser.FLOAT_LITERAL)
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 4)
                self.state = 323
                self.match(TyCParser.STRING_LITERAL)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 5)
                self.state = 324
                self.match(TyCParser.LEFT_PAREN)
                self.state = 325
                self.expression()
                self.state = 326
                self.match(TyCParser.RIGHT_PAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(TyCParser.VariableDeclarationContext,0)


        def SEMICOLON(self):
            return self.getToken(TyCParser.SEMICOLON, 0)

        def expressionStatement(self):
            return self.getTypedRuleContext(TyCParser.ExpressionStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(TyCParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(TyCParser.WhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(TyCParser.ForStatementContext,0)


        def switchStatement(self):
            return self.getTypedRuleContext(TyCParser.SwitchStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(TyCParser.ReturnStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(TyCParser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(TyCParser.ContinueStatementContext,0)


        def block(self):
            return self.getTypedRuleContext(TyCParser.BlockContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_statement




    def statement(self):

        localctx = TyCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_statement)
        try:
            self.state = 344
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.variableDeclaration()
                self.state = 331
                self.match(TyCParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
                self.expressionStatement()
                self.state = 334
                self.match(TyCParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 336
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 337
                self.whileStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 338
                self.forStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 339
                self.switchStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 340
                self.returnStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 341
                self.breakStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 342
                self.continueStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 343
                self.block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.ID)
            else:
                return self.getToken(TyCParser.ID, i)

        def MEMBER_ACCESS(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.MEMBER_ACCESS)
            else:
                return self.getToken(TyCParser.MEMBER_ACCESS, i)

        def getRuleIndex(self):
            return TyCParser.RULE_lvalue




    def lvalue(self):

        localctx = TyCParser.LvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_lvalue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(TyCParser.ID)
            self.state = 351
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 347
                self.match(TyCParser.MEMBER_ACCESS)
                self.state = 348
                self.match(TyCParser.ID)
                self.state = 353
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(TyCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_expressionStatement




    def expressionStatement(self):

        localctx = TyCParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACE(self):
            return self.getToken(TyCParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(TyCParser.RIGHT_BRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StatementContext)
            else:
                return self.getTypedRuleContext(TyCParser.StatementContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_block




    def block(self):

        localctx = TyCParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.match(TyCParser.LEFT_BRACE)
            self.state = 360
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073536493287776) != 0):
                self.state = 357
                self.statement()
                self.state = 362
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 363
            self.match(TyCParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(TyCParser.IF, 0)

        def LEFT_PAREN(self):
            return self.getToken(TyCParser.LEFT_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(TyCParser.ExpressionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(TyCParser.RIGHT_PAREN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StatementContext)
            else:
                return self.getTypedRuleContext(TyCParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(TyCParser.ELSE, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_ifStatement




    def ifStatement(self):

        localctx = TyCParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(TyCParser.IF)
            self.state = 366
            self.match(TyCParser.LEFT_PAREN)
            self.state = 367
            self.expression()
            self.state = 368
            self.match(TyCParser.RIGHT_PAREN)
            self.state = 369
            self.statement()
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 370
                self.match(TyCParser.ELSE)
                self.state = 371
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(TyCParser.WHILE, 0)

        def LEFT_PAREN(self):
            return self.getToken(TyCParser.LEFT_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(TyCParser.ExpressionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(TyCParser.RIGHT_PAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(TyCParser.StatementContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_whileStatement




    def whileStatement(self):

        localctx = TyCParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(TyCParser.WHILE)
            self.state = 375
            self.match(TyCParser.LEFT_PAREN)
            self.state = 376
            self.expression()
            self.state = 377
            self.match(TyCParser.RIGHT_PAREN)
            self.state = 378
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(TyCParser.FOR, 0)

        def LEFT_PAREN(self):
            return self.getToken(TyCParser.LEFT_PAREN, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(TyCParser.SEMICOLON)
            else:
                return self.getToken(TyCParser.SEMICOLON, i)

        def RIGHT_PAREN(self):
            return self.getToken(TyCParser.RIGHT_PAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(TyCParser.StatementContext,0)


        def forInit(self):
            return self.getTypedRuleContext(TyCParser.ForInitContext,0)


        def expression(self):
            return self.getTypedRuleContext(TyCParser.ExpressionContext,0)


        def forUpdate(self):
            return self.getTypedRuleContext(TyCParser.ForUpdateContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_forStatement




    def forStatement(self):

        localctx = TyCParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(TyCParser.FOR)
            self.state = 381
            self.match(TyCParser.LEFT_PAREN)
            self.state = 383
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 70368744261664) != 0):
                self.state = 382
                self.forInit()


            self.state = 385
            self.match(TyCParser.SEMICOLON)
            self.state = 387
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073536475070464) != 0):
                self.state = 386
                self.expression()


            self.state = 389
            self.match(TyCParser.SEMICOLON)
            self.state = 391
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073536475070464) != 0):
                self.state = 390
                self.forUpdate()


            self.state = 393
            self.match(TyCParser.RIGHT_PAREN)
            self.state = 394
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(TyCParser.VariableDeclarationContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_forInit




    def forInit(self):

        localctx = TyCParser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_forInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.variableDeclaration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForUpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(TyCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_forUpdate




    def forUpdate(self):

        localctx = TyCParser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(TyCParser.SWITCH, 0)

        def LEFT_PAREN(self):
            return self.getToken(TyCParser.LEFT_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(TyCParser.ExpressionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(TyCParser.RIGHT_PAREN, 0)

        def LEFT_BRACE(self):
            return self.getToken(TyCParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(TyCParser.RIGHT_BRACE, 0)

        def switchClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.SwitchClauseContext)
            else:
                return self.getTypedRuleContext(TyCParser.SwitchClauseContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_switchStatement




    def switchStatement(self):

        localctx = TyCParser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_switchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.match(TyCParser.SWITCH)
            self.state = 401
            self.match(TyCParser.LEFT_PAREN)
            self.state = 402
            self.expression()
            self.state = 403
            self.match(TyCParser.RIGHT_PAREN)
            self.state = 404
            self.match(TyCParser.LEFT_BRACE)
            self.state = 408
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==9:
                self.state = 405
                self.switchClause()
                self.state = 410
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 411
            self.match(TyCParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def caseClause(self):
            return self.getTypedRuleContext(TyCParser.CaseClauseContext,0)


        def defaultClause(self):
            return self.getTypedRuleContext(TyCParser.DefaultClauseContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_switchClause




    def switchClause(self):

        localctx = TyCParser.SwitchClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_switchClause)
        try:
            self.state = 415
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self.caseClause()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 414
                self.defaultClause()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(TyCParser.CASE, 0)

        def expression(self):
            return self.getTypedRuleContext(TyCParser.ExpressionContext,0)


        def COLON(self):
            return self.getToken(TyCParser.COLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StatementContext)
            else:
                return self.getTypedRuleContext(TyCParser.StatementContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_caseClause




    def caseClause(self):

        localctx = TyCParser.CaseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_caseClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.match(TyCParser.CASE)
            self.state = 418
            self.expression()
            self.state = 419
            self.match(TyCParser.COLON)
            self.state = 423
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073536493287776) != 0):
                self.state = 420
                self.statement()
                self.state = 425
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT(self):
            return self.getToken(TyCParser.DEFAULT, 0)

        def COLON(self):
            return self.getToken(TyCParser.COLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TyCParser.StatementContext)
            else:
                return self.getTypedRuleContext(TyCParser.StatementContext,i)


        def getRuleIndex(self):
            return TyCParser.RULE_defaultClause




    def defaultClause(self):

        localctx = TyCParser.DefaultClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_defaultClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(TyCParser.DEFAULT)
            self.state = 427
            self.match(TyCParser.COLON)
            self.state = 431
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073536493287776) != 0):
                self.state = 428
                self.statement()
                self.state = 433
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(TyCParser.RETURN, 0)

        def SEMICOLON(self):
            return self.getToken(TyCParser.SEMICOLON, 0)

        def expression(self):
            return self.getTypedRuleContext(TyCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return TyCParser.RULE_returnStatement




    def returnStatement(self):

        localctx = TyCParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.match(TyCParser.RETURN)
            self.state = 436
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073536475070464) != 0):
                self.state = 435
                self.expression()


            self.state = 438
            self.match(TyCParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(TyCParser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(TyCParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_breakStatement




    def breakStatement(self):

        localctx = TyCParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.match(TyCParser.BREAK)
            self.state = 441
            self.match(TyCParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(TyCParser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(TyCParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return TyCParser.RULE_continueStatement




    def continueStatement(self):

        localctx = TyCParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.match(TyCParser.CONTINUE)
            self.state = 444
            self.match(TyCParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





