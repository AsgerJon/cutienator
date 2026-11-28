"""
QmlAccelerometerReading binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlaccelerometer_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QmlAccelerometerReading to be private: it declares the class in a
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
  from ..QtSensors import QAccelerometer, QSensorReading
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAccelerometer = WAIT['QAccelerometer']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QmlAccelerometerReading(QmlSensorReading):
  """
  The cute side of Qt's QmlAccelerometerReading: a plain Python object
  standing in front of one C++ QmlAccelerometerReading.

  It is built on the cute 'QmlSensorReading', as Qt's QmlAccelerometerReading
  is built on Qt's QmlSensorReading, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QmlAccelerometerReading that has a ritual and that
  Python can call so far, 13 names in all: 'metaObject', 'tr', 'x', 'y', 'z',
  'xChanged', 'yChanged', 'zChanged', 'reading', 'readingUpdate',
  '_qt_property_m_x_offset', '_qt_property_m_y_offset',
  '_qt_property_m_z_offset'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QmlAccelerometerReading::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QmlAccelerometerReading::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QmlAccelerometerReading::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.
  - Qt's 'QmlAccelerometerReading::~QmlAccelerometerReading()': the
    destructor: Python never removes a C++ QmlAccelerometerReading.
  - Qt's 'QBindable<qreal> QmlAccelerometerReading::bindableX() const': gives
    a type Python has no way to take yet.
  - Qt's 'QBindable<qreal> QmlAccelerometerReading::bindableY() const': gives
    a type Python has no way to take yet.
  - Qt's 'QBindable<qreal> QmlAccelerometerReading::bindableZ() const': gives
    a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QmlAccelerometerReading is created at the first use, not by
    'QmlAccelerometerReading(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QmlAccelerometerReading.
  - Qt tells when it has removed the C++ QmlAccelerometerReading. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QmlAccelerometerReading that has no cute function yet,
    'bindableX', 'bindableY', 'bindableZ', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QmlAccelerometerReading::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlaccelerometerreading.html#tr

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
    #  QString QmlAccelerometerReading::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QmlAccelerometerReading2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def _qt_property_m_x_offset() -> int:
    """
    Calls Qt's 'size_t QmlAccelerometerReading::_qt_property_m_x_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlaccelerometerreading.html
    """
    #  size_t QmlAccelerometerReading::_qt_property_m_x_offset()
    return Rituals.call(
        'ritual_ZN23QmlAccelerometerReading23_qt_property_m_x_offsetEv',
    )

  @staticmethod
  def _qt_property_m_y_offset() -> int:
    """
    Calls Qt's 'size_t QmlAccelerometerReading::_qt_property_m_y_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlaccelerometerreading.html
    """
    #  size_t QmlAccelerometerReading::_qt_property_m_y_offset()
    return Rituals.call(
        'ritual_ZN23QmlAccelerometerReading23_qt_property_m_y_offsetEv',
    )

  @staticmethod
  def _qt_property_m_z_offset() -> int:
    """
    Calls Qt's 'size_t QmlAccelerometerReading::_qt_property_m_z_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlaccelerometerreading.html
    """
    #  size_t QmlAccelerometerReading::_qt_property_m_z_offset()
    return Rituals.call(
        'ritual_ZN23QmlAccelerometerReading23_qt_property_m_z_offsetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QmlAccelerometerReading'

  #  A C++ QmlAccelerometerReading Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QmlAccelerometerReading'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QmlAccelerometerReading::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlaccelerometerreading.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QmlAccelerometerReading::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QmlAccelerometerReading10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def x(self) -> float:
    """
    Calls Qt's 'qreal QmlAccelerometerReading::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlaccelerometerreading.html#x
    """
    #  qreal QmlAccelerometerReading::x() const
    return self.uglySide.call('ritual_ZNK23QmlAccelerometerReading1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'qreal QmlAccelerometerReading::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlaccelerometerreading.html#y
    """
    #  qreal QmlAccelerometerReading::y() const
    return self.uglySide.call('ritual_ZNK23QmlAccelerometerReading1yEv')

  def z(self) -> float:
    """
    Calls Qt's 'qreal QmlAccelerometerReading::z() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlaccelerometerreading.html#z
    """
    #  qreal QmlAccelerometerReading::z() const
    return self.uglySide.call('ritual_ZNK23QmlAccelerometerReading1zEv')

  def reading(self) -> Optional[QSensorReading]:
    """
    Calls Qt's 'QSensorReading *QmlAccelerometerReading::reading() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlaccelerometerreading.html#reading

    Returns
    -------

    Optional[QSensorReading]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSensorReading *QmlAccelerometerReading::reading() const
    ritual = 'ritual_ZNK23QmlAccelerometerReading7readingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK23QmlAccelerometerReading7readingEv'
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

  @overload(QAccelerometer)
  @overload(NoneType)
  def __init__(self, sensor: Optional[QAccelerometer]) -> None:
    """
    Notes what was given, for Qt's
    'QmlAccelerometerReading::QmlAccelerometerReading(QAccelerometer
    *sensor)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlaccelerometerreading.html

    Parameters
    ----------

    sensor : Optional[QAccelerometer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QmlAccelerometerReading::QmlAccelerometerReading(QAccelerometer
    #      *sensor)
    self._noteCreation(QmlAccelerometerReading, lambda: Rituals.call(
        'ritual_ZN23QmlAccelerometerReadingC1EP14QAccelerometer',
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

  def xChanged(self) -> None:
    """
    Calls Qt's 'void QmlAccelerometerReading::xChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlaccelerometerreading.html#xChanged
    """
    #  void QmlAccelerometerReading::xChanged()
    self.uglySide.call('ritual_ZN23QmlAccelerometerReading8xChangedEv')

  def yChanged(self) -> None:
    """
    Calls Qt's 'void QmlAccelerometerReading::yChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlaccelerometerreading.html#yChanged
    """
    #  void QmlAccelerometerReading::yChanged()
    self.uglySide.call('ritual_ZN23QmlAccelerometerReading8yChangedEv')

  def zChanged(self) -> None:
    """
    Calls Qt's 'void QmlAccelerometerReading::zChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlaccelerometerreading.html#zChanged
    """
    #  void QmlAccelerometerReading::zChanged()
    self.uglySide.call('ritual_ZN23QmlAccelerometerReading8zChangedEv')

  def readingUpdate(self) -> None:
    """
    Calls Qt's 'void QmlAccelerometerReading::readingUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlaccelerometerreading.html#readingUpdate
    """
    #  void QmlAccelerometerReading::readingUpdate()
    ritual = 'ritual_ZN23QmlAccelerometerReading13readingUpdateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QmlAccelerometerReading13readingUpdateEv'
    self.uglySide.call(ritual)

  @staticmethod
  def bindableX(*__, **_) -> Never:
    """
    Qt's 'QBindable<qreal> QmlAccelerometerReading::bindableX() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QmlAccelerometerReading.bindableX' has no cute function yet. Qt's "
        "'QBindable<qreal> QmlAccelerometerReading::bindableX() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def bindableY(*__, **_) -> Never:
    """
    Qt's 'QBindable<qreal> QmlAccelerometerReading::bindableY() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QmlAccelerometerReading.bindableY' has no cute function yet. Qt's "
        "'QBindable<qreal> QmlAccelerometerReading::bindableY() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def bindableZ(*__, **_) -> Never:
    """
    Qt's 'QBindable<qreal> QmlAccelerometerReading::bindableZ() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QmlAccelerometerReading.bindableZ' has no cute function yet. Qt's "
        "'QBindable<qreal> QmlAccelerometerReading::bindableZ() const': "
        "gives a type Python has no way to take yet.")
