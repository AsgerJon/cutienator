"""
QV4::RegExpCtor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4regexpobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::RegExpCtor to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import WAIT
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class RegExpCtor(QV4.FunctionObject):
  """
  The cute side of Qt's QV4::RegExpCtor: a plain Python object standing in
  front of one C++ QV4::RegExpCtor.

  It is built on the cute 'QV4::FunctionObject', as Qt's QV4::RegExpCtor is
  built on Qt's QV4::FunctionObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::RegExpCtor that has a ritual and that Python
  can call so far, 7 names in all: '__dataTest', 'd_unchecked', 'd',
  'lastMatch', 'lastInput', 'lastMatchStart', 'lastMatchEnd'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has no ritual
  ------------------

  7 of the 14 functions Qt declares: 3 forbidden; 2 leans on 'QV4; 1 not a
  gap; 1 Qt's library has no name for it, and its code in Qt's source does
  not compile apart from its file.

  What to expect
  --------------

  - The C++ QV4::RegExpCtor is created at the first use, not by
    'QV4::RegExpCtor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::RegExpCtor.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::RegExpCtor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.RegExpCtor]:
    """
    Calls Qt's 'QV4::Heap::RegExpCtor *QV4::RegExpCtor::d_unchecked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-regexpctor.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.RegExpCtor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::RegExpCtor *QV4::RegExpCtor::d_unchecked() const
    address = self.uglySide.call('ritual_ZNK3QV410RegExpCtor11d_uncheckedEv')
    return QV4.Heap.RegExpCtor._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.RegExpCtor]:
    """
    Calls Qt's 'QV4::Heap::RegExpCtor *QV4::RegExpCtor::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-regexpctor.html#d

    Returns
    -------

    Optional[QV4.Heap.RegExpCtor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::RegExpCtor *QV4::RegExpCtor::d() const
    address = self.uglySide.call('ritual_ZNK3QV410RegExpCtor1dEv')
    return QV4.Heap.RegExpCtor._cuteAt(address)

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
    Calls Qt's 'void QV4::RegExpCtor::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-regexpctor.html#__dataTest
    """
    #  void QV4::RegExpCtor::__dataTest()
    self.uglySide.call('ritual_ZN3QV410RegExpCtor10__dataTestEv')

  def lastMatch(self) -> QV4.Value:
    """
    Calls Qt's 'Value QV4::RegExpCtor::lastMatch()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-regexpctor.html#lastMatch

    Returns
    -------

    QV4.Value
      A new cute QV4::Value around the copy Qt gave back. Python owns it.
    """
    #  Value QV4::RegExpCtor::lastMatch()
    address = self.uglySide.call('ritual_ZN3QV410RegExpCtor9lastMatchEv')
    return QV4.Value._cuteOwning(address)

  def lastInput(self) -> Optional[QV4.Heap.String]:
    """
    Calls Qt's 'Heap::String *QV4::RegExpCtor::lastInput()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-regexpctor.html#lastInput

    Returns
    -------

    Optional[QV4.Heap.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::String *QV4::RegExpCtor::lastInput()
    address = self.uglySide.call('ritual_ZN3QV410RegExpCtor9lastInputEv')
    return QV4.Heap.String._cuteAt(address)

  def lastMatchStart(self) -> int:
    """
    Calls Qt's 'int QV4::RegExpCtor::lastMatchStart()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-regexpctor.html#lastMatchStart
    """
    #  int QV4::RegExpCtor::lastMatchStart()
    return self.uglySide.call('ritual_ZN3QV410RegExpCtor14lastMatchStartEv')

  def lastMatchEnd(self) -> int:
    """
    Calls Qt's 'int QV4::RegExpCtor::lastMatchEnd()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-regexpctor.html#lastMatchEnd
    """
    #  int QV4::RegExpCtor::lastMatchEnd()
    return self.uglySide.call('ritual_ZN3QV410RegExpCtor12lastMatchEndEv')
