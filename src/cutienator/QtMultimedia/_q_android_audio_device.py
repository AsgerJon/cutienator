"""
QAndroidAudioDevice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qandroidaudiodevice_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QAndroidAudioDevice to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QAudioDevice, QAudioDevicePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray
  from . import QAudioFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioFormat = WAIT['QAudioFormat']
  QByteArray = WAIT['QByteArray']


class QAndroidAudioDevice(QAudioDevicePrivate):
  """
  The cute side of Qt's QAndroidAudioDevice: a plain Python object standing
  in front of one C++ QAndroidAudioDevice.

  It is built on the cute 'QAudioDevicePrivate', as Qt's QAndroidAudioDevice
  is built on Qt's QAudioDevicePrivate, and has everything that class has.

  C++ hands a QAndroidAudioDevice around as a copy, so every C++
  QAndroidAudioDevice behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QAndroidAudioDevice that has a ritual and that
  Python can call so far, 1 name in all: 'isBluetoothDevice'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAndroidAudioDevice::~QAndroidAudioDevice()': the destructor:
    Python removes its C++ QAndroidAudioDevice by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QAndroidAudioDevice is created at the first use, not by
    'QAndroidAudioDevice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QAndroidAudioDevice back gives a copy the ritual made
    for Python, in a new cute QAndroidAudioDevice.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAndroidAudioDevice'

  #  Qt's '~QAndroidAudioDevice()'. Naming it makes this a value class:
  #  Python owns every C++ QAndroidAudioDevice behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QAndroidAudioDeviceD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isBluetoothDevice(self) -> bool:
    """
    Calls Qt's 'bool QAndroidAudioDevice::isBluetoothDevice() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qandroidaudiodevice.html#isBluetoothDevice
    """
    #  bool QAndroidAudioDevice::isBluetoothDevice() const
    return self.uglySide.call(
        'ritual_ZNK19QAndroidAudioDevice17isBluetoothDeviceEv',
    )

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

  @overload(QByteArray, str, QAudioDevice.Mode, QAudioFormat, bool)
  @overload(QByteArray, str, QAudioDevice.Mode, QAudioFormat, bool, bool)
  def __init__(
      self,
      device: QByteArray,
      desc: str,
      mode: QAudioDevice.Mode,
      preferredFormat: QAudioFormat,
      isBluetoothDevice: bool,
      isDefaultDevice: bool = False,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAndroidAudioDevice::QAndroidAudioDevice(QByteArray device, QString
    desc, QAudioDevice::Mode mode, QAudioFormat preferredFormat, bool
    isBluetoothDevice, bool isDefaultDevice)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qandroidaudiodevice.html#QAndroidAudioDevice

    Parameters
    ----------

    device : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    desc : str
      Passed on as it is: a QString is made of it for the call.

    mode : QAudioDevice.Mode
      Passed on as its number.

    preferredFormat : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.

    isBluetoothDevice : bool
      Passed on as it is.

    isDefaultDevice : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  QAndroidAudioDevice::QAndroidAudioDevice(QByteArray device, QString
    #      desc, QAudioDevice::Mode mode, QAudioFormat preferredFormat, bool
    #      isBluetoothDevice, bool isDefaultDevice)
    self._noteCreation(QAndroidAudioDevice, lambda: Rituals.call(
        'ritual_ZN19QAndroidAudioDeviceC1E10QByteArray7QStringN12QAudioDevi'
        'ce4ModeE12QAudioFormatbb',
        self._valueOf(device), desc, mode.value,
        self._valueOf(preferredFormat), isBluetoothDevice, isDefaultDevice,
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
