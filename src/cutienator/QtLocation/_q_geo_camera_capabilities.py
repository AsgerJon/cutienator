"""
QGeoCameraCapabilities binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeocameracapabilities_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QGeoCameraCapabilities to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QGeoCameraCapabilities(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGeoCameraCapabilities: a plain Python object
  standing in front of one C++ QGeoCameraCapabilities.

  C++ hands a QGeoCameraCapabilities around as a copy, so every C++
  QGeoCameraCapabilities behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGeoCameraCapabilities that has a ritual and that
  Python can call so far, 28 names in all: '__eq__', '__ne__', 'setTileSize',
  'tileSize', 'setMinimumZoomLevel', 'minimumZoomLevel',
  'minimumZoomLevelAt256', 'setMaximumZoomLevel', 'maximumZoomLevel',
  'maximumZoomLevelAt256', 'setSupportsBearing', 'supportsBearing',
  'setSupportsRolling', 'supportsRolling', 'setSupportsTilting',
  'supportsTilting', 'setMinimumTilt', 'minimumTilt', 'setMaximumTilt',
  'maximumTilt', 'setMinimumFieldOfView', 'minimumFieldOfView',
  'setMaximumFieldOfView', 'maximumFieldOfView', 'setOverzoomEnabled',
  'overzoomEnabled', 'isValid', 'isEqual'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QGeoCameraCapabilities::QGeoCameraCapabilities(QGeoCameraCapabilities
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QGeoCameraCapabilities::~QGeoCameraCapabilities()': the destructor:
    Python removes its C++ QGeoCameraCapabilities by it, and has no other use
    for it.
  - Qt's 'QGeoCameraCapabilities &QGeoCameraCapabilities::operator=(const
    QGeoCameraCapabilities &other)': assignment: Python binds a name and has
    no operator for it.
  - Qt's 'QGeoCameraCapabilities
    &QGeoCameraCapabilities::operator=(QGeoCameraCapabilities &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QGeoCameraCapabilities::swap(QGeoCameraCapabilities &other)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 38 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QGeoCameraCapabilities is created at the first use, not by
    'QGeoCameraCapabilities(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGeoCameraCapabilities back gives a copy the ritual
    made for Python, in a new cute QGeoCameraCapabilities.
  - Each name of Qt's QGeoCameraCapabilities that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoCameraCapabilities'

  #  Qt's '~QGeoCameraCapabilities()'. Naming it makes this a value class:
  #  Python owns every C++ QGeoCameraCapabilities behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QGeoCameraCapabilitiesD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def tileSize(self) -> int:
    """
    Calls Qt's 'int QGeoCameraCapabilities::tileSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#tileSize
    """
    #  int QGeoCameraCapabilities::tileSize() const
    return self.uglySide.call(
        'ritual_ZNK22QGeoCameraCapabilities8tileSizeEv',
    )

  def minimumZoomLevel(self) -> float:
    """
    Calls Qt's 'double QGeoCameraCapabilities::minimumZoomLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#minimumZoomLevel
    """
    #  double QGeoCameraCapabilities::minimumZoomLevel() const
    return self.uglySide.call(
        'ritual_ZNK22QGeoCameraCapabilities16minimumZoomLevelEv',
    )

  def minimumZoomLevelAt256(self) -> float:
    """
    Calls Qt's 'double QGeoCameraCapabilities::minimumZoomLevelAt256()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#minimumZoomLevelAt256
    """
    #  double QGeoCameraCapabilities::minimumZoomLevelAt256() const
    return self.uglySide.call(
        'ritual_ZNK22QGeoCameraCapabilities21minimumZoomLevelAt256Ev',
    )

  def maximumZoomLevel(self) -> float:
    """
    Calls Qt's 'double QGeoCameraCapabilities::maximumZoomLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#maximumZoomLevel
    """
    #  double QGeoCameraCapabilities::maximumZoomLevel() const
    return self.uglySide.call(
        'ritual_ZNK22QGeoCameraCapabilities16maximumZoomLevelEv',
    )

  def maximumZoomLevelAt256(self) -> float:
    """
    Calls Qt's 'double QGeoCameraCapabilities::maximumZoomLevelAt256()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#maximumZoomLevelAt256
    """
    #  double QGeoCameraCapabilities::maximumZoomLevelAt256() const
    return self.uglySide.call(
        'ritual_ZNK22QGeoCameraCapabilities21maximumZoomLevelAt256Ev',
    )

  def supportsBearing(self) -> bool:
    """
    Calls Qt's 'bool QGeoCameraCapabilities::supportsBearing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#supportsBearing
    """
    #  bool QGeoCameraCapabilities::supportsBearing() const
    return self.uglySide.call(
        'ritual_ZNK22QGeoCameraCapabilities15supportsBearingEv',
    )

  def supportsRolling(self) -> bool:
    """
    Calls Qt's 'bool QGeoCameraCapabilities::supportsRolling() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#supportsRolling
    """
    #  bool QGeoCameraCapabilities::supportsRolling() const
    return self.uglySide.call(
        'ritual_ZNK22QGeoCameraCapabilities15supportsRollingEv',
    )

  def supportsTilting(self) -> bool:
    """
    Calls Qt's 'bool QGeoCameraCapabilities::supportsTilting() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#supportsTilting
    """
    #  bool QGeoCameraCapabilities::supportsTilting() const
    return self.uglySide.call(
        'ritual_ZNK22QGeoCameraCapabilities15supportsTiltingEv',
    )

  def minimumTilt(self) -> float:
    """
    Calls Qt's 'double QGeoCameraCapabilities::minimumTilt() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#minimumTilt
    """
    #  double QGeoCameraCapabilities::minimumTilt() const
    return self.uglySide.call(
        'ritual_ZNK22QGeoCameraCapabilities11minimumTiltEv',
    )

  def maximumTilt(self) -> float:
    """
    Calls Qt's 'double QGeoCameraCapabilities::maximumTilt() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#maximumTilt
    """
    #  double QGeoCameraCapabilities::maximumTilt() const
    return self.uglySide.call(
        'ritual_ZNK22QGeoCameraCapabilities11maximumTiltEv',
    )

  def minimumFieldOfView(self) -> float:
    """
    Calls Qt's 'double QGeoCameraCapabilities::minimumFieldOfView() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#minimumFieldOfView
    """
    #  double QGeoCameraCapabilities::minimumFieldOfView() const
    return self.uglySide.call(
        'ritual_ZNK22QGeoCameraCapabilities18minimumFieldOfViewEv',
    )

  def maximumFieldOfView(self) -> float:
    """
    Calls Qt's 'double QGeoCameraCapabilities::maximumFieldOfView() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#maximumFieldOfView
    """
    #  double QGeoCameraCapabilities::maximumFieldOfView() const
    return self.uglySide.call(
        'ritual_ZNK22QGeoCameraCapabilities18maximumFieldOfViewEv',
    )

  def overzoomEnabled(self) -> bool:
    """
    Calls Qt's 'bool QGeoCameraCapabilities::overzoomEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#overzoomEnabled
    """
    #  bool QGeoCameraCapabilities::overzoomEnabled() const
    return self.uglySide.call(
        'ritual_ZNK22QGeoCameraCapabilities15overzoomEnabledEv',
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QGeoCameraCapabilities::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#isValid
    """
    #  bool QGeoCameraCapabilities::isValid() const
    return self.uglySide.call('ritual_ZNK22QGeoCameraCapabilities7isValidEv')

  @overload(THIS)
  def isEqual(self, other: QGeoCameraCapabilities) -> bool:
    """
    Calls Qt's 'bool QGeoCameraCapabilities::isEqual(const
    QGeoCameraCapabilities &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#isEqual

    Parameters
    ----------

    other : QGeoCameraCapabilities
      Passed on as a value: Qt reads the C++ QGeoCameraCapabilities, which
      stays Python's own.
    """
    #  bool QGeoCameraCapabilities::isEqual(const QGeoCameraCapabilities
    #      &other) const
    return self.uglySide.call(
        'ritual_ZNK22QGeoCameraCapabilities7isEqualERKS_',
        self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setTileSize(self, tileSize: int) -> None:
    """
    Calls Qt's 'void QGeoCameraCapabilities::setTileSize(int tileSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#setTileSize

    Parameters
    ----------

    tileSize : int
      Passed on as it is.
    """
    #  void QGeoCameraCapabilities::setTileSize(int tileSize)
    self.uglySide.call(
        'ritual_ZN22QGeoCameraCapabilities11setTileSizeEi', tileSize,
    )

  @overload(float)
  def setMinimumZoomLevel(self, minimumZoomLevel: float) -> None:
    """
    Calls Qt's 'void QGeoCameraCapabilities::setMinimumZoomLevel(double
    minimumZoomLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#setMinimumZoomLevel

    Parameters
    ----------

    minimumZoomLevel : float
      Passed on as it is.
    """
    #  void QGeoCameraCapabilities::setMinimumZoomLevel(double
    #      minimumZoomLevel)
    self.uglySide.call(
        'ritual_ZN22QGeoCameraCapabilities19setMinimumZoomLevelEd',
        minimumZoomLevel,
    )

  @overload(float)
  def setMaximumZoomLevel(self, maximumZoomLevel: float) -> None:
    """
    Calls Qt's 'void QGeoCameraCapabilities::setMaximumZoomLevel(double
    maximumZoomLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#setMaximumZoomLevel

    Parameters
    ----------

    maximumZoomLevel : float
      Passed on as it is.
    """
    #  void QGeoCameraCapabilities::setMaximumZoomLevel(double
    #      maximumZoomLevel)
    self.uglySide.call(
        'ritual_ZN22QGeoCameraCapabilities19setMaximumZoomLevelEd',
        maximumZoomLevel,
    )

  @overload(bool)
  def setSupportsBearing(self, supportsBearing: bool) -> None:
    """
    Calls Qt's 'void QGeoCameraCapabilities::setSupportsBearing(bool
    supportsBearing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#setSupportsBearing

    Parameters
    ----------

    supportsBearing : bool
      Passed on as it is.
    """
    #  void QGeoCameraCapabilities::setSupportsBearing(bool supportsBearing)
    self.uglySide.call(
        'ritual_ZN22QGeoCameraCapabilities18setSupportsBearingEb',
        supportsBearing,
    )

  @overload(bool)
  def setSupportsRolling(self, supportsRolling: bool) -> None:
    """
    Calls Qt's 'void QGeoCameraCapabilities::setSupportsRolling(bool
    supportsRolling)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#setSupportsRolling

    Parameters
    ----------

    supportsRolling : bool
      Passed on as it is.
    """
    #  void QGeoCameraCapabilities::setSupportsRolling(bool supportsRolling)
    self.uglySide.call(
        'ritual_ZN22QGeoCameraCapabilities18setSupportsRollingEb',
        supportsRolling,
    )

  @overload(bool)
  def setSupportsTilting(self, supportsTilting: bool) -> None:
    """
    Calls Qt's 'void QGeoCameraCapabilities::setSupportsTilting(bool
    supportsTilting)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#setSupportsTilting

    Parameters
    ----------

    supportsTilting : bool
      Passed on as it is.
    """
    #  void QGeoCameraCapabilities::setSupportsTilting(bool supportsTilting)
    self.uglySide.call(
        'ritual_ZN22QGeoCameraCapabilities18setSupportsTiltingEb',
        supportsTilting,
    )

  @overload(float)
  def setMinimumTilt(self, minimumTilt: float) -> None:
    """
    Calls Qt's 'void QGeoCameraCapabilities::setMinimumTilt(double
    minimumTilt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#setMinimumTilt

    Parameters
    ----------

    minimumTilt : float
      Passed on as it is.
    """
    #  void QGeoCameraCapabilities::setMinimumTilt(double minimumTilt)
    self.uglySide.call(
        'ritual_ZN22QGeoCameraCapabilities14setMinimumTiltEd', minimumTilt,
    )

  @overload(float)
  def setMaximumTilt(self, maximumTilt: float) -> None:
    """
    Calls Qt's 'void QGeoCameraCapabilities::setMaximumTilt(double
    maximumTilt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#setMaximumTilt

    Parameters
    ----------

    maximumTilt : float
      Passed on as it is.
    """
    #  void QGeoCameraCapabilities::setMaximumTilt(double maximumTilt)
    self.uglySide.call(
        'ritual_ZN22QGeoCameraCapabilities14setMaximumTiltEd', maximumTilt,
    )

  @overload(float)
  def setMinimumFieldOfView(self, minimumFieldOfView: float) -> None:
    """
    Calls Qt's 'void QGeoCameraCapabilities::setMinimumFieldOfView(double
    minimumFieldOfView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#setMinimumFieldOfView

    Parameters
    ----------

    minimumFieldOfView : float
      Passed on as it is.
    """
    #  void QGeoCameraCapabilities::setMinimumFieldOfView(double
    #      minimumFieldOfView)
    self.uglySide.call(
        'ritual_ZN22QGeoCameraCapabilities21setMinimumFieldOfViewEd',
        minimumFieldOfView,
    )

  @overload(float)
  def setMaximumFieldOfView(self, maximumFieldOfView: float) -> None:
    """
    Calls Qt's 'void QGeoCameraCapabilities::setMaximumFieldOfView(double
    maximumFieldOfView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#setMaximumFieldOfView

    Parameters
    ----------

    maximumFieldOfView : float
      Passed on as it is.
    """
    #  void QGeoCameraCapabilities::setMaximumFieldOfView(double
    #      maximumFieldOfView)
    self.uglySide.call(
        'ritual_ZN22QGeoCameraCapabilities21setMaximumFieldOfViewEd',
        maximumFieldOfView,
    )

  @overload(bool)
  def setOverzoomEnabled(self, overzoomEnabled: bool) -> None:
    """
    Calls Qt's 'void QGeoCameraCapabilities::setOverzoomEnabled(bool
    overzoomEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#setOverzoomEnabled

    Parameters
    ----------

    overzoomEnabled : bool
      Passed on as it is.
    """
    #  void QGeoCameraCapabilities::setOverzoomEnabled(bool overzoomEnabled)
    self.uglySide.call(
        'ritual_ZN22QGeoCameraCapabilities18setOverzoomEnabledEb',
        overzoomEnabled,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QGeoCameraCapabilities) -> bool:
    """
    Calls Qt's 'bool operator==(const QGeoCameraCapabilities &lhs, const
    QGeoCameraCapabilities &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#operator==

    Parameters
    ----------

    rhs : QGeoCameraCapabilities
      Passed on as a value: Qt reads the C++ QGeoCameraCapabilities, which
      stays Python's own.
    """
    #  bool operator==(const QGeoCameraCapabilities &lhs, const
    #      QGeoCameraCapabilities &rhs)
    return Rituals.call(
        'ritual_ZeqRK22QGeoCameraCapabilitiesS1_',
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
  def __ne__(self, rhs: QGeoCameraCapabilities) -> bool:
    """
    Calls Qt's 'bool operator!=(const QGeoCameraCapabilities &lhs, const
    QGeoCameraCapabilities &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#operator!=

    Parameters
    ----------

    rhs : QGeoCameraCapabilities
      Passed on as a value: Qt reads the C++ QGeoCameraCapabilities, which
      stays Python's own.
    """
    #  bool operator!=(const QGeoCameraCapabilities &lhs, const
    #      QGeoCameraCapabilities &rhs)
    return Rituals.call(
        'ritual_ZneRK22QGeoCameraCapabilitiesS1_',
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
    Notes what was given, for Qt's
    'QGeoCameraCapabilities::QGeoCameraCapabilities()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#QGeoCameraCapabilities
    """
    #  QGeoCameraCapabilities::QGeoCameraCapabilities()
    self._noteCreation(QGeoCameraCapabilities, lambda: Rituals.call(
        'ritual_ZN22QGeoCameraCapabilitiesC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QGeoCameraCapabilities) -> None:
    """
    Notes what was given, for Qt's
    'QGeoCameraCapabilities::QGeoCameraCapabilities(const
    QGeoCameraCapabilities &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeocameracapabilities.html#QGeoCameraCapabilities

    Parameters
    ----------

    other : QGeoCameraCapabilities
      Passed on as a value: Qt reads the C++ QGeoCameraCapabilities, which
      stays Python's own.
    """
    #  QGeoCameraCapabilities::QGeoCameraCapabilities(const
    #      QGeoCameraCapabilities &other)
    self._noteCreation(QGeoCameraCapabilities, lambda: Rituals.call(
        'ritual_ZN22QGeoCameraCapabilitiesC1ERKS_', self._valueOf(other),
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
    Qt's 'void QGeoCameraCapabilities::swap(QGeoCameraCapabilities &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGeoCameraCapabilities.swap' has no cute function yet. Qt's 'void "
        "QGeoCameraCapabilities::swap(QGeoCameraCapabilities &other)': "
        "takes a type Python has no way to hand over yet.")
