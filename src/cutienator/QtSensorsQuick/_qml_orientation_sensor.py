"""
QmlOrientationSensor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlorientationsensor_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QmlOrientationSensor to be private: it declares the class in a
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


class QmlOrientationSensor(QmlSensor):
  """
  The cute side of Qt's QmlOrientationSensor: a plain Python object standing
  in front of one C++ QmlOrientationSensor.

  It is built on the cute 'QmlSensor', as Qt's QmlOrientationSensor is built
  on Qt's QmlSensor, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QmlOrientationSensor that has a ritual and that
  Python can call so far, 4 names in all: 'metaObject', 'tr', 'sensor',
  'createReading'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QmlOrientationSensor::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QmlOrientationSensor::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QmlOrientationSensor::~QmlOrientationSensor()': the destructor:
    Python never removes a C++ QmlOrientationSensor.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QmlOrientationSensor is created at the first use, not by
    'QmlOrientationSensor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QmlOrientationSensor.
  - Qt tells when it has removed the C++ QmlOrientationSensor. Every call on
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
    Calls Qt's 'QString QmlOrientationSensor::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlorientationsensor.html#tr

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
    #  QString QmlOrientationSensor::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QmlOrientationSensor2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QmlOrientationSensor'

  #  A C++ QmlOrientationSensor Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QmlOrientationSensor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QmlOrientationSensor::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlorientationsensor.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QmlOrientationSensor::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QmlOrientationSensor10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sensor(self) -> Optional[QSensor]:
    """
    Calls Qt's 'QSensor *QmlOrientationSensor::sensor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlorientationsensor.html#sensor

    Returns
    -------

    Optional[QSensor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSensor *QmlOrientationSensor::sensor() const
    ritual = 'ritual_ZNK20QmlOrientationSensor6sensorEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QmlOrientationSensor6sensorEv'
    address = self.uglySide.call(ritual)
    from ..QtSensors import QSensor
    return QSensor._cuteAt(address)

  def createReading(self) -> Optional[QmlSensorReading]:
    """
    Calls Qt's 'QmlSensorReading *QmlOrientationSensor::createReading()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlorientationsensor.html#createReading

    Returns
    -------

    Optional[QmlSensorReading]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QmlSensorReading *QmlOrientationSensor::createReading() const
    ritual = 'ritual_ZNK20QmlOrientationSensor13createReadingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QmlOrientationSensor13createReadingEv'
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
    'QmlOrientationSensor::QmlOrientationSensor(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlorientationsensor.html#QmlOrientationSensor

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QmlOrientationSensor::QmlOrientationSensor(QObject *parent)
    self._noteCreation(QmlOrientationSensor, lambda: Rituals.call(
        'ritual_ZN20QmlOrientationSensorC1EP7QObject',
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
