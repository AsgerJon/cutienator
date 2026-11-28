"""
QQmlPropertyPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlproperty_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlPropertyPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QQmlProperty, QQmlPropertyData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaMethod, QMetaObject, QMetaProperty
  from ..QtCore import QMetaType, QObject, QUrl, QVariant
  from . import QQmlAbstractBinding, QQmlBoundSignalExpression
  from . import QQmlMetaObject, QQmlPropertyIndex
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QMetaObject = WAIT['QMetaObject']
  QMetaProperty = WAIT['QMetaProperty']
  QMetaType = WAIT['QMetaType']
  QObject = WAIT['QObject']
  QQmlAbstractBinding = WAIT['QQmlAbstractBinding']
  QQmlBoundSignalExpression = WAIT['QQmlBoundSignalExpression']
  QQmlPropertyIndex = WAIT['QQmlPropertyIndex']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlPropertyPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlPropertyPrivate: a plain Python object standing
  in front of one C++ QQmlPropertyPrivate.

  What exists
  -----------

  Every function of Qt's QQmlPropertyPrivate that has a ritual and that
  Python can call so far, 29 names in all: 'resolveUrlsOnAssignment',
  'encodedIndex', 'initProperty', 'initDefault', 'isValueType',
  'propertyType', 'type', 'propertyTypeCategory', 'readValueProperty',
  'writeValueProperty', 'rawMetaObjectForType', 'writeEnumProperty',
  'convertToWriteTargetType', 'reset', 'findAliasTarget', 'setBinding',
  'removeBinding', 'binding', 'signalIndex', 'get', 'signalExpression',
  'setSignalExpression', 'takeSignalExpression', 'write', 'propertyIndex',
  'findSignalByName', 'findPropertyByName', 'flushSignal', 'urlSequence'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlPropertyPrivate::~QQmlPropertyPrivate()': the destructor:
    Python never removes a C++ QQmlPropertyPrivate.
  - Qt's 'bool QQmlPropertyPrivate::writeValueProperty(QObject *a0, const
    QQmlPropertyData &a1, const QQmlPropertyData &valueTypeData, const
    QVariant &a3, const QQmlRefPointer<QQmlContextData> &a4,
    QQmlPropertyData::WriteFlags flags)': takes a type Python has no way to
    hand over yet.
  - Qt's 'bool QQmlPropertyPrivate::resetValueProperty(QObject *a0, const
    QQmlPropertyData &a1, const QQmlPropertyData &valueTypeData, const
    QQmlRefPointer<QQmlContextData> &a3, QQmlPropertyData::WriteFlags
    flags)': takes a type Python has no way to hand over yet.
  - Qt's 'ListCopyResult
    QQmlPropertyPrivate::convertToQQmlListProperty(QQmlListProperty<QObject>
    *listProperty, QMetaType actualListType, const QVariant &value)': names
    'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'bool QQmlPropertyPrivate::write(QObject *a0, const QQmlPropertyData
    &a1, const QVariant &a2, const QQmlRefPointer<QQmlContextData> &a3,
    QQmlPropertyData::WriteFlags flags)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QQmlPropertyPrivate::findAliasTarget(QObject *a0,
    QQmlPropertyIndex a1, QObject **a2, QQmlPropertyIndex *a3)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QQmlProperty QQmlPropertyPrivate::restore(QObject *a0, const
    QQmlPropertyData &a1, const QQmlPropertyData *a2, const
    QQmlRefPointer<QQmlContextData> &a3)': takes a type Python has no way to
    hand over yet.
  - Qt's 'bool QQmlPropertyPrivate::connect(const QObject *sender, int
    signal_index, const QObject *receiver, int method_index, int type, int
    *types)': takes a number to change where it is.
  - Qt's 'QList<QUrl> QQmlPropertyPrivate::urlSequence(const QVariant &value,
    const QQmlRefPointer<QQmlContextData> &ctxt)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QQmlProperty QQmlPropertyPrivate::create(QObject *target, const
    QString &propertyName, const QQmlRefPointer<QQmlContextData> &context,
    QQmlPropertyPrivate::InitFlags flags)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  1 of the 46 functions Qt declares: 1 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ QQmlPropertyPrivate is created at the first use, not by
    'QQmlPropertyPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlPropertyPrivate.
  - Each name of Qt's QQmlPropertyPrivate that has no cute function yet,
    'connect', 'convertToQQmlListProperty', 'create', 'effectiveContext',
    'resetValueProperty', 'restore', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlPropertyPrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class BindingFlag(CuteFlags):
    """
    The flags enum 'QQmlPropertyPrivate::BindingFlag' of Qt, with the 3 names
    Qt gives in it. Qt names the type of its combinations
    'QQmlPropertyPrivate::BindingFlags'.
    """

    NULL = 0x0
    DontEnable = 0x1
    OverrideSticky = 0x2

  BindingFlags = BindingFlag

  class InitFlag(CuteFlags, scoped=True):
    """
    The flags enum 'QQmlPropertyPrivate::InitFlag' of Qt, with the 3 names Qt
    gives in it. Qt names the type of its combinations
    'QQmlPropertyPrivate::InitFlags'. C++ keeps these names inside the enum,
    so the class that holds the enum does not have them.
    """

    NULL = 0x0
    AllowId = 0x1
    AllowSignal = 0x2

  InitFlags = InitFlag

  class ListCopyResult(CuteNum, scoped=True):
    """
    The enum 'QQmlPropertyPrivate::ListCopyResult' of Qt, with the 3 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Copied = Kee[int](0)
    WasEqual = Kee[int](1)
    TypeMismatch = Kee[int](2)

  #  The classes Qt writes inside QQmlPropertyPrivate, each a class in here
  #  as in C++.

  class ResolvedAlias(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlPropertyPrivate::ResolvedAlias: a plain Python
    object standing in front of one C++ QQmlPropertyPrivate::ResolvedAlias.

    C++ hands a QQmlPropertyPrivate::ResolvedAlias around as a copy, so every
    C++ QQmlPropertyPrivate::ResolvedAlias behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QQmlPropertyPrivate::ResolvedAlias yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlPropertyPrivate::ResolvedAlias::~ResolvedAlias()': the
      destructor: Python removes its C++ QQmlPropertyPrivate::ResolvedAlias
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQmlPropertyPrivate::ResolvedAlias is created at the first use,
      not by 'QQmlPropertyPrivate::ResolvedAlias(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlPropertyPrivate::ResolvedAlias back gives a
      copy the ritual made for Python, in a new cute
      QQmlPropertyPrivate::ResolvedAlias.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlPropertyPrivate::ResolvedAlias'

    #  Qt's '~QQmlPropertyPrivate::ResolvedAlias()'. Naming it makes this a
    #  value class: Python owns every C++ QQmlPropertyPrivate::ResolvedAlias
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN19QQmlPropertyPrivate13ResolvedAliasD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def resolveUrlsOnAssignment() -> bool:
    """
    Calls Qt's 'bool QQmlPropertyPrivate::resolveUrlsOnAssignment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#resolveUrlsOnAssignment
    """
    #  bool QQmlPropertyPrivate::resolveUrlsOnAssignment()
    return Rituals.call(
        'ritual_ZN19QQmlPropertyPrivate23resolveUrlsOnAssignmentEv',
    )

  @staticmethod
  @overload(QMetaType)
  def rawMetaObjectForType(metaType: QMetaType) -> QQmlMetaObject:
    """
    Calls Qt's 'QQmlMetaObject
    QQmlPropertyPrivate::rawMetaObjectForType(QMetaType metaType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#rawMetaObjectForType

    Parameters
    ----------

    metaType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    Returns
    -------

    QQmlMetaObject
      A new cute QQmlMetaObject around the copy Qt gave back. Python owns it.
    """
    #  QQmlMetaObject QQmlPropertyPrivate::rawMetaObjectForType(QMetaType
    #      metaType)
    address = Rituals.call(
        'ritual_ZN19QQmlPropertyPrivate20rawMetaObjectForTypeE9QMetaType',
        CuteMixin._valueOf(metaType),
    )
    from . import QQmlMetaObject
    return QQmlMetaObject._cuteOwning(address)

  @staticmethod
  @overload(QMetaProperty, int, QObject, QVariant, int)
  @overload(QMetaProperty, int, NoneType, QVariant, int)
  def writeEnumProperty(
      prop: QMetaProperty,
      idx: int,
      object: Optional[QObject],
      value: QVariant,
      flags: int,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyPrivate::writeEnumProperty(const
    QMetaProperty &prop, int idx, QObject *object, const QVariant &value, int
    flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#writeEnumProperty

    Parameters
    ----------

    prop : QMetaProperty
      Passed on as a value: Qt reads the C++ QMetaProperty, which stays
      Python's own.

    idx : int
      Passed on as it is.

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    flags : int
      Passed on as it is.
    """
    #  bool QQmlPropertyPrivate::writeEnumProperty(const QMetaProperty &prop,
    #      int idx, QObject *object, const QVariant &value, int flags)
    return Rituals.call(
        'ritual_ZN19QQmlPropertyPrivate17writeEnumPropertyERK13QMetaPropert'
        'yiP7QObjectRK8QVarianti',
        CuteMixin._valueOf(prop), idx, CuteMixin._addressOf(object,
        'QObject'), CuteMixin._valueOf(value), flags,
    )

  @staticmethod
  @overload(QVariant, QMetaType)
  def convertToWriteTargetType(
      value: QVariant,
      targetMetaType: QMetaType,
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlPropertyPrivate::convertToWriteTargetType(const
    QVariant &value, QMetaType targetMetaType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#convertToWriteTargetType

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    targetMetaType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlPropertyPrivate::convertToWriteTargetType(const QVariant
    #      &value, QMetaType targetMetaType)
    address = Rituals.call(
        'ritual_ZN19QQmlPropertyPrivate24convertToWriteTargetTypeERK8QVaria'
        'nt9QMetaType',
        CuteMixin._valueOf(value), CuteMixin._valueOf(targetMetaType),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @staticmethod
  @overload(QObject, QQmlPropertyData)
  @overload(NoneType, QQmlPropertyData)
  @overload(QObject, QQmlPropertyData, QQmlPropertyData.WriteFlags)
  @overload(NoneType, QQmlPropertyData, QQmlPropertyData.WriteFlags)
  def reset(
      a0: Optional[QObject],
      a1: QQmlPropertyData,
      flags: QQmlPropertyData.WriteFlags = QQmlPropertyData.WriteFlags(),
  ) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyPrivate::reset(QObject *a0, const
    QQmlPropertyData &a1, QQmlPropertyData::WriteFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertyprivate.html#reset

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QQmlPropertyData
      Passed on as a value: Qt reads the C++ QQmlPropertyData, which stays
      Python's own.

    flags : QQmlPropertyData.WriteFlags
      Passed on as its number. May be left out, as in Qt: it is then
      QQmlPropertyData.WriteFlags().
    """
    #  bool QQmlPropertyPrivate::reset(QObject *a0, const QQmlPropertyData
    #      &a1, QQmlPropertyData::WriteFlags flags)
    return Rituals.call(
        'ritual_ZN19QQmlPropertyPrivate5resetEP7QObjectRK16QQmlPropertyData'
        '6QFlagsINS2_9WriteFlagEE',
        CuteMixin._addressOf(a0, 'QObject'), CuteMixin._valueOf(a1),
        flags.value,
    )

  @staticmethod
  @overload(QObject, QQmlPropertyIndex)
  @overload(NoneType, QQmlPropertyIndex)
  def findAliasTarget(
      baseObject: Optional[QObject],
      baseIndex: QQmlPropertyIndex,
  ) -> ResolvedAlias:
    """
    Calls Qt's 'ResolvedAlias QQmlPropertyPrivate::findAliasTarget(QObject
    *baseObject, QQmlPropertyIndex baseIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#findAliasTarget

    Parameters
    ----------

    baseObject : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    baseIndex : QQmlPropertyIndex
      Passed on as a value: Qt reads the C++ QQmlPropertyIndex, which stays
      Python's own.

    Returns
    -------

    ResolvedAlias
      A new cute QQmlPropertyPrivate::ResolvedAlias around the copy Qt gave
      back. Python owns it.
    """
    #  ResolvedAlias QQmlPropertyPrivate::findAliasTarget(QObject
    #      *baseObject, QQmlPropertyIndex baseIndex)
    address = Rituals.call(
        'ritual_ZN19QQmlPropertyPrivate15findAliasTargetEP7QObject17QQmlPro'
        'pertyIndex',
        CuteMixin._addressOf(baseObject, 'QObject'),
        CuteMixin._valueOf(baseIndex),
    )
    return QQmlPropertyPrivate.ResolvedAlias._cuteOwning(address)

  @staticmethod
  @overload(QQmlAbstractBinding)
  @overload(NoneType)
  @overload(QQmlAbstractBinding, BindingFlags)
  @overload(NoneType, BindingFlags)
  @overload(QQmlAbstractBinding, BindingFlags, QQmlPropertyData.WriteFlags)
  @overload(NoneType, BindingFlags, QQmlPropertyData.WriteFlags)
  def setBinding(
      binding: Optional[QQmlAbstractBinding],
      flags: BindingFlags = BindingFlags.NULL,
      writeFlags: QQmlPropertyData.WriteFlags = (
          QQmlPropertyData.WriteFlags.DontRemoveBinding),
  ) -> None:
    """
    Calls Qt's 'void QQmlPropertyPrivate::setBinding(QQmlAbstractBinding
    *binding, BindingFlags flags, QQmlPropertyData::WriteFlags writeFlags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#setBinding

    Parameters
    ----------

    binding : Optional[QQmlAbstractBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : BindingFlags
      Passed on as its number. May be left out, as in Qt: it is then
      BindingFlags.NULL.

    writeFlags : QQmlPropertyData.WriteFlags
      Passed on as its number. May be left out, as in Qt: it is then
      QQmlPropertyData.WriteFlags.DontRemoveBinding.
    """
    #  void QQmlPropertyPrivate::setBinding(QQmlAbstractBinding *binding,
    #      BindingFlags flags, QQmlPropertyData::WriteFlags writeFlags)
    Rituals.call(
        'ritual_ZN19QQmlPropertyPrivate10setBindingEP19QQmlAbstractBinding6'
        'QFlagsINS_11BindingFlagEES2_IN16QQmlPropertyData9WriteFlagEE',
        CuteMixin._addressOf(binding, 'QQmlAbstractBinding'), flags.value,
        writeFlags.value,
    )

  @staticmethod
  @overload(QQmlProperty, QQmlAbstractBinding)
  @overload(QQmlProperty, NoneType)
  def setBinding(
      that: QQmlProperty,
      a1: Optional[QQmlAbstractBinding],
  ) -> None:
    """
    Calls Qt's 'void QQmlPropertyPrivate::setBinding(const QQmlProperty
    &that, QQmlAbstractBinding *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#setBinding

    Parameters
    ----------

    that : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.

    a1 : Optional[QQmlAbstractBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlPropertyPrivate::setBinding(const QQmlProperty &that,
    #      QQmlAbstractBinding *a1)
    Rituals.call(
        'ritual_ZN19QQmlPropertyPrivate10setBindingERK12QQmlPropertyP19QQml'
        'AbstractBinding',
        CuteMixin._valueOf(that), CuteMixin._addressOf(a1,
        'QQmlAbstractBinding'),
    )

  @staticmethod
  @overload(QQmlProperty)
  @overload(QQmlProperty, BindingFlags)
  def removeBinding(
      that: QQmlProperty,
      flags: BindingFlags = BindingFlags.NULL,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyPrivate::removeBinding(const QQmlProperty
    &that, BindingFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#removeBinding

    Parameters
    ----------

    that : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.

    flags : BindingFlags
      Passed on as its number. May be left out, as in Qt: it is then
      BindingFlags.NULL.
    """
    #  bool QQmlPropertyPrivate::removeBinding(const QQmlProperty &that,
    #      BindingFlags flags)
    return Rituals.call(
        'ritual_ZN19QQmlPropertyPrivate13removeBindingERK12QQmlProperty6QFl'
        'agsINS_11BindingFlagEE',
        CuteMixin._valueOf(that), flags.value,
    )

  @staticmethod
  @overload(QObject, QQmlPropertyIndex)
  @overload(NoneType, QQmlPropertyIndex)
  @overload(QObject, QQmlPropertyIndex, BindingFlags)
  @overload(NoneType, QQmlPropertyIndex, BindingFlags)
  def removeBinding(
      o: Optional[QObject],
      index: QQmlPropertyIndex,
      flags: BindingFlags = BindingFlags.NULL,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyPrivate::removeBinding(QObject *o,
    QQmlPropertyIndex index, BindingFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#removeBinding

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : QQmlPropertyIndex
      Passed on as a value: Qt reads the C++ QQmlPropertyIndex, which stays
      Python's own.

    flags : BindingFlags
      Passed on as its number. May be left out, as in Qt: it is then
      BindingFlags.NULL.
    """
    #  bool QQmlPropertyPrivate::removeBinding(QObject *o, QQmlPropertyIndex
    #      index, BindingFlags flags)
    return Rituals.call(
        'ritual_ZN19QQmlPropertyPrivate13removeBindingEP7QObject17QQmlPrope'
        'rtyIndex6QFlagsINS_11BindingFlagEE',
        CuteMixin._addressOf(o, 'QObject'), CuteMixin._valueOf(index),
        flags.value,
    )

  @staticmethod
  @overload(QQmlAbstractBinding)
  @overload(NoneType)
  @overload(QQmlAbstractBinding, BindingFlags)
  @overload(NoneType, BindingFlags)
  def removeBinding(
      b: Optional[QQmlAbstractBinding],
      flags: BindingFlags = BindingFlags.NULL,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyPrivate::removeBinding(QQmlAbstractBinding
    *b, QQmlPropertyPrivate::BindingFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#removeBinding

    Parameters
    ----------

    b : Optional[QQmlAbstractBinding]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : BindingFlags
      Passed on as its number. May be left out, as in Qt: it is then
      BindingFlags.NULL.
    """
    #  bool QQmlPropertyPrivate::removeBinding(QQmlAbstractBinding *b,
    #      QQmlPropertyPrivate::BindingFlags flags)
    return Rituals.call(
        'ritual_ZN19QQmlPropertyPrivate13removeBindingEP19QQmlAbstractBindi'
        'ng6QFlagsINS_11BindingFlagEE',
        CuteMixin._addressOf(b, 'QQmlAbstractBinding'), flags.value,
    )

  @staticmethod
  @overload(QObject, QQmlPropertyIndex)
  @overload(NoneType, QQmlPropertyIndex)
  def binding(
      a0: Optional[QObject],
      index: QQmlPropertyIndex,
  ) -> Optional[QQmlAbstractBinding]:
    """
    Calls Qt's 'QQmlAbstractBinding *QQmlPropertyPrivate::binding(QObject
    *a0, QQmlPropertyIndex index)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertyprivate.html#binding

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : QQmlPropertyIndex
      Passed on as a value: Qt reads the C++ QQmlPropertyIndex, which stays
      Python's own.

    Returns
    -------

    Optional[QQmlAbstractBinding]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlAbstractBinding *QQmlPropertyPrivate::binding(QObject *a0,
    #      QQmlPropertyIndex index)
    address = Rituals.call(
        'ritual_ZN19QQmlPropertyPrivate7bindingEP7QObject17QQmlPropertyInde'
        'x',
        CuteMixin._addressOf(a0, 'QObject'), CuteMixin._valueOf(index),
    )
    from . import QQmlAbstractBinding
    return QQmlAbstractBinding._cuteAt(address)

  @staticmethod
  @overload(QQmlProperty)
  def binding(that: QQmlProperty) -> Optional[QQmlAbstractBinding]:
    """
    Calls Qt's 'QQmlAbstractBinding *QQmlPropertyPrivate::binding(const
    QQmlProperty &that)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertyprivate.html#binding

    Parameters
    ----------

    that : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.

    Returns
    -------

    Optional[QQmlAbstractBinding]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlAbstractBinding *QQmlPropertyPrivate::binding(const QQmlProperty
    #      &that)
    address = Rituals.call(
        'ritual_ZN19QQmlPropertyPrivate7bindingERK12QQmlProperty',
        CuteMixin._valueOf(that),
    )
    from . import QQmlAbstractBinding
    return QQmlAbstractBinding._cuteAt(address)

  @staticmethod
  @overload(QQmlProperty)
  def get(p: QQmlProperty) -> Optional[QQmlPropertyPrivate]:
    """
    Calls Qt's 'QQmlPropertyPrivate *QQmlPropertyPrivate::get(const
    QQmlProperty &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertyprivate.html#get

    Parameters
    ----------

    p : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.

    Returns
    -------

    Optional[QQmlPropertyPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlPropertyPrivate *QQmlPropertyPrivate::get(const QQmlProperty &p)
    address = Rituals.call(
        'ritual_ZN19QQmlPropertyPrivate3getERK12QQmlProperty',
        CuteMixin._valueOf(p),
    )
    return QQmlPropertyPrivate._cuteAt(address)

  @staticmethod
  @overload(QQmlProperty)
  def signalExpression(
      that: QQmlProperty,
  ) -> Optional[QQmlBoundSignalExpression]:
    """
    Calls Qt's 'QQmlBoundSignalExpression
    *QQmlPropertyPrivate::signalExpression(const QQmlProperty &that)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#signalExpression

    Parameters
    ----------

    that : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.

    Returns
    -------

    Optional[QQmlBoundSignalExpression]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlBoundSignalExpression *QQmlPropertyPrivate::signalExpression(const
    #      QQmlProperty &that)
    address = Rituals.call(
        'ritual_ZN19QQmlPropertyPrivate16signalExpressionERK12QQmlProperty',
        CuteMixin._valueOf(that),
    )
    from . import QQmlBoundSignalExpression
    return QQmlBoundSignalExpression._cuteAt(address)

  @staticmethod
  @overload(QQmlProperty, QQmlBoundSignalExpression)
  @overload(QQmlProperty, NoneType)
  def setSignalExpression(
      that: QQmlProperty,
      a1: Optional[QQmlBoundSignalExpression],
  ) -> None:
    """
    Calls Qt's 'void QQmlPropertyPrivate::setSignalExpression(const
    QQmlProperty &that, QQmlBoundSignalExpression *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#setSignalExpression

    Parameters
    ----------

    that : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.

    a1 : Optional[QQmlBoundSignalExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlPropertyPrivate::setSignalExpression(const QQmlProperty
    #      &that, QQmlBoundSignalExpression *a1)
    Rituals.call(
        'ritual_ZN19QQmlPropertyPrivate19setSignalExpressionERK12QQmlProper'
        'tyP25QQmlBoundSignalExpression',
        CuteMixin._valueOf(that), CuteMixin._addressOf(a1),
    )

  @staticmethod
  @overload(QQmlProperty, QQmlBoundSignalExpression)
  @overload(QQmlProperty, NoneType)
  def takeSignalExpression(
      that: QQmlProperty,
      a1: Optional[QQmlBoundSignalExpression],
  ) -> None:
    """
    Calls Qt's 'void QQmlPropertyPrivate::takeSignalExpression(const
    QQmlProperty &that, QQmlBoundSignalExpression *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#takeSignalExpression

    Parameters
    ----------

    that : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.

    a1 : Optional[QQmlBoundSignalExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlPropertyPrivate::takeSignalExpression(const QQmlProperty
    #      &that, QQmlBoundSignalExpression *a1)
    Rituals.call(
        'ritual_ZN19QQmlPropertyPrivate20takeSignalExpressionERK12QQmlPrope'
        'rtyP25QQmlBoundSignalExpression',
        CuteMixin._valueOf(that), CuteMixin._addressOf(a1),
    )

  @staticmethod
  @overload(QQmlProperty, QVariant, QQmlPropertyData.WriteFlags)
  def write(
      that: QQmlProperty,
      a1: QVariant,
      a2: QQmlPropertyData.WriteFlags,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyPrivate::write(const QQmlProperty &that,
    const QVariant &a1, QQmlPropertyData::WriteFlags a2)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertyprivate.html#write

    Parameters
    ----------

    that : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.

    a1 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    a2 : QQmlPropertyData.WriteFlags
      Passed on as its number.
    """
    #  bool QQmlPropertyPrivate::write(const QQmlProperty &that, const
    #      QVariant &a1, QQmlPropertyData::WriteFlags a2)
    return Rituals.call(
        'ritual_ZN19QQmlPropertyPrivate5writeERK12QQmlPropertyRK8QVariant6Q'
        'FlagsIN16QQmlPropertyData9WriteFlagEE',
        CuteMixin._valueOf(that), CuteMixin._valueOf(a1), a2.value,
    )

  @staticmethod
  @overload(QQmlProperty)
  def propertyIndex(that: QQmlProperty) -> QQmlPropertyIndex:
    """
    Calls Qt's 'QQmlPropertyIndex QQmlPropertyPrivate::propertyIndex(const
    QQmlProperty &that)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#propertyIndex

    Parameters
    ----------

    that : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.

    Returns
    -------

    QQmlPropertyIndex
      A new cute QQmlPropertyIndex around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlPropertyIndex QQmlPropertyPrivate::propertyIndex(const
    #      QQmlProperty &that)
    address = Rituals.call(
        'ritual_ZN19QQmlPropertyPrivate13propertyIndexERK12QQmlProperty',
        CuteMixin._valueOf(that),
    )
    from . import QQmlPropertyIndex
    return QQmlPropertyIndex._cuteOwning(address)

  @staticmethod
  @overload(QMetaObject, QByteArray)
  @overload(NoneType, QByteArray)
  def findSignalByName(
      mo: Optional[QMetaObject],
      a1: QByteArray,
  ) -> QMetaMethod:
    """
    Calls Qt's 'QMetaMethod QQmlPropertyPrivate::findSignalByName(const
    QMetaObject *mo, const QByteArray &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#findSignalByName

    Parameters
    ----------

    mo : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QMetaMethod
      A new cute QMetaMethod around the copy Qt gave back. Python owns it.
    """
    #  QMetaMethod QQmlPropertyPrivate::findSignalByName(const QMetaObject
    #      *mo, const QByteArray &a1)
    address = Rituals.call(
        'ritual_ZN19QQmlPropertyPrivate16findSignalByNameEPK11QMetaObjectRK'
        '10QByteArray',
        CuteMixin._addressOf(mo, 'QMetaObject'), CuteMixin._valueOf(a1),
    )
    from ..QtCore import QMetaMethod
    return QMetaMethod._cuteOwning(address)

  @staticmethod
  @overload(QMetaObject, QByteArray)
  @overload(NoneType, QByteArray)
  def findPropertyByName(
      mo: Optional[QMetaObject],
      a1: QByteArray,
  ) -> QMetaProperty:
    """
    Calls Qt's 'QMetaProperty QQmlPropertyPrivate::findPropertyByName(const
    QMetaObject *mo, const QByteArray &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#findPropertyByName

    Parameters
    ----------

    mo : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QMetaProperty
      A new cute QMetaProperty around the copy Qt gave back. Python owns it.
    """
    #  QMetaProperty QQmlPropertyPrivate::findPropertyByName(const
    #      QMetaObject *mo, const QByteArray &a1)
    address = Rituals.call(
        'ritual_ZN19QQmlPropertyPrivate18findPropertyByNameEPK11QMetaObject'
        'RK10QByteArray',
        CuteMixin._addressOf(mo, 'QMetaObject'), CuteMixin._valueOf(a1),
    )
    from ..QtCore import QMetaProperty
    return QMetaProperty._cuteOwning(address)

  @staticmethod
  @overload(QObject, int)
  @overload(NoneType, int)
  def flushSignal(sender: Optional[QObject], signal_index: int) -> None:
    """
    Calls Qt's 'void QQmlPropertyPrivate::flushSignal(const QObject *sender,
    int signal_index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#flushSignal

    Parameters
    ----------

    sender : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    signal_index : int
      Passed on as it is.
    """
    #  void QQmlPropertyPrivate::flushSignal(const QObject *sender, int
    #      signal_index)
    Rituals.call(
        'ritual_ZN19QQmlPropertyPrivate11flushSignalEPK7QObjecti',
        CuteMixin._addressOf(sender, 'QObject'), signal_index,
    )

  @staticmethod
  @overload(QVariant)
  def urlSequence(value: QVariant) -> QList[QUrl]:
    """
    Calls Qt's 'QList<QUrl> QQmlPropertyPrivate::urlSequence(const QVariant
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#urlSequence

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QList[QUrl]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QUrl> QQmlPropertyPrivate::urlSequence(const QVariant &value)
    address = Rituals.call(
        'ritual_ZN19QQmlPropertyPrivate11urlSequenceERK8QVariant',
        CuteMixin._valueOf(value),
    )
    from ..QtCore import QUrl
    return QList[QUrl]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlPropertyPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def encodedIndex(self) -> QQmlPropertyIndex:
    """
    Calls Qt's 'QQmlPropertyIndex QQmlPropertyPrivate::encodedIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#encodedIndex

    Returns
    -------

    QQmlPropertyIndex
      A new cute QQmlPropertyIndex around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlPropertyIndex QQmlPropertyPrivate::encodedIndex() const
    address = self.uglySide.call(
        'ritual_ZNK19QQmlPropertyPrivate12encodedIndexEv',
    )
    from . import QQmlPropertyIndex
    return QQmlPropertyIndex._cuteOwning(address)

  @staticmethod
  @overload(QQmlPropertyData, QQmlPropertyData)
  def encodedIndex(
      core: QQmlPropertyData,
      valueTypeData: QQmlPropertyData,
  ) -> QQmlPropertyIndex:
    """
    Calls Qt's 'QQmlPropertyIndex QQmlPropertyPrivate::encodedIndex(const
    QQmlPropertyData &core, const QQmlPropertyData &valueTypeData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#encodedIndex

    Parameters
    ----------

    core : QQmlPropertyData
      Passed on as a value: Qt reads the C++ QQmlPropertyData, which stays
      Python's own.

    valueTypeData : QQmlPropertyData
      Passed on as a value: Qt reads the C++ QQmlPropertyData, which stays
      Python's own.

    Returns
    -------

    QQmlPropertyIndex
      A new cute QQmlPropertyIndex around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlPropertyIndex QQmlPropertyPrivate::encodedIndex(const
    #      QQmlPropertyData &core, const QQmlPropertyData &valueTypeData)
    address = Rituals.call(
        'ritual_ZN19QQmlPropertyPrivate12encodedIndexERK16QQmlPropertyDataS'
        '2_',
        CuteMixin._valueOf(core), CuteMixin._valueOf(valueTypeData),
    )
    from . import QQmlPropertyIndex
    return QQmlPropertyIndex._cuteOwning(address)

  def isValueType(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyPrivate::isValueType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#isValueType
    """
    #  bool QQmlPropertyPrivate::isValueType() const
    return self.uglySide.call(
        'ritual_ZNK19QQmlPropertyPrivate11isValueTypeEv',
    )

  def propertyType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QQmlPropertyPrivate::propertyType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#propertyType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QQmlPropertyPrivate::propertyType() const
    address = self.uglySide.call(
        'ritual_ZNK19QQmlPropertyPrivate12propertyTypeEv',
    )
    from ..QtCore import QMetaType
    return QMetaType._cuteOwning(address)

  def type(self) -> QQmlProperty.Type:
    """
    Calls Qt's 'QQmlProperty::Type QQmlPropertyPrivate::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertyprivate.html#type

    Returns
    -------

    QQmlProperty.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlProperty.Type(number)' gives.
    """
    #  QQmlProperty::Type QQmlPropertyPrivate::type() const
    return QQmlProperty.Type(self.uglySide.call(
        'ritual_ZNK19QQmlPropertyPrivate4typeEv',
    ))

  def propertyTypeCategory(self) -> QQmlProperty.PropertyTypeCategory:
    """
    Calls Qt's 'QQmlProperty::PropertyTypeCategory
    QQmlPropertyPrivate::propertyTypeCategory() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#propertyTypeCategory

    Returns
    -------

    QQmlProperty.PropertyTypeCategory
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQmlProperty.PropertyTypeCategory(number)' gives.
    """
    #  QQmlProperty::PropertyTypeCategory
    #      QQmlPropertyPrivate::propertyTypeCategory() const
    return QQmlProperty.PropertyTypeCategory(self.uglySide.call(
        'ritual_ZNK19QQmlPropertyPrivate20propertyTypeCategoryEv',
    ))

  def signalIndex(self) -> int:
    """
    Calls Qt's 'int QQmlPropertyPrivate::signalIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#signalIndex
    """
    #  int QQmlPropertyPrivate::signalIndex() const
    return self.uglySide.call(
        'ritual_ZNK19QQmlPropertyPrivate11signalIndexEv',
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQmlPropertyPrivate::QQmlPropertyPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#QQmlPropertyPrivate
    """
    #  QQmlPropertyPrivate::QQmlPropertyPrivate()
    self._noteCreation(QQmlPropertyPrivate, lambda: Rituals.call(
        'ritual_ZN19QQmlPropertyPrivateC1Ev',
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

  @overload(QObject, str)
  @overload(NoneType, str)
  @overload(QObject, str, InitFlags)
  @overload(NoneType, str, InitFlags)
  def initProperty(
      self,
      obj: Optional[QObject],
      name: str,
      flags: InitFlags = InitFlags.NULL,
  ) -> None:
    """
    Calls Qt's 'void QQmlPropertyPrivate::initProperty(QObject *obj, const
    QString &name, InitFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#initProperty

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.

    flags : InitFlags
      Passed on as its number. May be left out, as in Qt: it is then
      InitFlags.NULL.
    """
    #  void QQmlPropertyPrivate::initProperty(QObject *obj, const QString
    #      &name, InitFlags flags)
    self.uglySide.call(
        'ritual_ZN19QQmlPropertyPrivate12initPropertyEP7QObjectRK7QString6Q'
        'FlagsINS_8InitFlagEE',
        self._addressOf(obj, 'QObject'), name, flags.value,
    )

  @overload(QObject)
  @overload(NoneType)
  def initDefault(self, obj: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlPropertyPrivate::initDefault(QObject *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#initDefault

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlPropertyPrivate::initDefault(QObject *obj)
    self.uglySide.call(
        'ritual_ZN19QQmlPropertyPrivate11initDefaultEP7QObject',
        self._addressOf(obj, 'QObject'),
    )

  def readValueProperty(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlPropertyPrivate::readValueProperty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#readValueProperty

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlPropertyPrivate::readValueProperty()
    address = self.uglySide.call(
        'ritual_ZN19QQmlPropertyPrivate17readValuePropertyEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QVariant, QQmlPropertyData.WriteFlags)
  def writeValueProperty(
      self,
      a0: QVariant,
      a1: QQmlPropertyData.WriteFlags,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyPrivate::writeValueProperty(const QVariant
    &a0, QQmlPropertyData::WriteFlags a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertyprivate.html#writeValueProperty

    Parameters
    ----------

    a0 : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    a1 : QQmlPropertyData.WriteFlags
      Passed on as its number.
    """
    #  bool QQmlPropertyPrivate::writeValueProperty(const QVariant &a0,
    #      QQmlPropertyData::WriteFlags a1)
    return self.uglySide.call(
        'ritual_ZN19QQmlPropertyPrivate18writeValuePropertyERK8QVariant6QFl'
        'agsIN16QQmlPropertyData9WriteFlagEE',
        self._valueOf(a0), a1.value,
    )

  @staticmethod
  def connect(*__, **_) -> Never:
    """
    Qt's 'bool QQmlPropertyPrivate::connect(const QObject *sender, int
    signal_index, const QObject *receiver, int method_index, int type, int
    *types)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQmlPropertyPrivate.connect' has no cute function yet. Qt's 'bool "
        "QQmlPropertyPrivate::connect(const QObject *sender, int "
        "signal_index, const QObject *receiver, int method_index, int type, "
        "int *types)': takes a number to change where it is.")

  @staticmethod
  def convertToQQmlListProperty(*__, **_) -> Never:
    """
    Qt's 'ListCopyResult
    QQmlPropertyPrivate::convertToQQmlListProperty(QQmlListProperty<QObject>
    *listProperty, QMetaType actualListType, const QVariant &value)': names
    'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyPrivate.convertToQQmlListProperty' has no cute "
        "function yet. Qt's 'ListCopyResult "
        "QQmlPropertyPrivate::convertToQQmlListProperty(QQmlListProperty<QOb"
        "ject> *listProperty, QMetaType actualListType, const QVariant "
        "&value)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'QQmlProperty QQmlPropertyPrivate::create(QObject *target, const
    QString &propertyName, const QQmlRefPointer<QQmlContextData> &context,
    QQmlPropertyPrivate::InitFlags flags)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyPrivate.create' has no cute function yet. Qt's "
        "'QQmlProperty QQmlPropertyPrivate::create(QObject *target, const "
        "QString &propertyName, const QQmlRefPointer<QQmlContextData> "
        "&context, QQmlPropertyPrivate::InitFlags flags)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def effectiveContext(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QQmlContextData>
    QQmlPropertyPrivate::effectiveContext() const': the compiler refuses its
    ritual as it would be written here: member access into incomplete type
    'QQmlContextData'.
    """
    raise NotImplementedError(
        "'QQmlPropertyPrivate.effectiveContext' has no cute function yet. "
        "Qt's 'QQmlRefPointer<QQmlContextData> "
        "QQmlPropertyPrivate::effectiveContext() const': the compiler "
        "refuses its ritual as it would be written here: member access into "
        "incomplete type 'QQmlContextData'.")

  @staticmethod
  def resetValueProperty(*__, **_) -> Never:
    """
    Qt's 'bool QQmlPropertyPrivate::resetValueProperty(QObject *a0, const
    QQmlPropertyData &a1, const QQmlPropertyData &valueTypeData, const
    QQmlRefPointer<QQmlContextData> &a3, QQmlPropertyData::WriteFlags
    flags)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyPrivate.resetValueProperty' has no cute function yet. "
        "Qt's 'bool QQmlPropertyPrivate::resetValueProperty(QObject *a0, "
        "const QQmlPropertyData &a1, const QQmlPropertyData &valueTypeData, "
        "const QQmlRefPointer<QQmlContextData> &a3, "
        "QQmlPropertyData::WriteFlags flags)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def restore(*__, **_) -> Never:
    """
    Qt's 'QQmlProperty QQmlPropertyPrivate::restore(QObject *a0, const
    QQmlPropertyData &a1, const QQmlPropertyData *a2, const
    QQmlRefPointer<QQmlContextData> &a3)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyPrivate.restore' has no cute function yet. Qt's "
        "'QQmlProperty QQmlPropertyPrivate::restore(QObject *a0, const "
        "QQmlPropertyData &a1, const QQmlPropertyData *a2, const "
        "QQmlRefPointer<QQmlContextData> &a3)': takes a type Python has no "
        "way to hand over yet.")
