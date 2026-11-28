"""
QPen binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qpen.h, Qt
#  6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QBrush, QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBrush = WAIT['QBrush']
  QColor = WAIT['QColor']


class QPen(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPen: a plain Python object standing in front of one
  C++ QPen.

  C++ hands a QPen around as a copy, so every C++ QPen behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPen that has a ritual and that Python can call so
  far, 28 names in all: 'style', 'setStyle', 'dashOffset', 'setDashOffset',
  'miterLimit', 'setMiterLimit', 'widthF', 'setWidthF', 'width', 'setWidth',
  'color', 'setColor', 'brush', 'setBrush', 'isSolid', 'capStyle',
  'setCapStyle', 'joinStyle', 'setJoinStyle', 'isCosmetic', 'setCosmetic',
  '__eq__', '__ne__', 'isDetached', 'isSolidDefaultLine',
  'doCompareEqualColor', 'doCompareEqualStyle', 'detach'. It can be made from
  Python, in 5 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPen::~QPen()': the destructor: Python removes its C++ QPen by it,
    and has no other use for it.
  - Qt's 'QPen &QPen::operator=(const QPen &pen)': assignment: Python binds a
    name and has no operator for it.
  - Qt's 'QPen::QPen(QPen &&other)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QPen &QPen::operator=(QPen &&other)': assignment: Python binds a
    name and has no operator for it.
  - Qt's 'void QPen::swap(QPen &other)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QPen &QPen::operator=(QColor color)': assignment: Python binds a
    name and has no operator for it.
  - Qt's 'QPen &QPen::operator=(Qt::PenStyle style)': assignment: Python
    binds a name and has no operator for it.
  - Qt's 'QList<qreal> QPen::dashPattern() const': gives a type Python has no
    way to take yet.
  - Qt's 'void QPen::setDashPattern(const QList<qreal> &pattern)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QVariant QPen::operator QVariant() const': an operator Python has
    no name for.
  - Qt's 'QDataStream &operator>>(QDataStream &a0, QPen &a1)': an operator
    between other classes, written inside this one.
  - Qt's 'QDataStream &operator<<(QDataStream &a0, const QPen &a1)': takes a
    type Python has no way to hand over yet.
  - Qt's 'bool operator==(const QColor &lhs, const QPen &rhs)': takes in
    Python what 'bool operator==(const QPen &lhs, const QColor &rhs)' takes.
  - Qt's 'bool operator!=(const QColor &lhs, const QPen &rhs)': takes in
    Python what 'bool operator!=(const QPen &lhs, const QColor &rhs)' takes.
  - Qt's 'bool operator==(const QPen &lhs, const Qt::PenStyle &rhs)': takes a
    type Python has no way to hand over yet.
  - Qt's 'bool operator!=(const QPen &lhs, const Qt::PenStyle &rhs)': takes a
    type Python has no way to hand over yet.
  - Qt's 'bool operator==(const Qt::PenStyle &lhs, const QPen &rhs)': takes a
    type Python has no way to hand over yet.
  - Qt's 'bool operator!=(const Qt::PenStyle &lhs, const QPen &rhs)': takes a
    type Python has no way to hand over yet.
  - Qt's 'DataPtr &QPen::data_ptr()': gives a type Python has no way to take
    yet.

  What to expect
  --------------

  - The C++ QPen is created at the first use, not by 'QPen(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPen back gives a copy the ritual made for Python, in
    a new cute QPen.
  - Each name of Qt's QPen that has no cute function yet, 'dashPattern',
    'data_ptr', 'setDashPattern', 'swap', holds a function that raises
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
  __qt_class__ = 'QPen'

  #  Qt's '~QPen()'. Naming it makes this a value class: Python owns every
  #  C++ QPen behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN4QPenD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def style(self) -> Qt.PenStyle:
    """
    Calls Qt's 'Qt::PenStyle QPen::style() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#style

    Returns
    -------

    Qt.PenStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.PenStyle(number)'
      gives.
    """
    #  Qt::PenStyle QPen::style() const
    return Qt.PenStyle(self.uglySide.call('ritual_ZNK4QPen5styleEv'))

  def dashOffset(self) -> float:
    """
    Calls Qt's 'qreal QPen::dashOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#dashOffset
    """
    #  qreal QPen::dashOffset() const
    return self.uglySide.call('ritual_ZNK4QPen10dashOffsetEv')

  def miterLimit(self) -> float:
    """
    Calls Qt's 'qreal QPen::miterLimit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#miterLimit
    """
    #  qreal QPen::miterLimit() const
    return self.uglySide.call('ritual_ZNK4QPen10miterLimitEv')

  def widthF(self) -> float:
    """
    Calls Qt's 'qreal QPen::widthF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#widthF
    """
    #  qreal QPen::widthF() const
    return self.uglySide.call('ritual_ZNK4QPen6widthFEv')

  def width(self) -> int:
    """
    Calls Qt's 'int QPen::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#width
    """
    #  int QPen::width() const
    return self.uglySide.call('ritual_ZNK4QPen5widthEv')

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QPen::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QPen::color() const
    address = self.uglySide.call('ritual_ZNK4QPen5colorEv')
    from . import QColor
    return QColor._cuteOwning(address)

  def brush(self) -> QBrush:
    """
    Calls Qt's 'QBrush QPen::brush() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#brush

    Returns
    -------

    QBrush
      A new cute QBrush around the copy Qt gave back. Python owns it.
    """
    #  QBrush QPen::brush() const
    address = self.uglySide.call('ritual_ZNK4QPen5brushEv')
    from . import QBrush
    return QBrush._cuteOwning(address)

  def isSolid(self) -> bool:
    """
    Calls Qt's 'bool QPen::isSolid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#isSolid
    """
    #  bool QPen::isSolid() const
    return self.uglySide.call('ritual_ZNK4QPen7isSolidEv')

  def capStyle(self) -> Qt.PenCapStyle:
    """
    Calls Qt's 'Qt::PenCapStyle QPen::capStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#capStyle

    Returns
    -------

    Qt.PenCapStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.PenCapStyle(number)'
      gives.
    """
    #  Qt::PenCapStyle QPen::capStyle() const
    return Qt.PenCapStyle(self.uglySide.call('ritual_ZNK4QPen8capStyleEv'))

  def joinStyle(self) -> Qt.PenJoinStyle:
    """
    Calls Qt's 'Qt::PenJoinStyle QPen::joinStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#joinStyle

    Returns
    -------

    Qt.PenJoinStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.PenJoinStyle(number)'
      gives.
    """
    #  Qt::PenJoinStyle QPen::joinStyle() const
    return Qt.PenJoinStyle(self.uglySide.call('ritual_ZNK4QPen9joinStyleEv'))

  def isCosmetic(self) -> bool:
    """
    Calls Qt's 'bool QPen::isCosmetic() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#isCosmetic
    """
    #  bool QPen::isCosmetic() const
    return self.uglySide.call('ritual_ZNK4QPen10isCosmeticEv')

  def isSolidDefaultLine(self) -> bool:
    """
    Calls Qt's 'bool QPen::isSolidDefaultLine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#isSolidDefaultLine
    """
    #  bool QPen::isSolidDefaultLine() const
    return self.uglySide.call('ritual_ZNK4QPen18isSolidDefaultLineEv')

  @overload(QColor)
  def doCompareEqualColor(self, rhs: QColor) -> bool:
    """
    Calls Qt's 'bool QPen::doCompareEqualColor(QColor rhs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#doCompareEqualColor

    Parameters
    ----------

    rhs : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  bool QPen::doCompareEqualColor(QColor rhs) const
    return self.uglySide.call(
        'ritual_ZNK4QPen19doCompareEqualColorE6QColor', self._valueOf(rhs),
    )

  @overload(Qt.PenStyle)
  def doCompareEqualStyle(self, rhs: Qt.PenStyle) -> bool:
    """
    Calls Qt's 'bool QPen::doCompareEqualStyle(Qt::PenStyle rhs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#doCompareEqualStyle

    Parameters
    ----------

    rhs : Qt.PenStyle
      Passed on as its number.
    """
    #  bool QPen::doCompareEqualStyle(Qt::PenStyle rhs) const
    return self.uglySide.call(
        'ritual_ZNK4QPen19doCompareEqualStyleEN2Qt8PenStyleE', rhs.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.PenStyle)
  def setStyle(self, a0: Qt.PenStyle) -> None:
    """
    Calls Qt's 'void QPen::setStyle(Qt::PenStyle a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#setStyle

    Parameters
    ----------

    a0 : Qt.PenStyle
      Passed on as its number.
    """
    #  void QPen::setStyle(Qt::PenStyle a0)
    self.uglySide.call('ritual_ZN4QPen8setStyleEN2Qt8PenStyleE', a0.value)

  @overload(float)
  def setDashOffset(self, doffset: float) -> None:
    """
    Calls Qt's 'void QPen::setDashOffset(qreal doffset)'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#setDashOffset

    Parameters
    ----------

    doffset : float
      Passed on as it is.
    """
    #  void QPen::setDashOffset(qreal doffset)
    self.uglySide.call('ritual_ZN4QPen13setDashOffsetEd', doffset)

  @overload(float)
  def setMiterLimit(self, limit: float) -> None:
    """
    Calls Qt's 'void QPen::setMiterLimit(qreal limit)'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#setMiterLimit

    Parameters
    ----------

    limit : float
      Passed on as it is.
    """
    #  void QPen::setMiterLimit(qreal limit)
    self.uglySide.call('ritual_ZN4QPen13setMiterLimitEd', limit)

  @overload(float)
  def setWidthF(self, width: float) -> None:
    """
    Calls Qt's 'void QPen::setWidthF(qreal width)'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#setWidthF

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QPen::setWidthF(qreal width)
    self.uglySide.call('ritual_ZN4QPen9setWidthFEd', width)

  @overload(int)
  def setWidth(self, width: int) -> None:
    """
    Calls Qt's 'void QPen::setWidth(int width)'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#setWidth

    Parameters
    ----------

    width : int
      Passed on as it is.
    """
    #  void QPen::setWidth(int width)
    self.uglySide.call('ritual_ZN4QPen8setWidthEi', width)

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QPen::setColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QPen::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN4QPen8setColorERK6QColor', self._valueOf(color),
    )

  @overload(QBrush)
  def setBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void QPen::setBrush(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#setBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void QPen::setBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN4QPen8setBrushERK6QBrush', self._valueOf(brush),
    )

  @overload(Qt.PenCapStyle)
  def setCapStyle(self, pcs: Qt.PenCapStyle) -> None:
    """
    Calls Qt's 'void QPen::setCapStyle(Qt::PenCapStyle pcs)'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#setCapStyle

    Parameters
    ----------

    pcs : Qt.PenCapStyle
      Passed on as its number.
    """
    #  void QPen::setCapStyle(Qt::PenCapStyle pcs)
    self.uglySide.call(
        'ritual_ZN4QPen11setCapStyleEN2Qt11PenCapStyleE', pcs.value,
    )

  @overload(Qt.PenJoinStyle)
  def setJoinStyle(self, pcs: Qt.PenJoinStyle) -> None:
    """
    Calls Qt's 'void QPen::setJoinStyle(Qt::PenJoinStyle pcs)'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#setJoinStyle

    Parameters
    ----------

    pcs : Qt.PenJoinStyle
      Passed on as its number.
    """
    #  void QPen::setJoinStyle(Qt::PenJoinStyle pcs)
    self.uglySide.call(
        'ritual_ZN4QPen12setJoinStyleEN2Qt12PenJoinStyleE', pcs.value,
    )

  @overload(bool)
  def setCosmetic(self, cosmetic: bool) -> None:
    """
    Calls Qt's 'void QPen::setCosmetic(bool cosmetic)'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#setCosmetic

    Parameters
    ----------

    cosmetic : bool
      Passed on as it is.
    """
    #  void QPen::setCosmetic(bool cosmetic)
    self.uglySide.call('ritual_ZN4QPen11setCosmeticEb', cosmetic)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, p: QPen) -> bool:
    """
    Calls Qt's 'bool QPen::operator==(const QPen &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#operator==

    Parameters
    ----------

    p : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  bool QPen::operator==(const QPen &p) const
    return self.uglySide.call('ritual_ZNK4QPeneqERKS_', self._valueOf(p))

  @overload(QColor)
  def __eq__(self, rhs: QColor) -> bool:
    """
    Calls Qt's 'bool operator==(const QPen &lhs, const QColor &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#operator==

    Parameters
    ----------

    rhs : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  bool operator==(const QPen &lhs, const QColor &rhs)
    return Rituals.call(
        'ritual_ZeqRK4QPenRK6QColor',
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
  def __ne__(self, p: QPen) -> bool:
    """
    Calls Qt's 'bool QPen::operator!=(const QPen &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#operator!=

    Parameters
    ----------

    p : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  bool QPen::operator!=(const QPen &p) const
    return self.uglySide.call('ritual_ZNK4QPenneERKS_', self._valueOf(p))

  @overload(QColor)
  def __ne__(self, rhs: QColor) -> bool:
    """
    Calls Qt's 'bool operator!=(const QPen &lhs, const QColor &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#operator!=

    Parameters
    ----------

    rhs : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  bool operator!=(const QPen &lhs, const QColor &rhs)
    return Rituals.call(
        'ritual_ZneRK4QPenRK6QColor',
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
    Notes what was given, for Qt's 'QPen::QPen()', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#QPen
    """
    #  QPen::QPen()
    self._noteCreation(QPen, lambda: Rituals.call('ritual_ZN4QPenC1Ev'))

  @overload(Qt.PenStyle)
  def __init__(self, a0: Qt.PenStyle) -> None:
    """
    Notes what was given, for Qt's 'QPen::QPen(Qt::PenStyle a0)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#QPen

    Parameters
    ----------

    a0 : Qt.PenStyle
      Passed on as its number.
    """
    #  QPen::QPen(Qt::PenStyle a0)
    self._noteCreation(QPen, lambda: Rituals.call(
        'ritual_ZN4QPenC1EN2Qt8PenStyleE', a0.value,
    ))

  @overload(QColor)
  def __init__(self, color: QColor) -> None:
    """
    Notes what was given, for Qt's 'QPen::QPen(const QColor &color)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#QPen

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  QPen::QPen(const QColor &color)
    self._noteCreation(QPen, lambda: Rituals.call(
        'ritual_ZN4QPenC1ERK6QColor', self._valueOf(color),
    ))

  @overload(QBrush, float)
  @overload(QBrush, float, Qt.PenStyle)
  @overload(QBrush, float, Qt.PenStyle, Qt.PenCapStyle)
  @overload(QBrush, float, Qt.PenStyle, Qt.PenCapStyle, Qt.PenJoinStyle)
  def __init__(
      self,
      brush: QBrush,
      width: float,
      s: Qt.PenStyle = Qt.PenStyle.SolidLine,
      c: Qt.PenCapStyle = Qt.PenCapStyle.SquareCap,
      j: Qt.PenJoinStyle = Qt.PenJoinStyle.BevelJoin,
  ) -> None:
    """
    Notes what was given, for Qt's 'QPen::QPen(const QBrush &brush, qreal
    width, Qt::PenStyle s, Qt::PenCapStyle c, Qt::PenJoinStyle j)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#QPen

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.

    width : float
      Passed on as it is.

    s : Qt.PenStyle
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.PenStyle.SolidLine.

    c : Qt.PenCapStyle
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.PenCapStyle.SquareCap.

    j : Qt.PenJoinStyle
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.PenJoinStyle.BevelJoin.
    """
    #  QPen::QPen(const QBrush &brush, qreal width, Qt::PenStyle s,
    #      Qt::PenCapStyle c, Qt::PenJoinStyle j)
    self._noteCreation(QPen, lambda: Rituals.call(
        'ritual_ZN4QPenC1ERK6QBrushdN2Qt8PenStyleENS3_11PenCapStyleENS3_12P'
        'enJoinStyleE',
        self._valueOf(brush), width, s.value, c.value, j.value,
    ))

  @overload(THIS)
  def __init__(self, pen: QPen) -> None:
    """
    Notes what was given, for Qt's 'QPen::QPen(const QPen &pen)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#QPen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  QPen::QPen(const QPen &pen)
    self._noteCreation(QPen, lambda: Rituals.call(
        'ritual_ZN4QPenC1ERKS_', self._valueOf(pen),
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

  def isDetached(self) -> bool:
    """
    Calls Qt's 'bool QPen::isDetached()'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#isDetached
    """
    #  bool QPen::isDetached()
    return self.uglySide.call('ritual_ZN4QPen10isDetachedEv')

  def detach(self) -> None:
    """
    Calls Qt's 'void QPen::detach()'.

    Qt's own words: https://doc.qt.io/qt-6/qpen.html#detach
    """
    #  void QPen::detach()
    self.uglySide.call('ritual_ZN4QPen6detachEv')

  @staticmethod
  def dashPattern(*__, **_) -> Never:
    """
    Qt's 'QList<qreal> QPen::dashPattern() const': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QPen.dashPattern' has no cute function yet. Qt's 'QList<qreal> "
        "QPen::dashPattern() const': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def data_ptr(*__, **_) -> Never:
    """
    Qt's 'DataPtr &QPen::data_ptr()': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QPen.data_ptr' has no cute function yet. Qt's 'DataPtr "
        "&QPen::data_ptr()': gives a type Python has no way to take yet.")

  @staticmethod
  def setDashPattern(*__, **_) -> Never:
    """
    Qt's 'void QPen::setDashPattern(const QList<qreal> &pattern)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPen.setDashPattern' has no cute function yet. Qt's 'void "
        "QPen::setDashPattern(const QList<qreal> &pattern)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QPen::swap(QPen &other)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QPen.swap' has no cute function yet. Qt's 'void QPen::swap(QPen "
        "&other)': takes a type Python has no way to hand over yet.")
