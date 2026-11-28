"""
QQmlJS::AST::UiPragmaValueList binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlJS::AST::UiPragmaValueList to be private: it declares the
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


class UiPragmaValueList(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::AST::UiPragmaValueList: a plain Python object
  standing in front of one C++ QQmlJS::AST::UiPragmaValueList.

  What exists
  -----------

  Every function of Qt's QQmlJS::AST::UiPragmaValueList that has a ritual and
  that Python can call so far, 3 names in all: 'firstSourceLocation',
  'lastSourceLocation', 'finish'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlJS::AST::UiPragmaValueList::accept0(BaseVisitor
    *visitor)': names 'QQmlJS::AST::BaseVisitor', which has no cute class
    yet.

  What to expect
  --------------

  - The C++ QQmlJS::AST::UiPragmaValueList is created at the first use, not
    by 'QQmlJS::AST::UiPragmaValueList(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJS::AST::UiPragmaValueList.
  - Each name of Qt's QQmlJS::AST::UiPragmaValueList that has no cute
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
  __qt_class__ = 'QQmlJS::AST::UiPragmaValueList'

  #  A C++ QQmlJS::AST::UiPragmaValueList Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJS_AST_UiPragmaValueList'

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
    QQmlJS::AST::UiPragmaValueList::firstSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipragmavaluelist.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiPragmaValueList::firstSourceLocation()
    #      const
    ritual = (
        'ritual_ZNK6QQmlJS3AST17UiPragmaValueList19firstSourceLocationEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST17UiPragmaValueList19firstSourceLocatio'
          'nEv')
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def lastSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::UiPragmaValueList::lastSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipragmavaluelist.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiPragmaValueList::lastSourceLocation()
    #      const
    ritual = 'ritual_ZNK6QQmlJS3AST17UiPragmaValueList18lastSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST17UiPragmaValueList18lastSourceLocation'
          'Ev')
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
  def __init__(self, pool: Optional[QQmlJS.MemoryPool], value: str) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::UiPragmaValueList::UiPragmaValueList(QStringView value)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipragmavaluelist.html

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QQmlJS::AST::UiPragmaValueList::UiPragmaValueList(QStringView value)
    self._noteCreation(UiPragmaValueList, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST17UiPragmaValueListC1E11QStringView',
        self._addressOf(pool), value,
    ))

  @overload(WAIT['QQmlJS.MemoryPool'], THIS, str)
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType, str)
  @overload(NoneType, THIS, str)
  @overload(NoneType, NoneType, str)
  def __init__(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      previous: Optional[UiPragmaValueList],
      value: str,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::UiPragmaValueList::UiPragmaValueList(UiPragmaValueList
    *previous, QStringView value)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipragmavaluelist.html

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    previous : Optional[UiPragmaValueList]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QQmlJS::AST::UiPragmaValueList::UiPragmaValueList(UiPragmaValueList
    #      *previous, QStringView value)
    self._noteCreation(UiPragmaValueList, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST17UiPragmaValueListC1EPS1_11QStringView',
        self._addressOf(pool), self._addressOf(previous), value,
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

  def finish(self) -> Optional[UiPragmaValueList]:
    """
    Calls Qt's 'UiPragmaValueList *QQmlJS::AST::UiPragmaValueList::finish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uipragmavaluelist.html#finish

    Returns
    -------

    Optional[UiPragmaValueList]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  UiPragmaValueList *QQmlJS::AST::UiPragmaValueList::finish()
    address = self.uglySide.call(
        'ritual_ZN6QQmlJS3AST17UiPragmaValueList6finishEv',
    )
    return UiPragmaValueList._cuteAt(address)

  @staticmethod
  def accept0(*__, **_) -> Never:
    """
    Qt's 'void QQmlJS::AST::UiPragmaValueList::accept0(BaseVisitor
    *visitor)': names 'QQmlJS::AST::BaseVisitor', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.UiPragmaValueList.accept0' has no cute function yet. "
        "Qt's 'void QQmlJS::AST::UiPragmaValueList::accept0(BaseVisitor "
        "*visitor)': names 'QQmlJS::AST::BaseVisitor', which has no cute "
        "class yet.")
