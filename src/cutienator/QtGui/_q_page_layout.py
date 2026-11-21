"""
QPageLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qpagelayout.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QMargins, QMarginsF, QRect, QRectF
  from . import QPageSize
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMarginsF = WAIT['QMarginsF']
  QPageSize = WAIT['QPageSize']


class QPageLayout(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPageLayout: a plain Python object standing in front
  of one C++ QPageLayout.

  C++ hands a QPageLayout around as a copy, so every C++ QPageLayout behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPageLayout that has a ritual and that Python can
  call so far, 27 names in all: 'isEquivalentTo', 'isValid', 'setMode',
  'mode', 'setPageSize', 'pageSize', 'setOrientation', 'orientation',
  'setUnits', 'units', 'setMargins', 'setLeftMargin', 'setRightMargin',
  'setTopMargin', 'setBottomMargin', 'margins', 'marginsPoints',
  'marginsPixels', 'setMinimumMargins', 'minimumMargins', 'maximumMargins',
  'fullRect', 'fullRectPoints', 'fullRectPixels', 'paintRect',
  'paintRectPoints', 'paintRectPixels'. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPageLayout::~QPageLayout()': the destructor: Python removes its
    C++ QPageLayout by it, and has no other use for it.

  What has no ritual
  ------------------

  4 of the 38 functions Qt declares: 3 takes or gives a type that cannot be
  passed yet; 1 private.

  What to expect
  --------------

  - The C++ QPageLayout is created at the first use, not by
    'QPageLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPageLayout back gives a copy the ritual made for
    Python, in a new cute QPageLayout.
  """

  #  The enums Qt writes inside QPageLayout, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Mode(CuteNum):
    """
    The enum 'QPageLayout::Mode' of Qt, with the 2 names Qt gives in it.
    """

    StandardMode = Kee[int](0)
    FullPageMode = Kee[int](1)

  class Orientation(CuteNum):
    """
    The enum 'QPageLayout::Orientation' of Qt, with the 2 names Qt gives in
    it.
    """

    Portrait = Kee[int](0)
    Landscape = Kee[int](1)

  class OutOfBoundsPolicy(CuteNum, scoped=True):
    """
    The enum 'QPageLayout::OutOfBoundsPolicy' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Reject = Kee[int](0)
    Clamp = Kee[int](1)

  class Unit(CuteNum):
    """
    The enum 'QPageLayout::Unit' of Qt, with the 6 names Qt gives in it.
    """

    Millimeter = Kee[int](0)
    Point = Kee[int](1)
    Inch = Kee[int](2)
    Pica = Kee[int](3)
    Didot = Kee[int](4)
    Cicero = Kee[int](5)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPageLayout'

  #  Qt's '~QPageLayout()'. Naming it makes this a value class: Python owns
  #  every C++ QPageLayout behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QPageLayoutD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def isEquivalentTo(self, other: QPageLayout) -> bool:
    """
    Calls Qt's 'bool QPageLayout::isEquivalentTo(const QPageLayout &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#isEquivalentTo

    Parameters
    ----------

    other : QPageLayout
      Passed on as a value: Qt reads the C++ QPageLayout, which stays
      Python's own.
    """
    #  bool QPageLayout::isEquivalentTo(const QPageLayout &other) const
    return self.uglySide.call(
        'ritual_ZNK11QPageLayout14isEquivalentToERKS_', self._valueOf(other),
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QPageLayout::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#isValid
    """
    #  bool QPageLayout::isValid() const
    return self.uglySide.call('ritual_ZNK11QPageLayout7isValidEv')

  def mode(self) -> Mode:
    """
    Calls Qt's 'Mode QPageLayout::mode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#mode

    Returns
    -------

    Mode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Mode(number)' gives.
    """
    #  Mode QPageLayout::mode() const
    return QPageLayout.Mode(self.uglySide.call(
        'ritual_ZNK11QPageLayout4modeEv',
    ))

  def pageSize(self) -> QPageSize:
    """
    Calls Qt's 'QPageSize QPageLayout::pageSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#pageSize

    Returns
    -------

    QPageSize
      A new cute QPageSize around the copy Qt gave back. Python owns it.
    """
    #  QPageSize QPageLayout::pageSize() const
    address = self.uglySide.call('ritual_ZNK11QPageLayout8pageSizeEv')
    from . import QPageSize
    return QPageSize._cuteOwning(address)

  def orientation(self) -> Orientation:
    """
    Calls Qt's 'Orientation QPageLayout::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#orientation

    Returns
    -------

    Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Orientation(number)'
      gives.
    """
    #  Orientation QPageLayout::orientation() const
    return QPageLayout.Orientation(self.uglySide.call(
        'ritual_ZNK11QPageLayout11orientationEv',
    ))

  def units(self) -> Unit:
    """
    Calls Qt's 'Unit QPageLayout::units() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#units

    Returns
    -------

    Unit
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Unit(number)' gives.
    """
    #  Unit QPageLayout::units() const
    return QPageLayout.Unit(self.uglySide.call(
        'ritual_ZNK11QPageLayout5unitsEv',
    ))

  @overload()
  def margins(self) -> QMarginsF:
    """
    Calls Qt's 'QMarginsF QPageLayout::margins() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#margins

    Returns
    -------

    QMarginsF
      A new cute QMarginsF around the copy Qt gave back. Python owns it.
    """
    #  QMarginsF QPageLayout::margins() const
    address = self.uglySide.call('ritual_ZNK11QPageLayout7marginsEv')
    from ..QtCore import QMarginsF
    return QMarginsF._cuteOwning(address)

  @overload(Unit)
  def margins(self, units: Unit) -> QMarginsF:
    """
    Calls Qt's 'QMarginsF QPageLayout::margins(Unit units) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#margins

    Parameters
    ----------

    units : Unit
      Passed on as its number.

    Returns
    -------

    QMarginsF
      A new cute QMarginsF around the copy Qt gave back. Python owns it.
    """
    #  QMarginsF QPageLayout::margins(Unit units) const
    address = self.uglySide.call(
        'ritual_ZNK11QPageLayout7marginsENS_4UnitE', units.value,
    )
    from ..QtCore import QMarginsF
    return QMarginsF._cuteOwning(address)

  def marginsPoints(self) -> QMargins:
    """
    Calls Qt's 'QMargins QPageLayout::marginsPoints() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#marginsPoints

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins QPageLayout::marginsPoints() const
    address = self.uglySide.call('ritual_ZNK11QPageLayout13marginsPointsEv')
    from ..QtCore import QMargins
    return QMargins._cuteOwning(address)

  @overload(int)
  def marginsPixels(self, resolution: int) -> QMargins:
    """
    Calls Qt's 'QMargins QPageLayout::marginsPixels(int resolution) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#marginsPixels

    Parameters
    ----------

    resolution : int
      Passed on as it is.

    Returns
    -------

    QMargins
      A new cute QMargins around the copy Qt gave back. Python owns it.
    """
    #  QMargins QPageLayout::marginsPixels(int resolution) const
    address = self.uglySide.call(
        'ritual_ZNK11QPageLayout13marginsPixelsEi', resolution,
    )
    from ..QtCore import QMargins
    return QMargins._cuteOwning(address)

  def minimumMargins(self) -> QMarginsF:
    """
    Calls Qt's 'QMarginsF QPageLayout::minimumMargins() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#minimumMargins

    Returns
    -------

    QMarginsF
      A new cute QMarginsF around the copy Qt gave back. Python owns it.
    """
    #  QMarginsF QPageLayout::minimumMargins() const
    address = self.uglySide.call('ritual_ZNK11QPageLayout14minimumMarginsEv')
    from ..QtCore import QMarginsF
    return QMarginsF._cuteOwning(address)

  def maximumMargins(self) -> QMarginsF:
    """
    Calls Qt's 'QMarginsF QPageLayout::maximumMargins() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#maximumMargins

    Returns
    -------

    QMarginsF
      A new cute QMarginsF around the copy Qt gave back. Python owns it.
    """
    #  QMarginsF QPageLayout::maximumMargins() const
    address = self.uglySide.call('ritual_ZNK11QPageLayout14maximumMarginsEv')
    from ..QtCore import QMarginsF
    return QMarginsF._cuteOwning(address)

  @overload()
  def fullRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QPageLayout::fullRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#fullRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPageLayout::fullRect() const
    address = self.uglySide.call('ritual_ZNK11QPageLayout8fullRectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(Unit)
  def fullRect(self, units: Unit) -> QRectF:
    """
    Calls Qt's 'QRectF QPageLayout::fullRect(Unit units) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#fullRect

    Parameters
    ----------

    units : Unit
      Passed on as its number.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPageLayout::fullRect(Unit units) const
    address = self.uglySide.call(
        'ritual_ZNK11QPageLayout8fullRectENS_4UnitE', units.value,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def fullRectPoints(self) -> QRect:
    """
    Calls Qt's 'QRect QPageLayout::fullRectPoints() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#fullRectPoints

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPageLayout::fullRectPoints() const
    address = self.uglySide.call('ritual_ZNK11QPageLayout14fullRectPointsEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(int)
  def fullRectPixels(self, resolution: int) -> QRect:
    """
    Calls Qt's 'QRect QPageLayout::fullRectPixels(int resolution) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#fullRectPixels

    Parameters
    ----------

    resolution : int
      Passed on as it is.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPageLayout::fullRectPixels(int resolution) const
    address = self.uglySide.call(
        'ritual_ZNK11QPageLayout14fullRectPixelsEi', resolution,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload()
  def paintRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QPageLayout::paintRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#paintRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPageLayout::paintRect() const
    address = self.uglySide.call('ritual_ZNK11QPageLayout9paintRectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(Unit)
  def paintRect(self, units: Unit) -> QRectF:
    """
    Calls Qt's 'QRectF QPageLayout::paintRect(Unit units) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#paintRect

    Parameters
    ----------

    units : Unit
      Passed on as its number.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPageLayout::paintRect(Unit units) const
    address = self.uglySide.call(
        'ritual_ZNK11QPageLayout9paintRectENS_4UnitE', units.value,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def paintRectPoints(self) -> QRect:
    """
    Calls Qt's 'QRect QPageLayout::paintRectPoints() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#paintRectPoints

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPageLayout::paintRectPoints() const
    address = self.uglySide.call(
        'ritual_ZNK11QPageLayout15paintRectPointsEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(int)
  def paintRectPixels(self, resolution: int) -> QRect:
    """
    Calls Qt's 'QRect QPageLayout::paintRectPixels(int resolution) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#paintRectPixels

    Parameters
    ----------

    resolution : int
      Passed on as it is.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QPageLayout::paintRectPixels(int resolution) const
    address = self.uglySide.call(
        'ritual_ZNK11QPageLayout15paintRectPixelsEi', resolution,
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Mode)
  def setMode(self, mode: Mode) -> None:
    """
    Calls Qt's 'void QPageLayout::setMode(Mode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#setMode

    Parameters
    ----------

    mode : Mode
      Passed on as its number.
    """
    #  void QPageLayout::setMode(Mode mode)
    self.uglySide.call(
        'ritual_ZN11QPageLayout7setModeENS_4ModeE', mode.value,
    )

  @overload(QPageSize, QMarginsF)
  def setPageSize(self, pageSize: QPageSize, minMargins: QMarginsF) -> None:
    """
    Calls Qt's 'void QPageLayout::setPageSize(const QPageSize &pageSize,
    const QMarginsF &minMargins)'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#setPageSize

    Parameters
    ----------

    pageSize : QPageSize
      Passed on as a value: Qt reads the C++ QPageSize, which stays Python's
      own.

    minMargins : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.
    """
    #  void QPageLayout::setPageSize(const QPageSize &pageSize, const
    #      QMarginsF &minMargins)
    self.uglySide.call(
        'ritual_ZN11QPageLayout11setPageSizeERK9QPageSizeRK9QMarginsF',
        self._valueOf(pageSize), self._valueOf(minMargins),
    )

  @overload(Orientation)
  def setOrientation(self, orientation: Orientation) -> None:
    """
    Calls Qt's 'void QPageLayout::setOrientation(Orientation orientation)'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#setOrientation

    Parameters
    ----------

    orientation : Orientation
      Passed on as its number.
    """
    #  void QPageLayout::setOrientation(Orientation orientation)
    self.uglySide.call(
        'ritual_ZN11QPageLayout14setOrientationENS_11OrientationE',
        orientation.value,
    )

  @overload(Unit)
  def setUnits(self, units: Unit) -> None:
    """
    Calls Qt's 'void QPageLayout::setUnits(Unit units)'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#setUnits

    Parameters
    ----------

    units : Unit
      Passed on as its number.
    """
    #  void QPageLayout::setUnits(Unit units)
    self.uglySide.call(
        'ritual_ZN11QPageLayout8setUnitsENS_4UnitE', units.value,
    )

  @overload(QMarginsF)
  @overload(QMarginsF, OutOfBoundsPolicy)
  def setMargins(
      self,
      margins: QMarginsF,
      outOfBoundsPolicy: OutOfBoundsPolicy = OutOfBoundsPolicy.Reject,
  ) -> bool:
    """
    Calls Qt's 'bool QPageLayout::setMargins(const QMarginsF &margins,
    OutOfBoundsPolicy outOfBoundsPolicy)'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#setMargins

    Parameters
    ----------

    margins : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.

    outOfBoundsPolicy : OutOfBoundsPolicy
      Passed on as its number. May be left out, as in Qt: it is then
      OutOfBoundsPolicy.Reject.
    """
    #  bool QPageLayout::setMargins(const QMarginsF &margins,
    #      OutOfBoundsPolicy outOfBoundsPolicy)
    return self.uglySide.call(
        'ritual_ZN11QPageLayout10setMarginsERK9QMarginsFNS_17OutOfBoundsPol'
        'icyE',
        self._valueOf(margins), outOfBoundsPolicy.value,
    )

  @overload(float)
  @overload(float, OutOfBoundsPolicy)
  def setLeftMargin(
      self,
      leftMargin: float,
      outOfBoundsPolicy: OutOfBoundsPolicy = OutOfBoundsPolicy.Reject,
  ) -> bool:
    """
    Calls Qt's 'bool QPageLayout::setLeftMargin(qreal leftMargin,
    OutOfBoundsPolicy outOfBoundsPolicy)'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#setLeftMargin

    Parameters
    ----------

    leftMargin : float
      Passed on as it is.

    outOfBoundsPolicy : OutOfBoundsPolicy
      Passed on as its number. May be left out, as in Qt: it is then
      OutOfBoundsPolicy.Reject.
    """
    #  bool QPageLayout::setLeftMargin(qreal leftMargin, OutOfBoundsPolicy
    #      outOfBoundsPolicy)
    return self.uglySide.call(
        'ritual_ZN11QPageLayout13setLeftMarginEdNS_17OutOfBoundsPolicyE',
        leftMargin, outOfBoundsPolicy.value,
    )

  @overload(float)
  @overload(float, OutOfBoundsPolicy)
  def setRightMargin(
      self,
      rightMargin: float,
      outOfBoundsPolicy: OutOfBoundsPolicy = OutOfBoundsPolicy.Reject,
  ) -> bool:
    """
    Calls Qt's 'bool QPageLayout::setRightMargin(qreal rightMargin,
    OutOfBoundsPolicy outOfBoundsPolicy)'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#setRightMargin

    Parameters
    ----------

    rightMargin : float
      Passed on as it is.

    outOfBoundsPolicy : OutOfBoundsPolicy
      Passed on as its number. May be left out, as in Qt: it is then
      OutOfBoundsPolicy.Reject.
    """
    #  bool QPageLayout::setRightMargin(qreal rightMargin, OutOfBoundsPolicy
    #      outOfBoundsPolicy)
    return self.uglySide.call(
        'ritual_ZN11QPageLayout14setRightMarginEdNS_17OutOfBoundsPolicyE',
        rightMargin, outOfBoundsPolicy.value,
    )

  @overload(float)
  @overload(float, OutOfBoundsPolicy)
  def setTopMargin(
      self,
      topMargin: float,
      outOfBoundsPolicy: OutOfBoundsPolicy = OutOfBoundsPolicy.Reject,
  ) -> bool:
    """
    Calls Qt's 'bool QPageLayout::setTopMargin(qreal topMargin,
    OutOfBoundsPolicy outOfBoundsPolicy)'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#setTopMargin

    Parameters
    ----------

    topMargin : float
      Passed on as it is.

    outOfBoundsPolicy : OutOfBoundsPolicy
      Passed on as its number. May be left out, as in Qt: it is then
      OutOfBoundsPolicy.Reject.
    """
    #  bool QPageLayout::setTopMargin(qreal topMargin, OutOfBoundsPolicy
    #      outOfBoundsPolicy)
    return self.uglySide.call(
        'ritual_ZN11QPageLayout12setTopMarginEdNS_17OutOfBoundsPolicyE',
        topMargin, outOfBoundsPolicy.value,
    )

  @overload(float)
  @overload(float, OutOfBoundsPolicy)
  def setBottomMargin(
      self,
      bottomMargin: float,
      outOfBoundsPolicy: OutOfBoundsPolicy = OutOfBoundsPolicy.Reject,
  ) -> bool:
    """
    Calls Qt's 'bool QPageLayout::setBottomMargin(qreal bottomMargin,
    OutOfBoundsPolicy outOfBoundsPolicy)'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#setBottomMargin

    Parameters
    ----------

    bottomMargin : float
      Passed on as it is.

    outOfBoundsPolicy : OutOfBoundsPolicy
      Passed on as its number. May be left out, as in Qt: it is then
      OutOfBoundsPolicy.Reject.
    """
    #  bool QPageLayout::setBottomMargin(qreal bottomMargin,
    #      OutOfBoundsPolicy outOfBoundsPolicy)
    return self.uglySide.call(
        'ritual_ZN11QPageLayout15setBottomMarginEdNS_17OutOfBoundsPolicyE',
        bottomMargin, outOfBoundsPolicy.value,
    )

  @overload(QMarginsF)
  def setMinimumMargins(self, minMargins: QMarginsF) -> None:
    """
    Calls Qt's 'void QPageLayout::setMinimumMargins(const QMarginsF
    &minMargins)'.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#setMinimumMargins

    Parameters
    ----------

    minMargins : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.
    """
    #  void QPageLayout::setMinimumMargins(const QMarginsF &minMargins)
    self.uglySide.call(
        'ritual_ZN11QPageLayout17setMinimumMarginsERK9QMarginsF',
        self._valueOf(minMargins),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QPageLayout::QPageLayout()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#QPageLayout
    """
    #  QPageLayout::QPageLayout()
    self._noteCreation(QPageLayout, lambda: Rituals.call(
        'ritual_ZN11QPageLayoutC1Ev',
    ))

  @overload(QPageSize, Orientation, QMarginsF, Unit, QMarginsF)
  def __init__(
      self,
      pageSize: QPageSize,
      orientation: Orientation,
      margins: QMarginsF,
      units: Unit,
      minMargins: QMarginsF,
  ) -> None:
    """
    Notes what was given, for Qt's 'QPageLayout::QPageLayout(const QPageSize
    &pageSize, Orientation orientation, const QMarginsF &margins, Unit units,
    const QMarginsF &minMargins)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#QPageLayout

    Parameters
    ----------

    pageSize : QPageSize
      Passed on as a value: Qt reads the C++ QPageSize, which stays Python's
      own.

    orientation : Orientation
      Passed on as its number.

    margins : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.

    units : Unit
      Passed on as its number.

    minMargins : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.
    """
    #  QPageLayout::QPageLayout(const QPageSize &pageSize, Orientation
    #      orientation, const QMarginsF &margins, Unit units, const QMarginsF
    #      &minMargins)
    self._noteCreation(QPageLayout, lambda: Rituals.call(
        'ritual_ZN11QPageLayoutC1ERK9QPageSizeNS_11OrientationERK9QMarginsF'
        'NS_4UnitES6_',
        self._valueOf(pageSize), orientation.value, self._valueOf(margins),
        units.value, self._valueOf(minMargins),
    ))

  @overload(THIS)
  def __init__(self, other: QPageLayout) -> None:
    """
    Notes what was given, for Qt's 'QPageLayout::QPageLayout(const
    QPageLayout &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpagelayout.html#QPageLayout

    Parameters
    ----------

    other : QPageLayout
      Passed on as a value: Qt reads the C++ QPageLayout, which stays
      Python's own.
    """
    #  QPageLayout::QPageLayout(const QPageLayout &other)
    self._noteCreation(QPageLayout, lambda: Rituals.call(
        'ritual_ZN11QPageLayoutC1ERKS_', self._valueOf(other),
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
