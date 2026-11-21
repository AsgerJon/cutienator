"""
QMetaProperty binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qmetaobject.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QVariantType

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QMetaEnum, QMetaMethod, QMetaObject, QMetaType, QObject
  from . import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMetaProperty(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMetaProperty: a plain Python object standing in
  front of one C++ QMetaProperty.

  C++ hands a QMetaProperty around as a copy, so every C++ QMetaProperty
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMetaProperty that has a ritual and that Python can
  call so far, 35 names in all: 'name', 'typeName', 'type', 'userType',
  'typeId', 'metaType', 'propertyIndex', 'relativePropertyIndex',
  'isReadable', 'isWritable', 'isResettable', 'isDesignable', 'isScriptable',
  'isStored', 'isUser', 'isConstant', 'isFinal', 'isVirtual', 'isOverride',
  'isRequired', 'isBindable', 'isFlagType', 'isEnumType', 'enumerator',
  'hasNotifySignal', 'notifySignal', 'notifySignalIndex', 'revision', 'read',
  'write', 'reset', 'hasStdCppSet', 'isAlias', 'isValid',
  'enclosingMetaObject'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QUntypedBindable QMetaProperty::bindable(QObject *object) const':
    gives 'QUntypedBindable', which has no cute class yet.
  - Qt's 'QMetaProperty::~QMetaProperty()': the destructor: Python removes
    its C++ QMetaProperty by it, and has no other use for it.

  What has no ritual
  ------------------

  8 of the 46 functions Qt declares: 5 takes or gives a type that cannot be
  passed yet; 3 private.

  What to expect
  --------------

  - The C++ QMetaProperty is created at the first use, not by
    'QMetaProperty(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMetaProperty back gives a copy the ritual made for
    Python, in a new cute QMetaProperty.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMetaProperty'

  #  Qt's '~QMetaProperty()'. Naming it makes this a value class: Python owns
  #  every C++ QMetaProperty behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QMetaPropertyD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QMetaProperty::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#name

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QMetaProperty::name() const
    chars = self.uglySide.call('ritual_ZNK13QMetaProperty4nameEv')
    return None if chars is None else chars.decode()

  def typeName(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QMetaProperty::typeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#typeName

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QMetaProperty::typeName() const
    chars = self.uglySide.call('ritual_ZNK13QMetaProperty8typeNameEv')
    return None if chars is None else chars.decode()

  def type(self) -> QVariant.Type:
    """
    Calls Qt's 'QVariant::Type QMetaProperty::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#type

    Returns
    -------

    QVariant.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QVariant.Type(number)'
      gives.
    """
    #  QVariant::Type QMetaProperty::type() const
    return QVariantType(self.uglySide.call(
        'ritual_ZNK13QMetaProperty4typeEv',
    ))

  def userType(self) -> int:
    """
    Calls Qt's 'int QMetaProperty::userType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#userType
    """
    #  int QMetaProperty::userType() const
    return self.uglySide.call('ritual_ZNK13QMetaProperty8userTypeEv')

  def typeId(self) -> int:
    """
    Calls Qt's 'int QMetaProperty::typeId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#typeId
    """
    #  int QMetaProperty::typeId() const
    return self.uglySide.call('ritual_ZNK13QMetaProperty6typeIdEv')

  def metaType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QMetaProperty::metaType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#metaType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QMetaProperty::metaType() const
    address = self.uglySide.call('ritual_ZNK13QMetaProperty8metaTypeEv')
    from . import QMetaType
    return QMetaType._cuteOwning(address)

  def propertyIndex(self) -> int:
    """
    Calls Qt's 'int QMetaProperty::propertyIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#propertyIndex
    """
    #  int QMetaProperty::propertyIndex() const
    return self.uglySide.call('ritual_ZNK13QMetaProperty13propertyIndexEv')

  def relativePropertyIndex(self) -> int:
    """
    Calls Qt's 'int QMetaProperty::relativePropertyIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaproperty.html#relativePropertyIndex
    """
    #  int QMetaProperty::relativePropertyIndex() const
    return self.uglySide.call(
        'ritual_ZNK13QMetaProperty21relativePropertyIndexEv',
    )

  def isReadable(self) -> bool:
    """
    Calls Qt's 'bool QMetaProperty::isReadable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#isReadable
    """
    #  bool QMetaProperty::isReadable() const
    return self.uglySide.call('ritual_ZNK13QMetaProperty10isReadableEv')

  def isWritable(self) -> bool:
    """
    Calls Qt's 'bool QMetaProperty::isWritable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#isWritable
    """
    #  bool QMetaProperty::isWritable() const
    return self.uglySide.call('ritual_ZNK13QMetaProperty10isWritableEv')

  def isResettable(self) -> bool:
    """
    Calls Qt's 'bool QMetaProperty::isResettable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#isResettable
    """
    #  bool QMetaProperty::isResettable() const
    return self.uglySide.call('ritual_ZNK13QMetaProperty12isResettableEv')

  def isDesignable(self) -> bool:
    """
    Calls Qt's 'bool QMetaProperty::isDesignable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#isDesignable
    """
    #  bool QMetaProperty::isDesignable() const
    return self.uglySide.call('ritual_ZNK13QMetaProperty12isDesignableEv')

  def isScriptable(self) -> bool:
    """
    Calls Qt's 'bool QMetaProperty::isScriptable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#isScriptable
    """
    #  bool QMetaProperty::isScriptable() const
    return self.uglySide.call('ritual_ZNK13QMetaProperty12isScriptableEv')

  def isStored(self) -> bool:
    """
    Calls Qt's 'bool QMetaProperty::isStored() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#isStored
    """
    #  bool QMetaProperty::isStored() const
    return self.uglySide.call('ritual_ZNK13QMetaProperty8isStoredEv')

  def isUser(self) -> bool:
    """
    Calls Qt's 'bool QMetaProperty::isUser() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#isUser
    """
    #  bool QMetaProperty::isUser() const
    return self.uglySide.call('ritual_ZNK13QMetaProperty6isUserEv')

  def isConstant(self) -> bool:
    """
    Calls Qt's 'bool QMetaProperty::isConstant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#isConstant
    """
    #  bool QMetaProperty::isConstant() const
    return self.uglySide.call('ritual_ZNK13QMetaProperty10isConstantEv')

  def isFinal(self) -> bool:
    """
    Calls Qt's 'bool QMetaProperty::isFinal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#isFinal
    """
    #  bool QMetaProperty::isFinal() const
    return self.uglySide.call('ritual_ZNK13QMetaProperty7isFinalEv')

  def isVirtual(self) -> bool:
    """
    Calls Qt's 'bool QMetaProperty::isVirtual() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#isVirtual
    """
    #  bool QMetaProperty::isVirtual() const
    return self.uglySide.call('ritual_ZNK13QMetaProperty9isVirtualEv')

  def isOverride(self) -> bool:
    """
    Calls Qt's 'bool QMetaProperty::isOverride() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#isOverride
    """
    #  bool QMetaProperty::isOverride() const
    return self.uglySide.call('ritual_ZNK13QMetaProperty10isOverrideEv')

  def isRequired(self) -> bool:
    """
    Calls Qt's 'bool QMetaProperty::isRequired() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#isRequired
    """
    #  bool QMetaProperty::isRequired() const
    return self.uglySide.call('ritual_ZNK13QMetaProperty10isRequiredEv')

  def isBindable(self) -> bool:
    """
    Calls Qt's 'bool QMetaProperty::isBindable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#isBindable
    """
    #  bool QMetaProperty::isBindable() const
    return self.uglySide.call('ritual_ZNK13QMetaProperty10isBindableEv')

  def isFlagType(self) -> bool:
    """
    Calls Qt's 'bool QMetaProperty::isFlagType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#isFlagType
    """
    #  bool QMetaProperty::isFlagType() const
    return self.uglySide.call('ritual_ZNK13QMetaProperty10isFlagTypeEv')

  def isEnumType(self) -> bool:
    """
    Calls Qt's 'bool QMetaProperty::isEnumType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#isEnumType
    """
    #  bool QMetaProperty::isEnumType() const
    return self.uglySide.call('ritual_ZNK13QMetaProperty10isEnumTypeEv')

  def enumerator(self) -> QMetaEnum:
    """
    Calls Qt's 'QMetaEnum QMetaProperty::enumerator() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#enumerator

    Returns
    -------

    QMetaEnum
      A new cute QMetaEnum around the copy Qt gave back. Python owns it.
    """
    #  QMetaEnum QMetaProperty::enumerator() const
    address = self.uglySide.call('ritual_ZNK13QMetaProperty10enumeratorEv')
    from . import QMetaEnum
    return QMetaEnum._cuteOwning(address)

  def hasNotifySignal(self) -> bool:
    """
    Calls Qt's 'bool QMetaProperty::hasNotifySignal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#hasNotifySignal
    """
    #  bool QMetaProperty::hasNotifySignal() const
    return self.uglySide.call('ritual_ZNK13QMetaProperty15hasNotifySignalEv')

  def notifySignal(self) -> QMetaMethod:
    """
    Calls Qt's 'QMetaMethod QMetaProperty::notifySignal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#notifySignal

    Returns
    -------

    QMetaMethod
      A new cute QMetaMethod around the copy Qt gave back. Python owns it.
    """
    #  QMetaMethod QMetaProperty::notifySignal() const
    address = self.uglySide.call('ritual_ZNK13QMetaProperty12notifySignalEv')
    from . import QMetaMethod
    return QMetaMethod._cuteOwning(address)

  def notifySignalIndex(self) -> int:
    """
    Calls Qt's 'int QMetaProperty::notifySignalIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaproperty.html#notifySignalIndex
    """
    #  int QMetaProperty::notifySignalIndex() const
    return self.uglySide.call(
        'ritual_ZNK13QMetaProperty17notifySignalIndexEv',
    )

  def revision(self) -> int:
    """
    Calls Qt's 'int QMetaProperty::revision() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#revision
    """
    #  int QMetaProperty::revision() const
    return self.uglySide.call('ritual_ZNK13QMetaProperty8revisionEv')

  @overload(QObject)
  @overload(NoneType)
  def read(self, obj: Optional[QObject]) -> QVariant:
    """
    Calls Qt's 'QVariant QMetaProperty::read(const QObject *obj) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#read

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QMetaProperty::read(const QObject *obj) const
    address = self.uglySide.call(
        'ritual_ZNK13QMetaProperty4readEPK7QObject', self._addressOf(obj),
    )
    from . import QVariant
    return QVariant._cuteOwning(address)

  @overload(QObject, QVariant)
  @overload(NoneType, QVariant)
  def write(self, obj: Optional[QObject], value: QVariant) -> bool:
    """
    Calls Qt's 'bool QMetaProperty::write(QObject *obj, const QVariant
    &value) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#write

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QMetaProperty::write(QObject *obj, const QVariant &value) const
    return self.uglySide.call(
        'ritual_ZNK13QMetaProperty5writeEP7QObjectRK8QVariant',
        self._addressOf(obj), self._valueOf(value),
    )

  @overload(QObject)
  @overload(NoneType)
  def reset(self, obj: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool QMetaProperty::reset(QObject *obj) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#reset

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMetaProperty::reset(QObject *obj) const
    return self.uglySide.call(
        'ritual_ZNK13QMetaProperty5resetEP7QObject', self._addressOf(obj),
    )

  def hasStdCppSet(self) -> bool:
    """
    Calls Qt's 'bool QMetaProperty::hasStdCppSet() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#hasStdCppSet
    """
    #  bool QMetaProperty::hasStdCppSet() const
    return self.uglySide.call('ritual_ZNK13QMetaProperty12hasStdCppSetEv')

  def isAlias(self) -> bool:
    """
    Calls Qt's 'bool QMetaProperty::isAlias() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#isAlias
    """
    #  bool QMetaProperty::isAlias() const
    return self.uglySide.call('ritual_ZNK13QMetaProperty7isAliasEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QMetaProperty::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#isValid
    """
    #  bool QMetaProperty::isValid() const
    return self.uglySide.call('ritual_ZNK13QMetaProperty7isValidEv')

  def enclosingMetaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QMetaProperty::enclosingMetaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmetaproperty.html#enclosingMetaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMetaProperty::enclosingMetaObject() const
    address = self.uglySide.call(
        'ritual_ZNK13QMetaProperty19enclosingMetaObjectEv',
    )
    from . import QMetaObject
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
    Notes what was given, for Qt's 'QMetaProperty::QMetaProperty()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmetaproperty.html#QMetaProperty
    """
    #  QMetaProperty::QMetaProperty()
    self._noteCreation(QMetaProperty, lambda: Rituals.call(
        'ritual_ZN13QMetaPropertyC1Ev',
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
