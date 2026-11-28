"""
QQmlJS::AST::PatternElementList binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlJS::AST::PatternElementList to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
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


class PatternElementList(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::AST::PatternElementList: a plain Python
  object standing in front of one C++ QQmlJS::AST::PatternElementList.

  What exists
  -----------

  Every function of Qt's QQmlJS::AST::PatternElementList that has a ritual
  and that Python can call so far, 5 names in all: 'append', 'finish',
  'boundNames', 'firstSourceLocation', 'lastSourceLocation'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlJS::AST::PatternElementList::accept0(BaseVisitor
    *visitor)': names 'QQmlJS::AST::BaseVisitor', which has no cute class
    yet.

  What to expect
  --------------

  - The C++ QQmlJS::AST::PatternElementList is created at the first use, not
    by 'QQmlJS::AST::PatternElementList(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJS::AST::PatternElementList.
  - Each name of Qt's QQmlJS::AST::PatternElementList that has no cute
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
  __qt_class__ = 'QQmlJS::AST::PatternElementList'

  #  A C++ QQmlJS::AST::PatternElementList Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJS_AST_PatternElementList'

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
    QQmlJS::AST::PatternElementList::firstSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-patternelementlist.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::PatternElementList::firstSourceLocation()
    #      const
    ritual = (
        'ritual_ZNK6QQmlJS3AST18PatternElementList19firstSourceLocationEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST18PatternElementList19firstSourceLocati'
          'onEv')
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def lastSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::PatternElementList::lastSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-patternelementlist.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::PatternElementList::lastSourceLocation()
    #      const
    ritual = (
        'ritual_ZNK6QQmlJS3AST18PatternElementList18lastSourceLocationEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST18PatternElementList18lastSourceLocatio'
          'nEv')
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

  @overload(
      WAIT['QQmlJS.MemoryPool'], WAIT['QQmlJS.AST.Elision'],
      WAIT['QQmlJS.AST.PatternElement'],
  )
  @overload(WAIT['QQmlJS.MemoryPool'], WAIT['QQmlJS.AST.Elision'], NoneType)
  @overload(
      WAIT['QQmlJS.MemoryPool'], NoneType, WAIT['QQmlJS.AST.PatternElement'],
  )
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType, NoneType)
  @overload(
      NoneType, WAIT['QQmlJS.AST.Elision'],
      WAIT['QQmlJS.AST.PatternElement'],
  )
  @overload(NoneType, WAIT['QQmlJS.AST.Elision'], NoneType)
  @overload(NoneType, NoneType, WAIT['QQmlJS.AST.PatternElement'])
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      elision: Optional[QQmlJS.AST.Elision],
      element: Optional[QQmlJS.AST.PatternElement],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::PatternElementList::PatternElementList(Elision *elision,
    PatternElement *element)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-patternelementlist.html

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    elision : Optional[QQmlJS.AST.Elision]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    element : Optional[QQmlJS.AST.PatternElement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlJS::AST::PatternElementList::PatternElementList(Elision *elision,
    #      PatternElement *element)
    self._noteCreation(PatternElementList, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST18PatternElementListC1EPNS0_7ElisionEPNS0_14Pa'
        'tternElementE',
        self._addressOf(pool), self._addressOf(elision),
        self._addressOf(element),
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

  @overload(THIS)
  @overload(NoneType)
  def append(
      self,
      n: Optional[PatternElementList],
  ) -> Optional[PatternElementList]:
    """
    Calls Qt's 'PatternElementList
    *QQmlJS::AST::PatternElementList::append(PatternElementList *n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-patternelementlist.html#append

    Parameters
    ----------

    n : Optional[PatternElementList]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[PatternElementList]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  PatternElementList
    #      *QQmlJS::AST::PatternElementList::append(PatternElementList *n)
    address = self.uglySide.call(
        'ritual_ZN6QQmlJS3AST18PatternElementList6appendEPS1_',
        self._addressOf(n),
    )
    return PatternElementList._cuteAt(address)

  def finish(self) -> Optional[PatternElementList]:
    """
    Calls Qt's 'PatternElementList
    *QQmlJS::AST::PatternElementList::finish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-patternelementlist.html#finish

    Returns
    -------

    Optional[PatternElementList]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  PatternElementList *QQmlJS::AST::PatternElementList::finish()
    address = self.uglySide.call(
        'ritual_ZN6QQmlJS3AST18PatternElementList6finishEv',
    )
    return PatternElementList._cuteAt(address)

  @overload(WAIT['QQmlJS.AST.BoundNames'])
  @overload(NoneType)
  def boundNames(self, names: Optional[QQmlJS.AST.BoundNames]) -> None:
    """
    Calls Qt's 'void QQmlJS::AST::PatternElementList::boundNames(BoundNames
    *names)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-patternelementlist.html#boundNames

    Parameters
    ----------

    names : Optional[QQmlJS.AST.BoundNames]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlJS::AST::PatternElementList::boundNames(BoundNames *names)
    self.uglySide.call(
        'ritual_ZN6QQmlJS3AST18PatternElementList10boundNamesEPNS0_10BoundN'
        'amesE',
        self._addressOf(names),
    )

  @staticmethod
  def accept0(*__, **_) -> Never:
    """
    Qt's 'void QQmlJS::AST::PatternElementList::accept0(BaseVisitor
    *visitor)': names 'QQmlJS::AST::BaseVisitor', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.PatternElementList.accept0' has no cute function yet. "
        "Qt's 'void QQmlJS::AST::PatternElementList::accept0(BaseVisitor "
        "*visitor)': names 'QQmlJS::AST::BaseVisitor', which has no cute "
        "class yet.")
