"""
QmlGyroscopeReading binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlgyroscope_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QmlGyroscopeReading to be private: it declares the class in a
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
  from ..QtSensors import QGyroscope, QSensorReading
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGyroscope = WAIT['QGyroscope']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QmlGyroscopeReading(QmlSensorReading):
  """
  The cute side of Qt's QmlGyroscopeReading: a plain Python object standing
  in front of one C++ QmlGyroscopeReading.

  It is built on the cute 'QmlSensorReading', as Qt's QmlGyroscopeReading is
  built on Qt's QmlSensorReading, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QmlGyroscopeReading that has a ritual and that
  Python can call so far, 13 names in all: 'metaObject', 'tr', 'x', 'y', 'z',
  'xChanged', 'yChanged', 'zChanged', 'reading', 'readingUpdate',
  '_qt_property_m_x_offset', '_qt_property_m_y_offset',
  '_qt_property_m_z_offset'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QmlGyroscopeReading::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QmlGyroscopeReading::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QmlGyroscopeReading::qt_qmlMarker_uncreatable()': one of Qt's
    own inner workings.
  - Qt's 'QmlGyroscopeReading::~QmlGyroscopeReading()': the destructor:
    Python never removes a C++ QmlGyroscopeReading.
  - Qt's 'QBindable<qreal> QmlGyroscopeReading::bindableX() const': gives a
    type Python has no way to take yet.
  - Qt's 'QBindable<qreal> QmlGyroscopeReading::bindableY() const': gives a
    type Python has no way to take yet.
  - Qt's 'QBindable<qreal> QmlGyroscopeReading::bindableZ() const': gives a
    type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QmlGyroscopeReading is created at the first use, not by
    'QmlGyroscopeReading(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QmlGyroscopeReading.
  - Qt tells when it has removed the C++ QmlGyroscopeReading. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QmlGyroscopeReading that has no cute function yet,
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
    Calls Qt's 'QString QmlGyroscopeReading::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmlgyroscopereading.html#tr

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
    #  QString QmlGyroscopeReading::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QmlGyroscopeReading2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def _qt_property_m_x_offset() -> int:
    """
    Calls Qt's 'size_t QmlGyroscopeReading::_qt_property_m_x_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlgyroscopereading.html#_qt_property_m_x_offset
    """
    #  size_t QmlGyroscopeReading::_qt_property_m_x_offset()
    return Rituals.call(
        'ritual_ZN19QmlGyroscopeReading23_qt_property_m_x_offsetEv',
    )

  @staticmethod
  def _qt_property_m_y_offset() -> int:
    """
    Calls Qt's 'size_t QmlGyroscopeReading::_qt_property_m_y_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlgyroscopereading.html#_qt_property_m_y_offset
    """
    #  size_t QmlGyroscopeReading::_qt_property_m_y_offset()
    return Rituals.call(
        'ritual_ZN19QmlGyroscopeReading23_qt_property_m_y_offsetEv',
    )

  @staticmethod
  def _qt_property_m_z_offset() -> int:
    """
    Calls Qt's 'size_t QmlGyroscopeReading::_qt_property_m_z_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlgyroscopereading.html#_qt_property_m_z_offset
    """
    #  size_t QmlGyroscopeReading::_qt_property_m_z_offset()
    return Rituals.call(
        'ritual_ZN19QmlGyroscopeReading23_qt_property_m_z_offsetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QmlGyroscopeReading'

  #  A C++ QmlGyroscopeReading Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QmlGyroscopeReading'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QmlGyroscopeReading::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlgyroscopereading.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QmlGyroscopeReading::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QmlGyroscopeReading10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def x(self) -> float:
    """
    Calls Qt's 'qreal QmlGyroscopeReading::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlgyroscopereading.html#x
    """
    #  qreal QmlGyroscopeReading::x() const
    return self.uglySide.call('ritual_ZNK19QmlGyroscopeReading1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'qreal QmlGyroscopeReading::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlgyroscopereading.html#y
    """
    #  qreal QmlGyroscopeReading::y() const
    return self.uglySide.call('ritual_ZNK19QmlGyroscopeReading1yEv')

  def z(self) -> float:
    """
    Calls Qt's 'qreal QmlGyroscopeReading::z() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlgyroscopereading.html#z
    """
    #  qreal QmlGyroscopeReading::z() const
    return self.uglySide.call('ritual_ZNK19QmlGyroscopeReading1zEv')

  def reading(self) -> Optional[QSensorReading]:
    """
    Calls Qt's 'QSensorReading *QmlGyroscopeReading::reading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlgyroscopereading.html#reading

    Returns
    -------

    Optional[QSensorReading]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSensorReading *QmlGyroscopeReading::reading() const
    ritual = 'ritual_ZNK19QmlGyroscopeReading7readingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QmlGyroscopeReading7readingEv'
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

  @overload(QGyroscope)
  @overload(NoneType)
  def __init__(self, sensor: Optional[QGyroscope]) -> None:
    """
    Notes what was given, for Qt's
    'QmlGyroscopeReading::QmlGyroscopeReading(QGyroscope *sensor)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlgyroscopereading.html#QmlGyroscopeReading

    Parameters
    ----------

    sensor : Optional[QGyroscope]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QmlGyroscopeReading::QmlGyroscopeReading(QGyroscope *sensor)
    self._noteCreation(QmlGyroscopeReading, lambda: Rituals.call(
        'ritual_ZN19QmlGyroscopeReadingC1EP10QGyroscope',
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
    Calls Qt's 'void QmlGyroscopeReading::xChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qmlgyroscopereading.html#xChanged
    """
    #  void QmlGyroscopeReading::xChanged()
    self.uglySide.call('ritual_ZN19QmlGyroscopeReading8xChangedEv')

  def yChanged(self) -> None:
    """
    Calls Qt's 'void QmlGyroscopeReading::yChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qmlgyroscopereading.html#yChanged
    """
    #  void QmlGyroscopeReading::yChanged()
    self.uglySide.call('ritual_ZN19QmlGyroscopeReading8yChangedEv')

  def zChanged(self) -> None:
    """
    Calls Qt's 'void QmlGyroscopeReading::zChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qmlgyroscopereading.html#zChanged
    """
    #  void QmlGyroscopeReading::zChanged()
    self.uglySide.call('ritual_ZN19QmlGyroscopeReading8zChangedEv')

  def readingUpdate(self) -> None:
    """
    Calls Qt's 'void QmlGyroscopeReading::readingUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlgyroscopereading.html#readingUpdate
    """
    #  void QmlGyroscopeReading::readingUpdate()
    ritual = 'ritual_ZN19QmlGyroscopeReading13readingUpdateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QmlGyroscopeReading13readingUpdateEv'
    self.uglySide.call(ritual)

  @staticmethod
  def bindableX(*__, **_) -> Never:
    """
    Qt's 'QBindable<qreal> QmlGyroscopeReading::bindableX() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QmlGyroscopeReading.bindableX' has no cute function yet. Qt's "
        "'QBindable<qreal> QmlGyroscopeReading::bindableX() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def bindableY(*__, **_) -> Never:
    """
    Qt's 'QBindable<qreal> QmlGyroscopeReading::bindableY() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QmlGyroscopeReading.bindableY' has no cute function yet. Qt's "
        "'QBindable<qreal> QmlGyroscopeReading::bindableY() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def bindableZ(*__, **_) -> Never:
    """
    Qt's 'QBindable<qreal> QmlGyroscopeReading::bindableZ() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QmlGyroscopeReading.bindableZ' has no cute function yet. Qt's "
        "'QBindable<qreal> QmlGyroscopeReading::bindableZ() const': gives a "
        "type Python has no way to take yet.")
