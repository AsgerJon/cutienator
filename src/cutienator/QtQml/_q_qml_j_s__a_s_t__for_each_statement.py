"""
QQmlJS::AST::ForEachStatement binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlJS::AST::ForEachStatement to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute, WAIT
from . import QQmlJS

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class ForEachStatement(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::AST::ForEachStatement: a plain Python object
  standing in front of one C++ QQmlJS::AST::ForEachStatement.

  What exists
  -----------

  Every function of Qt's QQmlJS::AST::ForEachStatement that has a ritual and
  that Python can call so far, 3 names in all: 'firstSourceLocation',
  'lastSourceLocation', 'declaration'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJS::AST::ForEachStatement::ForEachStatement(ExpressionNode *i,
    ExpressionNode *e, Statement *stmt)': names
    'QQmlJS::AST::ExpressionNode', which has no cute class yet.
  - Qt's 'QQmlJS::AST::ForEachStatement::ForEachStatement(PatternElement *v,
    ExpressionNode *e, Statement *stmt)': names
    'QQmlJS::AST::ExpressionNode', which has no cute class yet.
  - Qt's 'void QQmlJS::AST::ForEachStatement::accept0(BaseVisitor *visitor)':
    names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.

  What to expect
  --------------

  - The C++ QQmlJS::AST::ForEachStatement is created at the first use, not by
    'QQmlJS::AST::ForEachStatement(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJS::AST::ForEachStatement.
  - Each name of Qt's QQmlJS::AST::ForEachStatement that has no cute function
    yet, '__init__', 'accept0', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJS::AST::ForEachStatement'

  #  A C++ QQmlJS::AST::ForEachStatement Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJS_AST_ForEachStatement'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def firstSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::ForEachStatement::firstSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-foreachstatement.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::ForEachStatement::firstSourceLocation()
    #      const
    ritual = 'ritual_ZNK6QQmlJS3AST16ForEachStatement19firstSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST16ForEachStatement19firstSourceLocation'
          'Ev')
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def lastSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::ForEachStatement::lastSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-foreachstatement.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::ForEachStatement::lastSourceLocation()
    #      const
    ritual = 'ritual_ZNK6QQmlJS3AST16ForEachStatement18lastSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST16ForEachStatement18lastSourceLocationE'
          'v')
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def declaration(self) -> Optional[QQmlJS.AST.PatternElement]:
    """
    Calls Qt's 'PatternElement *QQmlJS::AST::ForEachStatement::declaration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-foreachstatement.html#declaration

    Returns
    -------

    Optional[QQmlJS.AST.PatternElement]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  PatternElement *QQmlJS::AST::ForEachStatement::declaration() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST16ForEachStatement11declarationEv',
    )
    return QQmlJS.AST.PatternElement._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QQmlJS::AST::ForEachStatement::ForEachStatement(ExpressionNode
      *i, ExpressionNode *e, Statement *stmt)': names
      'QQmlJS::AST::ExpressionNode', which has no cute class yet.
    - Qt's 'QQmlJS::AST::ForEachStatement::ForEachStatement(PatternElement
      *v, ExpressionNode *e, Statement *stmt)': names
      'QQmlJS::AST::ExpressionNode', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.ForEachStatement.__init__' has no cute function yet. "
        "Qt's "
        "'QQmlJS::AST::ForEachStatement::ForEachStatement(ExpressionNode "
        "*i, ExpressionNode *e, Statement *stmt)': names "
        "'QQmlJS::AST::ExpressionNode', which has no cute class yet. Qt's "
        "'QQmlJS::AST::ForEachStatement::ForEachStatement(PatternElement "
        "*v, ExpressionNode *e, Statement *stmt)': names "
        "'QQmlJS::AST::ExpressionNode', which has no cute class yet.")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def accept0(*__, **_) -> Never:
    """
    Qt's 'void QQmlJS::AST::ForEachStatement::accept0(BaseVisitor *visitor)':
    names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.ForEachStatement.accept0' has no cute function yet. "
        "Qt's 'void QQmlJS::AST::ForEachStatement::accept0(BaseVisitor "
        "*visitor)': names 'QQmlJS::AST::BaseVisitor', which has no cute "
        "class yet.")
