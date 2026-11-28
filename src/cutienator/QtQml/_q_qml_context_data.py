"""
QQmlContextData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlcontextdata_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlContextData to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject, QUrl
  from . import QQmlComponentAttached, QQmlContext, QQmlContextPrivate
  from . import QQmlData, QQmlEngine, QQmlIncubatorPrivate
  from . import QQmlJavaScriptExpression, QQmlNotifier
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlComponentAttached = WAIT['QQmlComponentAttached']
  QQmlData = WAIT['QQmlData']
  QQmlEngine = WAIT['QQmlEngine']
  QQmlIncubatorPrivate = WAIT['QQmlIncubatorPrivate']
  QQmlJavaScriptExpression = WAIT['QQmlJavaScriptExpression']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlContextData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlContextData: a plain Python object standing in
  front of one C++ QQmlContextData.

  What exists
  -----------

  Every function of Qt's QQmlContextData that has a ritual and that Python
  can call so far, 70 names in all: 'addref', 'release', 'count', 'refCount',
  'emitDestruction', 'clearExpressions', 'clearContextRecursively',
  'clearChildrenAndSiblings', 'clearImportedScripts', 'clearOwnedObjects',
  'clearContextGuards', 'clearIdValues', 'invalidate', 'isValid',
  'isInternal', 'setInternal', 'isJSContext', 'setJSContext',
  'isPragmaLibraryContext', 'setPragmaLibraryContext', 'clearParent',
  'refreshExpressions', 'addOwnedObject', 'ownedObjects', 'setOwnedObjects',
  'installContext', 'resolvedUrl', 'asQQmlContext', 'asQQmlContextPrivate',
  'contextObject', 'setContextObject', 'deepClearContextObject', 'engine',
  'setEngine', 'publicContext', 'clearPublicContext', 'setExpressions',
  'expressions', 'takeExpressions', 'numIdValues', 'setIdValue',
  'isIdValueSet', 'idValueBindings', 'idValue', 'findObjectId', 'url',
  'urlString', 'setBaseUrlString', 'baseUrlString', 'setBaseUrl', 'baseUrl',
  'incubator', 'setIncubator', 'extraObject', 'setExtraObject',
  'isRootObjectInCreation', 'setRootObjectInCreation', 'importedScripts',
  'setImportedScripts', 'hasUnresolvedNames', 'setUnresolvedNames',
  'componentAttacheds', 'addComponentAttached', 'addExpression',
  'valueTypesAreAddressable', 'valueTypesAreAssertable',
  'hasExpressionsToRun', 'refreshExpressionsRecursive', 'initPropertyNames',
  'ensurePropertyNames'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlRefPointer<QQmlContextData>
    QQmlContextData::createRefCounted(const QQmlRefPointer<QQmlContextData>
    &parent)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlRefPointer<QQmlContextData> QQmlContextData::createChild(const
    QQmlRefPointer<QQmlContextData> &parent)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QQmlRefPointer<QV4::ExecutableCompilationUnit>
    QQmlContextData::typeCompilationUnit() const': gives a type Python has no
    way to take yet.
  - Qt's 'void QQmlContextData::setTypeCompilationUnit(const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QQmlContextData::initFromTypeCompilationUnit(const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit, int
    subComponentIndex)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlRefPointer<QQmlContextData> QQmlContextData::get(QQmlContext
    *context)': gives a type Python has no way to take yet.
  - Qt's 'QQmlRefPointer<QQmlContextData> QQmlContextData::parent() const':
    gives a type Python has no way to take yet.
  - Qt's 'void QQmlContextData::setChildContexts(const
    QQmlRefPointer<QQmlContextData> &childContexts)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QQmlRefPointer<QQmlContextData> QQmlContextData::childContexts()
    const': gives a type Python has no way to take yet.
  - Qt's 'QQmlRefPointer<QQmlContextData>
    QQmlContextData::takeChildContexts()': gives a type Python has no way to
    take yet.
  - Qt's 'QQmlRefPointer<QQmlContextData> QQmlContextData::nextChild()
    const': gives a type Python has no way to take yet.
  - Qt's 'QQmlRefPointer<QQmlTypeNameCache> QQmlContextData::imports()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QQmlContextData::setImports(const
    QQmlRefPointer<QQmlTypeNameCache> &imports)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QQmlRefPointer<QQmlContextData> QQmlContextData::linkedContext()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QQmlContextData::setLinkedContext(const
    QQmlRefPointer<QQmlContextData> &context)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QQmlContextData::QQmlContextData(Ownership ownership, QQmlContext
    *publicContext, const QQmlRefPointer<QQmlContextData> &parent, QQmlEngine
    *engine)': names the enum 'QQmlContextData::Ownership', whose class
    cannot be named here.
  - Qt's 'QQmlContextData::~QQmlContextData()': the destructor: Python never
    removes a C++ QQmlContextData.

  What has no ritual
  ------------------

  5 of the 94 functions Qt declares: 3 leans on 'QV4; 1 a template; 1 leans
  on 'QString QV4.

  What to expect
  --------------

  - The C++ QQmlContextData is created at the first use, not by
    'QQmlContextData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlContextData.
  - Each name of Qt's QQmlContextData that has no cute function yet,
    '__init__', 'addPropertyNameAndIndex', 'childContexts', 'createChild',
    'createRefCounted', 'get', 'imports', 'initFromTypeCompilationUnit',
    'linkedContext', 'nextChild', 'parent', 'propertyIndex', 'propertyName',
    'setChildContexts', 'setImports', 'setLinkedContext',
    'setTypeCompilationUnit', 'takeChildContexts', 'typeCompilationUnit',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QQmlContextData, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class QmlObjectKind(CuteNum):
    """
    The enum 'QQmlContextData::QmlObjectKind' of Qt, with the 2 names Qt
    gives in it.
    """

    OrdinaryObject = Kee[int](0)
    DocumentRoot = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlContextData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def count(self) -> int:
    """
    Calls Qt's 'int QQmlContextData::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#count
    """
    #  int QQmlContextData::count() const
    return self.uglySide.call('ritual_ZNK15QQmlContextData5countEv')

  def refCount(self) -> int:
    """
    Calls Qt's 'int QQmlContextData::refCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#refCount
    """
    #  int QQmlContextData::refCount() const
    return self.uglySide.call('ritual_ZNK15QQmlContextData8refCountEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQmlContextData::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#isValid
    """
    #  bool QQmlContextData::isValid() const
    return self.uglySide.call('ritual_ZNK15QQmlContextData7isValidEv')

  def isInternal(self) -> bool:
    """
    Calls Qt's 'bool QQmlContextData::isInternal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#isInternal
    """
    #  bool QQmlContextData::isInternal() const
    return self.uglySide.call('ritual_ZNK15QQmlContextData10isInternalEv')

  def isJSContext(self) -> bool:
    """
    Calls Qt's 'bool QQmlContextData::isJSContext() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#isJSContext
    """
    #  bool QQmlContextData::isJSContext() const
    return self.uglySide.call('ritual_ZNK15QQmlContextData11isJSContextEv')

  def isPragmaLibraryContext(self) -> bool:
    """
    Calls Qt's 'bool QQmlContextData::isPragmaLibraryContext() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#isPragmaLibraryContext
    """
    #  bool QQmlContextData::isPragmaLibraryContext() const
    return self.uglySide.call(
        'ritual_ZNK15QQmlContextData22isPragmaLibraryContextEv',
    )

  def ownedObjects(self) -> Optional[QQmlData]:
    """
    Calls Qt's 'QQmlData *QQmlContextData::ownedObjects() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#ownedObjects

    Returns
    -------

    Optional[QQmlData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlData *QQmlContextData::ownedObjects() const
    address = self.uglySide.call(
        'ritual_ZNK15QQmlContextData12ownedObjectsEv',
    )
    from . import QQmlData
    return QQmlData._cuteAt(address)

  @overload(QUrl)
  def resolvedUrl(self, a0: QUrl) -> QUrl:
    """
    Calls Qt's 'QUrl QQmlContextData::resolvedUrl(const QUrl &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#resolvedUrl

    Parameters
    ----------

    a0 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQmlContextData::resolvedUrl(const QUrl &a0) const
    address = self.uglySide.call(
        'ritual_ZNK15QQmlContextData11resolvedUrlERK4QUrl',
        self._valueOf(a0),
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def contextObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlContextData::contextObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#contextObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlContextData::contextObject() const
    address = self.uglySide.call(
        'ritual_ZNK15QQmlContextData13contextObjectEv',
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def engine(self) -> Optional[QQmlEngine]:
    """
    Calls Qt's 'QQmlEngine *QQmlContextData::engine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#engine

    Returns
    -------

    Optional[QQmlEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlEngine *QQmlContextData::engine() const
    address = self.uglySide.call('ritual_ZNK15QQmlContextData6engineEv')
    from . import QQmlEngine
    return QQmlEngine._cuteAt(address)

  def publicContext(self) -> Optional[QQmlContext]:
    """
    Calls Qt's 'QQmlContext *QQmlContextData::publicContext() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#publicContext

    Returns
    -------

    Optional[QQmlContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlContext *QQmlContextData::publicContext() const
    address = self.uglySide.call(
        'ritual_ZNK15QQmlContextData13publicContextEv',
    )
    from . import QQmlContext
    return QQmlContext._cuteAt(address)

  def expressions(self) -> Optional[QQmlJavaScriptExpression]:
    """
    Calls Qt's 'QQmlJavaScriptExpression *QQmlContextData::expressions()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#expressions

    Returns
    -------

    Optional[QQmlJavaScriptExpression]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlJavaScriptExpression *QQmlContextData::expressions() const
    address = self.uglySide.call(
        'ritual_ZNK15QQmlContextData11expressionsEv',
    )
    from . import QQmlJavaScriptExpression
    return QQmlJavaScriptExpression._cuteAt(address)

  def numIdValues(self) -> int:
    """
    Calls Qt's 'int QQmlContextData::numIdValues() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#numIdValues
    """
    #  int QQmlContextData::numIdValues() const
    return self.uglySide.call('ritual_ZNK15QQmlContextData11numIdValuesEv')

  @overload(int)
  def isIdValueSet(self, index: int) -> bool:
    """
    Calls Qt's 'bool QQmlContextData::isIdValueSet(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#isIdValueSet

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QQmlContextData::isIdValueSet(int index) const
    return self.uglySide.call(
        'ritual_ZNK15QQmlContextData12isIdValueSetEi', index,
    )

  @overload(int)
  def idValueBindings(self, index: int) -> Optional[QQmlNotifier]:
    """
    Calls Qt's 'QQmlNotifier *QQmlContextData::idValueBindings(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#idValueBindings

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QQmlNotifier]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlNotifier *QQmlContextData::idValueBindings(int index) const
    address = self.uglySide.call(
        'ritual_ZNK15QQmlContextData15idValueBindingsEi', index,
    )
    from . import QQmlNotifier
    return QQmlNotifier._cuteAt(address)

  @overload(int)
  def idValue(self, index: int) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlContextData::idValue(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#idValue

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlContextData::idValue(int index) const
    address = self.uglySide.call(
        'ritual_ZNK15QQmlContextData7idValueEi', index,
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  @overload(QObject)
  @overload(NoneType)
  def findObjectId(self, obj: Optional[QObject]) -> str:
    """
    Calls Qt's 'QString QQmlContextData::findObjectId(const QObject *obj)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#findObjectId

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlContextData::findObjectId(const QObject *obj) const
    return self.uglySide.call(
        'ritual_ZNK15QQmlContextData12findObjectIdEPK7QObject',
        self._addressOf(obj, 'QObject'),
    )

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQmlContextData::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQmlContextData::url() const
    address = self.uglySide.call('ritual_ZNK15QQmlContextData3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def urlString(self) -> str:
    """
    Calls Qt's 'QString QQmlContextData::urlString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#urlString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlContextData::urlString() const
    return self.uglySide.call('ritual_ZNK15QQmlContextData9urlStringEv')

  def baseUrlString(self) -> str:
    """
    Calls Qt's 'QString QQmlContextData::baseUrlString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#baseUrlString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlContextData::baseUrlString() const
    return self.uglySide.call('ritual_ZNK15QQmlContextData13baseUrlStringEv')

  def baseUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQmlContextData::baseUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#baseUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQmlContextData::baseUrl() const
    address = self.uglySide.call('ritual_ZNK15QQmlContextData7baseUrlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def incubator(self) -> Optional[QQmlIncubatorPrivate]:
    """
    Calls Qt's 'QQmlIncubatorPrivate *QQmlContextData::incubator() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#incubator

    Returns
    -------

    Optional[QQmlIncubatorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlIncubatorPrivate *QQmlContextData::incubator() const
    address = self.uglySide.call('ritual_ZNK15QQmlContextData9incubatorEv')
    from . import QQmlIncubatorPrivate
    return QQmlIncubatorPrivate._cuteAt(address)

  def extraObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlContextData::extraObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#extraObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlContextData::extraObject() const
    address = self.uglySide.call(
        'ritual_ZNK15QQmlContextData11extraObjectEv',
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def isRootObjectInCreation(self) -> bool:
    """
    Calls Qt's 'bool QQmlContextData::isRootObjectInCreation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#isRootObjectInCreation
    """
    #  bool QQmlContextData::isRootObjectInCreation() const
    return self.uglySide.call(
        'ritual_ZNK15QQmlContextData22isRootObjectInCreationEv',
    )

  def importedScripts(self) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue QQmlContextData::importedScripts() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#importedScripts
    """
    #  QV4::ReturnedValue QQmlContextData::importedScripts() const
    return self.uglySide.call(
        'ritual_ZNK15QQmlContextData15importedScriptsEv',
    )

  def hasUnresolvedNames(self) -> bool:
    """
    Calls Qt's 'bool QQmlContextData::hasUnresolvedNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#hasUnresolvedNames
    """
    #  bool QQmlContextData::hasUnresolvedNames() const
    return self.uglySide.call(
        'ritual_ZNK15QQmlContextData18hasUnresolvedNamesEv',
    )

  def componentAttacheds(self) -> Optional[QQmlComponentAttached]:
    """
    Calls Qt's 'QQmlComponentAttached *QQmlContextData::componentAttacheds()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#componentAttacheds

    Returns
    -------

    Optional[QQmlComponentAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponentAttached *QQmlContextData::componentAttacheds() const
    address = self.uglySide.call(
        'ritual_ZNK15QQmlContextData18componentAttachedsEv',
    )
    from . import QQmlComponentAttached
    return QQmlComponentAttached._cuteAt(address)

  def valueTypesAreAddressable(self) -> bool:
    """
    Calls Qt's 'bool QQmlContextData::valueTypesAreAddressable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#valueTypesAreAddressable
    """
    #  bool QQmlContextData::valueTypesAreAddressable() const
    return self.uglySide.call(
        'ritual_ZNK15QQmlContextData24valueTypesAreAddressableEv',
    )

  def valueTypesAreAssertable(self) -> bool:
    """
    Calls Qt's 'bool QQmlContextData::valueTypesAreAssertable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#valueTypesAreAssertable
    """
    #  bool QQmlContextData::valueTypesAreAssertable() const
    return self.uglySide.call(
        'ritual_ZNK15QQmlContextData23valueTypesAreAssertableEv',
    )

  @overload(bool)
  def hasExpressionsToRun(self, isGlobalRefresh: bool) -> bool:
    """
    Calls Qt's 'bool QQmlContextData::hasExpressionsToRun(bool
    isGlobalRefresh) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#hasExpressionsToRun

    Parameters
    ----------

    isGlobalRefresh : bool
      Passed on as it is.
    """
    #  bool QQmlContextData::hasExpressionsToRun(bool isGlobalRefresh) const
    return self.uglySide.call(
        'ritual_ZNK15QQmlContextData19hasExpressionsToRunEb',
        isGlobalRefresh,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setInternal(self, isInternal: bool) -> None:
    """
    Calls Qt's 'void QQmlContextData::setInternal(bool isInternal)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#setInternal

    Parameters
    ----------

    isInternal : bool
      Passed on as it is.
    """
    #  void QQmlContextData::setInternal(bool isInternal)
    self.uglySide.call(
        'ritual_ZN15QQmlContextData11setInternalEb', isInternal,
    )

  @overload(bool)
  def setJSContext(self, isJSContext: bool) -> None:
    """
    Calls Qt's 'void QQmlContextData::setJSContext(bool isJSContext)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#setJSContext

    Parameters
    ----------

    isJSContext : bool
      Passed on as it is.
    """
    #  void QQmlContextData::setJSContext(bool isJSContext)
    self.uglySide.call(
        'ritual_ZN15QQmlContextData12setJSContextEb', isJSContext,
    )

  @overload(bool)
  def setPragmaLibraryContext(self, library: bool) -> None:
    """
    Calls Qt's 'void QQmlContextData::setPragmaLibraryContext(bool library)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#setPragmaLibraryContext

    Parameters
    ----------

    library : bool
      Passed on as it is.
    """
    #  void QQmlContextData::setPragmaLibraryContext(bool library)
    self.uglySide.call(
        'ritual_ZN15QQmlContextData23setPragmaLibraryContextEb', library,
    )

  @overload(QQmlData)
  @overload(NoneType)
  def setOwnedObjects(self, ownedObjects: Optional[QQmlData]) -> None:
    """
    Calls Qt's 'void QQmlContextData::setOwnedObjects(QQmlData
    *ownedObjects)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#setOwnedObjects

    Parameters
    ----------

    ownedObjects : Optional[QQmlData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlContextData::setOwnedObjects(QQmlData *ownedObjects)
    self.uglySide.call(
        'ritual_ZN15QQmlContextData15setOwnedObjectsEP8QQmlData',
        self._addressOf(ownedObjects),
    )

  @overload(QObject)
  @overload(NoneType)
  def setContextObject(self, contextObject: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlContextData::setContextObject(QObject
    *contextObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#setContextObject

    Parameters
    ----------

    contextObject : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlContextData::setContextObject(QObject *contextObject)
    self.uglySide.call(
        'ritual_ZN15QQmlContextData16setContextObjectEP7QObject',
        self._addressOf(contextObject, 'QObject'),
    )

  @overload(QQmlEngine)
  @overload(NoneType)
  def setEngine(self, engine: Optional[QQmlEngine]) -> None:
    """
    Calls Qt's 'void QQmlContextData::setEngine(QQmlEngine *engine)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#setEngine

    Parameters
    ----------

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlContextData::setEngine(QQmlEngine *engine)
    self.uglySide.call(
        'ritual_ZN15QQmlContextData9setEngineEP10QQmlEngine',
        self._addressOf(engine),
    )

  @overload(QQmlJavaScriptExpression)
  @overload(NoneType)
  def setExpressions(
      self,
      expressions: Optional[QQmlJavaScriptExpression],
  ) -> None:
    """
    Calls Qt's 'void QQmlContextData::setExpressions(QQmlJavaScriptExpression
    *expressions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#setExpressions

    Parameters
    ----------

    expressions : Optional[QQmlJavaScriptExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlContextData::setExpressions(QQmlJavaScriptExpression
    #      *expressions)
    self.uglySide.call(
        'ritual_ZN15QQmlContextData14setExpressionsEP24QQmlJavaScriptExpres'
        'sion',
        self._addressOf(expressions, 'QQmlJavaScriptExpression'),
    )

  @overload(int, QObject)
  @overload(int, NoneType)
  def setIdValue(self, index: int, idValue: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlContextData::setIdValue(int index, QObject
    *idValue)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#setIdValue

    Parameters
    ----------

    index : int
      Passed on as it is.

    idValue : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlContextData::setIdValue(int index, QObject *idValue)
    self.uglySide.call(
        'ritual_ZN15QQmlContextData10setIdValueEiP7QObject',
        index, self._addressOf(idValue, 'QObject'),
    )

  @overload(str)
  def setBaseUrlString(self, baseUrlString: str) -> None:
    """
    Calls Qt's 'void QQmlContextData::setBaseUrlString(const QString
    &baseUrlString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#setBaseUrlString

    Parameters
    ----------

    baseUrlString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlContextData::setBaseUrlString(const QString &baseUrlString)
    self.uglySide.call(
        'ritual_ZN15QQmlContextData16setBaseUrlStringERK7QString',
        baseUrlString,
    )

  @overload(QUrl)
  def setBaseUrl(self, baseUrl: QUrl) -> None:
    """
    Calls Qt's 'void QQmlContextData::setBaseUrl(const QUrl &baseUrl)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#setBaseUrl

    Parameters
    ----------

    baseUrl : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQmlContextData::setBaseUrl(const QUrl &baseUrl)
    self.uglySide.call(
        'ritual_ZN15QQmlContextData10setBaseUrlERK4QUrl',
        self._valueOf(baseUrl),
    )

  @overload(QQmlIncubatorPrivate)
  @overload(NoneType)
  def setIncubator(self, incubator: Optional[QQmlIncubatorPrivate]) -> None:
    """
    Calls Qt's 'void QQmlContextData::setIncubator(QQmlIncubatorPrivate
    *incubator)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#setIncubator

    Parameters
    ----------

    incubator : Optional[QQmlIncubatorPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlContextData::setIncubator(QQmlIncubatorPrivate *incubator)
    self.uglySide.call(
        'ritual_ZN15QQmlContextData12setIncubatorEP20QQmlIncubatorPrivate',
        self._addressOf(incubator),
    )

  @overload(QObject)
  @overload(NoneType)
  def setExtraObject(self, extraObject: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlContextData::setExtraObject(QObject *extraObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#setExtraObject

    Parameters
    ----------

    extraObject : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlContextData::setExtraObject(QObject *extraObject)
    self.uglySide.call(
        'ritual_ZN15QQmlContextData14setExtraObjectEP7QObject',
        self._addressOf(extraObject, 'QObject'),
    )

  @overload(bool)
  def setRootObjectInCreation(self, rootInCreation: bool) -> None:
    """
    Calls Qt's 'void QQmlContextData::setRootObjectInCreation(bool
    rootInCreation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#setRootObjectInCreation

    Parameters
    ----------

    rootInCreation : bool
      Passed on as it is.
    """
    #  void QQmlContextData::setRootObjectInCreation(bool rootInCreation)
    self.uglySide.call(
        'ritual_ZN15QQmlContextData23setRootObjectInCreationEb',
        rootInCreation,
    )

  @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Value'])
  @overload(NoneType, WAIT['QV4.Value'])
  def setImportedScripts(
      self,
      engine: Optional[QV4.ExecutionEngine],
      scripts: QV4.Value,
  ) -> None:
    """
    Calls Qt's 'void QQmlContextData::setImportedScripts(QV4::ExecutionEngine
    *engine, QV4::Value scripts)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#setImportedScripts

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    scripts : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QQmlContextData::setImportedScripts(QV4::ExecutionEngine *engine,
    #      QV4::Value scripts)
    self.uglySide.call(
        'ritual_ZN15QQmlContextData18setImportedScriptsEPN3QV415ExecutionEn'
        'gineENS0_5ValueE',
        self._addressOf(engine), self._valueOf(scripts),
    )

  @overload(WAIT['QV4.ExecutionEngine'], int)
  @overload(NoneType, int)
  def setImportedScripts(
      self,
      engine: Optional[QV4.ExecutionEngine],
      scripts: int,
  ) -> None:
    """
    Calls Qt's 'void QQmlContextData::setImportedScripts(QV4::ExecutionEngine
    *engine, QV4::ReturnedValue scripts)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#setImportedScripts

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    scripts : int
      Passed on as it is.
    """
    #  void QQmlContextData::setImportedScripts(QV4::ExecutionEngine *engine,
    #      QV4::ReturnedValue scripts)
    self.uglySide.call(
        'ritual_ZN15QQmlContextData18setImportedScriptsEPN3QV415ExecutionEn'
        'gineEy',
        self._addressOf(engine), scripts,
    )

  @overload(bool)
  def setUnresolvedNames(self, hasUnresolvedNames: bool) -> None:
    """
    Calls Qt's 'void QQmlContextData::setUnresolvedNames(bool
    hasUnresolvedNames)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#setUnresolvedNames

    Parameters
    ----------

    hasUnresolvedNames : bool
      Passed on as it is.
    """
    #  void QQmlContextData::setUnresolvedNames(bool hasUnresolvedNames)
    self.uglySide.call(
        'ritual_ZN15QQmlContextData18setUnresolvedNamesEb',
        hasUnresolvedNames,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQmlContextData::QQmlContextData(Ownership ownership, QQmlContext
    *publicContext, const QQmlRefPointer<QQmlContextData> &parent, QQmlEngine
    *engine)': names the enum 'QQmlContextData::Ownership', whose class
    cannot be named here.
    """
    raise NotImplementedError(
        "'QQmlContextData.__init__' has no cute function yet. Qt's "
        "'QQmlContextData::QQmlContextData(Ownership ownership, QQmlContext "
        "*publicContext, const QQmlRefPointer<QQmlContextData> &parent, "
        "QQmlEngine *engine)': names the enum 'QQmlContextData::Ownership', "
        "whose class cannot be named here.")

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

  def addref(self) -> None:
    """
    Calls Qt's 'void QQmlContextData::addref() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#addref
    """
    #  void QQmlContextData::addref() const
    self.uglySide.call('ritual_ZNK15QQmlContextData6addrefEv')

  def release(self) -> None:
    """
    Calls Qt's 'void QQmlContextData::release() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#release
    """
    #  void QQmlContextData::release() const
    self.uglySide.call('ritual_ZNK15QQmlContextData7releaseEv')

  def emitDestruction(self) -> None:
    """
    Calls Qt's 'void QQmlContextData::emitDestruction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#emitDestruction
    """
    #  void QQmlContextData::emitDestruction()
    self.uglySide.call('ritual_ZN15QQmlContextData15emitDestructionEv')

  def clearExpressions(self) -> None:
    """
    Calls Qt's 'void QQmlContextData::clearExpressions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#clearExpressions
    """
    #  void QQmlContextData::clearExpressions()
    self.uglySide.call('ritual_ZN15QQmlContextData16clearExpressionsEv')

  def clearContextRecursively(self) -> None:
    """
    Calls Qt's 'void QQmlContextData::clearContextRecursively()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#clearContextRecursively
    """
    #  void QQmlContextData::clearContextRecursively()
    self.uglySide.call(
        'ritual_ZN15QQmlContextData23clearContextRecursivelyEv',
    )

  def clearChildrenAndSiblings(self) -> None:
    """
    Calls Qt's 'void QQmlContextData::clearChildrenAndSiblings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#clearChildrenAndSiblings
    """
    #  void QQmlContextData::clearChildrenAndSiblings()
    self.uglySide.call(
        'ritual_ZN15QQmlContextData24clearChildrenAndSiblingsEv',
    )

  def clearImportedScripts(self) -> None:
    """
    Calls Qt's 'void QQmlContextData::clearImportedScripts()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#clearImportedScripts
    """
    #  void QQmlContextData::clearImportedScripts()
    self.uglySide.call('ritual_ZN15QQmlContextData20clearImportedScriptsEv')

  def clearOwnedObjects(self) -> None:
    """
    Calls Qt's 'void QQmlContextData::clearOwnedObjects()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#clearOwnedObjects
    """
    #  void QQmlContextData::clearOwnedObjects()
    self.uglySide.call('ritual_ZN15QQmlContextData17clearOwnedObjectsEv')

  def clearContextGuards(self) -> None:
    """
    Calls Qt's 'void QQmlContextData::clearContextGuards()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#clearContextGuards
    """
    #  void QQmlContextData::clearContextGuards()
    self.uglySide.call('ritual_ZN15QQmlContextData18clearContextGuardsEv')

  def clearIdValues(self) -> None:
    """
    Calls Qt's 'void QQmlContextData::clearIdValues()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#clearIdValues
    """
    #  void QQmlContextData::clearIdValues()
    self.uglySide.call('ritual_ZN15QQmlContextData13clearIdValuesEv')

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QQmlContextData::invalidate()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#invalidate
    """
    #  void QQmlContextData::invalidate()
    self.uglySide.call('ritual_ZN15QQmlContextData10invalidateEv')

  def clearParent(self) -> None:
    """
    Calls Qt's 'void QQmlContextData::clearParent()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#clearParent
    """
    #  void QQmlContextData::clearParent()
    self.uglySide.call('ritual_ZN15QQmlContextData11clearParentEv')

  def refreshExpressions(self) -> None:
    """
    Calls Qt's 'void QQmlContextData::refreshExpressions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#refreshExpressions
    """
    #  void QQmlContextData::refreshExpressions()
    self.uglySide.call('ritual_ZN15QQmlContextData18refreshExpressionsEv')

  @overload(QQmlData)
  @overload(NoneType)
  def addOwnedObject(self, ownedObject: Optional[QQmlData]) -> None:
    """
    Calls Qt's 'void QQmlContextData::addOwnedObject(QQmlData *ownedObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#addOwnedObject

    Parameters
    ----------

    ownedObject : Optional[QQmlData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlContextData::addOwnedObject(QQmlData *ownedObject)
    self.uglySide.call(
        'ritual_ZN15QQmlContextData14addOwnedObjectEP8QQmlData',
        self._addressOf(ownedObject),
    )

  @overload(QQmlData, QmlObjectKind)
  @overload(NoneType, QmlObjectKind)
  def installContext(
      self,
      ddata: Optional[QQmlData],
      kind: QmlObjectKind,
  ) -> None:
    """
    Calls Qt's 'void QQmlContextData::installContext(QQmlData *ddata,
    QmlObjectKind kind)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#installContext

    Parameters
    ----------

    ddata : Optional[QQmlData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    kind : QmlObjectKind
      Passed on as its number.
    """
    #  void QQmlContextData::installContext(QQmlData *ddata, QmlObjectKind
    #      kind)
    self.uglySide.call(
        'ritual_ZN15QQmlContextData14installContextEP8QQmlDataNS_13QmlObjec'
        'tKindE',
        self._addressOf(ddata), kind.value,
    )

  def asQQmlContext(self) -> Optional[QQmlContext]:
    """
    Calls Qt's 'QQmlContext *QQmlContextData::asQQmlContext()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#asQQmlContext

    Returns
    -------

    Optional[QQmlContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlContext *QQmlContextData::asQQmlContext()
    address = self.uglySide.call(
        'ritual_ZN15QQmlContextData13asQQmlContextEv',
    )
    from . import QQmlContext
    return QQmlContext._cuteAt(address)

  def asQQmlContextPrivate(self) -> Optional[QQmlContextPrivate]:
    """
    Calls Qt's 'QQmlContextPrivate *QQmlContextData::asQQmlContextPrivate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#asQQmlContextPrivate

    Returns
    -------

    Optional[QQmlContextPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlContextPrivate *QQmlContextData::asQQmlContextPrivate()
    address = self.uglySide.call(
        'ritual_ZN15QQmlContextData20asQQmlContextPrivateEv',
    )
    from . import QQmlContextPrivate
    return QQmlContextPrivate._cuteAt(address)

  @overload(QObject)
  @overload(NoneType)
  def deepClearContextObject(self, contextObject: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlContextData::deepClearContextObject(QObject
    *contextObject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#deepClearContextObject

    Parameters
    ----------

    contextObject : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlContextData::deepClearContextObject(QObject *contextObject)
    self.uglySide.call(
        'ritual_ZN15QQmlContextData22deepClearContextObjectEP7QObject',
        self._addressOf(contextObject, 'QObject'),
    )

  def clearPublicContext(self) -> None:
    """
    Calls Qt's 'void QQmlContextData::clearPublicContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#clearPublicContext
    """
    #  void QQmlContextData::clearPublicContext()
    self.uglySide.call('ritual_ZN15QQmlContextData18clearPublicContextEv')

  def takeExpressions(self) -> Optional[QQmlJavaScriptExpression]:
    """
    Calls Qt's 'QQmlJavaScriptExpression
    *QQmlContextData::takeExpressions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#takeExpressions

    Returns
    -------

    Optional[QQmlJavaScriptExpression]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlJavaScriptExpression *QQmlContextData::takeExpressions()
    address = self.uglySide.call(
        'ritual_ZN15QQmlContextData15takeExpressionsEv',
    )
    from . import QQmlJavaScriptExpression
    return QQmlJavaScriptExpression._cuteAt(address)

  @overload(QQmlComponentAttached)
  @overload(NoneType)
  def addComponentAttached(
      self,
      attached: Optional[QQmlComponentAttached],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlContextData::addComponentAttached(QQmlComponentAttached *attached)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#addComponentAttached

    Parameters
    ----------

    attached : Optional[QQmlComponentAttached]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlContextData::addComponentAttached(QQmlComponentAttached
    #      *attached)
    self.uglySide.call(
        'ritual_ZN15QQmlContextData20addComponentAttachedEP21QQmlComponentA'
        'ttached',
        self._addressOf(attached),
    )

  @overload(QQmlJavaScriptExpression)
  @overload(NoneType)
  def addExpression(
      self,
      expression: Optional[QQmlJavaScriptExpression],
  ) -> None:
    """
    Calls Qt's 'void QQmlContextData::addExpression(QQmlJavaScriptExpression
    *expression)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcontextdata.html#addExpression

    Parameters
    ----------

    expression : Optional[QQmlJavaScriptExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlContextData::addExpression(QQmlJavaScriptExpression
    #      *expression)
    self.uglySide.call(
        'ritual_ZN15QQmlContextData13addExpressionEP24QQmlJavaScriptExpress'
        'ion',
        self._addressOf(expression, 'QQmlJavaScriptExpression'),
    )

  @overload(bool)
  def refreshExpressionsRecursive(self, isGlobal: bool) -> None:
    """
    Calls Qt's 'void QQmlContextData::refreshExpressionsRecursive(bool
    isGlobal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#refreshExpressionsRecursive

    Parameters
    ----------

    isGlobal : bool
      Passed on as it is.
    """
    #  void QQmlContextData::refreshExpressionsRecursive(bool isGlobal)
    self.uglySide.call(
        'ritual_ZN15QQmlContextData27refreshExpressionsRecursiveEb',
        isGlobal,
    )

  @overload(QQmlJavaScriptExpression)
  @overload(NoneType)
  def refreshExpressionsRecursive(
      self,
      a0: Optional[QQmlJavaScriptExpression],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlContextData::refreshExpressionsRecursive(QQmlJavaScriptExpression
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#refreshExpressionsRecursive

    Parameters
    ----------

    a0 : Optional[QQmlJavaScriptExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlContextData::refreshExpressionsRecursive(
    #      QQmlJavaScriptExpression *a0)
    self.uglySide.call(
        'ritual_ZN15QQmlContextData27refreshExpressionsRecursiveEP24QQmlJav'
        'aScriptExpression',
        self._addressOf(a0, 'QQmlJavaScriptExpression'),
    )

  def initPropertyNames(self) -> None:
    """
    Calls Qt's 'void QQmlContextData::initPropertyNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#initPropertyNames
    """
    #  void QQmlContextData::initPropertyNames() const
    self.uglySide.call('ritual_ZNK15QQmlContextData17initPropertyNamesEv')

  def ensurePropertyNames(self) -> None:
    """
    Calls Qt's 'void QQmlContextData::ensurePropertyNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcontextdata.html#ensurePropertyNames
    """
    #  void QQmlContextData::ensurePropertyNames() const
    self.uglySide.call('ritual_ZNK15QQmlContextData19ensurePropertyNamesEv')

  @staticmethod
  def addPropertyNameAndIndex(*__, **_) -> Never:
    """
    Qt's 'void QQmlContextData::addPropertyNameAndIndex(const QString &name,
    int index)': leans on 'QV4::IdentifierHash::toIdentifier(QString const&)
    const', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlContextData.addPropertyNameAndIndex' has no cute function "
        "yet. Qt's 'void QQmlContextData::addPropertyNameAndIndex(const "
        "QString &name, int index)': leans on "
        "'QV4::IdentifierHash::toIdentifier(QString const&) const', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def childContexts(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QQmlContextData> QQmlContextData::childContexts()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlContextData.childContexts' has no cute function yet. Qt's "
        "'QQmlRefPointer<QQmlContextData> QQmlContextData::childContexts() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def createChild(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QQmlContextData> QQmlContextData::createChild(const
    QQmlRefPointer<QQmlContextData> &parent)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlContextData.createChild' has no cute function yet. Qt's "
        "'QQmlRefPointer<QQmlContextData> "
        "QQmlContextData::createChild(const QQmlRefPointer<QQmlContextData> "
        "&parent)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def createRefCounted(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QQmlContextData>
    QQmlContextData::createRefCounted(const QQmlRefPointer<QQmlContextData>
    &parent)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlContextData.createRefCounted' has no cute function yet. Qt's "
        "'QQmlRefPointer<QQmlContextData> "
        "QQmlContextData::createRefCounted(const "
        "QQmlRefPointer<QQmlContextData> &parent)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def get(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QQmlContextData> QQmlContextData::get(QQmlContext
    *context)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlContextData.get' has no cute function yet. Qt's "
        "'QQmlRefPointer<QQmlContextData> QQmlContextData::get(QQmlContext "
        "*context)': gives a type Python has no way to take yet.")

  @staticmethod
  def imports(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QQmlTypeNameCache> QQmlContextData::imports()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlContextData.imports' has no cute function yet. Qt's "
        "'QQmlRefPointer<QQmlTypeNameCache> QQmlContextData::imports() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def initFromTypeCompilationUnit(*__, **_) -> Never:
    """
    Qt's 'void QQmlContextData::initFromTypeCompilationUnit(const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit, int
    subComponentIndex)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlContextData.initFromTypeCompilationUnit' has no cute function "
        "yet. Qt's 'void QQmlContextData::initFromTypeCompilationUnit(const "
        "QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit, int "
        "subComponentIndex)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def linkedContext(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QQmlContextData> QQmlContextData::linkedContext()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlContextData.linkedContext' has no cute function yet. Qt's "
        "'QQmlRefPointer<QQmlContextData> QQmlContextData::linkedContext() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def nextChild(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QQmlContextData> QQmlContextData::nextChild()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlContextData.nextChild' has no cute function yet. Qt's "
        "'QQmlRefPointer<QQmlContextData> QQmlContextData::nextChild() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def parent(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QQmlContextData> QQmlContextData::parent() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlContextData.parent' has no cute function yet. Qt's "
        "'QQmlRefPointer<QQmlContextData> QQmlContextData::parent() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def propertyIndex(*__, **_) -> Never:
    """
    - Qt's 'int QQmlContextData::propertyIndex(const QString &name) const':
      leans on 'QV4::IdentifierHash::toIdentifier(QString const&) const',
      which Qt's source does not mark for use from outside Qt and has no code
      for that could be taken.
    - Qt's 'int QQmlContextData::propertyIndex(QV4::Heap::String *name)
      const': leans on 'QV4::IdentifierHash::toIdentifier(QV4::Heap::String*)
      const', which Qt's source does not mark for use from outside Qt and has
      no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlContextData.propertyIndex' has no cute function yet. Qt's "
        "'int QQmlContextData::propertyIndex(const QString &name) const': "
        "leans on 'QV4::IdentifierHash::toIdentifier(QString const&) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken. Qt's 'int "
        "QQmlContextData::propertyIndex(QV4::Heap::String *name) const': "
        "leans on 'QV4::IdentifierHash::toIdentifier(QV4::Heap::String*) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def propertyName(*__, **_) -> Never:
    """
    Qt's 'QString QQmlContextData::propertyName(int index) const': leans on
    'QString QV4::IdentifierHash::toString<QString>(QV4::PropertyKey) const',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQmlContextData.propertyName' has no cute function yet. Qt's "
        "'QString QQmlContextData::propertyName(int index) const': leans on "
        "'QString QV4::IdentifierHash::toString<QString>(QV4::PropertyKey) "
        "const', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def setChildContexts(*__, **_) -> Never:
    """
    Qt's 'void QQmlContextData::setChildContexts(const
    QQmlRefPointer<QQmlContextData> &childContexts)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlContextData.setChildContexts' has no cute function yet. Qt's "
        "'void QQmlContextData::setChildContexts(const "
        "QQmlRefPointer<QQmlContextData> &childContexts)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def setImports(*__, **_) -> Never:
    """
    Qt's 'void QQmlContextData::setImports(const
    QQmlRefPointer<QQmlTypeNameCache> &imports)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlContextData.setImports' has no cute function yet. Qt's 'void "
        "QQmlContextData::setImports(const "
        "QQmlRefPointer<QQmlTypeNameCache> &imports)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def setLinkedContext(*__, **_) -> Never:
    """
    Qt's 'void QQmlContextData::setLinkedContext(const
    QQmlRefPointer<QQmlContextData> &context)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlContextData.setLinkedContext' has no cute function yet. Qt's "
        "'void QQmlContextData::setLinkedContext(const "
        "QQmlRefPointer<QQmlContextData> &context)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def setTypeCompilationUnit(*__, **_) -> Never:
    """
    Qt's 'void QQmlContextData::setTypeCompilationUnit(const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlContextData.setTypeCompilationUnit' has no cute function yet. "
        "Qt's 'void QQmlContextData::setTypeCompilationUnit(const "
        "QQmlRefPointer<QV4::ExecutableCompilationUnit> &unit)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def takeChildContexts(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QQmlContextData>
    QQmlContextData::takeChildContexts()': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QQmlContextData.takeChildContexts' has no cute function yet. Qt's "
        "'QQmlRefPointer<QQmlContextData> "
        "QQmlContextData::takeChildContexts()': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def typeCompilationUnit(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QV4::ExecutableCompilationUnit>
    QQmlContextData::typeCompilationUnit() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQmlContextData.typeCompilationUnit' has no cute function yet. "
        "Qt's 'QQmlRefPointer<QV4::ExecutableCompilationUnit> "
        "QQmlContextData::typeCompilationUnit() const': gives a type Python "
        "has no way to take yet.")
