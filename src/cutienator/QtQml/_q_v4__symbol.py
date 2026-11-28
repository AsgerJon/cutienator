"""
QV4::Symbol binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4symbol_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QV4::Symbol to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Symbol(QV4.StringOrSymbol):
  """
  The cute side of Qt's QV4::Symbol: a plain Python object standing in front
  of one C++ QV4::Symbol.

  It is built on the cute 'QV4::StringOrSymbol', as Qt's QV4::Symbol is built
  on Qt's QV4::StringOrSymbol, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Symbol that has a ritual and that Python can
  call so far, 6 names in all: '__dataTest', 'd_unchecked', 'd',
  'defaultInternalClass', 'virtualDestroy', 'descriptiveString'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has no ritual
  ------------------

  6 of the 12 functions Qt declares: 3 forbidden; 2 leans on 'QV4; 1 not a
  gap.

  What to expect
  --------------

  - The C++ QV4::Symbol is created at the first use, not by
    'QV4::Symbol(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Symbol.
  - Each name of Qt's QV4::Symbol that has no cute function yet, 'create',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.EngineBase'])
  @overload(NoneType)
  def defaultInternalClass(
      e: Optional[QV4.EngineBase],
  ) -> Optional[QV4.Heap.InternalClass]:
    """
    Calls Qt's 'Heap::InternalClass
    *QV4::Symbol::defaultInternalClass(QV4::EngineBase *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-symbol.html#defaultInternalClass

    Parameters
    ----------

    e : Optional[QV4.EngineBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.InternalClass]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::InternalClass *QV4::Symbol::defaultInternalClass(QV4::EngineBase
    #      *e)
    address = Rituals.call(
        'ritual_ZN3QV46Symbol20defaultInternalClassEPNS_10EngineBaseE',
        CuteMixin._addressOf(e),
    )
    return QV4.Heap.InternalClass._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.Heap.Base'])
  @overload(NoneType)
  def virtualDestroy(b: Optional[QV4.Heap.Base]) -> None:
    """
    Calls Qt's 'void QV4::Symbol::virtualDestroy(QV4::Heap::Base *b)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-symbol.html#virtualDestroy

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Symbol::virtualDestroy(QV4::Heap::Base *b)
    Rituals.call(
        'ritual_ZN3QV46Symbol14virtualDestroyEPNS_4Heap4BaseE',
        CuteMixin._addressOf(b),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Symbol'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.Symbol]:
    """
    Calls Qt's 'QV4::Heap::Symbol *QV4::Symbol::d_unchecked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-symbol.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.Symbol]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::Symbol *QV4::Symbol::d_unchecked() const
    address = self.uglySide.call('ritual_ZNK3QV46Symbol11d_uncheckedEv')
    return QV4.Heap.Symbol._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.Symbol]:
    """
    Calls Qt's 'QV4::Heap::Symbol *QV4::Symbol::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-symbol.html#d

    Returns
    -------

    Optional[QV4.Heap.Symbol]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::Symbol *QV4::Symbol::d() const
    address = self.uglySide.call('ritual_ZNK3QV46Symbol1dEv')
    return QV4.Heap.Symbol._cuteAt(address)

  def descriptiveString(self) -> str:
    """
    Calls Qt's 'QString QV4::Symbol::descriptiveString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-symbol.html#descriptiveString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::Symbol::descriptiveString() const
    return self.uglySide.call('ritual_ZNK3QV46Symbol17descriptiveStringEv')

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

  def __dataTest(self) -> None:
    """
    Calls Qt's 'void QV4::Symbol::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-symbol.html#__dataTest
    """
    #  void QV4::Symbol::__dataTest()
    self.uglySide.call('ritual_ZN3QV46Symbol10__dataTestEv')

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'Heap::Symbol *QV4::Symbol::create(ExecutionEngine *e, const QString
    &s)': leans on 'QV4::Symbol::static_vtbl', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QV4.Symbol.create' has no cute function yet. Qt's 'Heap::Symbol "
        "*QV4::Symbol::create(ExecutionEngine *e, const QString &s)': leans "
        "on 'QV4::Symbol::static_vtbl', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")
