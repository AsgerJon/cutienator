"""
QQmlJS::AST::FormalParameterList binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlJS::AST::FormalParameterList to be private: it declares the
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


class FormalParameterList(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::AST::FormalParameterList: a plain Python
  object standing in front of one C++ QQmlJS::AST::FormalParameterList.

  What exists
  -----------

  Every function of Qt's QQmlJS::AST::FormalParameterList that has a ritual
  and that Python can call so far, 9 names in all: 'append',
  'isSimpleParameterList', 'length', 'containsName', 'formals', 'boundNames',
  'firstSourceLocation', 'lastSourceLocation', 'finish'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlJS::AST::FormalParameterList::accept0(BaseVisitor
    *visitor)': names 'QQmlJS::AST::BaseVisitor', which has no cute class
    yet.

  What to expect
  --------------

  - The C++ QQmlJS::AST::FormalParameterList is created at the first use, not
    by 'QQmlJS::AST::FormalParameterList(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJS::AST::FormalParameterList.
  - Each name of Qt's QQmlJS::AST::FormalParameterList that has no cute
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
  __qt_class__ = 'QQmlJS::AST::FormalParameterList'

  #  A C++ QQmlJS::AST::FormalParameterList Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJS_AST_FormalParameterList'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def containsName(self, name: str) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::FormalParameterList::containsName(const
    QString &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-formalparameterlist.html#containsName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlJS::AST::FormalParameterList::containsName(const QString
    #      &name) const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST19FormalParameterList12containsNameERK7QStrin'
        'g',
        name,
    )

  def formals(self) -> QQmlJS.AST.BoundNames:
    """
    Calls Qt's 'BoundNames QQmlJS::AST::FormalParameterList::formals()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-formalparameterlist.html#formals

    Returns
    -------

    QQmlJS.AST.BoundNames
      A new cute QQmlJS::AST::BoundNames around the copy Qt gave back. Python
      owns it.
    """
    #  BoundNames QQmlJS::AST::FormalParameterList::formals() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST19FormalParameterList7formalsEv',
    )
    return QQmlJS.AST.BoundNames._cuteOwning(address)

  def boundNames(self) -> QQmlJS.AST.BoundNames:
    """
    Calls Qt's 'BoundNames QQmlJS::AST::FormalParameterList::boundNames()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-formalparameterlist.html#boundNames

    Returns
    -------

    QQmlJS.AST.BoundNames
      A new cute QQmlJS::AST::BoundNames around the copy Qt gave back. Python
      owns it.
    """
    #  BoundNames QQmlJS::AST::FormalParameterList::boundNames() const
    address = self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST19FormalParameterList10boundNamesEv',
    )
    return QQmlJS.AST.BoundNames._cuteOwning(address)

  def firstSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::FormalParameterList::firstSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-formalparameterlist.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::FormalParameterList::firstSourceLocation()
    #      const
    ritual = (
        'ritual_ZNK6QQmlJS3AST19FormalParameterList19firstSourceLocationEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST19FormalParameterList19firstSourceLocat'
          'ionEv')
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def lastSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::FormalParameterList::lastSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-formalparameterlist.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::FormalParameterList::lastSourceLocation()
    #      const
    ritual = (
        'ritual_ZNK6QQmlJS3AST19FormalParameterList18lastSourceLocationEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST19FormalParameterList18lastSourceLocati'
          'onEv')
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
      previous: Optional[FormalParameterList],
      e: Optional[QQmlJS.AST.PatternElement],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::FormalParameterList::FormalParameterList(
    FormalParameterList *previous, PatternElement *e)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-formalparameterlist.html

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    previous : Optional[FormalParameterList]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    e : Optional[QQmlJS.AST.PatternElement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlJS::AST::FormalParameterList::FormalParameterList(
    #      FormalParameterList *previous, PatternElement *e)
    self._noteCreation(FormalParameterList, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST19FormalParameterListC1EPS1_PNS0_14PatternElem'
        'entE',
        self._addressOf(pool), self._addressOf(previous), self._addressOf(e),
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
      n: Optional[FormalParameterList],
  ) -> Optional[FormalParameterList]:
    """
    Calls Qt's 'FormalParameterList
    *QQmlJS::AST::FormalParameterList::append(FormalParameterList *n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-formalparameterlist.html#append

    Parameters
    ----------

    n : Optional[FormalParameterList]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[FormalParameterList]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FormalParameterList
    #      *QQmlJS::AST::FormalParameterList::append(FormalParameterList *n)
    address = self.uglySide.call(
        'ritual_ZN6QQmlJS3AST19FormalParameterList6appendEPS1_',
        self._addressOf(n),
    )
    return FormalParameterList._cuteAt(address)

  def isSimpleParameterList(self) -> bool:
    """
    Calls Qt's 'bool
    QQmlJS::AST::FormalParameterList::isSimpleParameterList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-formalparameterlist.html
    """
    #  bool QQmlJS::AST::FormalParameterList::isSimpleParameterList()
    return self.uglySide.call(
        'ritual_ZN6QQmlJS3AST19FormalParameterList21isSimpleParameterListEv',
    )

  def length(self) -> int:
    """
    Calls Qt's 'int QQmlJS::AST::FormalParameterList::length()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-formalparameterlist.html#length
    """
    #  int QQmlJS::AST::FormalParameterList::length()
    return self.uglySide.call(
        'ritual_ZN6QQmlJS3AST19FormalParameterList6lengthEv',
    )

  @overload(WAIT['QQmlJS.MemoryPool'])
  @overload(NoneType)
  def finish(
      self,
      pool: Optional[QQmlJS.MemoryPool],
  ) -> Optional[FormalParameterList]:
    """
    Calls Qt's 'FormalParameterList
    *QQmlJS::AST::FormalParameterList::finish(MemoryPool *pool)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-formalparameterlist.html#finish

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[FormalParameterList]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  FormalParameterList
    #      *QQmlJS::AST::FormalParameterList::finish(MemoryPool *pool)
    address = self.uglySide.call(
        'ritual_ZN6QQmlJS3AST19FormalParameterList6finishEPNS_10MemoryPoolE',
        self._addressOf(pool),
    )
    return FormalParameterList._cuteAt(address)

  @staticmethod
  def accept0(*__, **_) -> Never:
    """
    Qt's 'void QQmlJS::AST::FormalParameterList::accept0(BaseVisitor
    *visitor)': names 'QQmlJS::AST::BaseVisitor', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.FormalParameterList.accept0' has no cute function yet. "
        "Qt's 'void QQmlJS::AST::FormalParameterList::accept0(BaseVisitor "
        "*visitor)': names 'QQmlJS::AST::BaseVisitor', which has no cute "
        "class yet.")
