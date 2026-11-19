"""
QPainterPath binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qpainterpath.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import Qt
from ._q_font import QFont
from ..QtCore import QPointF
from ._q_polygon_f import QPolygonF
from ..QtCore import QRectF
from ._q_region import QRegion
from ._q_transform import QTransform
from ._q_painter_path_element_type import ElementType

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QPainterPath(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPainterPath: a plain Python object standing in front
  of one C++ QPainterPath.

  C++ hands a QPainterPath around as a copy, so every C++ QPainterPath behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPainterPath that has a ritual and that Python can
  call so far, 44 names in all: 'clear', 'reserve', 'capacity',
  'closeSubpath', 'moveTo', 'lineTo', 'arcMoveTo', 'arcTo', 'cubicTo',
  'quadTo', 'currentPosition', 'addRect', 'addEllipse', 'addPolygon',
  'addText', 'addPath', 'addRegion', 'addRoundedRect', 'connectPath',
  'contains', 'intersects', 'translate', 'translated', 'boundingRect',
  'controlPointRect', 'fillRule', 'setFillRule', 'isEmpty', 'toReversed',
  'toFillPolygon', 'elementCount', 'setElementPositionAt',
  'isCachingEnabled', 'setCachingEnabled', 'length', 'percentAtLength',
  'pointAtPercent', 'angleAtPercent', 'slopeAtPercent', 'trimmed', 'united',
  'intersected', 'subtracted', 'simplified'. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPainterPath::~QPainterPath()': the destructor: Python removes its
    C++ QPainterPath by it, and has no other use for it.
  - Qt's 'QPainterPath::Element QPainterPath::elementAt(int i) const': gives
    'QPainterPath::Element', which has no cute class yet.
  - Qt's 'bool QPainterPath::operator==(const QPainterPath &other) const': an
    operator, which is not reflected yet.
  - Qt's 'bool QPainterPath::operator!=(const QPainterPath &other) const': an
    operator, which is not reflected yet.
  - Qt's 'QPainterPath QPainterPath::operator&(const QPainterPath &other)
    const': an operator, which is not reflected yet.
  - Qt's 'QPainterPath QPainterPath::operator|(const QPainterPath &other)
    const': an operator, which is not reflected yet.
  - Qt's 'QPainterPath QPainterPath::operator+(const QPainterPath &other)
    const': an operator, which is not reflected yet.
  - Qt's 'QPainterPath QPainterPath::operator-(const QPainterPath &other)
    const': an operator, which is not reflected yet.

  What has no ritual
  ------------------

  16 of the 87 functions Qt declares: 10 takes or gives a type that cannot be
  passed yet; 6 private.

  What to expect
  --------------

  - The C++ QPainterPath is created at the first use, not by
    'QPainterPath(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPainterPath back gives a copy the ritual made for
    Python, in a new cute QPainterPath.
  """

  #  The enums Qt writes inside QPainterPath, and the names Qt has for the
  #  combinations of its flags enums.
  ElementType = ElementType

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPainterPath'

  #  Qt's '~QPainterPath()'. Naming it makes this a value class: Python owns
  #  every C++ QPainterPath behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QPainterPathD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def capacity(self) -> int:
    """
    Calls Qt's 'int QPainterPath::capacity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#capacity
    """
    #  int QPainterPath::capacity() const
    return self.uglySide.call('ritual_ZNK12QPainterPath8capacityEv')

  def currentPosition(self) -> QPointF:
    """
    Calls Qt's 'QPointF QPainterPath::currentPosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#currentPosition

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QPainterPath::currentPosition() const
    address = self.uglySide.call(
        'ritual_ZNK12QPainterPath15currentPositionEv',
    )
    return QPointF._cuteOwning(address)

  @overload(QPointF)
  def contains(self, pt: QPointF) -> bool:
    """
    Calls Qt's 'bool QPainterPath::contains(const QPointF &pt) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#contains

    Parameters
    ----------

    pt : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QPainterPath::contains(const QPointF &pt) const
    return self.uglySide.call(
        'ritual_ZNK12QPainterPath8containsERK7QPointF', self._valueOf(pt),
    )

  @overload(QRectF)
  def contains(self, rect: QRectF) -> bool:
    """
    Calls Qt's 'bool QPainterPath::contains(const QRectF &rect) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#contains

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  bool QPainterPath::contains(const QRectF &rect) const
    return self.uglySide.call(
        'ritual_ZNK12QPainterPath8containsERK6QRectF', self._valueOf(rect),
    )

  @overload(THIS)
  def contains(self, p: QPainterPath) -> bool:
    """
    Calls Qt's 'bool QPainterPath::contains(const QPainterPath &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#contains

    Parameters
    ----------

    p : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.
    """
    #  bool QPainterPath::contains(const QPainterPath &p) const
    return self.uglySide.call(
        'ritual_ZNK12QPainterPath8containsERKS_', self._valueOf(p),
    )

  @overload(QRectF)
  def intersects(self, rect: QRectF) -> bool:
    """
    Calls Qt's 'bool QPainterPath::intersects(const QRectF &rect) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#intersects

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  bool QPainterPath::intersects(const QRectF &rect) const
    return self.uglySide.call(
        'ritual_ZNK12QPainterPath10intersectsERK6QRectF',
        self._valueOf(rect),
    )

  @overload(THIS)
  def intersects(self, p: QPainterPath) -> bool:
    """
    Calls Qt's 'bool QPainterPath::intersects(const QPainterPath &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#intersects

    Parameters
    ----------

    p : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.
    """
    #  bool QPainterPath::intersects(const QPainterPath &p) const
    return self.uglySide.call(
        'ritual_ZNK12QPainterPath10intersectsERKS_', self._valueOf(p),
    )

  @overload(float, float)
  def translated(self, dx: float, dy: float) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QPainterPath::translated(qreal dx, qreal dy)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#translated

    Parameters
    ----------

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QPainterPath::translated(qreal dx, qreal dy) const
    address = self.uglySide.call(
        'ritual_ZNK12QPainterPath10translatedEdd', dx, dy,
    )
    return QPainterPath._cuteOwning(address)

  @overload(QPointF)
  def translated(self, offset: QPointF) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QPainterPath::translated(const QPointF &offset)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#translated

    Parameters
    ----------

    offset : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QPainterPath::translated(const QPointF &offset) const
    address = self.uglySide.call(
        'ritual_ZNK12QPainterPath10translatedERK7QPointF',
        self._valueOf(offset),
    )
    return QPainterPath._cuteOwning(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QPainterPath::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPainterPath::boundingRect() const
    address = self.uglySide.call('ritual_ZNK12QPainterPath12boundingRectEv')
    return QRectF._cuteOwning(address)

  def controlPointRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QPainterPath::controlPointRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#controlPointRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QPainterPath::controlPointRect() const
    address = self.uglySide.call(
        'ritual_ZNK12QPainterPath16controlPointRectEv',
    )
    return QRectF._cuteOwning(address)

  def fillRule(self) -> Qt.FillRule:
    """
    Calls Qt's 'Qt::FillRule QPainterPath::fillRule() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#fillRule

    Returns
    -------

    Qt.FillRule
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.FillRule(number)'
      gives.
    """
    #  Qt::FillRule QPainterPath::fillRule() const
    return Qt.FillRule(self.uglySide.call(
        'ritual_ZNK12QPainterPath8fillRuleEv',
    ))

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QPainterPath::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#isEmpty
    """
    #  bool QPainterPath::isEmpty() const
    return self.uglySide.call('ritual_ZNK12QPainterPath7isEmptyEv')

  def toReversed(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QPainterPath::toReversed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#toReversed

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QPainterPath::toReversed() const
    address = self.uglySide.call('ritual_ZNK12QPainterPath10toReversedEv')
    return QPainterPath._cuteOwning(address)

  @overload()
  @overload(QTransform)
  def toFillPolygon(self, matrix: Optional[QTransform] = None) -> QPolygonF:
    """
    Calls Qt's 'QPolygonF QPainterPath::toFillPolygon(const QTransform
    &matrix) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#toFillPolygon

    Parameters
    ----------

    matrix : Optional[QTransform]
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own. May be left out, as in Qt: a new 'QTransform()' is then passed on.

    Returns
    -------

    QPolygonF
      A new cute QPolygonF around the copy Qt gave back. Python owns it.
    """
    #  QPolygonF QPainterPath::toFillPolygon(const QTransform &matrix) const
    if matrix is None:
      matrix = QTransform()
    address = self.uglySide.call(
        'ritual_ZNK12QPainterPath13toFillPolygonERK10QTransform',
        self._valueOf(matrix),
    )
    return QPolygonF._cuteOwning(address)

  def elementCount(self) -> int:
    """
    Calls Qt's 'int QPainterPath::elementCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#elementCount
    """
    #  int QPainterPath::elementCount() const
    return self.uglySide.call('ritual_ZNK12QPainterPath12elementCountEv')

  def isCachingEnabled(self) -> bool:
    """
    Calls Qt's 'bool QPainterPath::isCachingEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#isCachingEnabled
    """
    #  bool QPainterPath::isCachingEnabled() const
    return self.uglySide.call('ritual_ZNK12QPainterPath16isCachingEnabledEv')

  def length(self) -> float:
    """
    Calls Qt's 'qreal QPainterPath::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#length
    """
    #  qreal QPainterPath::length() const
    return self.uglySide.call('ritual_ZNK12QPainterPath6lengthEv')

  @overload(float)
  def percentAtLength(self, len: float) -> float:
    """
    Calls Qt's 'qreal QPainterPath::percentAtLength(qreal len) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#percentAtLength

    Parameters
    ----------

    len : float
      Passed on as it is.
    """
    #  qreal QPainterPath::percentAtLength(qreal len) const
    return self.uglySide.call(
        'ritual_ZNK12QPainterPath15percentAtLengthEd', len,
    )

  @overload(float)
  def pointAtPercent(self, t: float) -> QPointF:
    """
    Calls Qt's 'QPointF QPainterPath::pointAtPercent(qreal t) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#pointAtPercent

    Parameters
    ----------

    t : float
      Passed on as it is.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QPainterPath::pointAtPercent(qreal t) const
    address = self.uglySide.call(
        'ritual_ZNK12QPainterPath14pointAtPercentEd', t,
    )
    return QPointF._cuteOwning(address)

  @overload(float)
  def angleAtPercent(self, t: float) -> float:
    """
    Calls Qt's 'qreal QPainterPath::angleAtPercent(qreal t) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#angleAtPercent

    Parameters
    ----------

    t : float
      Passed on as it is.
    """
    #  qreal QPainterPath::angleAtPercent(qreal t) const
    return self.uglySide.call(
        'ritual_ZNK12QPainterPath14angleAtPercentEd', t,
    )

  @overload(float)
  def slopeAtPercent(self, t: float) -> float:
    """
    Calls Qt's 'qreal QPainterPath::slopeAtPercent(qreal t) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#slopeAtPercent

    Parameters
    ----------

    t : float
      Passed on as it is.
    """
    #  qreal QPainterPath::slopeAtPercent(qreal t) const
    return self.uglySide.call(
        'ritual_ZNK12QPainterPath14slopeAtPercentEd', t,
    )

  @overload(float, float)
  @overload(float, float, float)
  def trimmed(
      self,
      fromFraction: float,
      toFraction: float,
      offset: float = 0.0,
  ) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QPainterPath::trimmed(qreal fromFraction, qreal
    toFraction, qreal offset) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#trimmed

    Parameters
    ----------

    fromFraction : float
      Passed on as it is.

    toFraction : float
      Passed on as it is.

    offset : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QPainterPath::trimmed(qreal fromFraction, qreal
    #      toFraction, qreal offset) const
    address = self.uglySide.call(
        'ritual_ZNK12QPainterPath7trimmedEddd',
        fromFraction, toFraction, offset,
    )
    return QPainterPath._cuteOwning(address)

  @overload(THIS)
  def united(self, r: QPainterPath) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QPainterPath::united(const QPainterPath &r)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#united

    Parameters
    ----------

    r : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QPainterPath::united(const QPainterPath &r) const
    address = self.uglySide.call(
        'ritual_ZNK12QPainterPath6unitedERKS_', self._valueOf(r),
    )
    return QPainterPath._cuteOwning(address)

  @overload(THIS)
  def intersected(self, r: QPainterPath) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QPainterPath::intersected(const QPainterPath &r)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#intersected

    Parameters
    ----------

    r : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QPainterPath::intersected(const QPainterPath &r) const
    address = self.uglySide.call(
        'ritual_ZNK12QPainterPath11intersectedERKS_', self._valueOf(r),
    )
    return QPainterPath._cuteOwning(address)

  @overload(THIS)
  def subtracted(self, r: QPainterPath) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QPainterPath::subtracted(const QPainterPath &r)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#subtracted

    Parameters
    ----------

    r : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QPainterPath::subtracted(const QPainterPath &r) const
    address = self.uglySide.call(
        'ritual_ZNK12QPainterPath10subtractedERKS_', self._valueOf(r),
    )
    return QPainterPath._cuteOwning(address)

  def simplified(self) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QPainterPath::simplified() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#simplified

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QPainterPath::simplified() const
    address = self.uglySide.call('ritual_ZNK12QPainterPath10simplifiedEv')
    return QPainterPath._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.FillRule)
  def setFillRule(self, fillRule: Qt.FillRule) -> None:
    """
    Calls Qt's 'void QPainterPath::setFillRule(Qt::FillRule fillRule)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#setFillRule

    Parameters
    ----------

    fillRule : Qt.FillRule
      Passed on as its number.
    """
    #  void QPainterPath::setFillRule(Qt::FillRule fillRule)
    self.uglySide.call(
        'ritual_ZN12QPainterPath11setFillRuleEN2Qt8FillRuleE',
        fillRule.value,
    )

  @overload(int, float, float)
  def setElementPositionAt(self, i: int, x: float, y: float) -> None:
    """
    Calls Qt's 'void QPainterPath::setElementPositionAt(int i, qreal x, qreal
    y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterpath.html#setElementPositionAt

    Parameters
    ----------

    i : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QPainterPath::setElementPositionAt(int i, qreal x, qreal y)
    self.uglySide.call(
        'ritual_ZN12QPainterPath20setElementPositionAtEidd', i, x, y,
    )

  @overload(bool)
  def setCachingEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QPainterPath::setCachingEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpainterpath.html#setCachingEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QPainterPath::setCachingEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN12QPainterPath17setCachingEnabledEb', enabled,
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
    Notes what was given, for Qt's 'QPainterPath::QPainterPath()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#QPainterPath
    """
    #  QPainterPath::QPainterPath()
    self._noteCreation(QPainterPath, lambda: Rituals.call(
        'ritual_ZN12QPainterPathC1Ev',
    ))

  @overload(QPointF)
  def __init__(self, startPoint: QPointF) -> None:
    """
    Notes what was given, for Qt's 'QPainterPath::QPainterPath(const QPointF
    &startPoint)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#QPainterPath

    Parameters
    ----------

    startPoint : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  QPainterPath::QPainterPath(const QPointF &startPoint)
    self._noteCreation(QPainterPath, lambda: Rituals.call(
        'ritual_ZN12QPainterPathC1ERK7QPointF', self._valueOf(startPoint),
    ))

  @overload(THIS)
  def __init__(self, other: QPainterPath) -> None:
    """
    Notes what was given, for Qt's 'QPainterPath::QPainterPath(const
    QPainterPath &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#QPainterPath

    Parameters
    ----------

    other : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.
    """
    #  QPainterPath::QPainterPath(const QPainterPath &other)
    self._noteCreation(QPainterPath, lambda: Rituals.call(
        'ritual_ZN12QPainterPathC1ERKS_', self._valueOf(other),
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QPainterPath::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#clear
    """
    #  void QPainterPath::clear()
    self.uglySide.call('ritual_ZN12QPainterPath5clearEv')

  @overload(int)
  def reserve(self, size: int) -> None:
    """
    Calls Qt's 'void QPainterPath::reserve(int size)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#reserve

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QPainterPath::reserve(int size)
    self.uglySide.call('ritual_ZN12QPainterPath7reserveEi', size)

  def closeSubpath(self) -> None:
    """
    Calls Qt's 'void QPainterPath::closeSubpath()'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#closeSubpath
    """
    #  void QPainterPath::closeSubpath()
    self.uglySide.call('ritual_ZN12QPainterPath12closeSubpathEv')

  @overload(QPointF)
  def moveTo(self, p: QPointF) -> None:
    """
    Calls Qt's 'void QPainterPath::moveTo(const QPointF &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#moveTo

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QPainterPath::moveTo(const QPointF &p)
    self.uglySide.call(
        'ritual_ZN12QPainterPath6moveToERK7QPointF', self._valueOf(p),
    )

  @overload(float, float)
  def moveTo(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QPainterPath::moveTo(qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#moveTo

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QPainterPath::moveTo(qreal x, qreal y)
    self.uglySide.call('ritual_ZN12QPainterPath6moveToEdd', x, y)

  @overload(QPointF)
  def lineTo(self, p: QPointF) -> None:
    """
    Calls Qt's 'void QPainterPath::lineTo(const QPointF &p)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#lineTo

    Parameters
    ----------

    p : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QPainterPath::lineTo(const QPointF &p)
    self.uglySide.call(
        'ritual_ZN12QPainterPath6lineToERK7QPointF', self._valueOf(p),
    )

  @overload(float, float)
  def lineTo(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QPainterPath::lineTo(qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#lineTo

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QPainterPath::lineTo(qreal x, qreal y)
    self.uglySide.call('ritual_ZN12QPainterPath6lineToEdd', x, y)

  @overload(QRectF, float)
  def arcMoveTo(self, rect: QRectF, angle: float) -> None:
    """
    Calls Qt's 'void QPainterPath::arcMoveTo(const QRectF &rect, qreal
    angle)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#arcMoveTo

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    angle : float
      Passed on as it is.
    """
    #  void QPainterPath::arcMoveTo(const QRectF &rect, qreal angle)
    self.uglySide.call(
        'ritual_ZN12QPainterPath9arcMoveToERK6QRectFd',
        self._valueOf(rect), angle,
    )

  @overload(float, float, float, float, float)
  def arcMoveTo(
      self,
      x: float,
      y: float,
      w: float,
      h: float,
      angle: float,
  ) -> None:
    """
    Calls Qt's 'void QPainterPath::arcMoveTo(qreal x, qreal y, qreal w, qreal
    h, qreal angle)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#arcMoveTo

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.

    angle : float
      Passed on as it is.
    """
    #  void QPainterPath::arcMoveTo(qreal x, qreal y, qreal w, qreal h, qreal
    #      angle)
    self.uglySide.call(
        'ritual_ZN12QPainterPath9arcMoveToEddddd', x, y, w, h, angle,
    )

  @overload(QRectF, float, float)
  def arcTo(self, rect: QRectF, startAngle: float, arcLength: float) -> None:
    """
    Calls Qt's 'void QPainterPath::arcTo(const QRectF &rect, qreal
    startAngle, qreal arcLength)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#arcTo

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    startAngle : float
      Passed on as it is.

    arcLength : float
      Passed on as it is.
    """
    #  void QPainterPath::arcTo(const QRectF &rect, qreal startAngle, qreal
    #      arcLength)
    self.uglySide.call(
        'ritual_ZN12QPainterPath5arcToERK6QRectFdd',
        self._valueOf(rect), startAngle, arcLength,
    )

  @overload(float, float, float, float, float, float)
  def arcTo(
      self,
      x: float,
      y: float,
      w: float,
      h: float,
      startAngle: float,
      arcLength: float,
  ) -> None:
    """
    Calls Qt's 'void QPainterPath::arcTo(qreal x, qreal y, qreal w, qreal h,
    qreal startAngle, qreal arcLength)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#arcTo

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.

    startAngle : float
      Passed on as it is.

    arcLength : float
      Passed on as it is.
    """
    #  void QPainterPath::arcTo(qreal x, qreal y, qreal w, qreal h, qreal
    #      startAngle, qreal arcLength)
    self.uglySide.call(
        'ritual_ZN12QPainterPath5arcToEdddddd',
        x, y, w, h, startAngle, arcLength,
    )

  @overload(QPointF, QPointF, QPointF)
  def cubicTo(
      self,
      ctrlPt1: QPointF,
      ctrlPt2: QPointF,
      endPt: QPointF,
  ) -> None:
    """
    Calls Qt's 'void QPainterPath::cubicTo(const QPointF &ctrlPt1, const
    QPointF &ctrlPt2, const QPointF &endPt)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#cubicTo

    Parameters
    ----------

    ctrlPt1 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    ctrlPt2 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    endPt : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QPainterPath::cubicTo(const QPointF &ctrlPt1, const QPointF
    #      &ctrlPt2, const QPointF &endPt)
    self.uglySide.call(
        'ritual_ZN12QPainterPath7cubicToERK7QPointFS2_S2_',
        self._valueOf(ctrlPt1), self._valueOf(ctrlPt2), self._valueOf(endPt),
    )

  @overload(float, float, float, float, float, float)
  def cubicTo(
      self,
      ctrlPt1x: float,
      ctrlPt1y: float,
      ctrlPt2x: float,
      ctrlPt2y: float,
      endPtx: float,
      endPty: float,
  ) -> None:
    """
    Calls Qt's 'void QPainterPath::cubicTo(qreal ctrlPt1x, qreal ctrlPt1y,
    qreal ctrlPt2x, qreal ctrlPt2y, qreal endPtx, qreal endPty)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#cubicTo

    Parameters
    ----------

    ctrlPt1x : float
      Passed on as it is.

    ctrlPt1y : float
      Passed on as it is.

    ctrlPt2x : float
      Passed on as it is.

    ctrlPt2y : float
      Passed on as it is.

    endPtx : float
      Passed on as it is.

    endPty : float
      Passed on as it is.
    """
    #  void QPainterPath::cubicTo(qreal ctrlPt1x, qreal ctrlPt1y, qreal
    #      ctrlPt2x, qreal ctrlPt2y, qreal endPtx, qreal endPty)
    self.uglySide.call(
        'ritual_ZN12QPainterPath7cubicToEdddddd',
        ctrlPt1x, ctrlPt1y, ctrlPt2x, ctrlPt2y, endPtx, endPty,
    )

  @overload(QPointF, QPointF)
  def quadTo(self, ctrlPt: QPointF, endPt: QPointF) -> None:
    """
    Calls Qt's 'void QPainterPath::quadTo(const QPointF &ctrlPt, const
    QPointF &endPt)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#quadTo

    Parameters
    ----------

    ctrlPt : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    endPt : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QPainterPath::quadTo(const QPointF &ctrlPt, const QPointF &endPt)
    self.uglySide.call(
        'ritual_ZN12QPainterPath6quadToERK7QPointFS2_',
        self._valueOf(ctrlPt), self._valueOf(endPt),
    )

  @overload(float, float, float, float)
  def quadTo(
      self,
      ctrlPtx: float,
      ctrlPty: float,
      endPtx: float,
      endPty: float,
  ) -> None:
    """
    Calls Qt's 'void QPainterPath::quadTo(qreal ctrlPtx, qreal ctrlPty, qreal
    endPtx, qreal endPty)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#quadTo

    Parameters
    ----------

    ctrlPtx : float
      Passed on as it is.

    ctrlPty : float
      Passed on as it is.

    endPtx : float
      Passed on as it is.

    endPty : float
      Passed on as it is.
    """
    #  void QPainterPath::quadTo(qreal ctrlPtx, qreal ctrlPty, qreal endPtx,
    #      qreal endPty)
    self.uglySide.call(
        'ritual_ZN12QPainterPath6quadToEdddd',
        ctrlPtx, ctrlPty, endPtx, endPty,
    )

  @overload(QRectF)
  def addRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QPainterPath::addRect(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#addRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QPainterPath::addRect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN12QPainterPath7addRectERK6QRectF', self._valueOf(rect),
    )

  @overload(float, float, float, float)
  def addRect(self, x: float, y: float, w: float, h: float) -> None:
    """
    Calls Qt's 'void QPainterPath::addRect(qreal x, qreal y, qreal w, qreal
    h)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#addRect

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.
    """
    #  void QPainterPath::addRect(qreal x, qreal y, qreal w, qreal h)
    self.uglySide.call('ritual_ZN12QPainterPath7addRectEdddd', x, y, w, h)

  @overload(QRectF)
  def addEllipse(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QPainterPath::addEllipse(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#addEllipse

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QPainterPath::addEllipse(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN12QPainterPath10addEllipseERK6QRectF', self._valueOf(rect),
    )

  @overload(float, float, float, float)
  def addEllipse(self, x: float, y: float, w: float, h: float) -> None:
    """
    Calls Qt's 'void QPainterPath::addEllipse(qreal x, qreal y, qreal w,
    qreal h)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#addEllipse

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.
    """
    #  void QPainterPath::addEllipse(qreal x, qreal y, qreal w, qreal h)
    self.uglySide.call(
        'ritual_ZN12QPainterPath10addEllipseEdddd', x, y, w, h,
    )

  @overload(QPointF, float, float)
  def addEllipse(self, center: QPointF, rx: float, ry: float) -> None:
    """
    Calls Qt's 'void QPainterPath::addEllipse(const QPointF &center, qreal
    rx, qreal ry)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#addEllipse

    Parameters
    ----------

    center : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    rx : float
      Passed on as it is.

    ry : float
      Passed on as it is.
    """
    #  void QPainterPath::addEllipse(const QPointF &center, qreal rx, qreal
    #      ry)
    self.uglySide.call(
        'ritual_ZN12QPainterPath10addEllipseERK7QPointFdd',
        self._valueOf(center), rx, ry,
    )

  @overload(QPolygonF)
  def addPolygon(self, polygon: QPolygonF) -> None:
    """
    Calls Qt's 'void QPainterPath::addPolygon(const QPolygonF &polygon)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#addPolygon

    Parameters
    ----------

    polygon : QPolygonF
      Passed on as a value: Qt reads the C++ QPolygonF, which stays Python's
      own.
    """
    #  void QPainterPath::addPolygon(const QPolygonF &polygon)
    self.uglySide.call(
        'ritual_ZN12QPainterPath10addPolygonERK9QPolygonF',
        self._valueOf(polygon),
    )

  @overload(QPointF, QFont, str)
  def addText(self, point: QPointF, f: QFont, text: str) -> None:
    """
    Calls Qt's 'void QPainterPath::addText(const QPointF &point, const QFont
    &f, const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#addText

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    f : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPainterPath::addText(const QPointF &point, const QFont &f, const
    #      QString &text)
    self.uglySide.call(
        'ritual_ZN12QPainterPath7addTextERK7QPointFRK5QFontRK7QString',
        self._valueOf(point), self._valueOf(f), text,
    )

  @overload(float, float, QFont, str)
  def addText(self, x: float, y: float, f: QFont, text: str) -> None:
    """
    Calls Qt's 'void QPainterPath::addText(qreal x, qreal y, const QFont &f,
    const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#addText

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    f : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPainterPath::addText(qreal x, qreal y, const QFont &f, const
    #      QString &text)
    self.uglySide.call(
        'ritual_ZN12QPainterPath7addTextEddRK5QFontRK7QString',
        x, y, self._valueOf(f), text,
    )

  @overload(THIS)
  def addPath(self, path: QPainterPath) -> None:
    """
    Calls Qt's 'void QPainterPath::addPath(const QPainterPath &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#addPath

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.
    """
    #  void QPainterPath::addPath(const QPainterPath &path)
    self.uglySide.call(
        'ritual_ZN12QPainterPath7addPathERKS_', self._valueOf(path),
    )

  @overload(QRegion)
  def addRegion(self, region: QRegion) -> None:
    """
    Calls Qt's 'void QPainterPath::addRegion(const QRegion &region)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#addRegion

    Parameters
    ----------

    region : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QPainterPath::addRegion(const QRegion &region)
    self.uglySide.call(
        'ritual_ZN12QPainterPath9addRegionERK7QRegion',
        self._valueOf(region),
    )

  @overload(QRectF, float, float)
  @overload(QRectF, float, float, Qt.SizeMode)
  def addRoundedRect(
      self,
      rect: QRectF,
      xRadius: float,
      yRadius: float,
      mode: Qt.SizeMode = Qt.SizeMode.AbsoluteSize,
  ) -> None:
    """
    Calls Qt's 'void QPainterPath::addRoundedRect(const QRectF &rect, qreal
    xRadius, qreal yRadius, Qt::SizeMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#addRoundedRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    xRadius : float
      Passed on as it is.

    yRadius : float
      Passed on as it is.

    mode : Qt.SizeMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.SizeMode.AbsoluteSize.
    """
    #  void QPainterPath::addRoundedRect(const QRectF &rect, qreal xRadius,
    #      qreal yRadius, Qt::SizeMode mode)
    self.uglySide.call(
        'ritual_ZN12QPainterPath14addRoundedRectERK6QRectFddN2Qt8SizeModeE',
        self._valueOf(rect), xRadius, yRadius, mode.value,
    )

  @overload(float, float, float, float, float, float)
  @overload(float, float, float, float, float, float, Qt.SizeMode)
  def addRoundedRect(
      self,
      x: float,
      y: float,
      w: float,
      h: float,
      xRadius: float,
      yRadius: float,
      mode: Qt.SizeMode = Qt.SizeMode.AbsoluteSize,
  ) -> None:
    """
    Calls Qt's 'void QPainterPath::addRoundedRect(qreal x, qreal y, qreal w,
    qreal h, qreal xRadius, qreal yRadius, Qt::SizeMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#addRoundedRect

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.

    xRadius : float
      Passed on as it is.

    yRadius : float
      Passed on as it is.

    mode : Qt.SizeMode
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.SizeMode.AbsoluteSize.
    """
    #  void QPainterPath::addRoundedRect(qreal x, qreal y, qreal w, qreal h,
    #      qreal xRadius, qreal yRadius, Qt::SizeMode mode)
    self.uglySide.call(
        'ritual_ZN12QPainterPath14addRoundedRectEddddddN2Qt8SizeModeE',
        x, y, w, h, xRadius, yRadius, mode.value,
    )

  @overload(THIS)
  def connectPath(self, path: QPainterPath) -> None:
    """
    Calls Qt's 'void QPainterPath::connectPath(const QPainterPath &path)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#connectPath

    Parameters
    ----------

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.
    """
    #  void QPainterPath::connectPath(const QPainterPath &path)
    self.uglySide.call(
        'ritual_ZN12QPainterPath11connectPathERKS_', self._valueOf(path),
    )

  @overload(float, float)
  def translate(self, dx: float, dy: float) -> None:
    """
    Calls Qt's 'void QPainterPath::translate(qreal dx, qreal dy)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#translate

    Parameters
    ----------

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.
    """
    #  void QPainterPath::translate(qreal dx, qreal dy)
    self.uglySide.call('ritual_ZN12QPainterPath9translateEdd', dx, dy)

  @overload(QPointF)
  def translate(self, offset: QPointF) -> None:
    """
    Calls Qt's 'void QPainterPath::translate(const QPointF &offset)'.

    Qt's own words: https://doc.qt.io/qt-6/qpainterpath.html#translate

    Parameters
    ----------

    offset : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QPainterPath::translate(const QPointF &offset)
    self.uglySide.call(
        'ritual_ZN12QPainterPath9translateERK7QPointF',
        self._valueOf(offset),
    )
