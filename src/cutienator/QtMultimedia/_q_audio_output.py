"""
QAudioOutput binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qaudiooutput.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QAudioDevice, QPlatformAudioOutput
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioDevice = WAIT['QAudioDevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAudioOutput(QObject):
  """
  The cute side of Qt's QAudioOutput: a plain Python object standing in front
  of one C++ QAudioOutput.

  It is built on the cute 'QObject', as Qt's QAudioOutput is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAudioOutput that has a ritual and that Python can
  call so far, 12 names in all: 'metaObject', 'tr', 'device', 'volume',
  'isMuted', 'setDevice', 'setVolume', 'setMuted', 'deviceChanged',
  'volumeChanged', 'mutedChanged', 'handle'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAudioOutput::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QAudioOutput::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QAudioOutput::~QAudioOutput()': the destructor: Python never
    removes a C++ QAudioOutput.
  - Qt's 'void QAudioOutput::setDisconnectFunction(std::function<void ()>
    disconnectFunction)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 22 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QAudioOutput is created at the first use, not by
    'QAudioOutput(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAudioOutput.
  - Qt tells when it has removed the C++ QAudioOutput. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QAudioOutput that has no cute function yet,
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
    Calls Qt's 'QString QAudioOutput::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiooutput.html#tr

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
    #  QString QAudioOutput::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QAudioOutput2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAudioOutput'

  #  A C++ QAudioOutput Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAudioOutput'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAudioOutput::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiooutput.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAudioOutput::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QAudioOutput10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def device(self) -> QAudioDevice:
    """
    Calls Qt's 'QAudioDevice QAudioOutput::device() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiooutput.html#device

    Returns
    -------

    QAudioDevice
      A new cute QAudioDevice around the copy Qt gave back. Python owns it.
    """
    #  QAudioDevice QAudioOutput::device() const
    address = self.uglySide.call('ritual_ZNK12QAudioOutput6deviceEv')
    from . import QAudioDevice
    return QAudioDevice._cuteOwning(address)

  def volume(self) -> float:
    """
    Calls Qt's 'float QAudioOutput::volume() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiooutput.html#volume
    """
    #  float QAudioOutput::volume() const
    return self.uglySide.call('ritual_ZNK12QAudioOutput6volumeEv')

  def isMuted(self) -> bool:
    """
    Calls Qt's 'bool QAudioOutput::isMuted() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiooutput.html#isMuted
    """
    #  bool QAudioOutput::isMuted() const
    return self.uglySide.call('ritual_ZNK12QAudioOutput7isMutedEv')

  def handle(self) -> Optional[QPlatformAudioOutput]:
    """
    Calls Qt's 'QPlatformAudioOutput *QAudioOutput::handle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiooutput.html#handle

    Returns
    -------

    Optional[QPlatformAudioOutput]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformAudioOutput *QAudioOutput::handle() const
    address = self.uglySide.call('ritual_ZNK12QAudioOutput6handleEv')
    from . import QPlatformAudioOutput
    return QPlatformAudioOutput._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAudioDevice)
  def setDevice(self, device: QAudioDevice) -> None:
    """
    Calls Qt's 'void QAudioOutput::setDevice(const QAudioDevice &device)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiooutput.html#setDevice

    Parameters
    ----------

    device : QAudioDevice
      Passed on as a value: Qt reads the C++ QAudioDevice, which stays
      Python's own.
    """
    #  void QAudioOutput::setDevice(const QAudioDevice &device)
    self.uglySide.call(
        'ritual_ZN12QAudioOutput9setDeviceERK12QAudioDevice',
        self._valueOf(device),
    )

  @overload(float)
  def setVolume(self, volume: float) -> None:
    """
    Calls Qt's 'void QAudioOutput::setVolume(float volume)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiooutput.html#setVolume

    Parameters
    ----------

    volume : float
      Passed on as it is.
    """
    #  void QAudioOutput::setVolume(float volume)
    self.uglySide.call('ritual_ZN12QAudioOutput9setVolumeEf', volume)

  @overload(bool)
  def setMuted(self, muted: bool) -> None:
    """
    Calls Qt's 'void QAudioOutput::setMuted(bool muted)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiooutput.html#setMuted

    Parameters
    ----------

    muted : bool
      Passed on as it is.
    """
    #  void QAudioOutput::setMuted(bool muted)
    self.uglySide.call('ritual_ZN12QAudioOutput8setMutedEb', muted)

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
    Notes what was given, for Qt's 'QAudioOutput::QAudioOutput(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qaudiooutput.html#QAudioOutput

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAudioOutput::QAudioOutput(QObject *parent)
    self._noteCreation(QAudioOutput, lambda: Rituals.call(
        'ritual_ZN12QAudioOutputC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QAudioDevice)
  @overload(QAudioDevice, QObject)
  @overload(QAudioDevice, NoneType)
  def __init__(
      self,
      device: QAudioDevice,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QAudioOutput::QAudioOutput(const
    QAudioDevice &device, QObject *parent)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qaudiooutput.html#QAudioOutput

    Parameters
    ----------

    device : QAudioDevice
      Passed on as a value: Qt reads the C++ QAudioDevice, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAudioOutput::QAudioOutput(const QAudioDevice &device, QObject
    #      *parent)
    self._noteCreation(QAudioOutput, lambda: Rituals.call(
        'ritual_ZN12QAudioOutputC1ERK12QAudioDeviceP7QObject',
        self._valueOf(device), self._addressOf(parent, 'QObject'),
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
    Calls Qt's 'void QAudioOutput::deviceChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiooutput.html#deviceChanged
    """
    #  void QAudioOutput::deviceChanged()
    self.uglySide.call('ritual_ZN12QAudioOutput13deviceChangedEv')

  @overload(float)
  def volumeChanged(self, volume: float) -> None:
    """
    Calls Qt's 'void QAudioOutput::volumeChanged(float volume)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiooutput.html#volumeChanged

    Parameters
    ----------

    volume : float
      Passed on as it is.
    """
    #  void QAudioOutput::volumeChanged(float volume)
    self.uglySide.call('ritual_ZN12QAudioOutput13volumeChangedEf', volume)

  @overload(bool)
  def mutedChanged(self, muted: bool) -> None:
    """
    Calls Qt's 'void QAudioOutput::mutedChanged(bool muted)'.

    Qt's own words: https://doc.qt.io/qt-6/qaudiooutput.html#mutedChanged

    Parameters
    ----------

    muted : bool
      Passed on as it is.
    """
    #  void QAudioOutput::mutedChanged(bool muted)
    self.uglySide.call('ritual_ZN12QAudioOutput12mutedChangedEb', muted)

  @staticmethod
  def setDisconnectFunction(*__, **_) -> Never:
    """
    Qt's 'void QAudioOutput::setDisconnectFunction(std::function<void ()>
    disconnectFunction)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAudioOutput.setDisconnectFunction' has no cute function yet. "
        "Qt's 'void QAudioOutput::setDisconnectFunction(std::function<void "
        "()> disconnectFunction)': takes a type Python has no way to hand "
        "over yet.")
