"""
QV4::Heap::ReferenceObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4referenceobject_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::Heap::ReferenceObject to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from . import QQmlEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlEngine = WAIT['QQmlEngine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ReferenceObject(QV4.Heap.Object, QV4.Heap.ReferenceObjectData):
  """
  The cute side of Qt's QV4::Heap::ReferenceObject: a plain Python object
  standing in front of one C++ QV4::Heap::ReferenceObject.

  It is built on the cute 'QV4::Heap::Object', as Qt's
  QV4::Heap::ReferenceObject is built on Qt's QV4::Heap::Object, and has
  everything that class has. It is built on the cute
  'QV4::Heap::ReferenceObjectData' as well, as Qt's
  QV4::Heap::ReferenceObject is built on Qt's QV4::Heap::ReferenceObjectData
  too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::ReferenceObject that has a ritual and
  that Python can call so far, 24 names in all: 'markObjects', 'init',
  'flags', 'object', 'setObject', 'property', 'canWriteBack', 'isVariant',
  'enforcesLocation', 'setLocation', 'function', 'statementIndex',
  'isAttachedToProperty', 'isReference', 'isDirty', 'setDirty',
  'isAlwaysDirty', 'setAlwaysDirty', 'isConnected', 'destroy',
  'connectToNotifySignal', 'connectToBindable', 'hasFlag', 'setFlag'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What to expect
  --------------

  - The C++ QV4::Heap::ReferenceObject is created at the first use, not by
    'QV4::Heap::ReferenceObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::ReferenceObject.
  """

  #  The enums Qt writes inside QV4::Heap::ReferenceObject, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Flag(CuteFlags, number='unsigned char'):
    """
    The flags enum 'QV4::Heap::ReferenceObject::Flag' of Qt, with the 6 names
    Qt gives in it. Qt names the type of its combinations
    'QV4::Heap::ReferenceObject::Flags'.
    """

    NoFlag = 0x0
    CanWriteBack = 0x1
    IsVariant = 0x2
    EnforcesLocation = 0x4
    IsDirty = 0x8
    IsAlwaysDirty = 0x10

  Flags = Flag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QV4.Heap.Base, WAIT['QV4.MarkStack'])
  @overload(QV4.Heap.Base, NoneType)
  @overload(NoneType, WAIT['QV4.MarkStack'])
  @overload(NoneType, NoneType)
  def markObjects(
      b: Optional[QV4.Heap.Base],
      stack: Optional[QV4.MarkStack],
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::ReferenceObject::markObjects(Heap::Base *b,
    MarkStack *stack)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-referenceobject.html#markObjects

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::ReferenceObject::markObjects(Heap::Base *b, MarkStack
    #      *stack)
    Rituals.call(
        'ritual_ZN3QV44Heap15ReferenceObject11markObjectsEPNS0_4BaseEPNS_9M'
        'arkStackE',
        CuteMixin._addressOf(b), CuteMixin._addressOf(stack),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::ReferenceObject'

  #  Qt's QV4::Heap::ReferenceObject is built on more than one class. The
  #  part of a C++ QV4::Heap::ReferenceObject that belongs to a class after
  #  the first begins somewhere inside the object, and the ritual named for
  #  that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QV4::Heap::ReferenceObjectData':
          'ritual_cast_QV4_Heap_ReferenceObject_QV4_Heap_ReferenceObjectData',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def flags(self) -> Flags:
    """
    Calls Qt's 'Flags QV4::Heap::ReferenceObject::flags() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-referenceobject.html#flags

    Returns
    -------

    Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QV4::Heap::ReferenceObject::flags() const
    return ReferenceObject.Flags(self.uglySide.call(
        'ritual_ZNK3QV44Heap15ReferenceObject5flagsEv',
    ))

  def object(self) -> Optional[QV4.Heap.Object]:
    """
    Calls Qt's 'Object *QV4::Heap::ReferenceObject::object() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-referenceobject.html#object

    Returns
    -------

    Optional[QV4.Heap.Object]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Object *QV4::Heap::ReferenceObject::object() const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap15ReferenceObject6objectEv',
    )
    return QV4.Heap.Object._cuteAt(address)

  def property(self) -> int:
    """
    Calls Qt's 'int QV4::Heap::ReferenceObject::property() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-referenceobject.html#property
    """
    #  int QV4::Heap::ReferenceObject::property() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap15ReferenceObject8propertyEv',
    )

  def canWriteBack(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::ReferenceObject::canWriteBack() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-referenceobject.html#canWriteBack
    """
    #  bool QV4::Heap::ReferenceObject::canWriteBack() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap15ReferenceObject12canWriteBackEv',
    )

  def isVariant(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::ReferenceObject::isVariant() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-referenceobject.html#isVariant
    """
    #  bool QV4::Heap::ReferenceObject::isVariant() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap15ReferenceObject9isVariantEv',
    )

  def enforcesLocation(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::ReferenceObject::enforcesLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-referenceobject.html#enforcesLocation
    """
    #  bool QV4::Heap::ReferenceObject::enforcesLocation() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap15ReferenceObject16enforcesLocationEv',
    )

  def function(self) -> Optional[QV4.Function]:
    """
    Calls Qt's 'const Function *QV4::Heap::ReferenceObject::function()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-referenceobject.html#function

    Returns
    -------

    Optional[QV4.Function]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Function *QV4::Heap::ReferenceObject::function() const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap15ReferenceObject8functionEv',
    )
    return QV4.Function._cuteAt(address)

  def statementIndex(self) -> int:
    """
    Calls Qt's 'quint16 QV4::Heap::ReferenceObject::statementIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-referenceobject.html#statementIndex
    """
    #  quint16 QV4::Heap::ReferenceObject::statementIndex() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap15ReferenceObject14statementIndexEv',
    )

  def isAttachedToProperty(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::ReferenceObject::isAttachedToProperty()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-referenceobject.html#isAttachedToProperty
    """
    #  bool QV4::Heap::ReferenceObject::isAttachedToProperty() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap15ReferenceObject20isAttachedToPropertyEv',
    )

  def isReference(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::ReferenceObject::isReference() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-referenceobject.html#isReference
    """
    #  bool QV4::Heap::ReferenceObject::isReference() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap15ReferenceObject11isReferenceEv',
    )

  def isDirty(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::ReferenceObject::isDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-referenceobject.html#isDirty
    """
    #  bool QV4::Heap::ReferenceObject::isDirty() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap15ReferenceObject7isDirtyEv',
    )

  def isAlwaysDirty(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::ReferenceObject::isAlwaysDirty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-referenceobject.html#isAlwaysDirty
    """
    #  bool QV4::Heap::ReferenceObject::isAlwaysDirty() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap15ReferenceObject13isAlwaysDirtyEv',
    )

  @overload(Flag)
  def hasFlag(self, flag: Flag) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::ReferenceObject::hasFlag(Flag flag) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-referenceobject.html#hasFlag

    Parameters
    ----------

    flag : Flag
      Passed on as its number.
    """
    #  bool QV4::Heap::ReferenceObject::hasFlag(Flag flag) const
    return self.uglySide.call(
        'ritual_ZNK3QV44Heap15ReferenceObject7hasFlagENS1_4FlagE',
        flag.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QV4.Heap.Object)
  @overload(NoneType)
  def setObject(self, object: Optional[QV4.Heap.Object]) -> None:
    """
    Calls Qt's 'void QV4::Heap::ReferenceObject::setObject(Object *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-referenceobject.html#setObject

    Parameters
    ----------

    object : Optional[QV4.Heap.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::ReferenceObject::setObject(Object *object)
    self.uglySide.call(
        'ritual_ZN3QV44Heap15ReferenceObject9setObjectEPNS0_6ObjectE',
        self._addressOf(object),
    )

  @overload(WAIT['QV4.Function'], int)
  @overload(NoneType, int)
  def setLocation(
      self,
      function: Optional[QV4.Function],
      statement: int,
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::ReferenceObject::setLocation(const Function
    *function, quint16 statement)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-referenceobject.html#setLocation

    Parameters
    ----------

    function : Optional[QV4.Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    statement : int
      Passed on as it is.
    """
    #  void QV4::Heap::ReferenceObject::setLocation(const Function *function,
    #      quint16 statement)
    self.uglySide.call(
        'ritual_ZN3QV44Heap15ReferenceObject11setLocationEPKNS_8FunctionEt',
        self._addressOf(function), statement,
    )

  @overload(bool)
  def setDirty(self, dirty: bool) -> None:
    """
    Calls Qt's 'void QV4::Heap::ReferenceObject::setDirty(bool dirty)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-referenceobject.html#setDirty

    Parameters
    ----------

    dirty : bool
      Passed on as it is.
    """
    #  void QV4::Heap::ReferenceObject::setDirty(bool dirty)
    self.uglySide.call(
        'ritual_ZN3QV44Heap15ReferenceObject8setDirtyEb', dirty,
    )

  @overload(bool)
  def setAlwaysDirty(self, alwaysDirty: bool) -> None:
    """
    Calls Qt's 'void QV4::Heap::ReferenceObject::setAlwaysDirty(bool
    alwaysDirty)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-referenceobject.html#setAlwaysDirty

    Parameters
    ----------

    alwaysDirty : bool
      Passed on as it is.
    """
    #  void QV4::Heap::ReferenceObject::setAlwaysDirty(bool alwaysDirty)
    self.uglySide.call(
        'ritual_ZN3QV44Heap15ReferenceObject14setAlwaysDirtyEb', alwaysDirty,
    )

  @overload(Flag, bool)
  def setFlag(self, flag: Flag, set: bool) -> None:
    """
    Calls Qt's 'void QV4::Heap::ReferenceObject::setFlag(Flag flag, bool
    set)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-referenceobject.html#setFlag

    Parameters
    ----------

    flag : Flag
      Passed on as its number.

    set : bool
      Passed on as it is.
    """
    #  void QV4::Heap::ReferenceObject::setFlag(Flag flag, bool set)
    self.uglySide.call(
        'ritual_ZN3QV44Heap15ReferenceObject7setFlagENS1_4FlagEb',
        flag.value, set,
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

  @overload(QV4.Heap.Object, int, Flags)
  @overload(NoneType, int, Flags)
  def init(
      self,
      object: Optional[QV4.Heap.Object],
      property: int,
      flags: Flags,
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::ReferenceObject::init(Object *object, int
    property, Flags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-heap-referenceobject.html#init

    Parameters
    ----------

    object : Optional[QV4.Heap.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    property : int
      Passed on as it is.

    flags : Flags
      Passed on as its number.
    """
    #  void QV4::Heap::ReferenceObject::init(Object *object, int property,
    #      Flags flags)
    self.uglySide.call(
        'ritual_ZN3QV44Heap15ReferenceObject4initEPNS0_6ObjectEi6QFlagsINS1'
        '_4FlagEE',
        self._addressOf(object), property, flags.value,
    )

  def isConnected(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::ReferenceObject::isConnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-referenceobject.html#isConnected
    """
    #  bool QV4::Heap::ReferenceObject::isConnected()
    return self.uglySide.call(
        'ritual_ZN3QV44Heap15ReferenceObject11isConnectedEv',
    )

  def destroy(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::ReferenceObject::destroy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-referenceobject.html#destroy
    """
    #  void QV4::Heap::ReferenceObject::destroy()
    self.uglySide.call('ritual_ZN3QV44Heap15ReferenceObject7destroyEv')

  @overload(QObject, int, QQmlEngine)
  @overload(QObject, int, NoneType)
  @overload(NoneType, int, QQmlEngine)
  @overload(NoneType, int, NoneType)
  def connectToNotifySignal(
      self,
      obj: Optional[QObject],
      property: int,
      engine: Optional[QQmlEngine],
  ) -> None:
    """
    Calls Qt's 'void
    QV4::Heap::ReferenceObject::connectToNotifySignal(QObject *obj, int
    property, QQmlEngine *engine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-referenceobject.html

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    property : int
      Passed on as it is.

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::ReferenceObject::connectToNotifySignal(QObject *obj,
    #      int property, QQmlEngine *engine)
    self.uglySide.call(
        'ritual_ZN3QV44Heap15ReferenceObject21connectToNotifySignalEP7QObje'
        'ctiP10QQmlEngine',
        self._addressOf(obj, 'QObject'), property, self._addressOf(engine),
    )

  @overload(QObject, int, QQmlEngine)
  @overload(QObject, int, NoneType)
  @overload(NoneType, int, QQmlEngine)
  @overload(NoneType, int, NoneType)
  def connectToBindable(
      self,
      obj: Optional[QObject],
      property: int,
      engine: Optional[QQmlEngine],
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::ReferenceObject::connectToBindable(QObject
    *obj, int property, QQmlEngine *engine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-referenceobject.html#connectToBindable

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    property : int
      Passed on as it is.

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::ReferenceObject::connectToBindable(QObject *obj, int
    #      property, QQmlEngine *engine)
    self.uglySide.call(
        'ritual_ZN3QV44Heap15ReferenceObject17connectToBindableEP7QObjectiP'
        '10QQmlEngine',
        self._addressOf(obj, 'QObject'), property, self._addressOf(engine),
    )
