"""
QV4::TypedArray binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4typedarray_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::TypedArray to be private: it declares the class in a header
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


class TypedArray(QV4.Object):
  """
  The cute side of Qt's QV4::TypedArray: a plain Python object standing in
  front of one C++ QV4::TypedArray.

  It is built on the cute 'QV4::Object', as Qt's QV4::TypedArray is built on
  Qt's QV4::Object, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::TypedArray that has a ritual and that Python
  can call so far, 15 names in all: '__dataTest', 'd_unchecked', 'd',
  'create', 'byteOffset', 'byteLength', 'bytesPerElement', 'length',
  'constArrayData', 'hasDetachedArrayData', 'arrayDataLength',
  'virtualHasProperty', 'virtualGetOwnProperty', 'virtualPut',
  'virtualDefineOwnProperty'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QV4::VTable *QV4::TypedArray::staticVTable()': gives
    'QV4::VTable', which has no cute class yet.
  - Qt's 'char *QV4::TypedArray::arrayData()': gives 'char', which has no
    cute class yet.
  - Qt's 'Heap::TypedArray::Type QV4::TypedArray::arrayType() const': gives a
    type Python has no way to take yet.
  - Qt's 'ReturnedValue QV4::TypedArray::virtualGet(const Managed *m,
    PropertyKey id, const Value *receiver, bool *hasProperty)': takes a
    number to change where it is.
  - Qt's 'OwnPropertyKeyIterator
    *QV4::TypedArray::virtualOwnPropertyKeys(const Object *m, Value
    *target)': gives 'QV4::OwnPropertyKeyIterator', which has no cute class
    yet.

  What has no ritual
  ------------------

  4 of the 24 functions Qt declares: 3 forbidden; 1 not a gap.

  What to expect
  --------------

  - The C++ QV4::TypedArray is created at the first use, not by
    'QV4::TypedArray(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::TypedArray.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], QV4.TypedArrayType)
  @overload(NoneType, QV4.TypedArrayType)
  def create(
      e: Optional[QV4.ExecutionEngine],
      t: QV4.TypedArrayType,
  ) -> Optional[QV4.Heap.TypedArray]:
    """
    Calls Qt's 'Heap::TypedArray
    *QV4::TypedArray::create(QV4::ExecutionEngine *e, Heap::TypedArray::Type
    t)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-typedarray.html#create

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    t : QV4.TypedArrayType
      Passed on as its number.

    Returns
    -------

    Optional[QV4.Heap.TypedArray]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::TypedArray *QV4::TypedArray::create(QV4::ExecutionEngine *e,
    #      Heap::TypedArray::Type t)
    address = Rituals.call(
        'ritual_ZN3QV410TypedArray6createEPNS_15ExecutionEngineENS_14TypedA'
        'rrayTypeE',
        CuteMixin._addressOf(e), t.value,
    )
    return QV4.Heap.TypedArray._cuteAt(address)

  @staticmethod
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'])
  @overload(NoneType, WAIT['QV4.PropertyKey'])
  def virtualHasProperty(
      m: Optional[QV4.Managed],
      id: QV4.PropertyKey,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::TypedArray::virtualHasProperty(const Managed *m,
    PropertyKey id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-typedarray.html#virtualHasProperty

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.
    """
    #  bool QV4::TypedArray::virtualHasProperty(const Managed *m, PropertyKey
    #      id)
    return Rituals.call(
        'ritual_ZN3QV410TypedArray18virtualHasPropertyEPKNS_7ManagedENS_11P'
        'ropertyKeyE',
        CuteMixin._addressOf(m), CuteMixin._valueOf(id),
    )

  @staticmethod
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'], WAIT['QV4.Property'])
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'], NoneType)
  @overload(NoneType, WAIT['QV4.PropertyKey'], WAIT['QV4.Property'])
  @overload(NoneType, WAIT['QV4.PropertyKey'], NoneType)
  def virtualGetOwnProperty(
      m: Optional[QV4.Managed],
      id: QV4.PropertyKey,
      p: Optional[QV4.Property],
  ) -> QV4.PropertyAttributes:
    """
    Calls Qt's 'PropertyAttributes
    QV4::TypedArray::virtualGetOwnProperty(const Managed *m, PropertyKey id,
    Property *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-typedarray.html#virtualGetOwnProperty

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    p : Optional[QV4.Property]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QV4.PropertyAttributes
      A new cute QV4::PropertyAttributes around the copy Qt gave back. Python
      owns it.
    """
    #  PropertyAttributes QV4::TypedArray::virtualGetOwnProperty(const
    #      Managed *m, PropertyKey id, Property *p)
    address = Rituals.call(
        'ritual_ZN3QV410TypedArray21virtualGetOwnPropertyEPKNS_7ManagedENS_'
        '11PropertyKeyEPNS_8PropertyE',
        CuteMixin._addressOf(m), CuteMixin._valueOf(id),
        CuteMixin._addressOf(p),
    )
    return QV4.PropertyAttributes._cuteOwning(address)

  @staticmethod
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'], QV4.Value, QV4.Value)
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'], QV4.Value, NoneType)
  @overload(NoneType, WAIT['QV4.PropertyKey'], QV4.Value, QV4.Value)
  @overload(NoneType, WAIT['QV4.PropertyKey'], QV4.Value, NoneType)
  def virtualPut(
      m: Optional[QV4.Managed],
      id: QV4.PropertyKey,
      value: QV4.Value,
      receiver: Optional[QV4.Value],
  ) -> bool:
    """
    Calls Qt's 'bool QV4::TypedArray::virtualPut(Managed *m, PropertyKey id,
    const Value &value, Value *receiver)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-typedarray.html#virtualPut

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    receiver : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::TypedArray::virtualPut(Managed *m, PropertyKey id, const
    #      Value &value, Value *receiver)
    return Rituals.call(
        'ritual_ZN3QV410TypedArray10virtualPutEPNS_7ManagedENS_11PropertyKe'
        'yERKNS_5ValueEPS4_',
        CuteMixin._addressOf(m), CuteMixin._valueOf(id),
        CuteMixin._valueOf(value), CuteMixin._addressOf(receiver),
    )

  @staticmethod
  @overload(
      QV4.Managed, WAIT['QV4.PropertyKey'], WAIT['QV4.Property'],
      WAIT['QV4.PropertyAttributes'],
  )
  @overload(
      QV4.Managed, WAIT['QV4.PropertyKey'], NoneType,
      WAIT['QV4.PropertyAttributes'],
  )
  @overload(
      NoneType, WAIT['QV4.PropertyKey'], WAIT['QV4.Property'],
      WAIT['QV4.PropertyAttributes'],
  )
  @overload(
      NoneType, WAIT['QV4.PropertyKey'], NoneType,
      WAIT['QV4.PropertyAttributes'],
  )
  def virtualDefineOwnProperty(
      m: Optional[QV4.Managed],
      id: QV4.PropertyKey,
      p: Optional[QV4.Property],
      attrs: QV4.PropertyAttributes,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::TypedArray::virtualDefineOwnProperty(Managed *m,
    PropertyKey id, const Property *p, PropertyAttributes attrs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-typedarray.html#virtualDefineOwnProperty

    Parameters
    ----------

    m : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.

    p : Optional[QV4.Property]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    attrs : QV4.PropertyAttributes
      Passed on as a value: Qt reads the C++ QV4::PropertyAttributes, which
      stays Python's own.
    """
    #  bool QV4::TypedArray::virtualDefineOwnProperty(Managed *m, PropertyKey
    #      id, const Property *p, PropertyAttributes attrs)
    return Rituals.call(
        'ritual_ZN3QV410TypedArray24virtualDefineOwnPropertyEPNS_7ManagedEN'
        'S_11PropertyKeyEPKNS_8PropertyENS_18PropertyAttributesE',
        CuteMixin._addressOf(m), CuteMixin._valueOf(id),
        CuteMixin._addressOf(p), CuteMixin._valueOf(attrs),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::TypedArray'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.TypedArray]:
    """
    Calls Qt's 'QV4::Heap::TypedArray *QV4::TypedArray::d_unchecked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-typedarray.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.TypedArray]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::TypedArray *QV4::TypedArray::d_unchecked() const
    address = self.uglySide.call('ritual_ZNK3QV410TypedArray11d_uncheckedEv')
    return QV4.Heap.TypedArray._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.TypedArray]:
    """
    Calls Qt's 'QV4::Heap::TypedArray *QV4::TypedArray::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-typedarray.html#d

    Returns
    -------

    Optional[QV4.Heap.TypedArray]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::TypedArray *QV4::TypedArray::d() const
    address = self.uglySide.call('ritual_ZNK3QV410TypedArray1dEv')
    return QV4.Heap.TypedArray._cuteAt(address)

  def byteOffset(self) -> int:
    """
    Calls Qt's 'uint QV4::TypedArray::byteOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-typedarray.html#byteOffset
    """
    #  uint QV4::TypedArray::byteOffset() const
    return self.uglySide.call('ritual_ZNK3QV410TypedArray10byteOffsetEv')

  def byteLength(self) -> int:
    """
    Calls Qt's 'uint QV4::TypedArray::byteLength() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-typedarray.html#byteLength
    """
    #  uint QV4::TypedArray::byteLength() const
    return self.uglySide.call('ritual_ZNK3QV410TypedArray10byteLengthEv')

  def bytesPerElement(self) -> int:
    """
    Calls Qt's 'int QV4::TypedArray::bytesPerElement() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-typedarray.html#bytesPerElement
    """
    #  int QV4::TypedArray::bytesPerElement() const
    return self.uglySide.call(
        'ritual_ZNK3QV410TypedArray15bytesPerElementEv',
    )

  def length(self) -> int:
    """
    Calls Qt's 'uint QV4::TypedArray::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-typedarray.html#length
    """
    #  uint QV4::TypedArray::length() const
    return self.uglySide.call('ritual_ZNK3QV410TypedArray6lengthEv')

  def constArrayData(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QV4::TypedArray::constArrayData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-typedarray.html#constArrayData

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QV4::TypedArray::constArrayData() const
    chars = self.uglySide.call(
        'ritual_ZNK3QV410TypedArray14constArrayDataEv',
    )
    return None if chars is None else chars.decode()

  def hasDetachedArrayData(self) -> bool:
    """
    Calls Qt's 'bool QV4::TypedArray::hasDetachedArrayData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-typedarray.html#hasDetachedArrayData
    """
    #  bool QV4::TypedArray::hasDetachedArrayData() const
    return self.uglySide.call(
        'ritual_ZNK3QV410TypedArray20hasDetachedArrayDataEv',
    )

  def arrayDataLength(self) -> int:
    """
    Calls Qt's 'uint QV4::TypedArray::arrayDataLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-typedarray.html#arrayDataLength
    """
    #  uint QV4::TypedArray::arrayDataLength() const
    return self.uglySide.call(
        'ritual_ZNK3QV410TypedArray15arrayDataLengthEv',
    )

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
    Calls Qt's 'void QV4::TypedArray::__dataTest()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-typedarray.html#__dataTest
    """
    #  void QV4::TypedArray::__dataTest()
    self.uglySide.call('ritual_ZN3QV410TypedArray10__dataTestEv')
