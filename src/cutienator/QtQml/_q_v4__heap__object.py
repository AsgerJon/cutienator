"""
QV4::Heap::Object binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4object_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QV4::Heap::Object to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
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


class Object(QV4.Heap.Base, QV4.Heap.ObjectData):
  """
  The cute side of Qt's QV4::Heap::Object: a plain Python object standing in
  front of one C++ QV4::Heap::Object.

  It is built on the cute 'QV4::Heap::Base', as Qt's QV4::Heap::Object is
  built on Qt's QV4::Heap::Base, and has everything that class has. It is
  built on the cute 'QV4::Heap::ObjectData' as well, as Qt's
  QV4::Heap::Object is built on Qt's QV4::Heap::ObjectData too, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::Object that has a ritual and that Python
  can call so far, 10 names in all: 'markObjects', 'init',
  'inlinePropertyDataWithOffset', 'inlinePropertyData',
  'setInlinePropertyWithOffset', 'writablePropertyData', 'propertyData',
  'setProperty', 'setUsedAsProto', 'prototype'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const VTable *QV4::Heap::Object::vtable() const': gives
    'QV4::VTable', which has no cute class yet.

  What to expect
  --------------

  - The C++ QV4::Heap::Object is created at the first use, not by
    'QV4::Heap::Object(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::Object.
  - Each name of Qt's QV4::Heap::Object that has no cute function yet,
    'vtable', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

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
    Calls Qt's 'void QV4::Heap::Object::markObjects(Heap::Base *base,
    MarkStack *stack)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-object.html#markObjects

    Parameters
    ----------

    base : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::Object::markObjects(Heap::Base *base, MarkStack
    #      *stack)
    Rituals.call(
        'ritual_ZN3QV44Heap6Object11markObjectsEPNS0_4BaseEPNS_9MarkStackE',
        CuteMixin._addressOf(base), CuteMixin._addressOf(stack),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::Object'

  #  Qt's QV4::Heap::Object is built on more than one class. The part of a
  #  C++ QV4::Heap::Object that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QV4::Heap::ObjectData':
          'ritual_cast_QV4_Heap_Object_QV4_Heap_ObjectData',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def inlinePropertyDataWithOffset(
      self,
      indexWithOffset: int,
  ) -> Optional[QV4.Value]:
    """
    Calls Qt's 'const Value
    *QV4::Heap::Object::inlinePropertyDataWithOffset(uint indexWithOffset)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-object.html#inlinePropertyDataWithOffset

    Parameters
    ----------

    indexWithOffset : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Value]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Value *QV4::Heap::Object::inlinePropertyDataWithOffset(uint
    #      indexWithOffset) const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap6Object28inlinePropertyDataWithOffsetEj',
        indexWithOffset,
    )
    return QV4.Value._cuteAt(address)

  @overload(int)
  def inlinePropertyData(self, index: int) -> Optional[QV4.Value]:
    """
    Calls Qt's 'const Value *QV4::Heap::Object::inlinePropertyData(uint
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-object.html#inlinePropertyData

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Value]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Value *QV4::Heap::Object::inlinePropertyData(uint index) const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap6Object18inlinePropertyDataEj', index,
    )
    return QV4.Value._cuteAt(address)

  @overload(int)
  def propertyData(self, index: int) -> Optional[QV4.Value]:
    """
    Calls Qt's 'const Value *QV4::Heap::Object::propertyData(uint index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-object.html#propertyData

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Value]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Value *QV4::Heap::Object::propertyData(uint index) const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap6Object12propertyDataEj', index,
    )
    return QV4.Value._cuteAt(address)

  def prototype(self) -> Optional[Object]:
    """
    Calls Qt's 'Heap::Object *QV4::Heap::Object::prototype() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-object.html#prototype

    Returns
    -------

    Optional[Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::Object *QV4::Heap::Object::prototype() const
    address = self.uglySide.call('ritual_ZNK3QV44Heap6Object9prototypeEv')
    return Object._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QV4.ExecutionEngine'], int, WAIT['QV4.Value'])
  @overload(NoneType, int, WAIT['QV4.Value'])
  def setInlinePropertyWithOffset(
      self,
      e: Optional[QV4.ExecutionEngine],
      indexWithOffset: int,
      v: QV4.Value,
  ) -> None:
    """
    Calls Qt's 'void
    QV4::Heap::Object::setInlinePropertyWithOffset(ExecutionEngine *e, uint
    indexWithOffset, Value v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-object.html#setInlinePropertyWithOffset

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    indexWithOffset : int
      Passed on as it is.

    v : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QV4::Heap::Object::setInlinePropertyWithOffset(ExecutionEngine
    #      *e, uint indexWithOffset, Value v)
    self.uglySide.call(
        'ritual_ZN3QV44Heap6Object27setInlinePropertyWithOffsetEPNS_15Execu'
        'tionEngineEjNS_5ValueE',
        self._addressOf(e), indexWithOffset, self._valueOf(v),
    )

  @overload(WAIT['QV4.ExecutionEngine'], int, QV4.Heap.Base)
  @overload(WAIT['QV4.ExecutionEngine'], int, NoneType)
  @overload(NoneType, int, QV4.Heap.Base)
  @overload(NoneType, int, NoneType)
  def setInlinePropertyWithOffset(
      self,
      e: Optional[QV4.ExecutionEngine],
      indexWithOffset: int,
      b: Optional[QV4.Heap.Base],
  ) -> None:
    """
    Calls Qt's 'void
    QV4::Heap::Object::setInlinePropertyWithOffset(ExecutionEngine *e, uint
    indexWithOffset, Heap::Base *b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-object.html#setInlinePropertyWithOffset

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    indexWithOffset : int
      Passed on as it is.

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::Object::setInlinePropertyWithOffset(ExecutionEngine
    #      *e, uint indexWithOffset, Heap::Base *b)
    self.uglySide.call(
        'ritual_ZN3QV44Heap6Object27setInlinePropertyWithOffsetEPNS_15Execu'
        'tionEngineEjPNS0_4BaseE',
        self._addressOf(e), indexWithOffset, self._addressOf(b),
    )

  @overload(WAIT['QV4.ExecutionEngine'], int, WAIT['QV4.Value'])
  @overload(NoneType, int, WAIT['QV4.Value'])
  def setProperty(
      self,
      e: Optional[QV4.ExecutionEngine],
      index: int,
      v: QV4.Value,
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::Object::setProperty(ExecutionEngine *e, uint
    index, Value v)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-object.html#setProperty

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    v : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QV4::Heap::Object::setProperty(ExecutionEngine *e, uint index,
    #      Value v)
    self.uglySide.call(
        'ritual_ZN3QV44Heap6Object11setPropertyEPNS_15ExecutionEngineEjNS_5'
        'ValueE',
        self._addressOf(e), index, self._valueOf(v),
    )

  @overload(WAIT['QV4.ExecutionEngine'], int, QV4.Heap.Base)
  @overload(WAIT['QV4.ExecutionEngine'], int, NoneType)
  @overload(NoneType, int, QV4.Heap.Base)
  @overload(NoneType, int, NoneType)
  def setProperty(
      self,
      e: Optional[QV4.ExecutionEngine],
      index: int,
      b: Optional[QV4.Heap.Base],
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::Object::setProperty(ExecutionEngine *e, uint
    index, Heap::Base *b)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-object.html#setProperty

    Parameters
    ----------

    e : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::Object::setProperty(ExecutionEngine *e, uint index,
    #      Heap::Base *b)
    self.uglySide.call(
        'ritual_ZN3QV44Heap6Object11setPropertyEPNS_15ExecutionEngineEjPNS0'
        '_4BaseE',
        self._addressOf(e), index, self._addressOf(b),
    )

  def setUsedAsProto(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::Object::setUsedAsProto()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-object.html#setUsedAsProto
    """
    #  void QV4::Heap::Object::setUsedAsProto()
    self.uglySide.call('ritual_ZN3QV44Heap6Object14setUsedAsProtoEv')

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

  def init(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::Object::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-object.html#init
    """
    #  void QV4::Heap::Object::init()
    self.uglySide.call('ritual_ZN3QV44Heap6Object4initEv')

  @overload(int)
  def writablePropertyData(self, index: int) -> QV4.PropertyIndex:
    """
    Calls Qt's 'PropertyIndex QV4::Heap::Object::writablePropertyData(uint
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-object.html#writablePropertyData

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QV4.PropertyIndex
      A new cute QV4::PropertyIndex around the copy Qt gave back. Python owns
      it.
    """
    #  PropertyIndex QV4::Heap::Object::writablePropertyData(uint index)
    address = self.uglySide.call(
        'ritual_ZN3QV44Heap6Object20writablePropertyDataEj', index,
    )
    return QV4.PropertyIndex._cuteOwning(address)

  @staticmethod
  def vtable(*__, **_) -> Never:
    """
    Qt's 'const VTable *QV4::Heap::Object::vtable() const': gives
    'QV4::VTable', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Heap.Object.vtable' has no cute function yet. Qt's 'const "
        "VTable *QV4::Heap::Object::vtable() const': gives 'QV4::VTable', "
        "which has no cute class yet.")
