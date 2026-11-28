"""
QGeoCameraData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeocameradata_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoCameraData to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtPositioning import QGeoCoordinate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCoordinate = WAIT['QGeoCoordinate']


class QGeoCameraData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGeoCameraData: a plain Python object standing in
  front of one C++ QGeoCameraData.

  C++ hands a QGeoCameraData around as a copy, so every C++ QGeoCameraData
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoCameraData that has a ritual and that Python can
  call so far, 15 names in all: '__eq__', '__ne__', 'setCenter', 'center',
  'setBearing', 'bearing', 'setTilt', 'tilt', 'setRoll', 'roll',
  'setFieldOfView', 'fieldOfView', 'setZoomLevel', 'zoomLevel', 'isEqual'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoCameraData::QGeoCameraData(QGeoCameraData &&other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QGeoCameraData::~QGeoCameraData()': the destructor: Python removes
    its C++ QGeoCameraData by it, and has no other use for it.
  - Qt's 'QGeoCameraData &QGeoCameraData::operator=(const QGeoCameraData
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QGeoCameraData &QGeoCameraData::operator=(QGeoCameraData &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QGeoCameraData::swap(QGeoCameraData &other)': takes a type
    Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QGeoCameraData is created at the first use, not by
    'QGeoCameraData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoCameraData back gives a copy the ritual made for
    Python, in a new cute QGeoCameraData.
  - Each name of Qt's QGeoCameraData that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoCameraData'

  #  Qt's '~QGeoCameraData()'. Naming it makes this a value class: Python
  #  owns every C++ QGeoCameraData behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QGeoCameraDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def center(self) -> QGeoCoordinate:
    """
    Calls Qt's 'QGeoCoordinate QGeoCameraData::center() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocameradata.html#center

    Returns
    -------

    QGeoCoordinate
      A new cute QGeoCoordinate around the copy Qt gave back. Python owns it.
    """
    #  QGeoCoordinate QGeoCameraData::center() const
    address = self.uglySide.call('ritual_ZNK14QGeoCameraData6centerEv')
    from ..QtPositioning import QGeoCoordinate
    return QGeoCoordinate._cuteOwning(address)

  def bearing(self) -> float:
    """
    Calls Qt's 'double QGeoCameraData::bearing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocameradata.html#bearing
    """
    #  double QGeoCameraData::bearing() const
    return self.uglySide.call('ritual_ZNK14QGeoCameraData7bearingEv')

  def tilt(self) -> float:
    """
    Calls Qt's 'double QGeoCameraData::tilt() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocameradata.html#tilt
    """
    #  double QGeoCameraData::tilt() const
    return self.uglySide.call('ritual_ZNK14QGeoCameraData4tiltEv')

  def roll(self) -> float:
    """
    Calls Qt's 'double QGeoCameraData::roll() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocameradata.html#roll
    """
    #  double QGeoCameraData::roll() const
    return self.uglySide.call('ritual_ZNK14QGeoCameraData4rollEv')

  def fieldOfView(self) -> float:
    """
    Calls Qt's 'double QGeoCameraData::fieldOfView() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocameradata.html#fieldOfView
    """
    #  double QGeoCameraData::fieldOfView() const
    return self.uglySide.call('ritual_ZNK14QGeoCameraData11fieldOfViewEv')

  def zoomLevel(self) -> float:
    """
    Calls Qt's 'double QGeoCameraData::zoomLevel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocameradata.html#zoomLevel
    """
    #  double QGeoCameraData::zoomLevel() const
    return self.uglySide.call('ritual_ZNK14QGeoCameraData9zoomLevelEv')

  @overload(THIS)
  def isEqual(self, other: QGeoCameraData) -> bool:
    """
    Calls Qt's 'bool QGeoCameraData::isEqual(const QGeoCameraData &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocameradata.html#isEqual

    Parameters
    ----------

    other : QGeoCameraData
      Passed on as a value: Qt reads the C++ QGeoCameraData, which stays
      Python's own.
    """
    #  bool QGeoCameraData::isEqual(const QGeoCameraData &other) const
    return self.uglySide.call(
        'ritual_ZNK14QGeoCameraData7isEqualERKS_', self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGeoCoordinate)
  def setCenter(self, coordinate: QGeoCoordinate) -> None:
    """
    Calls Qt's 'void QGeoCameraData::setCenter(const QGeoCoordinate
    &coordinate)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocameradata.html#setCenter

    Parameters
    ----------

    coordinate : QGeoCoordinate
      Passed on as a value: Qt reads the C++ QGeoCoordinate, which stays
      Python's own.
    """
    #  void QGeoCameraData::setCenter(const QGeoCoordinate &coordinate)
    self.uglySide.call(
        'ritual_ZN14QGeoCameraData9setCenterERK14QGeoCoordinate',
        self._valueOf(coordinate),
    )

  @overload(float)
  def setBearing(self, bearing: float) -> None:
    """
    Calls Qt's 'void QGeoCameraData::setBearing(double bearing)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocameradata.html#setBearing

    Parameters
    ----------

    bearing : float
      Passed on as it is.
    """
    #  void QGeoCameraData::setBearing(double bearing)
    self.uglySide.call('ritual_ZN14QGeoCameraData10setBearingEd', bearing)

  @overload(float)
  def setTilt(self, tilt: float) -> None:
    """
    Calls Qt's 'void QGeoCameraData::setTilt(double tilt)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocameradata.html#setTilt

    Parameters
    ----------

    tilt : float
      Passed on as it is.
    """
    #  void QGeoCameraData::setTilt(double tilt)
    self.uglySide.call('ritual_ZN14QGeoCameraData7setTiltEd', tilt)

  @overload(float)
  def setRoll(self, roll: float) -> None:
    """
    Calls Qt's 'void QGeoCameraData::setRoll(double roll)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocameradata.html#setRoll

    Parameters
    ----------

    roll : float
      Passed on as it is.
    """
    #  void QGeoCameraData::setRoll(double roll)
    self.uglySide.call('ritual_ZN14QGeoCameraData7setRollEd', roll)

  @overload(float)
  def setFieldOfView(self, fieldOfView: float) -> None:
    """
    Calls Qt's 'void QGeoCameraData::setFieldOfView(double fieldOfView)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocameradata.html#setFieldOfView

    Parameters
    ----------

    fieldOfView : float
      Passed on as it is.
    """
    #  void QGeoCameraData::setFieldOfView(double fieldOfView)
    self.uglySide.call(
        'ritual_ZN14QGeoCameraData14setFieldOfViewEd', fieldOfView,
    )

  @overload(float)
  def setZoomLevel(self, zoomLevel: float) -> None:
    """
    Calls Qt's 'void QGeoCameraData::setZoomLevel(double zoomLevel)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocameradata.html#setZoomLevel

    Parameters
    ----------

    zoomLevel : float
      Passed on as it is.
    """
    #  void QGeoCameraData::setZoomLevel(double zoomLevel)
    self.uglySide.call(
        'ritual_ZN14QGeoCameraData12setZoomLevelEd', zoomLevel,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QGeoCameraData) -> bool:
    """
    Calls Qt's 'bool operator==(const QGeoCameraData &lhs, const
    QGeoCameraData &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocameradata.html#operator==

    Parameters
    ----------

    rhs : QGeoCameraData
      Passed on as a value: Qt reads the C++ QGeoCameraData, which stays
      Python's own.
    """
    #  bool operator==(const QGeoCameraData &lhs, const QGeoCameraData &rhs)
    return Rituals.call(
        'ritual_ZeqRK14QGeoCameraDataS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QGeoCameraData) -> bool:
    """
    Calls Qt's 'bool operator!=(const QGeoCameraData &lhs, const
    QGeoCameraData &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgeocameradata.html#operator!=

    Parameters
    ----------

    rhs : QGeoCameraData
      Passed on as a value: Qt reads the C++ QGeoCameraData, which stays
      Python's own.
    """
    #  bool operator!=(const QGeoCameraData &lhs, const QGeoCameraData &rhs)
    return Rituals.call(
        'ritual_ZneRK14QGeoCameraDataS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QGeoCameraData::QGeoCameraData()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeocameradata.html#QGeoCameraData
    """
    #  QGeoCameraData::QGeoCameraData()
    self._noteCreation(QGeoCameraData, lambda: Rituals.call(
        'ritual_ZN14QGeoCameraDataC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QGeoCameraData) -> None:
    """
    Notes what was given, for Qt's 'QGeoCameraData::QGeoCameraData(const
    QGeoCameraData &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgeocameradata.html#QGeoCameraData

    Parameters
    ----------

    other : QGeoCameraData
      Passed on as a value: Qt reads the C++ QGeoCameraData, which stays
      Python's own.
    """
    #  QGeoCameraData::QGeoCameraData(const QGeoCameraData &other)
    self._noteCreation(QGeoCameraData, lambda: Rituals.call(
        'ritual_ZN14QGeoCameraDataC1ERKS_', self._valueOf(other),
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
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QGeoCameraData::swap(QGeoCameraData &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoCameraData.swap' has no cute function yet. Qt's 'void "
        "QGeoCameraData::swap(QGeoCameraData &other)': takes a type Python "
        "has no way to hand over yet.")
