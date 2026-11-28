"""
QV4::ArrayData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4arraydata_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::ArrayData to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
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


class ArrayData(QV4.Managed):
  """
  The cute side of Qt's QV4::ArrayData: a plain Python object standing in
  front of one C++ QV4::ArrayData.

  It is built on the cute 'QV4::Managed', as Qt's QV4::ArrayData is built on
  Qt's QV4::Managed, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::ArrayData that has a ritual and that Python can
  call so far, 22 names in all: '__dataTest', 'd_unchecked', 'd', 'alloc',
  'setAlloc', 'setType', 'attrs', 'setAttrs', 'arrayData', 'setArrayData',
  'vtable', 'isSparse', 'length', 'hasAttributes', 'attributes', 'isEmpty',
  'get', 'ensureAttributes', 'realloc', 'sort', 'append', 'insert'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QV4::VTable *QV4::ArrayData::staticVTable()': gives
    'QV4::VTable', which has no cute class yet.
  - Qt's 'Type QV4::ArrayData::type() const': gives a type Python has no way
    to take yet.

  What has no ritual
  ------------------

  5 of the 29 functions Qt declares: 3 forbidden; 1 not a gap; 1 takes or
  gives a type that cannot be passed yet.

  What to expect
  --------------

  - The C++ QV4::ArrayData is created at the first use, not by
    'QV4::ArrayData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::ArrayData.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.Object'])
  @overload(NoneType)
  def ensureAttributes(o: Optional[QV4.Object]) -> None:
    """
    Calls Qt's 'void QV4::ArrayData::ensureAttributes(Object *o)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-arraydata.html#ensureAttributes

    Parameters
    ----------

    o : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::ArrayData::ensureAttributes(Object *o)
    Rituals.call(
        'ritual_ZN3QV49ArrayData16ensureAttributesEPNS_6ObjectE',
        CuteMixin._addressOf(o),
    )

  @staticmethod
  @overload(WAIT['QV4.Object'], QV4.Heap.ArrayData.Type, int, bool)
  @overload(NoneType, QV4.Heap.ArrayData.Type, int, bool)
  def realloc(
      o: Optional[QV4.Object],
      newType: QV4.Heap.ArrayData.Type,
      alloc: int,
      enforceAttributes: bool,
  ) -> None:
    """
    Calls Qt's 'void QV4::ArrayData::realloc(Object *o, Type newType, uint
    alloc, bool enforceAttributes)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-arraydata.html#realloc

    Parameters
    ----------

    o : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newType : QV4.Heap.ArrayData.Type
      Passed on as its number.

    alloc : int
      Passed on as it is.

    enforceAttributes : bool
      Passed on as it is.
    """
    #  void QV4::ArrayData::realloc(Object *o, Type newType, uint alloc, bool
    #      enforceAttributes)
    Rituals.call(
        'ritual_ZN3QV49ArrayData7reallocEPNS_6ObjectENS_4Heap9ArrayData4Typ'
        'eEjb',
        CuteMixin._addressOf(o), newType.value, alloc, enforceAttributes,
    )

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Object'], QV4.Value, int)
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, QV4.Value, int)
  @overload(NoneType, WAIT['QV4.Object'], QV4.Value, int)
  @overload(NoneType, NoneType, QV4.Value, int)
  def sort(
      engine: Optional[QV4.ExecutionEngine],
      thisObject: Optional[QV4.Object],
      comparefn: QV4.Value,
      dataLen: int,
  ) -> None:
    """
    Calls Qt's 'void QV4::ArrayData::sort(ExecutionEngine *engine, Object
    *thisObject, const Value &comparefn, uint dataLen)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-arraydata.html#sort

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    comparefn : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    dataLen : int
      Passed on as it is.
    """
    #  void QV4::ArrayData::sort(ExecutionEngine *engine, Object *thisObject,
    #      const Value &comparefn, uint dataLen)
    Rituals.call(
        'ritual_ZN3QV49ArrayData4sortEPNS_15ExecutionEngineEPNS_6ObjectERKN'
        'S_5ValueEj',
        CuteMixin._addressOf(engine), CuteMixin._addressOf(thisObject),
        CuteMixin._valueOf(comparefn), dataLen,
    )

  @staticmethod
  @overload(WAIT['QV4.Object'], WAIT['QV4.ArrayObject'], int)
  @overload(WAIT['QV4.Object'], NoneType, int)
  @overload(NoneType, WAIT['QV4.ArrayObject'], int)
  @overload(NoneType, NoneType, int)
  def append(
      obj: Optional[QV4.Object],
      otherObj: Optional[QV4.ArrayObject],
      n: int,
  ) -> int:
    """
    Calls Qt's 'uint QV4::ArrayData::append(Object *obj, ArrayObject
    *otherObj, uint n)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-arraydata.html#append

    Parameters
    ----------

    obj : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    otherObj : Optional[QV4.ArrayObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    n : int
      Passed on as it is.
    """
    #  uint QV4::ArrayData::append(Object *obj, ArrayObject *otherObj, uint
    #      n)
    return Rituals.call(
        'ritual_ZN3QV49ArrayData6appendEPNS_6ObjectEPNS_11ArrayObjectEj',
        CuteMixin._addressOf(obj), CuteMixin._addressOf(otherObj), n,
    )

  @staticmethod
  @overload(WAIT['QV4.Object'], int, QV4.Value)
  @overload(WAIT['QV4.Object'], int, NoneType)
  @overload(NoneType, int, QV4.Value)
  @overload(NoneType, int, NoneType)
  @overload(WAIT['QV4.Object'], int, QV4.Value, bool)
  @overload(WAIT['QV4.Object'], int, NoneType, bool)
  @overload(NoneType, int, QV4.Value, bool)
  @overload(NoneType, int, NoneType, bool)
  def insert(
      o: Optional[QV4.Object],
      index: int,
      v: Optional[QV4.Value],
      isAccessor: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QV4::ArrayData::insert(Object *o, uint index, const
    Value *v, bool isAccessor)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-arraydata.html#insert

    Parameters
    ----------

    o : Optional[QV4.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    v : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    isAccessor : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QV4::ArrayData::insert(Object *o, uint index, const Value *v,
    #      bool isAccessor)
    Rituals.call(
        'ritual_ZN3QV49ArrayData6insertEPNS_6ObjectEjPKNS_5ValueEb',
        CuteMixin._addressOf(o), index, CuteMixin._addressOf(v), isAccessor,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::ArrayData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.ArrayData]:
    """
    Calls Qt's 'QV4::Heap::ArrayData *QV4::ArrayData::d_unchecked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-arraydata.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.ArrayData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::ArrayData *QV4::ArrayData::d_unchecked() const
    address = self.uglySide.call('ritual_ZNK3QV49ArrayData11d_uncheckedEv')
    return QV4.Heap.ArrayData._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.ArrayData]:
    """
    Calls Qt's 'QV4::Heap::ArrayData *QV4::ArrayData::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-arraydata.html#d

    Returns
    -------

    Optional[QV4.Heap.ArrayData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::ArrayData *QV4::ArrayData::d() const
    address = self.uglySide.call('ritual_ZNK3QV49ArrayData1dEv')
    return QV4.Heap.ArrayData._cuteAt(address)

  def alloc(self) -> int:
    """
    Calls Qt's 'uint QV4::ArrayData::alloc() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-arraydata.html#alloc
    """
    #  uint QV4::ArrayData::alloc() const
    return self.uglySide.call('ritual_ZNK3QV49ArrayData5allocEv')

  def attrs(self) -> Optional[QV4.PropertyAttributes]:
    """
    Calls Qt's 'PropertyAttributes *QV4::ArrayData::attrs() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-arraydata.html#attrs

    Returns
    -------

    Optional[QV4.PropertyAttributes]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  PropertyAttributes *QV4::ArrayData::attrs() const
    address = self.uglySide.call('ritual_ZNK3QV49ArrayData5attrsEv')
    return QV4.PropertyAttributes._cuteAt(address)

  def arrayData(self) -> Optional[QV4.Value]:
    """
    Calls Qt's 'const Value *QV4::ArrayData::arrayData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-arraydata.html#arrayData

    Returns
    -------

    Optional[QV4.Value]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Value *QV4::ArrayData::arrayData() const
    address = self.uglySide.call('ritual_ZNK3QV49ArrayData9arrayDataEv')
    return QV4.Value._cuteAt(address)

  def vtable(self) -> Optional[QV4.ArrayVTable]:
    """
    Calls Qt's 'const ArrayVTable *QV4::ArrayData::vtable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-arraydata.html#vtable

    Returns
    -------

    Optional[QV4.ArrayVTable]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const ArrayVTable *QV4::ArrayData::vtable() const
    address = self.uglySide.call('ritual_ZNK3QV49ArrayData6vtableEv')
    return QV4.ArrayVTable._cuteAt(address)

  def isSparse(self) -> bool:
    """
    Calls Qt's 'bool QV4::ArrayData::isSparse() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-arraydata.html#isSparse
    """
    #  bool QV4::ArrayData::isSparse() const
    return self.uglySide.call('ritual_ZNK3QV49ArrayData8isSparseEv')

  def length(self) -> int:
    """
    Calls Qt's 'uint QV4::ArrayData::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-arraydata.html#length
    """
    #  uint QV4::ArrayData::length() const
    return self.uglySide.call('ritual_ZNK3QV49ArrayData6lengthEv')

  def hasAttributes(self) -> bool:
    """
    Calls Qt's 'bool QV4::ArrayData::hasAttributes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-arraydata.html#hasAttributes
    """
    #  bool QV4::ArrayData::hasAttributes() const
    return self.uglySide.call('ritual_ZNK3QV49ArrayData13hasAttributesEv')

  @overload(int)
  def attributes(self, i: int) -> QV4.PropertyAttributes:
    """
    Calls Qt's 'PropertyAttributes QV4::ArrayData::attributes(uint i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-arraydata.html#attributes

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    QV4.PropertyAttributes
      A new cute QV4::PropertyAttributes around the copy Qt gave back. Python
      owns it.
    """
    #  PropertyAttributes QV4::ArrayData::attributes(uint i) const
    address = self.uglySide.call('ritual_ZNK3QV49ArrayData10attributesEj', i)
    return QV4.PropertyAttributes._cuteOwning(address)

  @overload(int)
  def isEmpty(self, i: int) -> bool:
    """
    Calls Qt's 'bool QV4::ArrayData::isEmpty(uint i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-arraydata.html#isEmpty

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  bool QV4::ArrayData::isEmpty(uint i) const
    return self.uglySide.call('ritual_ZNK3QV49ArrayData7isEmptyEj', i)

  @overload(int)
  def get(self, i: int) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::ArrayData::get(uint i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-arraydata.html#get

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::ArrayData::get(uint i) const
    return self.uglySide.call('ritual_ZNK3QV49ArrayData3getEj', i)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setAlloc(self, a: int) -> None:
    """
    Calls Qt's 'void QV4::ArrayData::setAlloc(uint a)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-arraydata.html#setAlloc

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void QV4::ArrayData::setAlloc(uint a)
    self.uglySide.call('ritual_ZN3QV49ArrayData8setAllocEj', a)

  @overload(QV4.Heap.ArrayData.Type)
  def setType(self, t: QV4.Heap.ArrayData.Type) -> None:
    """
    Calls Qt's 'void QV4::ArrayData::setType(Type t)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-arraydata.html#setType

    Parameters
    ----------

    t : QV4.Heap.ArrayData.Type
      Passed on as its number.
    """
    #  void QV4::ArrayData::setType(Type t)
    self.uglySide.call(
        'ritual_ZN3QV49ArrayData7setTypeENS_4Heap9ArrayData4TypeE', t.value,
    )

  @overload(WAIT['QV4.PropertyAttributes'])
  @overload(NoneType)
  def setAttrs(self, a: Optional[QV4.PropertyAttributes]) -> None:
    """
    Calls Qt's 'void QV4::ArrayData::setAttrs(PropertyAttributes *a)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-arraydata.html#setAttrs

    Parameters
    ----------

    a : Optional[QV4.PropertyAttributes]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::ArrayData::setAttrs(PropertyAttributes *a)
    self.uglySide.call(
        'ritual_ZN3QV49ArrayData8setAttrsEPNS_18PropertyAttributesE',
        self._addressOf(a),
    )

  @overload(WAIT['QV4.EngineBase'], int, QV4.Value)
  @overload(NoneType, int, QV4.Value)
  def setArrayData(
      self,
      e: Optional[QV4.EngineBase],
      index: int,
      newVal: QV4.Value,
  ) -> None:
    """
    Calls Qt's 'void QV4::ArrayData::setArrayData(EngineBase *e, uint index,
    Value newVal)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-arraydata.html#setArrayData

    Parameters
    ----------

    e : Optional[QV4.EngineBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    newVal : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QV4::ArrayData::setArrayData(EngineBase *e, uint index, Value
    #      newVal)
    self.uglySide.call(
        'ritual_ZN3QV49ArrayData12setArrayDataEPNS_10EngineBaseEjNS_5ValueE',
        self._addressOf(e), index, self._valueOf(newVal),
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
    Calls Qt's 'void QV4::ArrayData::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-arraydata.html#__dataTest
    """
    #  void QV4::ArrayData::__dataTest()
    self.uglySide.call('ritual_ZN3QV49ArrayData10__dataTestEv')
