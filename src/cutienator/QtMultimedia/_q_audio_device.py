"""
QAudioDevice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qaudiodevice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QAudioFormat

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
  from . import QAudioDevicePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioDevicePrivate = WAIT['QAudioDevicePrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAudioDevice(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QAudioDevice: a plain Python object standing in front
  of one C++ QAudioDevice.

  C++ hands a QAudioDevice around as a copy, so every C++ QAudioDevice behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QAudioDevice that has a ritual and that Python can
  call so far, 15 names in all: '__eq__', '__ne__', 'isNull', 'id',
  'description', 'isDefault', 'mode', 'isFormatSupported', 'preferredFormat',
  'minimumSampleRate', 'maximumSampleRate', 'minimumChannelCount',
  'maximumChannelCount', 'channelConfiguration', 'handle'. It can be made
  from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAudioDevice::~QAudioDevice()': the destructor: Python removes its
    C++ QAudioDevice by it, and has no other use for it.
  - Qt's 'QAudioDevice::QAudioDevice(QAudioDevice &&other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QAudioDevice &QAudioDevice::operator=(QAudioDevice &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QAudioDevice::swap(QAudioDevice &other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QAudioDevice &QAudioDevice::operator=(const QAudioDevice &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QList<QAudioFormat::SampleFormat>
    QAudioDevice::supportedSampleFormats() const': gives a type Python has no
    way to take yet.

  What has no ritual
  ------------------

  3 of the 27 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QAudioDevice is created at the first use, not by
    'QAudioDevice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QAudioDevice back gives a copy the ritual made for
    Python, in a new cute QAudioDevice.
  - Each name of Qt's QAudioDevice that has no cute function yet,
    'supportedSampleFormats', 'swap', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QAudioDevice, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Mode(CuteNum):
    """
    The enum 'QAudioDevice::Mode' of Qt, with the 3 names Qt gives in it.
    """

    Null = Kee[int](0)
    Input = Kee[int](1)
    Output = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAudioDevice'

  #  Qt's '~QAudioDevice()'. Naming it makes this a value class: Python owns
  #  every C++ QAudioDevice behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QAudioDeviceD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QAudioDevice::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodevice.html#isNull
    """
    #  bool QAudioDevice::isNull() const
    return self.uglySide.call('ritual_ZNK12QAudioDevice6isNullEv')

  def id(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QAudioDevice::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodevice.html#id

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QAudioDevice::id() const
    address = self.uglySide.call('ritual_ZNK12QAudioDevice2idEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def description(self) -> str:
    """
    Calls Qt's 'QString QAudioDevice::description() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodevice.html#description

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAudioDevice::description() const
    return self.uglySide.call('ritual_ZNK12QAudioDevice11descriptionEv')

  def isDefault(self) -> bool:
    """
    Calls Qt's 'bool QAudioDevice::isDefault() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodevice.html#isDefault
    """
    #  bool QAudioDevice::isDefault() const
    return self.uglySide.call('ritual_ZNK12QAudioDevice9isDefaultEv')

  def mode(self) -> Mode:
    """
    Calls Qt's 'QAudioDevice::Mode QAudioDevice::mode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodevice.html#mode

    Returns
    -------

    Mode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Mode(number)' gives.
    """
    #  QAudioDevice::Mode QAudioDevice::mode() const
    return QAudioDevice.Mode(self.uglySide.call(
        'ritual_ZNK12QAudioDevice4modeEv',
    ))

  @overload(QAudioFormat)
  def isFormatSupported(self, format: QAudioFormat) -> bool:
    """
    Calls Qt's 'bool QAudioDevice::isFormatSupported(const QAudioFormat
    &format) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudiodevice.html#isFormatSupported

    Parameters
    ----------

    format : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.
    """
    #  bool QAudioDevice::isFormatSupported(const QAudioFormat &format) const
    return self.uglySide.call(
        'ritual_ZNK12QAudioDevice17isFormatSupportedERK12QAudioFormat',
        self._valueOf(format),
    )

  def preferredFormat(self) -> QAudioFormat:
    """
    Calls Qt's 'QAudioFormat QAudioDevice::preferredFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodevice.html#preferredFormat

    Returns
    -------

    QAudioFormat
      A new cute QAudioFormat around the copy Qt gave back. Python owns it.
    """
    #  QAudioFormat QAudioDevice::preferredFormat() const
    address = self.uglySide.call(
        'ritual_ZNK12QAudioDevice15preferredFormatEv',
    )
    return QAudioFormat._cuteOwning(address)

  def minimumSampleRate(self) -> int:
    """
    Calls Qt's 'int QAudioDevice::minimumSampleRate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudiodevice.html#minimumSampleRate
    """
    #  int QAudioDevice::minimumSampleRate() const
    return self.uglySide.call(
        'ritual_ZNK12QAudioDevice17minimumSampleRateEv',
    )

  def maximumSampleRate(self) -> int:
    """
    Calls Qt's 'int QAudioDevice::maximumSampleRate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudiodevice.html#maximumSampleRate
    """
    #  int QAudioDevice::maximumSampleRate() const
    return self.uglySide.call(
        'ritual_ZNK12QAudioDevice17maximumSampleRateEv',
    )

  def minimumChannelCount(self) -> int:
    """
    Calls Qt's 'int QAudioDevice::minimumChannelCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudiodevice.html#minimumChannelCount
    """
    #  int QAudioDevice::minimumChannelCount() const
    return self.uglySide.call(
        'ritual_ZNK12QAudioDevice19minimumChannelCountEv',
    )

  def maximumChannelCount(self) -> int:
    """
    Calls Qt's 'int QAudioDevice::maximumChannelCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudiodevice.html#maximumChannelCount
    """
    #  int QAudioDevice::maximumChannelCount() const
    return self.uglySide.call(
        'ritual_ZNK12QAudioDevice19maximumChannelCountEv',
    )

  def channelConfiguration(self) -> QAudioFormat.ChannelConfig:
    """
    Calls Qt's 'QAudioFormat::ChannelConfig
    QAudioDevice::channelConfiguration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudiodevice.html#channelConfiguration

    Returns
    -------

    QAudioFormat.ChannelConfig
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAudioFormat.ChannelConfig(number)' gives.
    """
    #  QAudioFormat::ChannelConfig QAudioDevice::channelConfiguration() const
    return QAudioFormat.ChannelConfig(self.uglySide.call(
        'ritual_ZNK12QAudioDevice20channelConfigurationEv',
    ))

  def handle(self) -> Optional[QAudioDevicePrivate]:
    """
    Calls Qt's 'const QAudioDevicePrivate *QAudioDevice::handle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodevice.html#handle

    Returns
    -------

    Optional[QAudioDevicePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QAudioDevicePrivate *QAudioDevice::handle() const
    address = self.uglySide.call('ritual_ZNK12QAudioDevice6handleEv')
    from . import QAudioDevicePrivate
    return QAudioDevicePrivate._cuteAt(address)

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
  def __eq__(self, other: QAudioDevice) -> bool:
    """
    Calls Qt's 'bool QAudioDevice::operator==(const QAudioDevice &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodevice.html#operator==

    Parameters
    ----------

    other : QAudioDevice
      Passed on as a value: Qt reads the C++ QAudioDevice, which stays
      Python's own.
    """
    #  bool QAudioDevice::operator==(const QAudioDevice &other) const
    return self.uglySide.call(
        'ritual_ZNK12QAudioDeviceeqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QAudioDevice) -> bool:
    """
    Calls Qt's 'bool QAudioDevice::operator!=(const QAudioDevice &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodevice.html#operator!=

    Parameters
    ----------

    other : QAudioDevice
      Passed on as a value: Qt reads the C++ QAudioDevice, which stays
      Python's own.
    """
    #  bool QAudioDevice::operator!=(const QAudioDevice &other) const
    return self.uglySide.call(
        'ritual_ZNK12QAudioDeviceneERKS_', self._valueOf(other),
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
    Notes what was given, for Qt's 'QAudioDevice::QAudioDevice()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodevice.html#QAudioDevice
    """
    #  QAudioDevice::QAudioDevice()
    self._noteCreation(QAudioDevice, lambda: Rituals.call(
        'ritual_ZN12QAudioDeviceC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QAudioDevice) -> None:
    """
    Notes what was given, for Qt's 'QAudioDevice::QAudioDevice(const
    QAudioDevice &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodevice.html#QAudioDevice

    Parameters
    ----------

    other : QAudioDevice
      Passed on as a value: Qt reads the C++ QAudioDevice, which stays
      Python's own.
    """
    #  QAudioDevice::QAudioDevice(const QAudioDevice &other)
    self._noteCreation(QAudioDevice, lambda: Rituals.call(
        'ritual_ZN12QAudioDeviceC1ERKS_', self._valueOf(other),
    ))

  @overload(QAudioDevicePrivate)
  @overload(NoneType)
  def __init__(self, p: Optional[QAudioDevicePrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QAudioDevice::QAudioDevice(QAudioDevicePrivate *p)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodevice.html#QAudioDevice

    Parameters
    ----------

    p : Optional[QAudioDevicePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAudioDevice::QAudioDevice(QAudioDevicePrivate *p)
    self._noteCreation(QAudioDevice, lambda: Rituals.call(
        'ritual_ZN12QAudioDeviceC1EP19QAudioDevicePrivate',
        self._addressOf(p),
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

  @staticmethod
  def supportedSampleFormats(*__, **_) -> Never:
    """
    Qt's 'QList<QAudioFormat::SampleFormat>
    QAudioDevice::supportedSampleFormats() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QAudioDevice.supportedSampleFormats' has no cute function yet. "
        "Qt's 'QList<QAudioFormat::SampleFormat> "
        "QAudioDevice::supportedSampleFormats() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QAudioDevice::swap(QAudioDevice &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAudioDevice.swap' has no cute function yet. Qt's 'void "
        "QAudioDevice::swap(QAudioDevice &other)': takes a type Python has "
        "no way to hand over yet.")


#  Qt's 'QList<QAudioDevice>': the list of QAudioDevice, which
#  'QList[QAudioDevice]' gives. It is made here, so that there is one as soon
#  as there can be a QAudioDevice.
QList.createKind(
    QAudioDevice, 'value',
    make='ritual_list_make_QAudioDevice',
    add='ritual_list_add_QAudioDevice',
    size='ritual_list_size_QAudioDevice',
    at='ritual_list_at_QAudioDevice',
    drop='ritual_list_drop_QAudioDevice',
)
