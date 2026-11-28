"""
QQmlJS::AST::CaseBlock binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlJS::AST::CaseBlock to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
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


class CaseBlock(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::AST::CaseBlock: a plain Python object
  standing in front of one C++ QQmlJS::AST::CaseBlock.

  What exists
  -----------

  Every function of Qt's QQmlJS::AST::CaseBlock that has a ritual and that
  Python can call so far, 2 names in all: 'firstSourceLocation',
  'lastSourceLocation'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlJS::AST::CaseBlock::accept0(BaseVisitor *visitor)': names
    'QQmlJS::AST::BaseVisitor', which has no cute class yet.

  What to expect
  --------------

  - The C++ QQmlJS::AST::CaseBlock is created at the first use, not by
    'QQmlJS::AST::CaseBlock(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJS::AST::CaseBlock.
  - Each name of Qt's QQmlJS::AST::CaseBlock that has no cute function yet,
    'accept0', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlJS::AST::CaseBlock'

  #  A C++ QQmlJS::AST::CaseBlock Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJS_AST_CaseBlock'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def firstSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation QQmlJS::AST::CaseBlock::firstSourceLocation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-caseblock.html#firstSourceLocation

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::CaseBlock::firstSourceLocation() const
    ritual = 'ritual_ZNK6QQmlJS3AST9CaseBlock19firstSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK6QQmlJS3AST9CaseBlock19firstSourceLocationEv'
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def lastSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation QQmlJS::AST::CaseBlock::lastSourceLocation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-caseblock.html#lastSourceLocation

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::CaseBlock::lastSourceLocation() const
    ritual = 'ritual_ZNK6QQmlJS3AST9CaseBlock18lastSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK6QQmlJS3AST9CaseBlock18lastSourceLocationEv'
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

  @overload(WAIT['QQmlJS.MemoryPool'], WAIT['QQmlJS.AST.CaseClauses'])
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType)
  @overload(NoneType, WAIT['QQmlJS.AST.CaseClauses'])
  @overload(NoneType, NoneType)
  @overload(
      WAIT['QQmlJS.MemoryPool'], WAIT['QQmlJS.AST.CaseClauses'],
      WAIT['QQmlJS.AST.DefaultClause'],
  )
  @overload(
      WAIT['QQmlJS.MemoryPool'], WAIT['QQmlJS.AST.CaseClauses'], NoneType,
  )
  @overload(
      WAIT['QQmlJS.MemoryPool'], NoneType, WAIT['QQmlJS.AST.DefaultClause'],
  )
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType, NoneType)
  @overload(
      NoneType, WAIT['QQmlJS.AST.CaseClauses'],
      WAIT['QQmlJS.AST.DefaultClause'],
  )
  @overload(NoneType, WAIT['QQmlJS.AST.CaseClauses'], NoneType)
  @overload(NoneType, NoneType, WAIT['QQmlJS.AST.DefaultClause'])
  @overload(NoneType, NoneType, NoneType)
  @overload(
      WAIT['QQmlJS.MemoryPool'], WAIT['QQmlJS.AST.CaseClauses'],
      WAIT['QQmlJS.AST.DefaultClause'], WAIT['QQmlJS.AST.CaseClauses'],
  )
  @overload(
      WAIT['QQmlJS.MemoryPool'], WAIT['QQmlJS.AST.CaseClauses'],
      WAIT['QQmlJS.AST.DefaultClause'], NoneType,
  )
  @overload(
      WAIT['QQmlJS.MemoryPool'], WAIT['QQmlJS.AST.CaseClauses'], NoneType,
      WAIT['QQmlJS.AST.CaseClauses'],
  )
  @overload(
      WAIT['QQmlJS.MemoryPool'], WAIT['QQmlJS.AST.CaseClauses'], NoneType,
      NoneType,
  )
  @overload(
      WAIT['QQmlJS.MemoryPool'], NoneType, WAIT['QQmlJS.AST.DefaultClause'],
      WAIT['QQmlJS.AST.CaseClauses'],
  )
  @overload(
      WAIT['QQmlJS.MemoryPool'], NoneType, WAIT['QQmlJS.AST.DefaultClause'],
      NoneType,
  )
  @overload(
      WAIT['QQmlJS.MemoryPool'], NoneType, NoneType,
      WAIT['QQmlJS.AST.CaseClauses'],
  )
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType, NoneType, NoneType)
  @overload(
      NoneType, WAIT['QQmlJS.AST.CaseClauses'],
      WAIT['QQmlJS.AST.DefaultClause'], WAIT['QQmlJS.AST.CaseClauses'],
  )
  @overload(
      NoneType, WAIT['QQmlJS.AST.CaseClauses'],
      WAIT['QQmlJS.AST.DefaultClause'], NoneType,
  )
  @overload(
      NoneType, WAIT['QQmlJS.AST.CaseClauses'], NoneType,
      WAIT['QQmlJS.AST.CaseClauses'],
  )
  @overload(NoneType, WAIT['QQmlJS.AST.CaseClauses'], NoneType, NoneType)
  @overload(
      NoneType, NoneType, WAIT['QQmlJS.AST.DefaultClause'],
      WAIT['QQmlJS.AST.CaseClauses'],
  )
  @overload(NoneType, NoneType, WAIT['QQmlJS.AST.DefaultClause'], NoneType)
  @overload(NoneType, NoneType, NoneType, WAIT['QQmlJS.AST.CaseClauses'])
  @overload(NoneType, NoneType, NoneType, NoneType)
  def __init__(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      c: Optional[QQmlJS.AST.CaseClauses],
      d: Optional[QQmlJS.AST.DefaultClause] = None,
      r: Optional[QQmlJS.AST.CaseClauses] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJS::AST::CaseBlock::CaseBlock(CaseClauses *c, DefaultClause *d,
    CaseClauses *r)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-caseblock.html#CaseBlock

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    c : Optional[QQmlJS.AST.CaseClauses]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    d : Optional[QQmlJS.AST.DefaultClause]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    r : Optional[QQmlJS.AST.CaseClauses]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlJS::AST::CaseBlock::CaseBlock(CaseClauses *c, DefaultClause *d,
    #      CaseClauses *r)
    self._noteCreation(CaseBlock, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST9CaseBlockC1EPNS0_11CaseClausesEPNS0_13Default'
        'ClauseES3_',
        self._addressOf(pool), self._addressOf(c), self._addressOf(d),
        self._addressOf(r),
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
    Qt's 'void QQmlJS::AST::CaseBlock::accept0(BaseVisitor *visitor)': names
    'QQmlJS::AST::BaseVisitor', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.CaseBlock.accept0' has no cute function yet. Qt's "
        "'void QQmlJS::AST::CaseBlock::accept0(BaseVisitor *visitor)': "
        "names 'QQmlJS::AST::BaseVisitor', which has no cute class yet.")
