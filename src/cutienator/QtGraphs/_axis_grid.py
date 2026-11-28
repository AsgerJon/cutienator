"""
AxisGrid binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/axisgrid_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means AxisGrid to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtQuick import QQuickShaderEffect

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF, QRectF
  from ..QtGui import QColor, QVector3D, QVector4D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']


class AxisGrid(QQuickShaderEffect):
  """
  The cute side of Qt's AxisGrid: a plain Python object standing in front of
  one C++ AxisGrid.

  It is built on the cute 'QQuickShaderEffect', as Qt's AxisGrid is built on
  Qt's QQuickShaderEffect, and has everything that class has.

  What exists
  -----------

  Every function of Qt's AxisGrid that has a ritual and that Python can call
  so far, 40 names in all: 'metaObject', 'setupShaders', 'iResolution',
  'smoothing', 'origo', 'gridVisibility', 'gridWidth', 'gridHeight',
  'gridMovement', 'subGridColor', 'gridColor', 'plotAreaBackgroundColor',
  'subGridLineWidth', 'gridLineWidth', 'verticalSubGridScale',
  'horizontalSubGridScale', 'isVerticalLogarithmic',
  'isHorizontalLogarithmic', 'verticalBase', 'horizontalBase',
  'componentComplete', 'geometryChange', 'iResolutionChanged',
  'smoothingChanged', 'origoChanged', 'gridVisibilityChanged',
  'gridWidthChanged', 'gridHeightChanged', 'gridMovementChanged',
  'subGridColorChanged', 'gridColorChanged',
  'plotAreaBackgroundColorChanged', 'subGridLineWidthChanged',
  'gridLineWidthChanged', 'verticalSubGridScaleChanged',
  'horizontalSubGridScaleChanged', 'verticalLogarithmicChanged',
  'horizontalLogarithmicChanged', 'verticalBaseChanged',
  'horizontalBaseChanged'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *AxisGrid::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int AxisGrid::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'AxisGrid::~AxisGrid()': the destructor: Python never removes a C++
    AxisGrid.

  What has no ritual
  ------------------

  21 of the 64 functions Qt declares: 19 leans on 'AxisGrid; 2 not a gap.

  What to expect
  --------------

  - The C++ AxisGrid is created at the first use, not by 'AxisGrid(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ AxisGrid.
  - Qt tells when it has removed the C++ AxisGrid. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's AxisGrid that has no cute function yet, '__init__',
    'setGridColor', 'setGridHeight', 'setGridLineWidth', 'setGridMovement',
    'setGridVisibility', 'setGridWidth', 'setHorizontalBase',
    'setHorizontalLogarithmic', 'setHorizontalSubGridScale', 'setOrigo',
    'setPlotAreaBackgroundColor', 'setSmoothing', 'setSubGridColor',
    'setSubGridLineWidth', 'setVerticalBase', 'setVerticalLogarithmic',
    'setVerticalSubGridScale', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'AxisGrid'

  #  A C++ AxisGrid Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_AxisGrid'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *AxisGrid::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisgrid.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *AxisGrid::metaObject() const
    address = self.uglySide.call('ritual_ZNK8AxisGrid10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def iResolution(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D AxisGrid::iResolution() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisgrid.html#iResolution

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D AxisGrid::iResolution() const
    address = self.uglySide.call('ritual_ZNK8AxisGrid11iResolutionEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def smoothing(self) -> float:
    """
    Calls Qt's 'qreal AxisGrid::smoothing() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisgrid.html#smoothing
    """
    #  qreal AxisGrid::smoothing() const
    return self.uglySide.call('ritual_ZNK8AxisGrid9smoothingEv')

  def origo(self) -> int:
    """
    Calls Qt's 'int AxisGrid::origo() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisgrid.html#origo
    """
    #  int AxisGrid::origo() const
    return self.uglySide.call('ritual_ZNK8AxisGrid5origoEv')

  def gridVisibility(self) -> QVector4D:
    """
    Calls Qt's 'QVector4D AxisGrid::gridVisibility() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisgrid.html#gridVisibility

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D AxisGrid::gridVisibility() const
    address = self.uglySide.call('ritual_ZNK8AxisGrid14gridVisibilityEv')
    from ..QtGui import QVector4D
    return QVector4D._cuteOwning(address)

  def gridWidth(self) -> float:
    """
    Calls Qt's 'qreal AxisGrid::gridWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisgrid.html#gridWidth
    """
    #  qreal AxisGrid::gridWidth() const
    return self.uglySide.call('ritual_ZNK8AxisGrid9gridWidthEv')

  def gridHeight(self) -> float:
    """
    Calls Qt's 'qreal AxisGrid::gridHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisgrid.html#gridHeight
    """
    #  qreal AxisGrid::gridHeight() const
    return self.uglySide.call('ritual_ZNK8AxisGrid10gridHeightEv')

  def gridMovement(self) -> QPointF:
    """
    Calls Qt's 'QPointF AxisGrid::gridMovement() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisgrid.html#gridMovement

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF AxisGrid::gridMovement() const
    address = self.uglySide.call('ritual_ZNK8AxisGrid12gridMovementEv')
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def subGridColor(self) -> QColor:
    """
    Calls Qt's 'QColor AxisGrid::subGridColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisgrid.html#subGridColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor AxisGrid::subGridColor() const
    address = self.uglySide.call('ritual_ZNK8AxisGrid12subGridColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def gridColor(self) -> QColor:
    """
    Calls Qt's 'QColor AxisGrid::gridColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisgrid.html#gridColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor AxisGrid::gridColor() const
    address = self.uglySide.call('ritual_ZNK8AxisGrid9gridColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def plotAreaBackgroundColor(self) -> QColor:
    """
    Calls Qt's 'QColor AxisGrid::plotAreaBackgroundColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisgrid.html#plotAreaBackgroundColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor AxisGrid::plotAreaBackgroundColor() const
    address = self.uglySide.call(
        'ritual_ZNK8AxisGrid23plotAreaBackgroundColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def subGridLineWidth(self) -> float:
    """
    Calls Qt's 'qreal AxisGrid::subGridLineWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisgrid.html#subGridLineWidth
    """
    #  qreal AxisGrid::subGridLineWidth() const
    return self.uglySide.call('ritual_ZNK8AxisGrid16subGridLineWidthEv')

  def gridLineWidth(self) -> float:
    """
    Calls Qt's 'qreal AxisGrid::gridLineWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisgrid.html#gridLineWidth
    """
    #  qreal AxisGrid::gridLineWidth() const
    return self.uglySide.call('ritual_ZNK8AxisGrid13gridLineWidthEv')

  def verticalSubGridScale(self) -> float:
    """
    Calls Qt's 'qreal AxisGrid::verticalSubGridScale() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisgrid.html#verticalSubGridScale
    """
    #  qreal AxisGrid::verticalSubGridScale() const
    return self.uglySide.call('ritual_ZNK8AxisGrid20verticalSubGridScaleEv')

  def horizontalSubGridScale(self) -> float:
    """
    Calls Qt's 'qreal AxisGrid::horizontalSubGridScale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisgrid.html#horizontalSubGridScale
    """
    #  qreal AxisGrid::horizontalSubGridScale() const
    return self.uglySide.call(
        'ritual_ZNK8AxisGrid22horizontalSubGridScaleEv',
    )

  def isVerticalLogarithmic(self) -> bool:
    """
    Calls Qt's 'bool AxisGrid::isVerticalLogarithmic() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisgrid.html#isVerticalLogarithmic
    """
    #  bool AxisGrid::isVerticalLogarithmic() const
    return self.uglySide.call('ritual_ZNK8AxisGrid21isVerticalLogarithmicEv')

  def isHorizontalLogarithmic(self) -> bool:
    """
    Calls Qt's 'bool AxisGrid::isHorizontalLogarithmic() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisgrid.html#isHorizontalLogarithmic
    """
    #  bool AxisGrid::isHorizontalLogarithmic() const
    return self.uglySide.call(
        'ritual_ZNK8AxisGrid23isHorizontalLogarithmicEv',
    )

  def verticalBase(self) -> float:
    """
    Calls Qt's 'qreal AxisGrid::verticalBase() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisgrid.html#verticalBase
    """
    #  qreal AxisGrid::verticalBase() const
    return self.uglySide.call('ritual_ZNK8AxisGrid12verticalBaseEv')

  def horizontalBase(self) -> float:
    """
    Calls Qt's 'qreal AxisGrid::horizontalBase() const'.

    Qt's own words: https://doc.qt.io/qt-6/axisgrid.html#horizontalBase
    """
    #  qreal AxisGrid::horizontalBase() const
    return self.uglySide.call('ritual_ZNK8AxisGrid14horizontalBaseEv')

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'AxisGrid::AxisGrid(QQuickItem *parent)': leans on
    'AxisGrid::qt_metacall(QMetaObject::Call, int, void**)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'AxisGrid.__init__' has no cute function yet. Qt's "
        "'AxisGrid::AxisGrid(QQuickItem *parent)': leans on "
        "'AxisGrid::qt_metacall(QMetaObject::Call, int, void**)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  def setupShaders(self) -> None:
    """
    Calls Qt's 'void AxisGrid::setupShaders()'.

    Qt's own words: https://doc.qt.io/qt-6/axisgrid.html#setupShaders
    """
    #  void AxisGrid::setupShaders()
    self.uglySide.call('ritual_ZN8AxisGrid12setupShadersEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void AxisGrid::componentComplete()'.

    Qt's own words: https://doc.qt.io/qt-6/axisgrid.html#componentComplete
    """
    #  void AxisGrid::componentComplete()
    ritual = 'ritual_ZN8AxisGrid17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8AxisGrid17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void AxisGrid::geometryChange(const QRectF &newGeometry,
    const QRectF &oldGeometry)'.

    Qt's own words: https://doc.qt.io/qt-6/axisgrid.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void AxisGrid::geometryChange(const QRectF &newGeometry, const QRectF
    #      &oldGeometry)
    self.uglySide.call(
        'ritual_ZN8AxisGrid14geometryChangeERK6QRectFS2_',
        self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  def iResolutionChanged(self) -> None:
    """
    Calls Qt's 'void AxisGrid::iResolutionChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/axisgrid.html#iResolutionChanged
    """
    #  void AxisGrid::iResolutionChanged()
    self.uglySide.call('ritual_ZN8AxisGrid18iResolutionChangedEv')

  def smoothingChanged(self) -> None:
    """
    Calls Qt's 'void AxisGrid::smoothingChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/axisgrid.html#smoothingChanged
    """
    #  void AxisGrid::smoothingChanged()
    self.uglySide.call('ritual_ZN8AxisGrid16smoothingChangedEv')

  def origoChanged(self) -> None:
    """
    Calls Qt's 'void AxisGrid::origoChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/axisgrid.html#origoChanged
    """
    #  void AxisGrid::origoChanged()
    self.uglySide.call('ritual_ZN8AxisGrid12origoChangedEv')

  def gridVisibilityChanged(self) -> None:
    """
    Calls Qt's 'void AxisGrid::gridVisibilityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisgrid.html#gridVisibilityChanged
    """
    #  void AxisGrid::gridVisibilityChanged()
    self.uglySide.call('ritual_ZN8AxisGrid21gridVisibilityChangedEv')

  def gridWidthChanged(self) -> None:
    """
    Calls Qt's 'void AxisGrid::gridWidthChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/axisgrid.html#gridWidthChanged
    """
    #  void AxisGrid::gridWidthChanged()
    self.uglySide.call('ritual_ZN8AxisGrid16gridWidthChangedEv')

  def gridHeightChanged(self) -> None:
    """
    Calls Qt's 'void AxisGrid::gridHeightChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/axisgrid.html#gridHeightChanged
    """
    #  void AxisGrid::gridHeightChanged()
    self.uglySide.call('ritual_ZN8AxisGrid17gridHeightChangedEv')

  def gridMovementChanged(self) -> None:
    """
    Calls Qt's 'void AxisGrid::gridMovementChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/axisgrid.html#gridMovementChanged
    """
    #  void AxisGrid::gridMovementChanged()
    self.uglySide.call('ritual_ZN8AxisGrid19gridMovementChangedEv')

  def subGridColorChanged(self) -> None:
    """
    Calls Qt's 'void AxisGrid::subGridColorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/axisgrid.html#subGridColorChanged
    """
    #  void AxisGrid::subGridColorChanged()
    self.uglySide.call('ritual_ZN8AxisGrid19subGridColorChangedEv')

  def gridColorChanged(self) -> None:
    """
    Calls Qt's 'void AxisGrid::gridColorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/axisgrid.html#gridColorChanged
    """
    #  void AxisGrid::gridColorChanged()
    self.uglySide.call('ritual_ZN8AxisGrid16gridColorChangedEv')

  def plotAreaBackgroundColorChanged(self) -> None:
    """
    Calls Qt's 'void AxisGrid::plotAreaBackgroundColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisgrid.html#plotAreaBackgroundColorChanged
    """
    #  void AxisGrid::plotAreaBackgroundColorChanged()
    self.uglySide.call(
        'ritual_ZN8AxisGrid30plotAreaBackgroundColorChangedEv',
    )

  def subGridLineWidthChanged(self) -> None:
    """
    Calls Qt's 'void AxisGrid::subGridLineWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisgrid.html#subGridLineWidthChanged
    """
    #  void AxisGrid::subGridLineWidthChanged()
    self.uglySide.call('ritual_ZN8AxisGrid23subGridLineWidthChangedEv')

  def gridLineWidthChanged(self) -> None:
    """
    Calls Qt's 'void AxisGrid::gridLineWidthChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/axisgrid.html#gridLineWidthChanged
    """
    #  void AxisGrid::gridLineWidthChanged()
    self.uglySide.call('ritual_ZN8AxisGrid20gridLineWidthChangedEv')

  def verticalSubGridScaleChanged(self) -> None:
    """
    Calls Qt's 'void AxisGrid::verticalSubGridScaleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisgrid.html#verticalSubGridScaleChanged
    """
    #  void AxisGrid::verticalSubGridScaleChanged()
    self.uglySide.call('ritual_ZN8AxisGrid27verticalSubGridScaleChangedEv')

  def horizontalSubGridScaleChanged(self) -> None:
    """
    Calls Qt's 'void AxisGrid::horizontalSubGridScaleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisgrid.html#horizontalSubGridScaleChanged
    """
    #  void AxisGrid::horizontalSubGridScaleChanged()
    self.uglySide.call('ritual_ZN8AxisGrid29horizontalSubGridScaleChangedEv')

  @overload(bool)
  def verticalLogarithmicChanged(self, logarithmic: bool) -> None:
    """
    Calls Qt's 'void AxisGrid::verticalLogarithmicChanged(bool logarithmic)'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisgrid.html#verticalLogarithmicChanged

    Parameters
    ----------

    logarithmic : bool
      Passed on as it is.
    """
    #  void AxisGrid::verticalLogarithmicChanged(bool logarithmic)
    self.uglySide.call(
        'ritual_ZN8AxisGrid26verticalLogarithmicChangedEb', logarithmic,
    )

  @overload(bool)
  def horizontalLogarithmicChanged(self, logarithmic: bool) -> None:
    """
    Calls Qt's 'void AxisGrid::horizontalLogarithmicChanged(bool
    logarithmic)'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisgrid.html#horizontalLogarithmicChanged

    Parameters
    ----------

    logarithmic : bool
      Passed on as it is.
    """
    #  void AxisGrid::horizontalLogarithmicChanged(bool logarithmic)
    self.uglySide.call(
        'ritual_ZN8AxisGrid28horizontalLogarithmicChangedEb', logarithmic,
    )

  @overload(float)
  def verticalBaseChanged(self, base: float) -> None:
    """
    Calls Qt's 'void AxisGrid::verticalBaseChanged(qreal base)'.

    Qt's own words: https://doc.qt.io/qt-6/axisgrid.html#verticalBaseChanged

    Parameters
    ----------

    base : float
      Passed on as it is.
    """
    #  void AxisGrid::verticalBaseChanged(qreal base)
    self.uglySide.call('ritual_ZN8AxisGrid19verticalBaseChangedEd', base)

  @overload(float)
  def horizontalBaseChanged(self, base: float) -> None:
    """
    Calls Qt's 'void AxisGrid::horizontalBaseChanged(qreal base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/axisgrid.html#horizontalBaseChanged

    Parameters
    ----------

    base : float
      Passed on as it is.
    """
    #  void AxisGrid::horizontalBaseChanged(qreal base)
    self.uglySide.call('ritual_ZN8AxisGrid21horizontalBaseChangedEd', base)

  @staticmethod
  def setGridColor(*__, **_) -> Never:
    """
    Qt's 'void AxisGrid::setGridColor(QColor newGridColor)': leans on
    'AxisGrid::gridColorChanged()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisGrid.setGridColor' has no cute function yet. Qt's 'void "
        "AxisGrid::setGridColor(QColor newGridColor)': leans on "
        "'AxisGrid::gridColorChanged()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setGridHeight(*__, **_) -> Never:
    """
    Qt's 'void AxisGrid::setGridHeight(qreal newGridHeight)': leans on
    'AxisGrid::gridHeightChanged()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisGrid.setGridHeight' has no cute function yet. Qt's 'void "
        "AxisGrid::setGridHeight(qreal newGridHeight)': leans on "
        "'AxisGrid::gridHeightChanged()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setGridLineWidth(*__, **_) -> Never:
    """
    Qt's 'void AxisGrid::setGridLineWidth(qreal newGridLineWidth)': leans on
    'AxisGrid::gridLineWidthChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisGrid.setGridLineWidth' has no cute function yet. Qt's 'void "
        "AxisGrid::setGridLineWidth(qreal newGridLineWidth)': leans on "
        "'AxisGrid::gridLineWidthChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setGridMovement(*__, **_) -> Never:
    """
    Qt's 'void AxisGrid::setGridMovement(QPointF newGridMovement)': leans on
    'AxisGrid::gridMovementChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisGrid.setGridMovement' has no cute function yet. Qt's 'void "
        "AxisGrid::setGridMovement(QPointF newGridMovement)': leans on "
        "'AxisGrid::gridMovementChanged()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setGridVisibility(*__, **_) -> Never:
    """
    Qt's 'void AxisGrid::setGridVisibility(const QVector4D
    &newGridVisibility)': leans on 'AxisGrid::gridVisibilityChanged()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'AxisGrid.setGridVisibility' has no cute function yet. Qt's 'void "
        "AxisGrid::setGridVisibility(const QVector4D &newGridVisibility)': "
        "leans on 'AxisGrid::gridVisibilityChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setGridWidth(*__, **_) -> Never:
    """
    Qt's 'void AxisGrid::setGridWidth(qreal newGridWidth)': leans on
    'AxisGrid::gridWidthChanged()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisGrid.setGridWidth' has no cute function yet. Qt's 'void "
        "AxisGrid::setGridWidth(qreal newGridWidth)': leans on "
        "'AxisGrid::gridWidthChanged()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setHorizontalBase(*__, **_) -> Never:
    """
    Qt's 'void AxisGrid::setHorizontalBase(qreal newBase)': leans on
    'AxisGrid::verticalBaseChanged(double)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisGrid.setHorizontalBase' has no cute function yet. Qt's 'void "
        "AxisGrid::setHorizontalBase(qreal newBase)': leans on "
        "'AxisGrid::verticalBaseChanged(double)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setHorizontalLogarithmic(*__, **_) -> Never:
    """
    Qt's 'void AxisGrid::setHorizontalLogarithmic(bool newLogarithmic)':
    leans on 'AxisGrid::horizontalLogarithmicChanged(bool)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'AxisGrid.setHorizontalLogarithmic' has no cute function yet. Qt's "
        "'void AxisGrid::setHorizontalLogarithmic(bool newLogarithmic)': "
        "leans on 'AxisGrid::horizontalLogarithmicChanged(bool)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setHorizontalSubGridScale(*__, **_) -> Never:
    """
    Qt's 'void AxisGrid::setHorizontalSubGridScale(qreal
    newHorizontalSubGridScale)': leans on
    'AxisGrid::horizontalSubGridScaleChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisGrid.setHorizontalSubGridScale' has no cute function yet. "
        "Qt's 'void AxisGrid::setHorizontalSubGridScale(qreal "
        "newHorizontalSubGridScale)': leans on "
        "'AxisGrid::horizontalSubGridScaleChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setOrigo(*__, **_) -> Never:
    """
    Qt's 'void AxisGrid::setOrigo(int newOrigo)': leans on
    'AxisGrid::origoChanged()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisGrid.setOrigo' has no cute function yet. Qt's 'void "
        "AxisGrid::setOrigo(int newOrigo)': leans on "
        "'AxisGrid::origoChanged()', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setPlotAreaBackgroundColor(*__, **_) -> Never:
    """
    Qt's 'void AxisGrid::setPlotAreaBackgroundColor(QColor color)': leans on
    'AxisGrid::plotAreaBackgroundColorChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisGrid.setPlotAreaBackgroundColor' has no cute function yet. "
        "Qt's 'void AxisGrid::setPlotAreaBackgroundColor(QColor color)': "
        "leans on 'AxisGrid::plotAreaBackgroundColorChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setSmoothing(*__, **_) -> Never:
    """
    Qt's 'void AxisGrid::setSmoothing(qreal newSmoothing)': leans on
    'AxisGrid::smoothingChanged()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisGrid.setSmoothing' has no cute function yet. Qt's 'void "
        "AxisGrid::setSmoothing(qreal newSmoothing)': leans on "
        "'AxisGrid::smoothingChanged()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setSubGridColor(*__, **_) -> Never:
    """
    Qt's 'void AxisGrid::setSubGridColor(QColor newSubGridColor)': leans on
    'AxisGrid::subGridColorChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisGrid.setSubGridColor' has no cute function yet. Qt's 'void "
        "AxisGrid::setSubGridColor(QColor newSubGridColor)': leans on "
        "'AxisGrid::subGridColorChanged()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def setSubGridLineWidth(*__, **_) -> Never:
    """
    Qt's 'void AxisGrid::setSubGridLineWidth(qreal newSubGridLineWidth)':
    leans on 'AxisGrid::subGridLineWidthChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisGrid.setSubGridLineWidth' has no cute function yet. Qt's "
        "'void AxisGrid::setSubGridLineWidth(qreal newSubGridLineWidth)': "
        "leans on 'AxisGrid::subGridLineWidthChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setVerticalBase(*__, **_) -> Never:
    """
    Qt's 'void AxisGrid::setVerticalBase(qreal newBase)': leans on
    'AxisGrid::verticalBaseChanged(double)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisGrid.setVerticalBase' has no cute function yet. Qt's 'void "
        "AxisGrid::setVerticalBase(qreal newBase)': leans on "
        "'AxisGrid::verticalBaseChanged(double)', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setVerticalLogarithmic(*__, **_) -> Never:
    """
    Qt's 'void AxisGrid::setVerticalLogarithmic(bool newLogarithmic)': leans
    on 'AxisGrid::verticalLogarithmicChanged(bool)', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisGrid.setVerticalLogarithmic' has no cute function yet. Qt's "
        "'void AxisGrid::setVerticalLogarithmic(bool newLogarithmic)': "
        "leans on 'AxisGrid::verticalLogarithmicChanged(bool)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setVerticalSubGridScale(*__, **_) -> Never:
    """
    Qt's 'void AxisGrid::setVerticalSubGridScale(qreal
    newVerticalSubGridScale)': leans on
    'AxisGrid::verticalSubGridScaleChanged()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'AxisGrid.setVerticalSubGridScale' has no cute function yet. Qt's "
        "'void AxisGrid::setVerticalSubGridScale(qreal "
        "newVerticalSubGridScale)': leans on "
        "'AxisGrid::verticalSubGridScaleChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")
