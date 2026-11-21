"""
QGraphicsDropShadowEffect binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qgraphicseffect.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QGraphicsEffect

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF, QRectF
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsDropShadowEffect(QGraphicsEffect):
  """
  The cute side of Qt's QGraphicsDropShadowEffect: a plain Python object
  standing in front of one C++ QGraphicsDropShadowEffect.

  It is built on the cute 'QGraphicsEffect', as Qt's
  QGraphicsDropShadowEffect is built on Qt's QGraphicsEffect, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsDropShadowEffect that has a ritual and that
  Python can call so far, 13 names in all: 'metaObject', 'tr',
  'boundingRectFor', 'offset', 'xOffset', 'yOffset', 'blurRadius', 'color',
  'setOffset', 'setXOffset', 'setYOffset', 'setBlurRadius', 'setColor'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsDropShadowEffect::~QGraphicsDropShadowEffect()': the
    destructor: Python never removes a C++ QGraphicsDropShadowEffect.

  What has no ritual
  ------------------

  12 of the 29 functions Qt declares: 3 private; 3 a signal; 2 takes or gives
  a type that cannot be passed yet; 2 forbidden; 1 a template; 1 protected.

  What to expect
  --------------

  - The C++ QGraphicsDropShadowEffect is created at the first use, not by
    'QGraphicsDropShadowEffect(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsDropShadowEffect.
  - Qt tells when it has removed the C++ QGraphicsDropShadowEffect. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QGraphicsDropShadowEffect::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsdropshadoweffect.html#tr

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
    #  QString QGraphicsDropShadowEffect::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QGraphicsDropShadowEffect2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsDropShadowEffect'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGraphicsDropShadowEffect::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsdropshadoweffect.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGraphicsDropShadowEffect::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QGraphicsDropShadowEffect10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QRectF)
  def boundingRectFor(self, rect: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsDropShadowEffect::boundingRectFor(const
    QRectF &rect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsdropshadoweffect.html#boundingRectFor

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsDropShadowEffect::boundingRectFor(const QRectF &rect)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK25QGraphicsDropShadowEffect15boundingRectForERK6QRectF',
        self._valueOf(rect),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def offset(self) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsDropShadowEffect::offset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsdropshadoweffect.html#offset

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsDropShadowEffect::offset() const
    address = self.uglySide.call(
        'ritual_ZNK25QGraphicsDropShadowEffect6offsetEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def xOffset(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsDropShadowEffect::xOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsdropshadoweffect.html#xOffset
    """
    #  qreal QGraphicsDropShadowEffect::xOffset() const
    return self.uglySide.call(
        'ritual_ZNK25QGraphicsDropShadowEffect7xOffsetEv',
    )

  def yOffset(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsDropShadowEffect::yOffset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsdropshadoweffect.html#yOffset
    """
    #  qreal QGraphicsDropShadowEffect::yOffset() const
    return self.uglySide.call(
        'ritual_ZNK25QGraphicsDropShadowEffect7yOffsetEv',
    )

  def blurRadius(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsDropShadowEffect::blurRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsdropshadoweffect.html#blurRadius
    """
    #  qreal QGraphicsDropShadowEffect::blurRadius() const
    return self.uglySide.call(
        'ritual_ZNK25QGraphicsDropShadowEffect10blurRadiusEv',
    )

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QGraphicsDropShadowEffect::color() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsdropshadoweffect.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QGraphicsDropShadowEffect::color() const
    address = self.uglySide.call(
        'ritual_ZNK25QGraphicsDropShadowEffect5colorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setOffset(self, ofs: QPointF) -> None:
    """
    Calls Qt's 'void QGraphicsDropShadowEffect::setOffset(const QPointF
    &ofs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsdropshadoweffect.html#setOffset

    Parameters
    ----------

    ofs : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphicsDropShadowEffect::setOffset(const QPointF &ofs)
    self.uglySide.call(
        'ritual_ZN25QGraphicsDropShadowEffect9setOffsetERK7QPointF',
        self._valueOf(ofs),
    )

  @overload(float, float)
  def setOffset(self, dx: float, dy: float) -> None:
    """
    Calls Qt's 'void QGraphicsDropShadowEffect::setOffset(qreal dx, qreal
    dy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsdropshadoweffect.html#setOffset

    Parameters
    ----------

    dx : float
      Passed on as it is.

    dy : float
      Passed on as it is.
    """
    #  void QGraphicsDropShadowEffect::setOffset(qreal dx, qreal dy)
    self.uglySide.call(
        'ritual_ZN25QGraphicsDropShadowEffect9setOffsetEdd', dx, dy,
    )

  @overload(float)
  def setOffset(self, d: float) -> None:
    """
    Calls Qt's 'void QGraphicsDropShadowEffect::setOffset(qreal d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsdropshadoweffect.html#setOffset

    Parameters
    ----------

    d : float
      Passed on as it is.
    """
    #  void QGraphicsDropShadowEffect::setOffset(qreal d)
    self.uglySide.call('ritual_ZN25QGraphicsDropShadowEffect9setOffsetEd', d)

  @overload(float)
  def setXOffset(self, dx: float) -> None:
    """
    Calls Qt's 'void QGraphicsDropShadowEffect::setXOffset(qreal dx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsdropshadoweffect.html#setXOffset

    Parameters
    ----------

    dx : float
      Passed on as it is.
    """
    #  void QGraphicsDropShadowEffect::setXOffset(qreal dx)
    self.uglySide.call(
        'ritual_ZN25QGraphicsDropShadowEffect10setXOffsetEd', dx,
    )

  @overload(float)
  def setYOffset(self, dy: float) -> None:
    """
    Calls Qt's 'void QGraphicsDropShadowEffect::setYOffset(qreal dy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsdropshadoweffect.html#setYOffset

    Parameters
    ----------

    dy : float
      Passed on as it is.
    """
    #  void QGraphicsDropShadowEffect::setYOffset(qreal dy)
    self.uglySide.call(
        'ritual_ZN25QGraphicsDropShadowEffect10setYOffsetEd', dy,
    )

  @overload(float)
  def setBlurRadius(self, blurRadius: float) -> None:
    """
    Calls Qt's 'void QGraphicsDropShadowEffect::setBlurRadius(qreal
    blurRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsdropshadoweffect.html#setBlurRadius

    Parameters
    ----------

    blurRadius : float
      Passed on as it is.
    """
    #  void QGraphicsDropShadowEffect::setBlurRadius(qreal blurRadius)
    self.uglySide.call(
        'ritual_ZN25QGraphicsDropShadowEffect13setBlurRadiusEd', blurRadius,
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QGraphicsDropShadowEffect::setColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsdropshadoweffect.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QGraphicsDropShadowEffect::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN25QGraphicsDropShadowEffect8setColorERK6QColor',
        self._valueOf(color),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsDropShadowEffect::QGraphicsDropShadowEffect(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsdropshadoweffect.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QGraphicsDropShadowEffect::QGraphicsDropShadowEffect(QObject *parent)
    self._noteCreation(QGraphicsDropShadowEffect, lambda: Rituals.call(
        'ritual_ZN25QGraphicsDropShadowEffectC1EP7QObject',
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
