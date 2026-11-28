"""
QV4::ESTable binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4estable_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::ESTable to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ESTable(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::ESTable: a plain Python object standing in front
  of one C++ QV4::ESTable.

  C++ hands a QV4::ESTable around as a copy, so every C++ QV4::ESTable behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::ESTable that has a ritual and that Python can
  call so far, 8 names in all: 'markObjects', 'clear', 'set', 'has',
  'remove', 'size', 'iterate', 'removeUnmarkedKeys'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::ESTable::~ESTable()': the destructor: Python removes its C++
    QV4::ESTable by it, and has no other use for it.
  - Qt's 'ReturnedValue QV4::ESTable::get(const Value &k, bool *hasValue)
    const': takes a number to change where it is.
  - Qt's 'void QV4::ESTable::observeShifts(ShiftObserver &observer)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QV4::ESTable::stopObservingShifts(ShiftObserver &observer)':
    takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QV4::ESTable is created at the first use, not by
    'QV4::ESTable(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::ESTable back gives a copy the ritual made for
    Python, in a new cute QV4::ESTable.
  - Each name of Qt's QV4::ESTable that has no cute function yet, 'get',
    'observeShifts', 'stopObservingShifts', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QV4::ESTable, each a class in here as in
  #  C++.

  class ShiftObserver(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::ESTable::ShiftObserver: a plain Python object
    standing in front of one C++ QV4::ESTable::ShiftObserver.

    C++ hands a QV4::ESTable::ShiftObserver around as a copy, so every C++
    QV4::ESTable::ShiftObserver behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QV4::ESTable::ShiftObserver that has a ritual and
    that Python can call so far, 1 name in all: 'next'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::ESTable::ShiftObserver::~ShiftObserver()': the destructor:
      Python removes its C++ QV4::ESTable::ShiftObserver by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QV4::ESTable::ShiftObserver is created at the first use, not by
      'QV4::ESTable::ShiftObserver(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::ESTable::ShiftObserver back gives a copy the
      ritual made for Python, in a new cute QV4::ESTable::ShiftObserver.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::ESTable::ShiftObserver'

    #  Qt's '~QV4::ESTable::ShiftObserver()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::ESTable::ShiftObserver behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV47ESTable13ShiftObserverD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def next(self) -> None:
      """
      Calls Qt's 'void QV4::ESTable::ShiftObserver::next()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-estable-shiftobserver.html#next
      """
      #  void QV4::ESTable::ShiftObserver::next()
      self.uglySide.call('ritual_ZN3QV47ESTable13ShiftObserver4nextEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::ESTable'

  #  Qt's '~QV4::ESTable()'. Naming it makes this a value class: Python owns
  #  every C++ QV4::ESTable behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV47ESTableD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QV4.Value'])
  def has(self, k: QV4.Value) -> bool:
    """
    Calls Qt's 'bool QV4::ESTable::has(const Value &k) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-estable.html#has

    Parameters
    ----------

    k : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  bool QV4::ESTable::has(const Value &k) const
    return self.uglySide.call(
        'ritual_ZNK3QV47ESTable3hasERKNS_5ValueE', self._valueOf(k),
    )

  def size(self) -> int:
    """
    Calls Qt's 'uint QV4::ESTable::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-estable.html#size
    """
    #  uint QV4::ESTable::size() const
    return self.uglySide.call('ritual_ZNK3QV47ESTable4sizeEv')

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QV4::ESTable::ESTable()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-estable.html#ESTable
    """
    #  QV4::ESTable::ESTable()
    self._noteCreation(ESTable, lambda: Rituals.call(
        'ritual_ZN3QV47ESTableC1Ev',
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

  @overload(WAIT['QV4.MarkStack'], bool)
  @overload(NoneType, bool)
  def markObjects(self, s: Optional[QV4.MarkStack], isWeakMap: bool) -> None:
    """
    Calls Qt's 'void QV4::ESTable::markObjects(MarkStack *s, bool
    isWeakMap)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-estable.html#markObjects

    Parameters
    ----------

    s : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    isWeakMap : bool
      Passed on as it is.
    """
    #  void QV4::ESTable::markObjects(MarkStack *s, bool isWeakMap)
    self.uglySide.call(
        'ritual_ZN3QV47ESTable11markObjectsEPNS_9MarkStackEb',
        self._addressOf(s), isWeakMap,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QV4::ESTable::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-estable.html#clear
    """
    #  void QV4::ESTable::clear()
    self.uglySide.call('ritual_ZN3QV47ESTable5clearEv')

  @overload(WAIT['QV4.Value'], WAIT['QV4.Value'])
  def set(self, k: QV4.Value, v: QV4.Value) -> None:
    """
    Calls Qt's 'void QV4::ESTable::set(const Value &k, const Value &v)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-estable.html#set

    Parameters
    ----------

    k : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    v : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QV4::ESTable::set(const Value &k, const Value &v)
    self.uglySide.call(
        'ritual_ZN3QV47ESTable3setERKNS_5ValueES3_',
        self._valueOf(k), self._valueOf(v),
    )

  @overload(WAIT['QV4.Value'])
  def remove(self, k: QV4.Value) -> bool:
    """
    Calls Qt's 'bool QV4::ESTable::remove(const Value &k)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-estable.html#remove

    Parameters
    ----------

    k : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  bool QV4::ESTable::remove(const Value &k)
    return self.uglySide.call(
        'ritual_ZN3QV47ESTable6removeERKNS_5ValueE', self._valueOf(k),
    )

  @overload(int, WAIT['QV4.Value'], WAIT['QV4.Value'])
  @overload(int, WAIT['QV4.Value'], NoneType)
  @overload(int, NoneType, WAIT['QV4.Value'])
  @overload(int, NoneType, NoneType)
  def iterate(
      self,
      idx: int,
      k: Optional[QV4.Value],
      v: Optional[QV4.Value],
  ) -> None:
    """
    Calls Qt's 'void QV4::ESTable::iterate(uint idx, Value *k, Value *v)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-estable.html#iterate

    Parameters
    ----------

    idx : int
      Passed on as it is.

    k : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    v : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::ESTable::iterate(uint idx, Value *k, Value *v)
    self.uglySide.call(
        'ritual_ZN3QV47ESTable7iterateEjPNS_5ValueES2_',
        idx, self._addressOf(k), self._addressOf(v),
    )

  def removeUnmarkedKeys(self) -> None:
    """
    Calls Qt's 'void QV4::ESTable::removeUnmarkedKeys()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-estable.html#removeUnmarkedKeys
    """
    #  void QV4::ESTable::removeUnmarkedKeys()
    self.uglySide.call('ritual_ZN3QV47ESTable18removeUnmarkedKeysEv')

  @staticmethod
  def get(*__, **_) -> Never:
    """
    Qt's 'ReturnedValue QV4::ESTable::get(const Value &k, bool *hasValue)
    const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QV4.ESTable.get' has no cute function yet. Qt's 'ReturnedValue "
        "QV4::ESTable::get(const Value &k, bool *hasValue) const': takes a "
        "number to change where it is.")

  @staticmethod
  def observeShifts(*__, **_) -> Never:
    """
    Qt's 'void QV4::ESTable::observeShifts(ShiftObserver &observer)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.ESTable.observeShifts' has no cute function yet. Qt's 'void "
        "QV4::ESTable::observeShifts(ShiftObserver &observer)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def stopObservingShifts(*__, **_) -> Never:
    """
    Qt's 'void QV4::ESTable::stopObservingShifts(ShiftObserver &observer)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.ESTable.stopObservingShifts' has no cute function yet. Qt's "
        "'void QV4::ESTable::stopObservingShifts(ShiftObserver &observer)': "
        "takes a type Python has no way to hand over yet.")
