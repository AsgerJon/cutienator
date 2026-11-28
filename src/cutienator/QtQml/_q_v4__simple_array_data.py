"""
QV4::SimpleArrayData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4arraydata_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::SimpleArrayData to be private: it declares the class in a
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


class SimpleArrayData(QV4.ArrayData):
  """
  The cute side of Qt's QV4::SimpleArrayData: a plain Python object standing
  in front of one C++ QV4::SimpleArrayData.

  It is built on the cute 'QV4::ArrayData', as Qt's QV4::SimpleArrayData is
  built on Qt's QV4::ArrayData, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::SimpleArrayData that has a ritual and that
  Python can call so far, 16 names in all: '__dataTest', 'd',
  'defaultInternalClass', 'mappedIndex', 'data', 'len', 'reallocate', 'get',
  'put', 'putArray', 'del_', 'setAttribute', 'push_front', 'pop_front',
  'truncate', 'length'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QV4::VTable *QV4::SimpleArrayData::staticVTable()': gives
    'QV4::VTable', which has no cute class yet.
  - Qt's 'Data *QV4::SimpleArrayData::d()': takes in Python what 'const Data
    *QV4::SimpleArrayData::d() const' takes.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 1 not a gap; 1 takes or gives a type
  that cannot be passed yet.

  What to expect
  --------------

  - The C++ QV4::SimpleArrayData is created at the first use, not by
    'QV4::SimpleArrayData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::SimpleArrayData.
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
    *QV4::SimpleArrayData::defaultInternalClass(QV4::EngineBase *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-simplearraydata.html#defaultInternalClass

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
    #      *QV4::SimpleArrayData::defaultInternalClass(QV4::EngineBase *e)
    address = Rituals.call(
        'ritual_ZN3QV415SimpleArrayData20defaultInternalClassEPNS_10EngineB'
        'aseE',
        CuteMixin._addressOf(e),
    )
    return QV4.Heap.InternalClass._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.Object'], int, bool)
  @overload(NoneType, int, bool)
  def reallocate(
      o: Optional[QV4.Object],
      n: int,
      enforceAttributes: bool,
  ) -> Optional[QV4.Heap.ArrayData]:
    """
    Calls Qt's 'Heap::ArrayData *QV4::SimpleArrayData::reallocate(Object *o,
    uint n, bool enforceAttributes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-simplearraydata.html#reallocate

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
    #  Heap::ArrayData *QV4::SimpleArrayData::reallocate(Object *o, uint n,
    #      bool enforceAttributes)
    address = Rituals.call(
        'ritual_ZN3QV415SimpleArrayData10reallocateEPNS_6ObjectEjb',
        CuteMixin._addressOf(o), n, enforceAttributes,
    )
    return QV4.Heap.ArrayData._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.Heap.ArrayData'], int)
  @overload(NoneType, int)
  def get(d: Optional[QV4.Heap.ArrayData], index: int) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::SimpleArrayData::get(const Heap::ArrayData
    *d, uint index)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-simplearraydata.html#get

    Parameters
    ----------

    d : Optional[QV4.Heap.ArrayData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::SimpleArrayData::get(const Heap::ArrayData *d, uint
    #      index)
    return Rituals.call(
        'ritual_ZN3QV415SimpleArrayData3getEPKNS_4Heap9ArrayDataEj',
        CuteMixin._addressOf(d), index,
    )

  @staticmethod
  @overload(WAIT['QV4.Object'], int, QV4.Value)
  @overload(NoneType, int, QV4.Value)
  def put(o: Optional[QV4.Object], index: int, value: QV4.Value) -> bool:
    """
    Calls Qt's 'bool QV4::SimpleArrayData::put(Object *o, uint index, const
    Value &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-simplearraydata.html#put

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
    #  bool QV4::SimpleArrayData::put(Object *o, uint index, const Value
    #      &value)
    return Rituals.call(
        'ritual_ZN3QV415SimpleArrayData3putEPNS_6ObjectEjRKNS_5ValueE',
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
    Calls Qt's 'bool QV4::SimpleArrayData::putArray(Object *o, uint index,
    const Value *values, uint n)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-simplearraydata.html#putArray

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
    #  bool QV4::SimpleArrayData::putArray(Object *o, uint index, const Value
    #      *values, uint n)
    return Rituals.call(
        'ritual_ZN3QV415SimpleArrayData8putArrayEPNS_6ObjectEjPKNS_5ValueEj',
        CuteMixin._addressOf(o), index, CuteMixin._addressOf(values), n,
    )

  @staticmethod
  @overload(WAIT['QV4.Object'], int)
  @overload(NoneType, int)
  def del_(o: Optional[QV4.Object], index: int) -> bool:
    """
    Calls Qt's 'bool QV4::SimpleArrayData::del(Object *o, uint index)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-simplearraydata.html#del

    Parameters
    ----------

    o : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.
    """
    #  bool QV4::SimpleArrayData::del(Object *o, uint index)
    return Rituals.call(
        'ritual_ZN3QV415SimpleArrayData3delEPNS_6ObjectEj',
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
    Calls Qt's 'void QV4::SimpleArrayData::setAttribute(Object *o, uint
    index, PropertyAttributes attrs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-simplearraydata.html#setAttribute

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
    #  void QV4::SimpleArrayData::setAttribute(Object *o, uint index,
    #      PropertyAttributes attrs)
    Rituals.call(
        'ritual_ZN3QV415SimpleArrayData12setAttributeEPNS_6ObjectEjNS_18Pro'
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
    Calls Qt's 'void QV4::SimpleArrayData::push_front(Object *o, const Value
    *values, uint n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-simplearraydata.html#push_front

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
    #  void QV4::SimpleArrayData::push_front(Object *o, const Value *values,
    #      uint n)
    Rituals.call(
        'ritual_ZN3QV415SimpleArrayData10push_frontEPNS_6ObjectEPKNS_5Value'
        'Ej',
        CuteMixin._addressOf(o), CuteMixin._addressOf(values), n,
    )

  @staticmethod
  @overload(WAIT['QV4.Object'])
  @overload(NoneType)
  def pop_front(o: Optional[QV4.Object]) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::SimpleArrayData::pop_front(Object *o)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-simplearraydata.html#pop_front

    Parameters
    ----------

    o : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::SimpleArrayData::pop_front(Object *o)
    return Rituals.call(
        'ritual_ZN3QV415SimpleArrayData9pop_frontEPNS_6ObjectE',
        CuteMixin._addressOf(o),
    )

  @staticmethod
  @overload(WAIT['QV4.Object'], int)
  @overload(NoneType, int)
  def truncate(o: Optional[QV4.Object], newLen: int) -> int:
    """
    Calls Qt's 'uint QV4::SimpleArrayData::truncate(Object *o, uint newLen)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-simplearraydata.html#truncate

    Parameters
    ----------

    o : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newLen : int
      Passed on as it is.
    """
    #  uint QV4::SimpleArrayData::truncate(Object *o, uint newLen)
    return Rituals.call(
        'ritual_ZN3QV415SimpleArrayData8truncateEPNS_6ObjectEj',
        CuteMixin._addressOf(o), newLen,
    )

  @staticmethod
  @overload(WAIT['QV4.Heap.ArrayData'])
  @overload(NoneType)
  def length(d: Optional[QV4.Heap.ArrayData]) -> int:
    """
    Calls Qt's 'uint QV4::SimpleArrayData::length(const Heap::ArrayData *d)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-simplearraydata.html#length

    Parameters
    ----------

    d : Optional[QV4.Heap.ArrayData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  uint QV4::SimpleArrayData::length(const Heap::ArrayData *d)
    return Rituals.call(
        'ritual_ZN3QV415SimpleArrayData6lengthEPKNS_4Heap9ArrayDataE',
        CuteMixin._addressOf(d),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::SimpleArrayData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d(self) -> Optional[QV4.Heap.SimpleArrayData]:
    """
    Calls Qt's 'const Data *QV4::SimpleArrayData::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-simplearraydata.html#d

    Returns
    -------

    Optional[QV4.Heap.SimpleArrayData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Data *QV4::SimpleArrayData::d() const
    address = self.uglySide.call('ritual_ZNK3QV415SimpleArrayData1dEv')
    return QV4.Heap.SimpleArrayData._cuteAt(address)

  @overload(int)
  def mappedIndex(self, index: int) -> int:
    """
    Calls Qt's 'uint QV4::SimpleArrayData::mappedIndex(uint index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-simplearraydata.html#mappedIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  uint QV4::SimpleArrayData::mappedIndex(uint index) const
    return self.uglySide.call(
        'ritual_ZNK3QV415SimpleArrayData11mappedIndexEj', index,
    )

  @overload(int)
  def data(self, index: int) -> QV4.Value:
    """
    Calls Qt's 'Value QV4::SimpleArrayData::data(uint index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-simplearraydata.html#data

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QV4.Value
      A new cute QV4::Value around the copy Qt gave back. Python owns it.
    """
    #  Value QV4::SimpleArrayData::data(uint index) const
    address = self.uglySide.call(
        'ritual_ZNK3QV415SimpleArrayData4dataEj', index,
    )
    return QV4.Value._cuteOwning(address)

  def len(self) -> int:
    """
    Calls Qt's 'uint QV4::SimpleArrayData::len() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-simplearraydata.html#len
    """
    #  uint QV4::SimpleArrayData::len() const
    return self.uglySide.call('ritual_ZNK3QV415SimpleArrayData3lenEv')

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
    Calls Qt's 'void QV4::SimpleArrayData::__dataTest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-simplearraydata.html#__dataTest
    """
    #  void QV4::SimpleArrayData::__dataTest()
    self.uglySide.call('ritual_ZN3QV415SimpleArrayData10__dataTestEv')
