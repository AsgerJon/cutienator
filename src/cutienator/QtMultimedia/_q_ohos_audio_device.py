"""
QOhosAudioDevice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qohosaudiodevice_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QOhosAudioDevice to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
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


class QOhosAudioDevice(QAudioDevicePrivate):
  """
  The cute side of Qt's QOhosAudioDevice: a plain Python object standing in
  front of one C++ QOhosAudioDevice.

  It is built on the cute 'QAudioDevicePrivate', as Qt's QOhosAudioDevice is
  built on Qt's QAudioDevicePrivate, and has everything that class has.

  C++ hands a QOhosAudioDevice around as a copy, so every C++
  QOhosAudioDevice behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QOhosAudioDevice yet. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOhosAudioDevice::~QOhosAudioDevice()': the destructor: Python
    removes its C++ QOhosAudioDevice by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QOhosAudioDevice is created at the first use, not by
    'QOhosAudioDevice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOhosAudioDevice back gives a copy the ritual made
    for Python, in a new cute QOhosAudioDevice.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOhosAudioDevice'

  #  Qt's '~QOhosAudioDevice()'. Naming it makes this a value class: Python
  #  owns every C++ QOhosAudioDevice behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QOhosAudioDeviceD1Ev'

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

  @overload(QByteArray, str, QAudioDevice.Mode, QAudioFormat, int, bool)
  def __init__(
      self,
      id: QByteArray,
      description: str,
      mode: QAudioDevice.Mode,
      preferredFormat: QAudioFormat,
      maximumChannelCount: int,
      isDefaultDevice: bool,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOhosAudioDevice::QOhosAudioDevice(QByteArray id, QString description,
    QAudioDevice::Mode mode, QAudioFormat preferredFormat, int
    maximumChannelCount, bool isDefaultDevice)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qohosaudiodevice.html#QOhosAudioDevice

    Parameters
    ----------

    id : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    description : str
      Passed on as it is: a QString is made of it for the call.

    mode : QAudioDevice.Mode
      Passed on as its number.

    preferredFormat : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.

    maximumChannelCount : int
      Passed on as it is.

    isDefaultDevice : bool
      Passed on as it is.
    """
    #  QOhosAudioDevice::QOhosAudioDevice(QByteArray id, QString description,
    #      QAudioDevice::Mode mode, QAudioFormat preferredFormat, int
    #      maximumChannelCount, bool isDefaultDevice)
    self._noteCreation(QOhosAudioDevice, lambda: Rituals.call(
        'ritual_ZN16QOhosAudioDeviceC1E10QByteArray7QStringN12QAudioDevice4'
        'ModeE12QAudioFormatib',
        self._valueOf(id), description, mode.value,
        self._valueOf(preferredFormat), maximumChannelCount, isDefaultDevice,
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
