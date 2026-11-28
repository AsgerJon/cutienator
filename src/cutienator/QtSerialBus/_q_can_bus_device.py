"""
QCanBusDevice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/qcanbusdevice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QCanBusDeviceInfo, QCanBusDevicePrivate, QCanBusFrame
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCanBusFrame = WAIT['QCanBusFrame']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCanBusDevice(QObject):
  """
  The cute side of Qt's QCanBusDevice: a plain Python object standing in
  front of one C++ QCanBusDevice.

  It is built on the cute 'QObject', as Qt's QCanBusDevice is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCanBusDevice that has a ritual and that Python can
  call so far, 37 names in all: 'metaObject', 'tr', 'd_func',
  'setConfigurationParameter', 'configurationParameter', 'writeFrame',
  'readFrame', 'readAllFrames', 'framesAvailable', 'framesToWrite',
  'resetController', 'hasBusStatus', 'busStatus', 'clear',
  'waitForFramesWritten', 'waitForFramesReceived', 'connectDevice',
  'disconnectDevice', 'state', 'error', 'errorString', 'interpretErrorFrame',
  'deviceInfo', 'errorOccurred', 'framesReceived', 'framesWritten',
  'stateChanged', 'setState', 'setError', 'clearError',
  'enqueueReceivedFrames', 'enqueueOutgoingFrame', 'dequeueOutgoingFrame',
  'hasOutgoingFrames', 'open', 'close', 'createDeviceInfo'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCanBusDevice::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QCanBusDevice::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QCanBusDevicePrivate *QCanBusDevice::d_func() const': takes
    in Python what 'QCanBusDevicePrivate *QCanBusDevice::d_func()' takes.
  - Qt's 'QList<ConfigurationKey> QCanBusDevice::configurationKeys() const':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  4 of the 47 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QCanBusDevice is created at the first use, not by
    'QCanBusDevice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCanBusDevice.
  - Qt tells when it has removed the C++ QCanBusDevice. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QCanBusDevice that has no cute function yet,
    'configurationKeys', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QCanBusDevice, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class CanBusDeviceState(CuteNum):
    """
    The enum 'QCanBusDevice::CanBusDeviceState' of Qt, with the 4 names Qt
    gives in it.
    """

    UnconnectedState = Kee[int](0)
    ConnectingState = Kee[int](1)
    ConnectedState = Kee[int](2)
    ClosingState = Kee[int](3)

  class CanBusError(CuteNum):
    """
    The enum 'QCanBusDevice::CanBusError' of Qt, with the 8 names Qt gives in
    it.
    """

    NoError = Kee[int](0)
    ReadError = Kee[int](1)
    WriteError = Kee[int](2)
    ConnectionError = Kee[int](3)
    ConfigurationError = Kee[int](4)
    UnknownError = Kee[int](5)
    OperationError = Kee[int](6)
    TimeoutError = Kee[int](7)

  class CanBusStatus(CuteNum, scoped=True):
    """
    The enum 'QCanBusDevice::CanBusStatus' of Qt, with the 5 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Unknown = Kee[int](0)
    Good = Kee[int](1)
    Warning = Kee[int](2)
    Error = Kee[int](3)
    BusOff = Kee[int](4)

  class ConfigurationKey(CuteNum):
    """
    The enum 'QCanBusDevice::ConfigurationKey' of Qt, with the 9 names Qt
    gives in it.
    """

    RawFilterKey = Kee[int](0)
    ErrorFilterKey = Kee[int](1)
    LoopbackKey = Kee[int](2)
    ReceiveOwnKey = Kee[int](3)
    BitRateKey = Kee[int](4)
    CanFdKey = Kee[int](5)
    DataBitRateKey = Kee[int](6)
    ProtocolKey = Kee[int](7)
    UserKey = Kee[int](30)

  class Direction(CuteFlags):
    """
    The flags enum 'QCanBusDevice::Direction' of Qt, with the 3 names Qt
    gives in it. Qt names the type of its combinations
    'QCanBusDevice::Directions'.
    """

    Input = 0x1
    Output = 0x2
    AllDirections = 0x3

  Directions = Direction

  #  The classes Qt writes inside QCanBusDevice, each a class in here as in
  #  C++.

  class Filter(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QCanBusDevice::Filter: a plain Python object
    standing in front of one C++ QCanBusDevice::Filter.

    C++ hands a QCanBusDevice::Filter around as a copy, so every C++
    QCanBusDevice::Filter behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QCanBusDevice::Filter that has a ritual and that
    Python can call so far, 2 names in all: '__eq__', '__ne__'. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QCanBusDevice::Filter::~Filter()': the destructor: Python removes
      its C++ QCanBusDevice::Filter by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QCanBusDevice::Filter is created at the first use, not by
      'QCanBusDevice::Filter(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QCanBusDevice::Filter back gives a copy the ritual
      made for Python, in a new cute QCanBusDevice::Filter.
    """

    #  The enums Qt writes inside QCanBusDevice::Filter, each a class in here
    #  as in C++, and the names Qt has for the combinations of its flags
    #  enums.

    class FormatFilter(CuteFlags):
      """
      The flags enum 'QCanBusDevice::Filter::FormatFilter' of Qt, with the 3
      names Qt gives in it. Qt names the type of its combinations
      'QCanBusDevice::Filter::FormatFilters'.
      """

      MatchBaseFormat = 0x1
      MatchExtendedFormat = 0x2
      MatchBaseAndExtendedFormat = 0x3

    FormatFilters = FormatFilter

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QCanBusDevice::Filter'

    #  Qt's '~QCanBusDevice::Filter()'. Naming it makes this a value class:
    #  Python owns every C++ QCanBusDevice::Filter behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN13QCanBusDevice6FilterD1Ev'

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

    @overload(THIS)
    def __eq__(self, b: QCanBusDevice.Filter) -> bool:
      """
      Calls Qt's 'bool operator==(const Filter &a, const Filter &b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcanbusdevice-filter.html#operator==

      Parameters
      ----------

      b : QCanBusDevice.Filter
        Passed on as a value: Qt reads the C++ QCanBusDevice::Filter, which
        stays Python's own.
      """
      #  bool operator==(const Filter &a, const Filter &b)
      return Rituals.call(
          'ritual_ZeqRKN13QCanBusDevice6FilterES2_',
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
    def __ne__(self, b: QCanBusDevice.Filter) -> bool:
      """
      Calls Qt's 'bool operator!=(const Filter &a, const Filter &b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcanbusdevice-filter.html#operator!=

      Parameters
      ----------

      b : QCanBusDevice.Filter
        Passed on as a value: Qt reads the C++ QCanBusDevice::Filter, which
        stays Python's own.
      """
      #  bool operator!=(const Filter &a, const Filter &b)
      return Rituals.call(
          'ritual_ZneRKN13QCanBusDevice6FilterES2_',
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
    Calls Qt's 'QString QCanBusDevice::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdevice.html#tr

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
    #  QString QCanBusDevice::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QCanBusDevice2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(str, str, bool, bool)
  def createDeviceInfo(
      plugin: str,
      name: str,
      isVirtual: bool,
      isFlexibleDataRateCapable: bool,
  ) -> QCanBusDeviceInfo:
    """
    Calls Qt's 'QCanBusDeviceInfo QCanBusDevice::createDeviceInfo(const
    QString &plugin, const QString &name, bool isVirtual, bool
    isFlexibleDataRateCapable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanbusdevice.html#createDeviceInfo

    Parameters
    ----------

    plugin : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.

    isVirtual : bool
      Passed on as it is.

    isFlexibleDataRateCapable : bool
      Passed on as it is.

    Returns
    -------

    QCanBusDeviceInfo
      A new cute QCanBusDeviceInfo around the copy Qt gave back. Python owns
      it.
    """
    #  QCanBusDeviceInfo QCanBusDevice::createDeviceInfo(const QString
    #      &plugin, const QString &name, bool isVirtual, bool
    #      isFlexibleDataRateCapable)
    address = Rituals.call(
        'ritual_ZN13QCanBusDevice16createDeviceInfoERK7QStringS2_bb',
        plugin, name, isVirtual, isFlexibleDataRateCapable,
    )
    from . import QCanBusDeviceInfo
    return QCanBusDeviceInfo._cuteOwning(address)

  @staticmethod
  @overload(str, str, str, str, str, int, bool, bool)
  def createDeviceInfo(
      plugin: str,
      name: str,
      serialNumber: str,
      description: str,
      alias: str,
      channel: int,
      isVirtual: bool,
      isFlexibleDataRateCapable: bool,
  ) -> QCanBusDeviceInfo:
    """
    Calls Qt's 'QCanBusDeviceInfo QCanBusDevice::createDeviceInfo(const
    QString &plugin, const QString &name, const QString &serialNumber, const
    QString &description, const QString &alias, int channel, bool isVirtual,
    bool isFlexibleDataRateCapable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanbusdevice.html#createDeviceInfo

    Parameters
    ----------

    plugin : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.

    serialNumber : str
      Passed on as it is: a QString is made of it for the call.

    description : str
      Passed on as it is: a QString is made of it for the call.

    alias : str
      Passed on as it is: a QString is made of it for the call.

    channel : int
      Passed on as it is.

    isVirtual : bool
      Passed on as it is.

    isFlexibleDataRateCapable : bool
      Passed on as it is.

    Returns
    -------

    QCanBusDeviceInfo
      A new cute QCanBusDeviceInfo around the copy Qt gave back. Python owns
      it.
    """
    #  QCanBusDeviceInfo QCanBusDevice::createDeviceInfo(const QString
    #      &plugin, const QString &name, const QString &serialNumber, const
    #      QString &description, const QString &alias, int channel, bool
    #      isVirtual, bool isFlexibleDataRateCapable)
    address = Rituals.call(
        'ritual_ZN13QCanBusDevice16createDeviceInfoERK7QStringS2_S2_S2_S2_i'
        'bb',
        plugin, name, serialNumber, description, alias, channel, isVirtual,
        isFlexibleDataRateCapable,
    )
    from . import QCanBusDeviceInfo
    return QCanBusDeviceInfo._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanBusDevice'

  #  A C++ QCanBusDevice Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCanBusDevice'

  #  The functions Qt calls itself that QCanBusDevice is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setConfigurationParameter': (
          ('_ZN13QCanBusDevice25setConfigurationParameterENS_16Configuratio'
           'nKeyERK8QVariant',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtSerialBus:QCanBusDevice.ConfigurationKey'),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
      'writeFrame': (
          ('_ZN13QCanBusDevice10writeFrameERK12QCanBusFrame',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtSerialBus:QCanBusFrame'),
           )),
      ),
      'resetController': (
          ('_ZN13QCanBusDevice15resetControllerEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'hasBusStatus': (
          ('_ZNK13QCanBusDevice12hasBusStatusEv',
           ('bool', 'number', ''),
           ()),
      ),
      'busStatus': (
          ('_ZN13QCanBusDevice9busStatusEv',
           ('int', 'enum', 'QtSerialBus:QCanBusDevice.CanBusStatus'),
           ()),
      ),
      'waitForFramesWritten': (
          ('_ZN13QCanBusDevice20waitForFramesWrittenEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'waitForFramesReceived': (
          ('_ZN13QCanBusDevice21waitForFramesReceivedEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'interpretErrorFrame': (
          ('_ZN13QCanBusDevice19interpretErrorFrameERK12QCanBusFrame',
           ('address', 'text', ''),
           (
               ('address', 'value', 'QtSerialBus:QCanBusFrame'),
           )),
      ),
      'deviceInfo': (
          ('_ZNK13QCanBusDevice10deviceInfoEv',
           ('address', 'value', 'QtSerialBus:QCanBusDeviceInfo'),
           ()),
      ),
      'open': (
          ('_ZN13QCanBusDevice4openEv',
           ('bool', 'number', ''),
           ()),
      ),
      'close': (
          ('_ZN13QCanBusDevice5closeEv',
           ('nothing', 'nothing', ''),
           ()),
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
    Calls Qt's 'const QMetaObject *QCanBusDevice::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdevice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCanBusDevice::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QCanBusDevice10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(ConfigurationKey)
  def configurationParameter(self, key: ConfigurationKey) -> QVariant:
    """
    Calls Qt's 'QVariant
    QCanBusDevice::configurationParameter(ConfigurationKey key) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanbusdevice.html#configurationParameter

    Parameters
    ----------

    key : ConfigurationKey
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QCanBusDevice::configurationParameter(ConfigurationKey key)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13QCanBusDevice22configurationParameterENS_16Configurati'
        'onKeyE',
        key.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def framesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QCanBusDevice::framesAvailable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdevice.html#framesAvailable
    """
    #  qint64 QCanBusDevice::framesAvailable() const
    return self.uglySide.call('ritual_ZNK13QCanBusDevice15framesAvailableEv')

  def framesToWrite(self) -> int:
    """
    Calls Qt's 'qint64 QCanBusDevice::framesToWrite() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdevice.html#framesToWrite
    """
    #  qint64 QCanBusDevice::framesToWrite() const
    return self.uglySide.call('ritual_ZNK13QCanBusDevice13framesToWriteEv')

  def hasBusStatus(self) -> bool:
    """
    Calls Qt's 'bool QCanBusDevice::hasBusStatus() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdevice.html#hasBusStatus
    """
    #  bool QCanBusDevice::hasBusStatus() const
    ritual = 'ritual_ZNK13QCanBusDevice12hasBusStatusEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QCanBusDevice12hasBusStatusEv'
    return self.uglySide.call(ritual)

  def state(self) -> CanBusDeviceState:
    """
    Calls Qt's 'CanBusDeviceState QCanBusDevice::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdevice.html#state

    Returns
    -------

    CanBusDeviceState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'CanBusDeviceState(number)' gives.
    """
    #  CanBusDeviceState QCanBusDevice::state() const
    return QCanBusDevice.CanBusDeviceState(self.uglySide.call(
        'ritual_ZNK13QCanBusDevice5stateEv',
    ))

  def error(self) -> CanBusError:
    """
    Calls Qt's 'CanBusError QCanBusDevice::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdevice.html#error

    Returns
    -------

    CanBusError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'CanBusError(number)'
      gives.
    """
    #  CanBusError QCanBusDevice::error() const
    return QCanBusDevice.CanBusError(self.uglySide.call(
        'ritual_ZNK13QCanBusDevice5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QCanBusDevice::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdevice.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCanBusDevice::errorString() const
    return self.uglySide.call('ritual_ZNK13QCanBusDevice11errorStringEv')

  def deviceInfo(self) -> QCanBusDeviceInfo:
    """
    Calls Qt's 'QCanBusDeviceInfo QCanBusDevice::deviceInfo() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdevice.html#deviceInfo

    Returns
    -------

    QCanBusDeviceInfo
      A new cute QCanBusDeviceInfo around the copy Qt gave back. Python owns
      it.
    """
    #  QCanBusDeviceInfo QCanBusDevice::deviceInfo() const
    ritual = 'ritual_ZNK13QCanBusDevice10deviceInfoEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QCanBusDevice10deviceInfoEv'
    address = self.uglySide.call(ritual)
    from . import QCanBusDeviceInfo
    return QCanBusDeviceInfo._cuteOwning(address)

  def hasOutgoingFrames(self) -> bool:
    """
    Calls Qt's 'bool QCanBusDevice::hasOutgoingFrames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanbusdevice.html#hasOutgoingFrames
    """
    #  bool QCanBusDevice::hasOutgoingFrames() const
    return self.uglySide.call(
        'ritual_ZNK13QCanBusDevice17hasOutgoingFramesEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(ConfigurationKey, QVariant)
  def setConfigurationParameter(
      self,
      key: ConfigurationKey,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void
    QCanBusDevice::setConfigurationParameter(ConfigurationKey key, const
    QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanbusdevice.html#setConfigurationParameter

    Parameters
    ----------

    key : ConfigurationKey
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QCanBusDevice::setConfigurationParameter(ConfigurationKey key,
    #      const QVariant &value)
    ritual = (
        'ritual_ZN13QCanBusDevice25setConfigurationParameterENS_16Configura'
        'tionKeyERK8QVariant')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QCanBusDevice25setConfigurationParameterENS_16Con'
          'figurationKeyERK8QVariant')
    self.uglySide.call(ritual, key.value, self._valueOf(value))

  @overload(CanBusDeviceState)
  def setState(self, newState: CanBusDeviceState) -> None:
    """
    Calls Qt's 'void QCanBusDevice::setState(QCanBusDevice::CanBusDeviceState
    newState)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdevice.html#setState

    Parameters
    ----------

    newState : CanBusDeviceState
      Passed on as its number.
    """
    #  void QCanBusDevice::setState(QCanBusDevice::CanBusDeviceState
    #      newState)
    self.uglySide.call(
        'ritual_ZN13QCanBusDevice8setStateENS_17CanBusDeviceStateE',
        newState.value,
    )

  @overload(str, CanBusError)
  def setError(self, errorText: str, a1: CanBusError) -> None:
    """
    Calls Qt's 'void QCanBusDevice::setError(const QString &errorText,
    QCanBusDevice::CanBusError a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdevice.html#setError

    Parameters
    ----------

    errorText : str
      Passed on as it is: a QString is made of it for the call.

    a1 : CanBusError
      Passed on as its number.
    """
    #  void QCanBusDevice::setError(const QString &errorText,
    #      QCanBusDevice::CanBusError a1)
    self.uglySide.call(
        'ritual_ZN13QCanBusDevice8setErrorERK7QStringNS_11CanBusErrorE',
        errorText, a1.value,
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
    Notes what was given, for Qt's 'QCanBusDevice::QCanBusDevice(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdevice.html#QCanBusDevice

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCanBusDevice::QCanBusDevice(QObject *parent)
    self._noteCreation(QCanBusDevice, lambda: Rituals.call(
        'ritual_ZN13QCanBusDeviceC1EP7QObject',
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

  def d_func(self) -> Optional[QCanBusDevicePrivate]:
    """
    Calls Qt's 'QCanBusDevicePrivate *QCanBusDevice::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdevice.html#d_func

    Returns
    -------

    Optional[QCanBusDevicePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCanBusDevicePrivate *QCanBusDevice::d_func()
    address = self.uglySide.call('ritual_ZN13QCanBusDevice6d_funcEv')
    from . import QCanBusDevicePrivate
    return QCanBusDevicePrivate._cuteAt(address)

  @overload(QCanBusFrame)
  def writeFrame(self, frame: QCanBusFrame) -> bool:
    """
    Calls Qt's 'bool QCanBusDevice::writeFrame(const QCanBusFrame &frame)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdevice.html#writeFrame

    Parameters
    ----------

    frame : QCanBusFrame
      Passed on as a value: Qt reads the C++ QCanBusFrame, which stays
      Python's own.
    """
    #  bool QCanBusDevice::writeFrame(const QCanBusFrame &frame)
    return self.uglySide.call(
        'ritual_ZN13QCanBusDevice10writeFrameERK12QCanBusFrame',
        self._valueOf(frame),
    )

  def readFrame(self) -> QCanBusFrame:
    """
    Calls Qt's 'QCanBusFrame QCanBusDevice::readFrame()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdevice.html#readFrame

    Returns
    -------

    QCanBusFrame
      A new cute QCanBusFrame around the copy Qt gave back. Python owns it.
    """
    #  QCanBusFrame QCanBusDevice::readFrame()
    address = self.uglySide.call('ritual_ZN13QCanBusDevice9readFrameEv')
    from . import QCanBusFrame
    return QCanBusFrame._cuteOwning(address)

  def readAllFrames(self) -> QList[QCanBusFrame]:
    """
    Calls Qt's 'QList<QCanBusFrame> QCanBusDevice::readAllFrames()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdevice.html#readAllFrames

    Returns
    -------

    QList[QCanBusFrame]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QCanBusFrame> QCanBusDevice::readAllFrames()
    address = self.uglySide.call('ritual_ZN13QCanBusDevice13readAllFramesEv')
    from . import QCanBusFrame
    return QList[QCanBusFrame]._cuteOwning(address)

  def resetController(self) -> None:
    """
    Calls Qt's 'void QCanBusDevice::resetController()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdevice.html#resetController
    """
    #  void QCanBusDevice::resetController()
    ritual = 'ritual_ZN13QCanBusDevice15resetControllerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QCanBusDevice15resetControllerEv'
    self.uglySide.call(ritual)

  def busStatus(self) -> CanBusStatus:
    """
    Calls Qt's 'CanBusStatus QCanBusDevice::busStatus()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdevice.html#busStatus

    Returns
    -------

    CanBusStatus
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'CanBusStatus(number)'
      gives.
    """
    #  CanBusStatus QCanBusDevice::busStatus()
    ritual = 'ritual_ZN13QCanBusDevice9busStatusEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QCanBusDevice9busStatusEv'
    return QCanBusDevice.CanBusStatus(self.uglySide.call(ritual))

  @overload()
  @overload(Directions)
  def clear(self, direction: Directions = Directions.AllDirections) -> None:
    """
    Calls Qt's 'void QCanBusDevice::clear(Directions direction)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdevice.html#clear

    Parameters
    ----------

    direction : Directions
      Passed on as its number. May be left out, as in Qt: it is then
      Directions.AllDirections.
    """
    #  void QCanBusDevice::clear(Directions direction)
    self.uglySide.call(
        'ritual_ZN13QCanBusDevice5clearE6QFlagsINS_9DirectionEE',
        direction.value,
    )

  @overload(int)
  def waitForFramesWritten(self, msecs: int) -> bool:
    """
    Calls Qt's 'bool QCanBusDevice::waitForFramesWritten(int msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanbusdevice.html#waitForFramesWritten

    Parameters
    ----------

    msecs : int
      Passed on as it is.
    """
    #  bool QCanBusDevice::waitForFramesWritten(int msecs)
    ritual = 'ritual_ZN13QCanBusDevice20waitForFramesWrittenEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QCanBusDevice20waitForFramesWrittenEi'
    return self.uglySide.call(ritual, msecs)

  @overload(int)
  def waitForFramesReceived(self, msecs: int) -> bool:
    """
    Calls Qt's 'bool QCanBusDevice::waitForFramesReceived(int msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanbusdevice.html#waitForFramesReceived

    Parameters
    ----------

    msecs : int
      Passed on as it is.
    """
    #  bool QCanBusDevice::waitForFramesReceived(int msecs)
    ritual = 'ritual_ZN13QCanBusDevice21waitForFramesReceivedEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QCanBusDevice21waitForFramesReceivedEi'
    return self.uglySide.call(ritual, msecs)

  def connectDevice(self) -> bool:
    """
    Calls Qt's 'bool QCanBusDevice::connectDevice()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdevice.html#connectDevice
    """
    #  bool QCanBusDevice::connectDevice()
    return self.uglySide.call('ritual_ZN13QCanBusDevice13connectDeviceEv')

  def disconnectDevice(self) -> None:
    """
    Calls Qt's 'void QCanBusDevice::disconnectDevice()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanbusdevice.html#disconnectDevice
    """
    #  void QCanBusDevice::disconnectDevice()
    self.uglySide.call('ritual_ZN13QCanBusDevice16disconnectDeviceEv')

  @overload(QCanBusFrame)
  def interpretErrorFrame(self, errorFrame: QCanBusFrame) -> str:
    """
    Calls Qt's 'QString QCanBusDevice::interpretErrorFrame(const QCanBusFrame
    &errorFrame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanbusdevice.html#interpretErrorFrame

    Parameters
    ----------

    errorFrame : QCanBusFrame
      Passed on as a value: Qt reads the C++ QCanBusFrame, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCanBusDevice::interpretErrorFrame(const QCanBusFrame
    #      &errorFrame)
    return self.uglySide.call(
        'ritual_ZN13QCanBusDevice19interpretErrorFrameERK12QCanBusFrame',
        self._valueOf(errorFrame),
    )

  @overload(CanBusError)
  def errorOccurred(self, a0: CanBusError) -> None:
    """
    Calls Qt's 'void QCanBusDevice::errorOccurred(QCanBusDevice::CanBusError
    a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdevice.html#errorOccurred

    Parameters
    ----------

    a0 : CanBusError
      Passed on as its number.
    """
    #  void QCanBusDevice::errorOccurred(QCanBusDevice::CanBusError a0)
    self.uglySide.call(
        'ritual_ZN13QCanBusDevice13errorOccurredENS_11CanBusErrorE',
        a0.value,
    )

  def framesReceived(self) -> None:
    """
    Calls Qt's 'void QCanBusDevice::framesReceived()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdevice.html#framesReceived
    """
    #  void QCanBusDevice::framesReceived()
    self.uglySide.call('ritual_ZN13QCanBusDevice14framesReceivedEv')

  @overload(int)
  def framesWritten(self, framesCount: int) -> None:
    """
    Calls Qt's 'void QCanBusDevice::framesWritten(qint64 framesCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdevice.html#framesWritten

    Parameters
    ----------

    framesCount : int
      Passed on as it is.
    """
    #  void QCanBusDevice::framesWritten(qint64 framesCount)
    self.uglySide.call(
        'ritual_ZN13QCanBusDevice13framesWrittenEx', framesCount,
    )

  @overload(CanBusDeviceState)
  def stateChanged(self, state: CanBusDeviceState) -> None:
    """
    Calls Qt's 'void
    QCanBusDevice::stateChanged(QCanBusDevice::CanBusDeviceState state)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdevice.html#stateChanged

    Parameters
    ----------

    state : CanBusDeviceState
      Passed on as its number.
    """
    #  void QCanBusDevice::stateChanged(QCanBusDevice::CanBusDeviceState
    #      state)
    self.uglySide.call(
        'ritual_ZN13QCanBusDevice12stateChangedENS_17CanBusDeviceStateE',
        state.value,
    )

  def clearError(self) -> None:
    """
    Calls Qt's 'void QCanBusDevice::clearError()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdevice.html#clearError
    """
    #  void QCanBusDevice::clearError()
    self.uglySide.call('ritual_ZN13QCanBusDevice10clearErrorEv')

  @overload(QList[QCanBusFrame])
  def enqueueReceivedFrames(self, newFrames: QList[QCanBusFrame]) -> None:
    """
    Calls Qt's 'void QCanBusDevice::enqueueReceivedFrames(const
    QList<QCanBusFrame> &newFrames)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanbusdevice.html#enqueueReceivedFrames

    Parameters
    ----------

    newFrames : QList[QCanBusFrame]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QCanBusDevice::enqueueReceivedFrames(const QList<QCanBusFrame>
    #      &newFrames)
    self.uglySide.call(
        'ritual_ZN13QCanBusDevice21enqueueReceivedFramesERK5QListI12QCanBus'
        'FrameE',
        self._valueOf(newFrames),
    )

  @overload(QCanBusFrame)
  def enqueueOutgoingFrame(self, newFrame: QCanBusFrame) -> None:
    """
    Calls Qt's 'void QCanBusDevice::enqueueOutgoingFrame(const QCanBusFrame
    &newFrame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanbusdevice.html#enqueueOutgoingFrame

    Parameters
    ----------

    newFrame : QCanBusFrame
      Passed on as a value: Qt reads the C++ QCanBusFrame, which stays
      Python's own.
    """
    #  void QCanBusDevice::enqueueOutgoingFrame(const QCanBusFrame &newFrame)
    self.uglySide.call(
        'ritual_ZN13QCanBusDevice20enqueueOutgoingFrameERK12QCanBusFrame',
        self._valueOf(newFrame),
    )

  def dequeueOutgoingFrame(self) -> QCanBusFrame:
    """
    Calls Qt's 'QCanBusFrame QCanBusDevice::dequeueOutgoingFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanbusdevice.html#dequeueOutgoingFrame

    Returns
    -------

    QCanBusFrame
      A new cute QCanBusFrame around the copy Qt gave back. Python owns it.
    """
    #  QCanBusFrame QCanBusDevice::dequeueOutgoingFrame()
    address = self.uglySide.call(
        'ritual_ZN13QCanBusDevice20dequeueOutgoingFrameEv',
    )
    from . import QCanBusFrame
    return QCanBusFrame._cuteOwning(address)

  def open(self) -> bool:
    """
    Calls Qt's 'bool QCanBusDevice::open()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdevice.html#open
    """
    #  bool QCanBusDevice::open()
    return self.uglySide.call('ritual_ZN13QCanBusDevice4openEv')

  def close(self) -> None:
    """
    Calls Qt's 'void QCanBusDevice::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanbusdevice.html#close
    """
    #  void QCanBusDevice::close()
    self.uglySide.call('ritual_ZN13QCanBusDevice5closeEv')

  @staticmethod
  def configurationKeys(*__, **_) -> Never:
    """
    Qt's 'QList<ConfigurationKey> QCanBusDevice::configurationKeys() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QCanBusDevice.configurationKeys' has no cute function yet. Qt's "
        "'QList<ConfigurationKey> QCanBusDevice::configurationKeys() "
        "const': gives a type Python has no way to take yet.")
