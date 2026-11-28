"""
QmlLightSensorReading binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmllightsensor_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QmlLightSensorReading to be private: it declares the class in a
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
  from ..QtSensors import QLightSensor, QSensorReading
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLightSensor = WAIT['QLightSensor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QmlLightSensorReading(QmlSensorReading):
  """
  The cute side of Qt's QmlLightSensorReading: a plain Python object standing
  in front of one C++ QmlLightSensorReading.

  It is built on the cute 'QmlSensorReading', as Qt's QmlLightSensorReading
  is built on Qt's QmlSensorReading, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QmlLightSensorReading that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'tr', 'illuminance',
  'illuminanceChanged', 'reading', 'readingUpdate',
  '_qt_property_m_illuminance_offset'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QmlLightSensorReading::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QmlLightSensorReading::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QmlLightSensorReading::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.
  - Qt's 'QmlLightSensorReading::~QmlLightSensorReading()': the destructor:
    Python never removes a C++ QmlLightSensorReading.
  - Qt's 'QBindable<qreal> QmlLightSensorReading::bindableIlluminance()
    const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QmlLightSensorReading is created at the first use, not by
    'QmlLightSensorReading(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QmlLightSensorReading.
  - Qt tells when it has removed the C++ QmlLightSensorReading. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QmlLightSensorReading that has no cute function yet,
    'bindableIlluminance', holds a function that raises
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
    Calls Qt's 'QString QmlLightSensorReading::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmllightsensorreading.html#tr

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
    #  QString QmlLightSensorReading::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QmlLightSensorReading2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def _qt_property_m_illuminance_offset() -> int:
    """
    Calls Qt's 'size_t
    QmlLightSensorReading::_qt_property_m_illuminance_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmllightsensorreading.html
    """
    #  size_t QmlLightSensorReading::_qt_property_m_illuminance_offset()
    return Rituals.call(
        'ritual_ZN21QmlLightSensorReading33_qt_property_m_illuminance_offse'
        'tEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QmlLightSensorReading'

  #  A C++ QmlLightSensorReading Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QmlLightSensorReading'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QmlLightSensorReading::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmllightsensorreading.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QmlLightSensorReading::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QmlLightSensorReading10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def illuminance(self) -> float:
    """
    Calls Qt's 'qreal QmlLightSensorReading::illuminance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmllightsensorreading.html#illuminance
    """
    #  qreal QmlLightSensorReading::illuminance() const
    return self.uglySide.call(
        'ritual_ZNK21QmlLightSensorReading11illuminanceEv',
    )

  def reading(self) -> Optional[QSensorReading]:
    """
    Calls Qt's 'QSensorReading *QmlLightSensorReading::reading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmllightsensorreading.html#reading

    Returns
    -------

    Optional[QSensorReading]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSensorReading *QmlLightSensorReading::reading() const
    ritual = 'ritual_ZNK21QmlLightSensorReading7readingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QmlLightSensorReading7readingEv'
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

  @overload(QLightSensor)
  @overload(NoneType)
  def __init__(self, sensor: Optional[QLightSensor]) -> None:
    """
    Notes what was given, for Qt's
    'QmlLightSensorReading::QmlLightSensorReading(QLightSensor *sensor)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmllightsensorreading.html#QmlLightSensorReading

    Parameters
    ----------

    sensor : Optional[QLightSensor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QmlLightSensorReading::QmlLightSensorReading(QLightSensor *sensor)
    self._noteCreation(QmlLightSensorReading, lambda: Rituals.call(
        'ritual_ZN21QmlLightSensorReadingC1EP12QLightSensor',
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

  def illuminanceChanged(self) -> None:
    """
    Calls Qt's 'void QmlLightSensorReading::illuminanceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmllightsensorreading.html#illuminanceChanged
    """
    #  void QmlLightSensorReading::illuminanceChanged()
    self.uglySide.call(
        'ritual_ZN21QmlLightSensorReading18illuminanceChangedEv',
    )

  def readingUpdate(self) -> None:
    """
    Calls Qt's 'void QmlLightSensorReading::readingUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmllightsensorreading.html#readingUpdate
    """
    #  void QmlLightSensorReading::readingUpdate()
    ritual = 'ritual_ZN21QmlLightSensorReading13readingUpdateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QmlLightSensorReading13readingUpdateEv'
    self.uglySide.call(ritual)

  @staticmethod
  def bindableIlluminance(*__, **_) -> Never:
    """
    Qt's 'QBindable<qreal> QmlLightSensorReading::bindableIlluminance()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QmlLightSensorReading.bindableIlluminance' has no cute function "
        "yet. Qt's 'QBindable<qreal> "
        "QmlLightSensorReading::bindableIlluminance() const': gives a type "
        "Python has no way to take yet.")
