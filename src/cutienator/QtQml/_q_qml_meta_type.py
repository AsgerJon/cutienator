"""
QQmlMetaType binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlmetatype_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlMetaType to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList
from . import QQmlDirParser, QQmlPrivate, QQmlPropertyCache

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaMethod, QMetaObject, QMetaProperty, QMetaType
  from ..QtCore import QObject, QTypeRevision, QUrl
  from . import QHashedStringRef, QQmlMetaObject, QQmlType, QQmlTypeModule
  from . import QQmlTypePrivate, QQmlValueType
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHashedStringRef = WAIT['QHashedStringRef']
  QMetaObject = WAIT['QMetaObject']
  QMetaType = WAIT['QMetaType']
  QObject = WAIT['QObject']
  QQmlType = WAIT['QQmlType']
  QQmlTypePrivate = WAIT['QQmlTypePrivate']
  QTypeRevision = WAIT['QTypeRevision']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlMetaType(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlMetaType: a plain Python object standing in front
  of one C++ QQmlMetaType.

  C++ hands a QQmlMetaType around as a copy, so every C++ QQmlMetaType behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlMetaType that has a ritual and that Python can
  call so far, 53 names in all: 'inlineComponentUrl', 'equalBaseUrls',
  'normalizedUrl', 'registerType', 'registerInterface',
  'registerCompositeType', 'findOrCreateSpeculativeInlineComponentType',
  'unregisterType', 'registerMetaObjectForType', 'registerModule',
  'protectModule', 'registerModuleImport', 'unregisterModuleImport',
  'typeId', 'registerUndeletableType', 'qmlTypeNames', 'qmlTypes',
  'qmlSingletonTypes', 'qmlAllTypes', 'qmlType', 'qmlTypeById',
  'firstQmlTypeForAttachmentMetaObject', 'qmlListType', 'propertyCache',
  'rawMetaObjectForType', 'metaObjectForType', 'propertyCacheForType',
  'rawPropertyCacheForType', 'canConvert', 'freeUnusedTypesAndCaches',
  'defaultProperty', 'defaultMethod', 'listValueType', 'isInterface',
  'interfaceIId', 'isList', 'latestModuleVersion', 'isStronglyLockedModule',
  'matchingModuleVersion', 'typeModule', 'prettyTypeName',
  'registerTypeAlias', 'registerAutoParentFunction',
  'registerSequentialContainer', 'unregisterSequentialContainer',
  'registerUnitCacheHook', 'clearTypeRegistrations',
  'qmlRemoveModuleRegistration', 'qmlRegisterModuleTypes', 'isValueType',
  'valueType', 'metaObjectForValueType', 'findPropertyCacheInCompositeTypes'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlType QQmlMetaType::findCompositeType(const QUrl &url, const
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit,
    CompositeTypeLookupMode mode)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QQmlType QQmlMetaType::findOrCreateFactualInlineComponentType(const
    QUrl &url, const QQmlRefPointer<QV4::CompiledData::CompilationUnit>
    &compilationUnit)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlType QQmlMetaType::findOrCreateFactualInlineComponentType(const
    QUrl &baseUrl, const QString &name, const
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QQmlType QQmlMetaType::registerSingletonType(const
    QQmlPrivate::RegisterSingletonType &type, const
    QQmlType::SingletonInstanceInfo::ConstPtr &siinfo)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QQmlType QQmlMetaType::registerCompositeSingletonType(const
    QQmlPrivate::RegisterCompositeSingletonType &type, const
    QQmlType::SingletonInstanceInfo::ConstPtr &siinfo)': takes a type Python
    has no way to hand over yet.
  - Qt's 'RegistrationResult QQmlMetaType::registerPluginTypes(QObject
    *instance, const QString &basePath, const QString &uri, const QString
    &typeNamespace, QTypeRevision version, QList<QQmlError> *errors)': names
    'QList<QQmlError>', which has no cute class yet.
  - Qt's 'QQmlType QQmlMetaType::typeForUrl(const QUrl &url, const
    QHashedStringRef &typeName, CompositeTypeLookupMode mode,
    QList<QQmlError> *errors, QTypeRevision version)': names
    'QList<QQmlError>', which has no cute class yet.
  - Qt's 'QList<QQmlDirParser::Import> QQmlMetaType::moduleImports(const
    QString &uri, QTypeRevision version)': gives a type Python has no way to
    take yet.
  - Qt's 'QObject *QQmlMetaType::toQObject(const QVariant &a0, bool *ok)':
    takes a number to change where it is.
  - Qt's 'QQmlAttachedPropertiesFunc
    QQmlMetaType::attachedPropertiesFunc(QQmlTypeLoader *typeLoader, const
    QMetaObject *a1)': gives a type Python has no way to take yet.
  - Qt's 'QList<QQmlPrivate::AutoParentFunction>
    QQmlMetaType::parentFunctions()': gives a type Python has no way to take
    yet.
  - Qt's 'const QQmlPrivate::CachedQmlUnit
    *QQmlMetaType::findCachedCompilationUnit(const QUrl &uri, CacheMode mode,
    CachedUnitLookupError *status)': names
    'QQmlMetaType::CachedUnitLookupError', which has no cute class yet.
  - Qt's 'void QQmlMetaType::prependCachedUnitLookupFunction(QQmlPrivate::
    QmlUnitCacheLookupFunction handler)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QQmlMetaType::removeCachedUnitLookupFunction(QQmlPrivate::
    QmlUnitCacheLookupFunction handler)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QQmlMetaType::removeFromInlineComponents(QSet<QUrl>
    &container, const QQmlTypePrivate *reference)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void QQmlMetaType::unregisterAutoParentFunction(const
    QQmlPrivate::AutoParentFunction &function)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QList<QQmlProxyMetaObject::ProxyData> QQmlMetaType::proxyData(const
    QMetaObject *mo, const QMetaObject *baseMetaObject, QMetaObject
    *lastMetaObject)': gives a type Python has no way to take yet.
  - Qt's 'void QQmlMetaType::clone(QMetaObjectBuilder &builder, const
    QMetaObject *mo, const QMetaObject *ignoreStart, const QMetaObject
    *ignoreEnd, ClonePolicy policy)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QQmlMetaType::qmlInsertModuleRegistration(const QString &uri,
    void (*)() registerFunction)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QQmlMetaType::registerInternalCompositeType(const
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlMetaType::unregisterInternalCompositeType(const
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlMetaType::deepClearCompositeType(const
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> &oldUnit)': takes a
    type Python has no way to hand over yet.
  - Qt's 'int QQmlMetaType::countInternalCompositeTypeSelfReferences(const
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QQmlMetaType::~QQmlMetaType()': the destructor: Python removes its
    C++ QQmlMetaType by it, and has no other use for it.

  What has no ritual
  ------------------

  4 of the 93 functions Qt declares: 2 a template; 2 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ QQmlMetaType is created at the first use, not by
    'QQmlMetaType(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlMetaType back gives a copy the ritual made for
    Python, in a new cute QQmlMetaType.
  - Each name of Qt's QQmlMetaType that has no cute function yet,
    'attachedPropertiesFunc', 'clone',
    'countInternalCompositeTypeSelfReferences', 'deepClearCompositeType',
    'findCachedCompilationUnit', 'findCompositeType',
    'findOrCreateFactualInlineComponentType', 'moduleImports',
    'obtainCompilationUnit', 'parentFunctions',
    'prependCachedUnitLookupFunction', 'proxyData',
    'qmlInsertModuleRegistration', 'registerCompositeSingletonType',
    'registerInternalCompositeType', 'registerPluginTypes',
    'registerSingletonType', 'removeCachedUnitLookupFunction',
    'removeFromInlineComponents', 'removeQQmlTypePrivate', 'toQObject',
    'typeForUrl', 'unregisterAutoParentFunction',
    'unregisterInternalCompositeType', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlMetaType, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class CacheMode(CuteNum):
    """
    The enum 'QQmlMetaType::CacheMode' of Qt, with the 3 names Qt gives in
    it.
    """

    RejectAll = Kee[int](0)
    AcceptUntyped = Kee[int](1)
    RequireFullyTyped = Kee[int](2)

  class CachedUnitLookupError(CuteNum, scoped=True):
    """
    The enum 'QQmlMetaType::CachedUnitLookupError' of Qt, with the 4 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    NoError = Kee[int](0)
    NoUnitFound = Kee[int](1)
    VersionMismatch = Kee[int](2)
    NotFullyTyped = Kee[int](3)

  class ClonePolicy(CuteNum):
    """
    The enum 'QQmlMetaType::ClonePolicy' of Qt, with the 2 names Qt gives in
    it.
    """

    CloneAll = Kee[int](0)
    CloneEnumsOnly = Kee[int](1)

  class CompositeTypeLookupMode(CuteNum):
    """
    The enum 'QQmlMetaType::CompositeTypeLookupMode' of Qt, with the 3 names
    Qt gives in it.
    """

    NonSingleton = Kee[int](0)
    Singleton = Kee[int](1)
    JavaScript = Kee[int](2)

  class RegistrationResult(CuteNum, scoped=True):
    """
    The enum 'QQmlMetaType::RegistrationResult' of Qt, with the 3 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Success = Kee[int](0)
    Failure = Kee[int](1)
    NoRegistrationFunction = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QUrl, str)
  def inlineComponentUrl(baseUrl: QUrl, name: str) -> QUrl:
    """
    Calls Qt's 'QUrl QQmlMetaType::inlineComponentUrl(const QUrl &baseUrl,
    const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html#inlineComponentUrl

    Parameters
    ----------

    baseUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQmlMetaType::inlineComponentUrl(const QUrl &baseUrl, const
    #      QString &name)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType18inlineComponentUrlERK4QUrlRK7QString',
        CuteMixin._valueOf(baseUrl), name,
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @staticmethod
  @overload(QUrl, QUrl)
  def equalBaseUrls(aUrl: QUrl, bUrl: QUrl) -> bool:
    """
    Calls Qt's 'bool QQmlMetaType::equalBaseUrls(const QUrl &aUrl, const QUrl
    &bUrl)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#equalBaseUrls

    Parameters
    ----------

    aUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    bUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QQmlMetaType::equalBaseUrls(const QUrl &aUrl, const QUrl &bUrl)
    return Rituals.call(
        'ritual_ZN12QQmlMetaType13equalBaseUrlsERK4QUrlS2_',
        CuteMixin._valueOf(aUrl), CuteMixin._valueOf(bUrl),
    )

  @staticmethod
  @overload(QUrl)
  def normalizedUrl(unNormalizedUrl: QUrl) -> QUrl:
    """
    Calls Qt's 'QUrl QQmlMetaType::normalizedUrl(const QUrl
    &unNormalizedUrl)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#normalizedUrl

    Parameters
    ----------

    unNormalizedUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQmlMetaType::normalizedUrl(const QUrl &unNormalizedUrl)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType13normalizedUrlERK4QUrl',
        CuteMixin._valueOf(unNormalizedUrl),
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  @staticmethod
  @overload(WAIT['QQmlPrivate.RegisterType'])
  def registerType(type: QQmlPrivate.RegisterType) -> QQmlType:
    """
    Calls Qt's 'QQmlType QQmlMetaType::registerType(const
    QQmlPrivate::RegisterType &type)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#registerType

    Parameters
    ----------

    type : QQmlPrivate.RegisterType
      Passed on as a value: Qt reads the C++ QQmlPrivate::RegisterType, which
      stays Python's own.

    Returns
    -------

    QQmlType
      A new cute QQmlType around the copy Qt gave back. Python owns it.
    """
    #  QQmlType QQmlMetaType::registerType(const QQmlPrivate::RegisterType
    #      &type)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType12registerTypeERKN11QQmlPrivate12RegisterTy'
        'peE',
        CuteMixin._valueOf(type),
    )
    from . import QQmlType
    return QQmlType._cuteOwning(address)

  @staticmethod
  @overload(WAIT['QQmlPrivate.RegisterInterface'])
  def registerInterface(type: QQmlPrivate.RegisterInterface) -> QQmlType:
    """
    Calls Qt's 'QQmlType QQmlMetaType::registerInterface(const
    QQmlPrivate::RegisterInterface &type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html#registerInterface

    Parameters
    ----------

    type : QQmlPrivate.RegisterInterface
      Passed on as a value: Qt reads the C++ QQmlPrivate::RegisterInterface,
      which stays Python's own.

    Returns
    -------

    QQmlType
      A new cute QQmlType around the copy Qt gave back. Python owns it.
    """
    #  QQmlType QQmlMetaType::registerInterface(const
    #      QQmlPrivate::RegisterInterface &type)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType17registerInterfaceERKN11QQmlPrivate17Regis'
        'terInterfaceE',
        CuteMixin._valueOf(type),
    )
    from . import QQmlType
    return QQmlType._cuteOwning(address)

  @staticmethod
  @overload(WAIT['QQmlPrivate.RegisterCompositeType'])
  def registerCompositeType(
      type: QQmlPrivate.RegisterCompositeType,
  ) -> QQmlType:
    """
    Calls Qt's 'QQmlType QQmlMetaType::registerCompositeType(const
    QQmlPrivate::RegisterCompositeType &type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html#registerCompositeType

    Parameters
    ----------

    type : QQmlPrivate.RegisterCompositeType
      Passed on as a value: Qt reads the C++
      QQmlPrivate::RegisterCompositeType, which stays Python's own.

    Returns
    -------

    QQmlType
      A new cute QQmlType around the copy Qt gave back. Python owns it.
    """
    #  QQmlType QQmlMetaType::registerCompositeType(const
    #      QQmlPrivate::RegisterCompositeType &type)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType21registerCompositeTypeERKN11QQmlPrivate21R'
        'egisterCompositeTypeE',
        CuteMixin._valueOf(type),
    )
    from . import QQmlType
    return QQmlType._cuteOwning(address)

  @staticmethod
  @overload(QUrl)
  def findOrCreateSpeculativeInlineComponentType(url: QUrl) -> QQmlType:
    """
    Calls Qt's 'QQmlType
    QQmlMetaType::findOrCreateSpeculativeInlineComponentType(const QUrl
    &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QQmlType
      A new cute QQmlType around the copy Qt gave back. Python owns it.
    """
    #  QQmlType
    #      QQmlMetaType::findOrCreateSpeculativeInlineComponentType(const
    #      QUrl &url)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType42findOrCreateSpeculativeInlineComponentTyp'
        'eERK4QUrl',
        CuteMixin._valueOf(url),
    )
    from . import QQmlType
    return QQmlType._cuteOwning(address)

  @staticmethod
  @overload(QQmlType, str)
  def findOrCreateSpeculativeInlineComponentType(
      outerType: QQmlType,
      name: str,
  ) -> QQmlType:
    """
    Calls Qt's 'QQmlType
    QQmlMetaType::findOrCreateSpeculativeInlineComponentType(const QQmlType
    &outerType, const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html

    Parameters
    ----------

    outerType : QQmlType
      Passed on as a value: Qt reads the C++ QQmlType, which stays Python's
      own.

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QQmlType
      A new cute QQmlType around the copy Qt gave back. Python owns it.
    """
    #  QQmlType
    #      QQmlMetaType::findOrCreateSpeculativeInlineComponentType(const
    #      QQmlType &outerType, const QString &name)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType42findOrCreateSpeculativeInlineComponentTyp'
        'eERK8QQmlTypeRK7QString',
        CuteMixin._valueOf(outerType), name,
    )
    from . import QQmlType
    return QQmlType._cuteOwning(address)

  @staticmethod
  @overload(int)
  def unregisterType(type: int) -> None:
    """
    Calls Qt's 'void QQmlMetaType::unregisterType(int type)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#unregisterType

    Parameters
    ----------

    type : int
      Passed on as it is.
    """
    #  void QQmlMetaType::unregisterType(int type)
    Rituals.call('ritual_ZN12QQmlMetaType14unregisterTypeEi', type)

  @staticmethod
  @overload(QMetaObject, QQmlTypePrivate)
  @overload(QMetaObject, NoneType)
  @overload(NoneType, QQmlTypePrivate)
  @overload(NoneType, NoneType)
  def registerMetaObjectForType(
      metaobject: Optional[QMetaObject],
      type: Optional[QQmlTypePrivate],
  ) -> None:
    """
    Calls Qt's 'void QQmlMetaType::registerMetaObjectForType(const
    QMetaObject *metaobject, const QQmlTypePrivate *type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html#registerMetaObjectForType

    Parameters
    ----------

    metaobject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : Optional[QQmlTypePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlMetaType::registerMetaObjectForType(const QMetaObject
    #      *metaobject, const QQmlTypePrivate *type)
    Rituals.call(
        'ritual_ZN12QQmlMetaType25registerMetaObjectForTypeEPK11QMetaObject'
        'PK15QQmlTypePrivate',
        CuteMixin._addressOf(metaobject, 'QMetaObject'),
        CuteMixin._addressOf(type),
    )

  @staticmethod
  @overload(str, QTypeRevision)
  @overload(NoneType, QTypeRevision)
  def registerModule(uri: Optional[str], version: QTypeRevision) -> None:
    """
    Calls Qt's 'void QQmlMetaType::registerModule(const char *uri,
    QTypeRevision version)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#registerModule

    Parameters
    ----------

    uri : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.
    """
    #  void QQmlMetaType::registerModule(const char *uri, QTypeRevision
    #      version)
    Rituals.call(
        'ritual_ZN12QQmlMetaType14registerModuleEPKc13QTypeRevision',
        CuteMixin._bytesOf(uri), CuteMixin._valueOf(version),
    )

  @staticmethod
  @overload(str, QTypeRevision)
  @overload(str, QTypeRevision, bool)
  def protectModule(
      uri: str,
      version: QTypeRevision,
      weakProtectAllVersions: bool = False,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlMetaType::protectModule(const QString &uri,
    QTypeRevision version, bool weakProtectAllVersions)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#protectModule

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.

    weakProtectAllVersions : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  bool QQmlMetaType::protectModule(const QString &uri, QTypeRevision
    #      version, bool weakProtectAllVersions)
    return Rituals.call(
        'ritual_ZN12QQmlMetaType13protectModuleERK7QString13QTypeRevisionb',
        uri, CuteMixin._valueOf(version), weakProtectAllVersions,
    )

  @staticmethod
  @overload(str, QTypeRevision, QQmlDirParser.Import)
  def registerModuleImport(
      uri: str,
      version: QTypeRevision,
      import_: QQmlDirParser.Import,
  ) -> None:
    """
    Calls Qt's 'void QQmlMetaType::registerModuleImport(const QString &uri,
    QTypeRevision version, const QQmlDirParser::Import &import)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html#registerModuleImport

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.

    import_ : QQmlDirParser.Import
      Passed on as a value: Qt reads the C++ QQmlDirParser::Import, which
      stays Python's own.
    """
    #  void QQmlMetaType::registerModuleImport(const QString &uri,
    #      QTypeRevision version, const QQmlDirParser::Import &import)
    Rituals.call(
        'ritual_ZN12QQmlMetaType20registerModuleImportERK7QString13QTypeRev'
        'isionRKN13QQmlDirParser6ImportE',
        uri, CuteMixin._valueOf(version), CuteMixin._valueOf(import_),
    )

  @staticmethod
  @overload(str, QTypeRevision, QQmlDirParser.Import)
  def unregisterModuleImport(
      uri: str,
      version: QTypeRevision,
      import_: QQmlDirParser.Import,
  ) -> None:
    """
    Calls Qt's 'void QQmlMetaType::unregisterModuleImport(const QString &uri,
    QTypeRevision version, const QQmlDirParser::Import &import)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html#unregisterModuleImport

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.

    import_ : QQmlDirParser.Import
      Passed on as a value: Qt reads the C++ QQmlDirParser::Import, which
      stays Python's own.
    """
    #  void QQmlMetaType::unregisterModuleImport(const QString &uri,
    #      QTypeRevision version, const QQmlDirParser::Import &import)
    Rituals.call(
        'ritual_ZN12QQmlMetaType22unregisterModuleImportERK7QString13QTypeR'
        'evisionRKN13QQmlDirParser6ImportE',
        uri, CuteMixin._valueOf(version), CuteMixin._valueOf(import_),
    )

  @staticmethod
  @overload(str, QTypeRevision, str)
  @overload(str, QTypeRevision, NoneType)
  @overload(NoneType, QTypeRevision, str)
  @overload(NoneType, QTypeRevision, NoneType)
  def typeId(
      uri: Optional[str],
      version: QTypeRevision,
      qmlName: Optional[str],
  ) -> int:
    """
    Calls Qt's 'int QQmlMetaType::typeId(const char *uri, QTypeRevision
    version, const char *qmlName)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#typeId

    Parameters
    ----------

    uri : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.

    qmlName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  int QQmlMetaType::typeId(const char *uri, QTypeRevision version, const
    #      char *qmlName)
    return Rituals.call(
        'ritual_ZN12QQmlMetaType6typeIdEPKc13QTypeRevisionS1_',
        CuteMixin._bytesOf(uri), CuteMixin._valueOf(version),
        CuteMixin._bytesOf(qmlName),
    )

  @staticmethod
  @overload(QQmlType)
  def registerUndeletableType(dtype: QQmlType) -> None:
    """
    Calls Qt's 'void QQmlMetaType::registerUndeletableType(const QQmlType
    &dtype)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html#registerUndeletableType

    Parameters
    ----------

    dtype : QQmlType
      Passed on as a value: Qt reads the C++ QQmlType, which stays Python's
      own.
    """
    #  void QQmlMetaType::registerUndeletableType(const QQmlType &dtype)
    Rituals.call(
        'ritual_ZN12QQmlMetaType23registerUndeletableTypeERK8QQmlType',
        CuteMixin._valueOf(dtype),
    )

  @staticmethod
  def qmlTypeNames() -> QStringList:
    """
    Calls Qt's 'QList<QString> QQmlMetaType::qmlTypeNames()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#qmlTypeNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QString> QQmlMetaType::qmlTypeNames()
    address = Rituals.call('ritual_ZN12QQmlMetaType12qmlTypeNamesEv')
    return QStringList._cuteOwning(address)

  @staticmethod
  def qmlTypes() -> QList[QQmlType]:
    """
    Calls Qt's 'QList<QQmlType> QQmlMetaType::qmlTypes()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#qmlTypes

    Returns
    -------

    QList[QQmlType]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQmlType> QQmlMetaType::qmlTypes()
    address = Rituals.call('ritual_ZN12QQmlMetaType8qmlTypesEv')
    from . import QQmlType
    return QList[QQmlType]._cuteOwning(address)

  @staticmethod
  def qmlSingletonTypes() -> QList[QQmlType]:
    """
    Calls Qt's 'QList<QQmlType> QQmlMetaType::qmlSingletonTypes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html#qmlSingletonTypes

    Returns
    -------

    QList[QQmlType]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQmlType> QQmlMetaType::qmlSingletonTypes()
    address = Rituals.call('ritual_ZN12QQmlMetaType17qmlSingletonTypesEv')
    from . import QQmlType
    return QList[QQmlType]._cuteOwning(address)

  @staticmethod
  def qmlAllTypes() -> QList[QQmlType]:
    """
    Calls Qt's 'QList<QQmlType> QQmlMetaType::qmlAllTypes()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#qmlAllTypes

    Returns
    -------

    QList[QQmlType]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQmlType> QQmlMetaType::qmlAllTypes()
    address = Rituals.call('ritual_ZN12QQmlMetaType11qmlAllTypesEv')
    from . import QQmlType
    return QList[QQmlType]._cuteOwning(address)

  @staticmethod
  @overload(str, QTypeRevision)
  def qmlType(qualifiedName: str, version: QTypeRevision) -> QQmlType:
    """
    Calls Qt's 'QQmlType QQmlMetaType::qmlType(const QString &qualifiedName,
    QTypeRevision version)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#qmlType

    Parameters
    ----------

    qualifiedName : str
      Passed on as it is: a QString is made of it for the call.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.

    Returns
    -------

    QQmlType
      A new cute QQmlType around the copy Qt gave back. Python owns it.
    """
    #  QQmlType QQmlMetaType::qmlType(const QString &qualifiedName,
    #      QTypeRevision version)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType7qmlTypeERK7QString13QTypeRevision',
        qualifiedName, CuteMixin._valueOf(version),
    )
    from . import QQmlType
    return QQmlType._cuteOwning(address)

  @staticmethod
  @overload(QHashedStringRef, QHashedStringRef, QTypeRevision)
  def qmlType(
      name: QHashedStringRef,
      module: QHashedStringRef,
      version: QTypeRevision,
  ) -> QQmlType:
    """
    Calls Qt's 'QQmlType QQmlMetaType::qmlType(const QHashedStringRef &name,
    const QHashedStringRef &module, QTypeRevision version)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#qmlType

    Parameters
    ----------

    name : QHashedStringRef
      Passed on as a value: Qt reads the C++ QHashedStringRef, which stays
      Python's own.

    module : QHashedStringRef
      Passed on as a value: Qt reads the C++ QHashedStringRef, which stays
      Python's own.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.

    Returns
    -------

    QQmlType
      A new cute QQmlType around the copy Qt gave back. Python owns it.
    """
    #  QQmlType QQmlMetaType::qmlType(const QHashedStringRef &name, const
    #      QHashedStringRef &module, QTypeRevision version)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType7qmlTypeERK16QHashedStringRefS2_13QTypeRevi'
        'sion',
        CuteMixin._valueOf(name), CuteMixin._valueOf(module),
        CuteMixin._valueOf(version),
    )
    from . import QQmlType
    return QQmlType._cuteOwning(address)

  @staticmethod
  @overload(QMetaObject)
  @overload(NoneType)
  def qmlType(a0: Optional[QMetaObject]) -> QQmlType:
    """
    Calls Qt's 'QQmlType QQmlMetaType::qmlType(const QMetaObject *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#qmlType

    Parameters
    ----------

    a0 : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QQmlType
      A new cute QQmlType around the copy Qt gave back. Python owns it.
    """
    #  QQmlType QQmlMetaType::qmlType(const QMetaObject *a0)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType7qmlTypeEPK11QMetaObject',
        CuteMixin._addressOf(a0, 'QMetaObject'),
    )
    from . import QQmlType
    return QQmlType._cuteOwning(address)

  @staticmethod
  @overload(QMetaObject, QHashedStringRef, QTypeRevision)
  @overload(NoneType, QHashedStringRef, QTypeRevision)
  def qmlType(
      metaObject: Optional[QMetaObject],
      module: QHashedStringRef,
      version: QTypeRevision,
  ) -> QQmlType:
    """
    Calls Qt's 'QQmlType QQmlMetaType::qmlType(const QMetaObject *metaObject,
    const QHashedStringRef &module, QTypeRevision version)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#qmlType

    Parameters
    ----------

    metaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    module : QHashedStringRef
      Passed on as a value: Qt reads the C++ QHashedStringRef, which stays
      Python's own.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.

    Returns
    -------

    QQmlType
      A new cute QQmlType around the copy Qt gave back. Python owns it.
    """
    #  QQmlType QQmlMetaType::qmlType(const QMetaObject *metaObject, const
    #      QHashedStringRef &module, QTypeRevision version)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType7qmlTypeEPK11QMetaObjectRK16QHashedStringRe'
        'f13QTypeRevision',
        CuteMixin._addressOf(metaObject, 'QMetaObject'),
        CuteMixin._valueOf(module), CuteMixin._valueOf(version),
    )
    from . import QQmlType
    return QQmlType._cuteOwning(address)

  @staticmethod
  @overload(QMetaType)
  def qmlType(metaType: QMetaType) -> QQmlType:
    """
    Calls Qt's 'QQmlType QQmlMetaType::qmlType(QMetaType metaType)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#qmlType

    Parameters
    ----------

    metaType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    Returns
    -------

    QQmlType
      A new cute QQmlType around the copy Qt gave back. Python owns it.
    """
    #  QQmlType QQmlMetaType::qmlType(QMetaType metaType)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType7qmlTypeE9QMetaType',
        CuteMixin._valueOf(metaType),
    )
    from . import QQmlType
    return QQmlType._cuteOwning(address)

  @staticmethod
  @overload(QUrl)
  def qmlType(unNormalizedUrl: QUrl) -> QQmlType:
    """
    Calls Qt's 'QQmlType QQmlMetaType::qmlType(const QUrl &unNormalizedUrl)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#qmlType

    Parameters
    ----------

    unNormalizedUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QQmlType
      A new cute QQmlType around the copy Qt gave back. Python owns it.
    """
    #  QQmlType QQmlMetaType::qmlType(const QUrl &unNormalizedUrl)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType7qmlTypeERK4QUrl',
        CuteMixin._valueOf(unNormalizedUrl),
    )
    from . import QQmlType
    return QQmlType._cuteOwning(address)

  @staticmethod
  @overload(int)
  def qmlTypeById(qmlTypeId: int) -> QQmlType:
    """
    Calls Qt's 'QQmlType QQmlMetaType::qmlTypeById(int qmlTypeId)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#qmlTypeById

    Parameters
    ----------

    qmlTypeId : int
      Passed on as it is.

    Returns
    -------

    QQmlType
      A new cute QQmlType around the copy Qt gave back. Python owns it.
    """
    #  QQmlType QQmlMetaType::qmlTypeById(int qmlTypeId)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType11qmlTypeByIdEi', qmlTypeId,
    )
    from . import QQmlType
    return QQmlType._cuteOwning(address)

  @staticmethod
  @overload(QMetaObject)
  @overload(NoneType)
  def firstQmlTypeForAttachmentMetaObject(
      attachmentMetaObject: Optional[QMetaObject],
  ) -> QQmlType:
    """
    Calls Qt's 'QQmlType
    QQmlMetaType::firstQmlTypeForAttachmentMetaObject(const QMetaObject
    *attachmentMetaObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html

    Parameters
    ----------

    attachmentMetaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QQmlType
      A new cute QQmlType around the copy Qt gave back. Python owns it.
    """
    #  QQmlType QQmlMetaType::firstQmlTypeForAttachmentMetaObject(const
    #      QMetaObject *attachmentMetaObject)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType35firstQmlTypeForAttachmentMetaObjectEPK11Q'
        'MetaObject',
        CuteMixin._addressOf(attachmentMetaObject, 'QMetaObject'),
    )
    from . import QQmlType
    return QQmlType._cuteOwning(address)

  @staticmethod
  @overload(QMetaType)
  def qmlListType(metaType: QMetaType) -> QQmlType:
    """
    Calls Qt's 'QQmlType QQmlMetaType::qmlListType(QMetaType metaType)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#qmlListType

    Parameters
    ----------

    metaType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    Returns
    -------

    QQmlType
      A new cute QQmlType around the copy Qt gave back. Python owns it.
    """
    #  QQmlType QQmlMetaType::qmlListType(QMetaType metaType)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType11qmlListTypeE9QMetaType',
        CuteMixin._valueOf(metaType),
    )
    from . import QQmlType
    return QQmlType._cuteOwning(address)

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  @overload(QObject, QTypeRevision)
  @overload(NoneType, QTypeRevision)
  def propertyCache(
      object: Optional[QObject],
      version: Optional[QTypeRevision] = None,
  ) -> QQmlPropertyCache.ConstPtr:
    """
    Calls Qt's 'QQmlPropertyCache::ConstPtr
    QQmlMetaType::propertyCache(QObject *object, QTypeRevision version)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#propertyCache

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    version : Optional[QTypeRevision]
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own. May be left out, as in Qt: a new 'QTypeRevision()' is
      then passed on.

    Returns
    -------

    QQmlPropertyCache.ConstPtr
      A new cute QQmlPropertyCache::ConstPtr around the copy Qt gave back.
      Python owns it.
    """
    #  QQmlPropertyCache::ConstPtr QQmlMetaType::propertyCache(QObject
    #      *object, QTypeRevision version)
    if version is None:
      from ..QtCore import QTypeRevision
      version = QTypeRevision()
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType13propertyCacheEP7QObject13QTypeRevision',
        CuteMixin._addressOf(object, 'QObject'), CuteMixin._valueOf(version),
    )
    return QQmlPropertyCache.ConstPtr._cuteOwning(address)

  @staticmethod
  @overload(QMetaObject)
  @overload(QMetaObject, QTypeRevision)
  def propertyCache(
      metaObject: Optional[QMetaObject],
      version: Optional[QTypeRevision] = None,
  ) -> QQmlPropertyCache.ConstPtr:
    """
    Calls Qt's 'QQmlPropertyCache::ConstPtr QQmlMetaType::propertyCache(const
    QMetaObject *metaObject, QTypeRevision version)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#propertyCache

    Parameters
    ----------

    metaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    version : Optional[QTypeRevision]
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own. May be left out, as in Qt: a new 'QTypeRevision()' is
      then passed on.

    Returns
    -------

    QQmlPropertyCache.ConstPtr
      A new cute QQmlPropertyCache::ConstPtr around the copy Qt gave back.
      Python owns it.
    """
    #  QQmlPropertyCache::ConstPtr QQmlMetaType::propertyCache(const
    #      QMetaObject *metaObject, QTypeRevision version)
    if version is None:
      from ..QtCore import QTypeRevision
      version = QTypeRevision()
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType13propertyCacheEPK11QMetaObject13QTypeRevis'
        'ion',
        CuteMixin._addressOf(metaObject, 'QMetaObject'),
        CuteMixin._valueOf(version),
    )
    return QQmlPropertyCache.ConstPtr._cuteOwning(address)

  @staticmethod
  @overload(QQmlType, QTypeRevision)
  def propertyCache(
      type: QQmlType,
      version: QTypeRevision,
  ) -> QQmlPropertyCache.ConstPtr:
    """
    Calls Qt's 'QQmlPropertyCache::ConstPtr QQmlMetaType::propertyCache(const
    QQmlType &type, QTypeRevision version)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#propertyCache

    Parameters
    ----------

    type : QQmlType
      Passed on as a value: Qt reads the C++ QQmlType, which stays Python's
      own.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.

    Returns
    -------

    QQmlPropertyCache.ConstPtr
      A new cute QQmlPropertyCache::ConstPtr around the copy Qt gave back.
      Python owns it.
    """
    #  QQmlPropertyCache::ConstPtr QQmlMetaType::propertyCache(const QQmlType
    #      &type, QTypeRevision version)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType13propertyCacheERK8QQmlType13QTypeRevision',
        CuteMixin._valueOf(type), CuteMixin._valueOf(version),
    )
    return QQmlPropertyCache.ConstPtr._cuteOwning(address)

  @staticmethod
  @overload(QMetaType)
  def rawMetaObjectForType(metaType: QMetaType) -> QQmlMetaObject:
    """
    Calls Qt's 'QQmlMetaObject QQmlMetaType::rawMetaObjectForType(QMetaType
    metaType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html#rawMetaObjectForType

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
    #  QQmlMetaObject QQmlMetaType::rawMetaObjectForType(QMetaType metaType)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType20rawMetaObjectForTypeE9QMetaType',
        CuteMixin._valueOf(metaType),
    )
    from . import QQmlMetaObject
    return QQmlMetaObject._cuteOwning(address)

  @staticmethod
  @overload(QMetaType)
  def metaObjectForType(metaType: QMetaType) -> QQmlMetaObject:
    """
    Calls Qt's 'QQmlMetaObject QQmlMetaType::metaObjectForType(QMetaType
    metaType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html#metaObjectForType

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
    #  QQmlMetaObject QQmlMetaType::metaObjectForType(QMetaType metaType)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType17metaObjectForTypeE9QMetaType',
        CuteMixin._valueOf(metaType),
    )
    from . import QQmlMetaObject
    return QQmlMetaObject._cuteOwning(address)

  @staticmethod
  @overload(QMetaType)
  def propertyCacheForType(
      metaType: QMetaType,
  ) -> QQmlPropertyCache.ConstPtr:
    """
    Calls Qt's 'QQmlPropertyCache::ConstPtr
    QQmlMetaType::propertyCacheForType(QMetaType metaType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html#propertyCacheForType

    Parameters
    ----------

    metaType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    Returns
    -------

    QQmlPropertyCache.ConstPtr
      A new cute QQmlPropertyCache::ConstPtr around the copy Qt gave back.
      Python owns it.
    """
    #  QQmlPropertyCache::ConstPtr
    #      QQmlMetaType::propertyCacheForType(QMetaType metaType)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType20propertyCacheForTypeE9QMetaType',
        CuteMixin._valueOf(metaType),
    )
    return QQmlPropertyCache.ConstPtr._cuteOwning(address)

  @staticmethod
  @overload(QMetaType)
  def rawPropertyCacheForType(
      metaType: QMetaType,
  ) -> QQmlPropertyCache.ConstPtr:
    """
    Calls Qt's 'QQmlPropertyCache::ConstPtr
    QQmlMetaType::rawPropertyCacheForType(QMetaType metaType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html#rawPropertyCacheForType

    Parameters
    ----------

    metaType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    Returns
    -------

    QQmlPropertyCache.ConstPtr
      A new cute QQmlPropertyCache::ConstPtr around the copy Qt gave back.
      Python owns it.
    """
    #  QQmlPropertyCache::ConstPtr
    #      QQmlMetaType::rawPropertyCacheForType(QMetaType metaType)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType23rawPropertyCacheForTypeE9QMetaType',
        CuteMixin._valueOf(metaType),
    )
    return QQmlPropertyCache.ConstPtr._cuteOwning(address)

  @staticmethod
  @overload(QMetaType, QTypeRevision)
  def rawPropertyCacheForType(
      metaType: QMetaType,
      version: QTypeRevision,
  ) -> QQmlPropertyCache.ConstPtr:
    """
    Calls Qt's 'QQmlPropertyCache::ConstPtr
    QQmlMetaType::rawPropertyCacheForType(QMetaType metaType, QTypeRevision
    version)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html#rawPropertyCacheForType

    Parameters
    ----------

    metaType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.

    Returns
    -------

    QQmlPropertyCache.ConstPtr
      A new cute QQmlPropertyCache::ConstPtr around the copy Qt gave back.
      Python owns it.
    """
    #  QQmlPropertyCache::ConstPtr
    #      QQmlMetaType::rawPropertyCacheForType(QMetaType metaType,
    #      QTypeRevision version)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType23rawPropertyCacheForTypeE9QMetaType13QType'
        'Revision',
        CuteMixin._valueOf(metaType), CuteMixin._valueOf(version),
    )
    return QQmlPropertyCache.ConstPtr._cuteOwning(address)

  @staticmethod
  @overload(QObject, QMetaType)
  @overload(NoneType, QMetaType)
  def canConvert(o: Optional[QObject], metaType: QMetaType) -> bool:
    """
    Calls Qt's 'bool QQmlMetaType::canConvert(QObject *o, QMetaType
    metaType)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#canConvert

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    metaType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  bool QQmlMetaType::canConvert(QObject *o, QMetaType metaType)
    return Rituals.call(
        'ritual_ZN12QQmlMetaType10canConvertEP7QObject9QMetaType',
        CuteMixin._addressOf(o, 'QObject'), CuteMixin._valueOf(metaType),
    )

  @staticmethod
  @overload(QQmlPropertyCache.ConstPtr, QMetaType)
  def canConvert(
      from_: QQmlPropertyCache.ConstPtr,
      metaType: QMetaType,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlMetaType::canConvert(const
    QQmlPropertyCache::ConstPtr &from, QMetaType metaType)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#canConvert

    Parameters
    ----------

    from_ : QQmlPropertyCache.ConstPtr
      Passed on as a value: Qt reads the C++ QQmlPropertyCache::ConstPtr,
      which stays Python's own.

    metaType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  bool QQmlMetaType::canConvert(const QQmlPropertyCache::ConstPtr &from,
    #      QMetaType metaType)
    return Rituals.call(
        'ritual_ZN12QQmlMetaType10canConvertERKN17QQmlPropertyCache8ConstPt'
        'rE9QMetaType',
        CuteMixin._valueOf(from_), CuteMixin._valueOf(metaType),
    )

  @staticmethod
  def freeUnusedTypesAndCaches() -> None:
    """
    Calls Qt's 'void QQmlMetaType::freeUnusedTypesAndCaches()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html#freeUnusedTypesAndCaches
    """
    #  void QQmlMetaType::freeUnusedTypesAndCaches()
    Rituals.call('ritual_ZN12QQmlMetaType24freeUnusedTypesAndCachesEv')

  @staticmethod
  @overload(QMetaObject)
  @overload(NoneType)
  def defaultProperty(a0: Optional[QMetaObject]) -> QMetaProperty:
    """
    Calls Qt's 'QMetaProperty QQmlMetaType::defaultProperty(const QMetaObject
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#defaultProperty

    Parameters
    ----------

    a0 : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QMetaProperty
      A new cute QMetaProperty around the copy Qt gave back. Python owns it.
    """
    #  QMetaProperty QQmlMetaType::defaultProperty(const QMetaObject *a0)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType15defaultPropertyEPK11QMetaObject',
        CuteMixin._addressOf(a0, 'QMetaObject'),
    )
    from ..QtCore import QMetaProperty
    return QMetaProperty._cuteOwning(address)

  @staticmethod
  @overload(QObject)
  def defaultProperty(a0: Optional[QObject]) -> QMetaProperty:
    """
    Calls Qt's 'QMetaProperty QQmlMetaType::defaultProperty(QObject *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#defaultProperty

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QMetaProperty
      A new cute QMetaProperty around the copy Qt gave back. Python owns it.
    """
    #  QMetaProperty QQmlMetaType::defaultProperty(QObject *a0)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType15defaultPropertyEP7QObject',
        CuteMixin._addressOf(a0, 'QObject'),
    )
    from ..QtCore import QMetaProperty
    return QMetaProperty._cuteOwning(address)

  @staticmethod
  @overload(QMetaObject)
  @overload(NoneType)
  def defaultMethod(a0: Optional[QMetaObject]) -> QMetaMethod:
    """
    Calls Qt's 'QMetaMethod QQmlMetaType::defaultMethod(const QMetaObject
    *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#defaultMethod

    Parameters
    ----------

    a0 : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QMetaMethod
      A new cute QMetaMethod around the copy Qt gave back. Python owns it.
    """
    #  QMetaMethod QQmlMetaType::defaultMethod(const QMetaObject *a0)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType13defaultMethodEPK11QMetaObject',
        CuteMixin._addressOf(a0, 'QMetaObject'),
    )
    from ..QtCore import QMetaMethod
    return QMetaMethod._cuteOwning(address)

  @staticmethod
  @overload(QObject)
  def defaultMethod(a0: Optional[QObject]) -> QMetaMethod:
    """
    Calls Qt's 'QMetaMethod QQmlMetaType::defaultMethod(QObject *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#defaultMethod

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QMetaMethod
      A new cute QMetaMethod around the copy Qt gave back. Python owns it.
    """
    #  QMetaMethod QQmlMetaType::defaultMethod(QObject *a0)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType13defaultMethodEP7QObject',
        CuteMixin._addressOf(a0, 'QObject'),
    )
    from ..QtCore import QMetaMethod
    return QMetaMethod._cuteOwning(address)

  @staticmethod
  @overload(QMetaType)
  def listValueType(type: QMetaType) -> QMetaType:
    """
    Calls Qt's 'QMetaType QQmlMetaType::listValueType(QMetaType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#listValueType

    Parameters
    ----------

    type : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QQmlMetaType::listValueType(QMetaType type)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType13listValueTypeE9QMetaType',
        CuteMixin._valueOf(type),
    )
    from ..QtCore import QMetaType
    return QMetaType._cuteOwning(address)

  @staticmethod
  @overload(QMetaType)
  def isInterface(type: QMetaType) -> bool:
    """
    Calls Qt's 'bool QQmlMetaType::isInterface(QMetaType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#isInterface

    Parameters
    ----------

    type : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  bool QQmlMetaType::isInterface(QMetaType type)
    return Rituals.call(
        'ritual_ZN12QQmlMetaType11isInterfaceE9QMetaType',
        CuteMixin._valueOf(type),
    )

  @staticmethod
  @overload(QMetaType)
  def interfaceIId(type: QMetaType) -> Optional[str]:
    """
    Calls Qt's 'const char *QQmlMetaType::interfaceIId(QMetaType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#interfaceIId

    Parameters
    ----------

    type : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QQmlMetaType::interfaceIId(QMetaType type)
    chars = Rituals.call(
        'ritual_ZN12QQmlMetaType12interfaceIIdE9QMetaType',
        CuteMixin._valueOf(type),
    )
    return None if chars is None else chars.decode()

  @staticmethod
  @overload(QMetaType)
  def isList(type: QMetaType) -> bool:
    """
    Calls Qt's 'bool QQmlMetaType::isList(QMetaType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#isList

    Parameters
    ----------

    type : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  bool QQmlMetaType::isList(QMetaType type)
    return Rituals.call(
        'ritual_ZN12QQmlMetaType6isListE9QMetaType',
        CuteMixin._valueOf(type),
    )

  @staticmethod
  @overload(str)
  def latestModuleVersion(uri: str) -> QTypeRevision:
    """
    Calls Qt's 'QTypeRevision QQmlMetaType::latestModuleVersion(const QString
    &uri)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html#latestModuleVersion

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QTypeRevision
      A new cute QTypeRevision around the copy Qt gave back. Python owns it.
    """
    #  QTypeRevision QQmlMetaType::latestModuleVersion(const QString &uri)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType19latestModuleVersionERK7QString', uri,
    )
    from ..QtCore import QTypeRevision
    return QTypeRevision._cuteOwning(address)

  @staticmethod
  @overload(str, QTypeRevision)
  def isStronglyLockedModule(uri: str, version: QTypeRevision) -> bool:
    """
    Calls Qt's 'bool QQmlMetaType::isStronglyLockedModule(const QString &uri,
    QTypeRevision version)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html#isStronglyLockedModule

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.
    """
    #  bool QQmlMetaType::isStronglyLockedModule(const QString &uri,
    #      QTypeRevision version)
    return Rituals.call(
        'ritual_ZN12QQmlMetaType22isStronglyLockedModuleERK7QString13QTypeR'
        'evision',
        uri, CuteMixin._valueOf(version),
    )

  @staticmethod
  @overload(str, QTypeRevision)
  def matchingModuleVersion(
      module: str,
      version: QTypeRevision,
  ) -> QTypeRevision:
    """
    Calls Qt's 'QTypeRevision QQmlMetaType::matchingModuleVersion(const
    QString &module, QTypeRevision version)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html#matchingModuleVersion

    Parameters
    ----------

    module : str
      Passed on as it is: a QString is made of it for the call.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.

    Returns
    -------

    QTypeRevision
      A new cute QTypeRevision around the copy Qt gave back. Python owns it.
    """
    #  QTypeRevision QQmlMetaType::matchingModuleVersion(const QString
    #      &module, QTypeRevision version)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType21matchingModuleVersionERK7QString13QTypeRe'
        'vision',
        module, CuteMixin._valueOf(version),
    )
    from ..QtCore import QTypeRevision
    return QTypeRevision._cuteOwning(address)

  @staticmethod
  @overload(str, QTypeRevision)
  def typeModule(
      uri: str,
      version: QTypeRevision,
  ) -> Optional[QQmlTypeModule]:
    """
    Calls Qt's 'QQmlTypeModule *QQmlMetaType::typeModule(const QString &uri,
    QTypeRevision version)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#typeModule

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.

    version : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.

    Returns
    -------

    Optional[QQmlTypeModule]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlTypeModule *QQmlMetaType::typeModule(const QString &uri,
    #      QTypeRevision version)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType10typeModuleERK7QString13QTypeRevision',
        uri, CuteMixin._valueOf(version),
    )
    from . import QQmlTypeModule
    return QQmlTypeModule._cuteAt(address)

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def prettyTypeName(object: Optional[QObject]) -> str:
    """
    Calls Qt's 'QString QQmlMetaType::prettyTypeName(const QObject *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#prettyTypeName

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlMetaType::prettyTypeName(const QObject *object)
    return Rituals.call(
        'ritual_ZN12QQmlMetaType14prettyTypeNameEPK7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )

  @staticmethod
  @overload(int, str)
  def registerTypeAlias(typeId: int, name: str) -> None:
    """
    Calls Qt's 'void QQmlMetaType::registerTypeAlias(int typeId, const
    QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html#registerTypeAlias

    Parameters
    ----------

    typeId : int
      Passed on as it is.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlMetaType::registerTypeAlias(int typeId, const QString &name)
    Rituals.call(
        'ritual_ZN12QQmlMetaType17registerTypeAliasEiRK7QString',
        typeId, name,
    )

  @staticmethod
  @overload(WAIT['QQmlPrivate.RegisterAutoParent'])
  def registerAutoParentFunction(
      autoparent: QQmlPrivate.RegisterAutoParent,
  ) -> int:
    """
    Calls Qt's 'int QQmlMetaType::registerAutoParentFunction(const
    QQmlPrivate::RegisterAutoParent &autoparent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html#registerAutoParentFunction

    Parameters
    ----------

    autoparent : QQmlPrivate.RegisterAutoParent
      Passed on as a value: Qt reads the C++ QQmlPrivate::RegisterAutoParent,
      which stays Python's own.
    """
    #  int QQmlMetaType::registerAutoParentFunction(const
    #      QQmlPrivate::RegisterAutoParent &autoparent)
    return Rituals.call(
        'ritual_ZN12QQmlMetaType26registerAutoParentFunctionERKN11QQmlPriva'
        'te18RegisterAutoParentE',
        CuteMixin._valueOf(autoparent),
    )

  @staticmethod
  @overload(WAIT['QQmlPrivate.RegisterSequentialContainer'])
  def registerSequentialContainer(
      sequenceRegistration: QQmlPrivate.RegisterSequentialContainer,
  ) -> QQmlType:
    """
    Calls Qt's 'QQmlType QQmlMetaType::registerSequentialContainer(const
    QQmlPrivate::RegisterSequentialContainer &sequenceRegistration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html#registerSequentialContainer

    Parameters
    ----------

    sequenceRegistration : QQmlPrivate.RegisterSequentialContainer
      Passed on as a value: Qt reads the C++
      QQmlPrivate::RegisterSequentialContainer, which stays Python's own.

    Returns
    -------

    QQmlType
      A new cute QQmlType around the copy Qt gave back. Python owns it.
    """
    #  QQmlType QQmlMetaType::registerSequentialContainer(const
    #      QQmlPrivate::RegisterSequentialContainer &sequenceRegistration)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType27registerSequentialContainerERKN11QQmlPriv'
        'ate27RegisterSequentialContainerE',
        CuteMixin._valueOf(sequenceRegistration),
    )
    from . import QQmlType
    return QQmlType._cuteOwning(address)

  @staticmethod
  @overload(int)
  def unregisterSequentialContainer(id: int) -> None:
    """
    Calls Qt's 'void QQmlMetaType::unregisterSequentialContainer(int id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html#unregisterSequentialContainer

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QQmlMetaType::unregisterSequentialContainer(int id)
    Rituals.call(
        'ritual_ZN12QQmlMetaType29unregisterSequentialContainerEi', id,
    )

  @staticmethod
  @overload(WAIT['QQmlPrivate.RegisterQmlUnitCacheHook'])
  def registerUnitCacheHook(
      hookRegistration: QQmlPrivate.RegisterQmlUnitCacheHook,
  ) -> int:
    """
    Calls Qt's 'int QQmlMetaType::registerUnitCacheHook(const
    QQmlPrivate::RegisterQmlUnitCacheHook &hookRegistration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html#registerUnitCacheHook

    Parameters
    ----------

    hookRegistration : QQmlPrivate.RegisterQmlUnitCacheHook
      Passed on as a value: Qt reads the C++
      QQmlPrivate::RegisterQmlUnitCacheHook, which stays Python's own.
    """
    #  int QQmlMetaType::registerUnitCacheHook(const
    #      QQmlPrivate::RegisterQmlUnitCacheHook &hookRegistration)
    return Rituals.call(
        'ritual_ZN12QQmlMetaType21registerUnitCacheHookERKN11QQmlPrivate24R'
        'egisterQmlUnitCacheHookE',
        CuteMixin._valueOf(hookRegistration),
    )

  @staticmethod
  def clearTypeRegistrations() -> None:
    """
    Calls Qt's 'void QQmlMetaType::clearTypeRegistrations()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html#clearTypeRegistrations
    """
    #  void QQmlMetaType::clearTypeRegistrations()
    Rituals.call('ritual_ZN12QQmlMetaType22clearTypeRegistrationsEv')

  @staticmethod
  @overload(str)
  def qmlRemoveModuleRegistration(uri: str) -> None:
    """
    Calls Qt's 'void QQmlMetaType::qmlRemoveModuleRegistration(const QString
    &uri)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html#qmlRemoveModuleRegistration

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlMetaType::qmlRemoveModuleRegistration(const QString &uri)
    Rituals.call(
        'ritual_ZN12QQmlMetaType27qmlRemoveModuleRegistrationERK7QString',
        uri,
    )

  @staticmethod
  @overload(str)
  def qmlRegisterModuleTypes(uri: str) -> bool:
    """
    Calls Qt's 'bool QQmlMetaType::qmlRegisterModuleTypes(const QString
    &uri)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html#qmlRegisterModuleTypes

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlMetaType::qmlRegisterModuleTypes(const QString &uri)
    return Rituals.call(
        'ritual_ZN12QQmlMetaType22qmlRegisterModuleTypesERK7QString', uri,
    )

  @staticmethod
  @overload(QMetaType)
  def isValueType(type: QMetaType) -> bool:
    """
    Calls Qt's 'bool QQmlMetaType::isValueType(QMetaType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#isValueType

    Parameters
    ----------

    type : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  bool QQmlMetaType::isValueType(QMetaType type)
    return Rituals.call(
        'ritual_ZN12QQmlMetaType11isValueTypeE9QMetaType',
        CuteMixin._valueOf(type),
    )

  @staticmethod
  @overload(QMetaType)
  def valueType(metaType: QMetaType) -> Optional[QQmlValueType]:
    """
    Calls Qt's 'QQmlValueType *QQmlMetaType::valueType(QMetaType metaType)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetatype.html#valueType

    Parameters
    ----------

    metaType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    Returns
    -------

    Optional[QQmlValueType]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlValueType *QQmlMetaType::valueType(QMetaType metaType)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType9valueTypeE9QMetaType',
        CuteMixin._valueOf(metaType),
    )
    from . import QQmlValueType
    return QQmlValueType._cuteAt(address)

  @staticmethod
  @overload(QMetaType)
  def metaObjectForValueType(type: QMetaType) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQmlMetaType::metaObjectForValueType(QMetaType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html#metaObjectForValueType

    Parameters
    ----------

    type : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlMetaType::metaObjectForValueType(QMetaType
    #      type)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType22metaObjectForValueTypeE9QMetaType',
        CuteMixin._valueOf(type),
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @staticmethod
  @overload(QMetaType)
  def findPropertyCacheInCompositeTypes(
      t: QMetaType,
  ) -> QQmlPropertyCache.ConstPtr:
    """
    Calls Qt's 'QQmlPropertyCache::ConstPtr
    QQmlMetaType::findPropertyCacheInCompositeTypes(QMetaType t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetatype.html

    Parameters
    ----------

    t : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    Returns
    -------

    QQmlPropertyCache.ConstPtr
      A new cute QQmlPropertyCache::ConstPtr around the copy Qt gave back.
      Python owns it.
    """
    #  QQmlPropertyCache::ConstPtr
    #      QQmlMetaType::findPropertyCacheInCompositeTypes(QMetaType t)
    address = Rituals.call(
        'ritual_ZN12QQmlMetaType33findPropertyCacheInCompositeTypesE9QMetaT'
        'ype',
        CuteMixin._valueOf(t),
    )
    return QQmlPropertyCache.ConstPtr._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlMetaType'

  #  Qt's '~QQmlMetaType()'. Naming it makes this a value class: Python owns
  #  every C++ QQmlMetaType behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QQmlMetaTypeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @staticmethod
  def attachedPropertiesFunc(*__, **_) -> Never:
    """
    Qt's 'QQmlAttachedPropertiesFunc
    QQmlMetaType::attachedPropertiesFunc(QQmlTypeLoader *typeLoader, const
    QMetaObject *a1)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlMetaType.attachedPropertiesFunc' has no cute function yet. "
        "Qt's 'QQmlAttachedPropertiesFunc "
        "QQmlMetaType::attachedPropertiesFunc(QQmlTypeLoader *typeLoader, "
        "const QMetaObject *a1)': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def clone(*__, **_) -> Never:
    """
    Qt's 'void QQmlMetaType::clone(QMetaObjectBuilder &builder, const
    QMetaObject *mo, const QMetaObject *ignoreStart, const QMetaObject
    *ignoreEnd, ClonePolicy policy)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQmlMetaType.clone' has no cute function yet. Qt's 'void "
        "QQmlMetaType::clone(QMetaObjectBuilder &builder, const QMetaObject "
        "*mo, const QMetaObject *ignoreStart, const QMetaObject *ignoreEnd, "
        "ClonePolicy policy)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def countInternalCompositeTypeSelfReferences(*__, **_) -> Never:
    """
    Qt's 'int QQmlMetaType::countInternalCompositeTypeSelfReferences(const
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlMetaType.countInternalCompositeTypeSelfReferences' has no "
        "cute function yet. Qt's 'int "
        "QQmlMetaType::countInternalCompositeTypeSelfReferences(const "
        "QQmlRefPointer<QV4::CompiledData::CompilationUnit> "
        "&compilationUnit)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def deepClearCompositeType(*__, **_) -> Never:
    """
    Qt's 'void QQmlMetaType::deepClearCompositeType(const
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> &oldUnit)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlMetaType.deepClearCompositeType' has no cute function yet. "
        "Qt's 'void QQmlMetaType::deepClearCompositeType(const "
        "QQmlRefPointer<QV4::CompiledData::CompilationUnit> &oldUnit)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def findCachedCompilationUnit(*__, **_) -> Never:
    """
    Qt's 'const QQmlPrivate::CachedQmlUnit
    *QQmlMetaType::findCachedCompilationUnit(const QUrl &uri, CacheMode mode,
    CachedUnitLookupError *status)': names
    'QQmlMetaType::CachedUnitLookupError', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlMetaType.findCachedCompilationUnit' has no cute function yet. "
        "Qt's 'const QQmlPrivate::CachedQmlUnit "
        "*QQmlMetaType::findCachedCompilationUnit(const QUrl &uri, "
        "CacheMode mode, CachedUnitLookupError *status)': names "
        "'QQmlMetaType::CachedUnitLookupError', which has no cute class yet."
    )

  @staticmethod
  def findCompositeType(*__, **_) -> Never:
    """
    Qt's 'QQmlType QQmlMetaType::findCompositeType(const QUrl &url, const
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit,
    CompositeTypeLookupMode mode)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQmlMetaType.findCompositeType' has no cute function yet. Qt's "
        "'QQmlType QQmlMetaType::findCompositeType(const QUrl &url, const "
        "QQmlRefPointer<QV4::CompiledData::CompilationUnit> "
        "&compilationUnit, CompositeTypeLookupMode mode)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def findOrCreateFactualInlineComponentType(*__, **_) -> Never:
    """
    - Qt's 'QQmlType
      QQmlMetaType::findOrCreateFactualInlineComponentType(const QUrl &url,
      const QQmlRefPointer<QV4::CompiledData::CompilationUnit>
      &compilationUnit)': takes a type Python has no way to hand over yet.
    - Qt's 'QQmlType
      QQmlMetaType::findOrCreateFactualInlineComponentType(const QUrl
      &baseUrl, const QString &name, const
      QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit)':
      takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlMetaType.findOrCreateFactualInlineComponentType' has no cute "
        "function yet. Qt's 'QQmlType "
        "QQmlMetaType::findOrCreateFactualInlineComponentType(const QUrl "
        "&url, const QQmlRefPointer<QV4::CompiledData::CompilationUnit> "
        "&compilationUnit)': takes a type Python has no way to hand over "
        "yet. Qt's 'QQmlType "
        "QQmlMetaType::findOrCreateFactualInlineComponentType(const QUrl "
        "&baseUrl, const QString &name, const "
        "QQmlRefPointer<QV4::CompiledData::CompilationUnit> "
        "&compilationUnit)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def moduleImports(*__, **_) -> Never:
    """
    Qt's 'QList<QQmlDirParser::Import> QQmlMetaType::moduleImports(const
    QString &uri, QTypeRevision version)': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QQmlMetaType.moduleImports' has no cute function yet. Qt's "
        "'QList<QQmlDirParser::Import> QQmlMetaType::moduleImports(const "
        "QString &uri, QTypeRevision version)': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def obtainCompilationUnit(*__, **_) -> Never:
    """
    - Qt's 'QQmlRefPointer<QV4::CompiledData::CompilationUnit>
      QQmlMetaType::obtainCompilationUnit(QMetaType type)': the compiler
      refuses its ritual as it would be written here: member access into
      incomplete type 'QV4::CompiledData::CompilationUnit'.
    - Qt's 'QQmlRefPointer<QV4::CompiledData::CompilationUnit>
      QQmlMetaType::obtainCompilationUnit(const QUrl &url)': the compiler
      refuses its ritual as it would be written here: member access into
      incomplete type 'QV4::CompiledData::CompilationUnit'.
    """
    raise NotImplementedError(
        "'QQmlMetaType.obtainCompilationUnit' has no cute function yet. "
        "Qt's 'QQmlRefPointer<QV4::CompiledData::CompilationUnit> "
        "QQmlMetaType::obtainCompilationUnit(QMetaType type)': the compiler "
        "refuses its ritual as it would be written here: member access into "
        "incomplete type 'QV4::CompiledData::CompilationUnit'. Qt's "
        "'QQmlRefPointer<QV4::CompiledData::CompilationUnit> "
        "QQmlMetaType::obtainCompilationUnit(const QUrl &url)': the "
        "compiler refuses its ritual as it would be written here: member "
        "access into incomplete type 'QV4::CompiledData::CompilationUnit'.")

  @staticmethod
  def parentFunctions(*__, **_) -> Never:
    """
    Qt's 'QList<QQmlPrivate::AutoParentFunction>
    QQmlMetaType::parentFunctions()': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QQmlMetaType.parentFunctions' has no cute function yet. Qt's "
        "'QList<QQmlPrivate::AutoParentFunction> "
        "QQmlMetaType::parentFunctions()': gives a type Python has no way "
        "to take yet.")

  @staticmethod
  def prependCachedUnitLookupFunction(*__, **_) -> Never:
    """
    Qt's 'void QQmlMetaType::prependCachedUnitLookupFunction(QQmlPrivate::
    QmlUnitCacheLookupFunction handler)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlMetaType.prependCachedUnitLookupFunction' has no cute "
        "function yet. Qt's 'void "
        "QQmlMetaType::prependCachedUnitLookupFunction(QQmlPrivate::QmlUnitC"
        "acheLookupFunction handler)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def proxyData(*__, **_) -> Never:
    """
    Qt's 'QList<QQmlProxyMetaObject::ProxyData> QQmlMetaType::proxyData(const
    QMetaObject *mo, const QMetaObject *baseMetaObject, QMetaObject
    *lastMetaObject)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlMetaType.proxyData' has no cute function yet. Qt's "
        "'QList<QQmlProxyMetaObject::ProxyData> "
        "QQmlMetaType::proxyData(const QMetaObject *mo, const QMetaObject "
        "*baseMetaObject, QMetaObject *lastMetaObject)': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def qmlInsertModuleRegistration(*__, **_) -> Never:
    """
    Qt's 'void QQmlMetaType::qmlInsertModuleRegistration(const QString &uri,
    void (*)() registerFunction)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQmlMetaType.qmlInsertModuleRegistration' has no cute function "
        "yet. Qt's 'void QQmlMetaType::qmlInsertModuleRegistration(const "
        "QString &uri, void (*)() registerFunction)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def registerCompositeSingletonType(*__, **_) -> Never:
    """
    Qt's 'QQmlType QQmlMetaType::registerCompositeSingletonType(const
    QQmlPrivate::RegisterCompositeSingletonType &type, const
    QQmlType::SingletonInstanceInfo::ConstPtr &siinfo)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlMetaType.registerCompositeSingletonType' has no cute function "
        "yet. Qt's 'QQmlType "
        "QQmlMetaType::registerCompositeSingletonType(const "
        "QQmlPrivate::RegisterCompositeSingletonType &type, const "
        "QQmlType::SingletonInstanceInfo::ConstPtr &siinfo)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def registerInternalCompositeType(*__, **_) -> Never:
    """
    Qt's 'void QQmlMetaType::registerInternalCompositeType(const
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlMetaType.registerInternalCompositeType' has no cute function "
        "yet. Qt's 'void QQmlMetaType::registerInternalCompositeType(const "
        "QQmlRefPointer<QV4::CompiledData::CompilationUnit> "
        "&compilationUnit)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def registerPluginTypes(*__, **_) -> Never:
    """
    Qt's 'RegistrationResult QQmlMetaType::registerPluginTypes(QObject
    *instance, const QString &basePath, const QString &uri, const QString
    &typeNamespace, QTypeRevision version, QList<QQmlError> *errors)': names
    'QList<QQmlError>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlMetaType.registerPluginTypes' has no cute function yet. Qt's "
        "'RegistrationResult QQmlMetaType::registerPluginTypes(QObject "
        "*instance, const QString &basePath, const QString &uri, const "
        "QString &typeNamespace, QTypeRevision version, QList<QQmlError> "
        "*errors)': names 'QList<QQmlError>', which has no cute class yet.")

  @staticmethod
  def registerSingletonType(*__, **_) -> Never:
    """
    Qt's 'QQmlType QQmlMetaType::registerSingletonType(const
    QQmlPrivate::RegisterSingletonType &type, const
    QQmlType::SingletonInstanceInfo::ConstPtr &siinfo)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlMetaType.registerSingletonType' has no cute function yet. "
        "Qt's 'QQmlType QQmlMetaType::registerSingletonType(const "
        "QQmlPrivate::RegisterSingletonType &type, const "
        "QQmlType::SingletonInstanceInfo::ConstPtr &siinfo)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def removeCachedUnitLookupFunction(*__, **_) -> Never:
    """
    Qt's 'void QQmlMetaType::removeCachedUnitLookupFunction(QQmlPrivate::
    QmlUnitCacheLookupFunction handler)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlMetaType.removeCachedUnitLookupFunction' has no cute function "
        "yet. Qt's 'void "
        "QQmlMetaType::removeCachedUnitLookupFunction(QQmlPrivate::QmlUnitCa"
        "cheLookupFunction handler)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def removeFromInlineComponents(*__, **_) -> Never:
    """
    - Qt's 'void QQmlMetaType::removeFromInlineComponents(QSet<QUrl>
      &container, const QQmlTypePrivate *reference)': takes a type Python has
      no way to hand over yet.
    - Qt's 'QQmlMetaType::removeFromInlineComponents': a template: a pattern
      and no single function.
    """
    raise NotImplementedError(
        "'QQmlMetaType.removeFromInlineComponents' has no cute function "
        "yet. Qt's 'void "
        "QQmlMetaType::removeFromInlineComponents(QSet<QUrl> &container, "
        "const QQmlTypePrivate *reference)': takes a type Python has no way "
        "to hand over yet. Qt's 'QQmlMetaType::removeFromInlineComponents': "
        "a template: a pattern and no single function.")

  @staticmethod
  def removeQQmlTypePrivate(*__, **_) -> Never:
    """
    Qt's 'QQmlMetaType::removeQQmlTypePrivate': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QQmlMetaType.removeQQmlTypePrivate' has no cute function yet. "
        "Qt's 'QQmlMetaType::removeQQmlTypePrivate': a template: a pattern "
        "and no single function.")

  @staticmethod
  def toQObject(*__, **_) -> Never:
    """
    Qt's 'QObject *QQmlMetaType::toQObject(const QVariant &a0, bool *ok)':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQmlMetaType.toQObject' has no cute function yet. Qt's 'QObject "
        "*QQmlMetaType::toQObject(const QVariant &a0, bool *ok)': takes a "
        "number to change where it is.")

  @staticmethod
  def typeForUrl(*__, **_) -> Never:
    """
    Qt's 'QQmlType QQmlMetaType::typeForUrl(const QUrl &url, const
    QHashedStringRef &typeName, CompositeTypeLookupMode mode,
    QList<QQmlError> *errors, QTypeRevision version)': names
    'QList<QQmlError>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlMetaType.typeForUrl' has no cute function yet. Qt's 'QQmlType "
        "QQmlMetaType::typeForUrl(const QUrl &url, const QHashedStringRef "
        "&typeName, CompositeTypeLookupMode mode, QList<QQmlError> *errors, "
        "QTypeRevision version)': names 'QList<QQmlError>', which has no "
        "cute class yet.")

  @staticmethod
  def unregisterAutoParentFunction(*__, **_) -> Never:
    """
    Qt's 'void QQmlMetaType::unregisterAutoParentFunction(const
    QQmlPrivate::AutoParentFunction &function)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlMetaType.unregisterAutoParentFunction' has no cute function "
        "yet. Qt's 'void QQmlMetaType::unregisterAutoParentFunction(const "
        "QQmlPrivate::AutoParentFunction &function)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def unregisterInternalCompositeType(*__, **_) -> Never:
    """
    Qt's 'void QQmlMetaType::unregisterInternalCompositeType(const
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> &compilationUnit)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlMetaType.unregisterInternalCompositeType' has no cute "
        "function yet. Qt's 'void "
        "QQmlMetaType::unregisterInternalCompositeType(const "
        "QQmlRefPointer<QV4::CompiledData::CompilationUnit> "
        "&compilationUnit)': takes a type Python has no way to hand over "
        "yet.")
