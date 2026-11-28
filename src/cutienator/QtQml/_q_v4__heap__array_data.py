"""
QV4::Heap::ArrayData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4arraydata_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::Heap::ArrayData to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ArrayData(QV4.Heap.Base, QV4.Heap.ArrayDataData):
  """
  The cute side of Qt's QV4::Heap::ArrayData: a plain Python object standing
  in front of one C++ QV4::Heap::ArrayData.

  It is built on the cute 'QV4::Heap::Base', as Qt's QV4::Heap::ArrayData is
  built on Qt's QV4::Heap::Base, and has everything that class has. It is
  built on the cute 'QV4::Heap::ArrayDataData' as well, as Qt's
  QV4::Heap::ArrayData is built on Qt's QV4::Heap::ArrayDataData too, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::ArrayData that has a ritual and that
  Python can call so far, 12 names in all: 'markObjects', 'isSparse',
  'vtable', 'get', 'getProperty', 'setProperty', 'getValueOrSetter',
  'attributes', 'isEmpty', 'length', 'setArrayData', 'mappedIndex'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What to expect
  --------------

  - The C++ QV4::Heap::ArrayData is created at the first use, not by
    'QV4::Heap::ArrayData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::ArrayData.
  """

  #  The enums Qt writes inside QV4::Heap::ArrayData, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum):
    """
    The enum 'QV4::Heap::ArrayData::Type' of Qt, with the 3 names Qt gives in
    it.
    """

    Simple = Kee[int](0)
    Sparse = Kee[int](1)
    Custom = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QV4.Heap.Base, WAIT['QV4.MarkStack'])
  @overload(QV4.Heap.Base, NoneType)
  @overload(NoneType, WAIT['QV4.MarkStack'])
  @overload(NoneType, NoneType)
  def markObjects(
      base: Optional[QV4.Heap.Base],
      stack: Optional[QV4.MarkStack],
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::ArrayData::markObjects(Heap::Base *base,
    MarkStack *stack)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-arraydata.html#markObjects

    Parameters
    ----------

    base : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::ArrayData::markObjects(Heap::Base *base, MarkStack
    #      *stack)
    Rituals.call(
        'ritual_ZN3QV44Heap9ArrayData11markObjectsEPNS0_4BaseEPNS_9MarkStac'
        'kE',
        CuteMixin._addressOf(base), CuteMixin._addressOf(stack),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::ArrayData'

  #  Qt's QV4::Heap::ArrayData is built on more than one class. The part of a
  #  C++ QV4::Heap::ArrayData that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QV4::Heap::ArrayDataData':
          'ritual_cast_QV4_Heap_ArrayData_QV4_Heap_ArrayDataData',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isSparse(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::ArrayData::isSparse() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-arraydata.html#isSparse
    """
    #  bool QV4::Heap::ArrayData::isSparse() const
    return self.uglySide.call('ritual_ZNK3QV44Heap9ArrayData8isSparseEv')

  def vtable(self) -> Optional[QV4.ArrayVTable]:
    """
    Calls Qt's 'const ArrayVTable *QV4::Heap::ArrayData::vtable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-arraydata.html#vtable

    Returns
    -------

    Optional[QV4.ArrayVTable]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const ArrayVTable *QV4::Heap::ArrayData::vtable() const
    address = self.uglySide.call('ritual_ZNK3QV44Heap9ArrayData6vtableEv')
    return QV4.ArrayVTable._cuteAt(address)

  @overload(int)
  def get(self, i: int) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Heap::ArrayData::get(uint i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-arraydata.html#get

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  ReturnedValue QV4::Heap::ArrayData::get(uint i) const
    return self.uglySide.call('ritual_ZNK3QV44Heap9ArrayData3getEj', i)

  @overload(int)
  def attributes(self, i: int) -> QV4.PropertyAttributes:
    """
    Calls Qt's 'PropertyAttributes QV4::Heap::ArrayData::attributes(uint i)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-arraydata.html#attributes

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
    #  PropertyAttributes QV4::Heap::ArrayData::attributes(uint i) const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap9ArrayData10attributesEj', i,
    )
    return QV4.PropertyAttributes._cuteOwning(address)

  @overload(int)
  def isEmpty(self, i: int) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::ArrayData::isEmpty(uint i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-arraydata.html#isEmpty

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  bool QV4::Heap::ArrayData::isEmpty(uint i) const
    return self.uglySide.call('ritual_ZNK3QV44Heap9ArrayData7isEmptyEj', i)

  def length(self) -> int:
    """
    Calls Qt's 'uint QV4::Heap::ArrayData::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-arraydata.html#length
    """
    #  uint QV4::Heap::ArrayData::length() const
    return self.uglySide.call('ritual_ZNK3QV44Heap9ArrayData6lengthEv')

  @overload(int)
  def mappedIndex(self, index: int) -> int:
    """
    Calls Qt's 'uint QV4::Heap::ArrayData::mappedIndex(uint index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-arraydata.html#mappedIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  uint QV4::Heap::ArrayData::mappedIndex(uint index) const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap9ArrayData11mappedIndexEj', index,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QV4.EngineBase'], int, WAIT['QV4.Property'])
  @overload(WAIT['QV4.EngineBase'], int, NoneType)
  @overload(NoneType, int, WAIT['QV4.Property'])
  @overload(NoneType, int, NoneType)
  def setProperty(
      self,
      e: Optional[QV4.EngineBase],
      index: int,
      p: Optional[QV4.Property],
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::ArrayData::setProperty(EngineBase *e, uint
    index, const Property *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-arraydata.html#setProperty

    Parameters
    ----------

    e : Optional[QV4.EngineBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    p : Optional[QV4.Property]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::ArrayData::setProperty(EngineBase *e, uint index,
    #      const Property *p)
    self.uglySide.call(
        'ritual_ZN3QV44Heap9ArrayData11setPropertyEPNS_10EngineBaseEjPKNS_8'
        'PropertyE',
        self._addressOf(e), index, self._addressOf(p),
    )

  @overload(WAIT['QV4.EngineBase'], int, WAIT['QV4.Value'])
  @overload(NoneType, int, WAIT['QV4.Value'])
  def setArrayData(
      self,
      e: Optional[QV4.EngineBase],
      index: int,
      newVal: QV4.Value,
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::ArrayData::setArrayData(EngineBase *e, uint
    index, Value newVal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-arraydata.html#setArrayData

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
    #  void QV4::Heap::ArrayData::setArrayData(EngineBase *e, uint index,
    #      Value newVal)
    self.uglySide.call(
        'ritual_ZN3QV44Heap9ArrayData12setArrayDataEPNS_10EngineBaseEjNS_5V'
        'alueE',
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

  @overload(int, WAIT['QV4.Property'], WAIT['QV4.PropertyAttributes'])
  @overload(int, WAIT['QV4.Property'], NoneType)
  @overload(int, NoneType, WAIT['QV4.PropertyAttributes'])
  @overload(int, NoneType, NoneType)
  def getProperty(
      self,
      index: int,
      p: Optional[QV4.Property],
      attrs: Optional[QV4.PropertyAttributes],
  ) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::ArrayData::getProperty(uint index, Property
    *p, PropertyAttributes *attrs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-arraydata.html#getProperty

    Parameters
    ----------

    index : int
      Passed on as it is.

    p : Optional[QV4.Property]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    attrs : Optional[QV4.PropertyAttributes]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::Heap::ArrayData::getProperty(uint index, Property *p,
    #      PropertyAttributes *attrs)
    return self.uglySide.call(
        'ritual_ZN3QV44Heap9ArrayData11getPropertyEjPNS_8PropertyEPNS_18Pro'
        'pertyAttributesE',
        index, self._addressOf(p), self._addressOf(attrs),
    )

  @overload(int, WAIT['QV4.PropertyAttributes'])
  @overload(int, NoneType)
  def getValueOrSetter(
      self,
      index: int,
      attrs: Optional[QV4.PropertyAttributes],
  ) -> QV4.PropertyIndex:
    """
    Calls Qt's 'PropertyIndex QV4::Heap::ArrayData::getValueOrSetter(uint
    index, PropertyAttributes *attrs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-arraydata.html#getValueOrSetter

    Parameters
    ----------

    index : int
      Passed on as it is.

    attrs : Optional[QV4.PropertyAttributes]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QV4.PropertyIndex
      A new cute QV4::PropertyIndex around the copy Qt gave back. Python owns
      it.
    """
    #  PropertyIndex QV4::Heap::ArrayData::getValueOrSetter(uint index,
    #      PropertyAttributes *attrs)
    address = self.uglySide.call(
        'ritual_ZN3QV44Heap9ArrayData16getValueOrSetterEjPNS_18PropertyAttr'
        'ibutesE',
        index, self._addressOf(attrs),
    )
    return QV4.PropertyIndex._cuteOwning(address)
