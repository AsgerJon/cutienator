"""
QQuickShapePath binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshape_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickShapePath to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QObject
  from . import QQuickShapeGradient, QQuickShapePathPrivate, QQuickShapeTrim
  from ..QtGui import QColor, QMatrix4x4
  from ..QtQuick import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QMatrix4x4 = WAIT['QMatrix4x4']
  QObject = WAIT['QObject']
  QQuickItem = WAIT['QQuickItem']
  QQuickShapeGradient = WAIT['QQuickShapeGradient']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickShapePath(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickShapePath: a plain Python object standing in
  front of one C++ QQuickShapePath.

  What exists
  -----------

  Every function of Qt's QQuickShapePath that has a ritual and that Python
  can call so far, 54 names in all: 'metaObject', 'tr', 'strokeColor',
  'setStrokeColor', 'strokeWidth', 'setStrokeWidth', 'setStrokeGradient',
  'strokeGradient', 'resetStrokeGradient', 'fillColor', 'setFillColor',
  'fillRule', 'setFillRule', 'joinStyle', 'setJoinStyle', 'miterLimit',
  'setMiterLimit', 'capStyle', 'setCapStyle', 'strokeStyle',
  'setStrokeStyle', 'dashOffset', 'setDashOffset', 'fillGradient',
  'setFillGradient', 'resetFillGradient', 'pathHints', 'setPathHints',
  'fillTransform', 'setFillTransform', 'fillItem', 'setFillItem', 'trim',
  'hasTrim', 'cosmeticStroke', 'setCosmeticStroke', 'shapePathChanged',
  'strokeColorChanged', 'strokeWidthChanged', 'fillColorChanged',
  'fillRuleChanged', 'joinStyleChanged', 'miterLimitChanged',
  'capStyleChanged', 'strokeStyleChanged', 'dashOffsetChanged',
  'dashPatternChanged', 'fillGradientChanged', 'pathHintsChanged',
  'fillTransformChanged', 'fillItemChanged', 'cosmeticStrokeChanged',
  'strokeGradientChanged', 'd_func'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickShapePath::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickShapePath::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickShapePath::~QQuickShapePath()': the destructor: Python never
    removes a C++ QQuickShapePath.
  - Qt's 'QList<qreal> QQuickShapePath::dashPattern() const': gives a type
    Python has no way to take yet.
  - Qt's 'void QQuickShapePath::setDashPattern(const QList<qreal> &array)':
    takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickShapePathPrivate *QQuickShapePath::d_func() const':
    takes in Python what 'QQuickShapePathPrivate *QQuickShapePath::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 65 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickShapePath is created at the first use, not by
    'QQuickShapePath(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickShapePath.
  - Qt tells when it has removed the C++ QQuickShapePath. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickShapePath that has no cute function yet,
    'dashPattern', 'setDashPattern', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickShapePath, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class CapStyle(CuteNum):
    """
    The enum 'QQuickShapePath::CapStyle' of Qt, with the 3 names Qt gives in
    it.
    """

    FlatCap = Kee[int](0)
    SquareCap = Kee[int](16)
    RoundCap = Kee[int](32)

  class FillRule(CuteNum):
    """
    The enum 'QQuickShapePath::FillRule' of Qt, with the 2 names Qt gives in
    it.
    """

    OddEvenFill = Kee[int](0)
    WindingFill = Kee[int](1)

  class JoinStyle(CuteNum):
    """
    The enum 'QQuickShapePath::JoinStyle' of Qt, with the 3 names Qt gives in
    it.
    """

    MiterJoin = Kee[int](0)
    BevelJoin = Kee[int](64)
    RoundJoin = Kee[int](128)

  class PathHint(CuteFlags):
    """
    The flags enum 'QQuickShapePath::PathHint' of Qt, with the 7 names Qt
    gives in it. Qt names the type of its combinations
    'QQuickShapePath::PathHints'.
    """

    PathLinear = 0x1
    PathQuadratic = 0x2
    PathConvex = 0x4
    PathFillOnRight = 0x8
    PathSolid = 0x10
    PathNonIntersecting = 0x20
    PathNonOverlappingControlPointTriangles = 0x40

  PathHints = PathHint

  class StrokeStyle(CuteNum):
    """
    The enum 'QQuickShapePath::StrokeStyle' of Qt, with the 2 names Qt gives
    in it.
    """

    SolidLine = Kee[int](1)
    DashLine = Kee[int](2)

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
    Calls Qt's 'QString QQuickShapePath::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapepath.html#tr

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
    #  QString QQuickShapePath::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQuickShapePath2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickShapePath'

  #  A C++ QQuickShapePath Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickShapePath'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickShapePath::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapepath.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickShapePath::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuickShapePath10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def strokeColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickShapePath::strokeColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapepath.html#strokeColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickShapePath::strokeColor() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickShapePath11strokeColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def strokeWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickShapePath::strokeWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapepath.html#strokeWidth
    """
    #  qreal QQuickShapePath::strokeWidth() const
    return self.uglySide.call('ritual_ZNK15QQuickShapePath11strokeWidthEv')

  def strokeGradient(self) -> Optional[QQuickShapeGradient]:
    """
    Calls Qt's 'QQuickShapeGradient *QQuickShapePath::strokeGradient()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#strokeGradient

    Returns
    -------

    Optional[QQuickShapeGradient]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickShapeGradient *QQuickShapePath::strokeGradient() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickShapePath14strokeGradientEv',
    )
    from . import QQuickShapeGradient
    return QQuickShapeGradient._cuteAt(address)

  def fillColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickShapePath::fillColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapepath.html#fillColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickShapePath::fillColor() const
    address = self.uglySide.call('ritual_ZNK15QQuickShapePath9fillColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def fillRule(self) -> FillRule:
    """
    Calls Qt's 'FillRule QQuickShapePath::fillRule() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapepath.html#fillRule

    Returns
    -------

    FillRule
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FillRule(number)' gives.
    """
    #  FillRule QQuickShapePath::fillRule() const
    return QQuickShapePath.FillRule(self.uglySide.call(
        'ritual_ZNK15QQuickShapePath8fillRuleEv',
    ))

  def joinStyle(self) -> JoinStyle:
    """
    Calls Qt's 'JoinStyle QQuickShapePath::joinStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapepath.html#joinStyle

    Returns
    -------

    JoinStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'JoinStyle(number)' gives.
    """
    #  JoinStyle QQuickShapePath::joinStyle() const
    return QQuickShapePath.JoinStyle(self.uglySide.call(
        'ritual_ZNK15QQuickShapePath9joinStyleEv',
    ))

  def miterLimit(self) -> int:
    """
    Calls Qt's 'int QQuickShapePath::miterLimit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapepath.html#miterLimit
    """
    #  int QQuickShapePath::miterLimit() const
    return self.uglySide.call('ritual_ZNK15QQuickShapePath10miterLimitEv')

  def capStyle(self) -> CapStyle:
    """
    Calls Qt's 'CapStyle QQuickShapePath::capStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapepath.html#capStyle

    Returns
    -------

    CapStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'CapStyle(number)' gives.
    """
    #  CapStyle QQuickShapePath::capStyle() const
    return QQuickShapePath.CapStyle(self.uglySide.call(
        'ritual_ZNK15QQuickShapePath8capStyleEv',
    ))

  def strokeStyle(self) -> StrokeStyle:
    """
    Calls Qt's 'StrokeStyle QQuickShapePath::strokeStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapepath.html#strokeStyle

    Returns
    -------

    StrokeStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'StrokeStyle(number)'
      gives.
    """
    #  StrokeStyle QQuickShapePath::strokeStyle() const
    return QQuickShapePath.StrokeStyle(self.uglySide.call(
        'ritual_ZNK15QQuickShapePath11strokeStyleEv',
    ))

  def dashOffset(self) -> float:
    """
    Calls Qt's 'qreal QQuickShapePath::dashOffset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapepath.html#dashOffset
    """
    #  qreal QQuickShapePath::dashOffset() const
    return self.uglySide.call('ritual_ZNK15QQuickShapePath10dashOffsetEv')

  def fillGradient(self) -> Optional[QQuickShapeGradient]:
    """
    Calls Qt's 'QQuickShapeGradient *QQuickShapePath::fillGradient() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapepath.html#fillGradient

    Returns
    -------

    Optional[QQuickShapeGradient]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickShapeGradient *QQuickShapePath::fillGradient() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickShapePath12fillGradientEv',
    )
    from . import QQuickShapeGradient
    return QQuickShapeGradient._cuteAt(address)

  def pathHints(self) -> PathHints:
    """
    Calls Qt's 'PathHints QQuickShapePath::pathHints() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapepath.html#pathHints

    Returns
    -------

    PathHints
      The value standing for the combination Qt gave back.
    """
    #  PathHints QQuickShapePath::pathHints() const
    return QQuickShapePath.PathHints(self.uglySide.call(
        'ritual_ZNK15QQuickShapePath9pathHintsEv',
    ))

  def fillTransform(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 QQuickShapePath::fillTransform() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapepath.html#fillTransform

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QQuickShapePath::fillTransform() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickShapePath13fillTransformEv',
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  def fillItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickShapePath::fillItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapepath.html#fillItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickShapePath::fillItem() const
    address = self.uglySide.call('ritual_ZNK15QQuickShapePath8fillItemEv')
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def hasTrim(self) -> bool:
    """
    Calls Qt's 'bool QQuickShapePath::hasTrim() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapepath.html#hasTrim
    """
    #  bool QQuickShapePath::hasTrim() const
    return self.uglySide.call('ritual_ZNK15QQuickShapePath7hasTrimEv')

  def cosmeticStroke(self) -> bool:
    """
    Calls Qt's 'bool QQuickShapePath::cosmeticStroke() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#cosmeticStroke
    """
    #  bool QQuickShapePath::cosmeticStroke() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickShapePath14cosmeticStrokeEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setStrokeColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickShapePath::setStrokeColor(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#setStrokeColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickShapePath::setStrokeColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN15QQuickShapePath14setStrokeColorERK6QColor',
        self._valueOf(color),
    )

  @overload(float)
  def setStrokeWidth(self, w: float) -> None:
    """
    Calls Qt's 'void QQuickShapePath::setStrokeWidth(qreal w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#setStrokeWidth

    Parameters
    ----------

    w : float
      Passed on as it is.
    """
    #  void QQuickShapePath::setStrokeWidth(qreal w)
    self.uglySide.call('ritual_ZN15QQuickShapePath14setStrokeWidthEd', w)

  @overload(QQuickShapeGradient)
  @overload(NoneType)
  def setStrokeGradient(
      self,
      gradient: Optional[QQuickShapeGradient],
  ) -> None:
    """
    Calls Qt's 'void QQuickShapePath::setStrokeGradient(QQuickShapeGradient
    *gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#setStrokeGradient

    Parameters
    ----------

    gradient : Optional[QQuickShapeGradient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickShapePath::setStrokeGradient(QQuickShapeGradient *gradient)
    self.uglySide.call(
        'ritual_ZN15QQuickShapePath17setStrokeGradientEP19QQuickShapeGradie'
        'nt',
        self._addressOf(gradient),
    )

  @overload(QColor)
  def setFillColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickShapePath::setFillColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapepath.html#setFillColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickShapePath::setFillColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN15QQuickShapePath12setFillColorERK6QColor',
        self._valueOf(color),
    )

  @overload(FillRule)
  def setFillRule(self, fillRule: FillRule) -> None:
    """
    Calls Qt's 'void QQuickShapePath::setFillRule(FillRule fillRule)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapepath.html#setFillRule

    Parameters
    ----------

    fillRule : FillRule
      Passed on as its number.
    """
    #  void QQuickShapePath::setFillRule(FillRule fillRule)
    self.uglySide.call(
        'ritual_ZN15QQuickShapePath11setFillRuleENS_8FillRuleE',
        fillRule.value,
    )

  @overload(JoinStyle)
  def setJoinStyle(self, style: JoinStyle) -> None:
    """
    Calls Qt's 'void QQuickShapePath::setJoinStyle(JoinStyle style)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapepath.html#setJoinStyle

    Parameters
    ----------

    style : JoinStyle
      Passed on as its number.
    """
    #  void QQuickShapePath::setJoinStyle(JoinStyle style)
    self.uglySide.call(
        'ritual_ZN15QQuickShapePath12setJoinStyleENS_9JoinStyleE',
        style.value,
    )

  @overload(int)
  def setMiterLimit(self, limit: int) -> None:
    """
    Calls Qt's 'void QQuickShapePath::setMiterLimit(int limit)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapepath.html#setMiterLimit

    Parameters
    ----------

    limit : int
      Passed on as it is.
    """
    #  void QQuickShapePath::setMiterLimit(int limit)
    self.uglySide.call('ritual_ZN15QQuickShapePath13setMiterLimitEi', limit)

  @overload(CapStyle)
  def setCapStyle(self, style: CapStyle) -> None:
    """
    Calls Qt's 'void QQuickShapePath::setCapStyle(CapStyle style)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapepath.html#setCapStyle

    Parameters
    ----------

    style : CapStyle
      Passed on as its number.
    """
    #  void QQuickShapePath::setCapStyle(CapStyle style)
    self.uglySide.call(
        'ritual_ZN15QQuickShapePath11setCapStyleENS_8CapStyleE', style.value,
    )

  @overload(StrokeStyle)
  def setStrokeStyle(self, style: StrokeStyle) -> None:
    """
    Calls Qt's 'void QQuickShapePath::setStrokeStyle(StrokeStyle style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#setStrokeStyle

    Parameters
    ----------

    style : StrokeStyle
      Passed on as its number.
    """
    #  void QQuickShapePath::setStrokeStyle(StrokeStyle style)
    self.uglySide.call(
        'ritual_ZN15QQuickShapePath14setStrokeStyleENS_11StrokeStyleE',
        style.value,
    )

  @overload(float)
  def setDashOffset(self, offset: float) -> None:
    """
    Calls Qt's 'void QQuickShapePath::setDashOffset(qreal offset)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapepath.html#setDashOffset

    Parameters
    ----------

    offset : float
      Passed on as it is.
    """
    #  void QQuickShapePath::setDashOffset(qreal offset)
    self.uglySide.call('ritual_ZN15QQuickShapePath13setDashOffsetEd', offset)

  @overload(QQuickShapeGradient)
  @overload(NoneType)
  def setFillGradient(self, gradient: Optional[QQuickShapeGradient]) -> None:
    """
    Calls Qt's 'void QQuickShapePath::setFillGradient(QQuickShapeGradient
    *gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#setFillGradient

    Parameters
    ----------

    gradient : Optional[QQuickShapeGradient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickShapePath::setFillGradient(QQuickShapeGradient *gradient)
    self.uglySide.call(
        'ritual_ZN15QQuickShapePath15setFillGradientEP19QQuickShapeGradient',
        self._addressOf(gradient),
    )

  @overload(PathHints)
  def setPathHints(self, newPathHints: PathHints) -> None:
    """
    Calls Qt's 'void QQuickShapePath::setPathHints(PathHints newPathHints)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapepath.html#setPathHints

    Parameters
    ----------

    newPathHints : PathHints
      Passed on as its number.
    """
    #  void QQuickShapePath::setPathHints(PathHints newPathHints)
    self.uglySide.call(
        'ritual_ZN15QQuickShapePath12setPathHintsE6QFlagsINS_8PathHintEE',
        newPathHints.value,
    )

  @overload(QMatrix4x4)
  def setFillTransform(self, matrix: QMatrix4x4) -> None:
    """
    Calls Qt's 'void QQuickShapePath::setFillTransform(const QMatrix4x4
    &matrix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#setFillTransform

    Parameters
    ----------

    matrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void QQuickShapePath::setFillTransform(const QMatrix4x4 &matrix)
    self.uglySide.call(
        'ritual_ZN15QQuickShapePath16setFillTransformERK10QMatrix4x4',
        self._valueOf(matrix),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setFillItem(self, newFillItem: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickShapePath::setFillItem(QQuickItem *newFillItem)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapepath.html#setFillItem

    Parameters
    ----------

    newFillItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickShapePath::setFillItem(QQuickItem *newFillItem)
    self.uglySide.call(
        'ritual_ZN15QQuickShapePath11setFillItemEP10QQuickItem',
        self._addressOf(newFillItem),
    )

  @overload(bool)
  def setCosmeticStroke(self, c: bool) -> None:
    """
    Calls Qt's 'void QQuickShapePath::setCosmeticStroke(bool c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#setCosmeticStroke

    Parameters
    ----------

    c : bool
      Passed on as it is.
    """
    #  void QQuickShapePath::setCosmeticStroke(bool c)
    self.uglySide.call('ritual_ZN15QQuickShapePath17setCosmeticStrokeEb', c)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickShapePath::QQuickShapePath(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#QQuickShapePath

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickShapePath::QQuickShapePath(QObject *parent)
    self._noteCreation(QQuickShapePath, lambda: Rituals.call(
        'ritual_ZN15QQuickShapePathC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def resetStrokeGradient(self) -> None:
    """
    Calls Qt's 'void QQuickShapePath::resetStrokeGradient()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#resetStrokeGradient
    """
    #  void QQuickShapePath::resetStrokeGradient()
    self.uglySide.call('ritual_ZN15QQuickShapePath19resetStrokeGradientEv')

  def resetFillGradient(self) -> None:
    """
    Calls Qt's 'void QQuickShapePath::resetFillGradient()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#resetFillGradient
    """
    #  void QQuickShapePath::resetFillGradient()
    self.uglySide.call('ritual_ZN15QQuickShapePath17resetFillGradientEv')

  def trim(self) -> Optional[QQuickShapeTrim]:
    """
    Calls Qt's 'QQuickShapeTrim *QQuickShapePath::trim()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapepath.html#trim

    Returns
    -------

    Optional[QQuickShapeTrim]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickShapeTrim *QQuickShapePath::trim()
    address = self.uglySide.call('ritual_ZN15QQuickShapePath4trimEv')
    from . import QQuickShapeTrim
    return QQuickShapeTrim._cuteAt(address)

  def shapePathChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShapePath::shapePathChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#shapePathChanged
    """
    #  void QQuickShapePath::shapePathChanged()
    self.uglySide.call('ritual_ZN15QQuickShapePath16shapePathChangedEv')

  def strokeColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShapePath::strokeColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#strokeColorChanged
    """
    #  void QQuickShapePath::strokeColorChanged()
    self.uglySide.call('ritual_ZN15QQuickShapePath18strokeColorChangedEv')

  def strokeWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShapePath::strokeWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#strokeWidthChanged
    """
    #  void QQuickShapePath::strokeWidthChanged()
    self.uglySide.call('ritual_ZN15QQuickShapePath18strokeWidthChangedEv')

  def fillColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShapePath::fillColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#fillColorChanged
    """
    #  void QQuickShapePath::fillColorChanged()
    self.uglySide.call('ritual_ZN15QQuickShapePath16fillColorChangedEv')

  def fillRuleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShapePath::fillRuleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#fillRuleChanged
    """
    #  void QQuickShapePath::fillRuleChanged()
    self.uglySide.call('ritual_ZN15QQuickShapePath15fillRuleChangedEv')

  def joinStyleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShapePath::joinStyleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#joinStyleChanged
    """
    #  void QQuickShapePath::joinStyleChanged()
    self.uglySide.call('ritual_ZN15QQuickShapePath16joinStyleChangedEv')

  def miterLimitChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShapePath::miterLimitChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#miterLimitChanged
    """
    #  void QQuickShapePath::miterLimitChanged()
    self.uglySide.call('ritual_ZN15QQuickShapePath17miterLimitChangedEv')

  def capStyleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShapePath::capStyleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#capStyleChanged
    """
    #  void QQuickShapePath::capStyleChanged()
    self.uglySide.call('ritual_ZN15QQuickShapePath15capStyleChangedEv')

  def strokeStyleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShapePath::strokeStyleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#strokeStyleChanged
    """
    #  void QQuickShapePath::strokeStyleChanged()
    self.uglySide.call('ritual_ZN15QQuickShapePath18strokeStyleChangedEv')

  def dashOffsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShapePath::dashOffsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#dashOffsetChanged
    """
    #  void QQuickShapePath::dashOffsetChanged()
    self.uglySide.call('ritual_ZN15QQuickShapePath17dashOffsetChangedEv')

  def dashPatternChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShapePath::dashPatternChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#dashPatternChanged
    """
    #  void QQuickShapePath::dashPatternChanged()
    self.uglySide.call('ritual_ZN15QQuickShapePath18dashPatternChangedEv')

  def fillGradientChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShapePath::fillGradientChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#fillGradientChanged
    """
    #  void QQuickShapePath::fillGradientChanged()
    self.uglySide.call('ritual_ZN15QQuickShapePath19fillGradientChangedEv')

  def pathHintsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShapePath::pathHintsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#pathHintsChanged
    """
    #  void QQuickShapePath::pathHintsChanged()
    self.uglySide.call('ritual_ZN15QQuickShapePath16pathHintsChangedEv')

  def fillTransformChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShapePath::fillTransformChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#fillTransformChanged
    """
    #  void QQuickShapePath::fillTransformChanged()
    self.uglySide.call('ritual_ZN15QQuickShapePath20fillTransformChangedEv')

  def fillItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShapePath::fillItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#fillItemChanged
    """
    #  void QQuickShapePath::fillItemChanged()
    self.uglySide.call('ritual_ZN15QQuickShapePath15fillItemChangedEv')

  def cosmeticStrokeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShapePath::cosmeticStrokeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#cosmeticStrokeChanged
    """
    #  void QQuickShapePath::cosmeticStrokeChanged()
    self.uglySide.call('ritual_ZN15QQuickShapePath21cosmeticStrokeChangedEv')

  def strokeGradientChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShapePath::strokeGradientChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshapepath.html#strokeGradientChanged
    """
    #  void QQuickShapePath::strokeGradientChanged()
    self.uglySide.call('ritual_ZN15QQuickShapePath21strokeGradientChangedEv')

  def d_func(self) -> Optional[QQuickShapePathPrivate]:
    """
    Calls Qt's 'QQuickShapePathPrivate *QQuickShapePath::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshapepath.html#d_func

    Returns
    -------

    Optional[QQuickShapePathPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickShapePathPrivate *QQuickShapePath::d_func()
    address = self.uglySide.call('ritual_ZN15QQuickShapePath6d_funcEv')
    from . import QQuickShapePathPrivate
    return QQuickShapePathPrivate._cuteAt(address)

  @staticmethod
  def dashPattern(*__, **_) -> Never:
    """
    Qt's 'QList<qreal> QQuickShapePath::dashPattern() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickShapePath.dashPattern' has no cute function yet. Qt's "
        "'QList<qreal> QQuickShapePath::dashPattern() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def setDashPattern(*__, **_) -> Never:
    """
    Qt's 'void QQuickShapePath::setDashPattern(const QList<qreal> &array)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickShapePath.setDashPattern' has no cute function yet. Qt's "
        "'void QQuickShapePath::setDashPattern(const QList<qreal> &array)': "
        "takes a type Python has no way to hand over yet.")
