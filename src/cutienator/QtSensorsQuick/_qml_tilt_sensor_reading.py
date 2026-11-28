"""
QmlTiltSensorReading binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmltiltsensor_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QmlTiltSensorReading to be private: it declares the class in a
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
  from ..QtSensors import QSensorReading, QTiltSensor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTiltSensor = WAIT['QTiltSensor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QmlTiltSensorReading(QmlSensorReading):
  """
  The cute side of Qt's QmlTiltSensorReading: a plain Python object standing
  in front of one C++ QmlTiltSensorReading.

  It is built on the cute 'QmlSensorReading', as Qt's QmlTiltSensorReading is
  built on Qt's QmlSensorReading, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QmlTiltSensorReading that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'tr', 'yRotation',
  'xRotation', 'yRotationChanged', 'xRotationChanged', 'reading',
  'readingUpdate', '_qt_property_m_yRotation_offset',
  '_qt_property_m_xRotation_offset'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QmlTiltSensorReading::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QmlTiltSensorReading::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QmlTiltSensorReading::qt_qmlMarker_uncreatable()': one of Qt's
    own inner workings.
  - Qt's 'QmlTiltSensorReading::~QmlTiltSensorReading()': the destructor:
    Python never removes a C++ QmlTiltSensorReading.
  - Qt's 'QBindable<qreal> QmlTiltSensorReading::bindableYRotation() const':
    gives a type Python has no way to take yet.
  - Qt's 'QBindable<qreal> QmlTiltSensorReading::bindableXRotation() const':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QmlTiltSensorReading is created at the first use, not by
    'QmlTiltSensorReading(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QmlTiltSensorReading.
  - Qt tells when it has removed the C++ QmlTiltSensorReading. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QmlTiltSensorReading that has no cute function yet,
    'bindableXRotation', 'bindableYRotation', holds a function that raises
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
    Calls Qt's 'QString QmlTiltSensorReading::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmltiltsensorreading.html#tr

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
    #  QString QmlTiltSensorReading::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QmlTiltSensorReading2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def _qt_property_m_yRotation_offset() -> int:
    """
    Calls Qt's 'size_t
    QmlTiltSensorReading::_qt_property_m_yRotation_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmltiltsensorreading.html
    """
    #  size_t QmlTiltSensorReading::_qt_property_m_yRotation_offset()
    return Rituals.call(
        'ritual_ZN20QmlTiltSensorReading31_qt_property_m_yRotation_offsetEv',
    )

  @staticmethod
  def _qt_property_m_xRotation_offset() -> int:
    """
    Calls Qt's 'size_t
    QmlTiltSensorReading::_qt_property_m_xRotation_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmltiltsensorreading.html
    """
    #  size_t QmlTiltSensorReading::_qt_property_m_xRotation_offset()
    return Rituals.call(
        'ritual_ZN20QmlTiltSensorReading31_qt_property_m_xRotation_offsetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QmlTiltSensorReading'

  #  A C++ QmlTiltSensorReading Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QmlTiltSensorReading'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QmlTiltSensorReading::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmltiltsensorreading.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QmlTiltSensorReading::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QmlTiltSensorReading10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def yRotation(self) -> float:
    """
    Calls Qt's 'qreal QmlTiltSensorReading::yRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmltiltsensorreading.html#yRotation
    """
    #  qreal QmlTiltSensorReading::yRotation() const
    return self.uglySide.call('ritual_ZNK20QmlTiltSensorReading9yRotationEv')

  def xRotation(self) -> float:
    """
    Calls Qt's 'qreal QmlTiltSensorReading::xRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmltiltsensorreading.html#xRotation
    """
    #  qreal QmlTiltSensorReading::xRotation() const
    return self.uglySide.call('ritual_ZNK20QmlTiltSensorReading9xRotationEv')

  def reading(self) -> Optional[QSensorReading]:
    """
    Calls Qt's 'QSensorReading *QmlTiltSensorReading::reading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmltiltsensorreading.html#reading

    Returns
    -------

    Optional[QSensorReading]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSensorReading *QmlTiltSensorReading::reading() const
    ritual = 'ritual_ZNK20QmlTiltSensorReading7readingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QmlTiltSensorReading7readingEv'
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

  @overload(QTiltSensor)
  @overload(NoneType)
  def __init__(self, sensor: Optional[QTiltSensor]) -> None:
    """
    Notes what was given, for Qt's
    'QmlTiltSensorReading::QmlTiltSensorReading(QTiltSensor *sensor)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmltiltsensorreading.html#QmlTiltSensorReading

    Parameters
    ----------

    sensor : Optional[QTiltSensor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QmlTiltSensorReading::QmlTiltSensorReading(QTiltSensor *sensor)
    self._noteCreation(QmlTiltSensorReading, lambda: Rituals.call(
        'ritual_ZN20QmlTiltSensorReadingC1EP11QTiltSensor',
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

  def yRotationChanged(self) -> None:
    """
    Calls Qt's 'void QmlTiltSensorReading::yRotationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmltiltsensorreading.html#yRotationChanged
    """
    #  void QmlTiltSensorReading::yRotationChanged()
    self.uglySide.call('ritual_ZN20QmlTiltSensorReading16yRotationChangedEv')

  def xRotationChanged(self) -> None:
    """
    Calls Qt's 'void QmlTiltSensorReading::xRotationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmltiltsensorreading.html#xRotationChanged
    """
    #  void QmlTiltSensorReading::xRotationChanged()
    self.uglySide.call('ritual_ZN20QmlTiltSensorReading16xRotationChangedEv')

  def readingUpdate(self) -> None:
    """
    Calls Qt's 'void QmlTiltSensorReading::readingUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmltiltsensorreading.html#readingUpdate
    """
    #  void QmlTiltSensorReading::readingUpdate()
    ritual = 'ritual_ZN20QmlTiltSensorReading13readingUpdateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QmlTiltSensorReading13readingUpdateEv'
    self.uglySide.call(ritual)

  @staticmethod
  def bindableXRotation(*__, **_) -> Never:
    """
    Qt's 'QBindable<qreal> QmlTiltSensorReading::bindableXRotation() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QmlTiltSensorReading.bindableXRotation' has no cute function yet. "
        "Qt's 'QBindable<qreal> QmlTiltSensorReading::bindableXRotation() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def bindableYRotation(*__, **_) -> Never:
    """
    Qt's 'QBindable<qreal> QmlTiltSensorReading::bindableYRotation() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QmlTiltSensorReading.bindableYRotation' has no cute function yet. "
        "Qt's 'QBindable<qreal> QmlTiltSensorReading::bindableYRotation() "
        "const': gives a type Python has no way to take yet.")
