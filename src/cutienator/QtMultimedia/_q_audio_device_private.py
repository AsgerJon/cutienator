"""
QAudioDevicePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qaudiodevice_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAudioDevicePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QSharedData
from . import QAudioDevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QAudioDevicePrivate(QSharedData):
  """
  The cute side of Qt's QAudioDevicePrivate: a plain Python object standing
  in front of one C++ QAudioDevicePrivate.

  It is built on the cute 'QSharedData', as Qt's QAudioDevicePrivate is built
  on Qt's QSharedData, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAudioDevicePrivate that has a ritual and that
  Python can call so far, 1 name in all: 'handle'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAudioDevicePrivate::~QAudioDevicePrivate()': the destructor:
    Python never removes a C++ QAudioDevicePrivate.
  - Qt's 'QAudioDeviceExpected<AudioDeviceFormat>
    QAudioDevicePrivate::format() const': gives a type Python has no way to
    take yet.
  - Qt's 'QAudioDeviceExpected<QAudioFormat>
    QAudioDevicePrivate::preferredFormat() const': gives a type Python has no
    way to take yet.
  - Qt's 'QAudioDeviceExpected<int> QAudioDevicePrivate::minimumSampleRate()
    const': gives a type Python has no way to take yet.
  - Qt's 'QAudioDeviceExpected<int> QAudioDevicePrivate::maximumSampleRate()
    const': gives a type Python has no way to take yet.
  - Qt's 'QAudioDeviceExpected<int>
    QAudioDevicePrivate::minimumChannelCount() const': gives a type Python
    has no way to take yet.
  - Qt's 'QAudioDeviceExpected<int>
    QAudioDevicePrivate::maximumChannelCount() const': gives a type Python
    has no way to take yet.
  - Qt's 'QAudioDeviceExpected<QList<QAudioFormat::SampleFormat>>
    QAudioDevicePrivate::supportedSampleFormats() const': gives a type Python
    has no way to take yet.
  - Qt's 'QAudioDeviceExpected<QAudioFormat::ChannelConfig>
    QAudioDevicePrivate::channelConfiguration() const': gives a type Python
    has no way to take yet.
  - Qt's 'QAudioDeviceExpected<bool>
    QAudioDevicePrivate::isFormatSupported(const QAudioFormat &format)
    const': gives a type Python has no way to take yet.
  - Qt's 'QAudioDevicePrivate *QAudioDevicePrivate::handle(QAudioDevice
    &device)': takes a type Python has no way to hand over yet.
  - Qt's 'QAudioDevicePrivate::QAudioDevicePrivate(const QAudioDevicePrivate
    &a0)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 18 functions Qt declares: 2 a template; 2 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ QAudioDevicePrivate is created at the first use, not by
    'QAudioDevicePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAudioDevicePrivate.
  - Each name of Qt's QAudioDevicePrivate that has no cute function yet,
    'channelConfiguration', 'createQAudioDevice', 'doWithDeviceFormat',
    'format', 'isFormatSupported', 'maximumChannelCount',
    'maximumSampleRate', 'minimumChannelCount', 'minimumSampleRate',
    'preferredFormat', 'supportedSampleFormats', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QAudioDevicePrivate, each a class in here
  #  as in C++.

  class AudioDeviceFormat(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QAudioDevicePrivate::AudioDeviceFormat: a plain
    Python object standing in front of one C++
    QAudioDevicePrivate::AudioDeviceFormat.

    C++ hands a QAudioDevicePrivate::AudioDeviceFormat around as a copy, so
    every C++ QAudioDevicePrivate::AudioDeviceFormat behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QAudioDevicePrivate::AudioDeviceFormat that has a
    ritual and that Python can call so far, 1 name in all: '__eq__'. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QAudioDevicePrivate::AudioDeviceFormat::~AudioDeviceFormat()':
      the destructor: Python removes its C++
      QAudioDevicePrivate::AudioDeviceFormat by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QAudioDevicePrivate::AudioDeviceFormat is created at the first
      use, not by 'QAudioDevicePrivate::AudioDeviceFormat(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QAudioDevicePrivate::AudioDeviceFormat back gives a
      copy the ritual made for Python, in a new cute
      QAudioDevicePrivate::AudioDeviceFormat.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QAudioDevicePrivate::AudioDeviceFormat'

    #  Qt's '~QAudioDevicePrivate::AudioDeviceFormat()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QAudioDevicePrivate::AudioDeviceFormat behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN19QAudioDevicePrivate17AudioDeviceFormatD1Ev')

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
    def __eq__(self, rhs: QAudioDevicePrivate.AudioDeviceFormat) -> bool:
      """
      Calls Qt's 'bool operator==(const AudioDeviceFormat &lhs, const
      AudioDeviceFormat &rhs)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qaudiodeviceprivate-audiodeviceformat.html

      Parameters
      ----------

      rhs : QAudioDevicePrivate.AudioDeviceFormat
        Passed on as a value: Qt reads the C++
        QAudioDevicePrivate::AudioDeviceFormat, which stays Python's own.
      """
      #  bool operator==(const AudioDeviceFormat &lhs, const
      #      AudioDeviceFormat &rhs)
      return Rituals.call(
          'ritual_ZeqRKN19QAudioDevicePrivate17AudioDeviceFormatES2_',
          CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
      )

    @overload.fallback
    def __eq__(self, *args: object) -> object:
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
  @overload(QAudioDevice)
  def handle(device: QAudioDevice) -> Optional[QAudioDevicePrivate]:
    """
    Calls Qt's 'const QAudioDevicePrivate *QAudioDevicePrivate::handle(const
    QAudioDevice &device)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiodeviceprivate.html#handle

    Parameters
    ----------

    device : QAudioDevice
      Passed on as a value: Qt reads the C++ QAudioDevice, which stays
      Python's own.

    Returns
    -------

    Optional[QAudioDevicePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QAudioDevicePrivate *QAudioDevicePrivate::handle(const
    #      QAudioDevice &device)
    address = Rituals.call(
        'ritual_ZN19QAudioDevicePrivate6handleERK12QAudioDevice',
        CuteMixin._valueOf(device),
    )
    return QAudioDevicePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAudioDevicePrivate'

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

  @overload(QByteArray, QAudioDevice.Mode, str, bool, AudioDeviceFormat)
  def __init__(
      self,
      i: QByteArray,
      m: QAudioDevice.Mode,
      description: str,
      isDefault: bool,
      format: AudioDeviceFormat,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAudioDevicePrivate::QAudioDevicePrivate(const QByteArray &i,
    QAudioDevice::Mode m, QString description, bool isDefault,
    AudioDeviceFormat format)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaudiodeviceprivate.html#QAudioDevicePrivate

    Parameters
    ----------

    i : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    m : QAudioDevice.Mode
      Passed on as its number.

    description : str
      Passed on as it is: a QString is made of it for the call.

    isDefault : bool
      Passed on as it is.

    format : AudioDeviceFormat
      Passed on as a value: Qt reads the C++
      QAudioDevicePrivate::AudioDeviceFormat, which stays Python's own.
    """
    #  QAudioDevicePrivate::QAudioDevicePrivate(const QByteArray &i,
    #      QAudioDevice::Mode m, QString description, bool isDefault,
    #      AudioDeviceFormat format)
    self._noteCreation(QAudioDevicePrivate, lambda: Rituals.call(
        'ritual_ZN19QAudioDevicePrivateC1ERK10QByteArrayN12QAudioDevice4Mod'
        'eE7QStringbNS_17AudioDeviceFormatE',
        self._valueOf(i), m.value, description, isDefault,
        self._valueOf(format),
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
  def channelConfiguration(*__, **_) -> Never:
    """
    Qt's 'QAudioDeviceExpected<QAudioFormat::ChannelConfig>
    QAudioDevicePrivate::channelConfiguration() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QAudioDevicePrivate.channelConfiguration' has no cute function "
        "yet. Qt's 'QAudioDeviceExpected<QAudioFormat::ChannelConfig> "
        "QAudioDevicePrivate::channelConfiguration() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def createQAudioDevice(*__, **_) -> Never:
    """
    Qt's 'QAudioDevice QAudioDevicePrivate::createQAudioDevice(std::
    unique_ptr<QAudioDevicePrivate> devicePrivate)': the compiler refuses its
    ritual as it would be written here: call to deleted constructor of
    'std::unique_ptr<QAudioDevicePrivate>'.
    """
    raise NotImplementedError(
        "'QAudioDevicePrivate.createQAudioDevice' has no cute function yet. "
        "Qt's 'QAudioDevice "
        "QAudioDevicePrivate::createQAudioDevice(std::unique_ptr<QAudioDevic"
        "ePrivate> devicePrivate)': the compiler refuses its ritual as it "
        "would be written here: call to deleted constructor of "
        "'std::unique_ptr<QAudioDevicePrivate>'.")

  @staticmethod
  def doWithDeviceFormat(*__, **_) -> Never:
    """
    Qt's 'QAudioDevicePrivate::doWithDeviceFormat': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QAudioDevicePrivate.doWithDeviceFormat' has no cute function yet. "
        "Qt's 'QAudioDevicePrivate::doWithDeviceFormat': a template: a "
        "pattern and no single function.")

  @staticmethod
  def format(*__, **_) -> Never:
    """
    Qt's 'QAudioDeviceExpected<AudioDeviceFormat>
    QAudioDevicePrivate::format() const': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QAudioDevicePrivate.format' has no cute function yet. Qt's "
        "'QAudioDeviceExpected<AudioDeviceFormat> "
        "QAudioDevicePrivate::format() const': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def isFormatSupported(*__, **_) -> Never:
    """
    Qt's 'QAudioDeviceExpected<bool>
    QAudioDevicePrivate::isFormatSupported(const QAudioFormat &format)
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAudioDevicePrivate.isFormatSupported' has no cute function yet. "
        "Qt's 'QAudioDeviceExpected<bool> "
        "QAudioDevicePrivate::isFormatSupported(const QAudioFormat &format) "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def maximumChannelCount(*__, **_) -> Never:
    """
    Qt's 'QAudioDeviceExpected<int>
    QAudioDevicePrivate::maximumChannelCount() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QAudioDevicePrivate.maximumChannelCount' has no cute function "
        "yet. Qt's 'QAudioDeviceExpected<int> "
        "QAudioDevicePrivate::maximumChannelCount() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def maximumSampleRate(*__, **_) -> Never:
    """
    Qt's 'QAudioDeviceExpected<int> QAudioDevicePrivate::maximumSampleRate()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAudioDevicePrivate.maximumSampleRate' has no cute function yet. "
        "Qt's 'QAudioDeviceExpected<int> "
        "QAudioDevicePrivate::maximumSampleRate() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def minimumChannelCount(*__, **_) -> Never:
    """
    Qt's 'QAudioDeviceExpected<int>
    QAudioDevicePrivate::minimumChannelCount() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QAudioDevicePrivate.minimumChannelCount' has no cute function "
        "yet. Qt's 'QAudioDeviceExpected<int> "
        "QAudioDevicePrivate::minimumChannelCount() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def minimumSampleRate(*__, **_) -> Never:
    """
    Qt's 'QAudioDeviceExpected<int> QAudioDevicePrivate::minimumSampleRate()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAudioDevicePrivate.minimumSampleRate' has no cute function yet. "
        "Qt's 'QAudioDeviceExpected<int> "
        "QAudioDevicePrivate::minimumSampleRate() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def preferredFormat(*__, **_) -> Never:
    """
    Qt's 'QAudioDeviceExpected<QAudioFormat>
    QAudioDevicePrivate::preferredFormat() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QAudioDevicePrivate.preferredFormat' has no cute function yet. "
        "Qt's 'QAudioDeviceExpected<QAudioFormat> "
        "QAudioDevicePrivate::preferredFormat() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def supportedSampleFormats(*__, **_) -> Never:
    """
    Qt's 'QAudioDeviceExpected<QList<QAudioFormat::SampleFormat>>
    QAudioDevicePrivate::supportedSampleFormats() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QAudioDevicePrivate.supportedSampleFormats' has no cute function "
        "yet. Qt's 'QAudioDeviceExpected<QList<QAudioFormat::SampleFormat>> "
        "QAudioDevicePrivate::supportedSampleFormats() const': gives a type "
        "Python has no way to take yet.")
