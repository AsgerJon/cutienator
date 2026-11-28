"""
QAudioInput binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qaudioinput.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QAudioDevice, QPlatformAudioInput
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioDevice = WAIT['QAudioDevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAudioInput(QObject):
  """
  The cute side of Qt's QAudioInput: a plain Python object standing in front
  of one C++ QAudioInput.

  It is built on the cute 'QObject', as Qt's QAudioInput is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAudioInput that has a ritual and that Python can
  call so far, 12 names in all: 'metaObject', 'tr', 'device', 'volume',
  'isMuted', 'setDevice', 'setVolume', 'setMuted', 'deviceChanged',
  'volumeChanged', 'mutedChanged', 'handle'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAudioInput::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QAudioInput::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QAudioInput::~QAudioInput()': the destructor: Python never removes
    a C++ QAudioInput.
  - Qt's 'void QAudioInput::setDisconnectFunction(std::function<void ()>
    disconnectFunction)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 22 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QAudioInput is created at the first use, not by
    'QAudioInput(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAudioInput.
  - Qt tells when it has removed the C++ QAudioInput. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QAudioInput that has no cute function yet,
    'setDisconnectFunction', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QAudioInput::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioinput.html#tr

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
    #  QString QAudioInput::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QAudioInput2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAudioInput'

  #  A C++ QAudioInput Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAudioInput'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAudioInput::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioinput.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAudioInput::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QAudioInput10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def device(self) -> QAudioDevice:
    """
    Calls Qt's 'QAudioDevice QAudioInput::device() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioinput.html#device

    Returns
    -------

    QAudioDevice
      A new cute QAudioDevice around the copy Qt gave back. Python owns it.
    """
    #  QAudioDevice QAudioInput::device() const
    address = self.uglySide.call('ritual_ZNK11QAudioInput6deviceEv')
    from . import QAudioDevice
    return QAudioDevice._cuteOwning(address)

  def volume(self) -> float:
    """
    Calls Qt's 'float QAudioInput::volume() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioinput.html#volume
    """
    #  float QAudioInput::volume() const
    return self.uglySide.call('ritual_ZNK11QAudioInput6volumeEv')

  def isMuted(self) -> bool:
    """
    Calls Qt's 'bool QAudioInput::isMuted() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioinput.html#isMuted
    """
    #  bool QAudioInput::isMuted() const
    return self.uglySide.call('ritual_ZNK11QAudioInput7isMutedEv')

  def handle(self) -> Optional[QPlatformAudioInput]:
    """
    Calls Qt's 'QPlatformAudioInput *QAudioInput::handle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioinput.html#handle

    Returns
    -------

    Optional[QPlatformAudioInput]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformAudioInput *QAudioInput::handle() const
    address = self.uglySide.call('ritual_ZNK11QAudioInput6handleEv')
    from . import QPlatformAudioInput
    return QPlatformAudioInput._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAudioDevice)
  def setDevice(self, device: QAudioDevice) -> None:
    """
    Calls Qt's 'void QAudioInput::setDevice(const QAudioDevice &device)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioinput.html#setDevice

    Parameters
    ----------

    device : QAudioDevice
      Passed on as a value: Qt reads the C++ QAudioDevice, which stays
      Python's own.
    """
    #  void QAudioInput::setDevice(const QAudioDevice &device)
    self.uglySide.call(
        'ritual_ZN11QAudioInput9setDeviceERK12QAudioDevice',
        self._valueOf(device),
    )

  @overload(float)
  def setVolume(self, volume: float) -> None:
    """
    Calls Qt's 'void QAudioInput::setVolume(float volume)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioinput.html#setVolume

    Parameters
    ----------

    volume : float
      Passed on as it is.
    """
    #  void QAudioInput::setVolume(float volume)
    self.uglySide.call('ritual_ZN11QAudioInput9setVolumeEf', volume)

  @overload(bool)
  def setMuted(self, muted: bool) -> None:
    """
    Calls Qt's 'void QAudioInput::setMuted(bool muted)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioinput.html#setMuted

    Parameters
    ----------

    muted : bool
      Passed on as it is.
    """
    #  void QAudioInput::setMuted(bool muted)
    self.uglySide.call('ritual_ZN11QAudioInput8setMutedEb', muted)

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
    Notes what was given, for Qt's 'QAudioInput::QAudioInput(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qaudioinput.html#QAudioInput

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAudioInput::QAudioInput(QObject *parent)
    self._noteCreation(QAudioInput, lambda: Rituals.call(
        'ritual_ZN11QAudioInputC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QAudioDevice)
  @overload(QAudioDevice, QObject)
  @overload(QAudioDevice, NoneType)
  def __init__(
      self,
      deviceInfo: QAudioDevice,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QAudioInput::QAudioInput(const
    QAudioDevice &deviceInfo, QObject *parent)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qaudioinput.html#QAudioInput

    Parameters
    ----------

    deviceInfo : QAudioDevice
      Passed on as a value: Qt reads the C++ QAudioDevice, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAudioInput::QAudioInput(const QAudioDevice &deviceInfo, QObject
    #      *parent)
    self._noteCreation(QAudioInput, lambda: Rituals.call(
        'ritual_ZN11QAudioInputC1ERK12QAudioDeviceP7QObject',
        self._valueOf(deviceInfo), self._addressOf(parent, 'QObject'),
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

  def deviceChanged(self) -> None:
    """
    Calls Qt's 'void QAudioInput::deviceChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioinput.html#deviceChanged
    """
    #  void QAudioInput::deviceChanged()
    self.uglySide.call('ritual_ZN11QAudioInput13deviceChangedEv')

  @overload(float)
  def volumeChanged(self, volume: float) -> None:
    """
    Calls Qt's 'void QAudioInput::volumeChanged(float volume)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioinput.html#volumeChanged

    Parameters
    ----------

    volume : float
      Passed on as it is.
    """
    #  void QAudioInput::volumeChanged(float volume)
    self.uglySide.call('ritual_ZN11QAudioInput13volumeChangedEf', volume)

  @overload(bool)
  def mutedChanged(self, muted: bool) -> None:
    """
    Calls Qt's 'void QAudioInput::mutedChanged(bool muted)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudioinput.html#mutedChanged

    Parameters
    ----------

    muted : bool
      Passed on as it is.
    """
    #  void QAudioInput::mutedChanged(bool muted)
    self.uglySide.call('ritual_ZN11QAudioInput12mutedChangedEb', muted)

  @staticmethod
  def setDisconnectFunction(*__, **_) -> Never:
    """
    Qt's 'void QAudioInput::setDisconnectFunction(std::function<void ()>
    disconnectFunction)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAudioInput.setDisconnectFunction' has no cute function yet. Qt's "
        "'void QAudioInput::setDisconnectFunction(std::function<void ()> "
        "disconnectFunction)': takes a type Python has no way to hand over "
        "yet.")
