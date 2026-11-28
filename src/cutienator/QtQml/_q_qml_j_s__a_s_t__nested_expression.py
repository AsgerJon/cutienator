"""
QQmlJS::AST::NestedExpression binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlJS::AST::NestedExpression to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import WAIT
from . import QQmlJS

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class NestedExpression(QQmlJS.AST.LeftHandSideExpression):
  """
  The cute side of Qt's QQmlJS::AST::NestedExpression: a plain Python object
  standing in front of one C++ QQmlJS::AST::NestedExpression.

  It is built on the cute 'QQmlJS::AST::LeftHandSideExpression', as Qt's
  QQmlJS::AST::NestedExpression is built on Qt's
  QQmlJS::AST::LeftHandSideExpression, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlJS::AST::NestedExpression that has a ritual and
  that Python can call so far, 4 names in all: 'firstSourceLocation',
  'lastSourceLocation', 'asFunctionDefinition', 'asClassDefinition'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJS::AST::NestedExpression::NestedExpression(ExpressionNode
    *expression)': names 'QQmlJS::AST::ExpressionNode', which has no cute
    class yet.
  - Qt's 'void QQmlJS::AST::NestedExpression::accept0(BaseVisitor *visitor)':
    names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.

  What to expect
  --------------

  - The C++ QQmlJS::AST::NestedExpression is created at the first use, not by
    'QQmlJS::AST::NestedExpression(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJS::AST::NestedExpression.
  - Each name of Qt's QQmlJS::AST::NestedExpression that has no cute function
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
  __qt_class__ = 'QQmlJS::AST::NestedExpression'

  #  A C++ QQmlJS::AST::NestedExpression Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJS_AST_NestedExpression'

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
    QQmlJS::AST::NestedExpression::firstSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-nestedexpression.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::NestedExpression::firstSourceLocation()
    #      const
    ritual = 'ritual_ZNK6QQmlJS3AST16NestedExpression19firstSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST16NestedExpression19firstSourceLocation'
          'Ev')
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def lastSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::NestedExpression::lastSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-nestedexpression.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::NestedExpression::lastSourceLocation()
    #      const
    ritual = 'ritual_ZNK6QQmlJS3AST16NestedExpression18lastSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST16NestedExpression18lastSourceLocationE'
          'v')
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

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
    Qt's 'QQmlJS::AST::NestedExpression::NestedExpression(ExpressionNode
    *expression)': names 'QQmlJS::AST::ExpressionNode', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.NestedExpression.__init__' has no cute function yet. "
        "Qt's "
        "'QQmlJS::AST::NestedExpression::NestedExpression(ExpressionNode "
        "*expression)': names 'QQmlJS::AST::ExpressionNode', which has no "
        "cute class yet.")

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

  def asFunctionDefinition(self) -> Optional[QQmlJS.AST.FunctionExpression]:
    """
    Calls Qt's 'FunctionExpression
    *QQmlJS::AST::NestedExpression::asFunctionDefinition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-nestedexpression.html

    Returns
    -------

    Optional[QQmlJS.AST.FunctionExpression]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FunctionExpression
    #      *QQmlJS::AST::NestedExpression::asFunctionDefinition()
    ritual = 'ritual_ZN6QQmlJS3AST16NestedExpression20asFunctionDefinitionEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST16NestedExpression20asFunctionDefinition'
          'Ev')
    address = self.uglySide.call(ritual)
    return QQmlJS.AST.FunctionExpression._cuteAt(address)

  def asClassDefinition(self) -> Optional[QQmlJS.AST.ClassExpression]:
    """
    Calls Qt's 'ClassExpression
    *QQmlJS::AST::NestedExpression::asClassDefinition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-nestedexpression.html#asClassDefinition

    Returns
    -------

    Optional[QQmlJS.AST.ClassExpression]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ClassExpression *QQmlJS::AST::NestedExpression::asClassDefinition()
    ritual = 'ritual_ZN6QQmlJS3AST16NestedExpression17asClassDefinitionEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST16NestedExpression17asClassDefinitionEv')
    address = self.uglySide.call(ritual)
    return QQmlJS.AST.ClassExpression._cuteAt(address)

  @staticmethod
  def accept0(*__, **_) -> Never:
    """
    Qt's 'void QQmlJS::AST::NestedExpression::accept0(BaseVisitor *visitor)':
    names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.NestedExpression.accept0' has no cute function yet. "
        "Qt's 'void QQmlJS::AST::NestedExpression::accept0(BaseVisitor "
        "*visitor)': names 'QQmlJS::AST::BaseVisitor', which has no cute "
        "class yet.")
