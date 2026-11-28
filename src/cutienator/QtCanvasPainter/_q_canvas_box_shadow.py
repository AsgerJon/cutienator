"""
QCanvasBoxShadow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/qcanvasboxshadow.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDebug, QRectF
  from ..QtGui import QColor
  from . import QCanvasBoxShadowPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCanvasBoxShadowPrivate = WAIT['QCanvasBoxShadowPrivate']
  QColor = WAIT['QColor']
  QDebug = WAIT['QDebug']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCanvasBoxShadow(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCanvasBoxShadow: a plain Python object standing in
  front of one C++ QCanvasBoxShadow.

  C++ hands a QCanvasBoxShadow around as a copy, so every C++
  QCanvasBoxShadow behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCanvasBoxShadow that has a ritual and that Python
  can call so far, 22 names in all: 'rect', 'setRect', 'boundingRect',
  'radius', 'setRadius', 'blur', 'setBlur', 'spread', 'setSpread', 'color',
  'setColor', 'topLeftRadius', 'setTopLeftRadius', 'topRightRadius',
  'setTopRightRadius', 'bottomLeftRadius', 'setBottomLeftRadius',
  'bottomRightRadius', 'setBottomRightRadius', '__eq__', '__ne__',
  '__rlshift__'. It can be made from Python, in 5 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCanvasBoxShadow &QCanvasBoxShadow::operator=(const
    QCanvasBoxShadow &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QCanvasBoxShadow::QCanvasBoxShadow(QCanvasBoxShadow &&a0)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QCanvasBoxShadow &QCanvasBoxShadow::operator=(QCanvasBoxShadow
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QCanvasBoxShadow::~QCanvasBoxShadow()': the destructor: Python
    removes its C++ QCanvasBoxShadow by it, and has no other use for it.
  - Qt's 'QCanvasBrush QCanvasBoxShadow::operator QCanvasBrush() const': an
    operator Python has no name for.
  - Qt's 'QVariant QCanvasBoxShadow::operator QVariant() const': an operator
    Python has no name for.
  - Qt's 'void QCanvasBoxShadow::swap(QCanvasBoxShadow &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QDataStream &operator<<(QDataStream &a0, const QCanvasBoxShadow
    &a1)': takes a type Python has no way to hand over yet.
  - Qt's 'QDataStream &operator>>(QDataStream &a0, QCanvasBoxShadow &a1)': an
    operator between other classes, written inside this one.

  What has no ritual
  ------------------

  1 of the 38 functions Qt declares: 1 leans on 'QCanvasBoxShadowPrivate.

  What to expect
  --------------

  - The C++ QCanvasBoxShadow is created at the first use, not by
    'QCanvasBoxShadow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanvasBoxShadow back gives a copy the ritual made
    for Python, in a new cute QCanvasBoxShadow.
  - Each name of Qt's QCanvasBoxShadow that has no cute function yet,
    'detach', 'swap', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanvasBoxShadow'

  #  Qt's '~QCanvasBoxShadow()'. Naming it makes this a value class: Python
  #  owns every C++ QCanvasBoxShadow behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QCanvasBoxShadowD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def rect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QCanvasBoxShadow::rect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasboxshadow.html#rect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QCanvasBoxShadow::rect() const
    address = self.uglySide.call('ritual_ZNK16QCanvasBoxShadow4rectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QCanvasBoxShadow::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasboxshadow.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QCanvasBoxShadow::boundingRect() const
    address = self.uglySide.call(
        'ritual_ZNK16QCanvasBoxShadow12boundingRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def radius(self) -> float:
    """
    Calls Qt's 'qreal QCanvasBoxShadow::radius() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasboxshadow.html#radius
    """
    #  qreal QCanvasBoxShadow::radius() const
    return self.uglySide.call('ritual_ZNK16QCanvasBoxShadow6radiusEv')

  def blur(self) -> float:
    """
    Calls Qt's 'qreal QCanvasBoxShadow::blur() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasboxshadow.html#blur
    """
    #  qreal QCanvasBoxShadow::blur() const
    return self.uglySide.call('ritual_ZNK16QCanvasBoxShadow4blurEv')

  def spread(self) -> float:
    """
    Calls Qt's 'qreal QCanvasBoxShadow::spread() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasboxshadow.html#spread
    """
    #  qreal QCanvasBoxShadow::spread() const
    return self.uglySide.call('ritual_ZNK16QCanvasBoxShadow6spreadEv')

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QCanvasBoxShadow::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasboxshadow.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QCanvasBoxShadow::color() const
    address = self.uglySide.call('ritual_ZNK16QCanvasBoxShadow5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def topLeftRadius(self) -> float:
    """
    Calls Qt's 'qreal QCanvasBoxShadow::topLeftRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasboxshadow.html#topLeftRadius
    """
    #  qreal QCanvasBoxShadow::topLeftRadius() const
    return self.uglySide.call(
        'ritual_ZNK16QCanvasBoxShadow13topLeftRadiusEv',
    )

  def topRightRadius(self) -> float:
    """
    Calls Qt's 'qreal QCanvasBoxShadow::topRightRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasboxshadow.html#topRightRadius
    """
    #  qreal QCanvasBoxShadow::topRightRadius() const
    return self.uglySide.call(
        'ritual_ZNK16QCanvasBoxShadow14topRightRadiusEv',
    )

  def bottomLeftRadius(self) -> float:
    """
    Calls Qt's 'qreal QCanvasBoxShadow::bottomLeftRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasboxshadow.html#bottomLeftRadius
    """
    #  qreal QCanvasBoxShadow::bottomLeftRadius() const
    return self.uglySide.call(
        'ritual_ZNK16QCanvasBoxShadow16bottomLeftRadiusEv',
    )

  def bottomRightRadius(self) -> float:
    """
    Calls Qt's 'qreal QCanvasBoxShadow::bottomRightRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasboxshadow.html#bottomRightRadius
    """
    #  qreal QCanvasBoxShadow::bottomRightRadius() const
    return self.uglySide.call(
        'ritual_ZNK16QCanvasBoxShadow17bottomRightRadiusEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRectF)
  def setRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void QCanvasBoxShadow::setRect(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasboxshadow.html#setRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QCanvasBoxShadow::setRect(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN16QCanvasBoxShadow7setRectERK6QRectF', self._valueOf(rect),
    )

  @overload(float, float, float, float)
  def setRect(self, x: float, y: float, width: float, height: float) -> None:
    """
    Calls Qt's 'void QCanvasBoxShadow::setRect(qreal x, qreal y, qreal width,
    qreal height)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasboxshadow.html#setRect

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
    #  void QCanvasBoxShadow::setRect(qreal x, qreal y, qreal width, qreal
    #      height)
    self.uglySide.call(
        'ritual_ZN16QCanvasBoxShadow7setRectEdddd', x, y, width, height,
    )

  @overload(float)
  def setRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QCanvasBoxShadow::setRadius(qreal radius)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasboxshadow.html#setRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QCanvasBoxShadow::setRadius(qreal radius)
    self.uglySide.call('ritual_ZN16QCanvasBoxShadow9setRadiusEd', radius)

  @overload(float)
  def setBlur(self, blur: float) -> None:
    """
    Calls Qt's 'void QCanvasBoxShadow::setBlur(qreal blur)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasboxshadow.html#setBlur

    Parameters
    ----------

    blur : float
      Passed on as it is.
    """
    #  void QCanvasBoxShadow::setBlur(qreal blur)
    self.uglySide.call('ritual_ZN16QCanvasBoxShadow7setBlurEd', blur)

  @overload(float)
  def setSpread(self, spread: float) -> None:
    """
    Calls Qt's 'void QCanvasBoxShadow::setSpread(qreal spread)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasboxshadow.html#setSpread

    Parameters
    ----------

    spread : float
      Passed on as it is.
    """
    #  void QCanvasBoxShadow::setSpread(qreal spread)
    self.uglySide.call('ritual_ZN16QCanvasBoxShadow9setSpreadEd', spread)

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QCanvasBoxShadow::setColor(QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasboxshadow.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QCanvasBoxShadow::setColor(QColor color)
    self.uglySide.call(
        'ritual_ZN16QCanvasBoxShadow8setColorE6QColor', self._valueOf(color),
    )

  @overload(float)
  def setTopLeftRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QCanvasBoxShadow::setTopLeftRadius(qreal radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasboxshadow.html#setTopLeftRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QCanvasBoxShadow::setTopLeftRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN16QCanvasBoxShadow16setTopLeftRadiusEd', radius,
    )

  @overload(float)
  def setTopRightRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QCanvasBoxShadow::setTopRightRadius(qreal radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasboxshadow.html#setTopRightRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QCanvasBoxShadow::setTopRightRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN16QCanvasBoxShadow17setTopRightRadiusEd', radius,
    )

  @overload(float)
  def setBottomLeftRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QCanvasBoxShadow::setBottomLeftRadius(qreal radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasboxshadow.html#setBottomLeftRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QCanvasBoxShadow::setBottomLeftRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN16QCanvasBoxShadow19setBottomLeftRadiusEd', radius,
    )

  @overload(float)
  def setBottomRightRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QCanvasBoxShadow::setBottomRightRadius(qreal radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasboxshadow.html#setBottomRightRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QCanvasBoxShadow::setBottomRightRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN16QCanvasBoxShadow20setBottomRightRadiusEd', radius,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QCanvasBoxShadow) -> bool:
    """
    Calls Qt's 'bool operator==(const QCanvasBoxShadow &lhs, const
    QCanvasBoxShadow &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasboxshadow.html#operator==

    Parameters
    ----------

    rhs : QCanvasBoxShadow
      Passed on as a value: Qt reads the C++ QCanvasBoxShadow, which stays
      Python's own.
    """
    #  bool operator==(const QCanvasBoxShadow &lhs, const QCanvasBoxShadow
    #      &rhs)
    return Rituals.call(
        'ritual_ZeqRK16QCanvasBoxShadowS1_',
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
  def __ne__(self, rhs: QCanvasBoxShadow) -> bool:
    """
    Calls Qt's 'bool operator!=(const QCanvasBoxShadow &lhs, const
    QCanvasBoxShadow &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasboxshadow.html#operator!=

    Parameters
    ----------

    rhs : QCanvasBoxShadow
      Passed on as a value: Qt reads the C++ QCanvasBoxShadow, which stays
      Python's own.
    """
    #  bool operator!=(const QCanvasBoxShadow &lhs, const QCanvasBoxShadow
    #      &rhs)
    return Rituals.call(
        'ritual_ZneRK16QCanvasBoxShadowS1_',
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
    Calls Qt's 'QDebug operator<<(QDebug a0, const QCanvasBoxShadow &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvasboxshadow.html#operator<<

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
    #  QDebug operator<<(QDebug a0, const QCanvasBoxShadow &a1)
    address = Rituals.call(
        'ritual_Zls6QDebugRK16QCanvasBoxShadow',
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
    Notes what was given, for Qt's 'QCanvasBoxShadow::QCanvasBoxShadow()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasboxshadow.html#QCanvasBoxShadow
    """
    #  QCanvasBoxShadow::QCanvasBoxShadow()
    self._noteCreation(QCanvasBoxShadow, lambda: Rituals.call(
        'ritual_ZN16QCanvasBoxShadowC1Ev',
    ))

  @overload(float, float, float, float)
  def __init__(
      self,
      x: float,
      y: float,
      width: float,
      height: float,
  ) -> None:
    """
    Notes what was given, for Qt's 'QCanvasBoxShadow::QCanvasBoxShadow(qreal
    x, qreal y, qreal width, qreal height)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasboxshadow.html#QCanvasBoxShadow

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
    #  QCanvasBoxShadow::QCanvasBoxShadow(qreal x, qreal y, qreal width,
    #      qreal height)
    self._noteCreation(QCanvasBoxShadow, lambda: Rituals.call(
        'ritual_ZN16QCanvasBoxShadowC1Edddd', x, y, width, height,
    ))

  @overload(QRectF)
  def __init__(self, rect: QRectF) -> None:
    """
    Notes what was given, for Qt's 'QCanvasBoxShadow::QCanvasBoxShadow(const
    QRectF &rect)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasboxshadow.html#QCanvasBoxShadow

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  QCanvasBoxShadow::QCanvasBoxShadow(const QRectF &rect)
    self._noteCreation(QCanvasBoxShadow, lambda: Rituals.call(
        'ritual_ZN16QCanvasBoxShadowC1ERK6QRectF', self._valueOf(rect),
    ))

  @overload(THIS)
  def __init__(self, a0: QCanvasBoxShadow) -> None:
    """
    Notes what was given, for Qt's 'QCanvasBoxShadow::QCanvasBoxShadow(const
    QCanvasBoxShadow &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasboxshadow.html#QCanvasBoxShadow

    Parameters
    ----------

    a0 : QCanvasBoxShadow
      Passed on as a value: Qt reads the C++ QCanvasBoxShadow, which stays
      Python's own.
    """
    #  QCanvasBoxShadow::QCanvasBoxShadow(const QCanvasBoxShadow &a0)
    self._noteCreation(QCanvasBoxShadow, lambda: Rituals.call(
        'ritual_ZN16QCanvasBoxShadowC1ERKS_', self._valueOf(a0),
    ))

  @overload(QCanvasBoxShadowPrivate)
  @overload(NoneType)
  def __init__(self, p: Optional[QCanvasBoxShadowPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasBoxShadow::QCanvasBoxShadow(QCanvasBoxShadowPrivate *p)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasboxshadow.html#QCanvasBoxShadow

    Parameters
    ----------

    p : Optional[QCanvasBoxShadowPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QCanvasBoxShadow::QCanvasBoxShadow(QCanvasBoxShadowPrivate *p)
    self._noteCreation(QCanvasBoxShadow, lambda: Rituals.call(
        'ritual_ZN16QCanvasBoxShadowC1EP23QCanvasBoxShadowPrivate',
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

  @staticmethod
  def detach(*__, **_) -> Never:
    """
    Qt's 'void QCanvasBoxShadow::detach()': leans on
    'QCanvasBoxShadowPrivate::createPaint(QCanvasPainter*) const', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QCanvasBoxShadow.detach' has no cute function yet. Qt's 'void "
        "QCanvasBoxShadow::detach()': leans on "
        "'QCanvasBoxShadowPrivate::createPaint(QCanvasPainter*) const', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QCanvasBoxShadow::swap(QCanvasBoxShadow &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCanvasBoxShadow.swap' has no cute function yet. Qt's 'void "
        "QCanvasBoxShadow::swap(QCanvasBoxShadow &other)': takes a type "
        "Python has no way to hand over yet.")
