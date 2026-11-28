"""
QScrollerProperties binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qscrollerproperties.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']


class QScrollerProperties(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QScrollerProperties: a plain Python object standing
  in front of one C++ QScrollerProperties.

  C++ hands a QScrollerProperties around as a copy, so every C++
  QScrollerProperties behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QScrollerProperties that has a ritual and that
  Python can call so far, 6 names in all: '__eq__', '__ne__',
  'setDefaultScrollerProperties', 'unsetDefaultScrollerProperties',
  'scrollMetric', 'setScrollMetric'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QScrollerProperties &QScrollerProperties::operator=(const
    QScrollerProperties &sp)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QScrollerProperties::~QScrollerProperties()': the destructor:
    Python removes its C++ QScrollerProperties by it, and has no other use
    for it.
  - Qt's 'QScrollerProperties::QScrollerProperties(QScrollerPropertiesPrivate
    &dd)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QScrollerProperties is created at the first use, not by
    'QScrollerProperties(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QScrollerProperties back gives a copy the ritual made
    for Python, in a new cute QScrollerProperties.
  """

  #  The enums Qt writes inside QScrollerProperties, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class FrameRates(CuteNum):
    """
    The enum 'QScrollerProperties::FrameRates' of Qt, with the 4 names Qt
    gives in it.
    """

    Standard = Kee[int](0)
    Fps60 = Kee[int](1)
    Fps30 = Kee[int](2)
    Fps20 = Kee[int](3)

  class OvershootPolicy(CuteNum):
    """
    The enum 'QScrollerProperties::OvershootPolicy' of Qt, with the 3 names
    Qt gives in it.
    """

    OvershootWhenScrollable = Kee[int](0)
    OvershootAlwaysOff = Kee[int](1)
    OvershootAlwaysOn = Kee[int](2)

  class ScrollMetric(CuteNum):
    """
    The enum 'QScrollerProperties::ScrollMetric' of Qt, with the 21 names Qt
    gives in it.
    """

    MousePressEventDelay = Kee[int](0)
    DragStartDistance = Kee[int](1)
    DragVelocitySmoothingFactor = Kee[int](2)
    AxisLockThreshold = Kee[int](3)
    ScrollingCurve = Kee[int](4)
    DecelerationFactor = Kee[int](5)
    MinimumVelocity = Kee[int](6)
    MaximumVelocity = Kee[int](7)
    MaximumClickThroughVelocity = Kee[int](8)
    AcceleratingFlickMaximumTime = Kee[int](9)
    AcceleratingFlickSpeedupFactor = Kee[int](10)
    SnapPositionRatio = Kee[int](11)
    SnapTime = Kee[int](12)
    OvershootDragResistanceFactor = Kee[int](13)
    OvershootDragDistanceFactor = Kee[int](14)
    OvershootScrollDistanceFactor = Kee[int](15)
    OvershootScrollTime = Kee[int](16)
    HorizontalOvershootPolicy = Kee[int](17)
    VerticalOvershootPolicy = Kee[int](18)
    FrameRate = Kee[int](19)
    ScrollMetricCount = Kee[int](20)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS)
  def setDefaultScrollerProperties(sp: QScrollerProperties) -> None:
    """
    Calls Qt's 'void QScrollerProperties::setDefaultScrollerProperties(const
    QScrollerProperties &sp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollerproperties.html

    Parameters
    ----------

    sp : QScrollerProperties
      Passed on as a value: Qt reads the C++ QScrollerProperties, which stays
      Python's own.
    """
    #  void QScrollerProperties::setDefaultScrollerProperties(const
    #      QScrollerProperties &sp)
    Rituals.call(
        'ritual_ZN19QScrollerProperties28setDefaultScrollerPropertiesERKS_',
        CuteMixin._valueOf(sp),
    )

  @staticmethod
  def unsetDefaultScrollerProperties() -> None:
    """
    Calls Qt's 'void QScrollerProperties::unsetDefaultScrollerProperties()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollerproperties.html
    """
    #  void QScrollerProperties::unsetDefaultScrollerProperties()
    Rituals.call(
        'ritual_ZN19QScrollerProperties30unsetDefaultScrollerPropertiesEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScrollerProperties'

  #  Qt's '~QScrollerProperties()'. Naming it makes this a value class:
  #  Python owns every C++ QScrollerProperties behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QScrollerPropertiesD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(ScrollMetric)
  def scrollMetric(self, metric: ScrollMetric) -> QVariant:
    """
    Calls Qt's 'QVariant QScrollerProperties::scrollMetric(ScrollMetric
    metric) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollerproperties.html#scrollMetric

    Parameters
    ----------

    metric : ScrollMetric
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QScrollerProperties::scrollMetric(ScrollMetric metric) const
    address = self.uglySide.call(
        'ritual_ZNK19QScrollerProperties12scrollMetricENS_12ScrollMetricE',
        metric.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(ScrollMetric, QVariant)
  def setScrollMetric(self, metric: ScrollMetric, value: QVariant) -> None:
    """
    Calls Qt's 'void QScrollerProperties::setScrollMetric(ScrollMetric
    metric, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollerproperties.html#setScrollMetric

    Parameters
    ----------

    metric : ScrollMetric
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QScrollerProperties::setScrollMetric(ScrollMetric metric, const
    #      QVariant &value)
    self.uglySide.call(
        'ritual_ZN19QScrollerProperties15setScrollMetricENS_12ScrollMetricE'
        'RK8QVariant',
        metric.value, self._valueOf(value),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, sp: QScrollerProperties) -> bool:
    """
    Calls Qt's 'bool QScrollerProperties::operator==(const
    QScrollerProperties &sp) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollerproperties.html#operator==

    Parameters
    ----------

    sp : QScrollerProperties
      Passed on as a value: Qt reads the C++ QScrollerProperties, which stays
      Python's own.
    """
    #  bool QScrollerProperties::operator==(const QScrollerProperties &sp)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QScrollerPropertieseqERKS_', self._valueOf(sp),
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
  def __ne__(self, sp: QScrollerProperties) -> bool:
    """
    Calls Qt's 'bool QScrollerProperties::operator!=(const
    QScrollerProperties &sp) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollerproperties.html#operator!=

    Parameters
    ----------

    sp : QScrollerProperties
      Passed on as a value: Qt reads the C++ QScrollerProperties, which stays
      Python's own.
    """
    #  bool QScrollerProperties::operator!=(const QScrollerProperties &sp)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QScrollerPropertiesneERKS_', self._valueOf(sp),
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
    'QScrollerProperties::QScrollerProperties()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollerproperties.html#QScrollerProperties
    """
    #  QScrollerProperties::QScrollerProperties()
    self._noteCreation(QScrollerProperties, lambda: Rituals.call(
        'ritual_ZN19QScrollerPropertiesC1Ev',
    ))

  @overload(THIS)
  def __init__(self, sp: QScrollerProperties) -> None:
    """
    Notes what was given, for Qt's
    'QScrollerProperties::QScrollerProperties(const QScrollerProperties
    &sp)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscrollerproperties.html#QScrollerProperties

    Parameters
    ----------

    sp : QScrollerProperties
      Passed on as a value: Qt reads the C++ QScrollerProperties, which stays
      Python's own.
    """
    #  QScrollerProperties::QScrollerProperties(const QScrollerProperties
    #      &sp)
    self._noteCreation(QScrollerProperties, lambda: Rituals.call(
        'ritual_ZN19QScrollerPropertiesC1ERKS_', self._valueOf(sp),
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
