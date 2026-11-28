"""
QQuickStarShape binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickShapesDesignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickstarshape_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickStarShape to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtQuickShapes import QQuickShapePath
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQuickStarShapePrivate
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


class QQuickStarShape(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickStarShape: a plain Python object standing in
  front of one C++ QQuickStarShape.

  What exists
  -----------

  Every function of Qt's QQuickStarShape that has a ritual and that Python
  can call so far, 42 names in all: 'metaObject', 'tr', 'dashOffset',
  'setDashOffset', 'cornerRadius', 'setCornerRadius', 'ratio', 'setRatio',
  'pointCount', 'setPointCount', 'strokeWidth', 'setStrokeWidth',
  'fillColor', 'setFillColor', 'strokeColor', 'setStrokeColor', 'capStyle',
  'setCapStyle', 'joinStyle', 'setJoinStyle', 'strokeStyle',
  'setStrokeStyle', 'fillGradient', 'setFillGradient', 'resetFillGradient',
  'fillItem', 'setFillItem', 'cornerRadiusChanged', 'ratioChanged',
  'pointCountChanged', 'strokeColorChanged', 'strokeWidthChanged',
  'fillColorChanged', 'joinStyleChanged', 'capStyleChanged',
  'strokeStyleChanged', 'dashOffsetChanged', 'dashPatternChanged',
  'fillGradientChanged', 'fillItemChanged', 'itemChange', 'd_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickStarShape::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickStarShape::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickStarShape::~QQuickStarShape()': the destructor: Python never
    removes a C++ QQuickStarShape.
  - Qt's 'QList<qreal> QQuickStarShape::dashPattern() const': gives a type
    Python has no way to take yet.
  - Qt's 'void QQuickStarShape::setDashPattern(const QList<qreal> &array)':
    takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickStarShapePrivate *QQuickStarShape::d_func() const':
    takes in Python what 'QQuickStarShapePrivate *QQuickStarShape::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 53 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickStarShape is created at the first use, not by
    'QQuickStarShape(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickStarShape.
  - Qt tells when it has removed the C++ QQuickStarShape. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickStarShape that has no cute function yet,
    'dashPattern', 'setDashPattern', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

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
    Calls Qt's 'QString QQuickStarShape::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstarshape.html#tr

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
    #  QString QQuickStarShape::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQuickStarShape2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickStarShape'

  #  A C++ QQuickStarShape Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickStarShape'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickStarShape::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstarshape.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickStarShape::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuickStarShape10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def dashOffset(self) -> float:
    """
    Calls Qt's 'qreal QQuickStarShape::dashOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstarshape.html#dashOffset
    """
    #  qreal QQuickStarShape::dashOffset() const
    return self.uglySide.call('ritual_ZNK15QQuickStarShape10dashOffsetEv')

  def cornerRadius(self) -> float:
    """
    Calls Qt's 'qreal QQuickStarShape::cornerRadius() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstarshape.html#cornerRadius
    """
    #  qreal QQuickStarShape::cornerRadius() const
    return self.uglySide.call('ritual_ZNK15QQuickStarShape12cornerRadiusEv')

  def ratio(self) -> float:
    """
    Calls Qt's 'qreal QQuickStarShape::ratio() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstarshape.html#ratio
    """
    #  qreal QQuickStarShape::ratio() const
    return self.uglySide.call('ritual_ZNK15QQuickStarShape5ratioEv')

  def pointCount(self) -> int:
    """
    Calls Qt's 'int QQuickStarShape::pointCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstarshape.html#pointCount
    """
    #  int QQuickStarShape::pointCount() const
    return self.uglySide.call('ritual_ZNK15QQuickStarShape10pointCountEv')

  def strokeWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickStarShape::strokeWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstarshape.html#strokeWidth
    """
    #  qreal QQuickStarShape::strokeWidth() const
    return self.uglySide.call('ritual_ZNK15QQuickStarShape11strokeWidthEv')

  def fillColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickStarShape::fillColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstarshape.html#fillColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickStarShape::fillColor() const
    address = self.uglySide.call('ritual_ZNK15QQuickStarShape9fillColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def strokeColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickStarShape::strokeColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstarshape.html#strokeColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickStarShape::strokeColor() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickStarShape11strokeColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def capStyle(self) -> QQuickShapePath.CapStyle:
    """
    Calls Qt's 'QQuickShapePath::CapStyle QQuickStarShape::capStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstarshape.html#capStyle

    Returns
    -------

    QQuickShapePath.CapStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickShapePath.CapStyle(number)' gives.
    """
    #  QQuickShapePath::CapStyle QQuickStarShape::capStyle() const
    return QQuickShapePath.CapStyle(self.uglySide.call(
        'ritual_ZNK15QQuickStarShape8capStyleEv',
    ))

  def joinStyle(self) -> QQuickShapePath.JoinStyle:
    """
    Calls Qt's 'QQuickShapePath::JoinStyle QQuickStarShape::joinStyle()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstarshape.html#joinStyle

    Returns
    -------

    QQuickShapePath.JoinStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickShapePath.JoinStyle(number)' gives.
    """
    #  QQuickShapePath::JoinStyle QQuickStarShape::joinStyle() const
    return QQuickShapePath.JoinStyle(self.uglySide.call(
        'ritual_ZNK15QQuickStarShape9joinStyleEv',
    ))

  def strokeStyle(self) -> QQuickShapePath.StrokeStyle:
    """
    Calls Qt's 'QQuickShapePath::StrokeStyle QQuickStarShape::strokeStyle()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstarshape.html#strokeStyle

    Returns
    -------

    QQuickShapePath.StrokeStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickShapePath.StrokeStyle(number)' gives.
    """
    #  QQuickShapePath::StrokeStyle QQuickStarShape::strokeStyle() const
    return QQuickShapePath.StrokeStyle(self.uglySide.call(
        'ritual_ZNK15QQuickStarShape11strokeStyleEv',
    ))

  def fillGradient(self) -> Optional[QQuickShapeGradient]:
    """
    Calls Qt's 'QQuickShapeGradient *QQuickStarShape::fillGradient() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstarshape.html#fillGradient

    Returns
    -------

    Optional[QQuickShapeGradient]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickShapeGradient *QQuickStarShape::fillGradient() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickStarShape12fillGradientEv',
    )
    from ..QtQuickShapes import QQuickShapeGradient
    return QQuickShapeGradient._cuteAt(address)

  def fillItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickStarShape::fillItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstarshape.html#fillItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickStarShape::fillItem() const
    address = self.uglySide.call('ritual_ZNK15QQuickStarShape8fillItemEv')
    return QQuickItem._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setDashOffset(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickStarShape::setDashOffset(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstarshape.html#setDashOffset

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickStarShape::setDashOffset(qreal a0)
    self.uglySide.call('ritual_ZN15QQuickStarShape13setDashOffsetEd', a0)

  @overload(float)
  def setCornerRadius(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickStarShape::setCornerRadius(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstarshape.html#setCornerRadius

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickStarShape::setCornerRadius(qreal a0)
    self.uglySide.call('ritual_ZN15QQuickStarShape15setCornerRadiusEd', a0)

  @overload(float)
  def setRatio(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickStarShape::setRatio(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstarshape.html#setRatio

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickStarShape::setRatio(qreal a0)
    self.uglySide.call('ritual_ZN15QQuickStarShape8setRatioEd', a0)

  @overload(int)
  def setPointCount(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickStarShape::setPointCount(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstarshape.html#setPointCount

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickStarShape::setPointCount(int a0)
    self.uglySide.call('ritual_ZN15QQuickStarShape13setPointCountEi', a0)

  @overload(float)
  def setStrokeWidth(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickStarShape::setStrokeWidth(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstarshape.html#setStrokeWidth

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickStarShape::setStrokeWidth(qreal a0)
    self.uglySide.call('ritual_ZN15QQuickStarShape14setStrokeWidthEd', a0)

  @overload(QColor)
  def setFillColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickStarShape::setFillColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstarshape.html#setFillColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickStarShape::setFillColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN15QQuickStarShape12setFillColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setStrokeColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickStarShape::setStrokeColor(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstarshape.html#setStrokeColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickStarShape::setStrokeColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN15QQuickStarShape14setStrokeColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QQuickShapePath.CapStyle)
  def setCapStyle(self, style: QQuickShapePath.CapStyle) -> None:
    """
    Calls Qt's 'void QQuickStarShape::setCapStyle(QQuickShapePath::CapStyle
    style)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstarshape.html#setCapStyle

    Parameters
    ----------

    style : QQuickShapePath.CapStyle
      Passed on as its number.
    """
    #  void QQuickStarShape::setCapStyle(QQuickShapePath::CapStyle style)
    self.uglySide.call(
        'ritual_ZN15QQuickStarShape11setCapStyleEN15QQuickShapePath8CapStyl'
        'eE',
        style.value,
    )

  @overload(QQuickShapePath.JoinStyle)
  def setJoinStyle(self, style: QQuickShapePath.JoinStyle) -> None:
    """
    Calls Qt's 'void QQuickStarShape::setJoinStyle(QQuickShapePath::JoinStyle
    style)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstarshape.html#setJoinStyle

    Parameters
    ----------

    style : QQuickShapePath.JoinStyle
      Passed on as its number.
    """
    #  void QQuickStarShape::setJoinStyle(QQuickShapePath::JoinStyle style)
    self.uglySide.call(
        'ritual_ZN15QQuickStarShape12setJoinStyleEN15QQuickShapePath9JoinSt'
        'yleE',
        style.value,
    )

  @overload(QQuickShapePath.StrokeStyle)
  def setStrokeStyle(self, style: QQuickShapePath.StrokeStyle) -> None:
    """
    Calls Qt's 'void
    QQuickStarShape::setStrokeStyle(QQuickShapePath::StrokeStyle style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstarshape.html#setStrokeStyle

    Parameters
    ----------

    style : QQuickShapePath.StrokeStyle
      Passed on as its number.
    """
    #  void QQuickStarShape::setStrokeStyle(QQuickShapePath::StrokeStyle
    #      style)
    self.uglySide.call(
        'ritual_ZN15QQuickStarShape14setStrokeStyleEN15QQuickShapePath11Str'
        'okeStyleE',
        style.value,
    )

  @overload(QQuickShapeGradient)
  @overload(NoneType)
  def setFillGradient(
      self,
      fillGradient: Optional[QQuickShapeGradient],
  ) -> None:
    """
    Calls Qt's 'void QQuickStarShape::setFillGradient(QQuickShapeGradient
    *fillGradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstarshape.html#setFillGradient

    Parameters
    ----------

    fillGradient : Optional[QQuickShapeGradient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickStarShape::setFillGradient(QQuickShapeGradient
    #      *fillGradient)
    self.uglySide.call(
        'ritual_ZN15QQuickStarShape15setFillGradientEP19QQuickShapeGradient',
        self._addressOf(fillGradient),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setFillItem(self, newFillItem: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickStarShape::setFillItem(QQuickItem *newFillItem)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstarshape.html#setFillItem

    Parameters
    ----------

    newFillItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickStarShape::setFillItem(QQuickItem *newFillItem)
    self.uglySide.call(
        'ritual_ZN15QQuickStarShape11setFillItemEP10QQuickItem',
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
    'QQuickStarShape::QQuickStarShape(QQuickItem *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstarshape.html#QQuickStarShape

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickStarShape::QQuickStarShape(QQuickItem *parent)
    self._noteCreation(QQuickStarShape, lambda: Rituals.call(
        'ritual_ZN15QQuickStarShapeC1EP10QQuickItem',
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
    Calls Qt's 'void QQuickStarShape::resetFillGradient()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstarshape.html#resetFillGradient
    """
    #  void QQuickStarShape::resetFillGradient()
    self.uglySide.call('ritual_ZN15QQuickStarShape17resetFillGradientEv')

  def cornerRadiusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStarShape::cornerRadiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstarshape.html#cornerRadiusChanged
    """
    #  void QQuickStarShape::cornerRadiusChanged()
    self.uglySide.call('ritual_ZN15QQuickStarShape19cornerRadiusChangedEv')

  def ratioChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStarShape::ratioChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstarshape.html#ratioChanged
    """
    #  void QQuickStarShape::ratioChanged()
    self.uglySide.call('ritual_ZN15QQuickStarShape12ratioChangedEv')

  def pointCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStarShape::pointCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstarshape.html#pointCountChanged
    """
    #  void QQuickStarShape::pointCountChanged()
    self.uglySide.call('ritual_ZN15QQuickStarShape17pointCountChangedEv')

  def strokeColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStarShape::strokeColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstarshape.html#strokeColorChanged
    """
    #  void QQuickStarShape::strokeColorChanged()
    self.uglySide.call('ritual_ZN15QQuickStarShape18strokeColorChangedEv')

  def strokeWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStarShape::strokeWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstarshape.html#strokeWidthChanged
    """
    #  void QQuickStarShape::strokeWidthChanged()
    self.uglySide.call('ritual_ZN15QQuickStarShape18strokeWidthChangedEv')

  def fillColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStarShape::fillColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstarshape.html#fillColorChanged
    """
    #  void QQuickStarShape::fillColorChanged()
    self.uglySide.call('ritual_ZN15QQuickStarShape16fillColorChangedEv')

  def joinStyleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStarShape::joinStyleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstarshape.html#joinStyleChanged
    """
    #  void QQuickStarShape::joinStyleChanged()
    self.uglySide.call('ritual_ZN15QQuickStarShape16joinStyleChangedEv')

  def capStyleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStarShape::capStyleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstarshape.html#capStyleChanged
    """
    #  void QQuickStarShape::capStyleChanged()
    self.uglySide.call('ritual_ZN15QQuickStarShape15capStyleChangedEv')

  def strokeStyleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStarShape::strokeStyleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstarshape.html#strokeStyleChanged
    """
    #  void QQuickStarShape::strokeStyleChanged()
    self.uglySide.call('ritual_ZN15QQuickStarShape18strokeStyleChangedEv')

  def dashOffsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStarShape::dashOffsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstarshape.html#dashOffsetChanged
    """
    #  void QQuickStarShape::dashOffsetChanged()
    self.uglySide.call('ritual_ZN15QQuickStarShape17dashOffsetChangedEv')

  def dashPatternChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStarShape::dashPatternChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstarshape.html#dashPatternChanged
    """
    #  void QQuickStarShape::dashPatternChanged()
    self.uglySide.call('ritual_ZN15QQuickStarShape18dashPatternChangedEv')

  def fillGradientChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStarShape::fillGradientChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstarshape.html#fillGradientChanged
    """
    #  void QQuickStarShape::fillGradientChanged()
    self.uglySide.call('ritual_ZN15QQuickStarShape19fillGradientChangedEv')

  def fillItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickStarShape::fillItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickstarshape.html#fillItemChanged
    """
    #  void QQuickStarShape::fillItemChanged()
    self.uglySide.call('ritual_ZN15QQuickStarShape15fillItemChangedEv')

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickStarShape::itemChange(ItemChange change, const
    ItemChangeData &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstarshape.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickStarShape::itemChange(ItemChange change, const
    #      ItemChangeData &value)
    ritual = (
        'ritual_ZN15QQuickStarShape10itemChangeEN10QQuickItem10ItemChangeER'
        'KNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickStarShape10itemChangeEN10QQuickItem10ItemCh'
          'angeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  def d_func(self) -> Optional[QQuickStarShapePrivate]:
    """
    Calls Qt's 'QQuickStarShapePrivate *QQuickStarShape::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickstarshape.html#d_func

    Returns
    -------

    Optional[QQuickStarShapePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickStarShapePrivate *QQuickStarShape::d_func()
    address = self.uglySide.call('ritual_ZN15QQuickStarShape6d_funcEv')
    from . import QQuickStarShapePrivate
    return QQuickStarShapePrivate._cuteAt(address)

  @staticmethod
  def dashPattern(*__, **_) -> Never:
    """
    Qt's 'QList<qreal> QQuickStarShape::dashPattern() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickStarShape.dashPattern' has no cute function yet. Qt's "
        "'QList<qreal> QQuickStarShape::dashPattern() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def setDashPattern(*__, **_) -> Never:
    """
    Qt's 'void QQuickStarShape::setDashPattern(const QList<qreal> &array)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickStarShape.setDashPattern' has no cute function yet. Qt's "
        "'void QQuickStarShape::setDashPattern(const QList<qreal> &array)': "
        "takes a type Python has no way to hand over yet.")
