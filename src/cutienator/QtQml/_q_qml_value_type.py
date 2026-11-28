"""
QQmlValueType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlvaluetype_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlValueType to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QDynamicMetaObjectData, QMetaObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaType, QObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaType = WAIT['QMetaType']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlValueType(QDynamicMetaObjectData):
  """
  The cute side of Qt's QQmlValueType: a plain Python object standing in
  front of one C++ QQmlValueType.

  It is built on the cute 'QDynamicMetaObjectData', as Qt's QQmlValueType is
  built on Qt's QDynamicMetaObjectData, and has everything that class has.

  C++ hands a QQmlValueType around as a copy, so every C++ QQmlValueType
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlValueType that has a ritual and that Python can
  call so far, 4 names in all: 'metaType', 'staticMetaObject',
  'toDynamicMetaObject', 'objectDestroyed'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlValueType::~QQmlValueType()': the destructor: Python removes
    its C++ QQmlValueType by it, and has no other use for it.
  - Qt's 'void *QQmlValueType::create() const': gives 'void', which has no
    cute class yet.
  - Qt's 'void QQmlValueType::destroy(void *gadgetPtr) const': names 'void',
    which has no cute class yet.
  - Qt's 'void QQmlValueType::construct(void *gadgetPtr, const void *copy)
    const': names 'void', which has no cute class yet.
  - Qt's 'void QQmlValueType::destruct(void *gadgetPtr) const': names 'void',
    which has no cute class yet.
  - Qt's 'int QQmlValueType::metaCall(QObject *obj, QMetaObject::Call type,
    int _id, void **argv)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QQmlValueType is created at the first use, not by
    'QQmlValueType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlValueType back gives a copy the ritual made for
    Python, in a new cute QQmlValueType.
  - Each name of Qt's QQmlValueType that has no cute function yet,
    'construct', 'create', 'destroy', 'destruct', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlValueType'

  #  A C++ QQmlValueType Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlValueType'

  #  Qt's '~QQmlValueType()'. Naming it makes this a value class: Python owns
  #  every C++ QQmlValueType behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QQmlValueTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QQmlValueType::metaType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvaluetype.html#metaType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QQmlValueType::metaType() const
    address = self.uglySide.call('ritual_ZNK13QQmlValueType8metaTypeEv')
    from ..QtCore import QMetaType
    return QMetaType._cuteOwning(address)

  def staticMetaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlValueType::staticMetaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvaluetype.html#staticMetaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlValueType::staticMetaObject() const
    address = self.uglySide.call(
        'ritual_ZNK13QQmlValueType16staticMetaObjectEv',
    )
    return QMetaObject._cuteAt(address)

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
    Notes what was given, for Qt's 'QQmlValueType::QQmlValueType()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvaluetype.html#QQmlValueType
    """
    #  QQmlValueType::QQmlValueType()
    self._noteCreation(QQmlValueType, lambda: Rituals.call(
        'ritual_ZN13QQmlValueTypeC1Ev',
    ))

  @overload(QMetaType, QMetaObject)
  @overload(QMetaType, NoneType)
  def __init__(
      self,
      type: QMetaType,
      staticMetaObject: Optional[QMetaObject],
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlValueType::QQmlValueType(QMetaType
    type, const QMetaObject *staticMetaObject)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvaluetype.html#QQmlValueType

    Parameters
    ----------

    type : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    staticMetaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlValueType::QQmlValueType(QMetaType type, const QMetaObject
    #      *staticMetaObject)
    self._noteCreation(QQmlValueType, lambda: Rituals.call(
        'ritual_ZN13QQmlValueTypeC1E9QMetaTypePK11QMetaObject',
        self._valueOf(type), self._addressOf(staticMetaObject,
        'QMetaObject'),
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

  @overload(QObject)
  @overload(NoneType)
  def toDynamicMetaObject(
      self,
      a0: Optional[QObject],
  ) -> Optional[QMetaObject]:
    """
    Calls Qt's 'QMetaObject *QQmlValueType::toDynamicMetaObject(QObject
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlvaluetype.html#toDynamicMetaObject

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMetaObject *QQmlValueType::toDynamicMetaObject(QObject *a0)
    ritual = 'ritual_ZN13QQmlValueType19toDynamicMetaObjectEP7QObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQmlValueType19toDynamicMetaObjectEP7QObject'
    address = self.uglySide.call(ritual, self._addressOf(a0, 'QObject'))
    return QMetaObject._cuteAt(address)

  @overload(QObject)
  @overload(NoneType)
  def objectDestroyed(self, a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlValueType::objectDestroyed(QObject *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlvaluetype.html#objectDestroyed

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlValueType::objectDestroyed(QObject *a0)
    ritual = 'ritual_ZN13QQmlValueType15objectDestroyedEP7QObject'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQmlValueType15objectDestroyedEP7QObject'
    self.uglySide.call(ritual, self._addressOf(a0, 'QObject'))

  @staticmethod
  def construct(*__, **_) -> Never:
    """
    Qt's 'void QQmlValueType::construct(void *gadgetPtr, const void *copy)
    const': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlValueType.construct' has no cute function yet. Qt's 'void "
        "QQmlValueType::construct(void *gadgetPtr, const void *copy) "
        "const': names 'void', which has no cute class yet.")

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'void *QQmlValueType::create() const': gives 'void', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QQmlValueType.create' has no cute function yet. Qt's 'void "
        "*QQmlValueType::create() const': gives 'void', which has no cute "
        "class yet.")

  @staticmethod
  def destroy(*__, **_) -> Never:
    """
    Qt's 'void QQmlValueType::destroy(void *gadgetPtr) const': names 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlValueType.destroy' has no cute function yet. Qt's 'void "
        "QQmlValueType::destroy(void *gadgetPtr) const': names 'void', "
        "which has no cute class yet.")

  @staticmethod
  def destruct(*__, **_) -> Never:
    """
    Qt's 'void QQmlValueType::destruct(void *gadgetPtr) const': names 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlValueType.destruct' has no cute function yet. Qt's 'void "
        "QQmlValueType::destruct(void *gadgetPtr) const': names 'void', "
        "which has no cute class yet.")
