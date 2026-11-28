"""
QmlIRProximitySensorReading binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlirproximitysensor_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QmlIRProximitySensorReading to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QmlSensorReading

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtSensors import QIRProximitySensor, QSensorReading
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIRProximitySensor = WAIT['QIRProximitySensor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QmlIRProximitySensorReading(QmlSensorReading):
  """
  The cute side of Qt's QmlIRProximitySensorReading: a plain Python object
  standing in front of one C++ QmlIRProximitySensorReading.

  It is built on the cute 'QmlSensorReading', as Qt's
  QmlIRProximitySensorReading is built on Qt's QmlSensorReading, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QmlIRProximitySensorReading that has a ritual and
  that Python can call so far, 7 names in all: 'metaObject', 'tr',
  'reflectance', 'reflectanceChanged', 'reading', 'readingUpdate',
  '_qt_property_m_reflectance_offset'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QmlIRProximitySensorReading::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QmlIRProximitySensorReading::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QmlIRProximitySensorReading::qt_qmlMarker_uncreatable()': one
    of Qt's own inner workings.
  - Qt's 'QmlIRProximitySensorReading::~QmlIRProximitySensorReading()': the
    destructor: Python never removes a C++ QmlIRProximitySensorReading.
  - Qt's 'QBindable<qreal> QmlIRProximitySensorReading::bindableReflectance()
    const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QmlIRProximitySensorReading is created at the first use, not by
    'QmlIRProximitySensorReading(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QmlIRProximitySensorReading.
  - Qt tells when it has removed the C++ QmlIRProximitySensorReading. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QmlIRProximitySensorReading that has no cute function
    yet, 'bindableReflectance', holds a function that raises
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
    Calls Qt's 'QString QmlIRProximitySensorReading::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlirproximitysensorreading.html#tr

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
    #  QString QmlIRProximitySensorReading::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN27QmlIRProximitySensorReading2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def _qt_property_m_reflectance_offset() -> int:
    """
    Calls Qt's 'size_t
    QmlIRProximitySensorReading::_qt_property_m_reflectance_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlirproximitysensorreading.html
    """
    #  size_t
    #      QmlIRProximitySensorReading::_qt_property_m_reflectance_offset()
    return Rituals.call(
        'ritual_ZN27QmlIRProximitySensorReading33_qt_property_m_reflectance'
        '_offsetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QmlIRProximitySensorReading'

  #  A C++ QmlIRProximitySensorReading Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QmlIRProximitySensorReading'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QmlIRProximitySensorReading::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlirproximitysensorreading.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QmlIRProximitySensorReading::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QmlIRProximitySensorReading10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def reflectance(self) -> float:
    """
    Calls Qt's 'qreal QmlIRProximitySensorReading::reflectance() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlirproximitysensorreading.html#reflectance
    """
    #  qreal QmlIRProximitySensorReading::reflectance() const
    return self.uglySide.call(
        'ritual_ZNK27QmlIRProximitySensorReading11reflectanceEv',
    )

  def reading(self) -> Optional[QSensorReading]:
    """
    Calls Qt's 'QSensorReading *QmlIRProximitySensorReading::reading()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlirproximitysensorreading.html#reading

    Returns
    -------

    Optional[QSensorReading]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSensorReading *QmlIRProximitySensorReading::reading() const
    ritual = 'ritual_ZNK27QmlIRProximitySensorReading7readingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK27QmlIRProximitySensorReading7readingEv'
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

  @overload(QIRProximitySensor)
  @overload(NoneType)
  def __init__(self, sensor: Optional[QIRProximitySensor]) -> None:
    """
    Notes what was given, for Qt's
    'QmlIRProximitySensorReading::QmlIRProximitySensorReading(
    QIRProximitySensor *sensor)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlirproximitysensorreading.html

    Parameters
    ----------

    sensor : Optional[QIRProximitySensor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QmlIRProximitySensorReading::QmlIRProximitySensorReading(
    #      QIRProximitySensor *sensor)
    self._noteCreation(QmlIRProximitySensorReading, lambda: Rituals.call(
        'ritual_ZN27QmlIRProximitySensorReadingC1EP18QIRProximitySensor',
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

  def reflectanceChanged(self) -> None:
    """
    Calls Qt's 'void QmlIRProximitySensorReading::reflectanceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlirproximitysensorreading.html
    """
    #  void QmlIRProximitySensorReading::reflectanceChanged()
    self.uglySide.call(
        'ritual_ZN27QmlIRProximitySensorReading18reflectanceChangedEv',
    )

  def readingUpdate(self) -> None:
    """
    Calls Qt's 'void QmlIRProximitySensorReading::readingUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlirproximitysensorreading.html#readingUpdate
    """
    #  void QmlIRProximitySensorReading::readingUpdate()
    ritual = 'ritual_ZN27QmlIRProximitySensorReading13readingUpdateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QmlIRProximitySensorReading13readingUpdateEv'
    self.uglySide.call(ritual)

  @staticmethod
  def bindableReflectance(*__, **_) -> Never:
    """
    Qt's 'QBindable<qreal> QmlIRProximitySensorReading::bindableReflectance()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QmlIRProximitySensorReading.bindableReflectance' has no cute "
        "function yet. Qt's 'QBindable<qreal> "
        "QmlIRProximitySensorReading::bindableReflectance() const': gives a "
        "type Python has no way to take yet.")
