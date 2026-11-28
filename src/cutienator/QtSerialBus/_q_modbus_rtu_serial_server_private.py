"""
QModbusRtuSerialServerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/6.12.0/QtSerialBus/private/qmodbusrtuserialserver_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QModbusRtuSerialServerPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QModbusServerPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QIODevice
  from . import QModbusRtuSerialServer


class QModbusRtuSerialServerPrivate(QModbusServerPrivate):
  """
  The cute side of Qt's QModbusRtuSerialServerPrivate: a plain Python object
  standing in front of one C++ QModbusRtuSerialServerPrivate.

  It is built on the cute 'QModbusServerPrivate', as Qt's
  QModbusRtuSerialServerPrivate is built on Qt's QModbusServerPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QModbusRtuSerialServerPrivate that has a ritual and
  that Python can call so far, 4 names in all: 'q_func', 'setupSerialPort',
  'setupEnvironment', 'device'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QModbusRtuSerialServer
    *QModbusRtuSerialServerPrivate::q_func() const': takes in Python what
    'QModbusRtuSerialServer *QModbusRtuSerialServerPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QModbusRtuSerialServerPrivate is created at the first use, not by
    'QModbusRtuSerialServerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QModbusRtuSerialServerPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QModbusRtuSerialServerPrivate'

  #  A C++ QModbusRtuSerialServerPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QModbusRtuSerialServerPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def device(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QModbusRtuSerialServerPrivate::device() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusrtuserialserverprivate.html#device

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QModbusRtuSerialServerPrivate::device() const
    ritual = 'ritual_ZNK29QModbusRtuSerialServerPrivate6deviceEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK29QModbusRtuSerialServerPrivate6deviceEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

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

  def q_func(self) -> Optional[QModbusRtuSerialServer]:
    """
    Calls Qt's 'QModbusRtuSerialServer
    *QModbusRtuSerialServerPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusrtuserialserverprivate.html#q_func

    Returns
    -------

    Optional[QModbusRtuSerialServer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QModbusRtuSerialServer *QModbusRtuSerialServerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN29QModbusRtuSerialServerPrivate6q_funcEv',
    )
    from . import QModbusRtuSerialServer
    return QModbusRtuSerialServer._cuteAt(address)

  def setupSerialPort(self) -> None:
    """
    Calls Qt's 'void QModbusRtuSerialServerPrivate::setupSerialPort()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusrtuserialserverprivate.html#setupSerialPort
    """
    #  void QModbusRtuSerialServerPrivate::setupSerialPort()
    self.uglySide.call(
        'ritual_ZN29QModbusRtuSerialServerPrivate15setupSerialPortEv',
    )

  def setupEnvironment(self) -> None:
    """
    Calls Qt's 'void QModbusRtuSerialServerPrivate::setupEnvironment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmodbusrtuserialserverprivate.html
    """
    #  void QModbusRtuSerialServerPrivate::setupEnvironment()
    self.uglySide.call(
        'ritual_ZN29QModbusRtuSerialServerPrivate16setupEnvironmentEv',
    )
