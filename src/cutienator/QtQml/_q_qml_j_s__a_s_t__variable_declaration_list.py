"""
QQmlJS::AST::VariableDeclarationList binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlJS::AST::VariableDeclarationList to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlJS

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class VariableDeclarationList(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::AST::VariableDeclarationList: a plain Python
  object standing in front of one C++ QQmlJS::AST::VariableDeclarationList.

  What exists
  -----------

  Every function of Qt's QQmlJS::AST::VariableDeclarationList that has a
  ritual and that Python can call so far, 3 names in all:
  'firstSourceLocation', 'lastSourceLocation', 'finish'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlJS::AST::VariableDeclarationList::accept0(BaseVisitor
    *visitor)': names 'QQmlJS::AST::BaseVisitor', which has no cute class
    yet.

  What to expect
  --------------

  - The C++ QQmlJS::AST::VariableDeclarationList is created at the first use,
    not by 'QQmlJS::AST::VariableDeclarationList(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJS::AST::VariableDeclarationList.
  - Each name of Qt's QQmlJS::AST::VariableDeclarationList that has no cute
    function yet, 'accept0', holds a function that raises
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
  __qt_class__ = 'QQmlJS::AST::VariableDeclarationList'

  #  A C++ QQmlJS::AST::VariableDeclarationList Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJS_AST_VariableDeclarationList'

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
    QQmlJS::AST::VariableDeclarationList::firstSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-variabledeclarationlist.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation
    #      QQmlJS::AST::VariableDeclarationList::firstSourceLocation() const
    ritual = (
        'ritual_ZNK6QQmlJS3AST23VariableDeclarationList19firstSourceLocatio'
        'nEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST23VariableDeclarationList19firstSourceL'
          'ocationEv')
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def lastSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::VariableDeclarationList::lastSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-variabledeclarationlist.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation
    #      QQmlJS::AST::VariableDeclarationList::lastSourceLocation() const
    ritual = (
        'ritual_ZNK6QQmlJS3AST23VariableDeclarationList18lastSourceLocation'
        'Ev')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST23VariableDeclarationList18lastSourceLo'
          'cationEv')
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

  @overload(WAIT['QQmlJS.MemoryPool'], WAIT['QQmlJS.AST.PatternElement'])
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType)
  @overload(NoneType, WAIT['QQmlJS.AST.PatternElement'])
  @overload(NoneType, NoneType)
  def __init__(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      decl: Optional[QQmlJS.AST.PatternElement],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::VariableDeclarationList::VariableDeclarationList(
    PatternElement *decl)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-variabledeclarationlist.html

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    decl : Optional[QQmlJS.AST.PatternElement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlJS::AST::VariableDeclarationList::VariableDeclarationList(
    #      PatternElement *decl)
    self._noteCreation(VariableDeclarationList, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST23VariableDeclarationListC1EPNS0_14PatternElem'
        'entE',
        self._addressOf(pool), self._addressOf(decl),
    ))

  @overload(
      WAIT['QQmlJS.MemoryPool'], THIS, WAIT['QQmlJS.AST.PatternElement'],
  )
  @overload(WAIT['QQmlJS.MemoryPool'], THIS, NoneType)
  @overload(
      WAIT['QQmlJS.MemoryPool'], NoneType, WAIT['QQmlJS.AST.PatternElement'],
  )
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType, NoneType)
  @overload(NoneType, THIS, WAIT['QQmlJS.AST.PatternElement'])
  @overload(NoneType, THIS, NoneType)
  @overload(NoneType, NoneType, WAIT['QQmlJS.AST.PatternElement'])
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      previous: Optional[VariableDeclarationList],
      decl: Optional[QQmlJS.AST.PatternElement],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::VariableDeclarationList::VariableDeclarationList(
    VariableDeclarationList *previous, PatternElement *decl)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-variabledeclarationlist.html

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    previous : Optional[VariableDeclarationList]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    decl : Optional[QQmlJS.AST.PatternElement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlJS::AST::VariableDeclarationList::VariableDeclarationList(
    #      VariableDeclarationList *previous, PatternElement *decl)
    self._noteCreation(VariableDeclarationList, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST23VariableDeclarationListC1EPS1_PNS0_14Pattern'
        'ElementE',
        self._addressOf(pool), self._addressOf(previous),
        self._addressOf(decl),
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

  @overload(QQmlJS.AST.VariableScope)
  def finish(
      self,
      s: QQmlJS.AST.VariableScope,
  ) -> Optional[VariableDeclarationList]:
    """
    Calls Qt's 'VariableDeclarationList
    *QQmlJS::AST::VariableDeclarationList::finish(VariableScope s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-variabledeclarationlist.html#finish

    Parameters
    ----------

    s : QQmlJS.AST.VariableScope
      Passed on as its number.

    Returns
    -------

    Optional[VariableDeclarationList]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  VariableDeclarationList
    #      *QQmlJS::AST::VariableDeclarationList::finish(VariableScope s)
    address = self.uglySide.call(
        'ritual_ZN6QQmlJS3AST23VariableDeclarationList6finishENS0_13Variabl'
        'eScopeE',
        s.value,
    )
    return VariableDeclarationList._cuteAt(address)

  @staticmethod
  def accept0(*__, **_) -> Never:
    """
    Qt's 'void QQmlJS::AST::VariableDeclarationList::accept0(BaseVisitor
    *visitor)': names 'QQmlJS::AST::BaseVisitor', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.VariableDeclarationList.accept0' has no cute function "
        "yet. Qt's 'void "
        "QQmlJS::AST::VariableDeclarationList::accept0(BaseVisitor "
        "*visitor)': names 'QQmlJS::AST::BaseVisitor', which has no cute "
        "class yet.")
