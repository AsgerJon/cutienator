"""
QPlatformAudioInput binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qplatformaudioinput_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QPlatformAudioInput to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QAudioDevice, QAudioInput
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioDevice = WAIT['QAudioDevice']
  QAudioInput = WAIT['QAudioInput']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformAudioInput(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlatformAudioInput: a plain Python object standing
  in front of one C++ QPlatformAudioInput.

  C++ hands a QPlatformAudioInput around as a copy, so every C++
  QPlatformAudioInput behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlatformAudioInput that has a ritual and that
  Python can call so far, 3 names in all: 'setAudioDevice', 'setMuted',
  'setVolume'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlatformAudioInput::~QPlatformAudioInput()': the destructor:
    Python removes its C++ QPlatformAudioInput by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QPlatformAudioInput is created at the first use, not by
    'QPlatformAudioInput(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlatformAudioInput back gives a copy the ritual made
    for Python, in a new cute QPlatformAudioInput.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformAudioInput'

  #  A C++ QPlatformAudioInput Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformAudioInput'

  #  The functions Qt calls itself that QPlatformAudioInput is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setAudioDevice': (
          ('_ZN19QPlatformAudioInput14setAudioDeviceERK12QAudioDevice',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtMultimedia:QAudioDevice'),
           )),
      ),
      'setMuted': (
          ('_ZN19QPlatformAudioInput8setMutedEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'setVolume': (
          ('_ZN19QPlatformAudioInput9setVolumeEf',
           ('nothing', 'nothing', ''),
           (
               ('float', 'number', ''),
           )),
      ),
  }

  #  Qt's '~QPlatformAudioInput()'. Naming it makes this a value class:
  #  Python owns every C++ QPlatformAudioInput behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QPlatformAudioInputD1Ev'

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

  @overload(QAudioDevice)
  def setAudioDevice(self, a0: QAudioDevice) -> None:
    """
    Calls Qt's 'void QPlatformAudioInput::setAudioDevice(const QAudioDevice
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudioinput.html#setAudioDevice

    Parameters
    ----------

    a0 : QAudioDevice
      Passed on as a value: Qt reads the C++ QAudioDevice, which stays
      Python's own.
    """
    #  void QPlatformAudioInput::setAudioDevice(const QAudioDevice &a0)
    ritual = (
        'ritual_ZN19QPlatformAudioInput14setAudioDeviceERK12QAudioDevice')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QPlatformAudioInput14setAudioDeviceERK12QAudioDev'
          'ice')
    self.uglySide.call(ritual, self._valueOf(a0))

  @overload(bool)
  def setMuted(self, a0: bool) -> None:
    """
    Calls Qt's 'void QPlatformAudioInput::setMuted(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudioinput.html#setMuted

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QPlatformAudioInput::setMuted(bool a0)
    ritual = 'ritual_ZN19QPlatformAudioInput8setMutedEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QPlatformAudioInput8setMutedEb'
    self.uglySide.call(ritual, a0)

  @overload(float)
  def setVolume(self, a0: float) -> None:
    """
    Calls Qt's 'void QPlatformAudioInput::setVolume(float a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudioinput.html#setVolume

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QPlatformAudioInput::setVolume(float a0)
    ritual = 'ritual_ZN19QPlatformAudioInput9setVolumeEf'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QPlatformAudioInput9setVolumeEf'
    self.uglySide.call(ritual, a0)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAudioInput)
  @overload(NoneType)
  def __init__(self, qq: Optional[QAudioInput]) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformAudioInput::QPlatformAudioInput(QAudioInput *qq)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudioinput.html#QPlatformAudioInput

    Parameters
    ----------

    qq : Optional[QAudioInput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPlatformAudioInput::QPlatformAudioInput(QAudioInput *qq)
    self._noteCreation(QPlatformAudioInput, lambda: Rituals.call(
        'ritual_ZN19QPlatformAudioInputC1EP11QAudioInput',
        self._addressOf(qq),
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
