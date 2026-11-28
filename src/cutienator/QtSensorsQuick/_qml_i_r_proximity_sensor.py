"""
QmlIRProximitySensor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlirproximitysensor_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QmlIRProximitySensor to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
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


class QmlIRProximitySensor(QmlSensor):
  """
  The cute side of Qt's QmlIRProximitySensor: a plain Python object standing
  in front of one C++ QmlIRProximitySensor.

  It is built on the cute 'QmlSensor', as Qt's QmlIRProximitySensor is built
  on Qt's QmlSensor, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QmlIRProximitySensor that has a ritual and that
  Python can call so far, 4 names in all: 'metaObject', 'tr', 'sensor',
  'createReading'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QmlIRProximitySensor::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QmlIRProximitySensor::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QmlIRProximitySensor::~QmlIRProximitySensor()': the destructor:
    Python never removes a C++ QmlIRProximitySensor.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QmlIRProximitySensor is created at the first use, not by
    'QmlIRProximitySensor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QmlIRProximitySensor.
  - Qt tells when it has removed the C++ QmlIRProximitySensor. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QmlIRProximitySensor::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlirproximitysensor.html#tr

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
    #  QString QmlIRProximitySensor::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QmlIRProximitySensor2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QmlIRProximitySensor'

  #  A C++ QmlIRProximitySensor Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QmlIRProximitySensor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QmlIRProximitySensor::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlirproximitysensor.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QmlIRProximitySensor::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QmlIRProximitySensor10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sensor(self) -> Optional[QSensor]:
    """
    Calls Qt's 'QSensor *QmlIRProximitySensor::sensor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlirproximitysensor.html#sensor

    Returns
    -------

    Optional[QSensor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSensor *QmlIRProximitySensor::sensor() const
    ritual = 'ritual_ZNK20QmlIRProximitySensor6sensorEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QmlIRProximitySensor6sensorEv'
    address = self.uglySide.call(ritual)
    from ..QtSensors import QSensor
    return QSensor._cuteAt(address)

  def createReading(self) -> Optional[QmlSensorReading]:
    """
    Calls Qt's 'QmlSensorReading *QmlIRProximitySensor::createReading()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlirproximitysensor.html#createReading

    Returns
    -------

    Optional[QmlSensorReading]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QmlSensorReading *QmlIRProximitySensor::createReading() const
    ritual = 'ritual_ZNK20QmlIRProximitySensor13createReadingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QmlIRProximitySensor13createReadingEv'
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
    'QmlIRProximitySensor::QmlIRProximitySensor(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlirproximitysensor.html#QmlIRProximitySensor

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QmlIRProximitySensor::QmlIRProximitySensor(QObject *parent)
    self._noteCreation(QmlIRProximitySensor, lambda: Rituals.call(
        'ritual_ZN20QmlIRProximitySensorC1EP7QObject',
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
