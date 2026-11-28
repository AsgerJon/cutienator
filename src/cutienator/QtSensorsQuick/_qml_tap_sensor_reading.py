"""
QmlTapSensorReading binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmltapsensor_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QmlTapSensorReading to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtSensors import QTapReading
from . import QmlSensorReading

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtSensors import QSensorReading, QTapSensor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTapSensor = WAIT['QTapSensor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QmlTapSensorReading(QmlSensorReading):
  """
  The cute side of Qt's QmlTapSensorReading: a plain Python object standing
  in front of one C++ QmlTapSensorReading.

  It is built on the cute 'QmlSensorReading', as Qt's QmlTapSensorReading is
  built on Qt's QmlSensorReading, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QmlTapSensorReading that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'tr',
  'tapDirection', 'isDoubleTap', 'tapDirectionChanged', 'isDoubleTapChanged',
  'reading', 'readingUpdate', '_qt_property_m_tapDirection_offset',
  '_qt_property_m_isDoubleTap_offset'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QmlTapSensorReading::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QmlTapSensorReading::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QmlTapSensorReading::qt_qmlMarker_uncreatable()': one of Qt's
    own inner workings.
  - Qt's 'QmlTapSensorReading::~QmlTapSensorReading()': the destructor:
    Python never removes a C++ QmlTapSensorReading.
  - Qt's 'QBindable<QTapReading::TapDirection>
    QmlTapSensorReading::bindableTapDirection() const': gives a type Python
    has no way to take yet.
  - Qt's 'QBindable<bool> QmlTapSensorReading::bindableDoubleTap() const':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QmlTapSensorReading is created at the first use, not by
    'QmlTapSensorReading(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QmlTapSensorReading.
  - Qt tells when it has removed the C++ QmlTapSensorReading. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QmlTapSensorReading that has no cute function yet,
    'bindableDoubleTap', 'bindableTapDirection', holds a function that raises
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
    Calls Qt's 'QString QmlTapSensorReading::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmltapsensorreading.html#tr

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
    #  QString QmlTapSensorReading::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QmlTapSensorReading2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def _qt_property_m_tapDirection_offset() -> int:
    """
    Calls Qt's 'size_t
    QmlTapSensorReading::_qt_property_m_tapDirection_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmltapsensorreading.html
    """
    #  size_t QmlTapSensorReading::_qt_property_m_tapDirection_offset()
    return Rituals.call(
        'ritual_ZN19QmlTapSensorReading34_qt_property_m_tapDirection_offset'
        'Ev',
    )

  @staticmethod
  def _qt_property_m_isDoubleTap_offset() -> int:
    """
    Calls Qt's 'size_t
    QmlTapSensorReading::_qt_property_m_isDoubleTap_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmltapsensorreading.html
    """
    #  size_t QmlTapSensorReading::_qt_property_m_isDoubleTap_offset()
    return Rituals.call(
        'ritual_ZN19QmlTapSensorReading33_qt_property_m_isDoubleTap_offsetE'
        'v',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QmlTapSensorReading'

  #  A C++ QmlTapSensorReading Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QmlTapSensorReading'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QmlTapSensorReading::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmltapsensorreading.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QmlTapSensorReading::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QmlTapSensorReading10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def tapDirection(self) -> QTapReading.TapDirection:
    """
    Calls Qt's 'QTapReading::TapDirection QmlTapSensorReading::tapDirection()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmltapsensorreading.html#tapDirection

    Returns
    -------

    QTapReading.TapDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QTapReading.TapDirection(number)' gives.
    """
    #  QTapReading::TapDirection QmlTapSensorReading::tapDirection() const
    return QTapReading.TapDirection(self.uglySide.call(
        'ritual_ZNK19QmlTapSensorReading12tapDirectionEv',
    ))

  def isDoubleTap(self) -> bool:
    """
    Calls Qt's 'bool QmlTapSensorReading::isDoubleTap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmltapsensorreading.html#isDoubleTap
    """
    #  bool QmlTapSensorReading::isDoubleTap() const
    return self.uglySide.call(
        'ritual_ZNK19QmlTapSensorReading11isDoubleTapEv',
    )

  def reading(self) -> Optional[QSensorReading]:
    """
    Calls Qt's 'QSensorReading *QmlTapSensorReading::reading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmltapsensorreading.html#reading

    Returns
    -------

    Optional[QSensorReading]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSensorReading *QmlTapSensorReading::reading() const
    ritual = 'ritual_ZNK19QmlTapSensorReading7readingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QmlTapSensorReading7readingEv'
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

  @overload(QTapSensor)
  @overload(NoneType)
  def __init__(self, sensor: Optional[QTapSensor]) -> None:
    """
    Notes what was given, for Qt's
    'QmlTapSensorReading::QmlTapSensorReading(QTapSensor *sensor)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmltapsensorreading.html#QmlTapSensorReading

    Parameters
    ----------

    sensor : Optional[QTapSensor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QmlTapSensorReading::QmlTapSensorReading(QTapSensor *sensor)
    self._noteCreation(QmlTapSensorReading, lambda: Rituals.call(
        'ritual_ZN19QmlTapSensorReadingC1EP10QTapSensor',
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

  def tapDirectionChanged(self) -> None:
    """
    Calls Qt's 'void QmlTapSensorReading::tapDirectionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmltapsensorreading.html#tapDirectionChanged
    """
    #  void QmlTapSensorReading::tapDirectionChanged()
    self.uglySide.call(
        'ritual_ZN19QmlTapSensorReading19tapDirectionChangedEv',
    )

  def isDoubleTapChanged(self) -> None:
    """
    Calls Qt's 'void QmlTapSensorReading::isDoubleTapChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmltapsensorreading.html#isDoubleTapChanged
    """
    #  void QmlTapSensorReading::isDoubleTapChanged()
    self.uglySide.call(
        'ritual_ZN19QmlTapSensorReading18isDoubleTapChangedEv',
    )

  def readingUpdate(self) -> None:
    """
    Calls Qt's 'void QmlTapSensorReading::readingUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmltapsensorreading.html#readingUpdate
    """
    #  void QmlTapSensorReading::readingUpdate()
    ritual = 'ritual_ZN19QmlTapSensorReading13readingUpdateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QmlTapSensorReading13readingUpdateEv'
    self.uglySide.call(ritual)

  @staticmethod
  def bindableDoubleTap(*__, **_) -> Never:
    """
    Qt's 'QBindable<bool> QmlTapSensorReading::bindableDoubleTap() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QmlTapSensorReading.bindableDoubleTap' has no cute function yet. "
        "Qt's 'QBindable<bool> QmlTapSensorReading::bindableDoubleTap() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def bindableTapDirection(*__, **_) -> Never:
    """
    Qt's 'QBindable<QTapReading::TapDirection>
    QmlTapSensorReading::bindableTapDirection() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QmlTapSensorReading.bindableTapDirection' has no cute function "
        "yet. Qt's 'QBindable<QTapReading::TapDirection> "
        "QmlTapSensorReading::bindableTapDirection() const': gives a type "
        "Python has no way to take yet.")
