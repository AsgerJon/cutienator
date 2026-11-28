"""
QQmlJS::AST::ArrayPattern binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlJS::AST::ArrayPattern to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
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


class ArrayPattern(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::AST::ArrayPattern: a plain Python object
  standing in front of one C++ QQmlJS::AST::ArrayPattern.

  What exists
  -----------

  Every function of Qt's QQmlJS::AST::ArrayPattern that has a ritual and that
  Python can call so far, 4 names in all: 'firstSourceLocation',
  'lastSourceLocation', 'isValidArrayLiteral',
  'convertLiteralToAssignmentPattern'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlJS::AST::ArrayPattern::accept0(BaseVisitor *visitor)':
    names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.

  What to expect
  --------------

  - The C++ QQmlJS::AST::ArrayPattern is created at the first use, not by
    'QQmlJS::AST::ArrayPattern(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJS::AST::ArrayPattern.
  - Each name of Qt's QQmlJS::AST::ArrayPattern that has no cute function
    yet, 'accept0', holds a function that raises 'NotImplementedError', and
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
  __qt_class__ = 'QQmlJS::AST::ArrayPattern'

  #  A C++ QQmlJS::AST::ArrayPattern Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJS_AST_ArrayPattern'

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
    QQmlJS::AST::ArrayPattern::firstSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-arraypattern.html#firstSourceLocation

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::ArrayPattern::firstSourceLocation() const
    ritual = 'ritual_ZNK6QQmlJS3AST12ArrayPattern19firstSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST12ArrayPattern19firstSourceLocationEv')
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def lastSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::ArrayPattern::lastSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-arraypattern.html#lastSourceLocation

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::ArrayPattern::lastSourceLocation() const
    ritual = 'ritual_ZNK6QQmlJS3AST12ArrayPattern18lastSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST12ArrayPattern18lastSourceLocationEv')
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  @overload()
  @overload(WAIT['QQmlJS.SourceLocation'])
  @overload(NoneType)
  def isValidArrayLiteral(
      self,
      errorLocation: Optional[QQmlJS.SourceLocation] = None,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQmlJS::AST::ArrayPattern::isValidArrayLiteral(SourceLocation
    *errorLocation) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-arraypattern.html#isValidArrayLiteral

    Parameters
    ----------

    errorLocation : Optional[QQmlJS.SourceLocation]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  bool QQmlJS::AST::ArrayPattern::isValidArrayLiteral(SourceLocation
    #      *errorLocation) const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST12ArrayPattern19isValidArrayLiteralEPNS_14Sou'
        'rceLocationE',
        self._addressOf(errorLocation),
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

  @overload(WAIT['QQmlJS.MemoryPool'], WAIT['QQmlJS.AST.PatternElementList'])
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType)
  @overload(NoneType, WAIT['QQmlJS.AST.PatternElementList'])
  @overload(NoneType, NoneType)
  def __init__(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      elts: Optional[QQmlJS.AST.PatternElementList],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::ArrayPattern::ArrayPattern(PatternElementList *elts)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-arraypattern.html#ArrayPattern

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    elts : Optional[QQmlJS.AST.PatternElementList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlJS::AST::ArrayPattern::ArrayPattern(PatternElementList *elts)
    self._noteCreation(ArrayPattern, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST12ArrayPatternC1EPNS0_18PatternElementListE',
        self._addressOf(pool), self._addressOf(elts),
    ))

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
    QQmlJS::AST::ArrayPattern::convertLiteralToAssignmentPattern(
    SourceLocation *errorLocation, QString *errorMessage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-arraypattern.html

    Parameters
    ----------

    errorLocation : Optional[QQmlJS.SourceLocation]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    errorMessage : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlJS::AST::ArrayPattern::convertLiteralToAssignmentPattern(
    #      SourceLocation *errorLocation, QString *errorMessage)
    ritual = (
        'ritual_ZN6QQmlJS3AST12ArrayPattern33convertLiteralToAssignmentPatt'
        'ernEPNS_14SourceLocationEP7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN6QQmlJS3AST12ArrayPattern33convertLiteralToAssignme'
          'ntPatternEPNS_14SourceLocationEP7QString')
    return self.uglySide.call(
        ritual,
        self._addressOf(errorLocation), self._addressOf(errorMessage),
    )

  @staticmethod
  def accept0(*__, **_) -> Never:
    """
    Qt's 'void QQmlJS::AST::ArrayPattern::accept0(BaseVisitor *visitor)':
    names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.ArrayPattern.accept0' has no cute function yet. Qt's "
        "'void QQmlJS::AST::ArrayPattern::accept0(BaseVisitor *visitor)': "
        "names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.")
