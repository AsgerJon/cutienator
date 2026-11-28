"""
QSensor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensors/qsensor.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject
  from . import QSensorBackend, QSensorFilter, QSensorPrivate, QSensorReading
  from . import qoutputrange
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QSensorFilter = WAIT['QSensorFilter']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSensor(QObject):
  """
  The cute side of Qt's QSensor: a plain Python object standing in front of
  one C++ QSensor.

  It is built on the cute 'QObject', as Qt's QSensor is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSensor that has a ritual and that Python can call
  so far, 61 names in all: 'metaObject', 'tr', 'identifier', 'setIdentifier',
  'type', 'connectToBackend', 'isConnectedToBackend', 'isBusy', 'setActive',
  'isActive', 'isAlwaysOn', 'setAlwaysOn', 'skipDuplicates',
  'setSkipDuplicates', 'dataRate', 'setDataRate', 'outputRanges',
  'outputRange', 'setOutputRange', 'description', 'error', 'addFilter',
  'removeFilter', 'filters', 'reading', 'sensorTypes', 'sensorsForType',
  'defaultSensorForType', 'isFeatureSupported', 'axesOrientationMode',
  'setAxesOrientationMode', 'currentOrientation', 'setCurrentOrientation',
  'userOrientation', 'setUserOrientation', 'maxBufferSize',
  'setMaxBufferSize', 'efficientBufferSize', 'setEfficientBufferSize',
  'bufferSize', 'setBufferSize', 'start', 'stop', 'busyChanged',
  'activeChanged', 'readingChanged', 'sensorError',
  'availableSensorsChanged', 'alwaysOnChanged', 'dataRateChanged',
  'skipDuplicatesChanged', 'axesOrientationModeChanged',
  'currentOrientationChanged', 'userOrientationChanged',
  'maxBufferSizeChanged', 'efficientBufferSizeChanged', 'bufferSizeChanged',
  'identifierChanged', 'backend', 'registerInstance', 'd_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSensor::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int QSensor::qt_metacall(QMetaObject::Call a0, int a1, void **a2)':
    one of Qt's own inner workings.
  - Qt's 'QSensor::~QSensor()': the destructor: Python never removes a C++
    QSensor.
  - Qt's 'qrangelist QSensor::availableDataRates() const': gives a type
    Python has no way to take yet.
  - Qt's 'QSensor::QSensor(const QByteArray &type, QSensorPrivate &dd,
    QObject *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QSensorPrivate *QSensor::d_func() const': takes in Python
    what 'QSensorPrivate *QSensor::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 72 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QSensor is created at the first use, not by 'QSensor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSensor.
  - Qt tells when it has removed the C++ QSensor. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QSensor that has no cute function yet,
    'availableDataRates', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QSensor, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class AxesOrientationMode(CuteNum):
    """
    The enum 'QSensor::AxesOrientationMode' of Qt, with the 3 names Qt gives
    in it.
    """

    FixedOrientation = Kee[int](0)
    AutomaticOrientation = Kee[int](1)
    UserOrientation = Kee[int](2)

  class Feature(CuteNum):
    """The enum 'QSensor::Feature' of Qt, with the 9 names Qt gives in it."""

    Buffering = Kee[int](0)
    AlwaysOn = Kee[int](1)
    GeoValues = Kee[int](2)
    FieldOfView = Kee[int](3)
    AccelerationMode = Kee[int](4)
    SkipDuplicates = Kee[int](5)
    AxesOrientation = Kee[int](6)
    PressureSensorTemperature = Kee[int](7)
    Reserved = Kee[int](257)

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
    Calls Qt's 'QString QSensor::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#tr

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
    #  QString QSensor::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN7QSensor2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def sensorTypes() -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QSensor::sensorTypes()'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#sensorTypes

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QSensor::sensorTypes()
    address = Rituals.call('ritual_ZN7QSensor11sensorTypesEv')
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  @staticmethod
  @overload(QByteArray)
  def sensorsForType(type: QByteArray) -> QList[QByteArray]:
    """
    Calls Qt's 'QList<QByteArray> QSensor::sensorsForType(const QByteArray
    &type)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#sensorsForType

    Parameters
    ----------

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QList[QByteArray]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QByteArray> QSensor::sensorsForType(const QByteArray &type)
    address = Rituals.call(
        'ritual_ZN7QSensor14sensorsForTypeERK10QByteArray',
        CuteMixin._valueOf(type),
    )
    from ..QtCore import QByteArray
    return QList[QByteArray]._cuteOwning(address)

  @staticmethod
  @overload(QByteArray)
  def defaultSensorForType(type: QByteArray) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSensor::defaultSensorForType(const QByteArray
    &type)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#defaultSensorForType

    Parameters
    ----------

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSensor::defaultSensorForType(const QByteArray &type)
    address = Rituals.call(
        'ritual_ZN7QSensor20defaultSensorForTypeERK10QByteArray',
        CuteMixin._valueOf(type),
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSensor'

  #  A C++ QSensor Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSensor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSensor::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSensor::metaObject() const
    address = self.uglySide.call('ritual_ZNK7QSensor10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def identifier(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSensor::identifier() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#identifier

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSensor::identifier() const
    address = self.uglySide.call('ritual_ZNK7QSensor10identifierEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def type(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QSensor::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#type

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QSensor::type() const
    address = self.uglySide.call('ritual_ZNK7QSensor4typeEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def isConnectedToBackend(self) -> bool:
    """
    Calls Qt's 'bool QSensor::isConnectedToBackend() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#isConnectedToBackend
    """
    #  bool QSensor::isConnectedToBackend() const
    return self.uglySide.call('ritual_ZNK7QSensor20isConnectedToBackendEv')

  def isBusy(self) -> bool:
    """
    Calls Qt's 'bool QSensor::isBusy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#isBusy
    """
    #  bool QSensor::isBusy() const
    return self.uglySide.call('ritual_ZNK7QSensor6isBusyEv')

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QSensor::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#isActive
    """
    #  bool QSensor::isActive() const
    return self.uglySide.call('ritual_ZNK7QSensor8isActiveEv')

  def isAlwaysOn(self) -> bool:
    """
    Calls Qt's 'bool QSensor::isAlwaysOn() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#isAlwaysOn
    """
    #  bool QSensor::isAlwaysOn() const
    return self.uglySide.call('ritual_ZNK7QSensor10isAlwaysOnEv')

  def skipDuplicates(self) -> bool:
    """
    Calls Qt's 'bool QSensor::skipDuplicates() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#skipDuplicates
    """
    #  bool QSensor::skipDuplicates() const
    return self.uglySide.call('ritual_ZNK7QSensor14skipDuplicatesEv')

  def dataRate(self) -> int:
    """
    Calls Qt's 'int QSensor::dataRate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#dataRate
    """
    #  int QSensor::dataRate() const
    return self.uglySide.call('ritual_ZNK7QSensor8dataRateEv')

  def outputRanges(self) -> QList[qoutputrange]:
    """
    Calls Qt's 'qoutputrangelist QSensor::outputRanges() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#outputRanges

    Returns
    -------

    QList[qoutputrange]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  qoutputrangelist QSensor::outputRanges() const
    address = self.uglySide.call('ritual_ZNK7QSensor12outputRangesEv')
    from . import qoutputrange
    return QList[qoutputrange]._cuteOwning(address)

  def outputRange(self) -> int:
    """
    Calls Qt's 'int QSensor::outputRange() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#outputRange
    """
    #  int QSensor::outputRange() const
    return self.uglySide.call('ritual_ZNK7QSensor11outputRangeEv')

  def description(self) -> str:
    """
    Calls Qt's 'QString QSensor::description() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#description

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSensor::description() const
    return self.uglySide.call('ritual_ZNK7QSensor11descriptionEv')

  def error(self) -> int:
    """
    Calls Qt's 'int QSensor::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#error
    """
    #  int QSensor::error() const
    return self.uglySide.call('ritual_ZNK7QSensor5errorEv')

  def filters(self) -> QList[QSensorFilter]:
    """
    Calls Qt's 'QList<QSensorFilter *> QSensor::filters() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#filters

    Returns
    -------

    QList[QSensorFilter]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSensorFilter *> QSensor::filters() const
    address = self.uglySide.call('ritual_ZNK7QSensor7filtersEv')
    from . import QSensorFilter
    return QList[QSensorFilter]._cuteOwning(address)

  def reading(self) -> Optional[QSensorReading]:
    """
    Calls Qt's 'QSensorReading *QSensor::reading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#reading

    Returns
    -------

    Optional[QSensorReading]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSensorReading *QSensor::reading() const
    address = self.uglySide.call('ritual_ZNK7QSensor7readingEv')
    from . import QSensorReading
    return QSensorReading._cuteAt(address)

  @overload(Feature)
  def isFeatureSupported(self, feature: Feature) -> bool:
    """
    Calls Qt's 'bool QSensor::isFeatureSupported(Feature feature) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#isFeatureSupported

    Parameters
    ----------

    feature : Feature
      Passed on as its number.
    """
    #  bool QSensor::isFeatureSupported(Feature feature) const
    return self.uglySide.call(
        'ritual_ZNK7QSensor18isFeatureSupportedENS_7FeatureE', feature.value,
    )

  def axesOrientationMode(self) -> AxesOrientationMode:
    """
    Calls Qt's 'AxesOrientationMode QSensor::axesOrientationMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#axesOrientationMode

    Returns
    -------

    AxesOrientationMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'AxesOrientationMode(number)' gives.
    """
    #  AxesOrientationMode QSensor::axesOrientationMode() const
    return QSensor.AxesOrientationMode(self.uglySide.call(
        'ritual_ZNK7QSensor19axesOrientationModeEv',
    ))

  def currentOrientation(self) -> int:
    """
    Calls Qt's 'int QSensor::currentOrientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#currentOrientation
    """
    #  int QSensor::currentOrientation() const
    return self.uglySide.call('ritual_ZNK7QSensor18currentOrientationEv')

  def userOrientation(self) -> int:
    """
    Calls Qt's 'int QSensor::userOrientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#userOrientation
    """
    #  int QSensor::userOrientation() const
    return self.uglySide.call('ritual_ZNK7QSensor15userOrientationEv')

  def maxBufferSize(self) -> int:
    """
    Calls Qt's 'int QSensor::maxBufferSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#maxBufferSize
    """
    #  int QSensor::maxBufferSize() const
    return self.uglySide.call('ritual_ZNK7QSensor13maxBufferSizeEv')

  def efficientBufferSize(self) -> int:
    """
    Calls Qt's 'int QSensor::efficientBufferSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#efficientBufferSize
    """
    #  int QSensor::efficientBufferSize() const
    return self.uglySide.call('ritual_ZNK7QSensor19efficientBufferSizeEv')

  def bufferSize(self) -> int:
    """
    Calls Qt's 'int QSensor::bufferSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#bufferSize
    """
    #  int QSensor::bufferSize() const
    return self.uglySide.call('ritual_ZNK7QSensor10bufferSizeEv')

  def backend(self) -> Optional[QSensorBackend]:
    """
    Calls Qt's 'QSensorBackend *QSensor::backend() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#backend

    Returns
    -------

    Optional[QSensorBackend]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSensorBackend *QSensor::backend() const
    address = self.uglySide.call('ritual_ZNK7QSensor7backendEv')
    from . import QSensorBackend
    return QSensorBackend._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def setIdentifier(self, identifier: QByteArray) -> None:
    """
    Calls Qt's 'void QSensor::setIdentifier(const QByteArray &identifier)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#setIdentifier

    Parameters
    ----------

    identifier : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSensor::setIdentifier(const QByteArray &identifier)
    self.uglySide.call(
        'ritual_ZN7QSensor13setIdentifierERK10QByteArray',
        self._valueOf(identifier),
    )

  @overload(bool)
  def setActive(self, active: bool) -> None:
    """
    Calls Qt's 'void QSensor::setActive(bool active)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#setActive

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QSensor::setActive(bool active)
    self.uglySide.call('ritual_ZN7QSensor9setActiveEb', active)

  @overload(bool)
  def setAlwaysOn(self, alwaysOn: bool) -> None:
    """
    Calls Qt's 'void QSensor::setAlwaysOn(bool alwaysOn)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#setAlwaysOn

    Parameters
    ----------

    alwaysOn : bool
      Passed on as it is.
    """
    #  void QSensor::setAlwaysOn(bool alwaysOn)
    self.uglySide.call('ritual_ZN7QSensor11setAlwaysOnEb', alwaysOn)

  @overload(bool)
  def setSkipDuplicates(self, skipDuplicates: bool) -> None:
    """
    Calls Qt's 'void QSensor::setSkipDuplicates(bool skipDuplicates)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#setSkipDuplicates

    Parameters
    ----------

    skipDuplicates : bool
      Passed on as it is.
    """
    #  void QSensor::setSkipDuplicates(bool skipDuplicates)
    self.uglySide.call(
        'ritual_ZN7QSensor17setSkipDuplicatesEb', skipDuplicates,
    )

  @overload(int)
  def setDataRate(self, rate: int) -> None:
    """
    Calls Qt's 'void QSensor::setDataRate(int rate)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#setDataRate

    Parameters
    ----------

    rate : int
      Passed on as it is.
    """
    #  void QSensor::setDataRate(int rate)
    self.uglySide.call('ritual_ZN7QSensor11setDataRateEi', rate)

  @overload(int)
  def setOutputRange(self, index: int) -> None:
    """
    Calls Qt's 'void QSensor::setOutputRange(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#setOutputRange

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QSensor::setOutputRange(int index)
    self.uglySide.call('ritual_ZN7QSensor14setOutputRangeEi', index)

  @overload(AxesOrientationMode)
  def setAxesOrientationMode(
      self,
      axesOrientationMode: AxesOrientationMode,
  ) -> None:
    """
    Calls Qt's 'void QSensor::setAxesOrientationMode(AxesOrientationMode
    axesOrientationMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsensor.html#setAxesOrientationMode

    Parameters
    ----------

    axesOrientationMode : AxesOrientationMode
      Passed on as its number.
    """
    #  void QSensor::setAxesOrientationMode(AxesOrientationMode
    #      axesOrientationMode)
    self.uglySide.call(
        'ritual_ZN7QSensor22setAxesOrientationModeENS_19AxesOrientationMode'
        'E',
        axesOrientationMode.value,
    )

  @overload(int)
  def setCurrentOrientation(self, currentOrientation: int) -> None:
    """
    Calls Qt's 'void QSensor::setCurrentOrientation(int currentOrientation)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#setCurrentOrientation

    Parameters
    ----------

    currentOrientation : int
      Passed on as it is.
    """
    #  void QSensor::setCurrentOrientation(int currentOrientation)
    self.uglySide.call(
        'ritual_ZN7QSensor21setCurrentOrientationEi', currentOrientation,
    )

  @overload(int)
  def setUserOrientation(self, userOrientation: int) -> None:
    """
    Calls Qt's 'void QSensor::setUserOrientation(int userOrientation)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#setUserOrientation

    Parameters
    ----------

    userOrientation : int
      Passed on as it is.
    """
    #  void QSensor::setUserOrientation(int userOrientation)
    self.uglySide.call(
        'ritual_ZN7QSensor18setUserOrientationEi', userOrientation,
    )

  @overload(int)
  def setMaxBufferSize(self, maxBufferSize: int) -> None:
    """
    Calls Qt's 'void QSensor::setMaxBufferSize(int maxBufferSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#setMaxBufferSize

    Parameters
    ----------

    maxBufferSize : int
      Passed on as it is.
    """
    #  void QSensor::setMaxBufferSize(int maxBufferSize)
    self.uglySide.call(
        'ritual_ZN7QSensor16setMaxBufferSizeEi', maxBufferSize,
    )

  @overload(int)
  def setEfficientBufferSize(self, efficientBufferSize: int) -> None:
    """
    Calls Qt's 'void QSensor::setEfficientBufferSize(int
    efficientBufferSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsensor.html#setEfficientBufferSize

    Parameters
    ----------

    efficientBufferSize : int
      Passed on as it is.
    """
    #  void QSensor::setEfficientBufferSize(int efficientBufferSize)
    self.uglySide.call(
        'ritual_ZN7QSensor22setEfficientBufferSizeEi', efficientBufferSize,
    )

  @overload(int)
  def setBufferSize(self, bufferSize: int) -> None:
    """
    Calls Qt's 'void QSensor::setBufferSize(int bufferSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#setBufferSize

    Parameters
    ----------

    bufferSize : int
      Passed on as it is.
    """
    #  void QSensor::setBufferSize(int bufferSize)
    self.uglySide.call('ritual_ZN7QSensor13setBufferSizeEi', bufferSize)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  @overload(QByteArray, QObject)
  @overload(QByteArray, NoneType)
  def __init__(
      self,
      type: QByteArray,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QSensor::QSensor(const QByteArray &type,
    QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#QSensor

    Parameters
    ----------

    type : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSensor::QSensor(const QByteArray &type, QObject *parent)
    self._noteCreation(QSensor, lambda: Rituals.call(
        'ritual_ZN7QSensorC1ERK10QByteArrayP7QObject',
        self._valueOf(type), self._addressOf(parent, 'QObject'),
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

  def connectToBackend(self) -> bool:
    """
    Calls Qt's 'bool QSensor::connectToBackend()'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#connectToBackend
    """
    #  bool QSensor::connectToBackend()
    return self.uglySide.call('ritual_ZN7QSensor16connectToBackendEv')

  @overload(QSensorFilter)
  @overload(NoneType)
  def addFilter(self, filter: Optional[QSensorFilter]) -> None:
    """
    Calls Qt's 'void QSensor::addFilter(QSensorFilter *filter)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#addFilter

    Parameters
    ----------

    filter : Optional[QSensorFilter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSensor::addFilter(QSensorFilter *filter)
    self.uglySide.call(
        'ritual_ZN7QSensor9addFilterEP13QSensorFilter',
        self._addressOf(filter),
    )

  @overload(QSensorFilter)
  @overload(NoneType)
  def removeFilter(self, filter: Optional[QSensorFilter]) -> None:
    """
    Calls Qt's 'void QSensor::removeFilter(QSensorFilter *filter)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#removeFilter

    Parameters
    ----------

    filter : Optional[QSensorFilter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSensor::removeFilter(QSensorFilter *filter)
    self.uglySide.call(
        'ritual_ZN7QSensor12removeFilterEP13QSensorFilter',
        self._addressOf(filter),
    )

  def start(self) -> bool:
    """
    Calls Qt's 'bool QSensor::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#start
    """
    #  bool QSensor::start()
    return self.uglySide.call('ritual_ZN7QSensor5startEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QSensor::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#stop
    """
    #  void QSensor::stop()
    self.uglySide.call('ritual_ZN7QSensor4stopEv')

  def busyChanged(self) -> None:
    """
    Calls Qt's 'void QSensor::busyChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#busyChanged
    """
    #  void QSensor::busyChanged()
    self.uglySide.call('ritual_ZN7QSensor11busyChangedEv')

  def activeChanged(self) -> None:
    """
    Calls Qt's 'void QSensor::activeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#activeChanged
    """
    #  void QSensor::activeChanged()
    self.uglySide.call('ritual_ZN7QSensor13activeChangedEv')

  def readingChanged(self) -> None:
    """
    Calls Qt's 'void QSensor::readingChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#readingChanged
    """
    #  void QSensor::readingChanged()
    self.uglySide.call('ritual_ZN7QSensor14readingChangedEv')

  @overload(int)
  def sensorError(self, error: int) -> None:
    """
    Calls Qt's 'void QSensor::sensorError(int error)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#sensorError

    Parameters
    ----------

    error : int
      Passed on as it is.
    """
    #  void QSensor::sensorError(int error)
    self.uglySide.call('ritual_ZN7QSensor11sensorErrorEi', error)

  def availableSensorsChanged(self) -> None:
    """
    Calls Qt's 'void QSensor::availableSensorsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsensor.html#availableSensorsChanged
    """
    #  void QSensor::availableSensorsChanged()
    self.uglySide.call('ritual_ZN7QSensor23availableSensorsChangedEv')

  def alwaysOnChanged(self) -> None:
    """
    Calls Qt's 'void QSensor::alwaysOnChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#alwaysOnChanged
    """
    #  void QSensor::alwaysOnChanged()
    self.uglySide.call('ritual_ZN7QSensor15alwaysOnChangedEv')

  def dataRateChanged(self) -> None:
    """
    Calls Qt's 'void QSensor::dataRateChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#dataRateChanged
    """
    #  void QSensor::dataRateChanged()
    self.uglySide.call('ritual_ZN7QSensor15dataRateChangedEv')

  @overload(bool)
  def skipDuplicatesChanged(self, skipDuplicates: bool) -> None:
    """
    Calls Qt's 'void QSensor::skipDuplicatesChanged(bool skipDuplicates)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#skipDuplicatesChanged

    Parameters
    ----------

    skipDuplicates : bool
      Passed on as it is.
    """
    #  void QSensor::skipDuplicatesChanged(bool skipDuplicates)
    self.uglySide.call(
        'ritual_ZN7QSensor21skipDuplicatesChangedEb', skipDuplicates,
    )

  @overload(AxesOrientationMode)
  def axesOrientationModeChanged(
      self,
      axesOrientationMode: AxesOrientationMode,
  ) -> None:
    """
    Calls Qt's 'void QSensor::axesOrientationModeChanged(AxesOrientationMode
    axesOrientationMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsensor.html#axesOrientationModeChanged

    Parameters
    ----------

    axesOrientationMode : AxesOrientationMode
      Passed on as its number.
    """
    #  void QSensor::axesOrientationModeChanged(AxesOrientationMode
    #      axesOrientationMode)
    self.uglySide.call(
        'ritual_ZN7QSensor26axesOrientationModeChangedENS_19AxesOrientation'
        'ModeE',
        axesOrientationMode.value,
    )

  @overload(int)
  def currentOrientationChanged(self, currentOrientation: int) -> None:
    """
    Calls Qt's 'void QSensor::currentOrientationChanged(int
    currentOrientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsensor.html#currentOrientationChanged

    Parameters
    ----------

    currentOrientation : int
      Passed on as it is.
    """
    #  void QSensor::currentOrientationChanged(int currentOrientation)
    self.uglySide.call(
        'ritual_ZN7QSensor25currentOrientationChangedEi', currentOrientation,
    )

  @overload(int)
  def userOrientationChanged(self, userOrientation: int) -> None:
    """
    Calls Qt's 'void QSensor::userOrientationChanged(int userOrientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsensor.html#userOrientationChanged

    Parameters
    ----------

    userOrientation : int
      Passed on as it is.
    """
    #  void QSensor::userOrientationChanged(int userOrientation)
    self.uglySide.call(
        'ritual_ZN7QSensor22userOrientationChangedEi', userOrientation,
    )

  @overload(int)
  def maxBufferSizeChanged(self, maxBufferSize: int) -> None:
    """
    Calls Qt's 'void QSensor::maxBufferSizeChanged(int maxBufferSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#maxBufferSizeChanged

    Parameters
    ----------

    maxBufferSize : int
      Passed on as it is.
    """
    #  void QSensor::maxBufferSizeChanged(int maxBufferSize)
    self.uglySide.call(
        'ritual_ZN7QSensor20maxBufferSizeChangedEi', maxBufferSize,
    )

  @overload(int)
  def efficientBufferSizeChanged(self, efficientBufferSize: int) -> None:
    """
    Calls Qt's 'void QSensor::efficientBufferSizeChanged(int
    efficientBufferSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsensor.html#efficientBufferSizeChanged

    Parameters
    ----------

    efficientBufferSize : int
      Passed on as it is.
    """
    #  void QSensor::efficientBufferSizeChanged(int efficientBufferSize)
    self.uglySide.call(
        'ritual_ZN7QSensor26efficientBufferSizeChangedEi',
        efficientBufferSize,
    )

  @overload(int)
  def bufferSizeChanged(self, bufferSize: int) -> None:
    """
    Calls Qt's 'void QSensor::bufferSizeChanged(int bufferSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#bufferSizeChanged

    Parameters
    ----------

    bufferSize : int
      Passed on as it is.
    """
    #  void QSensor::bufferSizeChanged(int bufferSize)
    self.uglySide.call('ritual_ZN7QSensor17bufferSizeChangedEi', bufferSize)

  def identifierChanged(self) -> None:
    """
    Calls Qt's 'void QSensor::identifierChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#identifierChanged
    """
    #  void QSensor::identifierChanged()
    self.uglySide.call('ritual_ZN7QSensor17identifierChangedEv')

  def registerInstance(self) -> None:
    """
    Calls Qt's 'void QSensor::registerInstance()'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#registerInstance
    """
    #  void QSensor::registerInstance()
    self.uglySide.call('ritual_ZN7QSensor16registerInstanceEv')

  def d_func(self) -> Optional[QSensorPrivate]:
    """
    Calls Qt's 'QSensorPrivate *QSensor::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsensor.html#d_func

    Returns
    -------

    Optional[QSensorPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSensorPrivate *QSensor::d_func()
    address = self.uglySide.call('ritual_ZN7QSensor6d_funcEv')
    from . import QSensorPrivate
    return QSensorPrivate._cuteAt(address)

  @staticmethod
  def availableDataRates(*__, **_) -> Never:
    """
    Qt's 'qrangelist QSensor::availableDataRates() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSensor.availableDataRates' has no cute function yet. Qt's "
        "'qrangelist QSensor::availableDataRates() const': gives a type "
        "Python has no way to take yet.")
