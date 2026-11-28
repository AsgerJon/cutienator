"""
QV4::StringOrSymbol binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4string_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QV4::StringOrSymbol to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class StringOrSymbol(QV4.Managed):
  """
  The cute side of Qt's QV4::StringOrSymbol: a plain Python object standing
  in front of one C++ QV4::StringOrSymbol.

  It is built on the cute 'QV4::Managed', as Qt's QV4::StringOrSymbol is
  built on Qt's QV4::Managed, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::StringOrSymbol that has a ritual and that
  Python can call so far, 8 names in all: '__dataTest', 'd_unchecked', 'd',
  'virtualDestroy', 'createPropertyKey', 'propertyKey', 'toPropertyKey',
  'toQString'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QV4::VTable *QV4::StringOrSymbol::staticVTable()': gives
    'QV4::VTable', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 13 functions Qt declares: 3 forbidden; 1 not a gap.

  What to expect
  --------------

  - The C++ QV4::StringOrSymbol is created at the first use, not by
    'QV4::StringOrSymbol(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::StringOrSymbol.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.Heap.Base'])
  @overload(NoneType)
  def virtualDestroy(b: Optional[QV4.Heap.Base]) -> None:
    """
    Calls Qt's 'void QV4::StringOrSymbol::virtualDestroy(QV4::Heap::Base
    *b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-stringorsymbol.html#virtualDestroy

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::StringOrSymbol::virtualDestroy(QV4::Heap::Base *b)
    Rituals.call(
        'ritual_ZN3QV414StringOrSymbol14virtualDestroyEPNS_4Heap4BaseE',
        CuteMixin._addressOf(b),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::StringOrSymbol'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.StringOrSymbol]:
    """
    Calls Qt's 'QV4::Heap::StringOrSymbol *QV4::StringOrSymbol::d_unchecked()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-stringorsymbol.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.StringOrSymbol]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::StringOrSymbol *QV4::StringOrSymbol::d_unchecked() const
    address = self.uglySide.call(
        'ritual_ZNK3QV414StringOrSymbol11d_uncheckedEv',
    )
    return QV4.Heap.StringOrSymbol._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.StringOrSymbol]:
    """
    Calls Qt's 'QV4::Heap::StringOrSymbol *QV4::StringOrSymbol::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-stringorsymbol.html#d

    Returns
    -------

    Optional[QV4.Heap.StringOrSymbol]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::StringOrSymbol *QV4::StringOrSymbol::d() const
    address = self.uglySide.call('ritual_ZNK3QV414StringOrSymbol1dEv')
    return QV4.Heap.StringOrSymbol._cuteAt(address)

  def propertyKey(self) -> QV4.PropertyKey:
    """
    Calls Qt's 'PropertyKey QV4::StringOrSymbol::propertyKey() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-stringorsymbol.html#propertyKey

    Returns
    -------

    QV4.PropertyKey
      A new cute QV4::PropertyKey around the copy Qt gave back. Python owns
      it.
    """
    #  PropertyKey QV4::StringOrSymbol::propertyKey() const
    address = self.uglySide.call(
        'ritual_ZNK3QV414StringOrSymbol11propertyKeyEv',
    )
    return QV4.PropertyKey._cuteOwning(address)

  def toPropertyKey(self) -> QV4.PropertyKey:
    """
    Calls Qt's 'PropertyKey QV4::StringOrSymbol::toPropertyKey() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-stringorsymbol.html#toPropertyKey

    Returns
    -------

    QV4.PropertyKey
      A new cute QV4::PropertyKey around the copy Qt gave back. Python owns
      it.
    """
    #  PropertyKey QV4::StringOrSymbol::toPropertyKey() const
    address = self.uglySide.call(
        'ritual_ZNK3QV414StringOrSymbol13toPropertyKeyEv',
    )
    return QV4.PropertyKey._cuteOwning(address)

  def toQString(self) -> str:
    """
    Calls Qt's 'QString QV4::StringOrSymbol::toQString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-stringorsymbol.html#toQString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::StringOrSymbol::toQString() const
    return self.uglySide.call('ritual_ZNK3QV414StringOrSymbol9toQStringEv')

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
    Calls Qt's 'void QV4::StringOrSymbol::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-stringorsymbol.html#__dataTest
    """
    #  void QV4::StringOrSymbol::__dataTest()
    self.uglySide.call('ritual_ZN3QV414StringOrSymbol10__dataTestEv')

  def createPropertyKey(self) -> None:
    """
    Calls Qt's 'void QV4::StringOrSymbol::createPropertyKey() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-stringorsymbol.html#createPropertyKey
    """
    #  void QV4::StringOrSymbol::createPropertyKey() const
    self.uglySide.call('ritual_ZNK3QV414StringOrSymbol17createPropertyKeyEv')
