"""
QmlAmbientTemperatureSensor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlambienttemperaturesensor_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QmlAmbientTemperatureSensor to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from . import QmlSensor

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtSensors import QSensor
  from . import QmlSensorReading

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QmlAmbientTemperatureSensor(QmlSensor):
  """
  The cute side of Qt's QmlAmbientTemperatureSensor: a plain Python object
  standing in front of one C++ QmlAmbientTemperatureSensor.

  It is built on the cute 'QmlSensor', as Qt's QmlAmbientTemperatureSensor is
  built on Qt's QmlSensor, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QmlAmbientTemperatureSensor that has a ritual and
  that Python can call so far, 4 names in all: 'metaObject', 'tr', 'sensor',
  'createReading'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QmlAmbientTemperatureSensor::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QmlAmbientTemperatureSensor::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QmlAmbientTemperatureSensor::~QmlAmbientTemperatureSensor()': the
    destructor: Python never removes a C++ QmlAmbientTemperatureSensor.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QmlAmbientTemperatureSensor is created at the first use, not by
    'QmlAmbientTemperatureSensor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QmlAmbientTemperatureSensor.
  - Qt tells when it has removed the C++ QmlAmbientTemperatureSensor. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QmlAmbientTemperatureSensor::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlambienttemperaturesensor.html#tr

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
    #  QString QmlAmbientTemperatureSensor::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN27QmlAmbientTemperatureSensor2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QmlAmbientTemperatureSensor'

  #  A C++ QmlAmbientTemperatureSensor Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QmlAmbientTemperatureSensor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QmlAmbientTemperatureSensor::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlambienttemperaturesensor.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QmlAmbientTemperatureSensor::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QmlAmbientTemperatureSensor10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sensor(self) -> Optional[QSensor]:
    """
    Calls Qt's 'QSensor *QmlAmbientTemperatureSensor::sensor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlambienttemperaturesensor.html#sensor

    Returns
    -------

    Optional[QSensor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSensor *QmlAmbientTemperatureSensor::sensor() const
    ritual = 'ritual_ZNK27QmlAmbientTemperatureSensor6sensorEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK27QmlAmbientTemperatureSensor6sensorEv'
    address = self.uglySide.call(ritual)
    from ..QtSensors import QSensor
    return QSensor._cuteAt(address)

  def createReading(self) -> Optional[QmlSensorReading]:
    """
    Calls Qt's 'QmlSensorReading
    *QmlAmbientTemperatureSensor::createReading() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlambienttemperaturesensor.html#createReading

    Returns
    -------

    Optional[QmlSensorReading]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QmlSensorReading *QmlAmbientTemperatureSensor::createReading() const
    ritual = 'ritual_ZNK27QmlAmbientTemperatureSensor13createReadingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK27QmlAmbientTemperatureSensor13createReadingEv'
    address = self.uglySide.call(ritual)
    from . import QmlSensorReading
    return QmlSensorReading._cuteAt(address)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QmlAmbientTemperatureSensor::QmlAmbientTemperatureSensor(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlambienttemperaturesensor.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QmlAmbientTemperatureSensor::QmlAmbientTemperatureSensor(QObject
    #      *parent)
    self._noteCreation(QmlAmbientTemperatureSensor, lambda: Rituals.call(
        'ritual_ZN27QmlAmbientTemperatureSensorC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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
