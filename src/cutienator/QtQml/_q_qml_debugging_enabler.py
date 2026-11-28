"""
QQmlDebuggingEnabler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/qqmldebug.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QHash, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QQmlDebuggingEnabler(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlDebuggingEnabler: a plain Python object standing
  in front of one C++ QQmlDebuggingEnabler.

  C++ hands a QQmlDebuggingEnabler around as a copy, so every C++
  QQmlDebuggingEnabler behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlDebuggingEnabler that has a ritual and that
  Python can call so far, 9 names in all: 'enableDebugging',
  'debuggerServices', 'inspectorServices', 'profilerServices',
  'nativeDebuggerServices', 'setServices', 'startTcpDebugServer',
  'connectToLocalDebugger', 'startDebugConnector'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlDebuggingEnabler::~QQmlDebuggingEnabler()': the destructor:
    Python removes its C++ QQmlDebuggingEnabler by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QQmlDebuggingEnabler is created at the first use, not by
    'QQmlDebuggingEnabler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlDebuggingEnabler back gives a copy the ritual
    made for Python, in a new cute QQmlDebuggingEnabler.
  """

  #  The enums Qt writes inside QQmlDebuggingEnabler, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class StartMode(CuteNum):
    """
    The enum 'QQmlDebuggingEnabler::StartMode' of Qt, with the 2 names Qt
    gives in it.
    """

    DoNotWaitForClient = Kee[int](0)
    WaitForClient = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(bool)
  def enableDebugging(printWarning: bool) -> None:
    """
    Calls Qt's 'void QQmlDebuggingEnabler::enableDebugging(bool
    printWarning)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebuggingenabler.html#enableDebugging

    Parameters
    ----------

    printWarning : bool
      Passed on as it is.
    """
    #  void QQmlDebuggingEnabler::enableDebugging(bool printWarning)
    Rituals.call(
        'ritual_ZN20QQmlDebuggingEnabler15enableDebuggingEb', printWarning,
    )

  @staticmethod
  def debuggerServices() -> QStringList:
    """
    Calls Qt's 'QStringList QQmlDebuggingEnabler::debuggerServices()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebuggingenabler.html#debuggerServices

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlDebuggingEnabler::debuggerServices()
    address = Rituals.call(
        'ritual_ZN20QQmlDebuggingEnabler16debuggerServicesEv',
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  def inspectorServices() -> QStringList:
    """
    Calls Qt's 'QStringList QQmlDebuggingEnabler::inspectorServices()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebuggingenabler.html#inspectorServices

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlDebuggingEnabler::inspectorServices()
    address = Rituals.call(
        'ritual_ZN20QQmlDebuggingEnabler17inspectorServicesEv',
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  def profilerServices() -> QStringList:
    """
    Calls Qt's 'QStringList QQmlDebuggingEnabler::profilerServices()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebuggingenabler.html#profilerServices

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlDebuggingEnabler::profilerServices()
    address = Rituals.call(
        'ritual_ZN20QQmlDebuggingEnabler16profilerServicesEv',
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  def nativeDebuggerServices() -> QStringList:
    """
    Calls Qt's 'QStringList QQmlDebuggingEnabler::nativeDebuggerServices()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebuggingenabler.html#nativeDebuggerServices

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQmlDebuggingEnabler::nativeDebuggerServices()
    address = Rituals.call(
        'ritual_ZN20QQmlDebuggingEnabler22nativeDebuggerServicesEv',
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(QStringList)
  def setServices(services: QStringList) -> None:
    """
    Calls Qt's 'void QQmlDebuggingEnabler::setServices(const QStringList
    &services)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebuggingenabler.html#setServices

    Parameters
    ----------

    services : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlDebuggingEnabler::setServices(const QStringList &services)
    Rituals.call(
        'ritual_ZN20QQmlDebuggingEnabler11setServicesERK5QListI7QStringE',
        CuteMixin._valueOf(services),
    )

  @staticmethod
  @overload(int)
  @overload(int, StartMode)
  @overload(int, StartMode, str)
  def startTcpDebugServer(
      port: int,
      mode: StartMode = StartMode.DoNotWaitForClient,
      hostName: str = '',
  ) -> bool:
    """
    Calls Qt's 'bool QQmlDebuggingEnabler::startTcpDebugServer(int port,
    StartMode mode, const QString &hostName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebuggingenabler.html#startTcpDebugServer

    Parameters
    ----------

    port : int
      Passed on as it is.

    mode : StartMode
      Passed on as its number. May be left out, as in Qt: it is then
      StartMode.DoNotWaitForClient.

    hostName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  bool QQmlDebuggingEnabler::startTcpDebugServer(int port, StartMode
    #      mode, const QString &hostName)
    return Rituals.call(
        'ritual_ZN20QQmlDebuggingEnabler19startTcpDebugServerEiNS_9StartMod'
        'eERK7QString',
        port, mode.value, hostName,
    )

  @staticmethod
  @overload(str)
  @overload(str, StartMode)
  def connectToLocalDebugger(
      socketFileName: str,
      mode: StartMode = StartMode.DoNotWaitForClient,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlDebuggingEnabler::connectToLocalDebugger(const
    QString &socketFileName, StartMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebuggingenabler.html#connectToLocalDebugger

    Parameters
    ----------

    socketFileName : str
      Passed on as it is: a QString is made of it for the call.

    mode : StartMode
      Passed on as its number. May be left out, as in Qt: it is then
      StartMode.DoNotWaitForClient.
    """
    #  bool QQmlDebuggingEnabler::connectToLocalDebugger(const QString
    #      &socketFileName, StartMode mode)
    return Rituals.call(
        'ritual_ZN20QQmlDebuggingEnabler22connectToLocalDebuggerERK7QString'
        'NS_9StartModeE',
        socketFileName, mode.value,
    )

  @staticmethod
  @overload(str, QHash[str, QVariant])
  def startDebugConnector(
      pluginName: str,
      configuration: QHash[str, QVariant],
  ) -> bool:
    """
    Calls Qt's 'bool QQmlDebuggingEnabler::startDebugConnector(const QString
    &pluginName, const QVariantHash &configuration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebuggingenabler.html#startDebugConnector

    Parameters
    ----------

    pluginName : str
      Passed on as it is: a QString is made of it for the call.

    configuration : QHash[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  bool QQmlDebuggingEnabler::startDebugConnector(const QString
    #      &pluginName, const QVariantHash &configuration)
    return Rituals.call(
        'ritual_ZN20QQmlDebuggingEnabler19startDebugConnectorERK7QStringRK5'
        'QHashIS0_8QVariantE',
        pluginName, CuteMixin._valueOf(configuration),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlDebuggingEnabler'

  #  Qt's '~QQmlDebuggingEnabler()'. Naming it makes this a value class:
  #  Python owns every C++ QQmlDebuggingEnabler behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QQmlDebuggingEnablerD1Ev'

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

  @overload()
  @overload(bool)
  def __init__(self, printWarning: bool = True) -> None:
    """
    Notes what was given, for Qt's
    'QQmlDebuggingEnabler::QQmlDebuggingEnabler(bool printWarning)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebuggingenabler.html#QQmlDebuggingEnabler

    Parameters
    ----------

    printWarning : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  QQmlDebuggingEnabler::QQmlDebuggingEnabler(bool printWarning)
    self._noteCreation(QQmlDebuggingEnabler, lambda: Rituals.call(
        'ritual_ZN20QQmlDebuggingEnablerC1Eb', printWarning,
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
