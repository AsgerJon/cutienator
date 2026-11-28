"""
QmlAmbientLightSensorReading binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSensorsQuick/6.12.0/QtSensorsQuick/private/qmlambientlightsensor_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QmlAmbientLightSensorReading to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtSensors import QAmbientLightReading
from . import QmlSensorReading

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtSensors import QAmbientLightSensor, QSensorReading
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAmbientLightSensor = WAIT['QAmbientLightSensor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QmlAmbientLightSensorReading(QmlSensorReading):
  """
  The cute side of Qt's QmlAmbientLightSensorReading: a plain Python object
  standing in front of one C++ QmlAmbientLightSensorReading.

  It is built on the cute 'QmlSensorReading', as Qt's
  QmlAmbientLightSensorReading is built on Qt's QmlSensorReading, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QmlAmbientLightSensorReading that has a ritual and
  that Python can call so far, 7 names in all: 'metaObject', 'tr',
  'lightLevel', 'lightLevelChanged', 'reading', 'readingUpdate',
  '_qt_property_m_lightLevel_offset'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QmlAmbientLightSensorReading::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QmlAmbientLightSensorReading::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QmlAmbientLightSensorReading::qt_qmlMarker_uncreatable()': one
    of Qt's own inner workings.
  - Qt's 'QmlAmbientLightSensorReading::~QmlAmbientLightSensorReading()': the
    destructor: Python never removes a C++ QmlAmbientLightSensorReading.
  - Qt's 'QBindable<QAmbientLightReading::LightLevel>
    QmlAmbientLightSensorReading::bindableLightLevel() const': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QmlAmbientLightSensorReading is created at the first use, not by
    'QmlAmbientLightSensorReading(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QmlAmbientLightSensorReading.
  - Qt tells when it has removed the C++ QmlAmbientLightSensorReading. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QmlAmbientLightSensorReading that has no cute function
    yet, 'bindableLightLevel', holds a function that raises
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
    Calls Qt's 'QString QmlAmbientLightSensorReading::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlambientlightsensorreading.html#tr

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
    #  QString QmlAmbientLightSensorReading::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN28QmlAmbientLightSensorReading2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def _qt_property_m_lightLevel_offset() -> int:
    """
    Calls Qt's 'size_t
    QmlAmbientLightSensorReading::_qt_property_m_lightLevel_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlambientlightsensorreading.html
    """
    #  size_t
    #      QmlAmbientLightSensorReading::_qt_property_m_lightLevel_offset()
    return Rituals.call(
        'ritual_ZN28QmlAmbientLightSensorReading32_qt_property_m_lightLevel'
        '_offsetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QmlAmbientLightSensorReading'

  #  A C++ QmlAmbientLightSensorReading Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QmlAmbientLightSensorReading'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QmlAmbientLightSensorReading::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlambientlightsensorreading.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QmlAmbientLightSensorReading::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QmlAmbientLightSensorReading10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def lightLevel(self) -> QAmbientLightReading.LightLevel:
    """
    Calls Qt's 'QAmbientLightReading::LightLevel
    QmlAmbientLightSensorReading::lightLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlambientlightsensorreading.html#lightLevel

    Returns
    -------

    QAmbientLightReading.LightLevel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QAmbientLightReading.LightLevel(number)' gives.
    """
    #  QAmbientLightReading::LightLevel
    #      QmlAmbientLightSensorReading::lightLevel() const
    return QAmbientLightReading.LightLevel(self.uglySide.call(
        'ritual_ZNK28QmlAmbientLightSensorReading10lightLevelEv',
    ))

  def reading(self) -> Optional[QSensorReading]:
    """
    Calls Qt's 'QSensorReading *QmlAmbientLightSensorReading::reading()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlambientlightsensorreading.html#reading

    Returns
    -------

    Optional[QSensorReading]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSensorReading *QmlAmbientLightSensorReading::reading() const
    ritual = 'ritual_ZNK28QmlAmbientLightSensorReading7readingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK28QmlAmbientLightSensorReading7readingEv'
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

  @overload(QAmbientLightSensor)
  @overload(NoneType)
  def __init__(self, sensor: Optional[QAmbientLightSensor]) -> None:
    """
    Notes what was given, for Qt's
    'QmlAmbientLightSensorReading::QmlAmbientLightSensorReading(
    QAmbientLightSensor *sensor)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlambientlightsensorreading.html

    Parameters
    ----------

    sensor : Optional[QAmbientLightSensor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QmlAmbientLightSensorReading::QmlAmbientLightSensorReading(
    #      QAmbientLightSensor *sensor)
    self._noteCreation(QmlAmbientLightSensorReading, lambda: Rituals.call(
        'ritual_ZN28QmlAmbientLightSensorReadingC1EP19QAmbientLightSensor',
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

  def lightLevelChanged(self) -> None:
    """
    Calls Qt's 'void QmlAmbientLightSensorReading::lightLevelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlambientlightsensorreading.html
    """
    #  void QmlAmbientLightSensorReading::lightLevelChanged()
    self.uglySide.call(
        'ritual_ZN28QmlAmbientLightSensorReading17lightLevelChangedEv',
    )

  def readingUpdate(self) -> None:
    """
    Calls Qt's 'void QmlAmbientLightSensorReading::readingUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmlambientlightsensorreading.html#readingUpdate
    """
    #  void QmlAmbientLightSensorReading::readingUpdate()
    ritual = 'ritual_ZN28QmlAmbientLightSensorReading13readingUpdateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN28QmlAmbientLightSensorReading13readingUpdateEv'
    self.uglySide.call(ritual)

  @staticmethod
  def bindableLightLevel(*__, **_) -> Never:
    """
    Qt's 'QBindable<QAmbientLightReading::LightLevel>
    QmlAmbientLightSensorReading::bindableLightLevel() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QmlAmbientLightSensorReading.bindableLightLevel' has no cute "
        "function yet. Qt's 'QBindable<QAmbientLightReading::LightLevel> "
        "QmlAmbientLightSensorReading::bindableLightLevel() const': gives a "
        "type Python has no way to take yet.")
