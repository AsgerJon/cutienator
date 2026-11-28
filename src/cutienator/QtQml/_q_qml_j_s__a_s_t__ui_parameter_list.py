"""
QQmlJS::AST::UiParameterList binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlJS::AST::UiParameterList to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
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


class UiParameterList(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::AST::UiParameterList: a plain Python object
  standing in front of one C++ QQmlJS::AST::UiParameterList.

  What exists
  -----------

  Every function of Qt's QQmlJS::AST::UiParameterList that has a ritual and
  that Python can call so far, 4 names in all: 'firstSourceLocation',
  'lastSourceLocation', 'lastOwnSourceLocation', 'finish'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlJS::AST::UiParameterList::accept0(BaseVisitor *a0)': names
    'QQmlJS::AST::BaseVisitor', which has no cute class yet.

  What to expect
  --------------

  - The C++ QQmlJS::AST::UiParameterList is created at the first use, not by
    'QQmlJS::AST::UiParameterList(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJS::AST::UiParameterList.
  - Each name of Qt's QQmlJS::AST::UiParameterList that has no cute function
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
  __qt_class__ = 'QQmlJS::AST::UiParameterList'

  #  A C++ QQmlJS::AST::UiParameterList Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJS_AST_UiParameterList'

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
    QQmlJS::AST::UiParameterList::firstSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uiparameterlist.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiParameterList::firstSourceLocation()
    #      const
    ritual = 'ritual_ZNK6QQmlJS3AST15UiParameterList19firstSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST15UiParameterList19firstSourceLocationE'
          'v')
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def lastSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::UiParameterList::lastSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uiparameterlist.html#lastSourceLocation

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiParameterList::lastSourceLocation()
    #      const
    ritual = 'ritual_ZNK6QQmlJS3AST15UiParameterList18lastSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST15UiParameterList18lastSourceLocationEv')
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def lastOwnSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::UiParameterList::lastOwnSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uiparameterlist.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiParameterList::lastOwnSourceLocation()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST15UiParameterList21lastOwnSourceLocationEv',
    )
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

  @overload(WAIT['QQmlJS.MemoryPool'], WAIT['QQmlJS.AST.Type'], str)
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType, str)
  @overload(NoneType, WAIT['QQmlJS.AST.Type'], str)
  @overload(NoneType, NoneType, str)
  def __init__(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      t: Optional[QQmlJS.AST.Type],
      n: str,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::UiParameterList::UiParameterList(Type *t, QStringView n)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uiparameterlist.html#UiParameterList

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    t : Optional[QQmlJS.AST.Type]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    n : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QQmlJS::AST::UiParameterList::UiParameterList(Type *t, QStringView n)
    self._noteCreation(UiParameterList, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST15UiParameterListC1EPNS0_4TypeE11QStringView',
        self._addressOf(pool), self._addressOf(t), n,
    ))

  @overload(WAIT['QQmlJS.MemoryPool'], THIS, WAIT['QQmlJS.AST.Type'], str)
  @overload(WAIT['QQmlJS.MemoryPool'], THIS, NoneType, str)
  @overload(
      WAIT['QQmlJS.MemoryPool'], NoneType, WAIT['QQmlJS.AST.Type'], str,
  )
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType, NoneType, str)
  @overload(NoneType, THIS, WAIT['QQmlJS.AST.Type'], str)
  @overload(NoneType, THIS, NoneType, str)
  @overload(NoneType, NoneType, WAIT['QQmlJS.AST.Type'], str)
  @overload(NoneType, NoneType, NoneType, str)
  def __init__(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      previous: Optional[UiParameterList],
      t: Optional[QQmlJS.AST.Type],
      n: str,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::UiParameterList::UiParameterList(UiParameterList *previous,
    Type *t, QStringView n)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uiparameterlist.html#UiParameterList

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    previous : Optional[UiParameterList]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    t : Optional[QQmlJS.AST.Type]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    n : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QQmlJS::AST::UiParameterList::UiParameterList(UiParameterList
    #      *previous, Type *t, QStringView n)
    self._noteCreation(UiParameterList, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST15UiParameterListC1EPS1_PNS0_4TypeE11QStringVi'
        'ew',
        self._addressOf(pool), self._addressOf(previous), self._addressOf(t),
        n,
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

  def finish(self) -> Optional[UiParameterList]:
    """
    Calls Qt's 'UiParameterList *QQmlJS::AST::UiParameterList::finish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uiparameterlist.html#finish

    Returns
    -------

    Optional[UiParameterList]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  UiParameterList *QQmlJS::AST::UiParameterList::finish()
    address = self.uglySide.call(
        'ritual_ZN6QQmlJS3AST15UiParameterList6finishEv',
    )
    return UiParameterList._cuteAt(address)

  @staticmethod
  def accept0(*__, **_) -> Never:
    """
    Qt's 'void QQmlJS::AST::UiParameterList::accept0(BaseVisitor *a0)': names
    'QQmlJS::AST::BaseVisitor', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.UiParameterList.accept0' has no cute function yet. "
        "Qt's 'void QQmlJS::AST::UiParameterList::accept0(BaseVisitor "
        "*a0)': names 'QQmlJS::AST::BaseVisitor', which has no cute class "
        "yet.")
