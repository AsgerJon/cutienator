"""
QDBusServiceWatcher binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/qdbusservicewatcher.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QDBusConnection
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusConnection = WAIT['QDBusConnection']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusServiceWatcher(QObject):
  """
  The cute side of Qt's QDBusServiceWatcher: a plain Python object standing
  in front of one C++ QDBusServiceWatcher.

  It is built on the cute 'QObject', as Qt's QDBusServiceWatcher is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDBusServiceWatcher that has a ritual and that
  Python can call so far, 13 names in all: 'metaObject', 'tr',
  'watchedServices', 'setWatchedServices', 'addWatchedService',
  'removeWatchedService', 'watchMode', 'setWatchMode', 'connection',
  'setConnection', 'serviceRegistered', 'serviceUnregistered',
  'serviceOwnerChanged'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDBusServiceWatcher::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QDBusServiceWatcher::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QDBusServiceWatcher::~QDBusServiceWatcher()': the destructor:
    Python never removes a C++ QDBusServiceWatcher.
  - Qt's 'QBindable<QStringList>
    QDBusServiceWatcher::bindableWatchedServices()': gives a type Python has
    no way to take yet.
  - Qt's 'QBindable<WatchMode> QDBusServiceWatcher::bindableWatchMode()':
    gives a type Python has no way to take yet.
  - Qt's 'QDBusServiceWatcherPrivate *QDBusServiceWatcher::d_func()': gives
    'QDBusServiceWatcherPrivate', which has no cute class yet.
  - Qt's 'const QDBusServiceWatcherPrivate *QDBusServiceWatcher::d_func()
    const': gives 'QDBusServiceWatcherPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 26 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QDBusServiceWatcher is created at the first use, not by
    'QDBusServiceWatcher(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDBusServiceWatcher.
  - Qt tells when it has removed the C++ QDBusServiceWatcher. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDBusServiceWatcher that has no cute function yet,
    'bindableWatchMode', 'bindableWatchedServices', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QDBusServiceWatcher, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class WatchModeFlag(CuteFlags):
    """
    The flags enum 'QDBusServiceWatcher::WatchModeFlag' of Qt, with the 3
    names Qt gives in it. Qt names the type of its combinations
    'QDBusServiceWatcher::WatchMode'.
    """

    WatchForRegistration = 0x1
    WatchForUnregistration = 0x2
    WatchForOwnerChange = 0x3

  WatchMode = WatchModeFlag

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
    Calls Qt's 'QString QDBusServiceWatcher::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusservicewatcher.html#tr

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
    #  QString QDBusServiceWatcher::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QDBusServiceWatcher2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusServiceWatcher'

  #  A C++ QDBusServiceWatcher Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDBusServiceWatcher'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDBusServiceWatcher::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusservicewatcher.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDBusServiceWatcher::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QDBusServiceWatcher10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def watchedServices(self) -> QStringList:
    """
    Calls Qt's 'QStringList QDBusServiceWatcher::watchedServices() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusservicewatcher.html#watchedServices

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QDBusServiceWatcher::watchedServices() const
    address = self.uglySide.call(
        'ritual_ZNK19QDBusServiceWatcher15watchedServicesEv',
    )
    return QStringList._cuteOwning(address)

  def watchMode(self) -> WatchMode:
    """
    Calls Qt's 'WatchMode QDBusServiceWatcher::watchMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbusservicewatcher.html#watchMode

    Returns
    -------

    WatchMode
      The value standing for the combination Qt gave back.
    """
    #  WatchMode QDBusServiceWatcher::watchMode() const
    return QDBusServiceWatcher.WatchMode(self.uglySide.call(
        'ritual_ZNK19QDBusServiceWatcher9watchModeEv',
    ))

  def connection(self) -> QDBusConnection:
    """
    Calls Qt's 'QDBusConnection QDBusServiceWatcher::connection() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusservicewatcher.html#connection

    Returns
    -------

    QDBusConnection
      A new cute QDBusConnection around the copy Qt gave back. Python owns
      it.
    """
    #  QDBusConnection QDBusServiceWatcher::connection() const
    address = self.uglySide.call(
        'ritual_ZNK19QDBusServiceWatcher10connectionEv',
    )
    from . import QDBusConnection
    return QDBusConnection._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStringList)
  def setWatchedServices(self, services: QStringList) -> None:
    """
    Calls Qt's 'void QDBusServiceWatcher::setWatchedServices(const
    QStringList &services)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusservicewatcher.html#setWatchedServices

    Parameters
    ----------

    services : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDBusServiceWatcher::setWatchedServices(const QStringList
    #      &services)
    self.uglySide.call(
        'ritual_ZN19QDBusServiceWatcher18setWatchedServicesERK5QListI7QStri'
        'ngE',
        self._valueOf(services),
    )

  @overload(WatchMode)
  def setWatchMode(self, mode: WatchMode) -> None:
    """
    Calls Qt's 'void QDBusServiceWatcher::setWatchMode(WatchMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusservicewatcher.html#setWatchMode

    Parameters
    ----------

    mode : WatchMode
      Passed on as its number.
    """
    #  void QDBusServiceWatcher::setWatchMode(WatchMode mode)
    self.uglySide.call(
        'ritual_ZN19QDBusServiceWatcher12setWatchModeE6QFlagsINS_13WatchMod'
        'eFlagEE',
        mode.value,
    )

  @overload(QDBusConnection)
  def setConnection(self, connection: QDBusConnection) -> None:
    """
    Calls Qt's 'void QDBusServiceWatcher::setConnection(const QDBusConnection
    &connection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusservicewatcher.html#setConnection

    Parameters
    ----------

    connection : QDBusConnection
      Passed on as a value: Qt reads the C++ QDBusConnection, which stays
      Python's own.
    """
    #  void QDBusServiceWatcher::setConnection(const QDBusConnection
    #      &connection)
    self.uglySide.call(
        'ritual_ZN19QDBusServiceWatcher13setConnectionERK15QDBusConnection',
        self._valueOf(connection),
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QDBusServiceWatcher::QDBusServiceWatcher(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusservicewatcher.html#QDBusServiceWatcher

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDBusServiceWatcher::QDBusServiceWatcher(QObject *parent)
    self._noteCreation(QDBusServiceWatcher, lambda: Rituals.call(
        'ritual_ZN19QDBusServiceWatcherC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(str, QDBusConnection)
  @overload(str, QDBusConnection, WatchMode)
  @overload(str, QDBusConnection, WatchMode, QObject)
  @overload(str, QDBusConnection, WatchMode, NoneType)
  def __init__(
      self,
      service: str,
      connection: QDBusConnection,
      watchMode: WatchMode = WatchMode.WatchForOwnerChange,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDBusServiceWatcher::QDBusServiceWatcher(const QString &service, const
    QDBusConnection &connection, WatchMode watchMode, QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusservicewatcher.html#QDBusServiceWatcher

    Parameters
    ----------

    service : str
      Passed on as it is: a QString is made of it for the call.

    connection : QDBusConnection
      Passed on as a value: Qt reads the C++ QDBusConnection, which stays
      Python's own.

    watchMode : WatchMode
      Passed on as its number. May be left out, as in Qt: it is then
      WatchMode.WatchForOwnerChange.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDBusServiceWatcher::QDBusServiceWatcher(const QString &service, const
    #      QDBusConnection &connection, WatchMode watchMode, QObject *parent)
    self._noteCreation(QDBusServiceWatcher, lambda: Rituals.call(
        'ritual_ZN19QDBusServiceWatcherC1ERK7QStringRK15QDBusConnection6QFl'
        'agsINS_13WatchModeFlagEEP7QObject',
        service, self._valueOf(connection), watchMode.value,
        self._addressOf(parent, 'QObject'),
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

  @overload(str)
  def addWatchedService(self, newService: str) -> None:
    """
    Calls Qt's 'void QDBusServiceWatcher::addWatchedService(const QString
    &newService)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusservicewatcher.html#addWatchedService

    Parameters
    ----------

    newService : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusServiceWatcher::addWatchedService(const QString &newService)
    self.uglySide.call(
        'ritual_ZN19QDBusServiceWatcher17addWatchedServiceERK7QString',
        newService,
    )

  @overload(str)
  def removeWatchedService(self, service: str) -> bool:
    """
    Calls Qt's 'bool QDBusServiceWatcher::removeWatchedService(const QString
    &service)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusservicewatcher.html#removeWatchedService

    Parameters
    ----------

    service : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDBusServiceWatcher::removeWatchedService(const QString &service)
    return self.uglySide.call(
        'ritual_ZN19QDBusServiceWatcher20removeWatchedServiceERK7QString',
        service,
    )

  @overload(str)
  def serviceRegistered(self, service: str) -> None:
    """
    Calls Qt's 'void QDBusServiceWatcher::serviceRegistered(const QString
    &service)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusservicewatcher.html#serviceRegistered

    Parameters
    ----------

    service : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusServiceWatcher::serviceRegistered(const QString &service)
    self.uglySide.call(
        'ritual_ZN19QDBusServiceWatcher17serviceRegisteredERK7QString',
        service,
    )

  @overload(str)
  def serviceUnregistered(self, service: str) -> None:
    """
    Calls Qt's 'void QDBusServiceWatcher::serviceUnregistered(const QString
    &service)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusservicewatcher.html#serviceUnregistered

    Parameters
    ----------

    service : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusServiceWatcher::serviceUnregistered(const QString &service)
    self.uglySide.call(
        'ritual_ZN19QDBusServiceWatcher19serviceUnregisteredERK7QString',
        service,
    )

  @overload(str, str, str)
  def serviceOwnerChanged(
      self,
      service: str,
      oldOwner: str,
      newOwner: str,
  ) -> None:
    """
    Calls Qt's 'void QDBusServiceWatcher::serviceOwnerChanged(const QString
    &service, const QString &oldOwner, const QString &newOwner)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbusservicewatcher.html#serviceOwnerChanged

    Parameters
    ----------

    service : str
      Passed on as it is: a QString is made of it for the call.

    oldOwner : str
      Passed on as it is: a QString is made of it for the call.

    newOwner : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDBusServiceWatcher::serviceOwnerChanged(const QString &service,
    #      const QString &oldOwner, const QString &newOwner)
    self.uglySide.call(
        'ritual_ZN19QDBusServiceWatcher19serviceOwnerChangedERK7QStringS2_S'
        '2_',
        service, oldOwner, newOwner,
    )

  @staticmethod
  def bindableWatchMode(*__, **_) -> Never:
    """
    Qt's 'QBindable<WatchMode> QDBusServiceWatcher::bindableWatchMode()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDBusServiceWatcher.bindableWatchMode' has no cute function yet. "
        "Qt's 'QBindable<WatchMode> "
        "QDBusServiceWatcher::bindableWatchMode()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def bindableWatchedServices(*__, **_) -> Never:
    """
    Qt's 'QBindable<QStringList>
    QDBusServiceWatcher::bindableWatchedServices()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QDBusServiceWatcher.bindableWatchedServices' has no cute function "
        "yet. Qt's 'QBindable<QStringList> "
        "QDBusServiceWatcher::bindableWatchedServices()': gives a type "
        "Python has no way to take yet.")
