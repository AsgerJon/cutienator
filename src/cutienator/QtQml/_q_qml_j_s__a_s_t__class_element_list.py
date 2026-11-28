"""
QQmlJS::AST::ClassElementList binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlJS::AST::ClassElementList to be private: it declares the
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


class ClassElementList(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::AST::ClassElementList: a plain Python object
  standing in front of one C++ QQmlJS::AST::ClassElementList.

  What exists
  -----------

  Every function of Qt's QQmlJS::AST::ClassElementList that has a ritual and
  that Python can call so far, 4 names in all: 'append',
  'firstSourceLocation', 'lastSourceLocation', 'finish'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlJS::AST::ClassElementList::accept0(BaseVisitor *visitor)':
    names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.

  What to expect
  --------------

  - The C++ QQmlJS::AST::ClassElementList is created at the first use, not by
    'QQmlJS::AST::ClassElementList(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJS::AST::ClassElementList.
  - Each name of Qt's QQmlJS::AST::ClassElementList that has no cute function
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
  __qt_class__ = 'QQmlJS::AST::ClassElementList'

  #  A C++ QQmlJS::AST::ClassElementList Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJS_AST_ClassElementList'

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
    QQmlJS::AST::ClassElementList::firstSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-classelementlist.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::ClassElementList::firstSourceLocation()
    #      const
    ritual = 'ritual_ZNK6QQmlJS3AST16ClassElementList19firstSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST16ClassElementList19firstSourceLocation'
          'Ev')
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def lastSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::ClassElementList::lastSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-classelementlist.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::ClassElementList::lastSourceLocation()
    #      const
    ritual = 'ritual_ZNK6QQmlJS3AST16ClassElementList18lastSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST16ClassElementList18lastSourceLocationE'
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

  @overload(
      WAIT['QQmlJS.MemoryPool'], WAIT['QQmlJS.AST.PatternProperty'], bool,
  )
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType, bool)
  @overload(NoneType, WAIT['QQmlJS.AST.PatternProperty'], bool)
  @overload(NoneType, NoneType, bool)
  def __init__(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      property: Optional[QQmlJS.AST.PatternProperty],
      isStatic: bool,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::ClassElementList::ClassElementList(PatternProperty
    *property, bool isStatic)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-classelementlist.html#ClassElementList

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    property : Optional[QQmlJS.AST.PatternProperty]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    isStatic : bool
      Passed on as it is.
    """
    #  QQmlJS::AST::ClassElementList::ClassElementList(PatternProperty
    #      *property, bool isStatic)
    self._noteCreation(ClassElementList, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST16ClassElementListC1EPNS0_15PatternPropertyEb',
        self._addressOf(pool), self._addressOf(property), isStatic,
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
      n: Optional[ClassElementList],
  ) -> Optional[ClassElementList]:
    """
    Calls Qt's 'ClassElementList
    *QQmlJS::AST::ClassElementList::append(ClassElementList *n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-classelementlist.html#append

    Parameters
    ----------

    n : Optional[ClassElementList]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[ClassElementList]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ClassElementList
    #      *QQmlJS::AST::ClassElementList::append(ClassElementList *n)
    address = self.uglySide.call(
        'ritual_ZN6QQmlJS3AST16ClassElementList6appendEPS1_',
        self._addressOf(n),
    )
    return ClassElementList._cuteAt(address)

  def finish(self) -> Optional[ClassElementList]:
    """
    Calls Qt's 'ClassElementList *QQmlJS::AST::ClassElementList::finish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-classelementlist.html#finish

    Returns
    -------

    Optional[ClassElementList]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ClassElementList *QQmlJS::AST::ClassElementList::finish()
    address = self.uglySide.call(
        'ritual_ZN6QQmlJS3AST16ClassElementList6finishEv',
    )
    return ClassElementList._cuteAt(address)

  @staticmethod
  def accept0(*__, **_) -> Never:
    """
    Qt's 'void QQmlJS::AST::ClassElementList::accept0(BaseVisitor *visitor)':
    names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.ClassElementList.accept0' has no cute function yet. "
        "Qt's 'void QQmlJS::AST::ClassElementList::accept0(BaseVisitor "
        "*visitor)': names 'QQmlJS::AST::BaseVisitor', which has no cute "
        "class yet.")
