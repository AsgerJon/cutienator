"""
QQuickPathRectangle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpath_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickPathRectangle to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QQuickCurve

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPathRectangle(QQuickCurve):
  """
  The cute side of Qt's QQuickPathRectangle: a plain Python object standing
  in front of one C++ QQuickPathRectangle.

  It is built on the cute 'QQuickCurve', as Qt's QQuickPathRectangle is built
  on Qt's QQuickCurve, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPathRectangle that has a ritual and that
  Python can call so far, 57 names in all: 'metaObject', 'tr', 'width',
  'setWidth', 'height', 'setHeight', 'strokeAdjustment',
  'setStrokeAdjustment', 'radius', 'setRadius', 'topLeftRadius',
  'setTopLeftRadius', 'resetTopLeftRadius', 'topRightRadius',
  'setTopRightRadius', 'resetTopRightRadius', 'bottomLeftRadius',
  'setBottomLeftRadius', 'resetBottomLeftRadius', 'bottomRightRadius',
  'setBottomRightRadius', 'resetBottomRightRadius', 'cornerRadius',
  'setCornerRadius', 'resetCornerRadius', 'hasBevel', 'setBevel',
  'hasTopLeftBevel', 'setTopLeftBevel', 'resetTopLeftBevel',
  'hasTopRightBevel', 'setTopRightBevel', 'resetTopRightBevel',
  'hasBottomLeftBevel', 'setBottomLeftBevel', 'resetBottomLeftBevel',
  'hasBottomRightBevel', 'setBottomRightBevel', 'resetBottomRightBevel',
  'cornerBevel', 'setCornerBevel', 'resetCornerBevel', 'widthChanged',
  'heightChanged', 'strokeAdjustmentChanged', 'radiusChanged',
  'topLeftRadiusChanged', 'topRightRadiusChanged', 'bottomLeftRadiusChanged',
  'bottomRightRadiusChanged', 'bevelChanged', 'topLeftBevelChanged',
  'topRightBevelChanged', 'bottomLeftBevelChanged',
  'bottomRightBevelChanged', 'emitCornerRadiusChanged',
  'emitCornerBevelChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPathRectangle::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickPathRectangle::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickPathRectangle::addToPath(QPainterPath &path, const
    QQuickPathData &a1)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 63 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickPathRectangle is created at the first use, not by
    'QQuickPathRectangle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPathRectangle.
  - Qt tells when it has removed the C++ QQuickPathRectangle. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickPathRectangle::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathrectangle.html#tr

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
    #  QString QQuickPathRectangle::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuickPathRectangle2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPathRectangle'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPathRectangle::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPathRectangle::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickPathRectangle10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def width(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathRectangle::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathrectangle.html#width
    """
    #  qreal QQuickPathRectangle::width() const
    return self.uglySide.call('ritual_ZNK19QQuickPathRectangle5widthEv')

  def height(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathRectangle::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathrectangle.html#height
    """
    #  qreal QQuickPathRectangle::height() const
    return self.uglySide.call('ritual_ZNK19QQuickPathRectangle6heightEv')

  def strokeAdjustment(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathRectangle::strokeAdjustment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#strokeAdjustment
    """
    #  qreal QQuickPathRectangle::strokeAdjustment() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickPathRectangle16strokeAdjustmentEv',
    )

  def radius(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathRectangle::radius() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathrectangle.html#radius
    """
    #  qreal QQuickPathRectangle::radius() const
    return self.uglySide.call('ritual_ZNK19QQuickPathRectangle6radiusEv')

  def topLeftRadius(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathRectangle::topLeftRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#topLeftRadius
    """
    #  qreal QQuickPathRectangle::topLeftRadius() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickPathRectangle13topLeftRadiusEv',
    )

  def topRightRadius(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathRectangle::topRightRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#topRightRadius
    """
    #  qreal QQuickPathRectangle::topRightRadius() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickPathRectangle14topRightRadiusEv',
    )

  def bottomLeftRadius(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathRectangle::bottomLeftRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#bottomLeftRadius
    """
    #  qreal QQuickPathRectangle::bottomLeftRadius() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickPathRectangle16bottomLeftRadiusEv',
    )

  def bottomRightRadius(self) -> float:
    """
    Calls Qt's 'qreal QQuickPathRectangle::bottomRightRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#bottomRightRadius
    """
    #  qreal QQuickPathRectangle::bottomRightRadius() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickPathRectangle17bottomRightRadiusEv',
    )

  @overload(Qt.Corner)
  def cornerRadius(self, corner: Qt.Corner) -> float:
    """
    Calls Qt's 'qreal QQuickPathRectangle::cornerRadius(Qt::Corner corner)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#cornerRadius

    Parameters
    ----------

    corner : Qt.Corner
      Passed on as its number.
    """
    #  qreal QQuickPathRectangle::cornerRadius(Qt::Corner corner) const
    return self.uglySide.call(
        'ritual_ZNK19QQuickPathRectangle12cornerRadiusEN2Qt6CornerE',
        corner.value,
    )

  def hasBevel(self) -> bool:
    """
    Calls Qt's 'bool QQuickPathRectangle::hasBevel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathrectangle.html#hasBevel
    """
    #  bool QQuickPathRectangle::hasBevel() const
    return self.uglySide.call('ritual_ZNK19QQuickPathRectangle8hasBevelEv')

  def hasTopLeftBevel(self) -> bool:
    """
    Calls Qt's 'bool QQuickPathRectangle::hasTopLeftBevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#hasTopLeftBevel
    """
    #  bool QQuickPathRectangle::hasTopLeftBevel() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickPathRectangle15hasTopLeftBevelEv',
    )

  def hasTopRightBevel(self) -> bool:
    """
    Calls Qt's 'bool QQuickPathRectangle::hasTopRightBevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#hasTopRightBevel
    """
    #  bool QQuickPathRectangle::hasTopRightBevel() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickPathRectangle16hasTopRightBevelEv',
    )

  def hasBottomLeftBevel(self) -> bool:
    """
    Calls Qt's 'bool QQuickPathRectangle::hasBottomLeftBevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#hasBottomLeftBevel
    """
    #  bool QQuickPathRectangle::hasBottomLeftBevel() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickPathRectangle18hasBottomLeftBevelEv',
    )

  def hasBottomRightBevel(self) -> bool:
    """
    Calls Qt's 'bool QQuickPathRectangle::hasBottomRightBevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#hasBottomRightBevel
    """
    #  bool QQuickPathRectangle::hasBottomRightBevel() const
    return self.uglySide.call(
        'ritual_ZNK19QQuickPathRectangle19hasBottomRightBevelEv',
    )

  @overload(Qt.Corner)
  def cornerBevel(self, corner: Qt.Corner) -> bool:
    """
    Calls Qt's 'bool QQuickPathRectangle::cornerBevel(Qt::Corner corner)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#cornerBevel

    Parameters
    ----------

    corner : Qt.Corner
      Passed on as its number.
    """
    #  bool QQuickPathRectangle::cornerBevel(Qt::Corner corner) const
    return self.uglySide.call(
        'ritual_ZNK19QQuickPathRectangle11cornerBevelEN2Qt6CornerE',
        corner.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setWidth(self, width: float) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::setWidth(qreal width)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathrectangle.html#setWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void QQuickPathRectangle::setWidth(qreal width)
    self.uglySide.call('ritual_ZN19QQuickPathRectangle8setWidthEd', width)

  @overload(float)
  def setHeight(self, height: float) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::setHeight(qreal height)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathrectangle.html#setHeight

    Parameters
    ----------

    height : float
      Passed on as it is.
    """
    #  void QQuickPathRectangle::setHeight(qreal height)
    self.uglySide.call('ritual_ZN19QQuickPathRectangle9setHeightEd', height)

  @overload(float)
  def setStrokeAdjustment(self, newStrokeAdjustment: float) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::setStrokeAdjustment(qreal
    newStrokeAdjustment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#setStrokeAdjustment

    Parameters
    ----------

    newStrokeAdjustment : float
      Passed on as it is.
    """
    #  void QQuickPathRectangle::setStrokeAdjustment(qreal
    #      newStrokeAdjustment)
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle19setStrokeAdjustmentEd',
        newStrokeAdjustment,
    )

  @overload(float)
  def setRadius(self, newRadius: float) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::setRadius(qreal newRadius)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathrectangle.html#setRadius

    Parameters
    ----------

    newRadius : float
      Passed on as it is.
    """
    #  void QQuickPathRectangle::setRadius(qreal newRadius)
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle9setRadiusEd', newRadius,
    )

  @overload(float)
  def setTopLeftRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::setTopLeftRadius(qreal radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#setTopLeftRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QQuickPathRectangle::setTopLeftRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle16setTopLeftRadiusEd', radius,
    )

  @overload(float)
  def setTopRightRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::setTopRightRadius(qreal radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#setTopRightRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QQuickPathRectangle::setTopRightRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle17setTopRightRadiusEd', radius,
    )

  @overload(float)
  def setBottomLeftRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::setBottomLeftRadius(qreal radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#setBottomLeftRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QQuickPathRectangle::setBottomLeftRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle19setBottomLeftRadiusEd', radius,
    )

  @overload(float)
  def setBottomRightRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::setBottomRightRadius(qreal
    radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#setBottomRightRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QQuickPathRectangle::setBottomRightRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle20setBottomRightRadiusEd', radius,
    )

  @overload(Qt.Corner, float)
  def setCornerRadius(
      self,
      corner: Qt.Corner,
      newCornerRadius: float,
  ) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::setCornerRadius(Qt::Corner corner,
    qreal newCornerRadius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#setCornerRadius

    Parameters
    ----------

    corner : Qt.Corner
      Passed on as its number.

    newCornerRadius : float
      Passed on as it is.
    """
    #  void QQuickPathRectangle::setCornerRadius(Qt::Corner corner, qreal
    #      newCornerRadius)
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle15setCornerRadiusEN2Qt6CornerEd',
        corner.value, newCornerRadius,
    )

  @overload(bool)
  def setBevel(self, bevel: bool) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::setBevel(bool bevel)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpathrectangle.html#setBevel

    Parameters
    ----------

    bevel : bool
      Passed on as it is.
    """
    #  void QQuickPathRectangle::setBevel(bool bevel)
    self.uglySide.call('ritual_ZN19QQuickPathRectangle8setBevelEb', bevel)

  @overload(bool)
  def setTopLeftBevel(self, bevel: bool) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::setTopLeftBevel(bool bevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#setTopLeftBevel

    Parameters
    ----------

    bevel : bool
      Passed on as it is.
    """
    #  void QQuickPathRectangle::setTopLeftBevel(bool bevel)
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle15setTopLeftBevelEb', bevel,
    )

  @overload(bool)
  def setTopRightBevel(self, bevel: bool) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::setTopRightBevel(bool bevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#setTopRightBevel

    Parameters
    ----------

    bevel : bool
      Passed on as it is.
    """
    #  void QQuickPathRectangle::setTopRightBevel(bool bevel)
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle16setTopRightBevelEb', bevel,
    )

  @overload(bool)
  def setBottomLeftBevel(self, bevel: bool) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::setBottomLeftBevel(bool bevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#setBottomLeftBevel

    Parameters
    ----------

    bevel : bool
      Passed on as it is.
    """
    #  void QQuickPathRectangle::setBottomLeftBevel(bool bevel)
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle18setBottomLeftBevelEb', bevel,
    )

  @overload(bool)
  def setBottomRightBevel(self, bevel: bool) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::setBottomRightBevel(bool bevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#setBottomRightBevel

    Parameters
    ----------

    bevel : bool
      Passed on as it is.
    """
    #  void QQuickPathRectangle::setBottomRightBevel(bool bevel)
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle19setBottomRightBevelEb', bevel,
    )

  @overload(Qt.Corner, bool)
  def setCornerBevel(self, corner: Qt.Corner, newCornerBevel: bool) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::setCornerBevel(Qt::Corner corner,
    bool newCornerBevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#setCornerBevel

    Parameters
    ----------

    corner : Qt.Corner
      Passed on as its number.

    newCornerBevel : bool
      Passed on as it is.
    """
    #  void QQuickPathRectangle::setCornerBevel(Qt::Corner corner, bool
    #      newCornerBevel)
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle14setCornerBevelEN2Qt6CornerEb',
        corner.value, newCornerBevel,
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
    'QQuickPathRectangle::QQuickPathRectangle(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#QQuickPathRectangle

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPathRectangle::QQuickPathRectangle(QObject *parent)
    self._noteCreation(QQuickPathRectangle, lambda: Rituals.call(
        'ritual_ZN19QQuickPathRectangleC1EP7QObject',
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

  def resetTopLeftRadius(self) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::resetTopLeftRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#resetTopLeftRadius
    """
    #  void QQuickPathRectangle::resetTopLeftRadius()
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle18resetTopLeftRadiusEv',
    )

  def resetTopRightRadius(self) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::resetTopRightRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#resetTopRightRadius
    """
    #  void QQuickPathRectangle::resetTopRightRadius()
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle19resetTopRightRadiusEv',
    )

  def resetBottomLeftRadius(self) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::resetBottomLeftRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#resetBottomLeftRadius
    """
    #  void QQuickPathRectangle::resetBottomLeftRadius()
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle21resetBottomLeftRadiusEv',
    )

  def resetBottomRightRadius(self) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::resetBottomRightRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#resetBottomRightRadius
    """
    #  void QQuickPathRectangle::resetBottomRightRadius()
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle22resetBottomRightRadiusEv',
    )

  @overload(Qt.Corner)
  def resetCornerRadius(self, corner: Qt.Corner) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::resetCornerRadius(Qt::Corner
    corner)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#resetCornerRadius

    Parameters
    ----------

    corner : Qt.Corner
      Passed on as its number.
    """
    #  void QQuickPathRectangle::resetCornerRadius(Qt::Corner corner)
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle17resetCornerRadiusEN2Qt6CornerE',
        corner.value,
    )

  def resetTopLeftBevel(self) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::resetTopLeftBevel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#resetTopLeftBevel
    """
    #  void QQuickPathRectangle::resetTopLeftBevel()
    self.uglySide.call('ritual_ZN19QQuickPathRectangle17resetTopLeftBevelEv')

  def resetTopRightBevel(self) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::resetTopRightBevel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#resetTopRightBevel
    """
    #  void QQuickPathRectangle::resetTopRightBevel()
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle18resetTopRightBevelEv',
    )

  def resetBottomLeftBevel(self) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::resetBottomLeftBevel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#resetBottomLeftBevel
    """
    #  void QQuickPathRectangle::resetBottomLeftBevel()
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle20resetBottomLeftBevelEv',
    )

  def resetBottomRightBevel(self) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::resetBottomRightBevel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#resetBottomRightBevel
    """
    #  void QQuickPathRectangle::resetBottomRightBevel()
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle21resetBottomRightBevelEv',
    )

  @overload(Qt.Corner)
  def resetCornerBevel(self, corner: Qt.Corner) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::resetCornerBevel(Qt::Corner
    corner)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#resetCornerBevel

    Parameters
    ----------

    corner : Qt.Corner
      Passed on as its number.
    """
    #  void QQuickPathRectangle::resetCornerBevel(Qt::Corner corner)
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle16resetCornerBevelEN2Qt6CornerE',
        corner.value,
    )

  def widthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::widthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#widthChanged
    """
    #  void QQuickPathRectangle::widthChanged()
    self.uglySide.call('ritual_ZN19QQuickPathRectangle12widthChangedEv')

  def heightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::heightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#heightChanged
    """
    #  void QQuickPathRectangle::heightChanged()
    self.uglySide.call('ritual_ZN19QQuickPathRectangle13heightChangedEv')

  def strokeAdjustmentChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::strokeAdjustmentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#strokeAdjustmentChanged
    """
    #  void QQuickPathRectangle::strokeAdjustmentChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle23strokeAdjustmentChangedEv',
    )

  def radiusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::radiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#radiusChanged
    """
    #  void QQuickPathRectangle::radiusChanged()
    self.uglySide.call('ritual_ZN19QQuickPathRectangle13radiusChangedEv')

  def topLeftRadiusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::topLeftRadiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#topLeftRadiusChanged
    """
    #  void QQuickPathRectangle::topLeftRadiusChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle20topLeftRadiusChangedEv',
    )

  def topRightRadiusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::topRightRadiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#topRightRadiusChanged
    """
    #  void QQuickPathRectangle::topRightRadiusChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle21topRightRadiusChangedEv',
    )

  def bottomLeftRadiusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::bottomLeftRadiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#bottomLeftRadiusChanged
    """
    #  void QQuickPathRectangle::bottomLeftRadiusChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle23bottomLeftRadiusChangedEv',
    )

  def bottomRightRadiusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::bottomRightRadiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#bottomRightRadiusChanged
    """
    #  void QQuickPathRectangle::bottomRightRadiusChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle24bottomRightRadiusChangedEv',
    )

  def bevelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::bevelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#bevelChanged
    """
    #  void QQuickPathRectangle::bevelChanged()
    self.uglySide.call('ritual_ZN19QQuickPathRectangle12bevelChangedEv')

  def topLeftBevelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::topLeftBevelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#topLeftBevelChanged
    """
    #  void QQuickPathRectangle::topLeftBevelChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle19topLeftBevelChangedEv',
    )

  def topRightBevelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::topRightBevelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#topRightBevelChanged
    """
    #  void QQuickPathRectangle::topRightBevelChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle20topRightBevelChangedEv',
    )

  def bottomLeftBevelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::bottomLeftBevelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#bottomLeftBevelChanged
    """
    #  void QQuickPathRectangle::bottomLeftBevelChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle22bottomLeftBevelChangedEv',
    )

  def bottomRightBevelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::bottomRightBevelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#bottomRightBevelChanged
    """
    #  void QQuickPathRectangle::bottomRightBevelChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle23bottomRightBevelChangedEv',
    )

  @overload(Qt.Corner)
  def emitCornerRadiusChanged(self, corner: Qt.Corner) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::emitCornerRadiusChanged(Qt::Corner
    corner)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#emitCornerRadiusChanged

    Parameters
    ----------

    corner : Qt.Corner
      Passed on as its number.
    """
    #  void QQuickPathRectangle::emitCornerRadiusChanged(Qt::Corner corner)
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle23emitCornerRadiusChangedEN2Qt6Corne'
        'rE',
        corner.value,
    )

  @overload(Qt.Corner)
  def emitCornerBevelChanged(self, corner: Qt.Corner) -> None:
    """
    Calls Qt's 'void QQuickPathRectangle::emitCornerBevelChanged(Qt::Corner
    corner)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpathrectangle.html#emitCornerBevelChanged

    Parameters
    ----------

    corner : Qt.Corner
      Passed on as its number.
    """
    #  void QQuickPathRectangle::emitCornerBevelChanged(Qt::Corner corner)
    self.uglySide.call(
        'ritual_ZN19QQuickPathRectangle22emitCornerBevelChangedEN2Qt6Corner'
        'E',
        corner.value,
    )
