"""
QQmlJS::AST::UiHeaderItemList binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlJS::AST::UiHeaderItemList to be private: it declares the
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


class UiHeaderItemList(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::AST::UiHeaderItemList: a plain Python object
  standing in front of one C++ QQmlJS::AST::UiHeaderItemList.

  What exists
  -----------

  Every function of Qt's QQmlJS::AST::UiHeaderItemList that has a ritual and
  that Python can call so far, 3 names in all: 'finish',
  'firstSourceLocation', 'lastSourceLocation'. It can be made from Python, in
  4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlJS::AST::UiHeaderItemList::accept0(BaseVisitor *visitor)':
    names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.

  What to expect
  --------------

  - The C++ QQmlJS::AST::UiHeaderItemList is created at the first use, not by
    'QQmlJS::AST::UiHeaderItemList(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJS::AST::UiHeaderItemList.
  - Each name of Qt's QQmlJS::AST::UiHeaderItemList that has no cute function
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
  __qt_class__ = 'QQmlJS::AST::UiHeaderItemList'

  #  A C++ QQmlJS::AST::UiHeaderItemList Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJS_AST_UiHeaderItemList'

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
    QQmlJS::AST::UiHeaderItemList::firstSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uiheaderitemlist.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiHeaderItemList::firstSourceLocation()
    #      const
    ritual = 'ritual_ZNK6QQmlJS3AST16UiHeaderItemList19firstSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST16UiHeaderItemList19firstSourceLocation'
          'Ev')
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def lastSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::UiHeaderItemList::lastSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uiheaderitemlist.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::UiHeaderItemList::lastSourceLocation()
    #      const
    ritual = 'ritual_ZNK6QQmlJS3AST16UiHeaderItemList18lastSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST16UiHeaderItemList18lastSourceLocationE'
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

  @overload(WAIT['QQmlJS.MemoryPool'], WAIT['QQmlJS.AST.UiImport'])
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType)
  @overload(NoneType, WAIT['QQmlJS.AST.UiImport'])
  @overload(NoneType, NoneType)
  def __init__(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      import_: Optional[QQmlJS.AST.UiImport],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::UiHeaderItemList::UiHeaderItemList(UiImport *import)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uiheaderitemlist.html#UiHeaderItemList

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    import_ : Optional[QQmlJS.AST.UiImport]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlJS::AST::UiHeaderItemList::UiHeaderItemList(UiImport *import)
    self._noteCreation(UiHeaderItemList, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST16UiHeaderItemListC1EPNS0_8UiImportE',
        self._addressOf(pool), self._addressOf(import_),
    ))

  @overload(WAIT['QQmlJS.MemoryPool'], WAIT['QQmlJS.AST.UiPragma'])
  @overload(NoneType, WAIT['QQmlJS.AST.UiPragma'])
  def __init__(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      pragma: Optional[QQmlJS.AST.UiPragma],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::UiHeaderItemList::UiHeaderItemList(UiPragma *pragma)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uiheaderitemlist.html#UiHeaderItemList

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pragma : Optional[QQmlJS.AST.UiPragma]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlJS::AST::UiHeaderItemList::UiHeaderItemList(UiPragma *pragma)
    self._noteCreation(UiHeaderItemList, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST16UiHeaderItemListC1EPNS0_8UiPragmaE',
        self._addressOf(pool), self._addressOf(pragma),
    ))

  @overload(WAIT['QQmlJS.MemoryPool'], THIS, WAIT['QQmlJS.AST.UiImport'])
  @overload(WAIT['QQmlJS.MemoryPool'], THIS, NoneType)
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType, WAIT['QQmlJS.AST.UiImport'])
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType, NoneType)
  @overload(NoneType, THIS, WAIT['QQmlJS.AST.UiImport'])
  @overload(NoneType, THIS, NoneType)
  @overload(NoneType, NoneType, WAIT['QQmlJS.AST.UiImport'])
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      previous: Optional[UiHeaderItemList],
      import_: Optional[QQmlJS.AST.UiImport],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::UiHeaderItemList::UiHeaderItemList(UiHeaderItemList
    *previous, UiImport *import)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uiheaderitemlist.html#UiHeaderItemList

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    previous : Optional[UiHeaderItemList]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    import_ : Optional[QQmlJS.AST.UiImport]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlJS::AST::UiHeaderItemList::UiHeaderItemList(UiHeaderItemList
    #      *previous, UiImport *import)
    self._noteCreation(UiHeaderItemList, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST16UiHeaderItemListC1EPS1_PNS0_8UiImportE',
        self._addressOf(pool), self._addressOf(previous),
        self._addressOf(import_),
    ))

  @overload(WAIT['QQmlJS.MemoryPool'], THIS, WAIT['QQmlJS.AST.UiPragma'])
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType, WAIT['QQmlJS.AST.UiPragma'])
  @overload(NoneType, THIS, WAIT['QQmlJS.AST.UiPragma'])
  @overload(NoneType, NoneType, WAIT['QQmlJS.AST.UiPragma'])
  def __init__(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      previous: Optional[UiHeaderItemList],
      pragma: Optional[QQmlJS.AST.UiPragma],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::UiHeaderItemList::UiHeaderItemList(UiHeaderItemList
    *previous, UiPragma *pragma)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uiheaderitemlist.html#UiHeaderItemList

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    previous : Optional[UiHeaderItemList]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pragma : Optional[QQmlJS.AST.UiPragma]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlJS::AST::UiHeaderItemList::UiHeaderItemList(UiHeaderItemList
    #      *previous, UiPragma *pragma)
    self._noteCreation(UiHeaderItemList, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST16UiHeaderItemListC1EPS1_PNS0_8UiPragmaE',
        self._addressOf(pool), self._addressOf(previous),
        self._addressOf(pragma),
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

  def finish(self) -> Optional[UiHeaderItemList]:
    """
    Calls Qt's 'UiHeaderItemList *QQmlJS::AST::UiHeaderItemList::finish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-uiheaderitemlist.html#finish

    Returns
    -------

    Optional[UiHeaderItemList]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  UiHeaderItemList *QQmlJS::AST::UiHeaderItemList::finish()
    address = self.uglySide.call(
        'ritual_ZN6QQmlJS3AST16UiHeaderItemList6finishEv',
    )
    return UiHeaderItemList._cuteAt(address)

  @staticmethod
  def accept0(*__, **_) -> Never:
    """
    Qt's 'void QQmlJS::AST::UiHeaderItemList::accept0(BaseVisitor *visitor)':
    names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.UiHeaderItemList.accept0' has no cute function yet. "
        "Qt's 'void QQmlJS::AST::UiHeaderItemList::accept0(BaseVisitor "
        "*visitor)': names 'QQmlJS::AST::BaseVisitor', which has no cute "
        "class yet.")
