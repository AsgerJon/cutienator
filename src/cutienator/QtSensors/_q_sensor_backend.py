"""
QSensorBackend binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensors/qsensorbackend.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QSensor

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QSensorReading
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSensorReading = WAIT['QSensorReading']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSensorBackend(QObject):
  """
  The cute side of Qt's QSensorBackend: a plain Python object standing in
  front of one C++ QSensorBackend.

  It is built on the cute 'QObject', as Qt's QSensorBackend is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSensorBackend that has a ritual and that Python can
  call so far, 16 names in all: 'metaObject', 'tr', 'start', 'stop',
  'isFeatureSupported', 'addDataRate', 'setDataRates', 'addOutputRange',
  'setDescription', 'reading', 'sensor', 'newReadingAvailable',
  'sensorStopped', 'sensorBusy', 'sensorError', 'setReadings'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSensorBackend::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QSensorBackend::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QSensorBackend::~QSensorBackend()': the destructor: Python never
    removes a C++ QSensorBackend.
  - Qt's 'QSensorBackendPrivate *QSensorBackend::d_func()': gives
    'QSensorBackendPrivate', which has no cute class yet.
  - Qt's 'const QSensorBackendPrivate *QSensorBackend::d_func() const': gives
    'QSensorBackendPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  5 of the 27 functions Qt declares: 2 not a gap; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QSensorBackend is created at the first use, not by
    'QSensorBackend(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSensorBackend.
  - Qt tells when it has removed the C++ QSensorBackend. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSensorBackend that has no cute function yet,
    'setReading', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString QSensorBackend::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensorbackend.html#tr

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
    #  QString QSensorBackend::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QSensorBackend2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSensorBackend'

  #  A C++ QSensorBackend Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSensorBackend'

  #  The functions Qt calls itself that QSensorBackend is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'start': (
          ('_ZN14QSensorBackend5startEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'stop': (
          ('_ZN14QSensorBackend4stopEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'isFeatureSupported': (
          ('_ZNK14QSensorBackend18isFeatureSupportedEN7QSensor7FeatureE',
           ('bool', 'number', ''),
           (
               ('int', 'enum', 'QtSensors:QSensor.Feature'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSensorBackend::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensorbackend.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSensorBackend::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QSensorBackend10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QSensor.Feature)
  def isFeatureSupported(self, feature: QSensor.Feature) -> bool:
    """
    Calls Qt's 'bool QSensorBackend::isFeatureSupported(QSensor::Feature
    feature) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsensorbackend.html#isFeatureSupported

    Parameters
    ----------

    feature : QSensor.Feature
      Passed on as its number.
    """
    #  bool QSensorBackend::isFeatureSupported(QSensor::Feature feature)
    #      const
    ritual = (
        'ritual_ZNK14QSensorBackend18isFeatureSupportedEN7QSensor7FeatureE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QSensorBackend18isFeatureSupportedEN7QSensor7Fea'
          'tureE')
    return self.uglySide.call(ritual, feature.value)

  def reading(self) -> Optional[QSensorReading]:
    """
    Calls Qt's 'QSensorReading *QSensorBackend::reading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensorbackend.html#reading

    Returns
    -------

    Optional[QSensorReading]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSensorReading *QSensorBackend::reading() const
    address = self.uglySide.call('ritual_ZNK14QSensorBackend7readingEv')
    from . import QSensorReading
    return QSensorReading._cuteAt(address)

  def sensor(self) -> Optional[QSensor]:
    """
    Calls Qt's 'QSensor *QSensorBackend::sensor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensorbackend.html#sensor

    Returns
    -------

    Optional[QSensor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSensor *QSensorBackend::sensor() const
    address = self.uglySide.call('ritual_ZNK14QSensorBackend6sensorEv')
    return QSensor._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSensor)
  @overload(NoneType)
  def setDataRates(self, otherSensor: Optional[QSensor]) -> None:
    """
    Calls Qt's 'void QSensorBackend::setDataRates(const QSensor
    *otherSensor)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensorbackend.html#setDataRates

    Parameters
    ----------

    otherSensor : Optional[QSensor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSensorBackend::setDataRates(const QSensor *otherSensor)
    self.uglySide.call(
        'ritual_ZN14QSensorBackend12setDataRatesEPK7QSensor',
        self._addressOf(otherSensor),
    )

  @overload(str)
  def setDescription(self, description: str) -> None:
    """
    Calls Qt's 'void QSensorBackend::setDescription(const QString
    &description)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensorbackend.html#setDescription

    Parameters
    ----------

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSensorBackend::setDescription(const QString &description)
    self.uglySide.call(
        'ritual_ZN14QSensorBackend14setDescriptionERK7QString', description,
    )

  @overload(QSensorReading, QSensorReading, QSensorReading)
  @overload(QSensorReading, QSensorReading, NoneType)
  @overload(QSensorReading, NoneType, QSensorReading)
  @overload(QSensorReading, NoneType, NoneType)
  @overload(NoneType, QSensorReading, QSensorReading)
  @overload(NoneType, QSensorReading, NoneType)
  @overload(NoneType, NoneType, QSensorReading)
  @overload(NoneType, NoneType, NoneType)
  def setReadings(
      self,
      device: Optional[QSensorReading],
      filter: Optional[QSensorReading],
      cache: Optional[QSensorReading],
  ) -> None:
    """
    Calls Qt's 'void QSensorBackend::setReadings(QSensorReading *device,
    QSensorReading *filter, QSensorReading *cache)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensorbackend.html#setReadings

    Parameters
    ----------

    device : Optional[QSensorReading]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    filter : Optional[QSensorReading]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    cache : Optional[QSensorReading]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSensorBackend::setReadings(QSensorReading *device,
    #      QSensorReading *filter, QSensorReading *cache)
    self.uglySide.call(
        'ritual_ZN14QSensorBackend11setReadingsEP14QSensorReadingS1_S1_',
        self._addressOf(device), self._addressOf(filter),
        self._addressOf(cache),
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

  @overload(QSensor)
  @overload(NoneType)
  @overload(QSensor, QObject)
  @overload(QSensor, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      sensor: Optional[QSensor],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSensorBackend::QSensorBackend(QSensor
    *sensor, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsensorbackend.html#QSensorBackend

    Parameters
    ----------

    sensor : Optional[QSensor]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSensorBackend::QSensorBackend(QSensor *sensor, QObject *parent)
    self._noteCreation(QSensorBackend, lambda: Rituals.call(
        'ritual_ZN14QSensorBackendC1EP7QSensorP7QObject',
        self._addressOf(sensor), self._addressOf(parent, 'QObject'),
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

  def start(self) -> None:
    """
    Calls Qt's 'void QSensorBackend::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qsensorbackend.html#start
    """
    #  void QSensorBackend::start()
    self.uglySide.call('ritual_ZN14QSensorBackend5startEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QSensorBackend::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qsensorbackend.html#stop
    """
    #  void QSensorBackend::stop()
    self.uglySide.call('ritual_ZN14QSensorBackend4stopEv')

  @overload(float, float)
  def addDataRate(self, min: float, max: float) -> None:
    """
    Calls Qt's 'void QSensorBackend::addDataRate(qreal min, qreal max)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensorbackend.html#addDataRate

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.
    """
    #  void QSensorBackend::addDataRate(qreal min, qreal max)
    self.uglySide.call('ritual_ZN14QSensorBackend11addDataRateEdd', min, max)

  @overload(float, float, float)
  def addOutputRange(self, min: float, max: float, accuracy: float) -> None:
    """
    Calls Qt's 'void QSensorBackend::addOutputRange(qreal min, qreal max,
    qreal accuracy)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensorbackend.html#addOutputRange

    Parameters
    ----------

    min : float
      Passed on as it is.

    max : float
      Passed on as it is.

    accuracy : float
      Passed on as it is.
    """
    #  void QSensorBackend::addOutputRange(qreal min, qreal max, qreal
    #      accuracy)
    self.uglySide.call(
        'ritual_ZN14QSensorBackend14addOutputRangeEddd', min, max, accuracy,
    )

  def newReadingAvailable(self) -> None:
    """
    Calls Qt's 'void QSensorBackend::newReadingAvailable()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsensorbackend.html#newReadingAvailable
    """
    #  void QSensorBackend::newReadingAvailable()
    self.uglySide.call('ritual_ZN14QSensorBackend19newReadingAvailableEv')

  def sensorStopped(self) -> None:
    """
    Calls Qt's 'void QSensorBackend::sensorStopped()'.

    Qt's own words: https://doc.qt.io/qt-6/qsensorbackend.html#sensorStopped
    """
    #  void QSensorBackend::sensorStopped()
    self.uglySide.call('ritual_ZN14QSensorBackend13sensorStoppedEv')

  @overload()
  @overload(bool)
  def sensorBusy(self, busy: bool = True) -> None:
    """
    Calls Qt's 'void QSensorBackend::sensorBusy(bool busy)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensorbackend.html#sensorBusy

    Parameters
    ----------

    busy : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QSensorBackend::sensorBusy(bool busy)
    self.uglySide.call('ritual_ZN14QSensorBackend10sensorBusyEb', busy)

  @overload(int)
  def sensorError(self, error: int) -> None:
    """
    Calls Qt's 'void QSensorBackend::sensorError(int error)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensorbackend.html#sensorError

    Parameters
    ----------

    error : int
      Passed on as it is.
    """
    #  void QSensorBackend::sensorError(int error)
    self.uglySide.call('ritual_ZN14QSensorBackend11sensorErrorEi', error)

  @staticmethod
  def setReading(*__, **_) -> Never:
    """
    Qt's 'QSensorBackend::setReading': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QSensorBackend.setReading' has no cute function yet. Qt's "
        "'QSensorBackend::setReading': a template: a pattern and no single "
        "function.")
