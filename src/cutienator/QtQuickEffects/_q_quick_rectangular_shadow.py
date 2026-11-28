"""
QQuickRectangularShadow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickEffects/6.12.0/QtQuickEffects/private/qquickrectangularshadow_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickRectangularShadow to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF
  from ..QtGui import QColor, QVector2D
  from . import QQuickRectangularShadowPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QRectF = WAIT['QRectF']
  QVector2D = WAIT['QVector2D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickRectangularShadow(QQuickItem):
  """
  The cute side of Qt's QQuickRectangularShadow: a plain Python object
  standing in front of one C++ QQuickRectangularShadow.

  It is built on the cute 'QQuickItem', as Qt's QQuickRectangularShadow is
  built on Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickRectangularShadow that has a ritual and that
  Python can call so far, 43 names in all: 'metaObject', 'tr', 'offset',
  'setOffset', 'color', 'setColor', 'blur', 'setBlur', 'radius', 'setRadius',
  'spread', 'setSpread', 'isCached', 'setCached', 'material', 'setMaterial',
  'topLeftRadius', 'setTopLeftRadius', 'resetTopLeftRadius',
  'topRightRadius', 'setTopRightRadius', 'resetTopRightRadius',
  'bottomLeftRadius', 'setBottomLeftRadius', 'resetBottomLeftRadius',
  'bottomRightRadius', 'setBottomRightRadius', 'resetBottomRightRadius',
  'offsetChanged', 'colorChanged', 'blurChanged', 'radiusChanged',
  'spreadChanged', 'cachedChanged', 'materialChanged',
  'topLeftRadiusChanged', 'topRightRadiusChanged', 'bottomLeftRadiusChanged',
  'bottomRightRadiusChanged', 'componentComplete', 'geometryChange',
  'itemChange', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickRectangularShadow::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickRectangularShadow::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickRectangularShadowPrivate
    *QQuickRectangularShadow::d_func() const': takes in Python what
    'QQuickRectangularShadowPrivate *QQuickRectangularShadow::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 49 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickRectangularShadow is created at the first use, not by
    'QQuickRectangularShadow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickRectangularShadow.
  - Qt tells when it has removed the C++ QQuickRectangularShadow. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickRectangularShadow::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangularshadow.html#tr

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
    #  QString QQuickRectangularShadow::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQuickRectangularShadow2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickRectangularShadow'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickRectangularShadow::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickRectangularShadow::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickRectangularShadow10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def offset(self) -> QVector2D:
    """
    Calls Qt's 'QVector2D QQuickRectangularShadow::offset() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#offset

    Returns
    -------

    QVector2D
      A new cute QVector2D around the copy Qt gave back. Python owns it.
    """
    #  QVector2D QQuickRectangularShadow::offset() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickRectangularShadow6offsetEv',
    )
    from ..QtGui import QVector2D
    return QVector2D._cuteOwning(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickRectangularShadow::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangularshadow.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickRectangularShadow::color() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickRectangularShadow5colorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def blur(self) -> float:
    """
    Calls Qt's 'qreal QQuickRectangularShadow::blur() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangularshadow.html#blur
    """
    #  qreal QQuickRectangularShadow::blur() const
    return self.uglySide.call('ritual_ZNK23QQuickRectangularShadow4blurEv')

  def radius(self) -> float:
    """
    Calls Qt's 'qreal QQuickRectangularShadow::radius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#radius
    """
    #  qreal QQuickRectangularShadow::radius() const
    return self.uglySide.call('ritual_ZNK23QQuickRectangularShadow6radiusEv')

  def spread(self) -> float:
    """
    Calls Qt's 'qreal QQuickRectangularShadow::spread() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#spread
    """
    #  qreal QQuickRectangularShadow::spread() const
    return self.uglySide.call('ritual_ZNK23QQuickRectangularShadow6spreadEv')

  def isCached(self) -> bool:
    """
    Calls Qt's 'bool QQuickRectangularShadow::isCached() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#isCached
    """
    #  bool QQuickRectangularShadow::isCached() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickRectangularShadow8isCachedEv',
    )

  def material(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickRectangularShadow::material() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#material

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickRectangularShadow::material() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickRectangularShadow8materialEv',
    )
    return QQuickItem._cuteAt(address)

  def topLeftRadius(self) -> float:
    """
    Calls Qt's 'qreal QQuickRectangularShadow::topLeftRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#topLeftRadius
    """
    #  qreal QQuickRectangularShadow::topLeftRadius() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickRectangularShadow13topLeftRadiusEv',
    )

  def topRightRadius(self) -> float:
    """
    Calls Qt's 'qreal QQuickRectangularShadow::topRightRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#topRightRadius
    """
    #  qreal QQuickRectangularShadow::topRightRadius() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickRectangularShadow14topRightRadiusEv',
    )

  def bottomLeftRadius(self) -> float:
    """
    Calls Qt's 'qreal QQuickRectangularShadow::bottomLeftRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#bottomLeftRadius
    """
    #  qreal QQuickRectangularShadow::bottomLeftRadius() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickRectangularShadow16bottomLeftRadiusEv',
    )

  def bottomRightRadius(self) -> float:
    """
    Calls Qt's 'qreal QQuickRectangularShadow::bottomRightRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#bottomRightRadius
    """
    #  qreal QQuickRectangularShadow::bottomRightRadius() const
    return self.uglySide.call(
        'ritual_ZNK23QQuickRectangularShadow17bottomRightRadiusEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector2D)
  def setOffset(self, offset: QVector2D) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::setOffset(const QVector2D
    &offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#setOffset

    Parameters
    ----------

    offset : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void QQuickRectangularShadow::setOffset(const QVector2D &offset)
    self.uglySide.call(
        'ritual_ZN23QQuickRectangularShadow9setOffsetERK9QVector2D',
        self._valueOf(offset),
    )

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::setColor(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickRectangularShadow::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN23QQuickRectangularShadow8setColorERK6QColor',
        self._valueOf(color),
    )

  @overload(float)
  def setBlur(self, blur: float) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::setBlur(qreal blur)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#setBlur

    Parameters
    ----------

    blur : float
      Passed on as it is.
    """
    #  void QQuickRectangularShadow::setBlur(qreal blur)
    self.uglySide.call('ritual_ZN23QQuickRectangularShadow7setBlurEd', blur)

  @overload(float)
  def setRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::setRadius(qreal radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#setRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QQuickRectangularShadow::setRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN23QQuickRectangularShadow9setRadiusEd', radius,
    )

  @overload(float)
  def setSpread(self, spread: float) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::setSpread(qreal spread)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#setSpread

    Parameters
    ----------

    spread : float
      Passed on as it is.
    """
    #  void QQuickRectangularShadow::setSpread(qreal spread)
    self.uglySide.call(
        'ritual_ZN23QQuickRectangularShadow9setSpreadEd', spread,
    )

  @overload(bool)
  def setCached(self, cached: bool) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::setCached(bool cached)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#setCached

    Parameters
    ----------

    cached : bool
      Passed on as it is.
    """
    #  void QQuickRectangularShadow::setCached(bool cached)
    self.uglySide.call(
        'ritual_ZN23QQuickRectangularShadow9setCachedEb', cached,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setMaterial(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::setMaterial(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#setMaterial

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRectangularShadow::setMaterial(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN23QQuickRectangularShadow11setMaterialEP10QQuickItem',
        self._addressOf(item),
    )

  @overload(float)
  def setTopLeftRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::setTopLeftRadius(qreal
    radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#setTopLeftRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QQuickRectangularShadow::setTopLeftRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN23QQuickRectangularShadow16setTopLeftRadiusEd', radius,
    )

  @overload(float)
  def setTopRightRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::setTopRightRadius(qreal
    radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#setTopRightRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QQuickRectangularShadow::setTopRightRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN23QQuickRectangularShadow17setTopRightRadiusEd', radius,
    )

  @overload(float)
  def setBottomLeftRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::setBottomLeftRadius(qreal
    radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#setBottomLeftRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QQuickRectangularShadow::setBottomLeftRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN23QQuickRectangularShadow19setBottomLeftRadiusEd', radius,
    )

  @overload(float)
  def setBottomRightRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::setBottomRightRadius(qreal
    radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#setBottomRightRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QQuickRectangularShadow::setBottomRightRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN23QQuickRectangularShadow20setBottomRightRadiusEd', radius,
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
    'QQuickRectangularShadow::QQuickRectangularShadow(QQuickItem *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickRectangularShadow::QQuickRectangularShadow(QQuickItem *parent)
    self._noteCreation(QQuickRectangularShadow, lambda: Rituals.call(
        'ritual_ZN23QQuickRectangularShadowC1EP10QQuickItem',
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

  def resetTopLeftRadius(self) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::resetTopLeftRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#resetTopLeftRadius
    """
    #  void QQuickRectangularShadow::resetTopLeftRadius()
    self.uglySide.call(
        'ritual_ZN23QQuickRectangularShadow18resetTopLeftRadiusEv',
    )

  def resetTopRightRadius(self) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::resetTopRightRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#resetTopRightRadius
    """
    #  void QQuickRectangularShadow::resetTopRightRadius()
    self.uglySide.call(
        'ritual_ZN23QQuickRectangularShadow19resetTopRightRadiusEv',
    )

  def resetBottomLeftRadius(self) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::resetBottomLeftRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#resetBottomLeftRadius
    """
    #  void QQuickRectangularShadow::resetBottomLeftRadius()
    self.uglySide.call(
        'ritual_ZN23QQuickRectangularShadow21resetBottomLeftRadiusEv',
    )

  def resetBottomRightRadius(self) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::resetBottomRightRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html
    """
    #  void QQuickRectangularShadow::resetBottomRightRadius()
    self.uglySide.call(
        'ritual_ZN23QQuickRectangularShadow22resetBottomRightRadiusEv',
    )

  def offsetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::offsetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#offsetChanged
    """
    #  void QQuickRectangularShadow::offsetChanged()
    self.uglySide.call('ritual_ZN23QQuickRectangularShadow13offsetChangedEv')

  def colorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::colorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#colorChanged
    """
    #  void QQuickRectangularShadow::colorChanged()
    self.uglySide.call('ritual_ZN23QQuickRectangularShadow12colorChangedEv')

  def blurChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::blurChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#blurChanged
    """
    #  void QQuickRectangularShadow::blurChanged()
    self.uglySide.call('ritual_ZN23QQuickRectangularShadow11blurChangedEv')

  def radiusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::radiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#radiusChanged
    """
    #  void QQuickRectangularShadow::radiusChanged()
    self.uglySide.call('ritual_ZN23QQuickRectangularShadow13radiusChangedEv')

  def spreadChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::spreadChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#spreadChanged
    """
    #  void QQuickRectangularShadow::spreadChanged()
    self.uglySide.call('ritual_ZN23QQuickRectangularShadow13spreadChangedEv')

  def cachedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::cachedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#cachedChanged
    """
    #  void QQuickRectangularShadow::cachedChanged()
    self.uglySide.call('ritual_ZN23QQuickRectangularShadow13cachedChangedEv')

  def materialChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::materialChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#materialChanged
    """
    #  void QQuickRectangularShadow::materialChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickRectangularShadow15materialChangedEv',
    )

  def topLeftRadiusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::topLeftRadiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#topLeftRadiusChanged
    """
    #  void QQuickRectangularShadow::topLeftRadiusChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickRectangularShadow20topLeftRadiusChangedEv',
    )

  def topRightRadiusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::topRightRadiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#topRightRadiusChanged
    """
    #  void QQuickRectangularShadow::topRightRadiusChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickRectangularShadow21topRightRadiusChangedEv',
    )

  def bottomLeftRadiusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::bottomLeftRadiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html
    """
    #  void QQuickRectangularShadow::bottomLeftRadiusChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickRectangularShadow23bottomLeftRadiusChangedEv',
    )

  def bottomRightRadiusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::bottomRightRadiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html
    """
    #  void QQuickRectangularShadow::bottomRightRadiusChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickRectangularShadow24bottomRightRadiusChangedEv',
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#componentComplete
    """
    #  void QQuickRectangularShadow::componentComplete()
    ritual = 'ritual_ZN23QQuickRectangularShadow17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQuickRectangularShadow17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickRectangularShadow::geometryChange(const QRectF
    #      &newGeometry, const QRectF &oldGeometry)
    ritual = (
        'ritual_ZN23QQuickRectangularShadow14geometryChangeERK6QRectFS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QQuickRectangularShadow14geometryChangeERK6QRectF'
          'S2_')
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickRectangularShadow::itemChange(ItemChange change,
    const ItemChangeData &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickRectangularShadow::itemChange(ItemChange change, const
    #      ItemChangeData &value)
    ritual = (
        'ritual_ZN23QQuickRectangularShadow10itemChangeEN10QQuickItem10Item'
        'ChangeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QQuickRectangularShadow10itemChangeEN10QQuickItem'
          '10ItemChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  def d_func(self) -> Optional[QQuickRectangularShadowPrivate]:
    """
    Calls Qt's 'QQuickRectangularShadowPrivate
    *QQuickRectangularShadow::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangularshadow.html#d_func

    Returns
    -------

    Optional[QQuickRectangularShadowPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickRectangularShadowPrivate *QQuickRectangularShadow::d_func()
    address = self.uglySide.call(
        'ritual_ZN23QQuickRectangularShadow6d_funcEv',
    )
    from . import QQuickRectangularShadowPrivate
    return QQuickRectangularShadowPrivate._cuteAt(address)
