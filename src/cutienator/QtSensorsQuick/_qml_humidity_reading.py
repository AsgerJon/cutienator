"""
QmlHumidityReading binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlhumiditysensor_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QmlHumidityReading to be private: it declares the class in a
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
  from ..QtSensors import QHumiditySensor, QSensorReading
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHumiditySensor = WAIT['QHumiditySensor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QmlHumidityReading(QmlSensorReading):
  """
  The cute side of Qt's QmlHumidityReading: a plain Python object standing in
  front of one C++ QmlHumidityReading.

  It is built on the cute 'QmlSensorReading', as Qt's QmlHumidityReading is
  built on Qt's QmlSensorReading, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QmlHumidityReading that has a ritual and that Python
  can call so far, 10 names in all: 'metaObject', 'tr', 'relativeHumidity',
  'absoluteHumidity', 'relativeHumidityChanged', 'absoluteHumidityChanged',
  'reading', 'readingUpdate', '_qt_property_m_relativeHumidity_offset',
  '_qt_property_m_absoluteHumidity_offset'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QmlHumidityReading::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QmlHumidityReading::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QmlHumidityReading::qt_qmlMarker_uncreatable()': one of Qt's
    own inner workings.
  - Qt's 'QmlHumidityReading::~QmlHumidityReading()': the destructor: Python
    never removes a C++ QmlHumidityReading.
  - Qt's 'QBindable<qreal> QmlHumidityReading::bindableRelativeHumidity()
    const': gives a type Python has no way to take yet.
  - Qt's 'QBindable<qreal> QmlHumidityReading::bindableAbsoluteHumidity()
    const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QmlHumidityReading is created at the first use, not by
    'QmlHumidityReading(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QmlHumidityReading.
  - Qt tells when it has removed the C++ QmlHumidityReading. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QmlHumidityReading that has no cute function yet,
    'bindableAbsoluteHumidity', 'bindableRelativeHumidity', holds a function
    that raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QmlHumidityReading::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlhumidityreading.html#tr

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
    #  QString QmlHumidityReading::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QmlHumidityReading2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def _qt_property_m_relativeHumidity_offset() -> int:
    """
    Calls Qt's 'size_t
    QmlHumidityReading::_qt_property_m_relativeHumidity_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlhumidityreading.html
    """
    #  size_t QmlHumidityReading::_qt_property_m_relativeHumidity_offset()
    return Rituals.call(
        'ritual_ZN18QmlHumidityReading38_qt_property_m_relativeHumidity_off'
        'setEv',
    )

  @staticmethod
  def _qt_property_m_absoluteHumidity_offset() -> int:
    """
    Calls Qt's 'size_t
    QmlHumidityReading::_qt_property_m_absoluteHumidity_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlhumidityreading.html
    """
    #  size_t QmlHumidityReading::_qt_property_m_absoluteHumidity_offset()
    return Rituals.call(
        'ritual_ZN18QmlHumidityReading38_qt_property_m_absoluteHumidity_off'
        'setEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QmlHumidityReading'

  #  A C++ QmlHumidityReading Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QmlHumidityReading'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QmlHumidityReading::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlhumidityreading.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QmlHumidityReading::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QmlHumidityReading10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def relativeHumidity(self) -> float:
    """
    Calls Qt's 'qreal QmlHumidityReading::relativeHumidity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlhumidityreading.html#relativeHumidity
    """
    #  qreal QmlHumidityReading::relativeHumidity() const
    return self.uglySide.call(
        'ritual_ZNK18QmlHumidityReading16relativeHumidityEv',
    )

  def absoluteHumidity(self) -> float:
    """
    Calls Qt's 'qreal QmlHumidityReading::absoluteHumidity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlhumidityreading.html#absoluteHumidity
    """
    #  qreal QmlHumidityReading::absoluteHumidity() const
    return self.uglySide.call(
        'ritual_ZNK18QmlHumidityReading16absoluteHumidityEv',
    )

  def reading(self) -> Optional[QSensorReading]:
    """
    Calls Qt's 'QSensorReading *QmlHumidityReading::reading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlhumidityreading.html#reading

    Returns
    -------

    Optional[QSensorReading]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSensorReading *QmlHumidityReading::reading() const
    ritual = 'ritual_ZNK18QmlHumidityReading7readingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QmlHumidityReading7readingEv'
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

  @overload(QHumiditySensor)
  @overload(NoneType)
  def __init__(self, sensor: Optional[QHumiditySensor]) -> None:
    """
    Notes what was given, for Qt's
    'QmlHumidityReading::QmlHumidityReading(QHumiditySensor *sensor)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlhumidityreading.html#QmlHumidityReading

    Parameters
    ----------

    sensor : Optional[QHumiditySensor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QmlHumidityReading::QmlHumidityReading(QHumiditySensor *sensor)
    self._noteCreation(QmlHumidityReading, lambda: Rituals.call(
        'ritual_ZN18QmlHumidityReadingC1EP15QHumiditySensor',
        self._addressOf(sensor),
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

  def relativeHumidityChanged(self) -> None:
    """
    Calls Qt's 'void QmlHumidityReading::relativeHumidityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlhumidityreading.html#relativeHumidityChanged
    """
    #  void QmlHumidityReading::relativeHumidityChanged()
    self.uglySide.call(
        'ritual_ZN18QmlHumidityReading23relativeHumidityChangedEv',
    )

  def absoluteHumidityChanged(self) -> None:
    """
    Calls Qt's 'void QmlHumidityReading::absoluteHumidityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlhumidityreading.html#absoluteHumidityChanged
    """
    #  void QmlHumidityReading::absoluteHumidityChanged()
    self.uglySide.call(
        'ritual_ZN18QmlHumidityReading23absoluteHumidityChangedEv',
    )

  def readingUpdate(self) -> None:
    """
    Calls Qt's 'void QmlHumidityReading::readingUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlhumidityreading.html#readingUpdate
    """
    #  void QmlHumidityReading::readingUpdate()
    ritual = 'ritual_ZN18QmlHumidityReading13readingUpdateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QmlHumidityReading13readingUpdateEv'
    self.uglySide.call(ritual)

  @staticmethod
  def bindableAbsoluteHumidity(*__, **_) -> Never:
    """
    Qt's 'QBindable<qreal> QmlHumidityReading::bindableAbsoluteHumidity()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QmlHumidityReading.bindableAbsoluteHumidity' has no cute function "
        "yet. Qt's 'QBindable<qreal> "
        "QmlHumidityReading::bindableAbsoluteHumidity() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def bindableRelativeHumidity(*__, **_) -> Never:
    """
    Qt's 'QBindable<qreal> QmlHumidityReading::bindableRelativeHumidity()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QmlHumidityReading.bindableRelativeHumidity' has no cute function "
        "yet. Qt's 'QBindable<qreal> "
        "QmlHumidityReading::bindableRelativeHumidity() const': gives a "
        "type Python has no way to take yet.")
