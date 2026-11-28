"""
QQmlJS::AST::PatternElement binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlJS::AST::PatternElement to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
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


class PatternElement(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::AST::PatternElement: a plain Python object
  standing in front of one C++ QQmlJS::AST::PatternElement.

  What exists
  -----------

  Every function of Qt's QQmlJS::AST::PatternElement that has a ritual and
  that Python can call so far, 9 names in all: 'unwrapInitializer',
  'convertLiteralToAssignmentPattern', 'firstSourceLocation',
  'lastSourceLocation', 'elementList', 'propertyList',
  'isVariableDeclaration', 'isLexicallyScoped', 'boundNames'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJS::AST::PatternElement::PatternElement(ExpressionNode *i, Type
    t)': names 'QQmlJS::AST::ExpressionNode', which has no cute class yet.
  - Qt's 'QQmlJS::AST::PatternElement::PatternElement(QStringView n,
    TypeAnnotation *typeAnnotation, ExpressionNode *i, Type t)': names
    'QQmlJS::AST::ExpressionNode', which has no cute class yet.
  - Qt's 'QQmlJS::AST::PatternElement::PatternElement(Pattern *pattern,
    ExpressionNode *i, Type t)': names 'QQmlJS::AST::Pattern', which has no
    cute class yet.
  - Qt's 'void QQmlJS::AST::PatternElement::accept0(BaseVisitor *visitor)':
    names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.
  - Qt's 'ExpressionNode *QQmlJS::AST::PatternElement::destructuringTarget()
    const': gives 'QQmlJS::AST::ExpressionNode', which has no cute class yet.
  - Qt's 'Pattern *QQmlJS::AST::PatternElement::destructuringPattern()
    const': gives 'QQmlJS::AST::Pattern', which has no cute class yet.

  What to expect
  --------------

  - The C++ QQmlJS::AST::PatternElement is created at the first use, not by
    'QQmlJS::AST::PatternElement(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJS::AST::PatternElement.
  - Each name of Qt's QQmlJS::AST::PatternElement that has no cute function
    yet, '__init__', 'accept0', 'destructuringPattern',
    'destructuringTarget', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlJS::AST::PatternElement, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Type(CuteNum):
    """
    The enum 'QQmlJS::AST::PatternElement::Type' of Qt, with the 7 names Qt
    gives in it.
    """

    Literal = Kee[int](0)
    Method = Kee[int](1)
    Getter = Kee[int](2)
    Setter = Kee[int](3)
    SpreadElement = Kee[int](4)
    RestElement = Kee[int](4)
    Binding = Kee[int](5)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJS::AST::PatternElement'

  #  A C++ QQmlJS::AST::PatternElement Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJS_AST_PatternElement'

  #  The functions Qt calls itself that QQmlJS::AST::PatternElement is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'convertLiteralToAssignmentPattern': (
          ('_ZN6QQmlJS3AST14PatternElement33convertLiteralToAssignmentPatte'
           'rnEPNS_14SourceLocationEP7QString',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtQml:QQmlJS.SourceLocation'),
               ('address', 'address', 'QtCore:QString'),
           )),
      ),
      'boundNames': (
          ('_ZN6QQmlJS3AST14PatternElement10boundNamesEPNS0_10BoundNamesE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQml:QQmlJS.AST.BoundNames'),
           )),
      ),
  }

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
    QQmlJS::AST::PatternElement::firstSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-patternelement.html#firstSourceLocation

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::PatternElement::firstSourceLocation()
    #      const
    ritual = 'ritual_ZNK6QQmlJS3AST14PatternElement19firstSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST14PatternElement19firstSourceLocationEv')
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def lastSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::PatternElement::lastSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-patternelement.html#lastSourceLocation

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::PatternElement::lastSourceLocation() const
    ritual = 'ritual_ZNK6QQmlJS3AST14PatternElement18lastSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST14PatternElement18lastSourceLocationEv')
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def elementList(self) -> Optional[QQmlJS.AST.PatternElementList]:
    """
    Calls Qt's 'PatternElementList
    *QQmlJS::AST::PatternElement::elementList() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-patternelement.html#elementList

    Returns
    -------

    Optional[QQmlJS.AST.PatternElementList]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  PatternElementList *QQmlJS::AST::PatternElement::elementList() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST14PatternElement11elementListEv',
    )
    return QQmlJS.AST.PatternElementList._cuteAt(address)

  def propertyList(self) -> Optional[QQmlJS.AST.PatternPropertyList]:
    """
    Calls Qt's 'PatternPropertyList
    *QQmlJS::AST::PatternElement::propertyList() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-patternelement.html#propertyList

    Returns
    -------

    Optional[QQmlJS.AST.PatternPropertyList]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  PatternPropertyList *QQmlJS::AST::PatternElement::propertyList() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST14PatternElement12propertyListEv',
    )
    return QQmlJS.AST.PatternPropertyList._cuteAt(address)

  def isVariableDeclaration(self) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::PatternElement::isVariableDeclaration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-patternelement.html
    """
    #  bool QQmlJS::AST::PatternElement::isVariableDeclaration() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST14PatternElement21isVariableDeclarationEv',
    )

  def isLexicallyScoped(self) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::PatternElement::isLexicallyScoped() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-patternelement.html#isLexicallyScoped
    """
    #  bool QQmlJS::AST::PatternElement::isLexicallyScoped() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST14PatternElement17isLexicallyScopedEv',
    )

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
    - Qt's 'QQmlJS::AST::PatternElement::PatternElement(ExpressionNode *i,
      Type t)': names 'QQmlJS::AST::ExpressionNode', which has no cute class
      yet.
    - Qt's 'QQmlJS::AST::PatternElement::PatternElement(QStringView n,
      TypeAnnotation *typeAnnotation, ExpressionNode *i, Type t)': names
      'QQmlJS::AST::ExpressionNode', which has no cute class yet.
    - Qt's 'QQmlJS::AST::PatternElement::PatternElement(Pattern *pattern,
      ExpressionNode *i, Type t)': names 'QQmlJS::AST::Pattern', which has no
      cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.PatternElement.__init__' has no cute function yet. "
        "Qt's 'QQmlJS::AST::PatternElement::PatternElement(ExpressionNode "
        "*i, Type t)': names 'QQmlJS::AST::ExpressionNode', which has no "
        "cute class yet. Qt's "
        "'QQmlJS::AST::PatternElement::PatternElement(QStringView n, "
        "TypeAnnotation *typeAnnotation, ExpressionNode *i, Type t)': names "
        "'QQmlJS::AST::ExpressionNode', which has no cute class yet. Qt's "
        "'QQmlJS::AST::PatternElement::PatternElement(Pattern *pattern, "
        "ExpressionNode *i, Type t)': names 'QQmlJS::AST::Pattern', which "
        "has no cute class yet.")

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

  def unwrapInitializer(self) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::PatternElement::unwrapInitializer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-patternelement.html#unwrapInitializer
    """
    #  void QQmlJS::AST::PatternElement::unwrapInitializer()
    self.uglySide.call(
        'ritual_ZN6QQmlJS3AST14PatternElement17unwrapInitializerEv',
    )

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
    QQmlJS::AST::PatternElement::convertLiteralToAssignmentPattern(
    SourceLocation *errorLocation, QString *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-patternelement.html

    Parameters
    ----------

    errorLocation : Optional[QQmlJS.SourceLocation]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::PatternElement::convertLiteralToAssignmentPattern(
    #      SourceLocation *errorLocation, QString *errorMessage)
    ritual = (
        'ritual_ZN6QQmlJS3AST14PatternElement33convertLiteralToAssignmentPa'
        'tternEPNS_14SourceLocationEP7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST14PatternElement33convertLiteralToAssign'
          'mentPatternEPNS_14SourceLocationEP7QString')
    return self.uglySide.call(
        ritual,
        self._addressOf(errorLocation), self._addressOf(errorMessage),
    )

  @overload(WAIT['QQmlJS.AST.BoundNames'])
  @overload(NoneType)
  def boundNames(self, names: Optional[QQmlJS.AST.BoundNames]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::PatternElement::boundNames(BoundNames
    *names)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-patternelement.html#boundNames

    Parameters
    ----------

    names : Optional[QQmlJS.AST.BoundNames]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::PatternElement::boundNames(BoundNames *names)
    ritual = (
        'ritual_ZN6QQmlJS3AST14PatternElement10boundNamesEPNS0_10BoundNames'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST14PatternElement10boundNamesEPNS0_10Boun'
          'dNamesE')
    self.uglySide.call(ritual, self._addressOf(names))

  @staticmethod
  def accept0(*__, **_) -> Never:
    """
    Qt's 'void QQmlJS::AST::PatternElement::accept0(BaseVisitor *visitor)':
    names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.PatternElement.accept0' has no cute function yet. Qt's "
        "'void QQmlJS::AST::PatternElement::accept0(BaseVisitor *visitor)': "
        "names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.")

  @staticmethod
  def destructuringPattern(*__, **_) -> Never:
    """
    Qt's 'Pattern *QQmlJS::AST::PatternElement::destructuringPattern()
    const': gives 'QQmlJS::AST::Pattern', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.PatternElement.destructuringPattern' has no cute "
        "function yet. Qt's 'Pattern "
        "*QQmlJS::AST::PatternElement::destructuringPattern() const': gives "
        "'QQmlJS::AST::Pattern', which has no cute class yet.")

  @staticmethod
  def destructuringTarget(*__, **_) -> Never:
    """
    Qt's 'ExpressionNode *QQmlJS::AST::PatternElement::destructuringTarget()
    const': gives 'QQmlJS::AST::ExpressionNode', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.PatternElement.destructuringTarget' has no cute "
        "function yet. Qt's 'ExpressionNode "
        "*QQmlJS::AST::PatternElement::destructuringTarget() const': gives "
        "'QQmlJS::AST::ExpressionNode', which has no cute class yet.")
