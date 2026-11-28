"""
QQmlJS::AST::Catch binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmljsast_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlJS::AST::Catch to be private: it declares the class in a
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


class Catch(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJS::AST::Catch: a plain Python object standing in
  front of one C++ QQmlJS::AST::Catch.

  What exists
  -----------

  Every function of Qt's QQmlJS::AST::Catch that has a ritual and that Python
  can call so far, 2 names in all: 'firstSourceLocation',
  'lastSourceLocation'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQmlJS::AST::Catch::accept0(BaseVisitor *visitor)': names
    'QQmlJS::AST::BaseVisitor', which has no cute class yet.

  What to expect
  --------------

  - The C++ QQmlJS::AST::Catch is created at the first use, not by
    'QQmlJS::AST::Catch(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlJS::AST::Catch.
  - Each name of Qt's QQmlJS::AST::Catch that has no cute function yet,
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
  __qt_class__ = 'QQmlJS::AST::Catch'

  #  A C++ QQmlJS::AST::Catch Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlJS_AST_Catch'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def firstSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation QQmlJS::AST::Catch::firstSourceLocation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-catch.html#firstSourceLocation

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::Catch::firstSourceLocation() const
    ritual = 'ritual_ZNK6QQmlJS3AST5Catch19firstSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK6QQmlJS3AST5Catch19firstSourceLocationEv'
    address = self.uglySide.call(ritual)
    return QQmlJS.SourceLocation._cuteOwning(address)

  def lastSourceLocation(self) -> QQmlJS.SourceLocation:
    """
    Calls Qt's 'SourceLocation QQmlJS::AST::Catch::lastSourceLocation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljs-ast-catch.html#lastSourceLocation

    Returns
    -------

    QQmlJS.SourceLocation
      A new cute QQmlJS::SourceLocation around the copy Qt gave back. Python
      owns it.
    """
    #  SourceLocation QQmlJS::AST::Catch::lastSourceLocation() const
    ritual = 'ritual_ZNK6QQmlJS3AST5Catch18lastSourceLocationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK6QQmlJS3AST5Catch18lastSourceLocationEv'
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
      WAIT['QQmlJS.MemoryPool'], WAIT['QQmlJS.AST.PatternElement'],
      WAIT['QQmlJS.AST.Block'],
  )
  @overload(
      WAIT['QQmlJS.MemoryPool'], WAIT['QQmlJS.AST.PatternElement'], NoneType,
  )
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType, WAIT['QQmlJS.AST.Block'])
  @overload(WAIT['QQmlJS.MemoryPool'], NoneType, NoneType)
  @overload(
      NoneType, WAIT['QQmlJS.AST.PatternElement'], WAIT['QQmlJS.AST.Block'],
  )
  @overload(NoneType, WAIT['QQmlJS.AST.PatternElement'], NoneType)
  @overload(NoneType, NoneType, WAIT['QQmlJS.AST.Block'])
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      pool: Optional[QQmlJS.MemoryPool],
      p: Optional[QQmlJS.AST.PatternElement],
      stmt: Optional[QQmlJS.AST.Block],
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlJS::AST::Catch::Catch(PatternElement
    *p, Block *stmt)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmljs-ast-catch.html#Catch

    Parameters
    ----------

    pool : Optional[QQmlJS.MemoryPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    p : Optional[QQmlJS.AST.PatternElement]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stmt : Optional[QQmlJS.AST.Block]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlJS::AST::Catch::Catch(PatternElement *p, Block *stmt)
    self._noteCreation(Catch, lambda: Rituals.call(
        'ritual_ZN6QQmlJS3AST5CatchC1EPNS0_14PatternElementEPNS0_5BlockE',
        self._addressOf(pool), self._addressOf(p), self._addressOf(stmt),
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
    Qt's 'void QQmlJS::AST::Catch::accept0(BaseVisitor *visitor)': names
    'QQmlJS::AST::BaseVisitor', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlJS.AST.Catch.accept0' has no cute function yet. Qt's 'void "
        "QQmlJS::AST::Catch::accept0(BaseVisitor *visitor)': names "
        "'QQmlJS::AST::BaseVisitor', which has no cute class yet.")
