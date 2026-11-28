"""
QQuickRectangle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickrectangle_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickRectangle to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor
  from ..QtQml import QJSValue
  from . import QQuickPen, QQuickRectanglePrivate, QSGNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QJSValue = WAIT['QJSValue']
  QSGNode = WAIT['QSGNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickRectangle(QQuickItem):
  """
  The cute side of Qt's QQuickRectangle: a plain Python object standing in
  front of one C++ QQuickRectangle.

  It is built on the cute 'QQuickItem', as Qt's QQuickRectangle is built on
  Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickRectangle that has a ritual and that Python
  can call so far, 32 names in all: 'metaObject', 'tr', 'color', 'setColor',
  'resetColor', 'border', 'gradient', 'setGradient', 'resetGradient',
  'radius', 'setRadius', 'topLeftRadius', 'setTopLeftRadius',
  'resetTopLeftRadius', 'topRightRadius', 'setTopRightRadius',
  'resetTopRightRadius', 'bottomLeftRadius', 'setBottomLeftRadius',
  'resetBottomLeftRadius', 'bottomRightRadius', 'setBottomRightRadius',
  'resetBottomRightRadius', 'colorChanged', 'radiusChanged',
  'topLeftRadiusChanged', 'topRightRadiusChanged', 'bottomLeftRadiusChanged',
  'bottomRightRadiusChanged', 'updatePaintNode', 'doUpdate', 'd_func'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickRectangle::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickRectangle::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickRectanglePrivate *QQuickRectangle::d_func() const':
    takes in Python what 'QQuickRectanglePrivate *QQuickRectangle::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 40 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickRectangle is created at the first use, not by
    'QQuickRectangle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickRectangle.
  - Qt tells when it has removed the C++ QQuickRectangle. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickRectangle::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangle.html#tr

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
    #  QString QQuickRectangle::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQuickRectangle2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickRectangle'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickRectangle::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickRectangle::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuickRectangle10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickRectangle::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangle.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickRectangle::color() const
    address = self.uglySide.call('ritual_ZNK15QQuickRectangle5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def gradient(self) -> QJSValue:
    """
    Calls Qt's 'QJSValue QQuickRectangle::gradient() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangle.html#gradient

    Returns
    -------

    QJSValue
      A new cute QJSValue around the copy Qt gave back. Python owns it.
    """
    #  QJSValue QQuickRectangle::gradient() const
    address = self.uglySide.call('ritual_ZNK15QQuickRectangle8gradientEv')
    from ..QtQml import QJSValue
    return QJSValue._cuteOwning(address)

  def radius(self) -> float:
    """
    Calls Qt's 'qreal QQuickRectangle::radius() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangle.html#radius
    """
    #  qreal QQuickRectangle::radius() const
    return self.uglySide.call('ritual_ZNK15QQuickRectangle6radiusEv')

  def topLeftRadius(self) -> float:
    """
    Calls Qt's 'qreal QQuickRectangle::topLeftRadius() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangle.html#topLeftRadius
    """
    #  qreal QQuickRectangle::topLeftRadius() const
    return self.uglySide.call('ritual_ZNK15QQuickRectangle13topLeftRadiusEv')

  def topRightRadius(self) -> float:
    """
    Calls Qt's 'qreal QQuickRectangle::topRightRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangle.html#topRightRadius
    """
    #  qreal QQuickRectangle::topRightRadius() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickRectangle14topRightRadiusEv',
    )

  def bottomLeftRadius(self) -> float:
    """
    Calls Qt's 'qreal QQuickRectangle::bottomLeftRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangle.html#bottomLeftRadius
    """
    #  qreal QQuickRectangle::bottomLeftRadius() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickRectangle16bottomLeftRadiusEv',
    )

  def bottomRightRadius(self) -> float:
    """
    Calls Qt's 'qreal QQuickRectangle::bottomRightRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangle.html#bottomRightRadius
    """
    #  qreal QQuickRectangle::bottomRightRadius() const
    return self.uglySide.call(
        'ritual_ZNK15QQuickRectangle17bottomRightRadiusEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setColor(self, a0: QColor) -> None:
    """
    Calls Qt's 'void QQuickRectangle::setColor(const QColor &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangle.html#setColor

    Parameters
    ----------

    a0 : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickRectangle::setColor(const QColor &a0)
    self.uglySide.call(
        'ritual_ZN15QQuickRectangle8setColorERK6QColor', self._valueOf(a0),
    )

  @overload(QJSValue)
  def setGradient(self, gradient: QJSValue) -> None:
    """
    Calls Qt's 'void QQuickRectangle::setGradient(const QJSValue &gradient)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangle.html#setGradient

    Parameters
    ----------

    gradient : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.
    """
    #  void QQuickRectangle::setGradient(const QJSValue &gradient)
    self.uglySide.call(
        'ritual_ZN15QQuickRectangle11setGradientERK8QJSValue',
        self._valueOf(gradient),
    )

  @overload(float)
  def setRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QQuickRectangle::setRadius(qreal radius)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangle.html#setRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QQuickRectangle::setRadius(qreal radius)
    self.uglySide.call('ritual_ZN15QQuickRectangle9setRadiusEd', radius)

  @overload(float)
  def setTopLeftRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QQuickRectangle::setTopLeftRadius(qreal radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangle.html#setTopLeftRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QQuickRectangle::setTopLeftRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN15QQuickRectangle16setTopLeftRadiusEd', radius,
    )

  @overload(float)
  def setTopRightRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QQuickRectangle::setTopRightRadius(qreal radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangle.html#setTopRightRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QQuickRectangle::setTopRightRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN15QQuickRectangle17setTopRightRadiusEd', radius,
    )

  @overload(float)
  def setBottomLeftRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QQuickRectangle::setBottomLeftRadius(qreal radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangle.html#setBottomLeftRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QQuickRectangle::setBottomLeftRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN15QQuickRectangle19setBottomLeftRadiusEd', radius,
    )

  @overload(float)
  def setBottomRightRadius(self, radius: float) -> None:
    """
    Calls Qt's 'void QQuickRectangle::setBottomRightRadius(qreal radius)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangle.html#setBottomRightRadius

    Parameters
    ----------

    radius : float
      Passed on as it is.
    """
    #  void QQuickRectangle::setBottomRightRadius(qreal radius)
    self.uglySide.call(
        'ritual_ZN15QQuickRectangle20setBottomRightRadiusEd', radius,
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
    'QQuickRectangle::QQuickRectangle(QQuickItem *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangle.html#QQuickRectangle

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickRectangle::QQuickRectangle(QQuickItem *parent)
    self._noteCreation(QQuickRectangle, lambda: Rituals.call(
        'ritual_ZN15QQuickRectangleC1EP10QQuickItem',
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

  def resetColor(self) -> None:
    """
    Calls Qt's 'void QQuickRectangle::resetColor()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangle.html#resetColor
    """
    #  void QQuickRectangle::resetColor()
    self.uglySide.call('ritual_ZN15QQuickRectangle10resetColorEv')

  def border(self) -> Optional[QQuickPen]:
    """
    Calls Qt's 'QQuickPen *QQuickRectangle::border()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangle.html#border

    Returns
    -------

    Optional[QQuickPen]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPen *QQuickRectangle::border()
    address = self.uglySide.call('ritual_ZN15QQuickRectangle6borderEv')
    from . import QQuickPen
    return QQuickPen._cuteAt(address)

  def resetGradient(self) -> None:
    """
    Calls Qt's 'void QQuickRectangle::resetGradient()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangle.html#resetGradient
    """
    #  void QQuickRectangle::resetGradient()
    self.uglySide.call('ritual_ZN15QQuickRectangle13resetGradientEv')

  def resetTopLeftRadius(self) -> None:
    """
    Calls Qt's 'void QQuickRectangle::resetTopLeftRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangle.html#resetTopLeftRadius
    """
    #  void QQuickRectangle::resetTopLeftRadius()
    self.uglySide.call('ritual_ZN15QQuickRectangle18resetTopLeftRadiusEv')

  def resetTopRightRadius(self) -> None:
    """
    Calls Qt's 'void QQuickRectangle::resetTopRightRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangle.html#resetTopRightRadius
    """
    #  void QQuickRectangle::resetTopRightRadius()
    self.uglySide.call('ritual_ZN15QQuickRectangle19resetTopRightRadiusEv')

  def resetBottomLeftRadius(self) -> None:
    """
    Calls Qt's 'void QQuickRectangle::resetBottomLeftRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangle.html#resetBottomLeftRadius
    """
    #  void QQuickRectangle::resetBottomLeftRadius()
    self.uglySide.call('ritual_ZN15QQuickRectangle21resetBottomLeftRadiusEv')

  def resetBottomRightRadius(self) -> None:
    """
    Calls Qt's 'void QQuickRectangle::resetBottomRightRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangle.html#resetBottomRightRadius
    """
    #  void QQuickRectangle::resetBottomRightRadius()
    self.uglySide.call(
        'ritual_ZN15QQuickRectangle22resetBottomRightRadiusEv',
    )

  def colorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangle::colorChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangle.html#colorChanged
    """
    #  void QQuickRectangle::colorChanged()
    self.uglySide.call('ritual_ZN15QQuickRectangle12colorChangedEv')

  def radiusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangle::radiusChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangle.html#radiusChanged
    """
    #  void QQuickRectangle::radiusChanged()
    self.uglySide.call('ritual_ZN15QQuickRectangle13radiusChangedEv')

  def topLeftRadiusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangle::topLeftRadiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangle.html#topLeftRadiusChanged
    """
    #  void QQuickRectangle::topLeftRadiusChanged()
    self.uglySide.call('ritual_ZN15QQuickRectangle20topLeftRadiusChangedEv')

  def topRightRadiusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangle::topRightRadiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangle.html#topRightRadiusChanged
    """
    #  void QQuickRectangle::topRightRadiusChanged()
    self.uglySide.call('ritual_ZN15QQuickRectangle21topRightRadiusChangedEv')

  def bottomLeftRadiusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangle::bottomLeftRadiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangle.html#bottomLeftRadiusChanged
    """
    #  void QQuickRectangle::bottomLeftRadiusChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickRectangle23bottomLeftRadiusChangedEv',
    )

  def bottomRightRadiusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRectangle::bottomRightRadiusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangle.html#bottomRightRadiusChanged
    """
    #  void QQuickRectangle::bottomRightRadiusChanged()
    self.uglySide.call(
        'ritual_ZN15QQuickRectangle24bottomRightRadiusChangedEv',
    )

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      a0: Optional[QSGNode],
      a1: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QQuickRectangle::updatePaintNode(QSGNode *a0,
    UpdatePaintNodeData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrectangle.html#updatePaintNode

    Parameters
    ----------

    a0 : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QQuickRectangle::updatePaintNode(QSGNode *a0,
    #      UpdatePaintNodeData *a1)
    ritual = (
        'ritual_ZN15QQuickRectangle15updatePaintNodeEP7QSGNodePN10QQuickIte'
        'm19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickRectangle15updatePaintNodeEP7QSGNodePN10QQu'
          'ickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(a0, 'QSGNode'), self._addressOf(a1),
    )
    from . import QSGNode
    return QSGNode._cuteAt(address)

  def doUpdate(self) -> None:
    """
    Calls Qt's 'void QQuickRectangle::doUpdate()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangle.html#doUpdate
    """
    #  void QQuickRectangle::doUpdate()
    self.uglySide.call('ritual_ZN15QQuickRectangle8doUpdateEv')

  def d_func(self) -> Optional[QQuickRectanglePrivate]:
    """
    Calls Qt's 'QQuickRectanglePrivate *QQuickRectangle::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrectangle.html#d_func

    Returns
    -------

    Optional[QQuickRectanglePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickRectanglePrivate *QQuickRectangle::d_func()
    address = self.uglySide.call('ritual_ZN15QQuickRectangle6d_funcEv')
    from . import QQuickRectanglePrivate
    return QQuickRectanglePrivate._cuteAt(address)
