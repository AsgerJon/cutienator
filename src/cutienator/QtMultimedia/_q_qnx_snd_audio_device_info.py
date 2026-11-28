"""
QQnxSndAudioDeviceInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qqnxsndaudiodevice_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQnxSndAudioDeviceInfo to be private: it declares the class in a
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


class QQnxSndAudioDeviceInfo(QAudioDevicePrivate):
  """
  The cute side of Qt's QQnxSndAudioDeviceInfo: a plain Python object
  standing in front of one C++ QQnxSndAudioDeviceInfo.

  It is built on the cute 'QAudioDevicePrivate', as Qt's
  QQnxSndAudioDeviceInfo is built on Qt's QAudioDevicePrivate, and has
  everything that class has.

  What exists
  -----------

  No function of Qt's QQnxSndAudioDeviceInfo yet. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQnxSndAudioDeviceInfo::~QQnxSndAudioDeviceInfo()': the destructor:
    Python never removes a C++ QQnxSndAudioDeviceInfo.

  What has no ritual
  ------------------

  4 of the 6 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QQnxSndAudioDeviceInfo is created at the first use, not by
    'QQnxSndAudioDeviceInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQnxSndAudioDeviceInfo.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQnxSndAudioDeviceInfo'

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

  @overload(QByteArray, str, QAudioDevice.Mode)
  def __init__(
      self,
      dev: QByteArray,
      description: str,
      mode: QAudioDevice.Mode,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQnxSndAudioDeviceInfo::QQnxSndAudioDeviceInfo(const QByteArray &dev,
    const QString &description, QAudioDevice::Mode mode)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqnxsndaudiodeviceinfo.html#QQnxSndAudioDeviceInfo

    Parameters
    ----------

    dev : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    description : str
      Passed on as it is: a QString is made of it for the call.

    mode : QAudioDevice.Mode
      Passed on as its number.
    """
    #  QQnxSndAudioDeviceInfo::QQnxSndAudioDeviceInfo(const QByteArray &dev,
    #      const QString &description, QAudioDevice::Mode mode)
    self._noteCreation(QQnxSndAudioDeviceInfo, lambda: Rituals.call(
        'ritual_ZN22QQnxSndAudioDeviceInfoC1ERK10QByteArrayRK7QStringN12QAu'
        'dioDevice4ModeE',
        self._valueOf(dev), description, mode.value,
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
