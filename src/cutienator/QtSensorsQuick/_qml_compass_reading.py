"""
QmlCompassReading binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlcompass_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QmlCompassReading to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QmlSensorReading

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtSensors import QCompass, QSensorReading
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCompass = WAIT['QCompass']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QmlCompassReading(QmlSensorReading):
  """
  The cute side of Qt's QmlCompassReading: a plain Python object standing in
  front of one C++ QmlCompassReading.

  It is built on the cute 'QmlSensorReading', as Qt's QmlCompassReading is
  built on Qt's QmlSensorReading, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QmlCompassReading that has a ritual and that Python
  can call so far, 10 names in all: 'metaObject', 'tr', 'azimuth',
  'calibrationLevel', 'azimuthChanged', 'calibrationLevelChanged', 'reading',
  'readingUpdate', '_qt_property_m_azimuth_offset',
  '_qt_property_m_calibrationLevel_offset'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QmlCompassReading::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QmlCompassReading::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QmlCompassReading::qt_qmlMarker_uncreatable()': one of Qt's
    own inner workings.
  - Qt's 'QmlCompassReading::~QmlCompassReading()': the destructor: Python
    never removes a C++ QmlCompassReading.
  - Qt's 'QBindable<qreal> QmlCompassReading::bindableAzimuth() const': gives
    a type Python has no way to take yet.
  - Qt's 'QBindable<qreal> QmlCompassReading::bindableCalibrationLevel()
    const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QmlCompassReading is created at the first use, not by
    'QmlCompassReading(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QmlCompassReading.
  - Qt tells when it has removed the C++ QmlCompassReading. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QmlCompassReading that has no cute function yet,
    'bindableAzimuth', 'bindableCalibrationLevel', holds a function that
    raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QmlCompassReading::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlcompassreading.html#tr

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
    #  QString QmlCompassReading::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QmlCompassReading2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def _qt_property_m_azimuth_offset() -> int:
    """
    Calls Qt's 'size_t QmlCompassReading::_qt_property_m_azimuth_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlcompassreading.html
    """
    #  size_t QmlCompassReading::_qt_property_m_azimuth_offset()
    return Rituals.call(
        'ritual_ZN17QmlCompassReading29_qt_property_m_azimuth_offsetEv',
    )

  @staticmethod
  def _qt_property_m_calibrationLevel_offset() -> int:
    """
    Calls Qt's 'size_t
    QmlCompassReading::_qt_property_m_calibrationLevel_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlcompassreading.html
    """
    #  size_t QmlCompassReading::_qt_property_m_calibrationLevel_offset()
    return Rituals.call(
        'ritual_ZN17QmlCompassReading38_qt_property_m_calibrationLevel_offs'
        'etEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QmlCompassReading'

  #  A C++ QmlCompassReading Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QmlCompassReading'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QmlCompassReading::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlcompassreading.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QmlCompassReading::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QmlCompassReading10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def azimuth(self) -> float:
    """
    Calls Qt's 'qreal QmlCompassReading::azimuth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlcompassreading.html#azimuth
    """
    #  qreal QmlCompassReading::azimuth() const
    return self.uglySide.call('ritual_ZNK17QmlCompassReading7azimuthEv')

  def calibrationLevel(self) -> float:
    """
    Calls Qt's 'qreal QmlCompassReading::calibrationLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlcompassreading.html#calibrationLevel
    """
    #  qreal QmlCompassReading::calibrationLevel() const
    return self.uglySide.call(
        'ritual_ZNK17QmlCompassReading16calibrationLevelEv',
    )

  def reading(self) -> Optional[QSensorReading]:
    """
    Calls Qt's 'QSensorReading *QmlCompassReading::reading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlcompassreading.html#reading

    Returns
    -------

    Optional[QSensorReading]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSensorReading *QmlCompassReading::reading() const
    ritual = 'ritual_ZNK17QmlCompassReading7readingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QmlCompassReading7readingEv'
    address = self.uglySide.call(ritual)
    from ..QtSensors import QSensorReading
    return QSensorReading._cuteAt(address)

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

  @overload(QCompass)
  @overload(NoneType)
  def __init__(self, sensor: Optional[QCompass]) -> None:
    """
    Notes what was given, for Qt's
    'QmlCompassReading::QmlCompassReading(QCompass *sensor)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlcompassreading.html#QmlCompassReading

    Parameters
    ----------

    sensor : Optional[QCompass]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QmlCompassReading::QmlCompassReading(QCompass *sensor)
    self._noteCreation(QmlCompassReading, lambda: Rituals.call(
        'ritual_ZN17QmlCompassReadingC1EP8QCompass', self._addressOf(sensor),
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

  def azimuthChanged(self) -> None:
    """
    Calls Qt's 'void QmlCompassReading::azimuthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlcompassreading.html#azimuthChanged
    """
    #  void QmlCompassReading::azimuthChanged()
    self.uglySide.call('ritual_ZN17QmlCompassReading14azimuthChangedEv')

  def calibrationLevelChanged(self) -> None:
    """
    Calls Qt's 'void QmlCompassReading::calibrationLevelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlcompassreading.html#calibrationLevelChanged
    """
    #  void QmlCompassReading::calibrationLevelChanged()
    self.uglySide.call(
        'ritual_ZN17QmlCompassReading23calibrationLevelChangedEv',
    )

  def readingUpdate(self) -> None:
    """
    Calls Qt's 'void QmlCompassReading::readingUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlcompassreading.html#readingUpdate
    """
    #  void QmlCompassReading::readingUpdate()
    ritual = 'ritual_ZN17QmlCompassReading13readingUpdateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QmlCompassReading13readingUpdateEv'
    self.uglySide.call(ritual)

  @staticmethod
  def bindableAzimuth(*__, **_) -> Never:
    """
    Qt's 'QBindable<qreal> QmlCompassReading::bindableAzimuth() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QmlCompassReading.bindableAzimuth' has no cute function yet. Qt's "
        "'QBindable<qreal> QmlCompassReading::bindableAzimuth() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def bindableCalibrationLevel(*__, **_) -> Never:
    """
    Qt's 'QBindable<qreal> QmlCompassReading::bindableCalibrationLevel()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QmlCompassReading.bindableCalibrationLevel' has no cute function "
        "yet. Qt's 'QBindable<qreal> "
        "QmlCompassReading::bindableCalibrationLevel() const': gives a type "
        "Python has no way to take yet.")
