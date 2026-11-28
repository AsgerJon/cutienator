"""
QQuickEllipseShape binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickShapesDesignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickellipseshape_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickEllipseShape to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtQuickShapes import QQuickShapePath
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQuickEllipseShapePrivate
  from ..QtGui import QColor
  from ..QtQuickShapes import QQuickShapeGradient
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QQuickShapeGradient = WAIT['QQuickShapeGradient']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickEllipseShape(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickEllipseShape: a plain Python object standing in
  front of one C++ QQuickEllipseShape.

  What exists
  -----------

  Every function of Qt's QQuickEllipseShape that has a ritual and that Python
  can call so far, 52 names in all: 'metaObject', 'tr', 'sweepAngle',
  'setSweepAngle', 'startAngle', 'setStartAngle', 'dashOffset',
  'setDashOffset', 'innerArcRatio', 'setInnerArcRatio', 'cornerRadius',
  'setCornerRadius', 'strokeWidth', 'setStrokeWidth', 'fillColor',
  'setFillColor', 'strokeColor', 'setStrokeColor', 'capStyle', 'setCapStyle',
  'joinStyle', 'setJoinStyle', 'strokeStyle', 'setStrokeStyle', 'fillRule',
  'setFillRule', 'fillGradient', 'setFillGradient', 'resetFillGradient',
  'borderMode', 'setBorderMode', 'resetBorderMode', 'fillItem',
  'setFillItem', 'innerArcRatioChanged', 'cornerRadiusChanged',
  'startAngleChanged', 'sweepAngleChanged', 'strokeColorChanged',
  'strokeWidthChanged', 'fillColorChanged', 'joinStyleChanged',
  'capStyleChanged', 'fillRuleChanged', 'strokeStyleChanged',
  'dashOffsetChanged', 'dashPatternChanged', 'fillGradientChanged',
  'borderModeChanged', 'fillItemChanged', 'itemChange', 'd_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickEllipseShape::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickEllipseShape::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickEllipseShape::~QQuickEllipseShape()': the destructor: Python
    never removes a C++ QQuickEllipseShape.
  - Qt's 'QList<qreal> QQuickEllipseShape::dashPattern() const': gives a type
    Python has no way to take yet.
  - Qt's 'void QQuickEllipseShape::setDashPattern(const QList<qreal>
    &array)': takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickEllipseShapePrivate *QQuickEllipseShape::d_func()
    const': takes in Python what 'QQuickEllipseShapePrivate
    *QQuickEllipseShape::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 63 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickEllipseShape is created at the first use, not by
    'QQuickEllipseShape(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickEllipseShape.
  - Qt tells when it has removed the C++ QQuickEllipseShape. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickEllipseShape that has no cute function yet,
    'dashPattern', 'setDashPattern', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickEllipseShape, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class BorderMode(CuteNum, scoped=True):
    """
    The enum 'QQuickEllipseShape::BorderMode' of Qt, with the 3 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Inside = Kee[int](0)
    Middle = Kee[int](1)
    Outside = Kee[int](2)

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
    Calls Qt's 'QString QQuickEllipseShape::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickellipseshape.html#tr

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
    #  QString QQuickEllipseShape::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQuickEllipseShape2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickEllipseShape'

  #  A C++ QQuickEllipseShape Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickEllipseShape'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickEllipseShape::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickellipseshape.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickEllipseShape::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickEllipseShape10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sweepAngle(self) -> float:
    """
    Calls Qt's 'qreal QQuickEllipseShape::sweepAngle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickellipseshape.html#sweepAngle
    """
    #  qreal QQuickEllipseShape::sweepAngle() const
    return self.uglySide.call('ritual_ZNK18QQuickEllipseShape10sweepAngleEv')

  def startAngle(self) -> float:
    """
    Calls Qt's 'qreal QQuickEllipseShape::startAngle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickellipseshape.html#startAngle
    """
    #  qreal QQuickEllipseShape::startAngle() const
    return self.uglySide.call('ritual_ZNK18QQuickEllipseShape10startAngleEv')

  def dashOffset(self) -> float:
    """
    Calls Qt's 'qreal QQuickEllipseShape::dashOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickellipseshape.html#dashOffset
    """
    #  qreal QQuickEllipseShape::dashOffset() const
    return self.uglySide.call('ritual_ZNK18QQuickEllipseShape10dashOffsetEv')

  def innerArcRatio(self) -> float:
    """
    Calls Qt's 'qreal QQuickEllipseShape::innerArcRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#innerArcRatio
    """
    #  qreal QQuickEllipseShape::innerArcRatio() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickEllipseShape13innerArcRatioEv',
    )

  def cornerRadius(self) -> float:
    """
    Calls Qt's 'qreal QQuickEllipseShape::cornerRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#cornerRadius
    """
    #  qreal QQuickEllipseShape::cornerRadius() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickEllipseShape12cornerRadiusEv',
    )

  def strokeWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickEllipseShape::strokeWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#strokeWidth
    """
    #  qreal QQuickEllipseShape::strokeWidth() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickEllipseShape11strokeWidthEv',
    )

  def fillColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickEllipseShape::fillColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickellipseshape.html#fillColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickEllipseShape::fillColor() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickEllipseShape9fillColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def strokeColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickEllipseShape::strokeColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#strokeColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickEllipseShape::strokeColor() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickEllipseShape11strokeColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def capStyle(self) -> QQuickShapePath.CapStyle:
    """
    Calls Qt's 'QQuickShapePath::CapStyle QQuickEllipseShape::capStyle()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickellipseshape.html#capStyle

    Returns
    -------

    QQuickShapePath.CapStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickShapePath.CapStyle(number)' gives.
    """
    #  QQuickShapePath::CapStyle QQuickEllipseShape::capStyle() const
    return QQuickShapePath.CapStyle(self.uglySide.call(
        'ritual_ZNK18QQuickEllipseShape8capStyleEv',
    ))

  def joinStyle(self) -> QQuickShapePath.JoinStyle:
    """
    Calls Qt's 'QQuickShapePath::JoinStyle QQuickEllipseShape::joinStyle()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickellipseshape.html#joinStyle

    Returns
    -------

    QQuickShapePath.JoinStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickShapePath.JoinStyle(number)' gives.
    """
    #  QQuickShapePath::JoinStyle QQuickEllipseShape::joinStyle() const
    return QQuickShapePath.JoinStyle(self.uglySide.call(
        'ritual_ZNK18QQuickEllipseShape9joinStyleEv',
    ))

  def strokeStyle(self) -> QQuickShapePath.StrokeStyle:
    """
    Calls Qt's 'QQuickShapePath::StrokeStyle
    QQuickEllipseShape::strokeStyle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#strokeStyle

    Returns
    -------

    QQuickShapePath.StrokeStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickShapePath.StrokeStyle(number)' gives.
    """
    #  QQuickShapePath::StrokeStyle QQuickEllipseShape::strokeStyle() const
    return QQuickShapePath.StrokeStyle(self.uglySide.call(
        'ritual_ZNK18QQuickEllipseShape11strokeStyleEv',
    ))

  def fillRule(self) -> QQuickShapePath.FillRule:
    """
    Calls Qt's 'QQuickShapePath::FillRule QQuickEllipseShape::fillRule()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickellipseshape.html#fillRule

    Returns
    -------

    QQuickShapePath.FillRule
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickShapePath.FillRule(number)' gives.
    """
    #  QQuickShapePath::FillRule QQuickEllipseShape::fillRule() const
    return QQuickShapePath.FillRule(self.uglySide.call(
        'ritual_ZNK18QQuickEllipseShape8fillRuleEv',
    ))

  def fillGradient(self) -> Optional[QQuickShapeGradient]:
    """
    Calls Qt's 'QQuickShapeGradient *QQuickEllipseShape::fillGradient()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#fillGradient

    Returns
    -------

    Optional[QQuickShapeGradient]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickShapeGradient *QQuickEllipseShape::fillGradient() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickEllipseShape12fillGradientEv',
    )
    from ..QtQuickShapes import QQuickShapeGradient
    return QQuickShapeGradient._cuteAt(address)

  def borderMode(self) -> BorderMode:
    """
    Calls Qt's 'BorderMode QQuickEllipseShape::borderMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickellipseshape.html#borderMode

    Returns
    -------

    BorderMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'BorderMode(number)'
      gives.
    """
    #  BorderMode QQuickEllipseShape::borderMode() const
    return QQuickEllipseShape.BorderMode(self.uglySide.call(
        'ritual_ZNK18QQuickEllipseShape10borderModeEv',
    ))

  def fillItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickEllipseShape::fillItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickellipseshape.html#fillItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickEllipseShape::fillItem() const
    address = self.uglySide.call('ritual_ZNK18QQuickEllipseShape8fillItemEv')
    return QQuickItem._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setSweepAngle(self, sweepAngle: float) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::setSweepAngle(qreal sweepAngle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#setSweepAngle

    Parameters
    ----------

    sweepAngle : float
      Passed on as it is.
    """
    #  void QQuickEllipseShape::setSweepAngle(qreal sweepAngle)
    self.uglySide.call(
        'ritual_ZN18QQuickEllipseShape13setSweepAngleEd', sweepAngle,
    )

  @overload(float)
  def setStartAngle(self, startAngle: float) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::setStartAngle(qreal startAngle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#setStartAngle

    Parameters
    ----------

    startAngle : float
      Passed on as it is.
    """
    #  void QQuickEllipseShape::setStartAngle(qreal startAngle)
    self.uglySide.call(
        'ritual_ZN18QQuickEllipseShape13setStartAngleEd', startAngle,
    )

  @overload(float)
  def setDashOffset(self, offset: float) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::setDashOffset(qreal offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#setDashOffset

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void QQuickEllipseShape::setDashOffset(qreal offset)
    self.uglySide.call(
        'ritual_ZN18QQuickEllipseShape13setDashOffsetEd', offset,
    )

  @overload(float)
  def setInnerArcRatio(self, innerArcRatio: float) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::setInnerArcRatio(qreal
    innerArcRatio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#setInnerArcRatio

    Parameters
    ----------

    innerArcRatio : float
      Passed on as it is.
    """
    #  void QQuickEllipseShape::setInnerArcRatio(qreal innerArcRatio)
    self.uglySide.call(
        'ritual_ZN18QQuickEllipseShape16setInnerArcRatioEd', innerArcRatio,
    )

  @overload(float)
  def setCornerRadius(self, cornerRadius: float) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::setCornerRadius(qreal
    cornerRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#setCornerRadius

    Parameters
    ----------

    cornerRadius : float
      Passed on as it is.
    """
    #  void QQuickEllipseShape::setCornerRadius(qreal cornerRadius)
    self.uglySide.call(
        'ritual_ZN18QQuickEllipseShape15setCornerRadiusEd', cornerRadius,
    )

  @overload(float)
  def setStrokeWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::setStrokeWidth(qreal width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#setStrokeWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QQuickEllipseShape::setStrokeWidth(qreal width)
    self.uglySide.call(
        'ritual_ZN18QQuickEllipseShape14setStrokeWidthEd', width,
    )

  @overload(QColor)
  def setFillColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::setFillColor(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#setFillColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickEllipseShape::setFillColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN18QQuickEllipseShape12setFillColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setStrokeColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::setStrokeColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#setStrokeColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickEllipseShape::setStrokeColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN18QQuickEllipseShape14setStrokeColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QQuickShapePath.CapStyle)
  def setCapStyle(self, style: QQuickShapePath.CapStyle) -> None:
    """
    Calls Qt's 'void
    QQuickEllipseShape::setCapStyle(QQuickShapePath::CapStyle style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#setCapStyle

    Parameters
    ----------

    style : QQuickShapePath.CapStyle
      Passed on as its number.
    """
    #  void QQuickEllipseShape::setCapStyle(QQuickShapePath::CapStyle style)
    self.uglySide.call(
        'ritual_ZN18QQuickEllipseShape11setCapStyleEN15QQuickShapePath8CapS'
        'tyleE',
        style.value,
    )

  @overload(QQuickShapePath.JoinStyle)
  def setJoinStyle(self, style: QQuickShapePath.JoinStyle) -> None:
    """
    Calls Qt's 'void
    QQuickEllipseShape::setJoinStyle(QQuickShapePath::JoinStyle style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#setJoinStyle

    Parameters
    ----------

    style : QQuickShapePath.JoinStyle
      Passed on as its number.
    """
    #  void QQuickEllipseShape::setJoinStyle(QQuickShapePath::JoinStyle
    #      style)
    self.uglySide.call(
        'ritual_ZN18QQuickEllipseShape12setJoinStyleEN15QQuickShapePath9Joi'
        'nStyleE',
        style.value,
    )

  @overload(QQuickShapePath.StrokeStyle)
  def setStrokeStyle(self, style: QQuickShapePath.StrokeStyle) -> None:
    """
    Calls Qt's 'void
    QQuickEllipseShape::setStrokeStyle(QQuickShapePath::StrokeStyle style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#setStrokeStyle

    Parameters
    ----------

    style : QQuickShapePath.StrokeStyle
      Passed on as its number.
    """
    #  void QQuickEllipseShape::setStrokeStyle(QQuickShapePath::StrokeStyle
    #      style)
    self.uglySide.call(
        'ritual_ZN18QQuickEllipseShape14setStrokeStyleEN15QQuickShapePath11'
        'StrokeStyleE',
        style.value,
    )

  @overload(QQuickShapePath.FillRule)
  def setFillRule(self, fillRule: QQuickShapePath.FillRule) -> None:
    """
    Calls Qt's 'void
    QQuickEllipseShape::setFillRule(QQuickShapePath::FillRule fillRule)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#setFillRule

    Parameters
    ----------

    fillRule : QQuickShapePath.FillRule
      Passed on as its number.
    """
    #  void QQuickEllipseShape::setFillRule(QQuickShapePath::FillRule
    #      fillRule)
    self.uglySide.call(
        'ritual_ZN18QQuickEllipseShape11setFillRuleEN15QQuickShapePath8Fill'
        'RuleE',
        fillRule.value,
    )

  @overload(QQuickShapeGradient)
  @overload(NoneType)
  def setFillGradient(
      self,
      fillGradient: Optional[QQuickShapeGradient],
  ) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::setFillGradient(QQuickShapeGradient
    *fillGradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#setFillGradient

    Parameters
    ----------

    fillGradient : Optional[QQuickShapeGradient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickEllipseShape::setFillGradient(QQuickShapeGradient
    #      *fillGradient)
    self.uglySide.call(
        'ritual_ZN18QQuickEllipseShape15setFillGradientEP19QQuickShapeGradi'
        'ent',
        self._addressOf(fillGradient),
    )

  @overload(BorderMode)
  def setBorderMode(self, borderMode: BorderMode) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::setBorderMode(BorderMode
    borderMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#setBorderMode

    Parameters
    ----------

    borderMode : BorderMode
      Passed on as its number.
    """
    #  void QQuickEllipseShape::setBorderMode(BorderMode borderMode)
    self.uglySide.call(
        'ritual_ZN18QQuickEllipseShape13setBorderModeENS_10BorderModeE',
        borderMode.value,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setFillItem(self, newFillItem: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::setFillItem(QQuickItem
    *newFillItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#setFillItem

    Parameters
    ----------

    newFillItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickEllipseShape::setFillItem(QQuickItem *newFillItem)
    self.uglySide.call(
        'ritual_ZN18QQuickEllipseShape11setFillItemEP10QQuickItem',
        self._addressOf(newFillItem),
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickEllipseShape::QQuickEllipseShape(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#QQuickEllipseShape

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickEllipseShape::QQuickEllipseShape(QQuickItem *parent)
    self._noteCreation(QQuickEllipseShape, lambda: Rituals.call(
        'ritual_ZN18QQuickEllipseShapeC1EP10QQuickItem',
        self._addressOf(parent),
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

  def resetFillGradient(self) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::resetFillGradient()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#resetFillGradient
    """
    #  void QQuickEllipseShape::resetFillGradient()
    self.uglySide.call('ritual_ZN18QQuickEllipseShape17resetFillGradientEv')

  def resetBorderMode(self) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::resetBorderMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#resetBorderMode
    """
    #  void QQuickEllipseShape::resetBorderMode()
    self.uglySide.call('ritual_ZN18QQuickEllipseShape15resetBorderModeEv')

  def innerArcRatioChanged(self) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::innerArcRatioChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#innerArcRatioChanged
    """
    #  void QQuickEllipseShape::innerArcRatioChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickEllipseShape20innerArcRatioChangedEv',
    )

  def cornerRadiusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::cornerRadiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#cornerRadiusChanged
    """
    #  void QQuickEllipseShape::cornerRadiusChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickEllipseShape19cornerRadiusChangedEv',
    )

  def startAngleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::startAngleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#startAngleChanged
    """
    #  void QQuickEllipseShape::startAngleChanged()
    self.uglySide.call('ritual_ZN18QQuickEllipseShape17startAngleChangedEv')

  def sweepAngleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::sweepAngleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#sweepAngleChanged
    """
    #  void QQuickEllipseShape::sweepAngleChanged()
    self.uglySide.call('ritual_ZN18QQuickEllipseShape17sweepAngleChangedEv')

  def strokeColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::strokeColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#strokeColorChanged
    """
    #  void QQuickEllipseShape::strokeColorChanged()
    self.uglySide.call('ritual_ZN18QQuickEllipseShape18strokeColorChangedEv')

  def strokeWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::strokeWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#strokeWidthChanged
    """
    #  void QQuickEllipseShape::strokeWidthChanged()
    self.uglySide.call('ritual_ZN18QQuickEllipseShape18strokeWidthChangedEv')

  def fillColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::fillColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#fillColorChanged
    """
    #  void QQuickEllipseShape::fillColorChanged()
    self.uglySide.call('ritual_ZN18QQuickEllipseShape16fillColorChangedEv')

  def joinStyleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::joinStyleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#joinStyleChanged
    """
    #  void QQuickEllipseShape::joinStyleChanged()
    self.uglySide.call('ritual_ZN18QQuickEllipseShape16joinStyleChangedEv')

  def capStyleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::capStyleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#capStyleChanged
    """
    #  void QQuickEllipseShape::capStyleChanged()
    self.uglySide.call('ritual_ZN18QQuickEllipseShape15capStyleChangedEv')

  def fillRuleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::fillRuleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#fillRuleChanged
    """
    #  void QQuickEllipseShape::fillRuleChanged()
    self.uglySide.call('ritual_ZN18QQuickEllipseShape15fillRuleChangedEv')

  def strokeStyleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::strokeStyleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#strokeStyleChanged
    """
    #  void QQuickEllipseShape::strokeStyleChanged()
    self.uglySide.call('ritual_ZN18QQuickEllipseShape18strokeStyleChangedEv')

  def dashOffsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::dashOffsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#dashOffsetChanged
    """
    #  void QQuickEllipseShape::dashOffsetChanged()
    self.uglySide.call('ritual_ZN18QQuickEllipseShape17dashOffsetChangedEv')

  def dashPatternChanged(self) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::dashPatternChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#dashPatternChanged
    """
    #  void QQuickEllipseShape::dashPatternChanged()
    self.uglySide.call('ritual_ZN18QQuickEllipseShape18dashPatternChangedEv')

  def fillGradientChanged(self) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::fillGradientChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#fillGradientChanged
    """
    #  void QQuickEllipseShape::fillGradientChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickEllipseShape19fillGradientChangedEv',
    )

  def borderModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::borderModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#borderModeChanged
    """
    #  void QQuickEllipseShape::borderModeChanged()
    self.uglySide.call('ritual_ZN18QQuickEllipseShape17borderModeChangedEv')

  def fillItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::fillItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickellipseshape.html#fillItemChanged
    """
    #  void QQuickEllipseShape::fillItemChanged()
    self.uglySide.call('ritual_ZN18QQuickEllipseShape15fillItemChangedEv')

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickEllipseShape::itemChange(ItemChange change, const
    ItemChangeData &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickellipseshape.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickEllipseShape::itemChange(ItemChange change, const
    #      ItemChangeData &value)
    ritual = (
        'ritual_ZN18QQuickEllipseShape10itemChangeEN10QQuickItem10ItemChang'
        'eERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickEllipseShape10itemChangeEN10QQuickItem10Ite'
          'mChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  def d_func(self) -> Optional[QQuickEllipseShapePrivate]:
    """
    Calls Qt's 'QQuickEllipseShapePrivate *QQuickEllipseShape::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickellipseshape.html#d_func

    Returns
    -------

    Optional[QQuickEllipseShapePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickEllipseShapePrivate *QQuickEllipseShape::d_func()
    address = self.uglySide.call('ritual_ZN18QQuickEllipseShape6d_funcEv')
    from . import QQuickEllipseShapePrivate
    return QQuickEllipseShapePrivate._cuteAt(address)

  @staticmethod
  def dashPattern(*__, **_) -> Never:
    """
    Qt's 'QList<qreal> QQuickEllipseShape::dashPattern() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickEllipseShape.dashPattern' has no cute function yet. Qt's "
        "'QList<qreal> QQuickEllipseShape::dashPattern() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def setDashPattern(*__, **_) -> Never:
    """
    Qt's 'void QQuickEllipseShape::setDashPattern(const QList<qreal>
    &array)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickEllipseShape.setDashPattern' has no cute function yet. Qt's "
        "'void QQuickEllipseShape::setDashPattern(const QList<qreal> "
        "&array)': takes a type Python has no way to hand over yet.")
