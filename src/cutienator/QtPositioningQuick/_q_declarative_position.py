"""
QDeclarativePosition binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPositioningQuick/6.12.0/QtPositioningQuick/private/qdeclarativeposition_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativePosition to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDateTime, QMetaObject
  from ..QtPositioning import QGeoCoordinate, QGeoPositionInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoPositionInfo = WAIT['QGeoPositionInfo']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativePosition(QObject):
  """
  The cute side of Qt's QDeclarativePosition: a plain Python object standing
  in front of one C++ QDeclarativePosition.

  It is built on the cute 'QObject', as Qt's QDeclarativePosition is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativePosition that has a ritual and that
  Python can call so far, 61 names in all: 'metaObject', 'tr',
  'isLatitudeValid', 'isLongitudeValid', 'isAltitudeValid', 'timestamp',
  'speed', 'isSpeedValid', 'coordinate', 'isHorizontalAccuracyValid',
  'horizontalAccuracy', 'isVerticalAccuracyValid', 'verticalAccuracy',
  'isDirectionValid', 'direction', 'isVerticalSpeedValid', 'verticalSpeed',
  'isMagneticVariationValid', 'magneticVariation', 'setPosition', 'position',
  'isDirectionAccuracyValid', 'directionAccuracy',
  'isLatitudeValidActualCalculation', 'isLongitudeValidActualCalculation',
  'isAltitudeValidActualCalculation', 'coordinateActualCalculation',
  'timestampActualCalculation', 'speedActualCalculation',
  'isSpeedValidActualCalculation', 'horizontalAccuracyActualCalculation',
  'verticalAccuracyActualCalculation',
  'isHorizontalAccuracyValidActualCalculation',
  'isVerticalAccuracyValidActualCalculation',
  'isDirectionValidActualCalculation', 'directionActualCalculation',
  'isVerticalSpeedValidActualCalculation', 'verticalSpeedActualCalculation',
  'magneticVariationActualCalculation',
  'isMagneticVariationValidActualCalculation',
  'directionAccuracyActualCalculation',
  'isDirectionAccuracyValidActualCalculation',
  '_qt_property_m_computedLatitudeValid_offset',
  '_qt_property_m_computedLongitudeValid_offset',
  '_qt_property_m_computedAltitudeValid_offset',
  '_qt_property_m_computedCoordinate_offset',
  '_qt_property_m_computedTimestamp_offset',
  '_qt_property_m_computedSpeed_offset',
  '_qt_property_m_computedSpeedValid_offset',
  '_qt_property_m_computedHorizontalAccuracy_offset',
  '_qt_property_m_computedVerticalAccuracy_offset',
  '_qt_property_m_computedHorizontalAccuracyValid_offset',
  '_qt_property_m_computedVerticalAccuracyValid_offset',
  '_qt_property_m_computedDirectionValid_offset',
  '_qt_property_m_computedDirection_offset',
  '_qt_property_m_computedVerticalSpeedValid_offset',
  '_qt_property_m_computedVerticalSpeed_offset',
  '_qt_property_m_computedMagneticVariation_offset',
  '_qt_property_m_computedMagneticVariationValid_offset',
  '_qt_property_m_computedDirectionAccuracy_offset',
  '_qt_property_m_computedDirectionAccuracyValid_offset'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativePosition::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QDeclarativePosition::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QDeclarativePosition::~QDeclarativePosition()': the destructor:
    Python never removes a C++ QDeclarativePosition.
  - Qt's 'QBindable<bool> QDeclarativePosition::bindableLatitudeValid()
    const': gives a type Python has no way to take yet.
  - Qt's 'QBindable<bool> QDeclarativePosition::bindableLongitudeValid()
    const': gives a type Python has no way to take yet.
  - Qt's 'QBindable<bool> QDeclarativePosition::bindableAltitudeValid()
    const': gives a type Python has no way to take yet.
  - Qt's 'QBindable<QGeoCoordinate>
    QDeclarativePosition::bindableCoordinate() const': gives a type Python
    has no way to take yet.
  - Qt's 'QBindable<QDateTime> QDeclarativePosition::bindableTimestamp()
    const': gives a type Python has no way to take yet.
  - Qt's 'QBindable<double> QDeclarativePosition::bindableSpeed() const':
    gives a type Python has no way to take yet.
  - Qt's 'QBindable<bool> QDeclarativePosition::bindableSpeedValid() const':
    gives a type Python has no way to take yet.
  - Qt's 'QBindable<qreal> QDeclarativePosition::bindableHorizontalAccuracy()
    const': gives a type Python has no way to take yet.
  - Qt's 'QBindable<qreal> QDeclarativePosition::binableVerticalAccuracy()
    const': gives a type Python has no way to take yet.
  - Qt's 'QBindable<bool>
    QDeclarativePosition::bindableHorizontalAccuracyValid() const': gives a
    type Python has no way to take yet.
  - Qt's 'QBindable<bool>
    QDeclarativePosition::bindableVerticalAccuracyValid() const': gives a
    type Python has no way to take yet.
  - Qt's 'QBindable<bool> QDeclarativePosition::bindableDirectionValid()
    const': gives a type Python has no way to take yet.
  - Qt's 'QBindable<double> QDeclarativePosition::bindableDirection() const':
    gives a type Python has no way to take yet.
  - Qt's 'QBindable<bool> QDeclarativePosition::bindableVerticalSpeedValid()
    const': gives a type Python has no way to take yet.
  - Qt's 'QBindable<double> QDeclarativePosition::bindableVerticalSpeed()
    const': gives a type Python has no way to take yet.
  - Qt's 'QBindable<double> QDeclarativePosition::bindableMagneticVariation()
    const': gives a type Python has no way to take yet.
  - Qt's 'QBindable<bool>
    QDeclarativePosition::bindableMagneticVariationValid() const': gives a
    type Python has no way to take yet.
  - Qt's 'QBindable<double> QDeclarativePosition::bindableDirectionAccuracy()
    const': gives a type Python has no way to take yet.
  - Qt's 'QBindable<bool>
    QDeclarativePosition::bindableDirectionAccuracyValid() const': gives a
    type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 86 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDeclarativePosition is created at the first use, not by
    'QDeclarativePosition(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativePosition.
  - Qt tells when it has removed the C++ QDeclarativePosition. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDeclarativePosition that has no cute function yet,
    'binableVerticalAccuracy', 'bindableAltitudeValid', 'bindableCoordinate',
    'bindableDirection', 'bindableDirectionAccuracy',
    'bindableDirectionAccuracyValid', 'bindableDirectionValid',
    'bindableHorizontalAccuracy', 'bindableHorizontalAccuracyValid',
    'bindableLatitudeValid', 'bindableLongitudeValid',
    'bindableMagneticVariation', 'bindableMagneticVariationValid',
    'bindableSpeed', 'bindableSpeedValid', 'bindableTimestamp',
    'bindableVerticalAccuracyValid', 'bindableVerticalSpeed',
    'bindableVerticalSpeedValid', holds a function that raises
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
    Calls Qt's 'QString QDeclarativePosition::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeposition.html#tr

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
    #  QString QDeclarativePosition::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QDeclarativePosition2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def _qt_property_m_computedLatitudeValid_offset() -> int:
    """
    Calls Qt's 'size_t
    QDeclarativePosition::_qt_property_m_computedLatitudeValid_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  size_t
    #      QDeclarativePosition::_qt_property_m_computedLatitudeValid_offset(
    #      )
    return Rituals.call(
        'ritual_ZN20QDeclarativePosition43_qt_property_m_computedLatitudeVa'
        'lid_offsetEv',
    )

  @staticmethod
  def _qt_property_m_computedLongitudeValid_offset() -> int:
    """
    Calls Qt's 'size_t
    QDeclarativePosition::_qt_property_m_computedLongitudeValid_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  size_t QDeclarativePosition::
    #      _qt_property_m_computedLongitudeValid_offset()
    return Rituals.call(
        'ritual_ZN20QDeclarativePosition44_qt_property_m_computedLongitudeV'
        'alid_offsetEv',
    )

  @staticmethod
  def _qt_property_m_computedAltitudeValid_offset() -> int:
    """
    Calls Qt's 'size_t
    QDeclarativePosition::_qt_property_m_computedAltitudeValid_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  size_t
    #      QDeclarativePosition::_qt_property_m_computedAltitudeValid_offset(
    #      )
    return Rituals.call(
        'ritual_ZN20QDeclarativePosition43_qt_property_m_computedAltitudeVa'
        'lid_offsetEv',
    )

  @staticmethod
  def _qt_property_m_computedCoordinate_offset() -> int:
    """
    Calls Qt's 'size_t
    QDeclarativePosition::_qt_property_m_computedCoordinate_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  size_t
    #      QDeclarativePosition::_qt_property_m_computedCoordinate_offset()
    return Rituals.call(
        'ritual_ZN20QDeclarativePosition40_qt_property_m_computedCoordinate'
        '_offsetEv',
    )

  @staticmethod
  def _qt_property_m_computedTimestamp_offset() -> int:
    """
    Calls Qt's 'size_t
    QDeclarativePosition::_qt_property_m_computedTimestamp_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  size_t QDeclarativePosition::_qt_property_m_computedTimestamp_offset()
    return Rituals.call(
        'ritual_ZN20QDeclarativePosition39_qt_property_m_computedTimestamp_'
        'offsetEv',
    )

  @staticmethod
  def _qt_property_m_computedSpeed_offset() -> int:
    """
    Calls Qt's 'size_t
    QDeclarativePosition::_qt_property_m_computedSpeed_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  size_t QDeclarativePosition::_qt_property_m_computedSpeed_offset()
    return Rituals.call(
        'ritual_ZN20QDeclarativePosition35_qt_property_m_computedSpeed_offs'
        'etEv',
    )

  @staticmethod
  def _qt_property_m_computedSpeedValid_offset() -> int:
    """
    Calls Qt's 'size_t
    QDeclarativePosition::_qt_property_m_computedSpeedValid_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  size_t
    #      QDeclarativePosition::_qt_property_m_computedSpeedValid_offset()
    return Rituals.call(
        'ritual_ZN20QDeclarativePosition40_qt_property_m_computedSpeedValid'
        '_offsetEv',
    )

  @staticmethod
  def _qt_property_m_computedHorizontalAccuracy_offset() -> int:
    """
    Calls Qt's 'size_t
    QDeclarativePosition::_qt_property_m_computedHorizontalAccuracy_offset(
    )'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  size_t QDeclarativePosition::
    #      _qt_property_m_computedHorizontalAccuracy_offset()
    return Rituals.call(
        'ritual_ZN20QDeclarativePosition48_qt_property_m_computedHorizontal'
        'Accuracy_offsetEv',
    )

  @staticmethod
  def _qt_property_m_computedVerticalAccuracy_offset() -> int:
    """
    Calls Qt's 'size_t
    QDeclarativePosition::_qt_property_m_computedVerticalAccuracy_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  size_t QDeclarativePosition::
    #      _qt_property_m_computedVerticalAccuracy_offset()
    return Rituals.call(
        'ritual_ZN20QDeclarativePosition46_qt_property_m_computedVerticalAc'
        'curacy_offsetEv',
    )

  @staticmethod
  def _qt_property_m_computedHorizontalAccuracyValid_offset() -> int:
    """
    Calls Qt's 'size_t QDeclarativePosition::
    _qt_property_m_computedHorizontalAccuracyValid_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  size_t QDeclarativePosition::
    #      _qt_property_m_computedHorizontalAccuracyValid_offset()
    return Rituals.call(
        'ritual_ZN20QDeclarativePosition53_qt_property_m_computedHorizontal'
        'AccuracyValid_offsetEv',
    )

  @staticmethod
  def _qt_property_m_computedVerticalAccuracyValid_offset() -> int:
    """
    Calls Qt's 'size_t QDeclarativePosition::
    _qt_property_m_computedVerticalAccuracyValid_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  size_t QDeclarativePosition::
    #      _qt_property_m_computedVerticalAccuracyValid_offset()
    return Rituals.call(
        'ritual_ZN20QDeclarativePosition51_qt_property_m_computedVerticalAc'
        'curacyValid_offsetEv',
    )

  @staticmethod
  def _qt_property_m_computedDirectionValid_offset() -> int:
    """
    Calls Qt's 'size_t
    QDeclarativePosition::_qt_property_m_computedDirectionValid_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  size_t QDeclarativePosition::
    #      _qt_property_m_computedDirectionValid_offset()
    return Rituals.call(
        'ritual_ZN20QDeclarativePosition44_qt_property_m_computedDirectionV'
        'alid_offsetEv',
    )

  @staticmethod
  def _qt_property_m_computedDirection_offset() -> int:
    """
    Calls Qt's 'size_t
    QDeclarativePosition::_qt_property_m_computedDirection_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  size_t QDeclarativePosition::_qt_property_m_computedDirection_offset()
    return Rituals.call(
        'ritual_ZN20QDeclarativePosition39_qt_property_m_computedDirection_'
        'offsetEv',
    )

  @staticmethod
  def _qt_property_m_computedVerticalSpeedValid_offset() -> int:
    """
    Calls Qt's 'size_t
    QDeclarativePosition::_qt_property_m_computedVerticalSpeedValid_offset(
    )'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  size_t QDeclarativePosition::
    #      _qt_property_m_computedVerticalSpeedValid_offset()
    return Rituals.call(
        'ritual_ZN20QDeclarativePosition48_qt_property_m_computedVerticalSp'
        'eedValid_offsetEv',
    )

  @staticmethod
  def _qt_property_m_computedVerticalSpeed_offset() -> int:
    """
    Calls Qt's 'size_t
    QDeclarativePosition::_qt_property_m_computedVerticalSpeed_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  size_t
    #      QDeclarativePosition::_qt_property_m_computedVerticalSpeed_offset(
    #      )
    return Rituals.call(
        'ritual_ZN20QDeclarativePosition43_qt_property_m_computedVerticalSp'
        'eed_offsetEv',
    )

  @staticmethod
  def _qt_property_m_computedMagneticVariation_offset() -> int:
    """
    Calls Qt's 'size_t
    QDeclarativePosition::_qt_property_m_computedMagneticVariation_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  size_t QDeclarativePosition::
    #      _qt_property_m_computedMagneticVariation_offset()
    return Rituals.call(
        'ritual_ZN20QDeclarativePosition47_qt_property_m_computedMagneticVa'
        'riation_offsetEv',
    )

  @staticmethod
  def _qt_property_m_computedMagneticVariationValid_offset() -> int:
    """
    Calls Qt's 'size_t QDeclarativePosition::
    _qt_property_m_computedMagneticVariationValid_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  size_t QDeclarativePosition::
    #      _qt_property_m_computedMagneticVariationValid_offset()
    return Rituals.call(
        'ritual_ZN20QDeclarativePosition52_qt_property_m_computedMagneticVa'
        'riationValid_offsetEv',
    )

  @staticmethod
  def _qt_property_m_computedDirectionAccuracy_offset() -> int:
    """
    Calls Qt's 'size_t
    QDeclarativePosition::_qt_property_m_computedDirectionAccuracy_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  size_t QDeclarativePosition::
    #      _qt_property_m_computedDirectionAccuracy_offset()
    return Rituals.call(
        'ritual_ZN20QDeclarativePosition47_qt_property_m_computedDirectionA'
        'ccuracy_offsetEv',
    )

  @staticmethod
  def _qt_property_m_computedDirectionAccuracyValid_offset() -> int:
    """
    Calls Qt's 'size_t QDeclarativePosition::
    _qt_property_m_computedDirectionAccuracyValid_offset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  size_t QDeclarativePosition::
    #      _qt_property_m_computedDirectionAccuracyValid_offset()
    return Rituals.call(
        'ritual_ZN20QDeclarativePosition52_qt_property_m_computedDirectionA'
        'ccuracyValid_offsetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativePosition'

  #  A C++ QDeclarativePosition Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativePosition'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDeclarativePosition::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDeclarativePosition::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isLatitudeValid(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativePosition::isLatitudeValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html#isLatitudeValid
    """
    #  bool QDeclarativePosition::isLatitudeValid() const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition15isLatitudeValidEv',
    )

  def isLongitudeValid(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativePosition::isLongitudeValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html#isLongitudeValid
    """
    #  bool QDeclarativePosition::isLongitudeValid() const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition16isLongitudeValidEv',
    )

  def isAltitudeValid(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativePosition::isAltitudeValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html#isAltitudeValid
    """
    #  bool QDeclarativePosition::isAltitudeValid() const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition15isAltitudeValidEv',
    )

  def timestamp(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDeclarativePosition::timestamp() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html#timestamp

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDeclarativePosition::timestamp() const
    address = self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition9timestampEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def speed(self) -> float:
    """
    Calls Qt's 'double QDeclarativePosition::speed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeposition.html#speed
    """
    #  double QDeclarativePosition::speed() const
    return self.uglySide.call('ritual_ZNK20QDeclarativePosition5speedEv')

  def isSpeedValid(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativePosition::isSpeedValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html#isSpeedValid
    """
    #  bool QDeclarativePosition::isSpeedValid() const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition12isSpeedValidEv',
    )

  def coordinate(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QDeclarativePosition::coordinate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html#coordinate

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QDeclarativePosition::coordinate() const
    address = self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition10coordinateEv',
    )
    from ..QtPositioning import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def isHorizontalAccuracyValid(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativePosition::isHorizontalAccuracyValid()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  bool QDeclarativePosition::isHorizontalAccuracyValid() const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition25isHorizontalAccuracyValidEv',
    )

  def horizontalAccuracy(self) -> float:
    """
    Calls Qt's 'qreal QDeclarativePosition::horizontalAccuracy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html#horizontalAccuracy
    """
    #  qreal QDeclarativePosition::horizontalAccuracy() const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition18horizontalAccuracyEv',
    )

  def isVerticalAccuracyValid(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativePosition::isVerticalAccuracyValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html#isVerticalAccuracyValid
    """
    #  bool QDeclarativePosition::isVerticalAccuracyValid() const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition23isVerticalAccuracyValidEv',
    )

  def verticalAccuracy(self) -> float:
    """
    Calls Qt's 'qreal QDeclarativePosition::verticalAccuracy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html#verticalAccuracy
    """
    #  qreal QDeclarativePosition::verticalAccuracy() const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition16verticalAccuracyEv',
    )

  def isDirectionValid(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativePosition::isDirectionValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html#isDirectionValid
    """
    #  bool QDeclarativePosition::isDirectionValid() const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition16isDirectionValidEv',
    )

  def direction(self) -> float:
    """
    Calls Qt's 'double QDeclarativePosition::direction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html#direction
    """
    #  double QDeclarativePosition::direction() const
    return self.uglySide.call('ritual_ZNK20QDeclarativePosition9directionEv')

  def isVerticalSpeedValid(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativePosition::isVerticalSpeedValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html#isVerticalSpeedValid
    """
    #  bool QDeclarativePosition::isVerticalSpeedValid() const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition20isVerticalSpeedValidEv',
    )

  def verticalSpeed(self) -> float:
    """
    Calls Qt's 'double QDeclarativePosition::verticalSpeed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html#verticalSpeed
    """
    #  double QDeclarativePosition::verticalSpeed() const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition13verticalSpeedEv',
    )

  def isMagneticVariationValid(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativePosition::isMagneticVariationValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html#isMagneticVariationValid
    """
    #  bool QDeclarativePosition::isMagneticVariationValid() const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition24isMagneticVariationValidEv',
    )

  def magneticVariation(self) -> float:
    """
    Calls Qt's 'double QDeclarativePosition::magneticVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html#magneticVariation
    """
    #  double QDeclarativePosition::magneticVariation() const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition17magneticVariationEv',
    )

  def position(self) -> QGeoPositionInfo:
    """
    Calls Qt's 'const QGeoPositionInfo &QDeclarativePosition::position()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeposition.html#position

    Returns
    -------

    QGeoPositionInfo
      A new cute QGeoPositionInfo around the copy Qt gave back. Python owns
      it.
    """
    #  const QGeoPositionInfo &QDeclarativePosition::position() const
    address = self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition8positionEv',
    )
    from ..QtPositioning import QGeoPositionInfo
    return QGeoPositionInfo._cuteOwning(address)

  def isDirectionAccuracyValid(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativePosition::isDirectionAccuracyValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html#isDirectionAccuracyValid
    """
    #  bool QDeclarativePosition::isDirectionAccuracyValid() const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition24isDirectionAccuracyValidEv',
    )

  def directionAccuracy(self) -> float:
    """
    Calls Qt's 'double QDeclarativePosition::directionAccuracy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html#directionAccuracy
    """
    #  double QDeclarativePosition::directionAccuracy() const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition17directionAccuracyEv',
    )

  def isLatitudeValidActualCalculation(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativePosition::isLatitudeValidActualCalculation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  bool QDeclarativePosition::isLatitudeValidActualCalculation() const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition32isLatitudeValidActualCalculation'
        'Ev',
    )

  def isLongitudeValidActualCalculation(self) -> bool:
    """
    Calls Qt's 'bool
    QDeclarativePosition::isLongitudeValidActualCalculation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  bool QDeclarativePosition::isLongitudeValidActualCalculation() const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition33isLongitudeValidActualCalculatio'
        'nEv',
    )

  def isAltitudeValidActualCalculation(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativePosition::isAltitudeValidActualCalculation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  bool QDeclarativePosition::isAltitudeValidActualCalculation() const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition32isAltitudeValidActualCalculation'
        'Ev',
    )

  def coordinateActualCalculation(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate
    QDeclarativePosition::coordinateActualCalculation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QDeclarativePosition::coordinateActualCalculation()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition27coordinateActualCalculationEv',
    )
    from ..QtPositioning import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def timestampActualCalculation(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDeclarativePosition::timestampActualCalculation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDeclarativePosition::timestampActualCalculation() const
    address = self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition26timestampActualCalculationEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def speedActualCalculation(self) -> float:
    """
    Calls Qt's 'double QDeclarativePosition::speedActualCalculation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html#speedActualCalculation
    """
    #  double QDeclarativePosition::speedActualCalculation() const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition22speedActualCalculationEv',
    )

  def isSpeedValidActualCalculation(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativePosition::isSpeedValidActualCalculation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  bool QDeclarativePosition::isSpeedValidActualCalculation() const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition29isSpeedValidActualCalculationEv',
    )

  def horizontalAccuracyActualCalculation(self) -> float:
    """
    Calls Qt's 'qreal
    QDeclarativePosition::horizontalAccuracyActualCalculation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  qreal QDeclarativePosition::horizontalAccuracyActualCalculation()
    #      const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition35horizontalAccuracyActualCalculat'
        'ionEv',
    )

  def verticalAccuracyActualCalculation(self) -> float:
    """
    Calls Qt's 'qreal
    QDeclarativePosition::verticalAccuracyActualCalculation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  qreal QDeclarativePosition::verticalAccuracyActualCalculation() const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition33verticalAccuracyActualCalculatio'
        'nEv',
    )

  def isHorizontalAccuracyValidActualCalculation(self) -> bool:
    """
    Calls Qt's 'bool
    QDeclarativePosition::isHorizontalAccuracyValidActualCalculation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  bool
    #      QDeclarativePosition::isHorizontalAccuracyValidActualCalculation()
    #      const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition42isHorizontalAccuracyValidActualC'
        'alculationEv',
    )

  def isVerticalAccuracyValidActualCalculation(self) -> bool:
    """
    Calls Qt's 'bool
    QDeclarativePosition::isVerticalAccuracyValidActualCalculation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  bool QDeclarativePosition::isVerticalAccuracyValidActualCalculation()
    #      const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition40isVerticalAccuracyValidActualCal'
        'culationEv',
    )

  def isDirectionValidActualCalculation(self) -> bool:
    """
    Calls Qt's 'bool
    QDeclarativePosition::isDirectionValidActualCalculation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  bool QDeclarativePosition::isDirectionValidActualCalculation() const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition33isDirectionValidActualCalculatio'
        'nEv',
    )

  def directionActualCalculation(self) -> float:
    """
    Calls Qt's 'double QDeclarativePosition::directionActualCalculation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  double QDeclarativePosition::directionActualCalculation() const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition26directionActualCalculationEv',
    )

  def isVerticalSpeedValidActualCalculation(self) -> bool:
    """
    Calls Qt's 'bool
    QDeclarativePosition::isVerticalSpeedValidActualCalculation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  bool QDeclarativePosition::isVerticalSpeedValidActualCalculation()
    #      const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition37isVerticalSpeedValidActualCalcul'
        'ationEv',
    )

  def verticalSpeedActualCalculation(self) -> float:
    """
    Calls Qt's 'double QDeclarativePosition::verticalSpeedActualCalculation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  double QDeclarativePosition::verticalSpeedActualCalculation() const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition30verticalSpeedActualCalculationEv',
    )

  def magneticVariationActualCalculation(self) -> float:
    """
    Calls Qt's 'double
    QDeclarativePosition::magneticVariationActualCalculation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  double QDeclarativePosition::magneticVariationActualCalculation()
    #      const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition34magneticVariationActualCalculati'
        'onEv',
    )

  def isMagneticVariationValidActualCalculation(self) -> bool:
    """
    Calls Qt's 'bool
    QDeclarativePosition::isMagneticVariationValidActualCalculation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  bool QDeclarativePosition::isMagneticVariationValidActualCalculation()
    #      const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition41isMagneticVariationValidActualCa'
        'lculationEv',
    )

  def directionAccuracyActualCalculation(self) -> float:
    """
    Calls Qt's 'double
    QDeclarativePosition::directionAccuracyActualCalculation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  double QDeclarativePosition::directionAccuracyActualCalculation()
    #      const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition34directionAccuracyActualCalculati'
        'onEv',
    )

  def isDirectionAccuracyValidActualCalculation(self) -> bool:
    """
    Calls Qt's 'bool
    QDeclarativePosition::isDirectionAccuracyValidActualCalculation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html
    """
    #  bool QDeclarativePosition::isDirectionAccuracyValidActualCalculation()
    #      const
    return self.uglySide.call(
        'ritual_ZNK20QDeclarativePosition41isDirectionAccuracyValidActualCa'
        'lculationEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGeoPositionInfo)
  def setPosition(self, info: QGeoPositionInfo) -> None:
    """
    Calls Qt's 'void QDeclarativePosition::setPosition(const QGeoPositionInfo
    &info)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html#setPosition

    Parameters
    ----------

    info : QGeoPositionInfo
      Passed on as a value: Qt reads the C++ QGeoPositionInfo, which stays
      Python's own.
    """
    #  void QDeclarativePosition::setPosition(const QGeoPositionInfo &info)
    self.uglySide.call(
        'ritual_ZN20QDeclarativePosition11setPositionERK16QGeoPositionInfo',
        self._valueOf(info),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QDeclarativePosition::QDeclarativePosition(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeposition.html#QDeclarativePosition

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativePosition::QDeclarativePosition(QObject *parent)
    self._noteCreation(QDeclarativePosition, lambda: Rituals.call(
        'ritual_ZN20QDeclarativePositionC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @staticmethod
  def binableVerticalAccuracy(*__, **_) -> Never:
    """
    Qt's 'QBindable<qreal> QDeclarativePosition::binableVerticalAccuracy()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativePosition.binableVerticalAccuracy' has no cute "
        "function yet. Qt's 'QBindable<qreal> "
        "QDeclarativePosition::binableVerticalAccuracy() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def bindableAltitudeValid(*__, **_) -> Never:
    """
    Qt's 'QBindable<bool> QDeclarativePosition::bindableAltitudeValid()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativePosition.bindableAltitudeValid' has no cute function "
        "yet. Qt's 'QBindable<bool> "
        "QDeclarativePosition::bindableAltitudeValid() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def bindableCoordinate(*__, **_) -> Never:
    """
    Qt's 'QBindable<QGeoCoordinate>
    QDeclarativePosition::bindableCoordinate() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativePosition.bindableCoordinate' has no cute function "
        "yet. Qt's 'QBindable<QGeoCoordinate> "
        "QDeclarativePosition::bindableCoordinate() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def bindableDirection(*__, **_) -> Never:
    """
    Qt's 'QBindable<double> QDeclarativePosition::bindableDirection() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativePosition.bindableDirection' has no cute function yet. "
        "Qt's 'QBindable<double> QDeclarativePosition::bindableDirection() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def bindableDirectionAccuracy(*__, **_) -> Never:
    """
    Qt's 'QBindable<double> QDeclarativePosition::bindableDirectionAccuracy()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativePosition.bindableDirectionAccuracy' has no cute "
        "function yet. Qt's 'QBindable<double> "
        "QDeclarativePosition::bindableDirectionAccuracy() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def bindableDirectionAccuracyValid(*__, **_) -> Never:
    """
    Qt's 'QBindable<bool>
    QDeclarativePosition::bindableDirectionAccuracyValid() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativePosition.bindableDirectionAccuracyValid' has no cute "
        "function yet. Qt's 'QBindable<bool> "
        "QDeclarativePosition::bindableDirectionAccuracyValid() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def bindableDirectionValid(*__, **_) -> Never:
    """
    Qt's 'QBindable<bool> QDeclarativePosition::bindableDirectionValid()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativePosition.bindableDirectionValid' has no cute function "
        "yet. Qt's 'QBindable<bool> "
        "QDeclarativePosition::bindableDirectionValid() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def bindableHorizontalAccuracy(*__, **_) -> Never:
    """
    Qt's 'QBindable<qreal> QDeclarativePosition::bindableHorizontalAccuracy()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativePosition.bindableHorizontalAccuracy' has no cute "
        "function yet. Qt's 'QBindable<qreal> "
        "QDeclarativePosition::bindableHorizontalAccuracy() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def bindableHorizontalAccuracyValid(*__, **_) -> Never:
    """
    Qt's 'QBindable<bool>
    QDeclarativePosition::bindableHorizontalAccuracyValid() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativePosition.bindableHorizontalAccuracyValid' has no cute "
        "function yet. Qt's 'QBindable<bool> "
        "QDeclarativePosition::bindableHorizontalAccuracyValid() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def bindableLatitudeValid(*__, **_) -> Never:
    """
    Qt's 'QBindable<bool> QDeclarativePosition::bindableLatitudeValid()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativePosition.bindableLatitudeValid' has no cute function "
        "yet. Qt's 'QBindable<bool> "
        "QDeclarativePosition::bindableLatitudeValid() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def bindableLongitudeValid(*__, **_) -> Never:
    """
    Qt's 'QBindable<bool> QDeclarativePosition::bindableLongitudeValid()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativePosition.bindableLongitudeValid' has no cute function "
        "yet. Qt's 'QBindable<bool> "
        "QDeclarativePosition::bindableLongitudeValid() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def bindableMagneticVariation(*__, **_) -> Never:
    """
    Qt's 'QBindable<double> QDeclarativePosition::bindableMagneticVariation()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativePosition.bindableMagneticVariation' has no cute "
        "function yet. Qt's 'QBindable<double> "
        "QDeclarativePosition::bindableMagneticVariation() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def bindableMagneticVariationValid(*__, **_) -> Never:
    """
    Qt's 'QBindable<bool>
    QDeclarativePosition::bindableMagneticVariationValid() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativePosition.bindableMagneticVariationValid' has no cute "
        "function yet. Qt's 'QBindable<bool> "
        "QDeclarativePosition::bindableMagneticVariationValid() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def bindableSpeed(*__, **_) -> Never:
    """
    Qt's 'QBindable<double> QDeclarativePosition::bindableSpeed() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativePosition.bindableSpeed' has no cute function yet. "
        "Qt's 'QBindable<double> QDeclarativePosition::bindableSpeed() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def bindableSpeedValid(*__, **_) -> Never:
    """
    Qt's 'QBindable<bool> QDeclarativePosition::bindableSpeedValid() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativePosition.bindableSpeedValid' has no cute function "
        "yet. Qt's 'QBindable<bool> "
        "QDeclarativePosition::bindableSpeedValid() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def bindableTimestamp(*__, **_) -> Never:
    """
    Qt's 'QBindable<QDateTime> QDeclarativePosition::bindableTimestamp()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativePosition.bindableTimestamp' has no cute function yet. "
        "Qt's 'QBindable<QDateTime> "
        "QDeclarativePosition::bindableTimestamp() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def bindableVerticalAccuracyValid(*__, **_) -> Never:
    """
    Qt's 'QBindable<bool>
    QDeclarativePosition::bindableVerticalAccuracyValid() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativePosition.bindableVerticalAccuracyValid' has no cute "
        "function yet. Qt's 'QBindable<bool> "
        "QDeclarativePosition::bindableVerticalAccuracyValid() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def bindableVerticalSpeed(*__, **_) -> Never:
    """
    Qt's 'QBindable<double> QDeclarativePosition::bindableVerticalSpeed()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativePosition.bindableVerticalSpeed' has no cute function "
        "yet. Qt's 'QBindable<double> "
        "QDeclarativePosition::bindableVerticalSpeed() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def bindableVerticalSpeedValid(*__, **_) -> Never:
    """
    Qt's 'QBindable<bool> QDeclarativePosition::bindableVerticalSpeedValid()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDeclarativePosition.bindableVerticalSpeedValid' has no cute "
        "function yet. Qt's 'QBindable<bool> "
        "QDeclarativePosition::bindableVerticalSpeedValid() const': gives a "
        "type Python has no way to take yet.")
