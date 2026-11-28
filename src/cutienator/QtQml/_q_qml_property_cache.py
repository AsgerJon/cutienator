"""
QQmlPropertyCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlPropertyCache to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QQmlPropertyData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QMetaType, QObject, QString
  from ..QtCore import QTypeRevision
  from . import QQmlEnumData, QQmlEnumValue, QQmlPropertyCacheMethodArguments
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QMetaObject = WAIT['QMetaObject']
  QMetaType = WAIT['QMetaType']
  QObject = WAIT['QObject']
  QQmlEnumValue = WAIT['QQmlEnumValue']
  QString = WAIT['QString']
  QTypeRevision = WAIT['QTypeRevision']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlPropertyCache(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlPropertyCache: a plain Python object standing in
  front of one C++ QQmlPropertyCache.

  What exists
  -----------

  Every function of Qt's QQmlPropertyCache that has a ritual and that Python
  can call so far, 39 names in all: 'update', 'invalidate', 'metaObject',
  'createMetaObject', 'firstCppMetaObject', 'property',
  'maybeUnresolvedProperty', 'method', 'signal', 'qmlEnum',
  'methodIndexToSignalIndex', 'defaultPropertyName', 'defaultProperty',
  'parent', 'setParent', 'overrideData', 'isAllowedInRevision',
  'originalClone', 'signalParameterNames', 'signalParameterStringForJS',
  'className', 'propertyCount', 'ownPropertyCount', 'propertyOffset',
  'methodCount', 'ownMethodCount', 'methodOffset', 'signalCount',
  'ownSignalCount', 'signalOffset', 'ownEnumCount', 'allowedRevision',
  'setAllowedRevision', 'isComposite', 'append', 'appendSignal',
  'appendMethod', 'appendEnum', 'createArgumentsObject'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Ptr QQmlPropertyCache::createStandalone(const QMetaObject *a0,
    QTypeRevision metaObjectRevision)': gives a type Python has no way to
    take yet.
  - Qt's 'QQmlPropertyCache::QQmlPropertyCache(OverrideSemantics::HandlerRef
    handleOverride)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlPropertyCache::~QQmlPropertyCache()': the destructor: Python
    never removes a C++ QQmlPropertyCache.
  - Qt's 'QQmlPropertyCache::Ptr QQmlPropertyCache::copy() const': gives a
    type Python has no way to take yet.
  - Qt's 'QQmlPropertyCache::Ptr QQmlPropertyCache::rebased(const
    QQmlPropertyCache::ConstPtr &parent) const': gives a type Python has no
    way to take yet.
  - Qt's 'QQmlPropertyCache::Ptr QQmlPropertyCache::copyAndAppend(const
    QMetaObject *a0, QTypeRevision typeVersion, QQmlPropertyData::Flags
    propertyFlags, QQmlPropertyData::Flags methodFlags,
    QQmlPropertyData::Flags signalFlags) const': gives a type Python has no
    way to take yet.
  - Qt's 'QQmlPropertyCache::Ptr QQmlPropertyCache::copyAndReserve(int
    propertyCount, int methodCount, int signalCount, int enumCount) const':
    gives a type Python has no way to take yet.
  - Qt's 'const QQmlPropertyData *QQmlPropertyCache::property(QObject *a0,
    QStringView a1, const QQmlRefPointer<QQmlContextData> &a2,
    QQmlPropertyData *a3)': takes a type Python has no way to hand over yet.
  - Qt's 'const QQmlPropertyData *QQmlPropertyCache::property(QObject *a0,
    const QLatin1String &a1, const QQmlRefPointer<QQmlContextData> &a2,
    QQmlPropertyData *a3)': takes a type Python has no way to hand over yet.
  - Qt's 'const QQmlPropertyData *QQmlPropertyCache::property(QObject *a0,
    const QV4::String *a1, const QQmlRefPointer<QQmlContextData> &a2,
    QQmlPropertyData *a3)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlPropertyCache::toMetaObjectBuilder(QMetaObjectBuilder &a0)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'bool QQmlPropertyCache::callJSFactoryMethod(QObject *object, void
    **args) const': takes a type Python has no way to hand over yet.
  - Qt's 'bool QQmlPropertyCache::determineMetaObjectSizes(const QMetaObject
    &mo, int *fieldCount, int *stringCount)': takes a number to change where
    it is.
  - Qt's 'bool QQmlPropertyCache::addToHash(QCryptographicHash &hash, const
    QMetaObject &mo)': takes a type Python has no way to hand over yet.
  - Qt's 'QByteArray QQmlPropertyCache::checksum(QHash<quintptr, QByteArray>
    *checksums, bool *ok) const': names 'QHash<quintptr, QByteArray>', which
    has no cute class yet.
  - Qt's 'QQmlPropertyCache::QQmlPropertyCache(const QQmlMetaObjectPointer
    &metaObject, OverrideSemantics::HandlerRef handleOverride)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QQmlPropertyCache::Ptr QQmlPropertyCache::copy(const
    QQmlMetaObjectPointer &mo, int reserve) const': takes a type Python has
    no way to hand over yet.
  - Qt's 'AppendResult QQmlPropertyCache::appendPropertyAttr(const QString
    &name, QQmlPropertyData &&data)': takes a type Python has no way to hand
    over yet.
  - Qt's 'AppendResult QQmlPropertyCache::appendAlias(const QString &a0,
    QQmlPropertyData::Flags flags, int coreIndex, QMetaType propType,
    QTypeRevision version, int notifyIndex, int encodedTargetIndex, int
    targetObjectId)': gives a type Python has no way to take yet.
  - Qt's 'AppendResult QQmlPropertyCache::appendComponentWrapper(int
    coreIndex, int wrappedObjectIndex)': gives a type Python has no way to
    take yet.

  What has no ritual
  ------------------

  6 of the 66 functions Qt declares: 4 a template; 2 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ QQmlPropertyCache is created at the first use, not by
    'QQmlPropertyCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlPropertyCache.
  - Each name of Qt's QQmlPropertyCache that has no cute function yet,
    '__init__', 'addToHash', 'appendAlias', 'appendComponentWrapper',
    'appendPropertyAttr', 'callJSFactoryMethod', 'checksum', 'copy',
    'copyAndAppend', 'copyAndReserve', 'createStandalone',
    'determineMetaObjectSizes', 'findNamedProperty', 'findProperty',
    'maybeLog', 'rebased', 'setNamedProperty', 'toMetaObjectBuilder', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QQmlPropertyCache, each a class in here as
  #  in C++.

  class ConstPtr(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlPropertyCache::ConstPtr: a plain Python object
    standing in front of one C++ QQmlPropertyCache::ConstPtr.

    C++ hands a QQmlPropertyCache::ConstPtr around as a copy, so every C++
    QQmlPropertyCache::ConstPtr behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QQmlPropertyCache::ConstPtr yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlPropertyCache::ConstPtr::ConstPtr(const Ptr &ptr)': takes a
      type Python has no way to hand over yet.
    - Qt's 'QQmlPropertyCache::ConstPtr::ConstPtr(Ptr &&ptr)': takes a type
      Python has no way to hand over yet.
    - Qt's 'ConstPtr &QQmlPropertyCache::ConstPtr::operator=(const Ptr
      &ptr)': assignment: Python binds a name and has no operator for it.
    - Qt's 'ConstPtr &QQmlPropertyCache::ConstPtr::operator=(Ptr &&ptr)':
      assignment: Python binds a name and has no operator for it.
    - Qt's 'QQmlPropertyCache::ConstPtr::~ConstPtr()': the destructor: Python
      removes its C++ QQmlPropertyCache::ConstPtr by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QQmlPropertyCache::ConstPtr is created at the first use, not by
      'QQmlPropertyCache::ConstPtr(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlPropertyCache::ConstPtr back gives a copy the
      ritual made for Python, in a new cute QQmlPropertyCache::ConstPtr.
    - Each name of Qt's QQmlPropertyCache::ConstPtr that has no cute function
      yet, '__init__', holds a function that raises 'NotImplementedError',
      and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlPropertyCache::ConstPtr'

    #  Qt's '~QQmlPropertyCache::ConstPtr()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlPropertyCache::ConstPtr behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN17QQmlPropertyCache8ConstPtrD1Ev'

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

    @staticmethod
    def __init__(*__, **_) -> Never:
      """
      - Qt's 'QQmlPropertyCache::ConstPtr::ConstPtr(const Ptr &ptr)': takes a
        type Python has no way to hand over yet.
      - Qt's 'QQmlPropertyCache::ConstPtr::ConstPtr(Ptr &&ptr)': takes a type
        Python has no way to hand over yet.
      """
      raise NotImplementedError(
          "'QQmlPropertyCache.ConstPtr.__init__' has no cute function yet. "
          "Qt's 'QQmlPropertyCache::ConstPtr::ConstPtr(const Ptr &ptr)': "
          "takes a type Python has no way to hand over yet. Qt's "
          "'QQmlPropertyCache::ConstPtr::ConstPtr(Ptr &&ptr)': takes a type "
          "Python has no way to hand over yet.")

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
  @overload(QList[QByteArray])
  @overload(QList[QByteArray], QString)
  @overload(QList[QByteArray], NoneType)
  def signalParameterStringForJS(
      parameterNameList: QList[QByteArray],
      errorString: Optional[QString] = None,
  ) -> str:
    """
    Calls Qt's 'QString QQmlPropertyCache::signalParameterStringForJS(const
    QList<QByteArray> &parameterNameList, QString *errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycache.html#signalParameterStringForJS

    Parameters
    ----------

    parameterNameList : QList[QByteArray]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    errorString : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlPropertyCache::signalParameterStringForJS(const
    #      QList<QByteArray> &parameterNameList, QString *errorString)
    return Rituals.call(
        'ritual_ZN17QQmlPropertyCache26signalParameterStringForJSERK5QListI'
        '10QByteArrayEP7QString',
        CuteMixin._valueOf(parameterNameList),
        CuteMixin._addressOf(errorString),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlPropertyCache'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlPropertyCache::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertycache.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlPropertyCache::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlPropertyCache10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def createMetaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlPropertyCache::createMetaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycache.html#createMetaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlPropertyCache::createMetaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlPropertyCache16createMetaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def firstCppMetaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlPropertyCache::firstCppMetaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycache.html#firstCppMetaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlPropertyCache::firstCppMetaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlPropertyCache18firstCppMetaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(int)
  def property(self, a0: int) -> Optional[QQmlPropertyData]:
    """
    Calls Qt's 'const QQmlPropertyData *QQmlPropertyCache::property(int a0)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertycache.html#property

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    Optional[QQmlPropertyData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QQmlPropertyData *QQmlPropertyCache::property(int a0) const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlPropertyCache8propertyEi', a0,
    )
    return QQmlPropertyData._cuteAt(address)

  @overload(int)
  def maybeUnresolvedProperty(self, a0: int) -> Optional[QQmlPropertyData]:
    """
    Calls Qt's 'const QQmlPropertyData
    *QQmlPropertyCache::maybeUnresolvedProperty(int a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycache.html#maybeUnresolvedProperty

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    Optional[QQmlPropertyData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QQmlPropertyData *QQmlPropertyCache::maybeUnresolvedProperty(int
    #      a0) const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlPropertyCache23maybeUnresolvedPropertyEi', a0,
    )
    return QQmlPropertyData._cuteAt(address)

  @overload(int)
  def method(self, a0: int) -> Optional[QQmlPropertyData]:
    """
    Calls Qt's 'const QQmlPropertyData *QQmlPropertyCache::method(int a0)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertycache.html#method

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    Optional[QQmlPropertyData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QQmlPropertyData *QQmlPropertyCache::method(int a0) const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlPropertyCache6methodEi', a0,
    )
    return QQmlPropertyData._cuteAt(address)

  @overload(int)
  def signal(self, index: int) -> Optional[QQmlPropertyData]:
    """
    Calls Qt's 'const QQmlPropertyData *QQmlPropertyCache::signal(int index)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertycache.html#signal

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QQmlPropertyData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QQmlPropertyData *QQmlPropertyCache::signal(int index) const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlPropertyCache6signalEi', index,
    )
    return QQmlPropertyData._cuteAt(address)

  @overload(int)
  def qmlEnum(self, a0: int) -> Optional[QQmlEnumData]:
    """
    Calls Qt's 'QQmlEnumData *QQmlPropertyCache::qmlEnum(int a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertycache.html#qmlEnum

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    Optional[QQmlEnumData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlEnumData *QQmlPropertyCache::qmlEnum(int a0) const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlPropertyCache7qmlEnumEi', a0,
    )
    from . import QQmlEnumData
    return QQmlEnumData._cuteAt(address)

  @overload(int)
  def methodIndexToSignalIndex(self, a0: int) -> int:
    """
    Calls Qt's 'int QQmlPropertyCache::methodIndexToSignalIndex(int a0)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycache.html#methodIndexToSignalIndex

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  int QQmlPropertyCache::methodIndexToSignalIndex(int a0) const
    return self.uglySide.call(
        'ritual_ZNK17QQmlPropertyCache24methodIndexToSignalIndexEi', a0,
    )

  def defaultPropertyName(self) -> str:
    """
    Calls Qt's 'QString QQmlPropertyCache::defaultPropertyName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycache.html#defaultPropertyName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlPropertyCache::defaultPropertyName() const
    return self.uglySide.call(
        'ritual_ZNK17QQmlPropertyCache19defaultPropertyNameEv',
    )

  def defaultProperty(self) -> Optional[QQmlPropertyData]:
    """
    Calls Qt's 'const QQmlPropertyData *QQmlPropertyCache::defaultProperty()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycache.html#defaultProperty

    Returns
    -------

    Optional[QQmlPropertyData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QQmlPropertyData *QQmlPropertyCache::defaultProperty() const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlPropertyCache15defaultPropertyEv',
    )
    return QQmlPropertyData._cuteAt(address)

  def parent(self) -> ConstPtr:
    """
    Calls Qt's 'const QQmlPropertyCache::ConstPtr
    &QQmlPropertyCache::parent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertycache.html#parent

    Returns
    -------

    ConstPtr
      A new cute QQmlPropertyCache::ConstPtr around the copy Qt gave back.
      Python owns it.
    """
    #  const QQmlPropertyCache::ConstPtr &QQmlPropertyCache::parent() const
    address = self.uglySide.call('ritual_ZNK17QQmlPropertyCache6parentEv')
    return QQmlPropertyCache.ConstPtr._cuteOwning(address)

  @overload(QQmlPropertyData)
  @overload(NoneType)
  def overrideData(
      self,
      a0: Optional[QQmlPropertyData],
  ) -> Optional[QQmlPropertyData]:
    """
    Calls Qt's 'const QQmlPropertyData *QQmlPropertyCache::overrideData(const
    QQmlPropertyData *a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycache.html#overrideData

    Parameters
    ----------

    a0 : Optional[QQmlPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQmlPropertyData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QQmlPropertyData *QQmlPropertyCache::overrideData(const
    #      QQmlPropertyData *a0) const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlPropertyCache12overrideDataEPK16QQmlPropertyData',
        self._addressOf(a0),
    )
    return QQmlPropertyData._cuteAt(address)

  @overload(QQmlPropertyData)
  @overload(NoneType)
  def isAllowedInRevision(self, a0: Optional[QQmlPropertyData]) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyCache::isAllowedInRevision(const
    QQmlPropertyData *a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycache.html#isAllowedInRevision

    Parameters
    ----------

    a0 : Optional[QQmlPropertyData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQmlPropertyCache::isAllowedInRevision(const QQmlPropertyData
    #      *a0) const
    return self.uglySide.call(
        'ritual_ZNK17QQmlPropertyCache19isAllowedInRevisionEPK16QQmlPropert'
        'yData',
        self._addressOf(a0),
    )

  @overload(int)
  def originalClone(self, index: int) -> int:
    """
    Calls Qt's 'int QQmlPropertyCache::originalClone(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycache.html#originalClone

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  int QQmlPropertyCache::originalClone(int index) const
    return self.uglySide.call(
        'ritual_ZNK17QQmlPropertyCache13originalCloneEi', index,
    )

  @staticmethod
  @overload(QObject, int)
  @overload(NoneType, int)
  def originalClone(a0: Optional[QObject], index: int) -> int:
    """
    Calls Qt's 'int QQmlPropertyCache::originalClone(const QObject *a0, int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycache.html#originalClone

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    index : int
      Passed on as it is.
    """
    #  int QQmlPropertyCache::originalClone(const QObject *a0, int index)
    return Rituals.call(
        'ritual_ZN17QQmlPropertyCache13originalCloneEPK7QObjecti',
        CuteMixin._addressOf(a0, 'QObject'), index,
    )

  @overload(int)
  def signalParameterNames(self, index: int) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QQmlPropertyCache::signalParameterNames(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycache.html#signalParameterNames

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QQmlPropertyCache::signalParameterNames(int index)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlPropertyCache20signalParameterNamesEi', index,
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  def className(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QQmlPropertyCache::className() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertycache.html#className

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QQmlPropertyCache::className() const
    chars = self.uglySide.call('ritual_ZNK17QQmlPropertyCache9classNameEv')
    return None if chars is None else chars.decode()

  def propertyCount(self) -> int:
    """
    Calls Qt's 'int QQmlPropertyCache::propertyCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycache.html#propertyCount
    """
    #  int QQmlPropertyCache::propertyCount() const
    return self.uglySide.call(
        'ritual_ZNK17QQmlPropertyCache13propertyCountEv',
    )

  def ownPropertyCount(self) -> int:
    """
    Calls Qt's 'int QQmlPropertyCache::ownPropertyCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycache.html#ownPropertyCount
    """
    #  int QQmlPropertyCache::ownPropertyCount() const
    return self.uglySide.call(
        'ritual_ZNK17QQmlPropertyCache16ownPropertyCountEv',
    )

  def propertyOffset(self) -> int:
    """
    Calls Qt's 'int QQmlPropertyCache::propertyOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycache.html#propertyOffset
    """
    #  int QQmlPropertyCache::propertyOffset() const
    return self.uglySide.call(
        'ritual_ZNK17QQmlPropertyCache14propertyOffsetEv',
    )

  def methodCount(self) -> int:
    """
    Calls Qt's 'int QQmlPropertyCache::methodCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertycache.html#methodCount
    """
    #  int QQmlPropertyCache::methodCount() const
    return self.uglySide.call('ritual_ZNK17QQmlPropertyCache11methodCountEv')

  def ownMethodCount(self) -> int:
    """
    Calls Qt's 'int QQmlPropertyCache::ownMethodCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycache.html#ownMethodCount
    """
    #  int QQmlPropertyCache::ownMethodCount() const
    return self.uglySide.call(
        'ritual_ZNK17QQmlPropertyCache14ownMethodCountEv',
    )

  def methodOffset(self) -> int:
    """
    Calls Qt's 'int QQmlPropertyCache::methodOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycache.html#methodOffset
    """
    #  int QQmlPropertyCache::methodOffset() const
    return self.uglySide.call(
        'ritual_ZNK17QQmlPropertyCache12methodOffsetEv',
    )

  def signalCount(self) -> int:
    """
    Calls Qt's 'int QQmlPropertyCache::signalCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertycache.html#signalCount
    """
    #  int QQmlPropertyCache::signalCount() const
    return self.uglySide.call('ritual_ZNK17QQmlPropertyCache11signalCountEv')

  def ownSignalCount(self) -> int:
    """
    Calls Qt's 'int QQmlPropertyCache::ownSignalCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycache.html#ownSignalCount
    """
    #  int QQmlPropertyCache::ownSignalCount() const
    return self.uglySide.call(
        'ritual_ZNK17QQmlPropertyCache14ownSignalCountEv',
    )

  def signalOffset(self) -> int:
    """
    Calls Qt's 'int QQmlPropertyCache::signalOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycache.html#signalOffset
    """
    #  int QQmlPropertyCache::signalOffset() const
    return self.uglySide.call(
        'ritual_ZNK17QQmlPropertyCache12signalOffsetEv',
    )

  def ownEnumCount(self) -> int:
    """
    Calls Qt's 'int QQmlPropertyCache::ownEnumCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycache.html#ownEnumCount
    """
    #  int QQmlPropertyCache::ownEnumCount() const
    return self.uglySide.call(
        'ritual_ZNK17QQmlPropertyCache12ownEnumCountEv',
    )

  @overload(int)
  def allowedRevision(self, index: int) -> QTypeRevision:
    """
    Calls Qt's 'QTypeRevision QQmlPropertyCache::allowedRevision(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycache.html#allowedRevision

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QTypeRevision
      A new cute QTypeRevision around the copy Qt gave back. Python owns it.
    """
    #  QTypeRevision QQmlPropertyCache::allowedRevision(int index) const
    address = self.uglySide.call(
        'ritual_ZNK17QQmlPropertyCache15allowedRevisionEi', index,
    )
    from ..QtCore import QTypeRevision
    return QTypeRevision._cuteOwning(address)

  def isComposite(self) -> bool:
    """
    Calls Qt's 'bool QQmlPropertyCache::isComposite() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertycache.html#isComposite
    """
    #  bool QQmlPropertyCache::isComposite() const
    return self.uglySide.call('ritual_ZNK17QQmlPropertyCache11isCompositeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(ConstPtr)
  def setParent(self, newParent: ConstPtr) -> None:
    """
    Calls Qt's 'void QQmlPropertyCache::setParent(QQmlPropertyCache::ConstPtr
    newParent)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertycache.html#setParent

    Parameters
    ----------

    newParent : ConstPtr
      Passed on as a value: Qt reads the C++ QQmlPropertyCache::ConstPtr,
      which stays Python's own.
    """
    #  void QQmlPropertyCache::setParent(QQmlPropertyCache::ConstPtr
    #      newParent)
    self.uglySide.call(
        'ritual_ZN17QQmlPropertyCache9setParentENS_8ConstPtrE',
        self._valueOf(newParent),
    )

  @overload(int, QTypeRevision)
  def setAllowedRevision(self, index: int, allowed: QTypeRevision) -> None:
    """
    Calls Qt's 'void QQmlPropertyCache::setAllowedRevision(int index,
    QTypeRevision allowed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycache.html#setAllowedRevision

    Parameters
    ----------

    index : int
      Passed on as it is.

    allowed : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.
    """
    #  void QQmlPropertyCache::setAllowedRevision(int index, QTypeRevision
    #      allowed)
    self.uglySide.call(
        'ritual_ZN17QQmlPropertyCache18setAllowedRevisionEi13QTypeRevision',
        index, self._valueOf(allowed),
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
    - Qt's
      'QQmlPropertyCache::QQmlPropertyCache(OverrideSemantics::HandlerRef
      handleOverride)': takes a type Python has no way to hand over yet.
    - Qt's 'QQmlPropertyCache::QQmlPropertyCache(const QQmlMetaObjectPointer
      &metaObject, OverrideSemantics::HandlerRef handleOverride)': takes a
      type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyCache.__init__' has no cute function yet. Qt's "
        "'QQmlPropertyCache::QQmlPropertyCache(OverrideSemantics::HandlerRef"
        " handleOverride)': takes a type Python has no way to hand over "
        "yet. Qt's 'QQmlPropertyCache::QQmlPropertyCache(const "
        "QQmlMetaObjectPointer &metaObject, OverrideSemantics::HandlerRef "
        "handleOverride)': takes a type Python has no way to hand over yet.")

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

  @overload(QMetaObject)
  @overload(NoneType)
  def update(self, a0: Optional[QMetaObject]) -> None:
    """
    Calls Qt's 'void QQmlPropertyCache::update(const QMetaObject *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertycache.html#update

    Parameters
    ----------

    a0 : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlPropertyCache::update(const QMetaObject *a0)
    self.uglySide.call(
        'ritual_ZN17QQmlPropertyCache6updateEPK11QMetaObject',
        self._addressOf(a0, 'QMetaObject'),
    )

  @overload(QMetaObject)
  @overload(NoneType)
  def invalidate(self, a0: Optional[QMetaObject]) -> None:
    """
    Calls Qt's 'void QQmlPropertyCache::invalidate(const QMetaObject *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertycache.html#invalidate

    Parameters
    ----------

    a0 : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlPropertyCache::invalidate(const QMetaObject *a0)
    self.uglySide.call(
        'ritual_ZN17QQmlPropertyCache10invalidateEPK11QMetaObject',
        self._addressOf(a0, 'QMetaObject'),
    )

  @overload(QMetaObject, QTypeRevision)
  @overload(NoneType, QTypeRevision)
  @overload(QMetaObject, QTypeRevision, QQmlPropertyData.Flags)
  @overload(NoneType, QTypeRevision, QQmlPropertyData.Flags)
  @overload(
      QMetaObject, QTypeRevision, QQmlPropertyData.Flags,
      QQmlPropertyData.Flags,
  )
  @overload(
      NoneType, QTypeRevision, QQmlPropertyData.Flags,
      QQmlPropertyData.Flags,
  )
  @overload(
      QMetaObject, QTypeRevision, QQmlPropertyData.Flags,
      QQmlPropertyData.Flags, QQmlPropertyData.Flags,
  )
  @overload(
      NoneType, QTypeRevision, QQmlPropertyData.Flags,
      QQmlPropertyData.Flags, QQmlPropertyData.Flags,
  )
  def append(
      self,
      a0: Optional[QMetaObject],
      typeVersion: QTypeRevision,
      propertyFlags: Optional[QQmlPropertyData.Flags] = None,
      methodFlags: Optional[QQmlPropertyData.Flags] = None,
      signalFlags: Optional[QQmlPropertyData.Flags] = None,
  ) -> None:
    """
    Calls Qt's 'void QQmlPropertyCache::append(const QMetaObject *a0,
    QTypeRevision typeVersion, QQmlPropertyData::Flags propertyFlags,
    QQmlPropertyData::Flags methodFlags, QQmlPropertyData::Flags
    signalFlags)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertycache.html#append

    Parameters
    ----------

    a0 : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    typeVersion : QTypeRevision
      Passed on as a value: Qt reads the C++ QTypeRevision, which stays
      Python's own.

    propertyFlags : Optional[QQmlPropertyData.Flags]
      Passed on as a value: Qt reads the C++ QQmlPropertyData::Flags, which
      stays Python's own. May be left out, as in Qt: a new
      'QQmlPropertyData.Flags()' is then passed on.

    methodFlags : Optional[QQmlPropertyData.Flags]
      Passed on as a value: Qt reads the C++ QQmlPropertyData::Flags, which
      stays Python's own. May be left out, as in Qt: a new
      'QQmlPropertyData.Flags()' is then passed on.

    signalFlags : Optional[QQmlPropertyData.Flags]
      Passed on as a value: Qt reads the C++ QQmlPropertyData::Flags, which
      stays Python's own. May be left out, as in Qt: a new
      'QQmlPropertyData.Flags()' is then passed on.
    """
    #  void QQmlPropertyCache::append(const QMetaObject *a0, QTypeRevision
    #      typeVersion, QQmlPropertyData::Flags propertyFlags,
    #      QQmlPropertyData::Flags methodFlags, QQmlPropertyData::Flags
    #      signalFlags)
    if propertyFlags is None:
      propertyFlags = QQmlPropertyData.Flags()
    if methodFlags is None:
      methodFlags = QQmlPropertyData.Flags()
    if signalFlags is None:
      signalFlags = QQmlPropertyData.Flags()
    self.uglySide.call(
        'ritual_ZN17QQmlPropertyCache6appendEPK11QMetaObject13QTypeRevision'
        'N16QQmlPropertyData5FlagsES5_S5_',
        self._addressOf(a0, 'QMetaObject'), self._valueOf(typeVersion),
        self._valueOf(propertyFlags), self._valueOf(methodFlags),
        self._valueOf(signalFlags),
    )

  @overload(str, QQmlPropertyData.Flags, int, QMetaType, QList[QByteArray])
  @overload(str, QQmlPropertyData.Flags, int, NoneType, QList[QByteArray])
  def appendSignal(
      self,
      a0: str,
      a1: QQmlPropertyData.Flags,
      coreIndex: int,
      types: Optional[QMetaType],
      names: QList[QByteArray],
  ) -> None:
    """
    Calls Qt's 'void QQmlPropertyCache::appendSignal(const QString &a0,
    QQmlPropertyData::Flags a1, int coreIndex, const QMetaType *types, const
    QList<QByteArray> &names)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycache.html#appendSignal

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    a1 : QQmlPropertyData.Flags
      Passed on as a value: Qt reads the C++ QQmlPropertyData::Flags, which
      stays Python's own.

    coreIndex : int
      Passed on as it is.

    types : Optional[QMetaType]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    names : QList[QByteArray]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlPropertyCache::appendSignal(const QString &a0,
    #      QQmlPropertyData::Flags a1, int coreIndex, const QMetaType *types,
    #      const QList<QByteArray> &names)
    self.uglySide.call(
        'ritual_ZN17QQmlPropertyCache12appendSignalERK7QStringN16QQmlProper'
        'tyData5FlagsEiPK9QMetaTypeRK5QListI10QByteArrayE',
        a0, self._valueOf(a1), coreIndex, self._addressOf(types),
        self._valueOf(names),
    )

  @overload(
      str, QQmlPropertyData.Flags, int, QMetaType, QList[QByteArray],
      QList[QMetaType],
  )
  def appendMethod(
      self,
      a0: str,
      flags: QQmlPropertyData.Flags,
      coreIndex: int,
      returnType: QMetaType,
      names: QList[QByteArray],
      parameterTypes: QList[QMetaType],
  ) -> None:
    """
    Calls Qt's 'void QQmlPropertyCache::appendMethod(const QString &a0,
    QQmlPropertyData::Flags flags, int coreIndex, QMetaType returnType, const
    QList<QByteArray> &names, const QList<QMetaType> &parameterTypes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycache.html#appendMethod

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    flags : QQmlPropertyData.Flags
      Passed on as a value: Qt reads the C++ QQmlPropertyData::Flags, which
      stays Python's own.

    coreIndex : int
      Passed on as it is.

    returnType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    names : QList[QByteArray]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    parameterTypes : QList[QMetaType]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlPropertyCache::appendMethod(const QString &a0,
    #      QQmlPropertyData::Flags flags, int coreIndex, QMetaType
    #      returnType, const QList<QByteArray> &names, const QList<QMetaType>
    #      &parameterTypes)
    self.uglySide.call(
        'ritual_ZN17QQmlPropertyCache12appendMethodERK7QStringN16QQmlProper'
        'tyData5FlagsEi9QMetaTypeRK5QListI10QByteArrayERKS6_IS5_E',
        a0, self._valueOf(flags), coreIndex, self._valueOf(returnType),
        self._valueOf(names), self._valueOf(parameterTypes),
    )

  @overload(str, QList[QQmlEnumValue])
  def appendEnum(self, a0: str, a1: QList[QQmlEnumValue]) -> None:
    """
    Calls Qt's 'void QQmlPropertyCache::appendEnum(const QString &a0, const
    QList<QQmlEnumValue> &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlpropertycache.html#appendEnum

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    a1 : QList[QQmlEnumValue]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlPropertyCache::appendEnum(const QString &a0, const
    #      QList<QQmlEnumValue> &a1)
    self.uglySide.call(
        'ritual_ZN17QQmlPropertyCache10appendEnumERK7QStringRK5QListI13QQml'
        'EnumValueE',
        a0, self._valueOf(a1),
    )

  @overload(int, QList[QByteArray])
  def createArgumentsObject(
      self,
      count: int,
      names: QList[QByteArray],
  ) -> Optional[QQmlPropertyCacheMethodArguments]:
    """
    Calls Qt's 'QQmlPropertyCacheMethodArguments
    *QQmlPropertyCache::createArgumentsObject(int count, const
    QList<QByteArray> &names)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlpropertycache.html#createArgumentsObject

    Parameters
    ----------

    count : int
      Passed on as it is.

    names : QList[QByteArray]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    Optional[QQmlPropertyCacheMethodArguments]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlPropertyCacheMethodArguments
    #      *QQmlPropertyCache::createArgumentsObject(int count, const
    #      QList<QByteArray> &names)
    address = self.uglySide.call(
        'ritual_ZN17QQmlPropertyCache21createArgumentsObjectEiRK5QListI10QB'
        'yteArrayE',
        count, self._valueOf(names),
    )
    from . import QQmlPropertyCacheMethodArguments
    return QQmlPropertyCacheMethodArguments._cuteAt(address)

  @staticmethod
  def addToHash(*__, **_) -> Never:
    """
    Qt's 'bool QQmlPropertyCache::addToHash(QCryptographicHash &hash, const
    QMetaObject &mo)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyCache.addToHash' has no cute function yet. Qt's 'bool "
        "QQmlPropertyCache::addToHash(QCryptographicHash &hash, const "
        "QMetaObject &mo)': takes a type Python has no way to hand over yet."
    )

  @staticmethod
  def appendAlias(*__, **_) -> Never:
    """
    Qt's 'AppendResult QQmlPropertyCache::appendAlias(const QString &a0,
    QQmlPropertyData::Flags flags, int coreIndex, QMetaType propType,
    QTypeRevision version, int notifyIndex, int encodedTargetIndex, int
    targetObjectId)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyCache.appendAlias' has no cute function yet. Qt's "
        "'AppendResult QQmlPropertyCache::appendAlias(const QString &a0, "
        "QQmlPropertyData::Flags flags, int coreIndex, QMetaType propType, "
        "QTypeRevision version, int notifyIndex, int encodedTargetIndex, "
        "int targetObjectId)': gives a type Python has no way to take yet.")

  @staticmethod
  def appendComponentWrapper(*__, **_) -> Never:
    """
    Qt's 'AppendResult QQmlPropertyCache::appendComponentWrapper(int
    coreIndex, int wrappedObjectIndex)': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyCache.appendComponentWrapper' has no cute function "
        "yet. Qt's 'AppendResult "
        "QQmlPropertyCache::appendComponentWrapper(int coreIndex, int "
        "wrappedObjectIndex)': gives a type Python has no way to take yet.")

  @staticmethod
  def appendPropertyAttr(*__, **_) -> Never:
    """
    Qt's 'AppendResult QQmlPropertyCache::appendPropertyAttr(const QString
    &name, QQmlPropertyData &&data)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyCache.appendPropertyAttr' has no cute function yet. "
        "Qt's 'AppendResult QQmlPropertyCache::appendPropertyAttr(const "
        "QString &name, QQmlPropertyData &&data)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def callJSFactoryMethod(*__, **_) -> Never:
    """
    Qt's 'bool QQmlPropertyCache::callJSFactoryMethod(QObject *object, void
    **args) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyCache.callJSFactoryMethod' has no cute function yet. "
        "Qt's 'bool QQmlPropertyCache::callJSFactoryMethod(QObject *object, "
        "void **args) const': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def checksum(*__, **_) -> Never:
    """
    Qt's 'QByteArray QQmlPropertyCache::checksum(QHash<quintptr, QByteArray>
    *checksums, bool *ok) const': names 'QHash<quintptr, QByteArray>', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyCache.checksum' has no cute function yet. Qt's "
        "'QByteArray QQmlPropertyCache::checksum(QHash<quintptr, "
        "QByteArray> *checksums, bool *ok) const': names 'QHash<quintptr, "
        "QByteArray>', which has no cute class yet.")

  @staticmethod
  def copy(*__, **_) -> Never:
    """
    - Qt's 'QQmlPropertyCache::Ptr QQmlPropertyCache::copy() const': gives a
      type Python has no way to take yet.
    - Qt's 'QQmlPropertyCache::Ptr QQmlPropertyCache::copy(const
      QQmlMetaObjectPointer &mo, int reserve) const': takes a type Python has
      no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyCache.copy' has no cute function yet. Qt's "
        "'QQmlPropertyCache::Ptr QQmlPropertyCache::copy() const': gives a "
        "type Python has no way to take yet. Qt's 'QQmlPropertyCache::Ptr "
        "QQmlPropertyCache::copy(const QQmlMetaObjectPointer &mo, int "
        "reserve) const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def copyAndAppend(*__, **_) -> Never:
    """
    Qt's 'QQmlPropertyCache::Ptr QQmlPropertyCache::copyAndAppend(const
    QMetaObject *a0, QTypeRevision typeVersion, QQmlPropertyData::Flags
    propertyFlags, QQmlPropertyData::Flags methodFlags,
    QQmlPropertyData::Flags signalFlags) const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyCache.copyAndAppend' has no cute function yet. Qt's "
        "'QQmlPropertyCache::Ptr QQmlPropertyCache::copyAndAppend(const "
        "QMetaObject *a0, QTypeRevision typeVersion, "
        "QQmlPropertyData::Flags propertyFlags, QQmlPropertyData::Flags "
        "methodFlags, QQmlPropertyData::Flags signalFlags) const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def copyAndReserve(*__, **_) -> Never:
    """
    Qt's 'QQmlPropertyCache::Ptr QQmlPropertyCache::copyAndReserve(int
    propertyCount, int methodCount, int signalCount, int enumCount) const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyCache.copyAndReserve' has no cute function yet. Qt's "
        "'QQmlPropertyCache::Ptr QQmlPropertyCache::copyAndReserve(int "
        "propertyCount, int methodCount, int signalCount, int enumCount) "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def createStandalone(*__, **_) -> Never:
    """
    Qt's 'Ptr QQmlPropertyCache::createStandalone(const QMetaObject *a0,
    QTypeRevision metaObjectRevision)': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyCache.createStandalone' has no cute function yet. "
        "Qt's 'Ptr QQmlPropertyCache::createStandalone(const QMetaObject "
        "*a0, QTypeRevision metaObjectRevision)': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def determineMetaObjectSizes(*__, **_) -> Never:
    """
    Qt's 'bool QQmlPropertyCache::determineMetaObjectSizes(const QMetaObject
    &mo, int *fieldCount, int *stringCount)': takes a number to change where
    it is.
    """
    raise NotImplementedError(
        "'QQmlPropertyCache.determineMetaObjectSizes' has no cute function "
        "yet. Qt's 'bool QQmlPropertyCache::determineMetaObjectSizes(const "
        "QMetaObject &mo, int *fieldCount, int *stringCount)': takes a "
        "number to change where it is.")

  @staticmethod
  def findNamedProperty(*__, **_) -> Never:
    """
    Qt's 'QQmlPropertyCache::findNamedProperty': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QQmlPropertyCache.findNamedProperty' has no cute function yet. "
        "Qt's 'QQmlPropertyCache::findNamedProperty': a template: a pattern "
        "and no single function.")

  @staticmethod
  def findProperty(*__, **_) -> Never:
    """
    - Qt's 'const QQmlPropertyData
      *QQmlPropertyCache::findProperty(StringCache::ConstIterator it, QObject
      *a1, const QQmlRefPointer<QQmlContextData> &a2) const': the compiler
      refuses its ritual as it would be written here: use of undeclared
      identifier 'StringCache'.
    - Qt's 'const QQmlPropertyData
      *QQmlPropertyCache::findProperty(StringCache::ConstIterator it, const
      QQmlVMEMetaObject *a1, const QQmlRefPointer<QQmlContextData> &a2)
      const': the compiler refuses its ritual as it would be written here:
      use of undeclared identifier 'StringCache'.
    """
    raise NotImplementedError(
        "'QQmlPropertyCache.findProperty' has no cute function yet. Qt's "
        "'const QQmlPropertyData "
        "*QQmlPropertyCache::findProperty(StringCache::ConstIterator it, "
        "QObject *a1, const QQmlRefPointer<QQmlContextData> &a2) const': "
        "the compiler refuses its ritual as it would be written here: use "
        "of undeclared identifier 'StringCache'. Qt's 'const "
        "QQmlPropertyData "
        "*QQmlPropertyCache::findProperty(StringCache::ConstIterator it, "
        "const QQmlVMEMetaObject *a1, const QQmlRefPointer<QQmlContextData> "
        "&a2) const': the compiler refuses its ritual as it would be "
        "written here: use of undeclared identifier 'StringCache'.")

  @staticmethod
  def maybeLog(*__, **_) -> Never:
    """
    Qt's 'QQmlPropertyCache::maybeLog': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQmlPropertyCache.maybeLog' has no cute function yet. Qt's "
        "'QQmlPropertyCache::maybeLog': a template: a pattern and no single "
        "function.")

  @staticmethod
  def rebased(*__, **_) -> Never:
    """
    Qt's 'QQmlPropertyCache::Ptr QQmlPropertyCache::rebased(const
    QQmlPropertyCache::ConstPtr &parent) const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyCache.rebased' has no cute function yet. Qt's "
        "'QQmlPropertyCache::Ptr QQmlPropertyCache::rebased(const "
        "QQmlPropertyCache::ConstPtr &parent) const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def setNamedProperty(*__, **_) -> Never:
    """
    Qt's 'QQmlPropertyCache::setNamedProperty': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QQmlPropertyCache.setNamedProperty' has no cute function yet. "
        "Qt's 'QQmlPropertyCache::setNamedProperty': a template: a pattern "
        "and no single function.")

  @staticmethod
  def toMetaObjectBuilder(*__, **_) -> Never:
    """
    Qt's 'void QQmlPropertyCache::toMetaObjectBuilder(QMetaObjectBuilder &a0)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlPropertyCache.toMetaObjectBuilder' has no cute function yet. "
        "Qt's 'void "
        "QQmlPropertyCache::toMetaObjectBuilder(QMetaObjectBuilder &a0) "
        "const': takes a type Python has no way to hand over yet.")
