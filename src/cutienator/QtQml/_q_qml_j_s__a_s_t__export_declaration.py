"""
QQmlJS::AST::ExportDeclaration binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlJS::AST::ExportDeclaration to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQmlJS

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ExportDeclaration(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::AST::ExportDeclaration: a plain Python object
  standing in front of one C++ QQmlJS::AST::ExportDeclaration.

  What exists
  -----------

  Every function of Qt's QQmlJS::AST::ExportDeclaration that has a ritual and
  that Python can call so far, 3 names in all: 'exportsAll',
  'firstSourceLocation', 'lastSourceLocation'. It can be made from Python, in
  3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlJS::AST::ExportDeclaration::ExportDeclaration(bool
    exportDefault, Node *variableStatementOrDeclaration)': names
    'QQmlJS::AST::Node', which has no cute class yet.
  - Qt's 'void QQmlJS::AST::ExportDeclaration::accept0(BaseVisitor
    *visitor)': names 'QQmlJS::AST::BaseVisitor', which has no cute class
    yet.

  What to expect
  --------------

  - The C++ QQmlJS::AST::ExportDeclaration is created at the first use, not
    by 'QQmlJS::AST::ExportDeclaration(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJS::AST::ExportDeclaration.
  - Each name of Qt's QQmlJS::AST::ExportDeclaration that has no cute
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
  __qt_class__ = 'QQmlJS::AST::ExportDeclaration'

  #  A C++ QQmlJS::AST::ExportDeclaration Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJS_AST_ExportDeclaration'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def exportsAll(self) -> bool:
    """
    Calls Qt's 'bool QQmlJS::AST::ExportDeclaration::exportsAll() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-exportdeclaration.html#exportsAll
    """
    #  bool QQmlJS::AST::ExportDeclaration::exportsAll() const
    return self.uglySide.call(
        'ritual_ZNK6QQmlJS3AST17ExportDeclaration10exportsAllEv',
    )

  def firstSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::ExportDeclaration::firstSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-exportdeclaration.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::ExportDeclaration::firstSourceLocation()
    #      const
    ritual = (
        'ritual_ZNK6QQmlJS3AST17ExportDeclaration19firstSourceLocationEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST17ExportDeclaration19firstSourceLocatio'
          'nEv')
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def lastSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation
    QQmlJS::AST::ExportDeclaration::lastSourceLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-exportdeclaration.html

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::ExportDeclaration::lastSourceLocation()
    #      const
    ritual = 'ritual_ZNK6QQmlJS3AST17ExportDeclaration18lastSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK6QQmlJS3AST17ExportDeclaration18lastSourceLocation'
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

  @overload(WAIT['QQmlJS.MemoryPool'], WAIT['QQmlJS.AST.FromClause'])
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType)
  @overload(NoneType, WAIT['QQmlJS.AST.FromClause'])
  @overload(NoneType, NoneType)
  def __init__(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      fromClause: Optional[QQmlJS.AST.FromClause],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::ExportDeclaration::ExportDeclaration(FromClause
    *fromClause)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-exportdeclaration.html

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    fromClause : Optional[QQmlJS.AST.FromClause]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlJS::AST::ExportDeclaration::ExportDeclaration(FromClause
    #      *fromClause)
    self._noteCreation(ExportDeclaration, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST17ExportDeclarationC1EPNS0_10FromClauseE',
        self._addressOf(pool), self._addressOf(fromClause),
    ))

  @overload(
      WAIT['QQmlJS.MemoryPool'], WAIT['QQmlJS.AST.ExportClause'],
      WAIT['QQmlJS.AST.FromClause'],
  )
  @overload(
      WAIT['QQmlJS.MemoryPool'], WAIT['QQmlJS.AST.ExportClause'], NoneType,
  )
  @overload(
      WAIT['QQmlJS.MemoryPool'], NoneType, WAIT['QQmlJS.AST.FromClause'],
  )
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType, NoneType)
  @overload(
      NoneType, WAIT['QQmlJS.AST.ExportClause'],
      WAIT['QQmlJS.AST.FromClause'],
  )
  @overload(NoneType, WAIT['QQmlJS.AST.ExportClause'], NoneType)
  @overload(NoneType, NoneType, WAIT['QQmlJS.AST.FromClause'])
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      exportClause: Optional[QQmlJS.AST.ExportClause],
      fromClause: Optional[QQmlJS.AST.FromClause],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::ExportDeclaration::ExportDeclaration(ExportClause
    *exportClause, FromClause *fromClause)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-exportdeclaration.html

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    exportClause : Optional[QQmlJS.AST.ExportClause]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    fromClause : Optional[QQmlJS.AST.FromClause]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlJS::AST::ExportDeclaration::ExportDeclaration(ExportClause
    #      *exportClause, FromClause *fromClause)
    self._noteCreation(ExportDeclaration, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST17ExportDeclarationC1EPNS0_12ExportClauseEPNS0'
        '_10FromClauseE',
        self._addressOf(pool), self._addressOf(exportClause),
        self._addressOf(fromClause),
    ))

  @overload(WAIT['QQmlJS.MemoryPool'], WAIT['QQmlJS.AST.ExportClause'])
  @overload(NoneType, WAIT['QQmlJS.AST.ExportClause'])
  def __init__(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      exportClause: Optional[QQmlJS.AST.ExportClause],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::ExportDeclaration::ExportDeclaration(ExportClause
    *exportClause)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-exportdeclaration.html

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    exportClause : Optional[QQmlJS.AST.ExportClause]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlJS::AST::ExportDeclaration::ExportDeclaration(ExportClause
    #      *exportClause)
    self._noteCreation(ExportDeclaration, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST17ExportDeclarationC1EPNS0_12ExportClauseE',
        self._addressOf(pool), self._addressOf(exportClause),
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

  @staticmethod
  def accept0(*__, **_) -> Never:
    """
    Qt's 'void QQmlJS::AST::ExportDeclaration::accept0(BaseVisitor
    *visitor)': names 'QQmlJS::AST::BaseVisitor', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.ExportDeclaration.accept0' has no cute function yet. "
        "Qt's 'void QQmlJS::AST::ExportDeclaration::accept0(BaseVisitor "
        "*visitor)': names 'QQmlJS::AST::BaseVisitor', which has no cute "
        "class yet.")
