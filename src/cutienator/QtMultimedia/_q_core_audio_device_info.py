"""
QCoreAudioDeviceInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qcoreaudiodevice_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QCoreAudioDeviceInfo to be private: it declares the class in a
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
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QCoreAudioDeviceInfo(QAudioDevicePrivate):
  """
  The cute side of Qt's QCoreAudioDeviceInfo: a plain Python object standing
  in front of one C++ QCoreAudioDeviceInfo.

  It is built on the cute 'QAudioDevicePrivate', as Qt's QCoreAudioDeviceInfo
  is built on Qt's QAudioDevicePrivate, and has everything that class has.

  C++ hands a QCoreAudioDeviceInfo around as a copy, so every C++
  QCoreAudioDeviceInfo behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QCoreAudioDeviceInfo yet. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCoreAudioDeviceInfo::~QCoreAudioDeviceInfo()': the destructor:
    Python removes its C++ QCoreAudioDeviceInfo by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QCoreAudioDeviceInfo is created at the first use, not by
    'QCoreAudioDeviceInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCoreAudioDeviceInfo back gives a copy the ritual
    made for Python, in a new cute QCoreAudioDeviceInfo.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCoreAudioDeviceInfo'

  #  Qt's '~QCoreAudioDeviceInfo()'. Naming it makes this a value class:
  #  Python owns every C++ QCoreAudioDeviceInfo behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QCoreAudioDeviceInfoD1Ev'

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

  @overload(QByteArray, QAudioDevice.Mode)
  def __init__(self, device: QByteArray, mode: QAudioDevice.Mode) -> None:
    """
    Notes what was given, for Qt's
    'QCoreAudioDeviceInfo::QCoreAudioDeviceInfo(const QByteArray &device,
    QAudioDevice::Mode mode)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreaudiodeviceinfo.html#QCoreAudioDeviceInfo

    Parameters
    ----------

    device : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    mode : QAudioDevice.Mode
      Passed on as its number.
    """
    #  QCoreAudioDeviceInfo::QCoreAudioDeviceInfo(const QByteArray &device,
    #      QAudioDevice::Mode mode)
    self._noteCreation(QCoreAudioDeviceInfo, lambda: Rituals.call(
        'ritual_ZN20QCoreAudioDeviceInfoC1ERK10QByteArrayN12QAudioDevice4Mo'
        'deE',
        self._valueOf(device), mode.value,
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
