"""
QModbusResponse binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/qmodbuspdu.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QModbusPdu

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QModbusResponse(QModbusPdu):
  """
  The cute side of Qt's QModbusResponse: a plain Python object standing in
  front of one C++ QModbusResponse.

  It is built on the cute 'QModbusPdu', as Qt's QModbusResponse is built on
  Qt's QModbusPdu, and has everything that class has.

  C++ hands a QModbusResponse around as a copy, so every C++ QModbusResponse
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QModbusResponse that has a ritual and that Python
  can call so far, 2 names in all: 'minimumDataSize', 'calculateDataSize'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QModbusResponse::QModbusResponse(const QModbusPdu &pdu)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QModbusResponse::~QModbusResponse()': the destructor: Python
    removes its C++ QModbusResponse by it, and has no other use for it.
  - Qt's 'void QModbusResponse::registerDataSizeCalculator(FunctionCode fc,
    CalcFuncPtr func)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 8 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QModbusResponse is created at the first use, not by
    'QModbusResponse(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QModbusResponse back gives a copy the ritual made for
    Python, in a new cute QModbusResponse.
  - Each name of Qt's QModbusResponse that has no cute function yet,
    'registerDataSizeCalculator', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS)
  def minimumDataSize(pdu: QModbusResponse) -> int:
    """
    Calls Qt's 'int QModbusResponse::minimumDataSize(const QModbusResponse
    &pdu)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusresponse.html#minimumDataSize

    Parameters
    ----------

    pdu : QModbusResponse
      Passed on as a value: Qt reads the C++ QModbusResponse, which stays
      Python's own.
    """
    #  int QModbusResponse::minimumDataSize(const QModbusResponse &pdu)
    return Rituals.call(
        'ritual_ZN15QModbusResponse15minimumDataSizeERKS_',
        CuteMixin._valueOf(pdu),
    )

  @staticmethod
  @overload(THIS)
  def calculateDataSize(pdu: QModbusResponse) -> int:
    """
    Calls Qt's 'int QModbusResponse::calculateDataSize(const QModbusResponse
    &pdu)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusresponse.html#calculateDataSize

    Parameters
    ----------

    pdu : QModbusResponse
      Passed on as a value: Qt reads the C++ QModbusResponse, which stays
      Python's own.
    """
    #  int QModbusResponse::calculateDataSize(const QModbusResponse &pdu)
    return Rituals.call(
        'ritual_ZN15QModbusResponse17calculateDataSizeERKS_',
        CuteMixin._valueOf(pdu),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QModbusResponse'

  #  A C++ QModbusResponse Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QModbusResponse'

  #  Qt's '~QModbusResponse()'. Naming it makes this a value class: Python
  #  owns every C++ QModbusResponse behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QModbusResponseD1Ev'

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QModbusResponse::QModbusResponse()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusresponse.html#QModbusResponse
    """
    #  QModbusResponse::QModbusResponse()
    self._noteCreation(QModbusResponse, lambda: Rituals.call(
        'ritual_ZN15QModbusResponseC1Ev',
    ))

  @overload(QModbusPdu.FunctionCode)
  @overload(QModbusPdu.FunctionCode, QByteArray)
  def __init__(
      self,
      code: QModbusPdu.FunctionCode,
      newData: Optional[QByteArray] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QModbusResponse::QModbusResponse(FunctionCode code, const QByteArray
    &newData)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusresponse.html#QModbusResponse

    Parameters
    ----------

    code : QModbusPdu.FunctionCode
      Passed on as its number.

    newData : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.
    """
    #  QModbusResponse::QModbusResponse(FunctionCode code, const QByteArray
    #      &newData)
    if newData is None:
      from ..QtCore import QByteArray
      newData = QByteArray()
    self._noteCreation(QModbusResponse, lambda: Rituals.call(
        'ritual_ZN15QModbusResponseC1EN10QModbusPdu12FunctionCodeERK10QByte'
        'Array',
        code.value, self._valueOf(newData),
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

  @staticmethod
  def registerDataSizeCalculator(*__, **_) -> Never:
    """
    Qt's 'void QModbusResponse::registerDataSizeCalculator(FunctionCode fc,
    CalcFuncPtr func)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QModbusResponse.registerDataSizeCalculator' has no cute function "
        "yet. Qt's 'void "
        "QModbusResponse::registerDataSizeCalculator(FunctionCode fc, "
        "CalcFuncPtr func)': takes a type Python has no way to hand over "
        "yet.")
