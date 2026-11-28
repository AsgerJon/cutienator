"""
QBluetoothServiceDiscoveryAgentPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothservicediscoveryagent_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QBluetoothServiceDiscoveryAgentPrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from . import QBluetoothDeviceDiscoveryAgent, QBluetoothServiceDiscoveryAgent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QBluetoothDeviceInfo, QBluetoothServiceInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBluetoothDeviceInfo = WAIT['QBluetoothDeviceInfo']
  QBluetoothServiceInfo = WAIT['QBluetoothServiceInfo']


class QBluetoothServiceDiscoveryAgentPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBluetoothServiceDiscoveryAgentPrivate: a plain
  Python object standing in front of one C++
  QBluetoothServiceDiscoveryAgentPrivate.

  What exists
  -----------

  Every function of Qt's QBluetoothServiceDiscoveryAgentPrivate that has a
  ritual and that Python can call so far, 9 names in all: 'q_func',
  'stopDeviceDiscovery', 'setDiscoveryState', 'discoveryState',
  'setDiscoveryMode', 'DiscoveryMode', '_q_deviceDiscovered',
  '_q_deviceDiscoveryError', 'isDuplicatedService'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QBluetoothServiceDiscoveryAgent
    *QBluetoothServiceDiscoveryAgentPrivate::q_func() const': takes in Python
    what 'QBluetoothServiceDiscoveryAgent
    *QBluetoothServiceDiscoveryAgentPrivate::q_func()' takes.

  What has no ritual
  ------------------

  17 of the 27 functions Qt declares: 6 leans on
  'QBluetoothServiceDiscoveryAgentPrivate; 5 Qt's library has no name for it,
  and its code in Qt's source does not compile apart from its file; 4 cannot
  be called and cannot be called through the meta-object and cannot be
  copied; 2 not a gap.

  What to expect
  --------------

  - The C++ QBluetoothServiceDiscoveryAgentPrivate is created at the first
    use, not by 'QBluetoothServiceDiscoveryAgentPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBluetoothServiceDiscoveryAgentPrivate.
  - Each name of Qt's QBluetoothServiceDiscoveryAgentPrivate that has no cute
    function yet, '__init__', '_q_deviceDiscoveryFinished',
    '_q_finishSdpScan', '_q_sdpScannerDone', '_q_serviceDiscoveryFinished',
    'parseServiceXml', 'performMinimalServiceDiscovery',
    'readAttributeValue', 'runExternalSdpScan', 'start',
    'startDeviceDiscovery', 'startServiceDiscovery', 'stop',
    'stopServiceDiscovery', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QBluetoothServiceDiscoveryAgentPrivate, each
  #  a class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class DiscoveryState(CuteNum):
    """
    The enum 'QBluetoothServiceDiscoveryAgentPrivate::DiscoveryState' of Qt,
    with the 3 names Qt gives in it.
    """

    Inactive = Kee[int](0)
    DeviceDiscovery = Kee[int](1)
    ServiceDiscovery = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBluetoothServiceDiscoveryAgentPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QBluetoothServiceInfo)
  def isDuplicatedService(self, serviceInfo: QBluetoothServiceInfo) -> bool:
    """
    Calls Qt's 'bool
    QBluetoothServiceDiscoveryAgentPrivate::isDuplicatedService(const
    QBluetoothServiceInfo &serviceInfo) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagentprivate.html

    Parameters
    ----------

    serviceInfo : QBluetoothServiceInfo
      Passed on as a value: Qt reads the C++ QBluetoothServiceInfo, which
      stays Python's own.
    """
    #  bool QBluetoothServiceDiscoveryAgentPrivate::isDuplicatedService(const
    #      QBluetoothServiceInfo &serviceInfo) const
    return self.uglySide.call(
        'ritual_ZNK38QBluetoothServiceDiscoveryAgentPrivate19isDuplicatedSe'
        'rviceERK21QBluetoothServiceInfo',
        self._valueOf(serviceInfo),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(DiscoveryState)
  def setDiscoveryState(self, s: DiscoveryState) -> None:
    """
    Calls Qt's 'void
    QBluetoothServiceDiscoveryAgentPrivate::setDiscoveryState(DiscoveryState
    s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagentprivate.html

    Parameters
    ----------

    s : DiscoveryState
      Passed on as its number.
    """
    #  void QBluetoothServiceDiscoveryAgentPrivate::setDiscoveryState(
    #      DiscoveryState s)
    self.uglySide.call(
        'ritual_ZN38QBluetoothServiceDiscoveryAgentPrivate17setDiscoverySta'
        'teENS_14DiscoveryStateE',
        s.value,
    )

  @overload(QBluetoothServiceDiscoveryAgent.DiscoveryMode)
  def setDiscoveryMode(
      self,
      m: QBluetoothServiceDiscoveryAgent.DiscoveryMode,
  ) -> None:
    """
    Calls Qt's 'void
    QBluetoothServiceDiscoveryAgentPrivate::setDiscoveryMode(
    QBluetoothServiceDiscoveryAgent::DiscoveryMode m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagentprivate.html

    Parameters
    ----------

    m : QBluetoothServiceDiscoveryAgent.DiscoveryMode
      Passed on as its number.
    """
    #  void QBluetoothServiceDiscoveryAgentPrivate::setDiscoveryMode(
    #      QBluetoothServiceDiscoveryAgent::DiscoveryMode m)
    self.uglySide.call(
        'ritual_ZN38QBluetoothServiceDiscoveryAgentPrivate16setDiscoveryMod'
        'eEN31QBluetoothServiceDiscoveryAgent13DiscoveryModeE',
        m.value,
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
    Qt's 'QBluetoothServiceDiscoveryAgentPrivate::
    QBluetoothServiceDiscoveryAgentPrivate(QBluetoothServiceDiscoveryAgent
    *qp, const QBluetoothAddress &deviceAdapter)': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QBluetoothServiceDiscoveryAgentPrivate.__init__' has no cute "
        "function yet. Qt's "
        "'QBluetoothServiceDiscoveryAgentPrivate::QBluetoothServiceDiscovery"
        "AgentPrivate(QBluetoothServiceDiscoveryAgent *qp, const "
        "QBluetoothAddress &deviceAdapter)': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

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

  def q_func(self) -> Optional[QBluetoothServiceDiscoveryAgent]:
    """
    Calls Qt's 'QBluetoothServiceDiscoveryAgent
    *QBluetoothServiceDiscoveryAgentPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagentprivate.html#q_func

    Returns
    -------

    Optional[QBluetoothServiceDiscoveryAgent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBluetoothServiceDiscoveryAgent
    #      *QBluetoothServiceDiscoveryAgentPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN38QBluetoothServiceDiscoveryAgentPrivate6q_funcEv',
    )
    return QBluetoothServiceDiscoveryAgent._cuteAt(address)

  def stopDeviceDiscovery(self) -> None:
    """
    Calls Qt's 'void
    QBluetoothServiceDiscoveryAgentPrivate::stopDeviceDiscovery()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagentprivate.html
    """
    #  void QBluetoothServiceDiscoveryAgentPrivate::stopDeviceDiscovery()
    self.uglySide.call(
        'ritual_ZN38QBluetoothServiceDiscoveryAgentPrivate19stopDeviceDisco'
        'veryEv',
    )

  def discoveryState(self) -> DiscoveryState:
    """
    Calls Qt's 'DiscoveryState
    QBluetoothServiceDiscoveryAgentPrivate::discoveryState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagentprivate.html

    Returns
    -------

    DiscoveryState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'DiscoveryState(number)'
      gives.
    """
    #  DiscoveryState
    #      QBluetoothServiceDiscoveryAgentPrivate::discoveryState()
    return QBluetoothServiceDiscoveryAgentPrivate.DiscoveryState(
        self.uglySide.call(
            'ritual_ZN38QBluetoothServiceDiscoveryAgentPrivate14discoverySt'
            'ateEv',
        ))

  def DiscoveryMode(self) -> QBluetoothServiceDiscoveryAgent.DiscoveryMode:
    """
    Calls Qt's 'QBluetoothServiceDiscoveryAgent::DiscoveryMode
    QBluetoothServiceDiscoveryAgentPrivate::DiscoveryMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagentprivate.html

    Returns
    -------

    QBluetoothServiceDiscoveryAgent.DiscoveryMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QBluetoothServiceDiscoveryAgent.DiscoveryMode(number)' gives.
    """
    #  QBluetoothServiceDiscoveryAgent::DiscoveryMode
    #      QBluetoothServiceDiscoveryAgentPrivate::DiscoveryMode()
    return QBluetoothServiceDiscoveryAgent.DiscoveryMode(self.uglySide.call(
        'ritual_ZN38QBluetoothServiceDiscoveryAgentPrivate13DiscoveryModeEv',
    ))

  @overload(QBluetoothDeviceInfo)
  def _q_deviceDiscovered(self, info: QBluetoothDeviceInfo) -> None:
    """
    Calls Qt's 'void
    QBluetoothServiceDiscoveryAgentPrivate::_q_deviceDiscovered(const
    QBluetoothDeviceInfo &info)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagentprivate.html

    Parameters
    ----------

    info : QBluetoothDeviceInfo
      Passed on as a value: Qt reads the C++ QBluetoothDeviceInfo, which
      stays Python's own.
    """
    #  void QBluetoothServiceDiscoveryAgentPrivate::_q_deviceDiscovered(const
    #      QBluetoothDeviceInfo &info)
    self.uglySide.call(
        'ritual_ZN38QBluetoothServiceDiscoveryAgentPrivate19_q_deviceDiscov'
        'eredERK20QBluetoothDeviceInfo',
        self._valueOf(info),
    )

  @overload(QBluetoothDeviceDiscoveryAgent.Error)
  def _q_deviceDiscoveryError(
      self,
      a0: QBluetoothDeviceDiscoveryAgent.Error,
  ) -> None:
    """
    Calls Qt's 'void
    QBluetoothServiceDiscoveryAgentPrivate::_q_deviceDiscoveryError(
    QBluetoothDeviceDiscoveryAgent::Error a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbluetoothservicediscoveryagentprivate.html

    Parameters
    ----------

    a0 : QBluetoothDeviceDiscoveryAgent.Error
      Passed on as its number.
    """
    #  void QBluetoothServiceDiscoveryAgentPrivate::_q_deviceDiscoveryError(
    #      QBluetoothDeviceDiscoveryAgent::Error a0)
    self.uglySide.call(
        'ritual_ZN38QBluetoothServiceDiscoveryAgentPrivate23_q_deviceDiscov'
        'eryErrorEN30QBluetoothDeviceDiscoveryAgent5ErrorE',
        a0.value,
    )

  @staticmethod
  def _q_deviceDiscoveryFinished(*__, **_) -> Never:
    """
    Qt's 'void
    QBluetoothServiceDiscoveryAgentPrivate::_q_deviceDiscoveryFinished()':
    leans on 'QBluetoothServiceDiscoveryAgentPrivate::start(QBluetoothAddress
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QBluetoothServiceDiscoveryAgentPrivate._q_deviceDiscoveryFinished'"
        " has no cute function yet. Qt's 'void "
        "QBluetoothServiceDiscoveryAgentPrivate::_q_deviceDiscoveryFinished("
        ")': leans on "
        "'QBluetoothServiceDiscoveryAgentPrivate::start(QBluetoothAddress "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def _q_finishSdpScan(*__, **_) -> Never:
    """
    Qt's 'void QBluetoothServiceDiscoveryAgentPrivate::_q_finishSdpScan(
    QBluetoothServiceDiscoveryAgent::Error errorCode, const QString
    &errorDescription, const QStringList &xmlRecords)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'QT_BT_BLUEZ'.
    """
    raise NotImplementedError(
        "'QBluetoothServiceDiscoveryAgentPrivate._q_finishSdpScan' has no "
        "cute function yet. Qt's 'void "
        "QBluetoothServiceDiscoveryAgentPrivate::_q_finishSdpScan(QBluetooth"
        "ServiceDiscoveryAgent::Error errorCode, const QString "
        "&errorDescription, const QStringList &xmlRecords)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'QT_BT_BLUEZ'.")

  @staticmethod
  def _q_sdpScannerDone(*__, **_) -> Never:
    """
    Qt's 'void QBluetoothServiceDiscoveryAgentPrivate::_q_sdpScannerDone(int
    exitCode, QProcess::ExitStatus status)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'QT_BT_BLUEZ'.
    """
    raise NotImplementedError(
        "'QBluetoothServiceDiscoveryAgentPrivate._q_sdpScannerDone' has no "
        "cute function yet. Qt's 'void "
        "QBluetoothServiceDiscoveryAgentPrivate::_q_sdpScannerDone(int "
        "exitCode, QProcess::ExitStatus status)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'QT_BT_BLUEZ'.")

  @staticmethod
  def _q_serviceDiscoveryFinished(*__, **_) -> Never:
    """
    Qt's 'void
    QBluetoothServiceDiscoveryAgentPrivate::_q_serviceDiscoveryFinished()':
    leans on 'QBluetoothServiceDiscoveryAgentPrivate::start(QBluetoothAddress
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QBluetoothServiceDiscoveryAgentPrivate._q_serviceDiscoveryFinished"
        "' has no cute function yet. Qt's 'void "
        "QBluetoothServiceDiscoveryAgentPrivate::_q_serviceDiscoveryFinished"
        "()': leans on "
        "'QBluetoothServiceDiscoveryAgentPrivate::start(QBluetoothAddress "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def parseServiceXml(*__, **_) -> Never:
    """
    Qt's 'QBluetoothServiceInfo
    QBluetoothServiceDiscoveryAgentPrivate::parseServiceXml(const QString
    &xml)': leans on
    'QBluetoothServiceDiscoveryAgentPrivate::readAttributeValue(
    QXmlStreamReader&, int)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QBluetoothServiceDiscoveryAgentPrivate.parseServiceXml' has no "
        "cute function yet. Qt's 'QBluetoothServiceInfo "
        "QBluetoothServiceDiscoveryAgentPrivate::parseServiceXml(const "
        "QString &xml)': leans on "
        "'QBluetoothServiceDiscoveryAgentPrivate::readAttributeValue(QXmlStr"
        "eamReader&, int)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def performMinimalServiceDiscovery(*__, **_) -> Never:
    """
    Qt's 'void
    QBluetoothServiceDiscoveryAgentPrivate::performMinimalServiceDiscovery(
    const QBluetoothAddress &deviceAddress)': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'ManagedObjectList'.
    """
    raise NotImplementedError(
        "'QBluetoothServiceDiscoveryAgentPrivate.performMinimalServiceDiscov"
        "ery' has no cute function yet. Qt's 'void "
        "QBluetoothServiceDiscoveryAgentPrivate::performMinimalServiceDiscov"
        "ery(const QBluetoothAddress &deviceAddress)': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'ManagedObjectList'.")

  @staticmethod
  def readAttributeValue(*__, **_) -> Never:
    """
    Qt's 'QVariant
    QBluetoothServiceDiscoveryAgentPrivate::readAttributeValue(
    QXmlStreamReader &xml, int depth)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'QT_BT_BLUEZ'.
    """
    raise NotImplementedError(
        "'QBluetoothServiceDiscoveryAgentPrivate.readAttributeValue' has no "
        "cute function yet. Qt's 'QVariant "
        "QBluetoothServiceDiscoveryAgentPrivate::readAttributeValue(QXmlStre"
        "amReader &xml, int depth)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: use "
        "of undeclared identifier 'QT_BT_BLUEZ'.")

  @staticmethod
  def runExternalSdpScan(*__, **_) -> Never:
    """
    Qt's 'void
    QBluetoothServiceDiscoveryAgentPrivate::runExternalSdpScan(const
    QBluetoothAddress &remoteAddress, const QBluetoothAddress
    &localAddress)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'QT_BT_BLUEZ'.
    """
    raise NotImplementedError(
        "'QBluetoothServiceDiscoveryAgentPrivate.runExternalSdpScan' has no "
        "cute function yet. Qt's 'void "
        "QBluetoothServiceDiscoveryAgentPrivate::runExternalSdpScan(const "
        "QBluetoothAddress &remoteAddress, const QBluetoothAddress "
        "&localAddress)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'QT_BT_BLUEZ'.")

  @staticmethod
  def start(*__, **_) -> Never:
    """
    Qt's 'void QBluetoothServiceDiscoveryAgentPrivate::start(const
    QBluetoothAddress &address)': cannot be called and cannot be called
    through the meta-object and cannot be copied: no header file has its
    code, Qt's source does not mark it or its class for use from outside Qt
    or writes it 'inline' or nowhere, and it is no signal, slot or invokable
    function giving back nothing, of a class built on QObject, and Qt's
    source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QBluetoothServiceDiscoveryAgentPrivate.start' has no cute "
        "function yet. Qt's 'void "
        "QBluetoothServiceDiscoveryAgentPrivate::start(const "
        "QBluetoothAddress &address)': cannot be called and cannot be "
        "called through the meta-object and cannot be copied: no header "
        "file has its code, Qt's source does not mark it or its class for "
        "use from outside Qt or writes it 'inline' or nowhere, and it is no "
        "signal, slot or invokable function giving back nothing, of a class "
        "built on QObject, and Qt's source has no code for it that could be "
        "told from the rest.")

  @staticmethod
  def startDeviceDiscovery(*__, **_) -> Never:
    """
    Qt's 'void
    QBluetoothServiceDiscoveryAgentPrivate::startDeviceDiscovery()': leans on
    'QBluetoothServiceDiscoveryAgentPrivate::start(QBluetoothAddress
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QBluetoothServiceDiscoveryAgentPrivate.startDeviceDiscovery' has "
        "no cute function yet. Qt's 'void "
        "QBluetoothServiceDiscoveryAgentPrivate::startDeviceDiscovery()': "
        "leans on "
        "'QBluetoothServiceDiscoveryAgentPrivate::start(QBluetoothAddress "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def startServiceDiscovery(*__, **_) -> Never:
    """
    Qt's 'void
    QBluetoothServiceDiscoveryAgentPrivate::startServiceDiscovery()': leans
    on 'QBluetoothServiceDiscoveryAgentPrivate::start(QBluetoothAddress
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QBluetoothServiceDiscoveryAgentPrivate.startServiceDiscovery' has "
        "no cute function yet. Qt's 'void "
        "QBluetoothServiceDiscoveryAgentPrivate::startServiceDiscovery()': "
        "leans on "
        "'QBluetoothServiceDiscoveryAgentPrivate::start(QBluetoothAddress "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

  @staticmethod
  def stop(*__, **_) -> Never:
    """
    Qt's 'void QBluetoothServiceDiscoveryAgentPrivate::stop()': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QBluetoothServiceDiscoveryAgentPrivate.stop' has no cute function "
        "yet. Qt's 'void QBluetoothServiceDiscoveryAgentPrivate::stop()': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def stopServiceDiscovery(*__, **_) -> Never:
    """
    Qt's 'void
    QBluetoothServiceDiscoveryAgentPrivate::stopServiceDiscovery()': leans on
    'QBluetoothServiceDiscoveryAgentPrivate::stop()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QBluetoothServiceDiscoveryAgentPrivate.stopServiceDiscovery' has "
        "no cute function yet. Qt's 'void "
        "QBluetoothServiceDiscoveryAgentPrivate::stopServiceDiscovery()': "
        "leans on 'QBluetoothServiceDiscoveryAgentPrivate::stop()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")
