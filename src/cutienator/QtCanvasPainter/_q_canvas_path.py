"""
QCanvasPath binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/qcanvaspath.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QCanvasPainter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF, QRectF
  from ..QtGui import QPainterPath, QTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainterPath = WAIT['QPainterPath']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QTransform = WAIT['QTransform']


class QCanvasPath(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCanvasPath: a plain Python object standing in front
  of one C++ QCanvasPath.

  C++ hands a QCanvasPath around as a copy, so every C++ QCanvasPath behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCanvasPath that has a ritual and that Python can
  call so far, 28 names in all: 'closePath', 'moveTo', 'lineTo',
  'bezierCurveTo', 'quadraticCurveTo', 'arcTo', 'arc', 'rect', 'roundRect',
  'ellipse', 'circle', 'setPathWinding', 'beginSolidSubPath',
  'beginHoleSubPath', 'addPath', 'isEmpty', 'clear', 'squeeze',
  'commandsSize', 'commandsDataSize', 'commandsCapacity',
  'commandsDataCapacity', 'reserve', 'currentPosition', 'positionAt',
  'sliced', '__eq__', '__ne__'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCanvasPath::~QCanvasPath()': the destructor: Python removes its
    C++ QCanvasPath by it, and has no other use for it.
  - Qt's 'QCanvasPath &QCanvasPath::operator=(const QCanvasPath &path)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QCanvasPath::QCanvasPath(QCanvasPath &&other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QCanvasPath &QCanvasPath::operator=(QCanvasPath &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QCanvasPath::swap(QCanvasPath &other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QVariant QCanvasPath::operator QVariant() const': an operator
    Python has no name for.
  - Qt's 'QCanvasPathPrivate *QCanvasPath::d_func()': gives
    'QCanvasPathPrivate', which has no cute class yet.
  - Qt's 'const QCanvasPathPrivate *QCanvasPath::d_func() const': gives
    'QCanvasPathPrivate', which has no cute class yet.

  What to expect
  --------------

  - The C++ QCanvasPath is created at the first use, not by
    'QCanvasPath(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanvasPath back gives a copy the ritual made for
    Python, in a new cute QCanvasPath.
  - Each name of Qt's QCanvasPath that has no cute function yet, 'd_func',
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
  __qt_class__ = 'QCanvasPath'

  #  Qt's '~QCanvasPath()'. Naming it makes this a value class: Python owns
  #  every C++ QCanvasPath behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QCanvasPathD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QCanvasPath::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#isEmpty
    """
    #  bool QCanvasPath::isEmpty() const
    return self.uglySide.call('ritual_ZNK11QCanvasPath7isEmptyEv')

  def commandsSize(self) -> int:
    """
    Calls Qt's 'qsizetype QCanvasPath::commandsSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#commandsSize
    """
    #  qsizetype QCanvasPath::commandsSize() const
    return self.uglySide.call('ritual_ZNK11QCanvasPath12commandsSizeEv')

  def commandsDataSize(self) -> int:
    """
    Calls Qt's 'qsizetype QCanvasPath::commandsDataSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#commandsDataSize
    """
    #  qsizetype QCanvasPath::commandsDataSize() const
    return self.uglySide.call('ritual_ZNK11QCanvasPath16commandsDataSizeEv')

  def commandsCapacity(self) -> int:
    """
    Calls Qt's 'qsizetype QCanvasPath::commandsCapacity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#commandsCapacity
    """
    #  qsizetype QCanvasPath::commandsCapacity() const
    return self.uglySide.call('ritual_ZNK11QCanvasPath16commandsCapacityEv')

  def commandsDataCapacity(self) -> int:
    """
    Calls Qt's 'qsizetype QCanvasPath::commandsDataCapacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspath.html#commandsDataCapacity
    """
    #  qsizetype QCanvasPath::commandsDataCapacity() const
    return self.uglySide.call(
        'ritual_ZNK11QCanvasPath20commandsDataCapacityEv',
    )

  def currentPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QCanvasPath::currentPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#currentPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QCanvasPath::currentPosition() const
    address = self.uglySide.call(
        'ritual_ZNK11QCanvasPath15currentPositionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(int)
  def positionAt(self, index: int) -> QPointF:
    """
    Calls Qt's 'QPointF QCanvasPath::positionAt(qsizetype index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#positionAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QCanvasPath::positionAt(qsizetype index) const
    address = self.uglySide.call(
        'ritual_ZNK11QCanvasPath10positionAtEx', index,
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  @overload(int, int)
  @overload(int, int, QTransform)
  def sliced(
      self,
      start: int,
      count: int,
      transform: Optional[QTransform] = None,
  ) -> QCanvasPath:
    """
    Calls Qt's 'QCanvasPath QCanvasPath::sliced(qsizetype start, qsizetype
    count, const QTransform &transform) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#sliced

    Parameters
    ----------

    start : int
      Passed on as it is.

    count : int
      Passed on as it is.

    transform : Optional[QTransform]
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own. May be left out, as in Qt: a new 'QTransform()' is then passed on.

    Returns
    -------

    QCanvasPath
      A new cute QCanvasPath around the copy Qt gave back. Python owns it.
    """
    #  QCanvasPath QCanvasPath::sliced(qsizetype start, qsizetype count,
    #      const QTransform &transform) const
    if transform is None:
      from ..QtGui import QTransform
      transform = QTransform()
    address = self.uglySide.call(
        'ritual_ZNK11QCanvasPath6slicedExxRK10QTransform',
        start, count, self._valueOf(transform),
    )
    return QCanvasPath._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QCanvasPainter.PathWinding)
  def setPathWinding(self, winding: QCanvasPainter.PathWinding) -> None:
    """
    Calls Qt's 'void QCanvasPath::setPathWinding(QCanvasPainter::PathWinding
    winding)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#setPathWinding

    Parameters
    ----------

    winding : QCanvasPainter.PathWinding
      Passed on as its number.
    """
    #  void QCanvasPath::setPathWinding(QCanvasPainter::PathWinding winding)
    self.uglySide.call(
        'ritual_ZN11QCanvasPath14setPathWindingEN14QCanvasPainter11PathWind'
        'ingE',
        winding.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QCanvasPath) -> bool:
    """
    Calls Qt's 'bool operator==(const QCanvasPath &lhs, const QCanvasPath
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#operator==

    Parameters
    ----------

    rhs : QCanvasPath
      Passed on as a value: Qt reads the C++ QCanvasPath, which stays
      Python's own.
    """
    #  bool operator==(const QCanvasPath &lhs, const QCanvasPath &rhs)
    return Rituals.call(
        'ritual_ZeqRK11QCanvasPathS1_',
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
  def __ne__(self, rhs: QCanvasPath) -> bool:
    """
    Calls Qt's 'bool operator!=(const QCanvasPath &lhs, const QCanvasPath
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#operator!=

    Parameters
    ----------

    rhs : QCanvasPath
      Passed on as a value: Qt reads the C++ QCanvasPath, which stays
      Python's own.
    """
    #  bool operator!=(const QCanvasPath &lhs, const QCanvasPath &rhs)
    return Rituals.call(
        'ritual_ZneRK11QCanvasPathS1_',
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
    Notes what was given, for Qt's 'QCanvasPath::QCanvasPath()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#QCanvasPath
    """
    #  QCanvasPath::QCanvasPath()
    self._noteCreation(QCanvasPath, lambda: Rituals.call(
        'ritual_ZN11QCanvasPathC1Ev',
    ))

  @overload(int)
  @overload(int, int)
  def __init__(self, commandsSize: int, commandsDataSize: int = -1) -> None:
    """
    Notes what was given, for Qt's 'QCanvasPath::QCanvasPath(qsizetype
    commandsSize, qsizetype commandsDataSize)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#QCanvasPath

    Parameters
    ----------

    commandsSize : int
      Passed on as it is.

    commandsDataSize : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  QCanvasPath::QCanvasPath(qsizetype commandsSize, qsizetype
    #      commandsDataSize)
    self._noteCreation(QCanvasPath, lambda: Rituals.call(
        'ritual_ZN11QCanvasPathC1Exx', commandsSize, commandsDataSize,
    ))

  @overload(THIS)
  def __init__(self, path: QCanvasPath) -> None:
    """
    Notes what was given, for Qt's 'QCanvasPath::QCanvasPath(const
    QCanvasPath &path)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#QCanvasPath

    Parameters
    ----------

    path : QCanvasPath
      Passed on as a value: Qt reads the C++ QCanvasPath, which stays
      Python's own.
    """
    #  QCanvasPath::QCanvasPath(const QCanvasPath &path)
    self._noteCreation(QCanvasPath, lambda: Rituals.call(
        'ritual_ZN11QCanvasPathC1ERKS_', self._valueOf(path),
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

  def closePath(self) -> None:
    """
    Calls Qt's 'void QCanvasPath::closePath()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#closePath
    """
    #  void QCanvasPath::closePath()
    self.uglySide.call('ritual_ZN11QCanvasPath9closePathEv')

  @overload(float, float)
  def moveTo(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QCanvasPath::moveTo(qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#moveTo

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QCanvasPath::moveTo(qreal x, qreal y)
    self.uglySide.call('ritual_ZN11QCanvasPath6moveToEdd', x, y)

  @overload(QPointF)
  def moveTo(self, point: QPointF) -> None:
    """
    Calls Qt's 'void QCanvasPath::moveTo(QPointF point)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#moveTo

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QCanvasPath::moveTo(QPointF point)
    self.uglySide.call(
        'ritual_ZN11QCanvasPath6moveToE7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(float, float)
  def lineTo(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QCanvasPath::lineTo(qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#lineTo

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QCanvasPath::lineTo(qreal x, qreal y)
    self.uglySide.call('ritual_ZN11QCanvasPath6lineToEdd', x, y)

  @overload(QPointF)
  def lineTo(self, point: QPointF) -> None:
    """
    Calls Qt's 'void QCanvasPath::lineTo(QPointF point)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#lineTo

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QCanvasPath::lineTo(QPointF point)
    self.uglySide.call(
        'ritual_ZN11QCanvasPath6lineToE7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(float, float, float, float, float, float)
  def bezierCurveTo(
      self,
      c1x: float,
      c1y: float,
      c2x: float,
      c2y: float,
      x: float,
      y: float,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPath::bezierCurveTo(qreal c1x, qreal c1y, qreal
    c2x, qreal c2y, qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#bezierCurveTo

    Parameters
    ----------

    c1x : float
      Passed on as it is.

    c1y : float
      Passed on as it is.

    c2x : float
      Passed on as it is.

    c2y : float
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QCanvasPath::bezierCurveTo(qreal c1x, qreal c1y, qreal c2x, qreal
    #      c2y, qreal x, qreal y)
    self.uglySide.call(
        'ritual_ZN11QCanvasPath13bezierCurveToEdddddd',
        c1x, c1y, c2x, c2y, x, y,
    )

  @overload(QPointF, QPointF, QPointF)
  def bezierCurveTo(
      self,
      controlPoint1: QPointF,
      controlPoint2: QPointF,
      endPoint: QPointF,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPath::bezierCurveTo(QPointF controlPoint1,
    QPointF controlPoint2, QPointF endPoint)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#bezierCurveTo

    Parameters
    ----------

    controlPoint1 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    controlPoint2 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    endPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QCanvasPath::bezierCurveTo(QPointF controlPoint1, QPointF
    #      controlPoint2, QPointF endPoint)
    self.uglySide.call(
        'ritual_ZN11QCanvasPath13bezierCurveToE7QPointFS0_S0_',
        self._valueOf(controlPoint1, 'QPointF'), self._valueOf(controlPoint2,
        'QPointF'), self._valueOf(endPoint, 'QPointF'),
    )

  @overload(float, float, float, float)
  def quadraticCurveTo(
      self,
      cx: float,
      cy: float,
      x: float,
      y: float,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPath::quadraticCurveTo(qreal cx, qreal cy, qreal
    x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#quadraticCurveTo

    Parameters
    ----------

    cx : float
      Passed on as it is.

    cy : float
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QCanvasPath::quadraticCurveTo(qreal cx, qreal cy, qreal x, qreal
    #      y)
    self.uglySide.call(
        'ritual_ZN11QCanvasPath16quadraticCurveToEdddd', cx, cy, x, y,
    )

  @overload(QPointF, QPointF)
  def quadraticCurveTo(
      self,
      controlPoint: QPointF,
      endPoint: QPointF,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPath::quadraticCurveTo(QPointF controlPoint,
    QPointF endPoint)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#quadraticCurveTo

    Parameters
    ----------

    controlPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    endPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QCanvasPath::quadraticCurveTo(QPointF controlPoint, QPointF
    #      endPoint)
    self.uglySide.call(
        'ritual_ZN11QCanvasPath16quadraticCurveToE7QPointFS0_',
        self._valueOf(controlPoint, 'QPointF'), self._valueOf(endPoint,
        'QPointF'),
    )

  @overload(float, float, float, float, float)
  def arcTo(
      self,
      c1x: float,
      c1y: float,
      c2x: float,
      c2y: float,
      radius: float,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPath::arcTo(qreal c1x, qreal c1y, qreal c2x,
    qreal c2y, qreal radius)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#arcTo

    Parameters
    ----------

    c1x : float
      Passed on as it is.

    c1y : float
      Passed on as it is.

    c2x : float
      Passed on as it is.

    c2y : float
      Passed on as it is.

    radius : float
      Passed on as it is.
    """
    #  void QCanvasPath::arcTo(qreal c1x, qreal c1y, qreal c2x, qreal c2y,
    #      qreal radius)
    self.uglySide.call(
        'ritual_ZN11QCanvasPath5arcToEddddd', c1x, c1y, c2x, c2y, radius,
    )

  @overload(QPointF, QPointF, float)
  def arcTo(
      self,
      controlPoint1: QPointF,
      controlPoint2: QPointF,
      radius: float,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPath::arcTo(QPointF controlPoint1, QPointF
    controlPoint2, qreal radius)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#arcTo

    Parameters
    ----------

    controlPoint1 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    controlPoint2 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    radius : float
      Passed on as it is.
    """
    #  void QCanvasPath::arcTo(QPointF controlPoint1, QPointF controlPoint2,
    #      qreal radius)
    self.uglySide.call(
        'ritual_ZN11QCanvasPath5arcToE7QPointFS0_d',
        self._valueOf(controlPoint1, 'QPointF'), self._valueOf(controlPoint2,
        'QPointF'), radius,
    )

  @overload(float, float, float, float, float)
  @overload(float, float, float, float, float, QCanvasPainter.PathWinding)
  @overload(
      float, float, float, float, float, QCanvasPainter.PathWinding,
      QCanvasPainter.PathConnection,
  )
  def arc(
      self,
      centerX: float,
      centerY: float,
      radius: float,
      a0: float,
      a1: float,
      direction: QCanvasPainter.PathWinding = (
          QCanvasPainter.PathWinding.ClockWise),
      connection: QCanvasPainter.PathConnection = (
          QCanvasPainter.PathConnection.Connected),
  ) -> None:
    """
    Calls Qt's 'void QCanvasPath::arc(qreal centerX, qreal centerY, qreal
    radius, qreal a0, qreal a1, QCanvasPainter::PathWinding direction,
    QCanvasPainter::PathConnection connection)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#arc

    Parameters
    ----------

    centerX : float
      Passed on as it is.

    centerY : float
      Passed on as it is.

    radius : float
      Passed on as it is.

    a0 : float
      Passed on as it is.

    a1 : float
      Passed on as it is.

    direction : QCanvasPainter.PathWinding
      Passed on as its number. May be left out, as in Qt: it is then
      QCanvasPainter.PathWinding.ClockWise.

    connection : QCanvasPainter.PathConnection
      Passed on as its number. May be left out, as in Qt: it is then
      QCanvasPainter.PathConnection.Connected.
    """
    #  void QCanvasPath::arc(qreal centerX, qreal centerY, qreal radius,
    #      qreal a0, qreal a1, QCanvasPainter::PathWinding direction,
    #      QCanvasPainter::PathConnection connection)
    self.uglySide.call(
        'ritual_ZN11QCanvasPath3arcEdddddN14QCanvasPainter11PathWindingENS0'
        '_14PathConnectionE',
        centerX, centerY, radius, a0, a1, direction.value, connection.value,
    )

  @overload(QPointF, float, float, float)
  @overload(QPointF, float, float, float, QCanvasPainter.PathWinding)
  @overload(
      QPointF, float, float, float, QCanvasPainter.PathWinding,
      QCanvasPainter.PathConnection,
  )
  def arc(
      self,
      centerPoint: QPointF,
      radius: float,
      a0: float,
      a1: float,
      direction: QCanvasPainter.PathWinding = (
          QCanvasPainter.PathWinding.ClockWise),
      connection: QCanvasPainter.PathConnection = (
          QCanvasPainter.PathConnection.Connected),
  ) -> None:
    """
    Calls Qt's 'void QCanvasPath::arc(QPointF centerPoint, qreal radius,
    qreal a0, qreal a1, QCanvasPainter::PathWinding direction,
    QCanvasPainter::PathConnection connection)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#arc

    Parameters
    ----------

    centerPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    radius : float
      Passed on as it is.

    a0 : float
      Passed on as it is.

    a1 : float
      Passed on as it is.

    direction : QCanvasPainter.PathWinding
      Passed on as its number. May be left out, as in Qt: it is then
      QCanvasPainter.PathWinding.ClockWise.

    connection : QCanvasPainter.PathConnection
      Passed on as its number. May be left out, as in Qt: it is then
      QCanvasPainter.PathConnection.Connected.
    """
    #  void QCanvasPath::arc(QPointF centerPoint, qreal radius, qreal a0,
    #      qreal a1, QCanvasPainter::PathWinding direction,
    #      QCanvasPainter::PathConnection connection)
    self.uglySide.call(
        'ritual_ZN11QCanvasPath3arcE7QPointFdddN14QCanvasPainter11PathWindi'
        'ngENS1_14PathConnectionE',
        self._valueOf(centerPoint, 'QPointF'), radius, a0, a1,
        direction.value, connection.value,
    )

  @overload(float, float, float, float)
  def rect(self, x: float, y: float, width: float, height: float) -> None:
    """
    Calls Qt's 'void QCanvasPath::rect(qreal x, qreal y, qreal width, qreal
    height)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#rect

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.
    """
    #  void QCanvasPath::rect(qreal x, qreal y, qreal width, qreal height)
    self.uglySide.call(
        'ritual_ZN11QCanvasPath4rectEdddd', x, y, width, height,
    )

  @overload(QRectF)
  def rect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QCanvasPath::rect(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#rect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QCanvasPath::rect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN11QCanvasPath4rectERK6QRectF', self._valueOf(rect),
    )

  @overload(float, float, float, float, float)
  def roundRect(
      self,
      x: float,
      y: float,
      width: float,
      height: float,
      radius: float,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPath::roundRect(qreal x, qreal y, qreal width,
    qreal height, qreal radius)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#roundRect

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.

    radius : float
      Passed on as it is.
    """
    #  void QCanvasPath::roundRect(qreal x, qreal y, qreal width, qreal
    #      height, qreal radius)
    self.uglySide.call(
        'ritual_ZN11QCanvasPath9roundRectEddddd',
        x, y, width, height, radius,
    )

  @overload(QRectF, float)
  def roundRect(self, rect: QRectF, radius: float) -> None:
    """
    Calls Qt's 'void QCanvasPath::roundRect(const QRectF &rect, qreal
    radius)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#roundRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    radius : float
      Passed on as it is.
    """
    #  void QCanvasPath::roundRect(const QRectF &rect, qreal radius)
    self.uglySide.call(
        'ritual_ZN11QCanvasPath9roundRectERK6QRectFd',
        self._valueOf(rect), radius,
    )

  @overload(float, float, float, float, float, float, float, float)
  def roundRect(
      self,
      x: float,
      y: float,
      width: float,
      height: float,
      radiusTopLeft: float,
      radiusTopRight: float,
      radiusBottomRight: float,
      radiusBottomLeft: float,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPath::roundRect(qreal x, qreal y, qreal width,
    qreal height, qreal radiusTopLeft, qreal radiusTopRight, qreal
    radiusBottomRight, qreal radiusBottomLeft)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#roundRect

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.

    radiusTopLeft : float
      Passed on as it is.

    radiusTopRight : float
      Passed on as it is.

    radiusBottomRight : float
      Passed on as it is.

    radiusBottomLeft : float
      Passed on as it is.
    """
    #  void QCanvasPath::roundRect(qreal x, qreal y, qreal width, qreal
    #      height, qreal radiusTopLeft, qreal radiusTopRight, qreal
    #      radiusBottomRight, qreal radiusBottomLeft)
    self.uglySide.call(
        'ritual_ZN11QCanvasPath9roundRectEdddddddd',
        x, y, width, height, radiusTopLeft, radiusTopRight,
        radiusBottomRight, radiusBottomLeft,
    )

  @overload(QRectF, float, float, float, float)
  def roundRect(
      self,
      rect: QRectF,
      radiusTopLeft: float,
      radiusTopRight: float,
      radiusBottomRight: float,
      radiusBottomLeft: float,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPath::roundRect(const QRectF &rect, qreal
    radiusTopLeft, qreal radiusTopRight, qreal radiusBottomRight, qreal
    radiusBottomLeft)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#roundRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    radiusTopLeft : float
      Passed on as it is.

    radiusTopRight : float
      Passed on as it is.

    radiusBottomRight : float
      Passed on as it is.

    radiusBottomLeft : float
      Passed on as it is.
    """
    #  void QCanvasPath::roundRect(const QRectF &rect, qreal radiusTopLeft,
    #      qreal radiusTopRight, qreal radiusBottomRight, qreal
    #      radiusBottomLeft)
    self.uglySide.call(
        'ritual_ZN11QCanvasPath9roundRectERK6QRectFdddd',
        self._valueOf(rect), radiusTopLeft, radiusTopRight,
        radiusBottomRight, radiusBottomLeft,
    )

  @overload(float, float, float, float)
  def ellipse(
      self,
      x: float,
      y: float,
      radiusX: float,
      radiusY: float,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPath::ellipse(qreal x, qreal y, qreal radiusX,
    qreal radiusY)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#ellipse

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    radiusX : float
      Passed on as it is.

    radiusY : float
      Passed on as it is.
    """
    #  void QCanvasPath::ellipse(qreal x, qreal y, qreal radiusX, qreal
    #      radiusY)
    self.uglySide.call(
        'ritual_ZN11QCanvasPath7ellipseEdddd', x, y, radiusX, radiusY,
    )

  @overload(QRectF)
  def ellipse(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QCanvasPath::ellipse(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#ellipse

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QCanvasPath::ellipse(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN11QCanvasPath7ellipseERK6QRectF', self._valueOf(rect),
    )

  @overload(float, float, float)
  def circle(self, x: float, y: float, radius: float) -> None:
    """
    Calls Qt's 'void QCanvasPath::circle(qreal x, qreal y, qreal radius)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#circle

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    radius : float
      Passed on as it is.
    """
    #  void QCanvasPath::circle(qreal x, qreal y, qreal radius)
    self.uglySide.call('ritual_ZN11QCanvasPath6circleEddd', x, y, radius)

  @overload(QPointF, float)
  def circle(self, centerPoint: QPointF, radius: float) -> None:
    """
    Calls Qt's 'void QCanvasPath::circle(QPointF centerPoint, qreal radius)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#circle

    Parameters
    ----------

    centerPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    radius : float
      Passed on as it is.
    """
    #  void QCanvasPath::circle(QPointF centerPoint, qreal radius)
    self.uglySide.call(
        'ritual_ZN11QCanvasPath6circleE7QPointFd',
        self._valueOf(centerPoint, 'QPointF'), radius,
    )

  def beginSolidSubPath(self) -> None:
    """
    Calls Qt's 'void QCanvasPath::beginSolidSubPath()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#beginSolidSubPath
    """
    #  void QCanvasPath::beginSolidSubPath()
    self.uglySide.call('ritual_ZN11QCanvasPath17beginSolidSubPathEv')

  def beginHoleSubPath(self) -> None:
    """
    Calls Qt's 'void QCanvasPath::beginHoleSubPath()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#beginHoleSubPath
    """
    #  void QCanvasPath::beginHoleSubPath()
    self.uglySide.call('ritual_ZN11QCanvasPath16beginHoleSubPathEv')

  @overload(THIS)
  @overload(THIS, QTransform)
  def addPath(
      self,
      path: QCanvasPath,
      transform: Optional[QTransform] = None,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPath::addPath(const QCanvasPath &path, const
    QTransform &transform)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#addPath

    Parameters
    ----------

    path : QCanvasPath
      Passed on as a value: Qt reads the C++ QCanvasPath, which stays
      Python's own.

    transform : Optional[QTransform]
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own. May be left out, as in Qt: a new 'QTransform()' is then passed on.
    """
    #  void QCanvasPath::addPath(const QCanvasPath &path, const QTransform
    #      &transform)
    if transform is None:
      from ..QtGui import QTransform
      transform = QTransform()
    self.uglySide.call(
        'ritual_ZN11QCanvasPath7addPathERKS_RK10QTransform',
        self._valueOf(path), self._valueOf(transform),
    )

  @overload(THIS, int, int)
  @overload(THIS, int, int, QTransform)
  def addPath(
      self,
      path: QCanvasPath,
      start: int,
      count: int,
      transform: Optional[QTransform] = None,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPath::addPath(const QCanvasPath &path, qsizetype
    start, qsizetype count, const QTransform &transform)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#addPath

    Parameters
    ----------

    path : QCanvasPath
      Passed on as a value: Qt reads the C++ QCanvasPath, which stays
      Python's own.

    start : int
      Passed on as it is.

    count : int
      Passed on as it is.

    transform : Optional[QTransform]
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own. May be left out, as in Qt: a new 'QTransform()' is then passed on.
    """
    #  void QCanvasPath::addPath(const QCanvasPath &path, qsizetype start,
    #      qsizetype count, const QTransform &transform)
    if transform is None:
      from ..QtGui import QTransform
      transform = QTransform()
    self.uglySide.call(
        'ritual_ZN11QCanvasPath7addPathERKS_xxRK10QTransform',
        self._valueOf(path), start, count, self._valueOf(transform),
    )

  @overload(str)
  @overload(str, QTransform)
  def addPath(
      self,
      svgPath: str,
      transform: Optional[QTransform] = None,
  ) -> None:
    """
    Calls Qt's 'void QCanvasPath::addPath(QStringView svgPath, const
    QTransform &transform)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#addPath

    Parameters
    ----------

    svgPath : str
      Passed on as it is: a QString is made of it for the call.

    transform : Optional[QTransform]
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own. May be left out, as in Qt: a new 'QTransform()' is then passed on.
    """
    #  void QCanvasPath::addPath(QStringView svgPath, const QTransform
    #      &transform)
    if transform is None:
      from ..QtGui import QTransform
      transform = QTransform()
    self.uglySide.call(
        'ritual_ZN11QCanvasPath7addPathE11QStringViewRK10QTransform',
        svgPath, self._valueOf(transform),
    )

  @overload(QPainterPath)
  def addPath(self, path: QPainterPath) -> None:
    """
    Calls Qt's 'void QCanvasPath::addPath(const QPainterPath &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#addPath

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.
    """
    #  void QCanvasPath::addPath(const QPainterPath &path)
    self.uglySide.call(
        'ritual_ZN11QCanvasPath7addPathERK12QPainterPath',
        self._valueOf(path),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QCanvasPath::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#clear
    """
    #  void QCanvasPath::clear()
    self.uglySide.call('ritual_ZN11QCanvasPath5clearEv')

  def squeeze(self) -> None:
    """
    Calls Qt's 'void QCanvasPath::squeeze()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#squeeze
    """
    #  void QCanvasPath::squeeze()
    self.uglySide.call('ritual_ZN11QCanvasPath7squeezeEv')

  @overload(int)
  @overload(int, int)
  def reserve(self, commandsSize: int, commandsDataSize: int = -1) -> None:
    """
    Calls Qt's 'void QCanvasPath::reserve(qsizetype commandsSize, qsizetype
    commandsDataSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspath.html#reserve

    Parameters
    ----------

    commandsSize : int
      Passed on as it is.

    commandsDataSize : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QCanvasPath::reserve(qsizetype commandsSize, qsizetype
    #      commandsDataSize)
    self.uglySide.call(
        'ritual_ZN11QCanvasPath7reserveExx', commandsSize, commandsDataSize,
    )

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QCanvasPathPrivate *QCanvasPath::d_func()': gives
      'QCanvasPathPrivate', which has no cute class yet.
    - Qt's 'const QCanvasPathPrivate *QCanvasPath::d_func() const': gives
      'QCanvasPathPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QCanvasPath.d_func' has no cute function yet. Qt's "
        "'QCanvasPathPrivate *QCanvasPath::d_func()': gives "
        "'QCanvasPathPrivate', which has no cute class yet. Qt's 'const "
        "QCanvasPathPrivate *QCanvasPath::d_func() const': gives "
        "'QCanvasPathPrivate', which has no cute class yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QCanvasPath::swap(QCanvasPath &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCanvasPath.swap' has no cute function yet. Qt's 'void "
        "QCanvasPath::swap(QCanvasPath &other)': takes a type Python has no "
        "way to hand over yet.")
