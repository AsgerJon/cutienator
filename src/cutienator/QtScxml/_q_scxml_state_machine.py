"""
QScxmlStateMachine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/qscxmlstatemachine.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QMap, QMetaObject, QObject, QStringList
from . import QScxmlCompiler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QIODevice, QVariant
  from . import QScxmlDataModel, QScxmlError, QScxmlEvent
  from . import QScxmlInvokableService, QScxmlStateMachinePrivate
  from . import QScxmlTableData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIODevice = WAIT['QIODevice']
  QScxmlDataModel = WAIT['QScxmlDataModel']
  QScxmlEvent = WAIT['QScxmlEvent']
  QScxmlInvokableService = WAIT['QScxmlInvokableService']
  QScxmlTableData = WAIT['QScxmlTableData']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScxmlStateMachine(QObject):
  """
  The cute side of Qt's QScxmlStateMachine: a plain Python object standing in
  front of one C++ QScxmlStateMachine.

  It is built on the cute 'QObject', as Qt's QScxmlStateMachine is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScxmlStateMachine that has a ritual and that Python
  can call so far, 42 names in all: 'd_func', 'metaObject', 'tr', 'fromFile',
  'fromData', 'parseErrors', 'sessionId', 'isInvoked', 'isInitialized',
  'setDataModel', 'dataModel', 'setLoader', 'loader', 'isRunning',
  'setRunning', 'initialValues', 'setInitialValues', 'name', 'stateNames',
  'activeStateNames', 'isActive', 'connectToState', 'connectToEvent',
  'submitEvent', 'cancelDelayedEvent', 'isDispatchableTarget',
  'invokedServices', 'tableData', 'setTableData', 'runningChanged',
  'invokedServicesChanged', 'log', 'reachedStableState', 'finished',
  'dataModelChanged', 'initialValuesChanged', 'initializedChanged',
  'loaderChanged', 'tableDataChanged', 'start', 'stop', 'init'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QScxmlStateMachinePrivate *QScxmlStateMachine::d_func()
    const': takes in Python what 'QScxmlStateMachinePrivate
    *QScxmlStateMachine::d_func()' takes.
  - Qt's 'void *QScxmlStateMachine::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QScxmlStateMachine::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QScxmlStateMachine::QScxmlStateMachine(QScxmlStateMachinePrivate
    &dd, QObject *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'QBindable<bool> QScxmlStateMachine::bindableInitialized() const':
    gives a type Python has no way to take yet.
  - Qt's 'QBindable<QScxmlDataModel *>
    QScxmlStateMachine::bindableDataModel()': gives a type Python has no way
    to take yet.
  - Qt's 'QBindable<QScxmlCompiler::Loader *>
    QScxmlStateMachine::bindableLoader()': gives a type Python has no way to
    take yet.
  - Qt's 'QBindable<QVariantMap>
    QScxmlStateMachine::bindableInitialValues()': gives a type Python has no
    way to take yet.
  - Qt's 'std::function<void (bool)> QScxmlStateMachine::onEntry(const
    QObject *receiver, const char *method)': gives a type Python has no way
    to take yet.
  - Qt's 'std::function<void (bool)> QScxmlStateMachine::onExit(const QObject
    *receiver, const char *method)': gives a type Python has no way to take
    yet.
  - Qt's 'QBindable<QList<QScxmlInvokableService *>>
    QScxmlStateMachine::bindableInvokedServices()': gives a type Python has
    no way to take yet.
  - Qt's 'QBindable<QScxmlTableData *>
    QScxmlStateMachine::bindableTableData()': gives a type Python has no way
    to take yet.
  - Qt's 'QMetaObject::Connection
    QScxmlStateMachine::connectToStateImpl(const QString &scxmlStateName,
    const QObject *receiver, void **slot, QtPrivate::QSlotObjectBase
    *slotObj, Qt::ConnectionType type)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QMetaObject::Connection
    QScxmlStateMachine::connectToEventImpl(const QString &scxmlEventSpec,
    const QObject *receiver, void **slot, QtPrivate::QSlotObjectBase
    *slotObj, Qt::ConnectionType type)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  10 of the 70 functions Qt declares: 8 a template; 2 not a gap.

  What to expect
  --------------

  - The C++ QScxmlStateMachine is created at the first use, not by
    'QScxmlStateMachine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScxmlStateMachine.
  - Qt tells when it has removed the C++ QScxmlStateMachine. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QScxmlStateMachine that has no cute function yet,
    'bindableDataModel', 'bindableInitialValues', 'bindableInitialized',
    'bindableInvokedServices', 'bindableLoader', 'bindableTableData',
    'connectToEventImpl', 'connectToStateImpl', 'onEntry', 'onExit', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QScxmlStateMachine::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlstatemachine.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScxmlStateMachine::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QScxmlStateMachine2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(str)
  def fromFile(fileName: str) -> Optional[QScxmlStateMachine]:
    """
    Calls Qt's 'QScxmlStateMachine *QScxmlStateMachine::fromFile(const
    QString &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlstatemachine.html#fromFile

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QScxmlStateMachine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlStateMachine *QScxmlStateMachine::fromFile(const QString
    #      &fileName)
    address = Rituals.call(
        'ritual_ZN18QScxmlStateMachine8fromFileERK7QString', fileName,
    )
    return QScxmlStateMachine._cuteAt(address)

  @staticmethod
  @overload(QIODevice)
  @overload(NoneType)
  @overload(QIODevice, str)
  @overload(NoneType, str)
  def fromData(
      data: Optional[QIODevice],
      fileName: str = '',
  ) -> Optional[QScxmlStateMachine]:
    """
    Calls Qt's 'QScxmlStateMachine *QScxmlStateMachine::fromData(QIODevice
    *data, const QString &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlstatemachine.html#fromData

    Parameters
    ----------

    data : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    fileName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    Optional[QScxmlStateMachine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlStateMachine *QScxmlStateMachine::fromData(QIODevice *data,
    #      const QString &fileName)
    address = Rituals.call(
        'ritual_ZN18QScxmlStateMachine8fromDataEP9QIODeviceRK7QString',
        CuteMixin._addressOf(data), fileName,
    )
    return QScxmlStateMachine._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlStateMachine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QScxmlStateMachine::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlstatemachine.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QScxmlStateMachine::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QScxmlStateMachine10metaObjectEv',
    )
    return QMetaObject._cuteAt(address)

  def parseErrors(self) -> QList[QScxmlError]:
    """
    Calls Qt's 'QList<QScxmlError> QScxmlStateMachine::parseErrors() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachine.html#parseErrors

    Returns
    -------

    QList[QScxmlError]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QScxmlError> QScxmlStateMachine::parseErrors() const
    address = self.uglySide.call(
        'ritual_ZNK18QScxmlStateMachine11parseErrorsEv',
    )
    from . import QScxmlError
    return QList[QScxmlError]._cuteOwning(address)

  def sessionId(self) -> str:
    """
    Calls Qt's 'QString QScxmlStateMachine::sessionId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlstatemachine.html#sessionId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScxmlStateMachine::sessionId() const
    return self.uglySide.call('ritual_ZNK18QScxmlStateMachine9sessionIdEv')

  def isInvoked(self) -> bool:
    """
    Calls Qt's 'bool QScxmlStateMachine::isInvoked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlstatemachine.html#isInvoked
    """
    #  bool QScxmlStateMachine::isInvoked() const
    return self.uglySide.call('ritual_ZNK18QScxmlStateMachine9isInvokedEv')

  def isInitialized(self) -> bool:
    """
    Calls Qt's 'bool QScxmlStateMachine::isInitialized() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachine.html#isInitialized
    """
    #  bool QScxmlStateMachine::isInitialized() const
    return self.uglySide.call(
        'ritual_ZNK18QScxmlStateMachine13isInitializedEv',
    )

  def dataModel(self) -> Optional[QScxmlDataModel]:
    """
    Calls Qt's 'QScxmlDataModel *QScxmlStateMachine::dataModel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlstatemachine.html#dataModel

    Returns
    -------

    Optional[QScxmlDataModel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlDataModel *QScxmlStateMachine::dataModel() const
    address = self.uglySide.call(
        'ritual_ZNK18QScxmlStateMachine9dataModelEv',
    )
    from . import QScxmlDataModel
    return QScxmlDataModel._cuteAt(address)

  def loader(self) -> Optional[QScxmlCompiler.Loader]:
    """
    Calls Qt's 'QScxmlCompiler::Loader *QScxmlStateMachine::loader() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlstatemachine.html#loader

    Returns
    -------

    Optional[QScxmlCompiler.Loader]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlCompiler::Loader *QScxmlStateMachine::loader() const
    address = self.uglySide.call('ritual_ZNK18QScxmlStateMachine6loaderEv')
    return QScxmlCompiler.Loader._cuteAt(address)

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool QScxmlStateMachine::isRunning() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlstatemachine.html#isRunning
    """
    #  bool QScxmlStateMachine::isRunning() const
    return self.uglySide.call('ritual_ZNK18QScxmlStateMachine9isRunningEv')

  def name(self) -> str:
    """
    Calls Qt's 'QString QScxmlStateMachine::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlstatemachine.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScxmlStateMachine::name() const
    return self.uglySide.call('ritual_ZNK18QScxmlStateMachine4nameEv')

  @overload()
  @overload(bool)
  def stateNames(self, compress: bool = True) -> QStringList:
    """
    Calls Qt's 'QStringList QScxmlStateMachine::stateNames(bool compress)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlstatemachine.html#stateNames

    Parameters
    ----------

    compress : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QScxmlStateMachine::stateNames(bool compress) const
    address = self.uglySide.call(
        'ritual_ZNK18QScxmlStateMachine10stateNamesEb', compress,
    )
    return QStringList._cuteOwning(address)

  @overload()
  @overload(bool)
  def activeStateNames(self, compress: bool = True) -> QStringList:
    """
    Calls Qt's 'QStringList QScxmlStateMachine::activeStateNames(bool
    compress) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachine.html#activeStateNames

    Parameters
    ----------

    compress : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QScxmlStateMachine::activeStateNames(bool compress) const
    address = self.uglySide.call(
        'ritual_ZNK18QScxmlStateMachine16activeStateNamesEb', compress,
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def isActive(self, scxmlStateName: str) -> bool:
    """
    Calls Qt's 'bool QScxmlStateMachine::isActive(const QString
    &scxmlStateName) const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlstatemachine.html#isActive

    Parameters
    ----------

    scxmlStateName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QScxmlStateMachine::isActive(const QString &scxmlStateName) const
    return self.uglySide.call(
        'ritual_ZNK18QScxmlStateMachine8isActiveERK7QString', scxmlStateName,
    )

  @overload(int)
  def isActive(self, stateIndex: int) -> bool:
    """
    Calls Qt's 'bool QScxmlStateMachine::isActive(int stateIndex) const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlstatemachine.html#isActive

    Parameters
    ----------

    stateIndex : int
      Passed on as it is.
    """
    #  bool QScxmlStateMachine::isActive(int stateIndex) const
    return self.uglySide.call(
        'ritual_ZNK18QScxmlStateMachine8isActiveEi', stateIndex,
    )

  @overload(str)
  def isDispatchableTarget(self, target: str) -> bool:
    """
    Calls Qt's 'bool QScxmlStateMachine::isDispatchableTarget(const QString
    &target) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachine.html#isDispatchableTarget

    Parameters
    ----------

    target : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QScxmlStateMachine::isDispatchableTarget(const QString &target)
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QScxmlStateMachine20isDispatchableTargetERK7QString',
        target,
    )

  def invokedServices(self) -> QList[QScxmlInvokableService]:
    """
    Calls Qt's 'QList<QScxmlInvokableService *>
    QScxmlStateMachine::invokedServices() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachine.html#invokedServices

    Returns
    -------

    QList[QScxmlInvokableService]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QScxmlInvokableService *> QScxmlStateMachine::invokedServices()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QScxmlStateMachine15invokedServicesEv',
    )
    from . import QScxmlInvokableService
    return QList[QScxmlInvokableService]._cuteOwning(address)

  def tableData(self) -> Optional[QScxmlTableData]:
    """
    Calls Qt's 'QScxmlTableData *QScxmlStateMachine::tableData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlstatemachine.html#tableData

    Returns
    -------

    Optional[QScxmlTableData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlTableData *QScxmlStateMachine::tableData() const
    address = self.uglySide.call(
        'ritual_ZNK18QScxmlStateMachine9tableDataEv',
    )
    from . import QScxmlTableData
    return QScxmlTableData._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QScxmlDataModel)
  @overload(NoneType)
  def setDataModel(self, model: Optional[QScxmlDataModel]) -> None:
    """
    Calls Qt's 'void QScxmlStateMachine::setDataModel(QScxmlDataModel
    *model)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachine.html#setDataModel

    Parameters
    ----------

    model : Optional[QScxmlDataModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlStateMachine::setDataModel(QScxmlDataModel *model)
    self.uglySide.call(
        'ritual_ZN18QScxmlStateMachine12setDataModelEP15QScxmlDataModel',
        self._addressOf(model),
    )

  @overload(QScxmlCompiler.Loader)
  @overload(NoneType)
  def setLoader(self, loader: Optional[QScxmlCompiler.Loader]) -> None:
    """
    Calls Qt's 'void QScxmlStateMachine::setLoader(QScxmlCompiler::Loader
    *loader)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlstatemachine.html#setLoader

    Parameters
    ----------

    loader : Optional[QScxmlCompiler.Loader]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlStateMachine::setLoader(QScxmlCompiler::Loader *loader)
    self.uglySide.call(
        'ritual_ZN18QScxmlStateMachine9setLoaderEPN14QScxmlCompiler6LoaderE',
        self._addressOf(loader),
    )

  @overload(bool)
  def setRunning(self, running: bool) -> None:
    """
    Calls Qt's 'void QScxmlStateMachine::setRunning(bool running)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlstatemachine.html#setRunning

    Parameters
    ----------

    running : bool
      Passed on as it is.
    """
    #  void QScxmlStateMachine::setRunning(bool running)
    self.uglySide.call(
        'ritual_ZN18QScxmlStateMachine10setRunningEb', running,
    )

  @overload(QMap[str, QVariant])
  def setInitialValues(self, initialValues: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void QScxmlStateMachine::setInitialValues(const QVariantMap
    &initialValues)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachine.html#setInitialValues

    Parameters
    ----------

    initialValues : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QScxmlStateMachine::setInitialValues(const QVariantMap
    #      &initialValues)
    self.uglySide.call(
        'ritual_ZN18QScxmlStateMachine16setInitialValuesERK4QMapI7QString8Q'
        'VariantE',
        self._valueOf(initialValues),
    )

  @overload(QScxmlTableData)
  @overload(NoneType)
  def setTableData(self, tableData: Optional[QScxmlTableData]) -> None:
    """
    Calls Qt's 'void QScxmlStateMachine::setTableData(QScxmlTableData
    *tableData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachine.html#setTableData

    Parameters
    ----------

    tableData : Optional[QScxmlTableData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlStateMachine::setTableData(QScxmlTableData *tableData)
    self.uglySide.call(
        'ritual_ZN18QScxmlStateMachine12setTableDataEP15QScxmlTableData',
        self._addressOf(tableData),
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

  @overload(QMetaObject)
  @overload(NoneType)
  @overload(QMetaObject, QObject)
  @overload(QMetaObject, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      metaObject: Optional[QMetaObject],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QScxmlStateMachine::QScxmlStateMachine(const QMetaObject *metaObject,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachine.html#QScxmlStateMachine

    Parameters
    ----------

    metaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QScxmlStateMachine::QScxmlStateMachine(const QMetaObject *metaObject,
    #      QObject *parent)
    self._noteCreation(QScxmlStateMachine, lambda: Rituals.call(
        'ritual_ZN18QScxmlStateMachineC1EPK11QMetaObjectP7QObject',
        self._addressOf(metaObject, 'QMetaObject'), self._addressOf(parent,
        'QObject'),
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

  def d_func(self) -> Optional[QScxmlStateMachinePrivate]:
    """
    Calls Qt's 'QScxmlStateMachinePrivate *QScxmlStateMachine::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlstatemachine.html#d_func

    Returns
    -------

    Optional[QScxmlStateMachinePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlStateMachinePrivate *QScxmlStateMachine::d_func()
    address = self.uglySide.call('ritual_ZN18QScxmlStateMachine6d_funcEv')
    from . import QScxmlStateMachinePrivate
    return QScxmlStateMachinePrivate._cuteAt(address)

  def initialValues(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QScxmlStateMachine::initialValues()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachine.html#initialValues

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QScxmlStateMachine::initialValues()
    address = self.uglySide.call(
        'ritual_ZN18QScxmlStateMachine13initialValuesEv',
    )
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  @overload(str, QObject, str)
  @overload(str, QObject, NoneType)
  @overload(str, NoneType, str)
  @overload(str, NoneType, NoneType)
  @overload(str, QObject, str, Qt.ConnectionType)
  @overload(str, QObject, NoneType, Qt.ConnectionType)
  @overload(str, NoneType, str, Qt.ConnectionType)
  @overload(str, NoneType, NoneType, Qt.ConnectionType)
  def connectToState(
      self,
      scxmlStateName: str,
      receiver: Optional[QObject],
      method: Optional[str],
      type: Qt.ConnectionType = Qt.ConnectionType.AutoConnection,
  ) -> QMetaObject.Connection:
    """
    Calls Qt's 'QMetaObject::Connection
    QScxmlStateMachine::connectToState(const QString &scxmlStateName, const
    QObject *receiver, const char *method, Qt::ConnectionType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachine.html#connectToState

    Parameters
    ----------

    scxmlStateName : str
      Passed on as it is: a QString is made of it for the call.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    method : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    type : Qt.ConnectionType
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ConnectionType.AutoConnection.

    Returns
    -------

    QMetaObject.Connection
      A new cute QMetaObject::Connection around the copy Qt gave back. Python
      owns it.
    """
    #  QMetaObject::Connection QScxmlStateMachine::connectToState(const
    #      QString &scxmlStateName, const QObject *receiver, const char
    #      *method, Qt::ConnectionType type)
    address = self.uglySide.call(
        'ritual_ZN18QScxmlStateMachine14connectToStateERK7QStringPK7QObject'
        'PKcN2Qt14ConnectionTypeE',
        scxmlStateName, self._addressOf(receiver, 'QObject'),
        self._bytesOf(method), type.value,
    )
    return QMetaObject.Connection._cuteOwning(address)

  @overload(str, QObject, str)
  @overload(str, QObject, NoneType)
  @overload(str, NoneType, str)
  @overload(str, NoneType, NoneType)
  @overload(str, QObject, str, Qt.ConnectionType)
  @overload(str, QObject, NoneType, Qt.ConnectionType)
  @overload(str, NoneType, str, Qt.ConnectionType)
  @overload(str, NoneType, NoneType, Qt.ConnectionType)
  def connectToEvent(
      self,
      scxmlEventSpec: str,
      receiver: Optional[QObject],
      method: Optional[str],
      type: Qt.ConnectionType = Qt.ConnectionType.AutoConnection,
  ) -> QMetaObject.Connection:
    """
    Calls Qt's 'QMetaObject::Connection
    QScxmlStateMachine::connectToEvent(const QString &scxmlEventSpec, const
    QObject *receiver, const char *method, Qt::ConnectionType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachine.html#connectToEvent

    Parameters
    ----------

    scxmlEventSpec : str
      Passed on as it is: a QString is made of it for the call.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    method : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    type : Qt.ConnectionType
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ConnectionType.AutoConnection.

    Returns
    -------

    QMetaObject.Connection
      A new cute QMetaObject::Connection around the copy Qt gave back. Python
      owns it.
    """
    #  QMetaObject::Connection QScxmlStateMachine::connectToEvent(const
    #      QString &scxmlEventSpec, const QObject *receiver, const char
    #      *method, Qt::ConnectionType type)
    address = self.uglySide.call(
        'ritual_ZN18QScxmlStateMachine14connectToEventERK7QStringPK7QObject'
        'PKcN2Qt14ConnectionTypeE',
        scxmlEventSpec, self._addressOf(receiver, 'QObject'),
        self._bytesOf(method), type.value,
    )
    return QMetaObject.Connection._cuteOwning(address)

  @overload(QScxmlEvent)
  @overload(NoneType)
  def submitEvent(self, event: Optional[QScxmlEvent]) -> None:
    """
    Calls Qt's 'void QScxmlStateMachine::submitEvent(QScxmlEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachine.html#submitEvent

    Parameters
    ----------

    event : Optional[QScxmlEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlStateMachine::submitEvent(QScxmlEvent *event)
    self.uglySide.call(
        'ritual_ZN18QScxmlStateMachine11submitEventEP11QScxmlEvent',
        self._addressOf(event),
    )

  @overload(str)
  def submitEvent(self, eventName: str) -> None:
    """
    Calls Qt's 'void QScxmlStateMachine::submitEvent(const QString
    &eventName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachine.html#submitEvent

    Parameters
    ----------

    eventName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QScxmlStateMachine::submitEvent(const QString &eventName)
    self.uglySide.call(
        'ritual_ZN18QScxmlStateMachine11submitEventERK7QString', eventName,
    )

  @overload(str, QVariant)
  def submitEvent(self, eventName: str, data: QVariant) -> None:
    """
    Calls Qt's 'void QScxmlStateMachine::submitEvent(const QString
    &eventName, const QVariant &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachine.html#submitEvent

    Parameters
    ----------

    eventName : str
      Passed on as it is: a QString is made of it for the call.

    data : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QScxmlStateMachine::submitEvent(const QString &eventName, const
    #      QVariant &data)
    self.uglySide.call(
        'ritual_ZN18QScxmlStateMachine11submitEventERK7QStringRK8QVariant',
        eventName, self._valueOf(data),
    )

  @overload(str)
  def cancelDelayedEvent(self, sendId: str) -> None:
    """
    Calls Qt's 'void QScxmlStateMachine::cancelDelayedEvent(const QString
    &sendId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachine.html#cancelDelayedEvent

    Parameters
    ----------

    sendId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QScxmlStateMachine::cancelDelayedEvent(const QString &sendId)
    self.uglySide.call(
        'ritual_ZN18QScxmlStateMachine18cancelDelayedEventERK7QString',
        sendId,
    )

  @overload(bool)
  def runningChanged(self, running: bool) -> None:
    """
    Calls Qt's 'void QScxmlStateMachine::runningChanged(bool running)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachine.html#runningChanged

    Parameters
    ----------

    running : bool
      Passed on as it is.
    """
    #  void QScxmlStateMachine::runningChanged(bool running)
    self.uglySide.call(
        'ritual_ZN18QScxmlStateMachine14runningChangedEb', running,
    )

  @overload(QList[QScxmlInvokableService])
  def invokedServicesChanged(
      self,
      invokedServices: QList[QScxmlInvokableService],
  ) -> None:
    """
    Calls Qt's 'void QScxmlStateMachine::invokedServicesChanged(const
    QList<QScxmlInvokableService *> &invokedServices)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachine.html#invokedServicesChanged

    Parameters
    ----------

    invokedServices : QList[QScxmlInvokableService]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QScxmlStateMachine::invokedServicesChanged(const
    #      QList<QScxmlInvokableService *> &invokedServices)
    self.uglySide.call(
        'ritual_ZN18QScxmlStateMachine22invokedServicesChangedERK5QListIP22'
        'QScxmlInvokableServiceE',
        self._valueOf(invokedServices),
    )

  @overload(str, str)
  def log(self, label: str, msg: str) -> None:
    """
    Calls Qt's 'void QScxmlStateMachine::log(const QString &label, const
    QString &msg)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlstatemachine.html#log

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.

    msg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QScxmlStateMachine::log(const QString &label, const QString &msg)
    self.uglySide.call(
        'ritual_ZN18QScxmlStateMachine3logERK7QStringS2_', label, msg,
    )

  def reachedStableState(self) -> None:
    """
    Calls Qt's 'void QScxmlStateMachine::reachedStableState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachine.html#reachedStableState
    """
    #  void QScxmlStateMachine::reachedStableState()
    self.uglySide.call('ritual_ZN18QScxmlStateMachine18reachedStableStateEv')

  def finished(self) -> None:
    """
    Calls Qt's 'void QScxmlStateMachine::finished()'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlstatemachine.html#finished
    """
    #  void QScxmlStateMachine::finished()
    self.uglySide.call('ritual_ZN18QScxmlStateMachine8finishedEv')

  @overload(QScxmlDataModel)
  @overload(NoneType)
  def dataModelChanged(self, model: Optional[QScxmlDataModel]) -> None:
    """
    Calls Qt's 'void QScxmlStateMachine::dataModelChanged(QScxmlDataModel
    *model)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachine.html#dataModelChanged

    Parameters
    ----------

    model : Optional[QScxmlDataModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlStateMachine::dataModelChanged(QScxmlDataModel *model)
    self.uglySide.call(
        'ritual_ZN18QScxmlStateMachine16dataModelChangedEP15QScxmlDataModel',
        self._addressOf(model),
    )

  @overload(QMap[str, QVariant])
  def initialValuesChanged(self, initialValues: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void QScxmlStateMachine::initialValuesChanged(const
    QVariantMap &initialValues)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachine.html#initialValuesChanged

    Parameters
    ----------

    initialValues : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QScxmlStateMachine::initialValuesChanged(const QVariantMap
    #      &initialValues)
    self.uglySide.call(
        'ritual_ZN18QScxmlStateMachine20initialValuesChangedERK4QMapI7QStri'
        'ng8QVariantE',
        self._valueOf(initialValues),
    )

  @overload(bool)
  def initializedChanged(self, initialized: bool) -> None:
    """
    Calls Qt's 'void QScxmlStateMachine::initializedChanged(bool
    initialized)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachine.html#initializedChanged

    Parameters
    ----------

    initialized : bool
      Passed on as it is.
    """
    #  void QScxmlStateMachine::initializedChanged(bool initialized)
    self.uglySide.call(
        'ritual_ZN18QScxmlStateMachine18initializedChangedEb', initialized,
    )

  @overload(QScxmlCompiler.Loader)
  @overload(NoneType)
  def loaderChanged(self, loader: Optional[QScxmlCompiler.Loader]) -> None:
    """
    Calls Qt's 'void QScxmlStateMachine::loaderChanged(QScxmlCompiler::Loader
    *loader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachine.html#loaderChanged

    Parameters
    ----------

    loader : Optional[QScxmlCompiler.Loader]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlStateMachine::loaderChanged(QScxmlCompiler::Loader *loader)
    self.uglySide.call(
        'ritual_ZN18QScxmlStateMachine13loaderChangedEPN14QScxmlCompiler6Lo'
        'aderE',
        self._addressOf(loader),
    )

  @overload(QScxmlTableData)
  @overload(NoneType)
  def tableDataChanged(self, tableData: Optional[QScxmlTableData]) -> None:
    """
    Calls Qt's 'void QScxmlStateMachine::tableDataChanged(QScxmlTableData
    *tableData)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlstatemachine.html#tableDataChanged

    Parameters
    ----------

    tableData : Optional[QScxmlTableData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlStateMachine::tableDataChanged(QScxmlTableData *tableData)
    self.uglySide.call(
        'ritual_ZN18QScxmlStateMachine16tableDataChangedEP15QScxmlTableData',
        self._addressOf(tableData),
    )

  def start(self) -> None:
    """
    Calls Qt's 'void QScxmlStateMachine::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlstatemachine.html#start
    """
    #  void QScxmlStateMachine::start()
    self.uglySide.call('ritual_ZN18QScxmlStateMachine5startEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QScxmlStateMachine::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlstatemachine.html#stop
    """
    #  void QScxmlStateMachine::stop()
    self.uglySide.call('ritual_ZN18QScxmlStateMachine4stopEv')

  def init(self) -> bool:
    """
    Calls Qt's 'bool QScxmlStateMachine::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlstatemachine.html#init
    """
    #  bool QScxmlStateMachine::init()
    return self.uglySide.call('ritual_ZN18QScxmlStateMachine4initEv')

  @staticmethod
  def bindableDataModel(*__, **_) -> Never:
    """
    Qt's 'QBindable<QScxmlDataModel *>
    QScxmlStateMachine::bindableDataModel()': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QScxmlStateMachine.bindableDataModel' has no cute function yet. "
        "Qt's 'QBindable<QScxmlDataModel *> "
        "QScxmlStateMachine::bindableDataModel()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def bindableInitialValues(*__, **_) -> Never:
    """
    Qt's 'QBindable<QVariantMap>
    QScxmlStateMachine::bindableInitialValues()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QScxmlStateMachine.bindableInitialValues' has no cute function "
        "yet. Qt's 'QBindable<QVariantMap> "
        "QScxmlStateMachine::bindableInitialValues()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def bindableInitialized(*__, **_) -> Never:
    """
    Qt's 'QBindable<bool> QScxmlStateMachine::bindableInitialized() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QScxmlStateMachine.bindableInitialized' has no cute function yet. "
        "Qt's 'QBindable<bool> QScxmlStateMachine::bindableInitialized() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def bindableInvokedServices(*__, **_) -> Never:
    """
    Qt's 'QBindable<QList<QScxmlInvokableService *>>
    QScxmlStateMachine::bindableInvokedServices()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QScxmlStateMachine.bindableInvokedServices' has no cute function "
        "yet. Qt's 'QBindable<QList<QScxmlInvokableService *>> "
        "QScxmlStateMachine::bindableInvokedServices()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def bindableLoader(*__, **_) -> Never:
    """
    Qt's 'QBindable<QScxmlCompiler::Loader *>
    QScxmlStateMachine::bindableLoader()': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QScxmlStateMachine.bindableLoader' has no cute function yet. Qt's "
        "'QBindable<QScxmlCompiler::Loader *> "
        "QScxmlStateMachine::bindableLoader()': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def bindableTableData(*__, **_) -> Never:
    """
    Qt's 'QBindable<QScxmlTableData *>
    QScxmlStateMachine::bindableTableData()': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QScxmlStateMachine.bindableTableData' has no cute function yet. "
        "Qt's 'QBindable<QScxmlTableData *> "
        "QScxmlStateMachine::bindableTableData()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def connectToEventImpl(*__, **_) -> Never:
    """
    Qt's 'QMetaObject::Connection
    QScxmlStateMachine::connectToEventImpl(const QString &scxmlEventSpec,
    const QObject *receiver, void **slot, QtPrivate::QSlotObjectBase
    *slotObj, Qt::ConnectionType type)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QScxmlStateMachine.connectToEventImpl' has no cute function yet. "
        "Qt's 'QMetaObject::Connection "
        "QScxmlStateMachine::connectToEventImpl(const QString "
        "&scxmlEventSpec, const QObject *receiver, void **slot, "
        "QtPrivate::QSlotObjectBase *slotObj, Qt::ConnectionType type)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def connectToStateImpl(*__, **_) -> Never:
    """
    Qt's 'QMetaObject::Connection
    QScxmlStateMachine::connectToStateImpl(const QString &scxmlStateName,
    const QObject *receiver, void **slot, QtPrivate::QSlotObjectBase
    *slotObj, Qt::ConnectionType type)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QScxmlStateMachine.connectToStateImpl' has no cute function yet. "
        "Qt's 'QMetaObject::Connection "
        "QScxmlStateMachine::connectToStateImpl(const QString "
        "&scxmlStateName, const QObject *receiver, void **slot, "
        "QtPrivate::QSlotObjectBase *slotObj, Qt::ConnectionType type)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def onEntry(*__, **_) -> Never:
    """
    - Qt's 'std::function<void (bool)> QScxmlStateMachine::onEntry(const
      QObject *receiver, const char *method)': gives a type Python has no way
      to take yet.
    - Qt's 'QScxmlStateMachine::onEntry': a template: a pattern and no single
      function.
    """
    raise NotImplementedError(
        "'QScxmlStateMachine.onEntry' has no cute function yet. Qt's "
        "'std::function<void (bool)> QScxmlStateMachine::onEntry(const "
        "QObject *receiver, const char *method)': gives a type Python has "
        "no way to take yet. Qt's 'QScxmlStateMachine::onEntry': a "
        "template: a pattern and no single function.")

  @staticmethod
  def onExit(*__, **_) -> Never:
    """
    - Qt's 'std::function<void (bool)> QScxmlStateMachine::onExit(const
      QObject *receiver, const char *method)': gives a type Python has no way
      to take yet.
    - Qt's 'QScxmlStateMachine::onExit': a template: a pattern and no single
      function.
    """
    raise NotImplementedError(
        "'QScxmlStateMachine.onExit' has no cute function yet. Qt's "
        "'std::function<void (bool)> QScxmlStateMachine::onExit(const "
        "QObject *receiver, const char *method)': gives a type Python has "
        "no way to take yet. Qt's 'QScxmlStateMachine::onExit': a template: "
        "a pattern and no single function.")
