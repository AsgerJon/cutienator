"""
QModbusExceptionResponse binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/qmodbuspdu.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QModbusPdu, QModbusResponse


class QModbusExceptionResponse(QModbusResponse):
  """
  The cute side of Qt's QModbusExceptionResponse: a plain Python object
  standing in front of one C++ QModbusExceptionResponse.

  It is built on the cute 'QModbusResponse', as Qt's QModbusExceptionResponse
  is built on Qt's QModbusResponse, and has everything that class has.

  C++ hands a QModbusExceptionResponse around as a copy, so every C++
  QModbusExceptionResponse behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QModbusExceptionResponse that has a ritual and that
  Python can call so far, 2 names in all: 'setFunctionCode',
  'setExceptionCode'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QModbusExceptionResponse::QModbusExceptionResponse(const QModbusPdu
    &pdu)': takes a type Python has no way to hand over yet.
  - Qt's 'QModbusExceptionResponse::~QModbusExceptionResponse()': the
    destructor: Python removes its C++ QModbusExceptionResponse by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QModbusExceptionResponse is created at the first use, not by
    'QModbusExceptionResponse(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QModbusExceptionResponse back gives a copy the ritual
    made for Python, in a new cute QModbusExceptionResponse.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QModbusExceptionResponse'

  #  A C++ QModbusExceptionResponse Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QModbusExceptionResponse'

  #  Qt's '~QModbusExceptionResponse()'. Naming it makes this a value class:
  #  Python owns every C++ QModbusExceptionResponse behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24QModbusExceptionResponseD1Ev'

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

  @overload(QModbusPdu.FunctionCode)
  def setFunctionCode(self, c: QModbusPdu.FunctionCode) -> None:
    """
    Calls Qt's 'void QModbusExceptionResponse::setFunctionCode(FunctionCode
    c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusexceptionresponse.html#setFunctionCode

    Parameters
    ----------

    c : QModbusPdu.FunctionCode
      Passed on as its number.
    """
    #  void QModbusExceptionResponse::setFunctionCode(FunctionCode c)
    ritual = (
        'ritual_ZN24QModbusExceptionResponse15setFunctionCodeEN10QModbusPdu'
        '12FunctionCodeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QModbusExceptionResponse15setFunctionCodeEN10QMod'
          'busPdu12FunctionCodeE')
    self.uglySide.call(ritual, c.value)

  @overload(QModbusPdu.ExceptionCode)
  def setExceptionCode(self, ec: QModbusPdu.ExceptionCode) -> None:
    """
    Calls Qt's 'void QModbusExceptionResponse::setExceptionCode(ExceptionCode
    ec)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusexceptionresponse.html#setExceptionCode

    Parameters
    ----------

    ec : QModbusPdu.ExceptionCode
      Passed on as its number.
    """
    #  void QModbusExceptionResponse::setExceptionCode(ExceptionCode ec)
    self.uglySide.call(
        'ritual_ZN24QModbusExceptionResponse16setExceptionCodeEN10QModbusPd'
        'u13ExceptionCodeE',
        ec.value,
    )

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QModbusExceptionResponse::QModbusExceptionResponse()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusexceptionresponse.html
    """
    #  QModbusExceptionResponse::QModbusExceptionResponse()
    self._noteCreation(QModbusExceptionResponse, lambda: Rituals.call(
        'ritual_ZN24QModbusExceptionResponseC1Ev',
    ))

  @overload(QModbusPdu.FunctionCode, QModbusPdu.ExceptionCode)
  def __init__(
      self,
      fc: QModbusPdu.FunctionCode,
      ec: QModbusPdu.ExceptionCode,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QModbusExceptionResponse::QModbusExceptionResponse(FunctionCode fc,
    ExceptionCode ec)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusexceptionresponse.html

    Parameters
    ----------

    fc : QModbusPdu.FunctionCode
      Passed on as its number.

    ec : QModbusPdu.ExceptionCode
      Passed on as its number.
    """
    #  QModbusExceptionResponse::QModbusExceptionResponse(FunctionCode fc,
    #      ExceptionCode ec)
    self._noteCreation(QModbusExceptionResponse, lambda: Rituals.call(
        'ritual_ZN24QModbusExceptionResponseC1EN10QModbusPdu12FunctionCodeE'
        'NS0_13ExceptionCodeE',
        fc.value, ec.value,
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
