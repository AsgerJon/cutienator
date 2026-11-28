"""
QmlLidReading binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmllidsensor_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QmlLidReading to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QmlSensorReading

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtSensors import QLidSensor, QSensorReading
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLidSensor = WAIT['QLidSensor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QmlLidReading(QmlSensorReading):
  """
  The cute side of Qt's QmlLidReading: a plain Python object standing in
  front of one C++ QmlLidReading.

  It is built on the cute 'QmlSensorReading', as Qt's QmlLidReading is built
  on Qt's QmlSensorReading, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QmlLidReading that has a ritual and that Python can
  call so far, 10 names in all: 'metaObject', 'tr', 'backLidClosed',
  'frontLidClosed', 'backLidChanged', 'frontLidChanged', 'reading',
  'readingUpdate', '_qt_property_m_backClosed_offset',
  '_qt_property_m_frontClosed_offset'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QmlLidReading::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QmlLidReading::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QmlLidReading::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QmlLidReading::~QmlLidReading()': the destructor: Python never
    removes a C++ QmlLidReading.
  - Qt's 'QBindable<bool> QmlLidReading::bindableBackLidClosed() const':
    gives a type Python has no way to take yet.
  - Qt's 'QBindable<bool> QmlLidReading::bindableFrontLidClosed() const':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QmlLidReading is created at the first use, not by
    'QmlLidReading(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QmlLidReading.
  - Qt tells when it has removed the C++ QmlLidReading. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QmlLidReading that has no cute function yet,
    'bindableBackLidClosed', 'bindableFrontLidClosed', holds a function that
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
    Calls Qt's 'QString QmlLidReading::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmllidreading.html#tr

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
    #  QString QmlLidReading::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QmlLidReading2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def _qt_property_m_backClosed_offset() -> int:
    """
    Calls Qt's 'size_t QmlLidReading::_qt_property_m_backClosed_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmllidreading.html
    """
    #  size_t QmlLidReading::_qt_property_m_backClosed_offset()
    return Rituals.call(
        'ritual_ZN13QmlLidReading32_qt_property_m_backClosed_offsetEv',
    )

  @staticmethod
  def _qt_property_m_frontClosed_offset() -> int:
    """
    Calls Qt's 'size_t QmlLidReading::_qt_property_m_frontClosed_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmllidreading.html
    """
    #  size_t QmlLidReading::_qt_property_m_frontClosed_offset()
    return Rituals.call(
        'ritual_ZN13QmlLidReading33_qt_property_m_frontClosed_offsetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QmlLidReading'

  #  A C++ QmlLidReading Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QmlLidReading'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QmlLidReading::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmllidreading.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QmlLidReading::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QmlLidReading10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def backLidClosed(self) -> bool:
    """
    Calls Qt's 'bool QmlLidReading::backLidClosed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmllidreading.html#backLidClosed
    """
    #  bool QmlLidReading::backLidClosed() const
    return self.uglySide.call('ritual_ZNK13QmlLidReading13backLidClosedEv')

  def frontLidClosed(self) -> bool:
    """
    Calls Qt's 'bool QmlLidReading::frontLidClosed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmllidreading.html#frontLidClosed
    """
    #  bool QmlLidReading::frontLidClosed() const
    return self.uglySide.call('ritual_ZNK13QmlLidReading14frontLidClosedEv')

  def reading(self) -> Optional[QSensorReading]:
    """
    Calls Qt's 'QSensorReading *QmlLidReading::reading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmllidreading.html#reading

    Returns
    -------

    Optional[QSensorReading]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSensorReading *QmlLidReading::reading() const
    ritual = 'ritual_ZNK13QmlLidReading7readingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QmlLidReading7readingEv'
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

  @overload(QLidSensor)
  @overload(NoneType)
  def __init__(self, sensor: Optional[QLidSensor]) -> None:
    """
    Notes what was given, for Qt's 'QmlLidReading::QmlLidReading(QLidSensor
    *sensor)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmllidreading.html#QmlLidReading

    Parameters
    ----------

    sensor : Optional[QLidSensor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QmlLidReading::QmlLidReading(QLidSensor *sensor)
    self._noteCreation(QmlLidReading, lambda: Rituals.call(
        'ritual_ZN13QmlLidReadingC1EP10QLidSensor', self._addressOf(sensor),
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

  @overload(bool)
  def backLidChanged(self, closed: bool) -> None:
    """
    Calls Qt's 'void QmlLidReading::backLidChanged(bool closed)'.

    Qt's own words: https://doc.qt.io/qt-6/qmllidreading.html#backLidChanged

    Parameters
    ----------

    closed : bool
      Passed on as it is.
    """
    #  void QmlLidReading::backLidChanged(bool closed)
    self.uglySide.call('ritual_ZN13QmlLidReading14backLidChangedEb', closed)

  @overload(bool)
  def frontLidChanged(self, closed: bool) -> bool:
    """
    Calls Qt's 'bool QmlLidReading::frontLidChanged(bool closed)'.

    Qt's own words: https://doc.qt.io/qt-6/qmllidreading.html#frontLidChanged

    Parameters
    ----------

    closed : bool
      Passed on as it is.
    """
    #  bool QmlLidReading::frontLidChanged(bool closed)
    return self.uglySide.call(
        'ritual_ZN13QmlLidReading15frontLidChangedEb', closed,
    )

  def readingUpdate(self) -> None:
    """
    Calls Qt's 'void QmlLidReading::readingUpdate()'.

    Qt's own words: https://doc.qt.io/qt-6/qmllidreading.html#readingUpdate
    """
    #  void QmlLidReading::readingUpdate()
    ritual = 'ritual_ZN13QmlLidReading13readingUpdateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QmlLidReading13readingUpdateEv'
    self.uglySide.call(ritual)

  @staticmethod
  def bindableBackLidClosed(*__, **_) -> Never:
    """
    Qt's 'QBindable<bool> QmlLidReading::bindableBackLidClosed() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QmlLidReading.bindableBackLidClosed' has no cute function yet. "
        "Qt's 'QBindable<bool> QmlLidReading::bindableBackLidClosed() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def bindableFrontLidClosed(*__, **_) -> Never:
    """
    Qt's 'QBindable<bool> QmlLidReading::bindableFrontLidClosed() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QmlLidReading.bindableFrontLidClosed' has no cute function yet. "
        "Qt's 'QBindable<bool> QmlLidReading::bindableFrontLidClosed() "
        "const': gives a type Python has no way to take yet.")
