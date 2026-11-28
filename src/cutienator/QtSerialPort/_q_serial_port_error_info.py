"""
QSerialPortErrorInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialPort/6.12.0/QtSerialPort/private/qserialport_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSerialPortErrorInfo to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QSerialPort


class QSerialPortErrorInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSerialPortErrorInfo: a plain Python object standing
  in front of one C++ QSerialPortErrorInfo.

  C++ hands a QSerialPortErrorInfo around as a copy, so every C++
  QSerialPortErrorInfo behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QSerialPortErrorInfo yet. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSerialPortErrorInfo::~QSerialPortErrorInfo()': the destructor:
    Python removes its C++ QSerialPortErrorInfo by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QSerialPortErrorInfo is created at the first use, not by
    'QSerialPortErrorInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSerialPortErrorInfo back gives a copy the ritual
    made for Python, in a new cute QSerialPortErrorInfo.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSerialPortErrorInfo'

  #  Qt's '~QSerialPortErrorInfo()'. Naming it makes this a value class:
  #  Python owns every C++ QSerialPortErrorInfo behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QSerialPortErrorInfoD1Ev'

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

  @overload()
  @overload(QSerialPort.SerialPortError)
  @overload(QSerialPort.SerialPortError, str)
  def __init__(
      self,
      newErrorCode: QSerialPort.SerialPortError = (
          QSerialPort.SerialPortError.UnknownError),
      newErrorString: str = '',
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSerialPortErrorInfo::QSerialPortErrorInfo(QSerialPort::SerialPortError
    newErrorCode, const QString &newErrorString)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qserialporterrorinfo.html#QSerialPortErrorInfo

    Parameters
    ----------

    newErrorCode : QSerialPort.SerialPortError
      Passed on as its number. May be left out, as in Qt: it is then
      QSerialPort.SerialPortError.UnknownError.

    newErrorString : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  QSerialPortErrorInfo::QSerialPortErrorInfo(QSerialPort::
    #      SerialPortError newErrorCode, const QString &newErrorString)
    self._noteCreation(QSerialPortErrorInfo, lambda: Rituals.call(
        'ritual_ZN20QSerialPortErrorInfoC1EN11QSerialPort15SerialPortErrorE'
        'RK7QString',
        newErrorCode.value, newErrorString,
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
