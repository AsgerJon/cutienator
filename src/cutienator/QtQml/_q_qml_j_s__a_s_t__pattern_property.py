"""
QQmlJS::AST::PatternProperty binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlJS::AST::PatternProperty to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QQmlJS

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QString
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QString = WAIT['QString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PatternProperty(QQmlJS.AST.PatternElement):
  """
  The cute side of Qt's QQmlJS::AST::PatternProperty: a plain Python object
  standing in front of one C++ QQmlJS::AST::PatternProperty.

  It is built on the cute 'QQmlJS::AST::PatternElement', as Qt's
  QQmlJS::AST::PatternProperty is built on Qt's QQmlJS::AST::PatternElement,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlJS::AST::PatternProperty that has a ritual and
  that Python can call so far, 4 names in all: 'firstSourceLocation',
  'lastSourceLocation', 'boundNames', 'convertLiteralToAssignmentPattern'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJS::AST::PatternProperty::PatternProperty(PropertyName *name,
    QStringView n, ExpressionNode *i)': names 'QQmlJS::AST::ExpressionNode',
    which has no cute class yet.
  - Qt's 'QQmlJS::AST::PatternProperty::PatternProperty(PropertyName *name,
    Pattern *pattern, ExpressionNode *i)': names 'QQmlJS::AST::Pattern',
    which has no cute class yet.
  - Qt's 'void QQmlJS::AST::PatternProperty::accept0(BaseVisitor *visitor)':
    names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.

  What has no ritual
  ------------------

  1 of the 8 functions Qt declares: 1 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ QQmlJS::AST::PatternProperty is created at the first use, not by
    'QQmlJS::AST::PatternProperty(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJS::AST::PatternProperty.
  - Each name of Qt's QQmlJS::AST::PatternProperty that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJS::AST::PatternProperty'

  #  A C++ QQmlJS::AST::PatternProperty Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJS_AST_PatternProperty'

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
    QQmlJS::AST::PatternProperty::firstSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-patternproperty.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::PatternProperty::firstSourceLocation()
    #      const
    ritual = 'ritual_ZNK6QQmlJS3AST15PatternProperty19firstSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST15PatternProperty19firstSourceLocationE'
          'v')
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def lastSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::PatternProperty::lastSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-patternproperty.html#lastSourceLocation

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::PatternProperty::lastSourceLocation()
    #      const
    ritual = 'ritual_ZNK6QQmlJS3AST15PatternProperty18lastSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST15PatternProperty18lastSourceLocationEv')
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
    - Qt's 'QQmlJS::AST::PatternProperty::PatternProperty(PropertyName *name,
      QStringView n, ExpressionNode *i)': names
      'QQmlJS::AST::ExpressionNode', which has no cute class yet.
    - Qt's 'QQmlJS::AST::PatternProperty::PatternProperty(PropertyName *name,
      Pattern *pattern, ExpressionNode *i)': names 'QQmlJS::AST::Pattern',
      which has no cute class yet.
    - Qt's 'QQmlJS::AST::PatternProperty::PatternProperty(PropertyName *name,
      ExpressionNode *i, Type t)': the compiler refuses its ritual as it
      would be written here: no matching constructor for initialization of
      'CuteQQmlJS_AST_PatternProperty'.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.PatternProperty.__init__' has no cute function yet. "
        "Qt's 'QQmlJS::AST::PatternProperty::PatternProperty(PropertyName "
        "*name, QStringView n, ExpressionNode *i)': names "
        "'QQmlJS::AST::ExpressionNode', which has no cute class yet. Qt's "
        "'QQmlJS::AST::PatternProperty::PatternProperty(PropertyName *name, "
        "Pattern *pattern, ExpressionNode *i)': names "
        "'QQmlJS::AST::Pattern', which has no cute class yet. Qt's "
        "'QQmlJS::AST::PatternProperty::PatternProperty(PropertyName *name, "
        "ExpressionNode *i, Type t)': the compiler refuses its ritual as it "
        "would be written here: no matching constructor for initialization "
        "of 'CuteQQmlJS_AST_PatternProperty'.")

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

  @overload(WAIT['QQmlJS.AST.BoundNames'])
  @overload(NoneType)
  def boundNames(self, names: Optional[QQmlJS.AST.BoundNames]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::PatternProperty::boundNames(BoundNames
    *names)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-patternproperty.html#boundNames

    Parameters
    ----------

    names : Optional[QQmlJS.AST.BoundNames]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::PatternProperty::boundNames(BoundNames *names)
    ritual = (
        'ritual_ZN6QQmlJS3AST15PatternProperty10boundNamesEPNS0_10BoundName'
        'sE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST15PatternProperty10boundNamesEPNS0_10Bou'
          'ndNamesE')
    self.uglySide.call(ritual, self._addressOf(names))

  @overload(WAIT['QQmlJS.SourceLocation'], QString)
  @overload(WAIT['QQmlJS.SourceLocation'], NoneType)
  @overload(NoneType, QString)
  @overload(NoneType, NoneType)
  def convertLiteralToAssignmentPattern(
      self,
      errorLocation: Optional[QQmlJS.SourceLocation],
      errorMessage: Optional[QString],
  ) -> bool:
    """
    Calls Qt's 'bool
    QQmlJS::AST::PatternProperty::convertLiteralToAssignmentPattern(
    SourceLocation *errorLocation, QString *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-patternproperty.html

    Parameters
    ----------

    errorLocation : Optional[QQmlJS.SourceLocation]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::PatternProperty::convertLiteralToAssignmentPattern(
    #      SourceLocation *errorLocation, QString *errorMessage)
    ritual = (
        'ritual_ZN6QQmlJS3AST15PatternProperty33convertLiteralToAssignmentP'
        'atternEPNS_14SourceLocationEP7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST15PatternProperty33convertLiteralToAssig'
          'nmentPatternEPNS_14SourceLocationEP7QString')
    return self.uglySide.call(
        ritual,
        self._addressOf(errorLocation), self._addressOf(errorMessage),
    )
