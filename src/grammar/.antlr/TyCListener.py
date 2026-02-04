# Generated from /Users/codeleap/Uni/PPL/assignment/assignment1/tyc-compiler/src/grammar/TyC.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
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


    # Enter a parse tree produced by TyCParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:TyCParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by TyCParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:TyCParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by TyCParser#returnType.
    def enterReturnType(self, ctx:TyCParser.ReturnTypeContext):
        pass

    # Exit a parse tree produced by TyCParser#returnType.
    def exitReturnType(self, ctx:TyCParser.ReturnTypeContext):
        pass


    # Enter a parse tree produced by TyCParser#parameterList.
    def enterParameterList(self, ctx:TyCParser.ParameterListContext):
        pass

    # Exit a parse tree produced by TyCParser#parameterList.
    def exitParameterList(self, ctx:TyCParser.ParameterListContext):
        pass


    # Enter a parse tree produced by TyCParser#parameter.
    def enterParameter(self, ctx:TyCParser.ParameterContext):
        pass

    # Exit a parse tree produced by TyCParser#parameter.
    def exitParameter(self, ctx:TyCParser.ParameterContext):
        pass


    # Enter a parse tree produced by TyCParser#argumentList.
    def enterArgumentList(self, ctx:TyCParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by TyCParser#argumentList.
    def exitArgumentList(self, ctx:TyCParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by TyCParser#structDeclaration.
    def enterStructDeclaration(self, ctx:TyCParser.StructDeclarationContext):
        pass

    # Exit a parse tree produced by TyCParser#structDeclaration.
    def exitStructDeclaration(self, ctx:TyCParser.StructDeclarationContext):
        pass


    # Enter a parse tree produced by TyCParser#structMemberList.
    def enterStructMemberList(self, ctx:TyCParser.StructMemberListContext):
        pass

    # Exit a parse tree produced by TyCParser#structMemberList.
    def exitStructMemberList(self, ctx:TyCParser.StructMemberListContext):
        pass


    # Enter a parse tree produced by TyCParser#structMember.
    def enterStructMember(self, ctx:TyCParser.StructMemberContext):
        pass

    # Exit a parse tree produced by TyCParser#structMember.
    def exitStructMember(self, ctx:TyCParser.StructMemberContext):
        pass


    # Enter a parse tree produced by TyCParser#structInit.
    def enterStructInit(self, ctx:TyCParser.StructInitContext):
        pass

    # Exit a parse tree produced by TyCParser#structInit.
    def exitStructInit(self, ctx:TyCParser.StructInitContext):
        pass


    # Enter a parse tree produced by TyCParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:TyCParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by TyCParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:TyCParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by TyCParser#expression.
    def enterExpression(self, ctx:TyCParser.ExpressionContext):
        pass

    # Exit a parse tree produced by TyCParser#expression.
    def exitExpression(self, ctx:TyCParser.ExpressionContext):
        pass


    # Enter a parse tree produced by TyCParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:TyCParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by TyCParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:TyCParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by TyCParser#orExpression.
    def enterOrExpression(self, ctx:TyCParser.OrExpressionContext):
        pass

    # Exit a parse tree produced by TyCParser#orExpression.
    def exitOrExpression(self, ctx:TyCParser.OrExpressionContext):
        pass


    # Enter a parse tree produced by TyCParser#andExpression.
    def enterAndExpression(self, ctx:TyCParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by TyCParser#andExpression.
    def exitAndExpression(self, ctx:TyCParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by TyCParser#equalityExpression.
    def enterEqualityExpression(self, ctx:TyCParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by TyCParser#equalityExpression.
    def exitEqualityExpression(self, ctx:TyCParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by TyCParser#relationalExpression.
    def enterRelationalExpression(self, ctx:TyCParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by TyCParser#relationalExpression.
    def exitRelationalExpression(self, ctx:TyCParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by TyCParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:TyCParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by TyCParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:TyCParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by TyCParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:TyCParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by TyCParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:TyCParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by TyCParser#unaryExpression.
    def enterUnaryExpression(self, ctx:TyCParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by TyCParser#unaryExpression.
    def exitUnaryExpression(self, ctx:TyCParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by TyCParser#postfixExpression.
    def enterPostfixExpression(self, ctx:TyCParser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by TyCParser#postfixExpression.
    def exitPostfixExpression(self, ctx:TyCParser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by TyCParser#postfixOp.
    def enterPostfixOp(self, ctx:TyCParser.PostfixOpContext):
        pass

    # Exit a parse tree produced by TyCParser#postfixOp.
    def exitPostfixOp(self, ctx:TyCParser.PostfixOpContext):
        pass


    # Enter a parse tree produced by TyCParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:TyCParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by TyCParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:TyCParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by TyCParser#statement.
    def enterStatement(self, ctx:TyCParser.StatementContext):
        pass

    # Exit a parse tree produced by TyCParser#statement.
    def exitStatement(self, ctx:TyCParser.StatementContext):
        pass


    # Enter a parse tree produced by TyCParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:TyCParser.AssignmentStatementContext):
        pass

    # Exit a parse tree produced by TyCParser#assignmentStatement.
    def exitAssignmentStatement(self, ctx:TyCParser.AssignmentStatementContext):
        pass


    # Enter a parse tree produced by TyCParser#lvalue.
    def enterLvalue(self, ctx:TyCParser.LvalueContext):
        pass

    # Exit a parse tree produced by TyCParser#lvalue.
    def exitLvalue(self, ctx:TyCParser.LvalueContext):
        pass


    # Enter a parse tree produced by TyCParser#expressionStatement.
    def enterExpressionStatement(self, ctx:TyCParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by TyCParser#expressionStatement.
    def exitExpressionStatement(self, ctx:TyCParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by TyCParser#block.
    def enterBlock(self, ctx:TyCParser.BlockContext):
        pass

    # Exit a parse tree produced by TyCParser#block.
    def exitBlock(self, ctx:TyCParser.BlockContext):
        pass


    # Enter a parse tree produced by TyCParser#ifStatement.
    def enterIfStatement(self, ctx:TyCParser.IfStatementContext):
        pass

    # Exit a parse tree produced by TyCParser#ifStatement.
    def exitIfStatement(self, ctx:TyCParser.IfStatementContext):
        pass


    # Enter a parse tree produced by TyCParser#whileStatement.
    def enterWhileStatement(self, ctx:TyCParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by TyCParser#whileStatement.
    def exitWhileStatement(self, ctx:TyCParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by TyCParser#forStatement.
    def enterForStatement(self, ctx:TyCParser.ForStatementContext):
        pass

    # Exit a parse tree produced by TyCParser#forStatement.
    def exitForStatement(self, ctx:TyCParser.ForStatementContext):
        pass


    # Enter a parse tree produced by TyCParser#forInit.
    def enterForInit(self, ctx:TyCParser.ForInitContext):
        pass

    # Exit a parse tree produced by TyCParser#forInit.
    def exitForInit(self, ctx:TyCParser.ForInitContext):
        pass


    # Enter a parse tree produced by TyCParser#forUpdate.
    def enterForUpdate(self, ctx:TyCParser.ForUpdateContext):
        pass

    # Exit a parse tree produced by TyCParser#forUpdate.
    def exitForUpdate(self, ctx:TyCParser.ForUpdateContext):
        pass


    # Enter a parse tree produced by TyCParser#switchStatement.
    def enterSwitchStatement(self, ctx:TyCParser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by TyCParser#switchStatement.
    def exitSwitchStatement(self, ctx:TyCParser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by TyCParser#caseClause.
    def enterCaseClause(self, ctx:TyCParser.CaseClauseContext):
        pass

    # Exit a parse tree produced by TyCParser#caseClause.
    def exitCaseClause(self, ctx:TyCParser.CaseClauseContext):
        pass


    # Enter a parse tree produced by TyCParser#defaultClause.
    def enterDefaultClause(self, ctx:TyCParser.DefaultClauseContext):
        pass

    # Exit a parse tree produced by TyCParser#defaultClause.
    def exitDefaultClause(self, ctx:TyCParser.DefaultClauseContext):
        pass


    # Enter a parse tree produced by TyCParser#returnStatement.
    def enterReturnStatement(self, ctx:TyCParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by TyCParser#returnStatement.
    def exitReturnStatement(self, ctx:TyCParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by TyCParser#breakStatement.
    def enterBreakStatement(self, ctx:TyCParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by TyCParser#breakStatement.
    def exitBreakStatement(self, ctx:TyCParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by TyCParser#continueStatement.
    def enterContinueStatement(self, ctx:TyCParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by TyCParser#continueStatement.
    def exitContinueStatement(self, ctx:TyCParser.ContinueStatementContext):
        pass



del TyCParser