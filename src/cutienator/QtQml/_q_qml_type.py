"""
QQmlType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmltype_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QQmlType to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QMetaSequence, QMetaType
  from ..QtCore import QObject, QTypeRevision, QUrl
  from . import QHashedString, QHashedStringRef, QQmlCustomParser
  from . import QQmlTypeLoader, QQmlTypePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHashedStringRef = WAIT['QHashedStringRef']
  QObject = WAIT['QObject']
  QQmlTypeLoader = WAIT['QQmlTypeLoader']
  QQmlTypePrivate = WAIT['QQmlTypePrivate']
  QTypeRevision = WAIT['QTypeRevision']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlType(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlType: a plain Python object standing in front of
  one C++ QQmlType.

  C++ hands a QQmlType around as a copy, so every C++ QQmlType behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlType that has a ritual and that Python can call
  so far, 48 names in all: 'isValid', 'typeName', 'qmlTypeName',
  'elementName', 'module', 'version', 'availableInVersion',
  'canConstructValueType', 'canPopulateValueType', 'create',
  'createWithQQmlData', 'customParser', 'isCreatable', 'extensionMetaObject',
  'isExtendedType', 'noCreationReason', 'isSingleton', 'isInterface',
  'isComposite', 'isCompositeSingleton', 'isQObjectSingleton',
  'isQJSValueSingleton', 'isSequentialContainer', 'isValueType', 'typeId',
  'qListTypeId', 'listMetaSequence', 'metaObject', 'metaObjectForValueType',
  'baseMetaObject', 'metaObjectRevision', 'containsRevisionedAttributes',
  'attachedPropertiesType', 'parserStatusCast', 'interfaceIId',
  'propertyValueSourceCast', 'propertyValueInterceptorCast', 'finalizerCast',
  'index', 'isInlineComponentType', 'sourceUrl', 'priv', 'refHandle',
  'derefHandle', 'refCount', 'createProxy', '__eq__', '__ne__'. It can be
  made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlType::QQmlType(QQmlType &&other)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QQmlType &QQmlType::operator=(const QQmlType &other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QQmlType &QQmlType::operator=(QQmlType &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QQmlType::~QQmlType()': the destructor: Python removes its C++
    QQmlType by it, and has no other use for it.
  - Qt's 'CreateValueTypeFunc QQmlType::createValueTypeFunction() const':
    gives a type Python has no way to take yet.
  - Qt's 'QObject *QQmlType::create(void **a0, size_t a1) const': takes a
    type Python has no way to hand over yet.
  - Qt's 'CreateFunc QQmlType::createFunction() const': gives a type Python
    has no way to take yet.
  - Qt's 'ExtensionFunc QQmlType::extensionFunction() const': gives a type
    Python has no way to take yet.
  - Qt's 'QQmlAttachedPropertiesFunc
    QQmlType::attachedPropertiesFunction(QQmlTypeLoader *typeLoader) const':
    gives a type Python has no way to take yet.
  - Qt's 'SingletonInstanceInfo::ConstPtr QQmlType::singletonInstanceInfo()
    const': gives a type Python has no way to take yet.
  - Qt's 'int QQmlType::enumValue(QQmlTypeLoader *typeLoader, const
    QHashedStringRef &a1, bool *ok) const': takes a number to change where it
    is.
  - Qt's 'int QQmlType::enumValue(QQmlTypeLoader *typeLoader, const
    QHashedCStringRef &a1, bool *ok) const': takes a number to change where
    it is.
  - Qt's 'int QQmlType::enumValue(QQmlTypeLoader *typeLoader, const
    QV4::String *a1, bool *ok) const': takes a number to change where it is.
  - Qt's 'int QQmlType::scopedEnumIndex(QQmlTypeLoader *typeLoader, const
    QV4::String *a1, bool *ok) const': takes a number to change where it is.
  - Qt's 'int QQmlType::scopedEnumIndex(QQmlTypeLoader *typeLoader, const
    QString &a1, bool *ok) const': takes a number to change where it is.
  - Qt's 'int QQmlType::unscopedEnumIndex(QQmlTypeLoader *typeLoader, const
    QV4::String *a1, bool *ok) const': takes a number to change where it is.
  - Qt's 'int QQmlType::unscopedEnumIndex(QQmlTypeLoader *typeLoader, const
    QString &a1, bool *ok) const': takes a number to change where it is.
  - Qt's 'int QQmlType::scopedEnumValue(QQmlTypeLoader *typeLoader, int
    index, const QV4::String *a2, bool *ok) const': takes a number to change
    where it is.
  - Qt's 'int QQmlType::scopedEnumValue(QQmlTypeLoader *typeLoader, int
    index, const QString &a2, bool *ok) const': takes a number to change
    where it is.
  - Qt's 'int QQmlType::scopedEnumValue(QQmlTypeLoader *typeLoader, const
    QHashedStringRef &a1, const QHashedStringRef &a2, bool *ok) const': takes
    a number to change where it is.
  - Qt's 'int QQmlType::unscopedEnumValue(QQmlTypeLoader *typeLoader, int
    index, const QV4::String *a2, bool *ok) const': takes a number to change
    where it is.
  - Qt's 'int QQmlType::unscopedEnumValue(QQmlTypeLoader *typeLoader, int
    index, const QString &a2, bool *ok) const': takes a number to change
    where it is.
  - Qt's 'int QQmlType::unscopedEnumValue(QQmlTypeLoader *typeLoader, const
    QHashedStringRef &a1, const QHashedStringRef &a2, bool *ok) const': takes
    a number to change where it is.
  - Qt's 'QString QQmlType::scopedEnumKey(QQmlTypeLoader *typeLoader, int
    index, int value, bool *ok) const': takes a number to change where it is.
  - Qt's 'QStringList QQmlType::scopedEnumKeys(QQmlTypeLoader *typeLoader,
    int index, int value, bool *ok) const': takes a number to change where it
    is.
  - Qt's 'QString QQmlType::unscopedEnumKey(QQmlTypeLoader *typeLoader, int
    index, int value, bool *ok) const': takes a number to change where it is.
  - Qt's 'QStringList QQmlType::unscopedEnumKeys(QQmlTypeLoader *typeLoader,
    int index, int value, bool *ok) const': takes a number to change where it
    is.

  What to expect
  --------------

  - The C++ QQmlType is created at the first use, not by 'QQmlType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlType back gives a copy the ritual made for
    Python, in a new cute QQmlType.
  - Each name of Qt's QQmlType that has no cute function yet,
    'attachedPropertiesFunction', 'createFunction',
    'createValueTypeFunction', 'enumValue', 'extensionFunction',
    'scopedEnumIndex', 'scopedEnumKey', 'scopedEnumKeys', 'scopedEnumValue',
    'singletonInstanceInfo', 'unscopedEnumIndex', 'unscopedEnumKey',
    'unscopedEnumKeys', 'unscopedEnumValue', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlType, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class RegistrationType(CuteNum):
    """
    The enum 'QQmlType::RegistrationType' of Qt, with the 9 names Qt gives in
    it.
    """

    CppType = Kee[int](0)
    SingletonType = Kee[int](1)
    InterfaceType = Kee[int](2)
    CompositeType = Kee[int](3)
    CompositeSingletonType = Kee[int](4)
    InlineComponentType = Kee[int](5)
    SequentialContainerType = Kee[int](6)
    JavaScriptType = Kee[int](7)
    AnyRegistrationType = Kee[int](255)

  #  The classes Qt writes inside QQmlType, each a class in here as in C++.

  class SingletonInstanceInfo(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlType::SingletonInstanceInfo: a plain Python
    object standing in front of one C++ QQmlType::SingletonInstanceInfo.

    What exists
    -----------

    No function of Qt's QQmlType::SingletonInstanceInfo yet. It can be made
    from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'Ptr QQmlType::SingletonInstanceInfo::create()': gives a type
      Python has no way to take yet.

    What has no ritual
    ------------------

    4 of the 6 functions Qt declares: 4 forbidden.

    What to expect
    --------------

    - The C++ QQmlType::SingletonInstanceInfo is created at the first use,
      not by 'QQmlType::SingletonInstanceInfo(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QQmlType::SingletonInstanceInfo.
    - Each name of Qt's QQmlType::SingletonInstanceInfo that has no cute
      function yet, 'create', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlType::SingletonInstanceInfo'

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QQmlType::SingletonInstanceInfo::SingletonInstanceInfo()', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmltype-singletoninstanceinfo.html
      """
      #  QQmlType::SingletonInstanceInfo::SingletonInstanceInfo()
      self._noteCreation(
          QQmlType.SingletonInstanceInfo, lambda: Rituals.call(
              'ritual_ZN8QQmlType21SingletonInstanceInfoC1Ev',
          ))

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

    @staticmethod
    def create(*__, **_) -> Never:
      """
      Qt's 'Ptr QQmlType::SingletonInstanceInfo::create()': gives a type
      Python has no way to take yet.
      """
      raise NotImplementedError(
          "'QQmlType.SingletonInstanceInfo.create' has no cute function "
          "yet. Qt's 'Ptr QQmlType::SingletonInstanceInfo::create()': gives "
          "a type Python has no way to take yet.")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQmlTypePrivate)
  @overload(NoneType)
  def refHandle(priv: Optional[QQmlTypePrivate]) -> None:
    """
    Calls Qt's 'void QQmlType::refHandle(const QQmlTypePrivate *priv)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#refHandle

    Parameters
    ----------

    priv : Optional[QQmlTypePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlType::refHandle(const QQmlTypePrivate *priv)
    Rituals.call(
        'ritual_ZN8QQmlType9refHandleEPK15QQmlTypePrivate',
        CuteMixin._addressOf(priv),
    )

  @staticmethod
  @overload(QQmlTypePrivate)
  @overload(NoneType)
  def derefHandle(priv: Optional[QQmlTypePrivate]) -> None:
    """
    Calls Qt's 'void QQmlType::derefHandle(const QQmlTypePrivate *priv)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#derefHandle

    Parameters
    ----------

    priv : Optional[QQmlTypePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlType::derefHandle(const QQmlTypePrivate *priv)
    Rituals.call(
        'ritual_ZN8QQmlType11derefHandleEPK15QQmlTypePrivate',
        CuteMixin._addressOf(priv),
    )

  @staticmethod
  @overload(QQmlTypePrivate)
  @overload(NoneType)
  def refCount(priv: Optional[QQmlTypePrivate]) -> int:
    """
    Calls Qt's 'int QQmlType::refCount(const QQmlTypePrivate *priv)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#refCount

    Parameters
    ----------

    priv : Optional[QQmlTypePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QQmlType::refCount(const QQmlTypePrivate *priv)
    return Rituals.call(
        'ritual_ZN8QQmlType8refCountEPK15QQmlTypePrivate',
        CuteMixin._addressOf(priv),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlType'

  #  Qt's '~QQmlType()'. Naming it makes this a value class: Python owns
  #  every C++ QQmlType behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8QQmlTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlType::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#isValid
    """
    #  bool QQmlType::isValid() const
    return self.uglySide.call('ritual_ZNK8QQmlType7isValidEv')

  def typeName(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QQmlType::typeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#typeName

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QQmlType::typeName() const
    address = self.uglySide.call('ritual_ZNK8QQmlType8typeNameEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def qmlTypeName(self) -> str:
    """
    Calls Qt's 'QString QQmlType::qmlTypeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#qmlTypeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlType::qmlTypeName() const
    return self.uglySide.call('ritual_ZNK8QQmlType11qmlTypeNameEv')

  def elementName(self) -> str:
    """
    Calls Qt's 'QString QQmlType::elementName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#elementName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlType::elementName() const
    return self.uglySide.call('ritual_ZNK8QQmlType11elementNameEv')

  def module(self) -> QHashedString:
    """
    Calls Qt's 'QHashedString QQmlType::module() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#module

    Returns
    -------

    QHashedString
      A new cute QHashedString around the copy Qt gave back. Python owns it.
    """
    #  QHashedString QQmlType::module() const
    address = self.uglySide.call('ritual_ZNK8QQmlType6moduleEv')
    from . import QHashedString
    return QHashedString._cuteOwning(address)

  def version(self) -> QTypeRevision:
    """
    Calls Qt's 'QTypeRevision QQmlType::version() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#version

    Returns
    -------

    QTypeRevision
      A new cute QTypeRevision around the copy Qt gave back. Python owns it.
    """
    #  QTypeRevision QQmlType::version() const
    address = self.uglySide.call('ritual_ZNK8QQmlType7versionEv')
    from ..QtCore import QTypeRevision
    return QTypeRevision._cuteOwning(address)

  @overload(QTypeRevision)
  def availableInVersion(self, version: QTypeRevision) -> bool:
    """
    Calls Qt's 'bool QQmlType::availableInVersion(QTypeRevision version)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#availableInVersion

    Parameters
    ----------

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.
    """
    #  bool QQmlType::availableInVersion(QTypeRevision version) const
    return self.uglySide.call(
        'ritual_ZNK8QQmlType18availableInVersionE13QTypeRevision',
        self._valueOf(version),
    )

  @overload(QHashedStringRef, QTypeRevision)
  def availableInVersion(
      self,
      module: QHashedStringRef,
      version: QTypeRevision,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlType::availableInVersion(const QHashedStringRef
    &module, QTypeRevision version) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#availableInVersion

    Parameters
    ----------

    module : QHashedStringRef
      Passed on as a value: Qt reads the C++ QHashedStringRef, which stays
      Python's own.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.
    """
    #  bool QQmlType::availableInVersion(const QHashedStringRef &module,
    #      QTypeRevision version) const
    return self.uglySide.call(
        'ritual_ZNK8QQmlType18availableInVersionERK16QHashedStringRef13QTyp'
        'eRevision',
        self._valueOf(module), self._valueOf(version),
    )

  def canConstructValueType(self) -> bool:
    """
    Calls Qt's 'bool QQmlType::canConstructValueType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltype.html#canConstructValueType
    """
    #  bool QQmlType::canConstructValueType() const
    return self.uglySide.call('ritual_ZNK8QQmlType21canConstructValueTypeEv')

  def canPopulateValueType(self) -> bool:
    """
    Calls Qt's 'bool QQmlType::canPopulateValueType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#canPopulateValueType
    """
    #  bool QQmlType::canPopulateValueType() const
    return self.uglySide.call('ritual_ZNK8QQmlType20canPopulateValueTypeEv')

  def create(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlType::create() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#create

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlType::create() const
    address = self.uglySide.call('ritual_ZNK8QQmlType6createEv')
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def createWithQQmlData(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlType::createWithQQmlData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#createWithQQmlData

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlType::createWithQQmlData() const
    address = self.uglySide.call('ritual_ZNK8QQmlType18createWithQQmlDataEv')
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def customParser(self) -> Optional[QQmlCustomParser]:
    """
    Calls Qt's 'QQmlCustomParser *QQmlType::customParser() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#customParser

    Returns
    -------

    Optional[QQmlCustomParser]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlCustomParser *QQmlType::customParser() const
    address = self.uglySide.call('ritual_ZNK8QQmlType12customParserEv')
    from . import QQmlCustomParser
    return QQmlCustomParser._cuteAt(address)

  def isCreatable(self) -> bool:
    """
    Calls Qt's 'bool QQmlType::isCreatable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#isCreatable
    """
    #  bool QQmlType::isCreatable() const
    return self.uglySide.call('ritual_ZNK8QQmlType11isCreatableEv')

  def extensionMetaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlType::extensionMetaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#extensionMetaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlType::extensionMetaObject() const
    address = self.uglySide.call(
        'ritual_ZNK8QQmlType19extensionMetaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isExtendedType(self) -> bool:
    """
    Calls Qt's 'bool QQmlType::isExtendedType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#isExtendedType
    """
    #  bool QQmlType::isExtendedType() const
    return self.uglySide.call('ritual_ZNK8QQmlType14isExtendedTypeEv')

  def noCreationReason(self) -> str:
    """
    Calls Qt's 'QString QQmlType::noCreationReason() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#noCreationReason

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlType::noCreationReason() const
    return self.uglySide.call('ritual_ZNK8QQmlType16noCreationReasonEv')

  def isSingleton(self) -> bool:
    """
    Calls Qt's 'bool QQmlType::isSingleton() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#isSingleton
    """
    #  bool QQmlType::isSingleton() const
    return self.uglySide.call('ritual_ZNK8QQmlType11isSingletonEv')

  def isInterface(self) -> bool:
    """
    Calls Qt's 'bool QQmlType::isInterface() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#isInterface
    """
    #  bool QQmlType::isInterface() const
    return self.uglySide.call('ritual_ZNK8QQmlType11isInterfaceEv')

  def isComposite(self) -> bool:
    """
    Calls Qt's 'bool QQmlType::isComposite() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#isComposite
    """
    #  bool QQmlType::isComposite() const
    return self.uglySide.call('ritual_ZNK8QQmlType11isCompositeEv')

  def isCompositeSingleton(self) -> bool:
    """
    Calls Qt's 'bool QQmlType::isCompositeSingleton() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#isCompositeSingleton
    """
    #  bool QQmlType::isCompositeSingleton() const
    return self.uglySide.call('ritual_ZNK8QQmlType20isCompositeSingletonEv')

  def isQObjectSingleton(self) -> bool:
    """
    Calls Qt's 'bool QQmlType::isQObjectSingleton() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#isQObjectSingleton
    """
    #  bool QQmlType::isQObjectSingleton() const
    return self.uglySide.call('ritual_ZNK8QQmlType18isQObjectSingletonEv')

  def isQJSValueSingleton(self) -> bool:
    """
    Calls Qt's 'bool QQmlType::isQJSValueSingleton() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#isQJSValueSingleton
    """
    #  bool QQmlType::isQJSValueSingleton() const
    return self.uglySide.call('ritual_ZNK8QQmlType19isQJSValueSingletonEv')

  def isSequentialContainer(self) -> bool:
    """
    Calls Qt's 'bool QQmlType::isSequentialContainer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltype.html#isSequentialContainer
    """
    #  bool QQmlType::isSequentialContainer() const
    return self.uglySide.call('ritual_ZNK8QQmlType21isSequentialContainerEv')

  def isValueType(self) -> bool:
    """
    Calls Qt's 'bool QQmlType::isValueType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#isValueType
    """
    #  bool QQmlType::isValueType() const
    return self.uglySide.call('ritual_ZNK8QQmlType11isValueTypeEv')

  def typeId(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QQmlType::typeId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#typeId

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QQmlType::typeId() const
    address = self.uglySide.call('ritual_ZNK8QQmlType6typeIdEv')
    from ..QtCore import QMetaType
    return QMetaType._cuteOwning(address)

  def qListTypeId(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QQmlType::qListTypeId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#qListTypeId

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QQmlType::qListTypeId() const
    address = self.uglySide.call('ritual_ZNK8QQmlType11qListTypeIdEv')
    from ..QtCore import QMetaType
    return QMetaType._cuteOwning(address)

  def listMetaSequence(self) -> QMetaSequence:
    """
    Calls Qt's 'QMetaSequence QQmlType::listMetaSequence() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#listMetaSequence

    Returns
    -------

    QMetaSequence
      A new cute QMetaSequence around the copy Qt gave back. Python owns it.
    """
    #  QMetaSequence QQmlType::listMetaSequence() const
    address = self.uglySide.call('ritual_ZNK8QQmlType16listMetaSequenceEv')
    from ..QtCore import QMetaSequence
    return QMetaSequence._cuteOwning(address)

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlType::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlType::metaObject() const
    address = self.uglySide.call('ritual_ZNK8QQmlType10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def metaObjectForValueType(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlType::metaObjectForValueType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltype.html#metaObjectForValueType

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlType::metaObjectForValueType() const
    address = self.uglySide.call(
        'ritual_ZNK8QQmlType22metaObjectForValueTypeEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def baseMetaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlType::baseMetaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#baseMetaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlType::baseMetaObject() const
    address = self.uglySide.call('ritual_ZNK8QQmlType14baseMetaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def metaObjectRevision(self) -> QTypeRevision:
    """
    Calls Qt's 'QTypeRevision QQmlType::metaObjectRevision() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#metaObjectRevision

    Returns
    -------

    QTypeRevision
      A new cute QTypeRevision around the copy Qt gave back. Python owns it.
    """
    #  QTypeRevision QQmlType::metaObjectRevision() const
    address = self.uglySide.call('ritual_ZNK8QQmlType18metaObjectRevisionEv')
    from ..QtCore import QTypeRevision
    return QTypeRevision._cuteOwning(address)

  def containsRevisionedAttributes(self) -> bool:
    """
    Calls Qt's 'bool QQmlType::containsRevisionedAttributes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltype.html#containsRevisionedAttributes
    """
    #  bool QQmlType::containsRevisionedAttributes() const
    return self.uglySide.call(
        'ritual_ZNK8QQmlType28containsRevisionedAttributesEv',
    )

  @overload(QQmlTypeLoader)
  @overload(NoneType)
  def attachedPropertiesType(
      self,
      typeLoader: Optional[QQmlTypeLoader],
  ) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQmlType::attachedPropertiesType(QQmlTypeLoader *typeLoader) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltype.html#attachedPropertiesType

    Parameters
    ----------

    typeLoader : Optional[QQmlTypeLoader]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlType::attachedPropertiesType(QQmlTypeLoader
    #      *typeLoader) const
    address = self.uglySide.call(
        'ritual_ZNK8QQmlType22attachedPropertiesTypeEP14QQmlTypeLoader',
        self._addressOf(typeLoader),
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def parserStatusCast(self) -> int:
    """
    Calls Qt's 'int QQmlType::parserStatusCast() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#parserStatusCast
    """
    #  int QQmlType::parserStatusCast() const
    return self.uglySide.call('ritual_ZNK8QQmlType16parserStatusCastEv')

  def interfaceIId(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QQmlType::interfaceIId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#interfaceIId

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QQmlType::interfaceIId() const
    chars = self.uglySide.call('ritual_ZNK8QQmlType12interfaceIIdEv')
    return None if chars is None else chars.decode()

  def propertyValueSourceCast(self) -> int:
    """
    Calls Qt's 'int QQmlType::propertyValueSourceCast() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltype.html#propertyValueSourceCast
    """
    #  int QQmlType::propertyValueSourceCast() const
    return self.uglySide.call(
        'ritual_ZNK8QQmlType23propertyValueSourceCastEv',
    )

  def propertyValueInterceptorCast(self) -> int:
    """
    Calls Qt's 'int QQmlType::propertyValueInterceptorCast() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltype.html#propertyValueInterceptorCast
    """
    #  int QQmlType::propertyValueInterceptorCast() const
    return self.uglySide.call(
        'ritual_ZNK8QQmlType28propertyValueInterceptorCastEv',
    )

  def finalizerCast(self) -> int:
    """
    Calls Qt's 'int QQmlType::finalizerCast() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#finalizerCast
    """
    #  int QQmlType::finalizerCast() const
    return self.uglySide.call('ritual_ZNK8QQmlType13finalizerCastEv')

  def index(self) -> int:
    """
    Calls Qt's 'int QQmlType::index() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#index
    """
    #  int QQmlType::index() const
    return self.uglySide.call('ritual_ZNK8QQmlType5indexEv')

  def isInlineComponentType(self) -> bool:
    """
    Calls Qt's 'bool QQmlType::isInlineComponentType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltype.html#isInlineComponentType
    """
    #  bool QQmlType::isInlineComponentType() const
    return self.uglySide.call('ritual_ZNK8QQmlType21isInlineComponentTypeEv')

  def sourceUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQmlType::sourceUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#sourceUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQmlType::sourceUrl() const
    address = self.uglySide.call('ritual_ZNK8QQmlType9sourceUrlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def priv(self) -> Optional[QQmlTypePrivate]:
    """
    Calls Qt's 'const QQmlTypePrivate *QQmlType::priv() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#priv

    Returns
    -------

    Optional[QQmlTypePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QQmlTypePrivate *QQmlType::priv() const
    address = self.uglySide.call('ritual_ZNK8QQmlType4privEv')
    from . import QQmlTypePrivate
    return QQmlTypePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, b: QQmlType) -> bool:
    """
    Calls Qt's 'bool operator==(const QQmlType &a, const QQmlType &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#operator==

    Parameters
    ----------

    b : QQmlType
      Passed on as a value: Qt reads the C++ QQmlType, which stays Python's
      own.
    """
    #  bool operator==(const QQmlType &a, const QQmlType &b)
    return Rituals.call(
        'ritual_ZeqRK8QQmlTypeS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, b: QQmlType) -> bool:
    """
    Calls Qt's 'bool operator!=(const QQmlType &a, const QQmlType &b)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#operator!=

    Parameters
    ----------

    b : QQmlType
      Passed on as a value: Qt reads the C++ QQmlType, which stays Python's
      own.
    """
    #  bool operator!=(const QQmlType &a, const QQmlType &b)
    return Rituals.call(
        'ritual_ZneRK8QQmlTypeS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(b),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QQmlType::QQmlType()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#QQmlType
    """
    #  QQmlType::QQmlType()
    self._noteCreation(QQmlType, lambda: Rituals.call(
        'ritual_ZN8QQmlTypeC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QQmlType) -> None:
    """
    Notes what was given, for Qt's 'QQmlType::QQmlType(const QQmlType
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#QQmlType

    Parameters
    ----------

    other : QQmlType
      Passed on as a value: Qt reads the C++ QQmlType, which stays Python's
      own.
    """
    #  QQmlType::QQmlType(const QQmlType &other)
    self._noteCreation(QQmlType, lambda: Rituals.call(
        'ritual_ZN8QQmlTypeC1ERKS_', self._valueOf(other),
    ))

  @overload(QQmlTypePrivate)
  @overload(NoneType)
  def __init__(self, priv: Optional[QQmlTypePrivate]) -> None:
    """
    Notes what was given, for Qt's 'QQmlType::QQmlType(const QQmlTypePrivate
    *priv)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#QQmlType

    Parameters
    ----------

    priv : Optional[QQmlTypePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlType::QQmlType(const QQmlTypePrivate *priv)
    self._noteCreation(QQmlType, lambda: Rituals.call(
        'ritual_ZN8QQmlTypeC1EPK15QQmlTypePrivate', self._addressOf(priv),
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
  def createProxy(self, instance: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlType::createProxy(QObject *instance) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltype.html#createProxy

    Parameters
    ----------

    instance : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlType::createProxy(QObject *instance) const
    self.uglySide.call(
        'ritual_ZNK8QQmlType11createProxyEP7QObject',
        self._addressOf(instance, 'QObject'),
    )

  @staticmethod
  def attachedPropertiesFunction(*__, **_) -> Never:
    """
    Qt's 'QQmlAttachedPropertiesFunc
    QQmlType::attachedPropertiesFunction(QQmlTypeLoader *typeLoader) const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlType.attachedPropertiesFunction' has no cute function yet. "
        "Qt's 'QQmlAttachedPropertiesFunc "
        "QQmlType::attachedPropertiesFunction(QQmlTypeLoader *typeLoader) "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def createFunction(*__, **_) -> Never:
    """
    Qt's 'CreateFunc QQmlType::createFunction() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlType.createFunction' has no cute function yet. Qt's "
        "'CreateFunc QQmlType::createFunction() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def createValueTypeFunction(*__, **_) -> Never:
    """
    Qt's 'CreateValueTypeFunc QQmlType::createValueTypeFunction() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlType.createValueTypeFunction' has no cute function yet. Qt's "
        "'CreateValueTypeFunc QQmlType::createValueTypeFunction() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def enumValue(*__, **_) -> Never:
    """
    - Qt's 'int QQmlType::enumValue(QQmlTypeLoader *typeLoader, const
      QHashedStringRef &a1, bool *ok) const': takes a number to change where
      it is.
    - Qt's 'int QQmlType::enumValue(QQmlTypeLoader *typeLoader, const
      QHashedCStringRef &a1, bool *ok) const': takes a number to change where
      it is.
    - Qt's 'int QQmlType::enumValue(QQmlTypeLoader *typeLoader, const
      QV4::String *a1, bool *ok) const': takes a number to change where it
      is.
    """
    raise NotImplementedError(
        "'QQmlType.enumValue' has no cute function yet. Qt's 'int "
        "QQmlType::enumValue(QQmlTypeLoader *typeLoader, const "
        "QHashedStringRef &a1, bool *ok) const': takes a number to change "
        "where it is. Qt's 'int QQmlType::enumValue(QQmlTypeLoader "
        "*typeLoader, const QHashedCStringRef &a1, bool *ok) const': takes "
        "a number to change where it is. Qt's 'int "
        "QQmlType::enumValue(QQmlTypeLoader *typeLoader, const QV4::String "
        "*a1, bool *ok) const': takes a number to change where it is.")

  @staticmethod
  def extensionFunction(*__, **_) -> Never:
    """
    Qt's 'ExtensionFunc QQmlType::extensionFunction() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlType.extensionFunction' has no cute function yet. Qt's "
        "'ExtensionFunc QQmlType::extensionFunction() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def scopedEnumIndex(*__, **_) -> Never:
    """
    - Qt's 'int QQmlType::scopedEnumIndex(QQmlTypeLoader *typeLoader, const
      QV4::String *a1, bool *ok) const': takes a number to change where it
      is.
    - Qt's 'int QQmlType::scopedEnumIndex(QQmlTypeLoader *typeLoader, const
      QString &a1, bool *ok) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQmlType.scopedEnumIndex' has no cute function yet. Qt's 'int "
        "QQmlType::scopedEnumIndex(QQmlTypeLoader *typeLoader, const "
        "QV4::String *a1, bool *ok) const': takes a number to change where "
        "it is. Qt's 'int QQmlType::scopedEnumIndex(QQmlTypeLoader "
        "*typeLoader, const QString &a1, bool *ok) const': takes a number "
        "to change where it is.")

  @staticmethod
  def scopedEnumKey(*__, **_) -> Never:
    """
    Qt's 'QString QQmlType::scopedEnumKey(QQmlTypeLoader *typeLoader, int
    index, int value, bool *ok) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQmlType.scopedEnumKey' has no cute function yet. Qt's 'QString "
        "QQmlType::scopedEnumKey(QQmlTypeLoader *typeLoader, int index, int "
        "value, bool *ok) const': takes a number to change where it is.")

  @staticmethod
  def scopedEnumKeys(*__, **_) -> Never:
    """
    Qt's 'QStringList QQmlType::scopedEnumKeys(QQmlTypeLoader *typeLoader,
    int index, int value, bool *ok) const': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QQmlType.scopedEnumKeys' has no cute function yet. Qt's "
        "'QStringList QQmlType::scopedEnumKeys(QQmlTypeLoader *typeLoader, "
        "int index, int value, bool *ok) const': takes a number to change "
        "where it is.")

  @staticmethod
  def scopedEnumValue(*__, **_) -> Never:
    """
    - Qt's 'int QQmlType::scopedEnumValue(QQmlTypeLoader *typeLoader, int
      index, const QV4::String *a2, bool *ok) const': takes a number to
      change where it is.
    - Qt's 'int QQmlType::scopedEnumValue(QQmlTypeLoader *typeLoader, int
      index, const QString &a2, bool *ok) const': takes a number to change
      where it is.
    - Qt's 'int QQmlType::scopedEnumValue(QQmlTypeLoader *typeLoader, const
      QHashedStringRef &a1, const QHashedStringRef &a2, bool *ok) const':
      takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQmlType.scopedEnumValue' has no cute function yet. Qt's 'int "
        "QQmlType::scopedEnumValue(QQmlTypeLoader *typeLoader, int index, "
        "const QV4::String *a2, bool *ok) const': takes a number to change "
        "where it is. Qt's 'int QQmlType::scopedEnumValue(QQmlTypeLoader "
        "*typeLoader, int index, const QString &a2, bool *ok) const': takes "
        "a number to change where it is. Qt's 'int "
        "QQmlType::scopedEnumValue(QQmlTypeLoader *typeLoader, const "
        "QHashedStringRef &a1, const QHashedStringRef &a2, bool *ok) "
        "const': takes a number to change where it is.")

  @staticmethod
  def singletonInstanceInfo(*__, **_) -> Never:
    """
    Qt's 'SingletonInstanceInfo::ConstPtr QQmlType::singletonInstanceInfo()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlType.singletonInstanceInfo' has no cute function yet. Qt's "
        "'SingletonInstanceInfo::ConstPtr QQmlType::singletonInstanceInfo() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def unscopedEnumIndex(*__, **_) -> Never:
    """
    - Qt's 'int QQmlType::unscopedEnumIndex(QQmlTypeLoader *typeLoader, const
      QV4::String *a1, bool *ok) const': takes a number to change where it
      is.
    - Qt's 'int QQmlType::unscopedEnumIndex(QQmlTypeLoader *typeLoader, const
      QString &a1, bool *ok) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQmlType.unscopedEnumIndex' has no cute function yet. Qt's 'int "
        "QQmlType::unscopedEnumIndex(QQmlTypeLoader *typeLoader, const "
        "QV4::String *a1, bool *ok) const': takes a number to change where "
        "it is. Qt's 'int QQmlType::unscopedEnumIndex(QQmlTypeLoader "
        "*typeLoader, const QString &a1, bool *ok) const': takes a number "
        "to change where it is.")

  @staticmethod
  def unscopedEnumKey(*__, **_) -> Never:
    """
    Qt's 'QString QQmlType::unscopedEnumKey(QQmlTypeLoader *typeLoader, int
    index, int value, bool *ok) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQmlType.unscopedEnumKey' has no cute function yet. Qt's 'QString "
        "QQmlType::unscopedEnumKey(QQmlTypeLoader *typeLoader, int index, "
        "int value, bool *ok) const': takes a number to change where it is.")

  @staticmethod
  def unscopedEnumKeys(*__, **_) -> Never:
    """
    Qt's 'QStringList QQmlType::unscopedEnumKeys(QQmlTypeLoader *typeLoader,
    int index, int value, bool *ok) const': takes a number to change where it
    is.
    """
    raise NotImplementedError(
        "'QQmlType.unscopedEnumKeys' has no cute function yet. Qt's "
        "'QStringList QQmlType::unscopedEnumKeys(QQmlTypeLoader "
        "*typeLoader, int index, int value, bool *ok) const': takes a "
        "number to change where it is.")

  @staticmethod
  def unscopedEnumValue(*__, **_) -> Never:
    """
    - Qt's 'int QQmlType::unscopedEnumValue(QQmlTypeLoader *typeLoader, int
      index, const QV4::String *a2, bool *ok) const': takes a number to
      change where it is.
    - Qt's 'int QQmlType::unscopedEnumValue(QQmlTypeLoader *typeLoader, int
      index, const QString &a2, bool *ok) const': takes a number to change
      where it is.
    - Qt's 'int QQmlType::unscopedEnumValue(QQmlTypeLoader *typeLoader, const
      QHashedStringRef &a1, const QHashedStringRef &a2, bool *ok) const':
      takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQmlType.unscopedEnumValue' has no cute function yet. Qt's 'int "
        "QQmlType::unscopedEnumValue(QQmlTypeLoader *typeLoader, int index, "
        "const QV4::String *a2, bool *ok) const': takes a number to change "
        "where it is. Qt's 'int QQmlType::unscopedEnumValue(QQmlTypeLoader "
        "*typeLoader, int index, const QString &a2, bool *ok) const': takes "
        "a number to change where it is. Qt's 'int "
        "QQmlType::unscopedEnumValue(QQmlTypeLoader *typeLoader, const "
        "QHashedStringRef &a1, const QHashedStringRef &a2, bool *ok) "
        "const': takes a number to change where it is.")


#  Qt's 'QList<QQmlType>': the list of QQmlType, which 'QList[QQmlType]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QQmlType.
QList.createKind(
    QQmlType, 'value',
    make='ritual_list_make_QQmlType',
    add='ritual_list_add_QQmlType',
    size='ritual_list_size_QQmlType',
    at='ritual_list_at_QQmlType',
    drop='ritual_list_drop_QQmlType',
)
