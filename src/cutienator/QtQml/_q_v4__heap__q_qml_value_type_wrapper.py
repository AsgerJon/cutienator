"""
QV4::Heap::QQmlValueTypeWrapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlvaluetypewrapper_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QV4::Heap::QQmlValueTypeWrapper to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QMetaType, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObject = WAIT['QMetaObject']
  QMetaType = WAIT['QMetaType']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlValueTypeWrapper(QV4.Heap.ReferenceObject, QV4.Heap.QQmlValueTypeWrapperData):
  """
  The cute side of Qt's QV4::Heap::QQmlValueTypeWrapper: a plain Python
  object standing in front of one C++ QV4::Heap::QQmlValueTypeWrapper.

  It is built on the cute 'QV4::Heap::ReferenceObject', as Qt's
  QV4::Heap::QQmlValueTypeWrapper is built on Qt's
  QV4::Heap::ReferenceObject, and has everything that class has. It is built
  on the cute 'QV4::Heap::QQmlValueTypeWrapperData' as well, as Qt's
  QV4::Heap::QQmlValueTypeWrapper is built on Qt's
  QV4::Heap::QQmlValueTypeWrapperData too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Heap::QQmlValueTypeWrapper that has a ritual
  and that Python can call so far, 11 names in all: 'markObjects',
  'detached', 'destroy', 'metaType', 'metaObject', 'toVariant', 'setVariant',
  'readReference', 'writeBack', 'setMetaObject', 'setMetaType'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QV4::Heap::QQmlValueTypeWrapper::init(const void *data,
    QMetaType metaType, const QMetaObject *metaObject, Object *object, int
    property, Flags flags)': names 'void', which has no cute class yet.
  - Qt's 'void QV4::Heap::QQmlValueTypeWrapper::setGadgetPtr(void
    *gadgetPtr)': names 'void', which has no cute class yet.
  - Qt's 'void *QV4::Heap::QQmlValueTypeWrapper::gadgetPtr() const': gives
    'void', which has no cute class yet.
  - Qt's 'void QV4::Heap::QQmlValueTypeWrapper::setData(const void *data)':
    names 'void', which has no cute class yet.
  - Qt's 'void *QV4::Heap::QQmlValueTypeWrapper::storagePointer()': gives
    'void', which has no cute class yet.

  What to expect
  --------------

  - The C++ QV4::Heap::QQmlValueTypeWrapper is created at the first use, not
    by 'QV4::Heap::QQmlValueTypeWrapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Heap::QQmlValueTypeWrapper.
  - Each name of Qt's QV4::Heap::QQmlValueTypeWrapper that has no cute
    function yet, 'gadgetPtr', 'setData', 'setGadgetPtr', 'storagePointer',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
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
      b: Optional[QV4.Heap.Base],
      stack: Optional[QV4.MarkStack],
  ) -> None:
    """
    Calls Qt's 'void QV4::Heap::QQmlValueTypeWrapper::markObjects(Heap::Base
    *b, MarkStack *stack)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qqmlvaluetypewrapper.html#markObjects

    Parameters
    ----------

    b : Optional[QV4.Heap.Base]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::QQmlValueTypeWrapper::markObjects(Heap::Base *b,
    #      MarkStack *stack)
    Rituals.call(
        'ritual_ZN3QV44Heap20QQmlValueTypeWrapper11markObjectsEPNS0_4BaseEP'
        'NS_9MarkStackE',
        CuteMixin._addressOf(b), CuteMixin._addressOf(stack),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Heap::QQmlValueTypeWrapper'

  #  Qt's QV4::Heap::QQmlValueTypeWrapper is built on more than one class.
  #  The part of a C++ QV4::Heap::QQmlValueTypeWrapper that belongs to a
  #  class after the first begins somewhere inside the object, and the ritual
  #  named for that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QV4::Heap::QQmlValueTypeWrapperData':
          'ritual_cast_QV4_Heap_QQmlValueTypeWrapper_QV4_Heap_QQmlValueTypeWrapperData',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def detached(self) -> Optional[QQmlValueTypeWrapper]:
    """
    Calls Qt's 'QQmlValueTypeWrapper
    *QV4::Heap::QQmlValueTypeWrapper::detached() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qqmlvaluetypewrapper.html#detached

    Returns
    -------

    Optional[QQmlValueTypeWrapper]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlValueTypeWrapper *QV4::Heap::QQmlValueTypeWrapper::detached()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap20QQmlValueTypeWrapper8detachedEv',
    )
    return QQmlValueTypeWrapper._cuteAt(address)

  def metaType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QV4::Heap::QQmlValueTypeWrapper::metaType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qqmlvaluetypewrapper.html#metaType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QV4::Heap::QQmlValueTypeWrapper::metaType() const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap20QQmlValueTypeWrapper8metaTypeEv',
    )
    from ..QtCore import QMetaType
    return QMetaType._cuteOwning(address)

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QV4::Heap::QQmlValueTypeWrapper::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qqmlvaluetypewrapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QV4::Heap::QQmlValueTypeWrapper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap20QQmlValueTypeWrapper10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def toVariant(self) -> QVariant:
    """
    Calls Qt's 'QVariant QV4::Heap::QQmlValueTypeWrapper::toVariant() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qqmlvaluetypewrapper.html#toVariant

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QV4::Heap::QQmlValueTypeWrapper::toVariant() const
    address = self.uglySide.call(
        'ritual_ZNK3QV44Heap20QQmlValueTypeWrapper9toVariantEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setVariant(self, variant: QVariant) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::QQmlValueTypeWrapper::setVariant(const
    QVariant &variant)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qqmlvaluetypewrapper.html#setVariant

    Parameters
    ----------

    variant : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QV4::Heap::QQmlValueTypeWrapper::setVariant(const QVariant
    #      &variant)
    return self.uglySide.call(
        'ritual_ZN3QV44Heap20QQmlValueTypeWrapper10setVariantERK8QVariant',
        self._valueOf(variant),
    )

  @overload(QMetaObject)
  @overload(NoneType)
  def setMetaObject(self, metaObject: Optional[QMetaObject]) -> None:
    """
    Calls Qt's 'void QV4::Heap::QQmlValueTypeWrapper::setMetaObject(const
    QMetaObject *metaObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qqmlvaluetypewrapper.html#setMetaObject

    Parameters
    ----------

    metaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Heap::QQmlValueTypeWrapper::setMetaObject(const QMetaObject
    #      *metaObject)
    self.uglySide.call(
        'ritual_ZN3QV44Heap20QQmlValueTypeWrapper13setMetaObjectEPK11QMetaO'
        'bject',
        self._addressOf(metaObject, 'QMetaObject'),
    )

  @overload(QMetaType)
  def setMetaType(self, metaType: QMetaType) -> None:
    """
    Calls Qt's 'void QV4::Heap::QQmlValueTypeWrapper::setMetaType(QMetaType
    metaType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qqmlvaluetypewrapper.html#setMetaType

    Parameters
    ----------

    metaType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  void QV4::Heap::QQmlValueTypeWrapper::setMetaType(QMetaType metaType)
    self.uglySide.call(
        'ritual_ZN3QV44Heap20QQmlValueTypeWrapper11setMetaTypeE9QMetaType',
        self._valueOf(metaType),
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

  def destroy(self) -> None:
    """
    Calls Qt's 'void QV4::Heap::QQmlValueTypeWrapper::destroy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qqmlvaluetypewrapper.html#destroy
    """
    #  void QV4::Heap::QQmlValueTypeWrapper::destroy()
    self.uglySide.call('ritual_ZN3QV44Heap20QQmlValueTypeWrapper7destroyEv')

  def readReference(self) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::QQmlValueTypeWrapper::readReference()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qqmlvaluetypewrapper.html#readReference
    """
    #  bool QV4::Heap::QQmlValueTypeWrapper::readReference()
    return self.uglySide.call(
        'ritual_ZN3QV44Heap20QQmlValueTypeWrapper13readReferenceEv',
    )

  @overload()
  @overload(int)
  def writeBack(self, propertyIndex: int = -1) -> bool:
    """
    Calls Qt's 'bool QV4::Heap::QQmlValueTypeWrapper::writeBack(int
    propertyIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-heap-qqmlvaluetypewrapper.html#writeBack

    Parameters
    ----------

    propertyIndex : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  bool QV4::Heap::QQmlValueTypeWrapper::writeBack(int propertyIndex)
    return self.uglySide.call(
        'ritual_ZN3QV44Heap20QQmlValueTypeWrapper9writeBackEi',
        propertyIndex,
    )

  @staticmethod
  def gadgetPtr(*__, **_) -> Never:
    """
    Qt's 'void *QV4::Heap::QQmlValueTypeWrapper::gadgetPtr() const': gives
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Heap.QQmlValueTypeWrapper.gadgetPtr' has no cute function "
        "yet. Qt's 'void *QV4::Heap::QQmlValueTypeWrapper::gadgetPtr() "
        "const': gives 'void', which has no cute class yet.")

  @staticmethod
  def setData(*__, **_) -> Never:
    """
    Qt's 'void QV4::Heap::QQmlValueTypeWrapper::setData(const void *data)':
    names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Heap.QQmlValueTypeWrapper.setData' has no cute function yet. "
        "Qt's 'void QV4::Heap::QQmlValueTypeWrapper::setData(const void "
        "*data)': names 'void', which has no cute class yet.")

  @staticmethod
  def setGadgetPtr(*__, **_) -> Never:
    """
    Qt's 'void QV4::Heap::QQmlValueTypeWrapper::setGadgetPtr(void
    *gadgetPtr)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Heap.QQmlValueTypeWrapper.setGadgetPtr' has no cute function "
        "yet. Qt's 'void QV4::Heap::QQmlValueTypeWrapper::setGadgetPtr(void "
        "*gadgetPtr)': names 'void', which has no cute class yet.")

  @staticmethod
  def storagePointer(*__, **_) -> Never:
    """
    Qt's 'void *QV4::Heap::QQmlValueTypeWrapper::storagePointer()': gives
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Heap.QQmlValueTypeWrapper.storagePointer' has no cute "
        "function yet. Qt's 'void "
        "*QV4::Heap::QQmlValueTypeWrapper::storagePointer()': gives 'void', "
        "which has no cute class yet.")
