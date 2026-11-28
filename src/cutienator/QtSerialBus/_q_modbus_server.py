"""
QModbusServer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/qmodbusserver.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QModbusDataUnit, QModbusDevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QModbusServerPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QModbusServer(QModbusDevice):
  """
  The cute side of Qt's QModbusServer: a plain Python object standing in
  front of one C++ QModbusServer.

  It is built on the cute 'QModbusDevice', as Qt's QModbusServer is built on
  Qt's QModbusDevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QModbusServer that has a ritual and that Python can
  call so far, 13 names in all: 'metaObject', 'tr', 'd_func',
  'serverAddress', 'setServerAddress', 'processesBroadcast', 'value',
  'setValue', 'data', 'setData', 'dataWritten', 'writeData', 'readData'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QModbusServer::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QModbusServer::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QModbusServerPrivate *QModbusServer::d_func() const': takes
    in Python what 'QModbusServerPrivate *QModbusServer::d_func()' takes.
  - Qt's 'QModbusServer::~QModbusServer()': the destructor: Python never
    removes a C++ QModbusServer.
  - Qt's 'bool QModbusServer::setMap(const QModbusDataUnitMap &map)': takes a
    type Python has no way to hand over yet.
  - Qt's 'bool QModbusServer::data(QModbusDataUnit::RegisterType table,
    quint16 address, quint16 *data) const': takes a number to change where it
    is.
  - Qt's 'QModbusServer::QModbusServer(QModbusServerPrivate &dd, QObject
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'QModbusResponse QModbusServer::processRequest(const QModbusPdu
    &request)': takes a type Python has no way to hand over yet.
  - Qt's 'QModbusResponse QModbusServer::processPrivateRequest(const
    QModbusPdu &request)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 26 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QModbusServer is created at the first use, not by
    'QModbusServer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QModbusServer.
  - Qt tells when it has removed the C++ QModbusServer. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QModbusServer that has no cute function yet,
    'processPrivateRequest', 'processRequest', 'setMap', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QModbusServer, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Option(CuteNum):
    """
    The enum 'QModbusServer::Option' of Qt, with the 10 names Qt gives in it.
    """

    DiagnosticRegister = Kee[int](0)
    ExceptionStatusOffset = Kee[int](1)
    DeviceBusy = Kee[int](2)
    AsciiInputDelimiter = Kee[int](3)
    ListenOnlyMode = Kee[int](4)
    ServerIdentifier = Kee[int](5)
    RunIndicatorStatus = Kee[int](6)
    AdditionalData = Kee[int](7)
    DeviceIdentification = Kee[int](8)
    UserOption = Kee[int](256)

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
    Calls Qt's 'QString QModbusServer::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusserver.html#tr

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
    #  QString QModbusServer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QModbusServer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QModbusServer'

  #  A C++ QModbusServer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QModbusServer'

  #  The functions Qt calls itself that QModbusServer is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'setMap': (
          'bool QModbusServer::setMap(const QModbusDataUnitMap &)',
      ),
      'processRequest': (
          'QModbusResponse QModbusServer::processRequest(const QModbusPdu '
          '&)',
      ),
      'processPrivateRequest': (
          'QModbusResponse QModbusServer::processPrivateRequest(const '
          'QModbusPdu &)',
      ),
  }

  #  The functions Qt calls itself that QModbusServer is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'processesBroadcast': (
          ('_ZNK13QModbusServer18processesBroadcastEv',
           ('bool', 'number', ''),
           ()),
      ),
      'value': (
          ('_ZNK13QModbusServer5valueEi',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('int', 'number', ''),
           )),
      ),
      'setValue': (
          ('_ZN13QModbusServer8setValueEiRK8QVariant',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'writeData': (
          ('_ZN13QModbusServer9writeDataERK15QModbusDataUnit',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtSerialBus:QModbusDataUnit'),
           )),
      ),
      'readData': (
          ('_ZNK13QModbusServer8readDataEP15QModbusDataUnit',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtSerialBus:QModbusDataUnit'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QModbusServer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusserver.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QModbusServer::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QModbusServer10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def serverAddress(self) -> int:
    """
    Calls Qt's 'int QModbusServer::serverAddress() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusserver.html#serverAddress
    """
    #  int QModbusServer::serverAddress() const
    return self.uglySide.call('ritual_ZNK13QModbusServer13serverAddressEv')

  def processesBroadcast(self) -> bool:
    """
    Calls Qt's 'bool QModbusServer::processesBroadcast() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusserver.html#processesBroadcast
    """
    #  bool QModbusServer::processesBroadcast() const
    ritual = 'ritual_ZNK13QModbusServer18processesBroadcastEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QModbusServer18processesBroadcastEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def value(self, option: int) -> QVariant:
    """
    Calls Qt's 'QVariant QModbusServer::value(int option) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusserver.html#value

    Parameters
    ----------

    option : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QModbusServer::value(int option) const
    ritual = 'ritual_ZNK13QModbusServer5valueEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QModbusServer5valueEi'
    address = self.uglySide.call(ritual, option)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QModbusDataUnit)
  @overload(NoneType)
  def data(self, newData: Optional[QModbusDataUnit]) -> bool:
    """
    Calls Qt's 'bool QModbusServer::data(QModbusDataUnit *newData) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusserver.html#data

    Parameters
    ----------

    newData : Optional[QModbusDataUnit]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QModbusServer::data(QModbusDataUnit *newData) const
    return self.uglySide.call(
        'ritual_ZNK13QModbusServer4dataEP15QModbusDataUnit',
        self._addressOf(newData),
    )

  @overload(QModbusDataUnit)
  @overload(NoneType)
  def readData(self, newData: Optional[QModbusDataUnit]) -> bool:
    """
    Calls Qt's 'bool QModbusServer::readData(QModbusDataUnit *newData)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusserver.html#readData

    Parameters
    ----------

    newData : Optional[QModbusDataUnit]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QModbusServer::readData(QModbusDataUnit *newData) const
    ritual = 'ritual_ZNK13QModbusServer8readDataEP15QModbusDataUnit'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QModbusServer8readDataEP15QModbusDataUnit'
    return self.uglySide.call(ritual, self._addressOf(newData))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setServerAddress(self, serverAddress: int) -> None:
    """
    Calls Qt's 'void QModbusServer::setServerAddress(int serverAddress)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusserver.html#setServerAddress

    Parameters
    ----------

    serverAddress : int
      Passed on as it is.
    """
    #  void QModbusServer::setServerAddress(int serverAddress)
    self.uglySide.call(
        'ritual_ZN13QModbusServer16setServerAddressEi', serverAddress,
    )

  @overload(int, QVariant)
  def setValue(self, option: int, value: QVariant) -> bool:
    """
    Calls Qt's 'bool QModbusServer::setValue(int option, const QVariant
    &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusserver.html#setValue

    Parameters
    ----------

    option : int
      Passed on as it is.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QModbusServer::setValue(int option, const QVariant &value)
    ritual = 'ritual_ZN13QModbusServer8setValueEiRK8QVariant'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QModbusServer8setValueEiRK8QVariant'
    return self.uglySide.call(ritual, option, self._valueOf(value))

  @overload(QModbusDataUnit)
  def setData(self, unit: QModbusDataUnit) -> bool:
    """
    Calls Qt's 'bool QModbusServer::setData(const QModbusDataUnit &unit)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusserver.html#setData

    Parameters
    ----------

    unit : QModbusDataUnit
      Passed on as a value: Qt reads the C++ QModbusDataUnit, which stays
      Python's own.
    """
    #  bool QModbusServer::setData(const QModbusDataUnit &unit)
    return self.uglySide.call(
        'ritual_ZN13QModbusServer7setDataERK15QModbusDataUnit',
        self._valueOf(unit),
    )

  @overload(QModbusDataUnit.RegisterType, int, int)
  def setData(
      self,
      table: QModbusDataUnit.RegisterType,
      address: int,
      data: int,
  ) -> bool:
    """
    Calls Qt's 'bool QModbusServer::setData(QModbusDataUnit::RegisterType
    table, quint16 address, quint16 data)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusserver.html#setData

    Parameters
    ----------

    table : QModbusDataUnit.RegisterType
      Passed on as its number.

    address : int
      Passed on as it is.

    data : int
      Passed on as it is.
    """
    #  bool QModbusServer::setData(QModbusDataUnit::RegisterType table,
    #      quint16 address, quint16 data)
    return self.uglySide.call(
        'ritual_ZN13QModbusServer7setDataEN15QModbusDataUnit12RegisterTypeE'
        'tt',
        table.value, address, data,
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
    Notes what was given, for Qt's 'QModbusServer::QModbusServer(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusserver.html#QModbusServer

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QModbusServer::QModbusServer(QObject *parent)
    self._noteCreation(QModbusServer, lambda: Rituals.call(
        'ritual_ZN13QModbusServerC1EP7QObject',
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

  def d_func(self) -> Optional[QModbusServerPrivate]:
    """
    Calls Qt's 'QModbusServerPrivate *QModbusServer::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusserver.html#d_func

    Returns
    -------

    Optional[QModbusServerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QModbusServerPrivate *QModbusServer::d_func()
    address = self.uglySide.call('ritual_ZN13QModbusServer6d_funcEv')
    from . import QModbusServerPrivate
    return QModbusServerPrivate._cuteAt(address)

  @overload(QModbusDataUnit.RegisterType, int, int)
  def dataWritten(
      self,
      table: QModbusDataUnit.RegisterType,
      address: int,
      size: int,
  ) -> None:
    """
    Calls Qt's 'void QModbusServer::dataWritten(QModbusDataUnit::RegisterType
    table, int address, int size)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusserver.html#dataWritten

    Parameters
    ----------

    table : QModbusDataUnit.RegisterType
      Passed on as its number.

    address : int
      Passed on as it is.

    size : int
      Passed on as it is.
    """
    #  void QModbusServer::dataWritten(QModbusDataUnit::RegisterType table,
    #      int address, int size)
    self.uglySide.call(
        'ritual_ZN13QModbusServer11dataWrittenEN15QModbusDataUnit12Register'
        'TypeEii',
        table.value, address, size,
    )

  @overload(QModbusDataUnit)
  def writeData(self, unit: QModbusDataUnit) -> bool:
    """
    Calls Qt's 'bool QModbusServer::writeData(const QModbusDataUnit &unit)'.

    Qt's own words: https://doc.qt.io/qt-6/qmodbusserver.html#writeData

    Parameters
    ----------

    unit : QModbusDataUnit
      Passed on as a value: Qt reads the C++ QModbusDataUnit, which stays
      Python's own.
    """
    #  bool QModbusServer::writeData(const QModbusDataUnit &unit)
    ritual = 'ritual_ZN13QModbusServer9writeDataERK15QModbusDataUnit'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QModbusServer9writeDataERK15QModbusDataUnit'
    return self.uglySide.call(ritual, self._valueOf(unit))

  @staticmethod
  def processPrivateRequest(*__, **_) -> Never:
    """
    Qt's 'QModbusResponse QModbusServer::processPrivateRequest(const
    QModbusPdu &request)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QModbusServer.processPrivateRequest' has no cute function yet. "
        "Qt's 'QModbusResponse QModbusServer::processPrivateRequest(const "
        "QModbusPdu &request)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def processRequest(*__, **_) -> Never:
    """
    Qt's 'QModbusResponse QModbusServer::processRequest(const QModbusPdu
    &request)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QModbusServer.processRequest' has no cute function yet. Qt's "
        "'QModbusResponse QModbusServer::processRequest(const QModbusPdu "
        "&request)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setMap(*__, **_) -> Never:
    """
    Qt's 'bool QModbusServer::setMap(const QModbusDataUnitMap &map)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QModbusServer.setMap' has no cute function yet. Qt's 'bool "
        "QModbusServer::setMap(const QModbusDataUnitMap &map)': takes a "
        "type Python has no way to hand over yet.")
