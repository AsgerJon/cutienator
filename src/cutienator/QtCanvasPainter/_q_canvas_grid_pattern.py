"""
QCanvasGridPattern binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/qcanvasgridpattern.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDebug, QPointF, QSizeF
  from ..QtGui import QColor
  from . import QCanvasGridPatternPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCanvasGridPatternPrivate = WAIT['QCanvasGridPatternPrivate']
  QColor = WAIT['QColor']
  QDebug = WAIT['QDebug']
  QPointF = WAIT['QPointF']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCanvasGridPattern(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCanvasGridPattern: a plain Python object standing in
  front of one C++ QCanvasGridPattern.

  C++ hands a QCanvasGridPattern around as a copy, so every C++
  QCanvasGridPattern behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCanvasGridPattern that has a ritual and that Python
  can call so far, 18 names in all: 'startPosition', 'setStartPosition',
  'cellSize', 'setCellSize', 'lineWidth', 'setLineWidth', 'feather',
  'setFeather', 'rotation', 'setRotation', 'lineColor', 'setLineColor',
  'backgroundColor', 'setBackgroundColor', '__eq__', '__ne__', 'detach',
  '__rlshift__'. It can be made from Python, in 5 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCanvasGridPattern &QCanvasGridPattern::operator=(const
    QCanvasGridPattern &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QCanvasGridPattern::QCanvasGridPattern(QCanvasGridPattern &&a0)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QCanvasGridPattern
    &QCanvasGridPattern::operator=(QCanvasGridPattern &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QCanvasGridPattern::~QCanvasGridPattern()': the destructor: Python
    removes its C++ QCanvasGridPattern by it, and has no other use for it.
  - Qt's 'QCanvasBrush QCanvasGridPattern::operator QCanvasBrush() const': an
    operator Python has no name for.
  - Qt's 'QVariant QCanvasGridPattern::operator QVariant() const': an
    operator Python has no name for.
  - Qt's 'void QCanvasGridPattern::swap(QCanvasGridPattern &other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QDataStream &operator<<(QDataStream &a0, const QCanvasGridPattern
    &a1)': takes a type Python has no way to hand over yet.
  - Qt's 'QDataStream &operator>>(QDataStream &a0, QCanvasGridPattern &a1)':
    an operator between other classes, written inside this one.

  What to expect
  --------------

  - The C++ QCanvasGridPattern is created at the first use, not by
    'QCanvasGridPattern(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanvasGridPattern back gives a copy the ritual made
    for Python, in a new cute QCanvasGridPattern.
  - Each name of Qt's QCanvasGridPattern that has no cute function yet,
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
  __qt_class__ = 'QCanvasGridPattern'

  #  Qt's '~QCanvasGridPattern()'. Naming it makes this a value class: Python
  #  owns every C++ QCanvasGridPattern behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QCanvasGridPatternD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def startPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QCanvasGridPattern::startPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgridpattern.html#startPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QCanvasGridPattern::startPosition() const
    address = self.uglySide.call(
        'ritual_ZNK18QCanvasGridPattern13startPositionEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def cellSize(self) -> QSizeF:
    """
    Calls Qt's 'QSizeF QCanvasGridPattern::cellSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasgridpattern.html#cellSize

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QCanvasGridPattern::cellSize() const
    address = self.uglySide.call('ritual_ZNK18QCanvasGridPattern8cellSizeEv')
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  def lineWidth(self) -> float:
    """
    Calls Qt's 'qreal QCanvasGridPattern::lineWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasgridpattern.html#lineWidth
    """
    #  qreal QCanvasGridPattern::lineWidth() const
    return self.uglySide.call('ritual_ZNK18QCanvasGridPattern9lineWidthEv')

  def feather(self) -> float:
    """
    Calls Qt's 'qreal QCanvasGridPattern::feather() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasgridpattern.html#feather
    """
    #  qreal QCanvasGridPattern::feather() const
    return self.uglySide.call('ritual_ZNK18QCanvasGridPattern7featherEv')

  def rotation(self) -> float:
    """
    Calls Qt's 'qreal QCanvasGridPattern::rotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasgridpattern.html#rotation
    """
    #  qreal QCanvasGridPattern::rotation() const
    return self.uglySide.call('ritual_ZNK18QCanvasGridPattern8rotationEv')

  def lineColor(self) -> QColor:
    """
    Calls Qt's 'QColor QCanvasGridPattern::lineColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasgridpattern.html#lineColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QCanvasGridPattern::lineColor() const
    address = self.uglySide.call(
        'ritual_ZNK18QCanvasGridPattern9lineColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def backgroundColor(self) -> QColor:
    """
    Calls Qt's 'QColor QCanvasGridPattern::backgroundColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgridpattern.html#backgroundColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QCanvasGridPattern::backgroundColor() const
    address = self.uglySide.call(
        'ritual_ZNK18QCanvasGridPattern15backgroundColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float, float)
  def setStartPosition(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QCanvasGridPattern::setStartPosition(qreal x, qreal y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgridpattern.html#setStartPosition

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QCanvasGridPattern::setStartPosition(qreal x, qreal y)
    self.uglySide.call(
        'ritual_ZN18QCanvasGridPattern16setStartPositionEdd', x, y,
    )

  @overload(QPointF)
  def setStartPosition(self, point: QPointF) -> None:
    """
    Calls Qt's 'void QCanvasGridPattern::setStartPosition(QPointF point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgridpattern.html#setStartPosition

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QCanvasGridPattern::setStartPosition(QPointF point)
    self.uglySide.call(
        'ritual_ZN18QCanvasGridPattern16setStartPositionE7QPointF',
        self._valueOf(point, 'QPointF'),
    )

  @overload(float, float)
  def setCellSize(self, width: float, height: float) -> None:
    """
    Calls Qt's 'void QCanvasGridPattern::setCellSize(qreal width, qreal
    height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgridpattern.html#setCellSize

    Parameters
    ----------

    width : float
      Passed on as it is.

    height : float
      Passed on as it is.
    """
    #  void QCanvasGridPattern::setCellSize(qreal width, qreal height)
    self.uglySide.call(
        'ritual_ZN18QCanvasGridPattern11setCellSizeEdd', width, height,
    )

  @overload(QSizeF)
  def setCellSize(self, size: QSizeF) -> None:
    """
    Calls Qt's 'void QCanvasGridPattern::setCellSize(QSizeF size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgridpattern.html#setCellSize

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QCanvasGridPattern::setCellSize(QSizeF size)
    self.uglySide.call(
        'ritual_ZN18QCanvasGridPattern11setCellSizeE6QSizeF',
        self._valueOf(size),
    )

  @overload(float)
  def setLineWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QCanvasGridPattern::setLineWidth(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgridpattern.html#setLineWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QCanvasGridPattern::setLineWidth(qreal width)
    self.uglySide.call(
        'ritual_ZN18QCanvasGridPattern12setLineWidthEd', width,
    )

  @overload(float)
  def setFeather(self, feather: float) -> None:
    """
    Calls Qt's 'void QCanvasGridPattern::setFeather(qreal feather)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasgridpattern.html#setFeather

    Parameters
    ----------

    feather : float
      Passed on as it is.
    """
    #  void QCanvasGridPattern::setFeather(qreal feather)
    self.uglySide.call(
        'ritual_ZN18QCanvasGridPattern10setFeatherEd', feather,
    )

  @overload(float)
  def setRotation(self, rotation: float) -> None:
    """
    Calls Qt's 'void QCanvasGridPattern::setRotation(qreal rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgridpattern.html#setRotation

    Parameters
    ----------

    rotation : float
      Passed on as it is.
    """
    #  void QCanvasGridPattern::setRotation(qreal rotation)
    self.uglySide.call(
        'ritual_ZN18QCanvasGridPattern11setRotationEd', rotation,
    )

  @overload(QColor)
  def setLineColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QCanvasGridPattern::setLineColor(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgridpattern.html#setLineColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QCanvasGridPattern::setLineColor(QColor color)
    self.uglySide.call(
        'ritual_ZN18QCanvasGridPattern12setLineColorE6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setBackgroundColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QCanvasGridPattern::setBackgroundColor(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgridpattern.html#setBackgroundColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QCanvasGridPattern::setBackgroundColor(QColor color)
    self.uglySide.call(
        'ritual_ZN18QCanvasGridPattern18setBackgroundColorE6QColor',
        self._valueOf(color),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QCanvasGridPattern) -> bool:
    """
    Calls Qt's 'bool operator==(const QCanvasGridPattern &lhs, const
    QCanvasGridPattern &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasgridpattern.html#operator==

    Parameters
    ----------

    rhs : QCanvasGridPattern
      Passed on as a value: Qt reads the C++ QCanvasGridPattern, which stays
      Python's own.
    """
    #  bool operator==(const QCanvasGridPattern &lhs, const
    #      QCanvasGridPattern &rhs)
    return Rituals.call(
        'ritual_ZeqRK18QCanvasGridPatternS1_',
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
  def __ne__(self, rhs: QCanvasGridPattern) -> bool:
    """
    Calls Qt's 'bool operator!=(const QCanvasGridPattern &lhs, const
    QCanvasGridPattern &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasgridpattern.html#operator!=

    Parameters
    ----------

    rhs : QCanvasGridPattern
      Passed on as a value: Qt reads the C++ QCanvasGridPattern, which stays
      Python's own.
    """
    #  bool operator!=(const QCanvasGridPattern &lhs, const
    #      QCanvasGridPattern &rhs)
    return Rituals.call(
        'ritual_ZneRK18QCanvasGridPatternS1_',
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

  @overload(QDebug)
  def __rlshift__(self, a0: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug a0, const QCanvasGridPattern &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasgridpattern.html#operator<<

    Parameters
    ----------

    a0 : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug a0, const QCanvasGridPattern &a1)
    address = Rituals.call(
        'ritual_Zls6QDebugRK18QCanvasGridPattern',
        CuteMixin._valueOf(a0), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
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
    'QCanvasGridPattern::QCanvasGridPattern()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgridpattern.html#QCanvasGridPattern
    """
    #  QCanvasGridPattern::QCanvasGridPattern()
    self._noteCreation(QCanvasGridPattern, lambda: Rituals.call(
        'ritual_ZN18QCanvasGridPatternC1Ev',
    ))

  @overload(QPointF, QSizeF)
  def __init__(self, startPosition: QPointF, cellSize: QSizeF) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasGridPattern::QCanvasGridPattern(QPointF startPosition, QSizeF
    cellSize)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgridpattern.html#QCanvasGridPattern

    Parameters
    ----------

    startPosition : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    cellSize : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  QCanvasGridPattern::QCanvasGridPattern(QPointF startPosition, QSizeF
    #      cellSize)
    self._noteCreation(QCanvasGridPattern, lambda: Rituals.call(
        'ritual_ZN18QCanvasGridPatternC1E7QPointF6QSizeF',
        self._valueOf(startPosition, 'QPointF'), self._valueOf(cellSize),
    ))

  @overload(float, float, float, float)
  def __init__(
      self,
      startX: float,
      startY: float,
      cellWidth: float,
      cellHeight: float,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasGridPattern::QCanvasGridPattern(qreal startX, qreal startY, qreal
    cellWidth, qreal cellHeight)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgridpattern.html#QCanvasGridPattern

    Parameters
    ----------

    startX : float
      Passed on as it is.

    startY : float
      Passed on as it is.

    cellWidth : float
      Passed on as it is.

    cellHeight : float
      Passed on as it is.
    """
    #  QCanvasGridPattern::QCanvasGridPattern(qreal startX, qreal startY,
    #      qreal cellWidth, qreal cellHeight)
    self._noteCreation(QCanvasGridPattern, lambda: Rituals.call(
        'ritual_ZN18QCanvasGridPatternC1Edddd',
        startX, startY, cellWidth, cellHeight,
    ))

  @overload(THIS)
  def __init__(self, a0: QCanvasGridPattern) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasGridPattern::QCanvasGridPattern(const QCanvasGridPattern &a0)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgridpattern.html#QCanvasGridPattern

    Parameters
    ----------

    a0 : QCanvasGridPattern
      Passed on as a value: Qt reads the C++ QCanvasGridPattern, which stays
      Python's own.
    """
    #  QCanvasGridPattern::QCanvasGridPattern(const QCanvasGridPattern &a0)
    self._noteCreation(QCanvasGridPattern, lambda: Rituals.call(
        'ritual_ZN18QCanvasGridPatternC1ERKS_', self._valueOf(a0),
    ))

  @overload(QCanvasGridPatternPrivate)
  @overload(NoneType)
  def __init__(self, p: Optional[QCanvasGridPatternPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasGridPattern::QCanvasGridPattern(QCanvasGridPatternPrivate *p)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasgridpattern.html#QCanvasGridPattern

    Parameters
    ----------

    p : Optional[QCanvasGridPatternPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QCanvasGridPattern::QCanvasGridPattern(QCanvasGridPatternPrivate *p)
    self._noteCreation(QCanvasGridPattern, lambda: Rituals.call(
        'ritual_ZN18QCanvasGridPatternC1EP25QCanvasGridPatternPrivate',
        self._addressOf(p),
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

  def detach(self) -> None:
    """
    Calls Qt's 'void QCanvasGridPattern::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasgridpattern.html#detach
    """
    #  void QCanvasGridPattern::detach()
    self.uglySide.call('ritual_ZN18QCanvasGridPattern6detachEv')

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QCanvasGridPattern::swap(QCanvasGridPattern &other)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCanvasGridPattern.swap' has no cute function yet. Qt's 'void "
        "QCanvasGridPattern::swap(QCanvasGridPattern &other)': takes a type "
        "Python has no way to hand over yet.")
