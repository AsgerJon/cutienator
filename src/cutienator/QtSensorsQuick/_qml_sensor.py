"""
QmlSensor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlsensor_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QmlSensor to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject
  from ..QtSensors import QSensor
  from . import QmlSensorReading
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QmlSensor(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QmlSensor: a plain Python object standing in front of
  one C++ QmlSensor.

  It is built on the cute 'QObject', as Qt's QmlSensor is built on Qt's
  QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QmlSensor is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QmlSensor that has a ritual and that Python can call
  so far, 57 names in all: 'metaObject', 'tr', 'identifier', 'setIdentifier',
  'type', 'isConnectedToBackend', 'isBusy', 'setActive', 'isActive',
  'isAlwaysOn', 'setAlwaysOn', 'skipDuplicates', 'setSkipDuplicates',
  'dataRate', 'setDataRate', 'outputRange', 'setOutputRange', 'description',
  'error', 'reading', 'isFeatureSupported', 'axesOrientationMode',
  'setAxesOrientationMode', 'currentOrientation', 'userOrientation',
  'setUserOrientation', 'maxBufferSize', 'efficientBufferSize', 'bufferSize',
  'setBufferSize', 'sensor', 'componentComplete', 'start', 'stop',
  'identifierChanged', 'connectedToBackendChanged',
  'availableDataRatesChanged', 'dataRateChanged', 'readingChanged',
  'activeChanged', 'outputRangesChanged', 'outputRangeChanged',
  'descriptionChanged', 'errorChanged', 'alwaysOnChanged', 'busyChanged',
  'skipDuplicatesChanged', 'axesOrientationModeChanged',
  'currentOrientationChanged', 'userOrientationChanged',
  'maxBufferSizeChanged', 'efficientBufferSizeChanged', 'bufferSizeChanged',
  'createReading', 'updateReading', 'classBegin',
  '_qt_property_m_reading_offset'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QmlSensor::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QmlSensor::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QmlSensorPrivate *QmlSensor::d_func()': gives 'QmlSensorPrivate',
    which has no cute class yet.
  - Qt's 'const QmlSensorPrivate *QmlSensor::d_func() const': gives
    'QmlSensorPrivate', which has no cute class yet.
  - Qt's 'void QmlSensor::qt_qmlMarker_uncreatable()': one of Qt's own inner
    workings.
  - Qt's 'QmlSensor::~QmlSensor()': the destructor: Python never removes a
    C++ QmlSensor.
  - Qt's 'QQmlListProperty<QmlSensorRange> QmlSensor::availableDataRates()
    const': gives a type Python has no way to take yet.
  - Qt's 'QQmlListProperty<QmlSensorOutputRange> QmlSensor::outputRanges()
    const': gives a type Python has no way to take yet.
  - Qt's 'QBindable<QmlSensorReading *> QmlSensor::bindableReading() const':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 69 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QmlSensor is created at the first use, not by 'QmlSensor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QmlSensor.
  - Qt tells when it has removed the C++ QmlSensor. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QmlSensor that has no cute function yet,
    'availableDataRates', 'bindableReading', 'outputRanges', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QmlSensor, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class AxesOrientationMode(CuteNum):
    """
    The enum 'QmlSensor::AxesOrientationMode' of Qt, with the 3 names Qt
    gives in it.
    """

    FixedOrientation = Kee[int](0)
    AutomaticOrientation = Kee[int](1)
    UserOrientation = Kee[int](2)

  class Feature(CuteNum):
    """
    The enum 'QmlSensor::Feature' of Qt, with the 8 names Qt gives in it.
    """

    Buffering = Kee[int](0)
    AlwaysOn = Kee[int](1)
    GeoValues = Kee[int](2)
    FieldOfView = Kee[int](3)
    AccelerationMode = Kee[int](4)
    SkipDuplicates = Kee[int](5)
    AxesOrientation = Kee[int](6)
    PressureSensorTemperature = Kee[int](7)

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
    Calls Qt's 'QString QmlSensor::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#tr

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
    #  QString QmlSensor::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QmlSensor2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def _qt_property_m_reading_offset() -> int:
    """
    Calls Qt's 'size_t QmlSensor::_qt_property_m_reading_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlsensor.html#_qt_property_m_reading_offset
    """
    #  size_t QmlSensor::_qt_property_m_reading_offset()
    return Rituals.call(
        'ritual_ZN9QmlSensor29_qt_property_m_reading_offsetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QmlSensor'

  #  Qt's QmlSensor is built on more than one class. The part of a C++
  #  QmlSensor that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QmlSensor_QQmlParserStatus',
  }

  #  A C++ QmlSensor Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QmlSensor'

  #  The functions Qt calls itself that QmlSensor is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'sensor': (
          ('_ZNK9QmlSensor6sensorEv',
           ('address', 'address', 'QtSensors:QSensor'),
           ()),
      ),
      'createReading': (
          ('_ZNK9QmlSensor13createReadingEv',
           ('address', 'address', 'QtSensorsQuick:QmlSensorReading'),
           ()),
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
    Calls Qt's 'const QMetaObject *QmlSensor::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QmlSensor::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QmlSensor10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def identifier(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QmlSensor::identifier() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#identifier

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QmlSensor::identifier() const
    address = self.uglySide.call('ritual_ZNK9QmlSensor10identifierEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def type(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QmlSensor::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#type

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QmlSensor::type() const
    address = self.uglySide.call('ritual_ZNK9QmlSensor4typeEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def isConnectedToBackend(self) -> bool:
    """
    Calls Qt's 'bool QmlSensor::isConnectedToBackend() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlsensor.html#isConnectedToBackend
    """
    #  bool QmlSensor::isConnectedToBackend() const
    return self.uglySide.call('ritual_ZNK9QmlSensor20isConnectedToBackendEv')

  def isBusy(self) -> bool:
    """
    Calls Qt's 'bool QmlSensor::isBusy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#isBusy
    """
    #  bool QmlSensor::isBusy() const
    return self.uglySide.call('ritual_ZNK9QmlSensor6isBusyEv')

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QmlSensor::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#isActive
    """
    #  bool QmlSensor::isActive() const
    return self.uglySide.call('ritual_ZNK9QmlSensor8isActiveEv')

  def isAlwaysOn(self) -> bool:
    """
    Calls Qt's 'bool QmlSensor::isAlwaysOn() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#isAlwaysOn
    """
    #  bool QmlSensor::isAlwaysOn() const
    return self.uglySide.call('ritual_ZNK9QmlSensor10isAlwaysOnEv')

  def skipDuplicates(self) -> bool:
    """
    Calls Qt's 'bool QmlSensor::skipDuplicates() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#skipDuplicates
    """
    #  bool QmlSensor::skipDuplicates() const
    return self.uglySide.call('ritual_ZNK9QmlSensor14skipDuplicatesEv')

  def dataRate(self) -> int:
    """
    Calls Qt's 'int QmlSensor::dataRate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#dataRate
    """
    #  int QmlSensor::dataRate() const
    return self.uglySide.call('ritual_ZNK9QmlSensor8dataRateEv')

  def outputRange(self) -> int:
    """
    Calls Qt's 'int QmlSensor::outputRange() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#outputRange
    """
    #  int QmlSensor::outputRange() const
    return self.uglySide.call('ritual_ZNK9QmlSensor11outputRangeEv')

  def description(self) -> str:
    """
    Calls Qt's 'QString QmlSensor::description() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#description

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QmlSensor::description() const
    return self.uglySide.call('ritual_ZNK9QmlSensor11descriptionEv')

  def error(self) -> int:
    """
    Calls Qt's 'int QmlSensor::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#error
    """
    #  int QmlSensor::error() const
    return self.uglySide.call('ritual_ZNK9QmlSensor5errorEv')

  def reading(self) -> Optional[QmlSensorReading]:
    """
    Calls Qt's 'QmlSensorReading *QmlSensor::reading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#reading

    Returns
    -------

    Optional[QmlSensorReading]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QmlSensorReading *QmlSensor::reading() const
    address = self.uglySide.call('ritual_ZNK9QmlSensor7readingEv')
    from . import QmlSensorReading
    return QmlSensorReading._cuteAt(address)

  @overload(Feature)
  def isFeatureSupported(self, feature: Feature) -> bool:
    """
    Calls Qt's 'bool QmlSensor::isFeatureSupported(Feature feature) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#isFeatureSupported

    Parameters
    ----------

    feature : Feature
      Passed on as its number.
    """
    #  bool QmlSensor::isFeatureSupported(Feature feature) const
    return self.uglySide.call(
        'ritual_ZNK9QmlSensor18isFeatureSupportedENS_7FeatureE',
        feature.value,
    )

  def axesOrientationMode(self) -> AxesOrientationMode:
    """
    Calls Qt's 'AxesOrientationMode QmlSensor::axesOrientationMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#axesOrientationMode

    Returns
    -------

    AxesOrientationMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'AxesOrientationMode(number)' gives.
    """
    #  AxesOrientationMode QmlSensor::axesOrientationMode() const
    return QmlSensor.AxesOrientationMode(self.uglySide.call(
        'ritual_ZNK9QmlSensor19axesOrientationModeEv',
    ))

  def currentOrientation(self) -> int:
    """
    Calls Qt's 'int QmlSensor::currentOrientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#currentOrientation
    """
    #  int QmlSensor::currentOrientation() const
    return self.uglySide.call('ritual_ZNK9QmlSensor18currentOrientationEv')

  def userOrientation(self) -> int:
    """
    Calls Qt's 'int QmlSensor::userOrientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#userOrientation
    """
    #  int QmlSensor::userOrientation() const
    return self.uglySide.call('ritual_ZNK9QmlSensor15userOrientationEv')

  def maxBufferSize(self) -> int:
    """
    Calls Qt's 'int QmlSensor::maxBufferSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#maxBufferSize
    """
    #  int QmlSensor::maxBufferSize() const
    return self.uglySide.call('ritual_ZNK9QmlSensor13maxBufferSizeEv')

  def efficientBufferSize(self) -> int:
    """
    Calls Qt's 'int QmlSensor::efficientBufferSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#efficientBufferSize
    """
    #  int QmlSensor::efficientBufferSize() const
    return self.uglySide.call('ritual_ZNK9QmlSensor19efficientBufferSizeEv')

  def bufferSize(self) -> int:
    """
    Calls Qt's 'int QmlSensor::bufferSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#bufferSize
    """
    #  int QmlSensor::bufferSize() const
    return self.uglySide.call('ritual_ZNK9QmlSensor10bufferSizeEv')

  def sensor(self) -> Optional[QSensor]:
    """
    Calls Qt's 'QSensor *QmlSensor::sensor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#sensor

    Returns
    -------

    Optional[QSensor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSensor *QmlSensor::sensor() const
    address = self.uglySide.call('ritual_ZNK9QmlSensor6sensorEv')
    from ..QtSensors import QSensor
    return QSensor._cuteAt(address)

  def createReading(self) -> Optional[QmlSensorReading]:
    """
    Calls Qt's 'QmlSensorReading *QmlSensor::createReading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#createReading

    Returns
    -------

    Optional[QmlSensorReading]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QmlSensorReading *QmlSensor::createReading() const
    address = self.uglySide.call('ritual_ZNK9QmlSensor13createReadingEv')
    from . import QmlSensorReading
    return QmlSensorReading._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def setIdentifier(self, identifier: QByteArray) -> None:
    """
    Calls Qt's 'void QmlSensor::setIdentifier(const QByteArray &identifier)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#setIdentifier

    Parameters
    ----------

    identifier : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QmlSensor::setIdentifier(const QByteArray &identifier)
    self.uglySide.call(
        'ritual_ZN9QmlSensor13setIdentifierERK10QByteArray',
        self._valueOf(identifier),
    )

  @overload(bool)
  def setActive(self, active: bool) -> None:
    """
    Calls Qt's 'void QmlSensor::setActive(bool active)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#setActive

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QmlSensor::setActive(bool active)
    self.uglySide.call('ritual_ZN9QmlSensor9setActiveEb', active)

  @overload(bool)
  def setAlwaysOn(self, alwaysOn: bool) -> None:
    """
    Calls Qt's 'void QmlSensor::setAlwaysOn(bool alwaysOn)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#setAlwaysOn

    Parameters
    ----------

    alwaysOn : bool
      Passed on as it is.
    """
    #  void QmlSensor::setAlwaysOn(bool alwaysOn)
    self.uglySide.call('ritual_ZN9QmlSensor11setAlwaysOnEb', alwaysOn)

  @overload(bool)
  def setSkipDuplicates(self, skipDuplicates: bool) -> None:
    """
    Calls Qt's 'void QmlSensor::setSkipDuplicates(bool skipDuplicates)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#setSkipDuplicates

    Parameters
    ----------

    skipDuplicates : bool
      Passed on as it is.
    """
    #  void QmlSensor::setSkipDuplicates(bool skipDuplicates)
    self.uglySide.call(
        'ritual_ZN9QmlSensor17setSkipDuplicatesEb', skipDuplicates,
    )

  @overload(int)
  def setDataRate(self, rate: int) -> None:
    """
    Calls Qt's 'void QmlSensor::setDataRate(int rate)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#setDataRate

    Parameters
    ----------

    rate : int
      Passed on as it is.
    """
    #  void QmlSensor::setDataRate(int rate)
    self.uglySide.call('ritual_ZN9QmlSensor11setDataRateEi', rate)

  @overload(int)
  def setOutputRange(self, index: int) -> None:
    """
    Calls Qt's 'void QmlSensor::setOutputRange(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#setOutputRange

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QmlSensor::setOutputRange(int index)
    self.uglySide.call('ritual_ZN9QmlSensor14setOutputRangeEi', index)

  @overload(AxesOrientationMode)
  def setAxesOrientationMode(
      self,
      axesOrientationMode: AxesOrientationMode,
  ) -> None:
    """
    Calls Qt's 'void QmlSensor::setAxesOrientationMode(AxesOrientationMode
    axesOrientationMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlsensor.html#setAxesOrientationMode

    Parameters
    ----------

    axesOrientationMode : AxesOrientationMode
      Passed on as its number.
    """
    #  void QmlSensor::setAxesOrientationMode(AxesOrientationMode
    #      axesOrientationMode)
    self.uglySide.call(
        'ritual_ZN9QmlSensor22setAxesOrientationModeENS_19AxesOrientationMo'
        'deE',
        axesOrientationMode.value,
    )

  @overload(int)
  def setUserOrientation(self, userOrientation: int) -> None:
    """
    Calls Qt's 'void QmlSensor::setUserOrientation(int userOrientation)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#setUserOrientation

    Parameters
    ----------

    userOrientation : int
      Passed on as it is.
    """
    #  void QmlSensor::setUserOrientation(int userOrientation)
    self.uglySide.call(
        'ritual_ZN9QmlSensor18setUserOrientationEi', userOrientation,
    )

  @overload(int)
  def setBufferSize(self, bufferSize: int) -> None:
    """
    Calls Qt's 'void QmlSensor::setBufferSize(int bufferSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#setBufferSize

    Parameters
    ----------

    bufferSize : int
      Passed on as it is.
    """
    #  void QmlSensor::setBufferSize(int bufferSize)
    self.uglySide.call('ritual_ZN9QmlSensor13setBufferSizeEi', bufferSize)

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
    Notes what was given, for Qt's 'QmlSensor::QmlSensor(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#QmlSensor

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QmlSensor::QmlSensor(QObject *parent)
    self._noteCreation(QmlSensor, lambda: Rituals.call(
        'ritual_ZN9QmlSensorC1EP7QObject',
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

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QmlSensor::componentComplete()'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#componentComplete
    """
    #  void QmlSensor::componentComplete()
    ritual = 'ritual_ZN9QmlSensor17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QmlSensor17componentCompleteEv'
    self.uglySide.call(ritual)

  def start(self) -> bool:
    """
    Calls Qt's 'bool QmlSensor::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#start
    """
    #  bool QmlSensor::start()
    return self.uglySide.call('ritual_ZN9QmlSensor5startEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QmlSensor::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#stop
    """
    #  void QmlSensor::stop()
    self.uglySide.call('ritual_ZN9QmlSensor4stopEv')

  def identifierChanged(self) -> None:
    """
    Calls Qt's 'void QmlSensor::identifierChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#identifierChanged
    """
    #  void QmlSensor::identifierChanged()
    self.uglySide.call('ritual_ZN9QmlSensor17identifierChangedEv')

  def connectedToBackendChanged(self) -> None:
    """
    Calls Qt's 'void QmlSensor::connectedToBackendChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlsensor.html#connectedToBackendChanged
    """
    #  void QmlSensor::connectedToBackendChanged()
    self.uglySide.call('ritual_ZN9QmlSensor25connectedToBackendChangedEv')

  def availableDataRatesChanged(self) -> None:
    """
    Calls Qt's 'void QmlSensor::availableDataRatesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlsensor.html#availableDataRatesChanged
    """
    #  void QmlSensor::availableDataRatesChanged()
    self.uglySide.call('ritual_ZN9QmlSensor25availableDataRatesChangedEv')

  def dataRateChanged(self) -> None:
    """
    Calls Qt's 'void QmlSensor::dataRateChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#dataRateChanged
    """
    #  void QmlSensor::dataRateChanged()
    self.uglySide.call('ritual_ZN9QmlSensor15dataRateChangedEv')

  def readingChanged(self) -> None:
    """
    Calls Qt's 'void QmlSensor::readingChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#readingChanged
    """
    #  void QmlSensor::readingChanged()
    self.uglySide.call('ritual_ZN9QmlSensor14readingChangedEv')

  def activeChanged(self) -> None:
    """
    Calls Qt's 'void QmlSensor::activeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#activeChanged
    """
    #  void QmlSensor::activeChanged()
    self.uglySide.call('ritual_ZN9QmlSensor13activeChangedEv')

  def outputRangesChanged(self) -> None:
    """
    Calls Qt's 'void QmlSensor::outputRangesChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#outputRangesChanged
    """
    #  void QmlSensor::outputRangesChanged()
    self.uglySide.call('ritual_ZN9QmlSensor19outputRangesChangedEv')

  def outputRangeChanged(self) -> None:
    """
    Calls Qt's 'void QmlSensor::outputRangeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#outputRangeChanged
    """
    #  void QmlSensor::outputRangeChanged()
    self.uglySide.call('ritual_ZN9QmlSensor18outputRangeChangedEv')

  def descriptionChanged(self) -> None:
    """
    Calls Qt's 'void QmlSensor::descriptionChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#descriptionChanged
    """
    #  void QmlSensor::descriptionChanged()
    self.uglySide.call('ritual_ZN9QmlSensor18descriptionChangedEv')

  def errorChanged(self) -> None:
    """
    Calls Qt's 'void QmlSensor::errorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#errorChanged
    """
    #  void QmlSensor::errorChanged()
    self.uglySide.call('ritual_ZN9QmlSensor12errorChangedEv')

  def alwaysOnChanged(self) -> None:
    """
    Calls Qt's 'void QmlSensor::alwaysOnChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#alwaysOnChanged
    """
    #  void QmlSensor::alwaysOnChanged()
    self.uglySide.call('ritual_ZN9QmlSensor15alwaysOnChangedEv')

  def busyChanged(self) -> None:
    """
    Calls Qt's 'void QmlSensor::busyChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#busyChanged
    """
    #  void QmlSensor::busyChanged()
    self.uglySide.call('ritual_ZN9QmlSensor11busyChangedEv')

  @overload(bool)
  def skipDuplicatesChanged(self, skipDuplicates: bool) -> None:
    """
    Calls Qt's 'void QmlSensor::skipDuplicatesChanged(bool skipDuplicates)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlsensor.html#skipDuplicatesChanged

    Parameters
    ----------

    skipDuplicates : bool
      Passed on as it is.
    """
    #  void QmlSensor::skipDuplicatesChanged(bool skipDuplicates)
    self.uglySide.call(
        'ritual_ZN9QmlSensor21skipDuplicatesChangedEb', skipDuplicates,
    )

  @overload(AxesOrientationMode)
  def axesOrientationModeChanged(
      self,
      axesOrientationMode: AxesOrientationMode,
  ) -> None:
    """
    Calls Qt's 'void
    QmlSensor::axesOrientationModeChanged(AxesOrientationMode
    axesOrientationMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlsensor.html#axesOrientationModeChanged

    Parameters
    ----------

    axesOrientationMode : AxesOrientationMode
      Passed on as its number.
    """
    #  void QmlSensor::axesOrientationModeChanged(AxesOrientationMode
    #      axesOrientationMode)
    self.uglySide.call(
        'ritual_ZN9QmlSensor26axesOrientationModeChangedENS_19AxesOrientati'
        'onModeE',
        axesOrientationMode.value,
    )

  @overload(int)
  def currentOrientationChanged(self, currentOrientation: int) -> None:
    """
    Calls Qt's 'void QmlSensor::currentOrientationChanged(int
    currentOrientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlsensor.html#currentOrientationChanged

    Parameters
    ----------

    currentOrientation : int
      Passed on as it is.
    """
    #  void QmlSensor::currentOrientationChanged(int currentOrientation)
    self.uglySide.call(
        'ritual_ZN9QmlSensor25currentOrientationChangedEi',
        currentOrientation,
    )

  @overload(int)
  def userOrientationChanged(self, userOrientation: int) -> None:
    """
    Calls Qt's 'void QmlSensor::userOrientationChanged(int userOrientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlsensor.html#userOrientationChanged

    Parameters
    ----------

    userOrientation : int
      Passed on as it is.
    """
    #  void QmlSensor::userOrientationChanged(int userOrientation)
    self.uglySide.call(
        'ritual_ZN9QmlSensor22userOrientationChangedEi', userOrientation,
    )

  @overload(int)
  def maxBufferSizeChanged(self, maxBufferSize: int) -> None:
    """
    Calls Qt's 'void QmlSensor::maxBufferSizeChanged(int maxBufferSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlsensor.html#maxBufferSizeChanged

    Parameters
    ----------

    maxBufferSize : int
      Passed on as it is.
    """
    #  void QmlSensor::maxBufferSizeChanged(int maxBufferSize)
    self.uglySide.call(
        'ritual_ZN9QmlSensor20maxBufferSizeChangedEi', maxBufferSize,
    )

  @overload(int)
  def efficientBufferSizeChanged(self, efficientBufferSize: int) -> None:
    """
    Calls Qt's 'void QmlSensor::efficientBufferSizeChanged(int
    efficientBufferSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlsensor.html#efficientBufferSizeChanged

    Parameters
    ----------

    efficientBufferSize : int
      Passed on as it is.
    """
    #  void QmlSensor::efficientBufferSizeChanged(int efficientBufferSize)
    self.uglySide.call(
        'ritual_ZN9QmlSensor26efficientBufferSizeChangedEi',
        efficientBufferSize,
    )

  @overload(int)
  def bufferSizeChanged(self, bufferSize: int) -> None:
    """
    Calls Qt's 'void QmlSensor::bufferSizeChanged(int bufferSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#bufferSizeChanged

    Parameters
    ----------

    bufferSize : int
      Passed on as it is.
    """
    #  void QmlSensor::bufferSizeChanged(int bufferSize)
    self.uglySide.call(
        'ritual_ZN9QmlSensor17bufferSizeChangedEi', bufferSize,
    )

  def updateReading(self) -> None:
    """
    Calls Qt's 'void QmlSensor::updateReading()'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#updateReading
    """
    #  void QmlSensor::updateReading()
    self.uglySide.call('ritual_ZN9QmlSensor13updateReadingEv')

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QmlSensor::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qmlsensor.html#classBegin
    """
    #  void QmlSensor::classBegin()
    ritual = 'ritual_ZN9QmlSensor10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QmlSensor10classBeginEv'
    self.uglySide.call(ritual)

  @staticmethod
  def availableDataRates(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QmlSensorRange> QmlSensor::availableDataRates()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QmlSensor.availableDataRates' has no cute function yet. Qt's "
        "'QQmlListProperty<QmlSensorRange> QmlSensor::availableDataRates() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def bindableReading(*__, **_) -> Never:
    """
    Qt's 'QBindable<QmlSensorReading *> QmlSensor::bindableReading() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QmlSensor.bindableReading' has no cute function yet. Qt's "
        "'QBindable<QmlSensorReading *> QmlSensor::bindableReading() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def outputRanges(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QmlSensorOutputRange> QmlSensor::outputRanges()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QmlSensor.outputRanges' has no cute function yet. Qt's "
        "'QQmlListProperty<QmlSensorOutputRange> QmlSensor::outputRanges() "
        "const': gives a type Python has no way to take yet.")
