"""
QPlatformAudioEndpointBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qaudiosystem_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QPlatformAudioEndpointBase to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QAudio

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QAudioDevice, QAudioFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioDevice = WAIT['QAudioDevice']
  QAudioFormat = WAIT['QAudioFormat']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformAudioEndpointBase(QObject):
  """
  The cute side of Qt's QPlatformAudioEndpointBase: a plain Python object
  standing in front of one C++ QPlatformAudioEndpointBase.

  It is built on the cute 'QObject', as Qt's QPlatformAudioEndpointBase is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformAudioEndpointBase that has a ritual and
  that Python can call so far, 12 names in all: 'metaObject', 'tr', 'error',
  'state', 'setError', 'isFormatSupported', 'format', 'setVolume', 'volume',
  'stateChanged', 'updateStreamState', 'inferState'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformAudioEndpointBase::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QPlatformAudioEndpointBase::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QPlatformAudioEndpointBase::~QPlatformAudioEndpointBase()': the
    destructor: Python never removes a C++ QPlatformAudioEndpointBase.
  - Qt's 'void QPlatformAudioEndpointBase::updateStreamIdle(bool idle,
    EmitStateSignal a1)': names the enum
    'QPlatformAudioEndpointBase::EmitStateSignal', whose class cannot be
    named here.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPlatformAudioEndpointBase is created at the first use, not by
    'QPlatformAudioEndpointBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformAudioEndpointBase.
  - Qt tells when it has removed the C++ QPlatformAudioEndpointBase. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPlatformAudioEndpointBase that has no cute function
    yet, 'updateStreamIdle', holds a function that raises
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
    Calls Qt's 'QString QPlatformAudioEndpointBase::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudioendpointbase.html#tr

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
    #  QString QPlatformAudioEndpointBase::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QPlatformAudioEndpointBase2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformAudioEndpointBase'

  #  A C++ QPlatformAudioEndpointBase Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformAudioEndpointBase'

  #  The functions Qt calls itself that QPlatformAudioEndpointBase is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'state': (
          ('_ZNK26QPlatformAudioEndpointBase5stateEv',
           ('int', 'enum', 'QtMultimedia:QAudio.State'),
           ()),
      ),
      'setError': (
          ('_ZN26QPlatformAudioEndpointBase8setErrorEN6QAudio5ErrorE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtMultimedia:QAudio.Error'),
           )),
      ),
      'isFormatSupported': (
          ('_ZNK26QPlatformAudioEndpointBase17isFormatSupportedERK12QAudioF'
           'ormat',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtMultimedia:QAudioFormat'),
           )),
      ),
      'setVolume': (
          ('_ZN26QPlatformAudioEndpointBase9setVolumeEf',
           ('nothing', 'nothing', ''),
           (
               ('float', 'number', ''),
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
    Calls Qt's 'const QMetaObject *QPlatformAudioEndpointBase::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudioendpointbase.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformAudioEndpointBase::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QPlatformAudioEndpointBase10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def error(self) -> QAudio.Error:
    """
    Calls Qt's 'QAudio::Error QPlatformAudioEndpointBase::error() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudioendpointbase.html#error

    Returns
    -------

    QAudio.Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAudio.Error(number)'
      gives.
    """
    #  QAudio::Error QPlatformAudioEndpointBase::error() const
    return QAudio.Error(self.uglySide.call(
        'ritual_ZNK26QPlatformAudioEndpointBase5errorEv',
    ))

  def state(self) -> QAudio.State:
    """
    Calls Qt's 'QAudio::State QPlatformAudioEndpointBase::state() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudioendpointbase.html#state

    Returns
    -------

    QAudio.State
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAudio.State(number)'
      gives.
    """
    #  QAudio::State QPlatformAudioEndpointBase::state() const
    ritual = 'ritual_ZNK26QPlatformAudioEndpointBase5stateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QPlatformAudioEndpointBase5stateEv'
    return QAudio.State(self.uglySide.call(ritual))

  @overload(QAudioFormat)
  def isFormatSupported(self, format: QAudioFormat) -> bool:
    """
    Calls Qt's 'bool QPlatformAudioEndpointBase::isFormatSupported(const
    QAudioFormat &format) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudioendpointbase.html#isFormatSupported

    Parameters
    ----------

    format : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.
    """
    #  bool QPlatformAudioEndpointBase::isFormatSupported(const QAudioFormat
    #      &format) const
    ritual = (
        'ritual_ZNK26QPlatformAudioEndpointBase17isFormatSupportedERK12QAud'
        'ioFormat')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK26QPlatformAudioEndpointBase17isFormatSupportedERK'
          '12QAudioFormat')
    return self.uglySide.call(ritual, self._valueOf(format))

  def format(self) -> QAudioFormat:
    """
    Calls Qt's 'QAudioFormat QPlatformAudioEndpointBase::format() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudioendpointbase.html#format

    Returns
    -------

    QAudioFormat
      A new cute QAudioFormat around the copy Qt gave back. Python owns it.
    """
    #  QAudioFormat QPlatformAudioEndpointBase::format() const
    address = self.uglySide.call(
        'ritual_ZNK26QPlatformAudioEndpointBase6formatEv',
    )
    from . import QAudioFormat
    return QAudioFormat._cuteOwning(address)

  def volume(self) -> float:
    """
    Calls Qt's 'float QPlatformAudioEndpointBase::volume() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudioendpointbase.html#volume
    """
    #  float QPlatformAudioEndpointBase::volume() const
    return self.uglySide.call(
        'ritual_ZNK26QPlatformAudioEndpointBase6volumeEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAudio.Error)
  def setError(self, a0: QAudio.Error) -> None:
    """
    Calls Qt's 'void QPlatformAudioEndpointBase::setError(QAudio::Error a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudioendpointbase.html#setError

    Parameters
    ----------

    a0 : QAudio.Error
      Passed on as its number.
    """
    #  void QPlatformAudioEndpointBase::setError(QAudio::Error a0)
    ritual = 'ritual_ZN26QPlatformAudioEndpointBase8setErrorEN6QAudio5ErrorE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QPlatformAudioEndpointBase8setErrorEN6QAudio5Erro'
          'rE')
    self.uglySide.call(ritual, a0.value)

  @overload(float)
  def setVolume(self, volume: float) -> None:
    """
    Calls Qt's 'void QPlatformAudioEndpointBase::setVolume(float volume)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudioendpointbase.html#setVolume

    Parameters
    ----------

    volume : float
      Passed on as it is.
    """
    #  void QPlatformAudioEndpointBase::setVolume(float volume)
    ritual = 'ritual_ZN26QPlatformAudioEndpointBase9setVolumeEf'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QPlatformAudioEndpointBase9setVolumeEf'
    self.uglySide.call(ritual, volume)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAudioDevice, QAudioFormat, QObject)
  @overload(QAudioDevice, QAudioFormat, NoneType)
  def __init__(
      self,
      a0: QAudioDevice,
      a1: QAudioFormat,
      parent: Optional[QObject],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformAudioEndpointBase::QPlatformAudioEndpointBase(QAudioDevice a0,
    const QAudioFormat &a1, QObject *parent)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudioendpointbase.html

    Parameters
    ----------

    a0 : QAudioDevice
      Passed on as a value: Qt reads the C++ QAudioDevice, which stays
      Python's own.

    a1 : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPlatformAudioEndpointBase::QPlatformAudioEndpointBase(QAudioDevice
    #      a0, const QAudioFormat &a1, QObject *parent)
    self._noteCreation(QPlatformAudioEndpointBase, lambda: Rituals.call(
        'ritual_ZN26QPlatformAudioEndpointBaseC1E12QAudioDeviceRK12QAudioFo'
        'rmatP7QObject',
        self._valueOf(a0), self._valueOf(a1), self._addressOf(parent,
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

  @overload(QAudio.State)
  def stateChanged(self, a0: QAudio.State) -> None:
    """
    Calls Qt's 'void QPlatformAudioEndpointBase::stateChanged(QtAudio::State
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudioendpointbase.html#stateChanged

    Parameters
    ----------

    a0 : QAudio.State
      Passed on as its number.
    """
    #  void QPlatformAudioEndpointBase::stateChanged(QtAudio::State a0)
    self.uglySide.call(
        'ritual_ZN26QPlatformAudioEndpointBase12stateChangedEN6QAudio5State'
        'E',
        a0.value,
    )

  @overload(QAudio.State)
  def updateStreamState(self, a0: QAudio.State) -> None:
    """
    Calls Qt's 'void
    QPlatformAudioEndpointBase::updateStreamState(QAudio::State a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudioendpointbase.html#updateStreamState

    Parameters
    ----------

    a0 : QAudio.State
      Passed on as its number.
    """
    #  void QPlatformAudioEndpointBase::updateStreamState(QAudio::State a0)
    self.uglySide.call(
        'ritual_ZN26QPlatformAudioEndpointBase17updateStreamStateEN6QAudio5'
        'StateE',
        a0.value,
    )

  def inferState(self) -> None:
    """
    Calls Qt's 'void QPlatformAudioEndpointBase::inferState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudioendpointbase.html#inferState
    """
    #  void QPlatformAudioEndpointBase::inferState()
    self.uglySide.call('ritual_ZN26QPlatformAudioEndpointBase10inferStateEv')

  @staticmethod
  def updateStreamIdle(*__, **_) -> Never:
    """
    Qt's 'void QPlatformAudioEndpointBase::updateStreamIdle(bool idle,
    EmitStateSignal a1)': names the enum
    'QPlatformAudioEndpointBase::EmitStateSignal', whose class cannot be
    named here.
    """
    raise NotImplementedError(
        "'QPlatformAudioEndpointBase.updateStreamIdle' has no cute function "
        "yet. Qt's 'void QPlatformAudioEndpointBase::updateStreamIdle(bool "
        "idle, EmitStateSignal a1)': names the enum "
        "'QPlatformAudioEndpointBase::EmitStateSignal', whose class cannot "
        "be named here.")
