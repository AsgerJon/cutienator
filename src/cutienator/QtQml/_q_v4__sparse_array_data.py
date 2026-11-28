"""
QV4::SparseArrayData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4arraydata_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::SparseArrayData to be private: it declares the class in a
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


class SparseArrayData(QV4.ArrayData):
  """
  The cute side of Qt's QV4::SparseArrayData: a plain Python object standing
  in front of one C++ QV4::SparseArrayData.

  It is built on the cute 'QV4::ArrayData', as Qt's QV4::SparseArrayData is
  built on Qt's QV4::ArrayData, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::SparseArrayData that has a ritual and that
  Python can call so far, 19 names in all: '__dataTest', 'd',
  'defaultInternalClass', 'virtualDestroy', 'sparse', 'setSparse',
  'allocate', 'free', 'mappedIndex', 'reallocate', 'get', 'put', 'putArray',
  'del_', 'setAttribute', 'push_front', 'pop_front', 'truncate', 'length'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QV4::VTable *QV4::SparseArrayData::staticVTable()': gives
    'QV4::VTable', which has no cute class yet.
  - Qt's 'Data *QV4::SparseArrayData::d()': takes in Python what 'const Data
    *QV4::SparseArrayData::d() const' takes.

  What has no ritual
  ------------------

  1 of the 22 functions Qt declares: 1 not a gap.

  What to expect
  --------------

  - The C++ QV4::SparseArrayData is created at the first use, not by
    'QV4::SparseArrayData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::SparseArrayData.
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
    *QV4::SparseArrayData::defaultInternalClass(QV4::EngineBase *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sparsearraydata.html#defaultInternalClass

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
    #  Heap::InternalClass
    #      *QV4::SparseArrayData::defaultInternalClass(QV4::EngineBase *e)
    address = Rituals.call(
        'ritual_ZN3QV415SparseArrayData20defaultInternalClassEPNS_10EngineB'
        'aseE',
        CuteMixin._addressOf(e),
    )
    return QV4.Heap.InternalClass._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.Heap.Base'])
  @overload(NoneType)
  def virtualDestroy(b: Optional[QV4.Heap.Base]) -> None:
    """
    Calls Qt's 'void QV4::SparseArrayData::virtualDestroy(QV4::Heap::Base
    *b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sparsearraydata.html#virtualDestroy

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::SparseArrayData::virtualDestroy(QV4::Heap::Base *b)
    Rituals.call(
        'ritual_ZN3QV415SparseArrayData14virtualDestroyEPNS_4Heap4BaseE',
        CuteMixin._addressOf(b),
    )

  @staticmethod
  @overload(WAIT['QV4.Object'])
  @overload(NoneType)
  @overload(WAIT['QV4.Object'], bool)
  @overload(NoneType, bool)
  def allocate(o: Optional[QV4.Object], doubleSlot: bool = False) -> int:
    """
    Calls Qt's 'uint QV4::SparseArrayData::allocate(Object *o, bool
    doubleSlot)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearraydata.html#allocate

    Parameters
    ----------

    o : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    doubleSlot : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  uint QV4::SparseArrayData::allocate(Object *o, bool doubleSlot)
    return Rituals.call(
        'ritual_ZN3QV415SparseArrayData8allocateEPNS_6ObjectEb',
        CuteMixin._addressOf(o), doubleSlot,
    )

  @staticmethod
  @overload(WAIT['QV4.Heap.ArrayData'], int)
  @overload(NoneType, int)
  def free(d: Optional[QV4.Heap.ArrayData], idx: int) -> None:
    """
    Calls Qt's 'void QV4::SparseArrayData::free(Heap::ArrayData *d, uint
    idx)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearraydata.html#free

    Parameters
    ----------

    d : Optional[QV4.Heap.ArrayData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    idx : int
      Passed on as it is.
    """
    #  void QV4::SparseArrayData::free(Heap::ArrayData *d, uint idx)
    Rituals.call(
        'ritual_ZN3QV415SparseArrayData4freeEPNS_4Heap9ArrayDataEj',
        CuteMixin._addressOf(d), idx,
    )

  @staticmethod
  @overload(WAIT['QV4.Object'], int, bool)
  @overload(NoneType, int, bool)
  def reallocate(
      o: Optional[QV4.Object],
      n: int,
      enforceAttributes: bool,
  ) -> Optional[QV4.Heap.ArrayData]:
    """
    Calls Qt's 'Heap::ArrayData *QV4::SparseArrayData::reallocate(Object *o,
    uint n, bool enforceAttributes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sparsearraydata.html#reallocate

    Parameters
    ----------

    o : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    n : int
      Passed on as it is.

    enforceAttributes : bool
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Heap.ArrayData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::ArrayData *QV4::SparseArrayData::reallocate(Object *o, uint n,
    #      bool enforceAttributes)
    address = Rituals.call(
        'ritual_ZN3QV415SparseArrayData10reallocateEPNS_6ObjectEjb',
        CuteMixin._addressOf(o), n, enforceAttributes,
    )
    return QV4.Heap.ArrayData._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.Heap.ArrayData'], int)
  @overload(NoneType, int)
  def get(d: Optional[QV4.Heap.ArrayData], index: int) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::SparseArrayData::get(const Heap::ArrayData
    *d, uint index)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearraydata.html#get

    Parameters
    ----------

    d : Optional[QV4.Heap.ArrayData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::SparseArrayData::get(const Heap::ArrayData *d, uint
    #      index)
    return Rituals.call(
        'ritual_ZN3QV415SparseArrayData3getEPKNS_4Heap9ArrayDataEj',
        CuteMixin._addressOf(d), index,
    )

  @staticmethod
  @overload(WAIT['QV4.Object'], int, QV4.Value)
  @overload(NoneType, int, QV4.Value)
  def put(o: Optional[QV4.Object], index: int, value: QV4.Value) -> bool:
    """
    Calls Qt's 'bool QV4::SparseArrayData::put(Object *o, uint index, const
    Value &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearraydata.html#put

    Parameters
    ----------

    o : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  bool QV4::SparseArrayData::put(Object *o, uint index, const Value
    #      &value)
    return Rituals.call(
        'ritual_ZN3QV415SparseArrayData3putEPNS_6ObjectEjRKNS_5ValueE',
        CuteMixin._addressOf(o), index, CuteMixin._valueOf(value),
    )

  @staticmethod
  @overload(WAIT['QV4.Object'], int, QV4.Value, int)
  @overload(WAIT['QV4.Object'], int, NoneType, int)
  @overload(NoneType, int, QV4.Value, int)
  @overload(NoneType, int, NoneType, int)
  def putArray(
      o: Optional[QV4.Object],
      index: int,
      values: Optional[QV4.Value],
      n: int,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::SparseArrayData::putArray(Object *o, uint index,
    const Value *values, uint n)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearraydata.html#putArray

    Parameters
    ----------

    o : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    values : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    n : int
      Passed on as it is.
    """
    #  bool QV4::SparseArrayData::putArray(Object *o, uint index, const Value
    #      *values, uint n)
    return Rituals.call(
        'ritual_ZN3QV415SparseArrayData8putArrayEPNS_6ObjectEjPKNS_5ValueEj',
        CuteMixin._addressOf(o), index, CuteMixin._addressOf(values), n,
    )

  @staticmethod
  @overload(WAIT['QV4.Object'], int)
  @overload(NoneType, int)
  def del_(o: Optional[QV4.Object], index: int) -> bool:
    """
    Calls Qt's 'bool QV4::SparseArrayData::del(Object *o, uint index)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearraydata.html#del

    Parameters
    ----------

    o : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.
    """
    #  bool QV4::SparseArrayData::del(Object *o, uint index)
    return Rituals.call(
        'ritual_ZN3QV415SparseArrayData3delEPNS_6ObjectEj',
        CuteMixin._addressOf(o), index,
    )

  @staticmethod
  @overload(WAIT['QV4.Object'], int, WAIT['QV4.PropertyAttributes'])
  @overload(NoneType, int, WAIT['QV4.PropertyAttributes'])
  def setAttribute(
      o: Optional[QV4.Object],
      index: int,
      attrs: QV4.PropertyAttributes,
  ) -> None:
    """
    Calls Qt's 'void QV4::SparseArrayData::setAttribute(Object *o, uint
    index, PropertyAttributes attrs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sparsearraydata.html#setAttribute

    Parameters
    ----------

    o : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    attrs : QV4.PropertyAttributes
      Passed on as a value: Qt reads the C++ QV4::PropertyAttributes, which
      stays Python's own.
    """
    #  void QV4::SparseArrayData::setAttribute(Object *o, uint index,
    #      PropertyAttributes attrs)
    Rituals.call(
        'ritual_ZN3QV415SparseArrayData12setAttributeEPNS_6ObjectEjNS_18Pro'
        'pertyAttributesE',
        CuteMixin._addressOf(o), index, CuteMixin._valueOf(attrs),
    )

  @staticmethod
  @overload(WAIT['QV4.Object'], QV4.Value, int)
  @overload(WAIT['QV4.Object'], NoneType, int)
  @overload(NoneType, QV4.Value, int)
  @overload(NoneType, NoneType, int)
  def push_front(
      o: Optional[QV4.Object],
      values: Optional[QV4.Value],
      n: int,
  ) -> None:
    """
    Calls Qt's 'void QV4::SparseArrayData::push_front(Object *o, const Value
    *values, uint n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sparsearraydata.html#push_front

    Parameters
    ----------

    o : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    values : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    n : int
      Passed on as it is.
    """
    #  void QV4::SparseArrayData::push_front(Object *o, const Value *values,
    #      uint n)
    Rituals.call(
        'ritual_ZN3QV415SparseArrayData10push_frontEPNS_6ObjectEPKNS_5Value'
        'Ej',
        CuteMixin._addressOf(o), CuteMixin._addressOf(values), n,
    )

  @staticmethod
  @overload(WAIT['QV4.Object'])
  @overload(NoneType)
  def pop_front(o: Optional[QV4.Object]) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::SparseArrayData::pop_front(Object *o)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearraydata.html#pop_front

    Parameters
    ----------

    o : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::SparseArrayData::pop_front(Object *o)
    return Rituals.call(
        'ritual_ZN3QV415SparseArrayData9pop_frontEPNS_6ObjectE',
        CuteMixin._addressOf(o),
    )

  @staticmethod
  @overload(WAIT['QV4.Object'], int)
  @overload(NoneType, int)
  def truncate(o: Optional[QV4.Object], newLen: int) -> int:
    """
    Calls Qt's 'uint QV4::SparseArrayData::truncate(Object *o, uint newLen)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearraydata.html#truncate

    Parameters
    ----------

    o : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newLen : int
      Passed on as it is.
    """
    #  uint QV4::SparseArrayData::truncate(Object *o, uint newLen)
    return Rituals.call(
        'ritual_ZN3QV415SparseArrayData8truncateEPNS_6ObjectEj',
        CuteMixin._addressOf(o), newLen,
    )

  @staticmethod
  @overload(WAIT['QV4.Heap.ArrayData'])
  @overload(NoneType)
  def length(d: Optional[QV4.Heap.ArrayData]) -> int:
    """
    Calls Qt's 'uint QV4::SparseArrayData::length(const Heap::ArrayData *d)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearraydata.html#length

    Parameters
    ----------

    d : Optional[QV4.Heap.ArrayData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  uint QV4::SparseArrayData::length(const Heap::ArrayData *d)
    return Rituals.call(
        'ritual_ZN3QV415SparseArrayData6lengthEPKNS_4Heap9ArrayDataE',
        CuteMixin._addressOf(d),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::SparseArrayData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d(self) -> Optional[QV4.Heap.SparseArrayData]:
    """
    Calls Qt's 'const Data *QV4::SparseArrayData::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearraydata.html#d

    Returns
    -------

    Optional[QV4.Heap.SparseArrayData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Data *QV4::SparseArrayData::d() const
    address = self.uglySide.call('ritual_ZNK3QV415SparseArrayData1dEv')
    return QV4.Heap.SparseArrayData._cuteAt(address)

  def sparse(self) -> Optional[QV4.SparseArray]:
    """
    Calls Qt's 'SparseArray *QV4::SparseArrayData::sparse() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearraydata.html#sparse

    Returns
    -------

    Optional[QV4.SparseArray]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  SparseArray *QV4::SparseArrayData::sparse() const
    address = self.uglySide.call('ritual_ZNK3QV415SparseArrayData6sparseEv')
    return QV4.SparseArray._cuteAt(address)

  @overload(int)
  def mappedIndex(self, index: int) -> int:
    """
    Calls Qt's 'uint QV4::SparseArrayData::mappedIndex(uint index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sparsearraydata.html#mappedIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  uint QV4::SparseArrayData::mappedIndex(uint index) const
    return self.uglySide.call(
        'ritual_ZNK3QV415SparseArrayData11mappedIndexEj', index,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QV4.SparseArray'])
  @overload(NoneType)
  def setSparse(self, s: Optional[QV4.SparseArray]) -> None:
    """
    Calls Qt's 'void QV4::SparseArrayData::setSparse(SparseArray *s)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-sparsearraydata.html#setSparse

    Parameters
    ----------

    s : Optional[QV4.SparseArray]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::SparseArrayData::setSparse(SparseArray *s)
    self.uglySide.call(
        'ritual_ZN3QV415SparseArrayData9setSparseEPNS_11SparseArrayE',
        self._addressOf(s),
    )

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
    Calls Qt's 'void QV4::SparseArrayData::__dataTest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-sparsearraydata.html#__dataTest
    """
    #  void QV4::SparseArrayData::__dataTest()
    self.uglySide.call('ritual_ZN3QV415SparseArrayData10__dataTestEv')
