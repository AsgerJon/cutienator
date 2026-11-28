"""
QQmlJS::AST::UiEnumMemberList binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlJS::AST::UiEnumMemberList to be private: it declares the
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


class UiEnumMemberList(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::AST::UiEnumMemberList: a plain Python object
  standing in front of one C++ QQmlJS::AST::UiEnumMemberList.

  What exists
  -----------

  Every function of Qt's QQmlJS::AST::UiEnumMemberList that has a ritual and
  that Python can call so far, 3 names in all: 'firstSourceLocation',
  'lastSourceLocation', 'finish'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlJS::AST::UiEnumMemberList::accept0(BaseVisitor *visitor)':
    names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.

  What to expect
  --------------

  - The C++ QQmlJS::AST::UiEnumMemberList is created at the first use, not by
    'QQmlJS::AST::UiEnumMemberList(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJS::AST::UiEnumMemberList.
  - Each name of Qt's QQmlJS::AST::UiEnumMemberList that has no cute function
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
  __qt_class__ = 'QQmlJS::AST::UiEnumMemberList'

  #  A C++ QQmlJS::AST::UiEnumMemberList Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJS_AST_UiEnumMemberList'

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
    QQmlJS::AST::UiEnumMemberList::firstSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uienummemberlist.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiEnumMemberList::firstSourceLocation()
    #      const
    ritual = 'ritual_ZNK6QQmlJS3AST16UiEnumMemberList19firstSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST16UiEnumMemberList19firstSourceLocation'
          'Ev')
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def lastSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::UiEnumMemberList::lastSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uienummemberlist.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiEnumMemberList::lastSourceLocation()
    #      const
    ritual = 'ritual_ZNK6QQmlJS3AST16UiEnumMemberList18lastSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST16UiEnumMemberList18lastSourceLocationE'
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

  @overload(WAIT['QQmlJS.MemoryPool'], str)
  @overload(NoneType, str)
  @overload(WAIT['QQmlJS.MemoryPool'], str, float)
  @overload(NoneType, str, float)
  def __init__(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      member: str,
      v: float = 0.0,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::UiEnumMemberList::UiEnumMemberList(QStringView member,
    double v)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uienummemberlist.html#UiEnumMemberList

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : str
      Passed on as it is: a QString is made of it for the call.

    v : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  QQmlJS::AST::UiEnumMemberList::UiEnumMemberList(QStringView member,
    #      double v)
    self._noteCreation(UiEnumMemberList, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST16UiEnumMemberListC1E11QStringViewd',
        self._addressOf(pool), member, v,
    ))

  @overload(WAIT['QQmlJS.MemoryPool'], THIS, str)
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType, str)
  @overload(NoneType, THIS, str)
  @overload(NoneType, NoneType, str)
  def __init__(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      previous: Optional[UiEnumMemberList],
      member: str,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::UiEnumMemberList::UiEnumMemberList(UiEnumMemberList
    *previous, QStringView member)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uienummemberlist.html#UiEnumMemberList

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    previous : Optional[UiEnumMemberList]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QQmlJS::AST::UiEnumMemberList::UiEnumMemberList(UiEnumMemberList
    #      *previous, QStringView member)
    self._noteCreation(UiEnumMemberList, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST16UiEnumMemberListC1EPS1_11QStringView',
        self._addressOf(pool), self._addressOf(previous), member,
    ))

  @overload(WAIT['QQmlJS.MemoryPool'], THIS, str, float)
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType, str, float)
  @overload(NoneType, THIS, str, float)
  @overload(NoneType, NoneType, str, float)
  def __init__(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      previous: Optional[UiEnumMemberList],
      member: str,
      v: float,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::UiEnumMemberList::UiEnumMemberList(UiEnumMemberList
    *previous, QStringView member, double v)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uienummemberlist.html#UiEnumMemberList

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    previous : Optional[UiEnumMemberList]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : str
      Passed on as it is: a QString is made of it for the call.

    v : float
      Passed on as it is.
    """
    #  QQmlJS::AST::UiEnumMemberList::UiEnumMemberList(UiEnumMemberList
    #      *previous, QStringView member, double v)
    self._noteCreation(UiEnumMemberList, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST16UiEnumMemberListC1EPS1_11QStringViewd',
        self._addressOf(pool), self._addressOf(previous), member, v,
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

  def finish(self) -> Optional[UiEnumMemberList]:
    """
    Calls Qt's 'UiEnumMemberList *QQmlJS::AST::UiEnumMemberList::finish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uienummemberlist.html#finish

    Returns
    -------

    Optional[UiEnumMemberList]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  UiEnumMemberList *QQmlJS::AST::UiEnumMemberList::finish()
    address = self.uglySide.call(
        'ritual_ZN6QQmlJS3AST16UiEnumMemberList6finishEv',
    )
    return UiEnumMemberList._cuteAt(address)

  @staticmethod
  def accept0(*__, **_) -> Never:
    """
    Qt's 'void QQmlJS::AST::UiEnumMemberList::accept0(BaseVisitor *visitor)':
    names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.UiEnumMemberList.accept0' has no cute function yet. "
        "Qt's 'void QQmlJS::AST::UiEnumMemberList::accept0(BaseVisitor "
        "*visitor)': names 'QQmlJS::AST::BaseVisitor', which has no cute "
        "class yet.")
