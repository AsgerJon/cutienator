"""
QWidgetEffectSourcePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QWidgetEffectSourcePrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QGraphicsEffect, QGraphicsEffectSourcePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPoint, QRect, QRectF
  from ..QtGui import QPainter, QPixmap
  from . import QGraphicsItem, QStyleOption, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QPoint = WAIT['QPoint']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWidgetEffectSourcePrivate(QGraphicsEffectSourcePrivate):
  """
  The cute side of Qt's QWidgetEffectSourcePrivate: a plain Python object
  standing in front of one C++ QWidgetEffectSourcePrivate.

  It is built on the cute 'QGraphicsEffectSourcePrivate', as Qt's
  QWidgetEffectSourcePrivate is built on Qt's QGraphicsEffectSourcePrivate,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWidgetEffectSourcePrivate that has a ritual and
  that Python can call so far, 11 names in all: 'detach', 'graphicsItem',
  'widget', 'update', 'isPixmap', 'effectBoundingRectChanged', 'styleOption',
  'deviceRect', 'boundingRect', 'draw', 'pixmap'. It can be made from Python,
  in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QWidgetEffectSourcePrivate is created at the first use, not by
    'QWidgetEffectSourcePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWidgetEffectSourcePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWidgetEffectSourcePrivate'

  #  A C++ QWidgetEffectSourcePrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWidgetEffectSourcePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def graphicsItem(self) -> Optional[QGraphicsItem]:
    """
    Calls Qt's 'const QGraphicsItem
    *QWidgetEffectSourcePrivate::graphicsItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgeteffectsourceprivate.html#graphicsItem

    Returns
    -------

    Optional[QGraphicsItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QGraphicsItem *QWidgetEffectSourcePrivate::graphicsItem() const
    ritual = 'ritual_ZNK26QWidgetEffectSourcePrivate12graphicsItemEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QWidgetEffectSourcePrivate12graphicsItemEv'
    address = self.uglySide.call(ritual)
    from . import QGraphicsItem
    return QGraphicsItem._cuteAt(address)

  def widget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'const QWidget *QWidgetEffectSourcePrivate::widget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgeteffectsourceprivate.html#widget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QWidget *QWidgetEffectSourcePrivate::widget() const
    ritual = 'ritual_ZNK26QWidgetEffectSourcePrivate6widgetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QWidgetEffectSourcePrivate6widgetEv'
    address = self.uglySide.call(ritual)
    from . import QWidget
    return QWidget._cuteAt(address)

  def isPixmap(self) -> bool:
    """
    Calls Qt's 'bool QWidgetEffectSourcePrivate::isPixmap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgeteffectsourceprivate.html#isPixmap
    """
    #  bool QWidgetEffectSourcePrivate::isPixmap() const
    ritual = 'ritual_ZNK26QWidgetEffectSourcePrivate8isPixmapEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QWidgetEffectSourcePrivate8isPixmapEv'
    return self.uglySide.call(ritual)

  def styleOption(self) -> Optional[QStyleOption]:
    """
    Calls Qt's 'const QStyleOption *QWidgetEffectSourcePrivate::styleOption()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgeteffectsourceprivate.html#styleOption

    Returns
    -------

    Optional[QStyleOption]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QStyleOption *QWidgetEffectSourcePrivate::styleOption() const
    ritual = 'ritual_ZNK26QWidgetEffectSourcePrivate11styleOptionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QWidgetEffectSourcePrivate11styleOptionEv'
    address = self.uglySide.call(ritual)
    from . import QStyleOption
    return QStyleOption._cuteAt(address)

  def deviceRect(self) -> QRect:
    """
    Calls Qt's 'QRect QWidgetEffectSourcePrivate::deviceRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgeteffectsourceprivate.html#deviceRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWidgetEffectSourcePrivate::deviceRect() const
    ritual = 'ritual_ZNK26QWidgetEffectSourcePrivate10deviceRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QWidgetEffectSourcePrivate10deviceRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(Qt.CoordinateSystem)
  def boundingRect(self, system: Qt.CoordinateSystem) -> QRectF:
    """
    Calls Qt's 'QRectF
    QWidgetEffectSourcePrivate::boundingRect(Qt::CoordinateSystem system)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgeteffectsourceprivate.html#boundingRect

    Parameters
    ----------

    system : Qt.CoordinateSystem
      Passed on as its number.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QWidgetEffectSourcePrivate::boundingRect(Qt::CoordinateSystem
    #      system) const
    ritual = (
        'ritual_ZNK26QWidgetEffectSourcePrivate12boundingRectEN2Qt16Coordin'
        'ateSystemE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK26QWidgetEffectSourcePrivate12boundingRectEN2Qt16C'
          'oordinateSystemE')
    address = self.uglySide.call(ritual, system.value)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(Qt.CoordinateSystem, QPoint, QGraphicsEffect.PixmapPadMode)
  @overload(Qt.CoordinateSystem, NoneType, QGraphicsEffect.PixmapPadMode)
  def pixmap(
      self,
      system: Qt.CoordinateSystem,
      offset: Optional[QPoint],
      mode: QGraphicsEffect.PixmapPadMode,
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap
    QWidgetEffectSourcePrivate::pixmap(Qt::CoordinateSystem system, QPoint
    *offset, QGraphicsEffect::PixmapPadMode mode) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgeteffectsourceprivate.html#pixmap

    Parameters
    ----------

    system : Qt.CoordinateSystem
      Passed on as its number.

    offset : Optional[QPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mode : QGraphicsEffect.PixmapPadMode
      Passed on as its number.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QWidgetEffectSourcePrivate::pixmap(Qt::CoordinateSystem
    #      system, QPoint *offset, QGraphicsEffect::PixmapPadMode mode) const
    ritual = (
        'ritual_ZNK26QWidgetEffectSourcePrivate6pixmapEN2Qt16CoordinateSyst'
        'emEP6QPointN15QGraphicsEffect13PixmapPadModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK26QWidgetEffectSourcePrivate6pixmapEN2Qt16Coordina'
          'teSystemEP6QPointN15QGraphicsEffect13PixmapPadModeE')
    address = self.uglySide.call(
        ritual, system.value, self._addressOf(offset), mode.value,
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, widget: Optional[QWidget]) -> None:
    """
    Notes what was given, for Qt's
    'QWidgetEffectSourcePrivate::QWidgetEffectSourcePrivate(QWidget
    *widget)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgeteffectsourceprivate.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWidgetEffectSourcePrivate::QWidgetEffectSourcePrivate(QWidget
    #      *widget)
    self._noteCreation(QWidgetEffectSourcePrivate, lambda: Rituals.call(
        'ritual_ZN26QWidgetEffectSourcePrivateC1EP7QWidget',
        self._addressOf(widget),
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

  def detach(self) -> None:
    """
    Calls Qt's 'void QWidgetEffectSourcePrivate::detach()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgeteffectsourceprivate.html#detach
    """
    #  void QWidgetEffectSourcePrivate::detach()
    ritual = 'ritual_ZN26QWidgetEffectSourcePrivate6detachEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QWidgetEffectSourcePrivate6detachEv'
    self.uglySide.call(ritual)

  def update(self) -> None:
    """
    Calls Qt's 'void QWidgetEffectSourcePrivate::update()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgeteffectsourceprivate.html#update
    """
    #  void QWidgetEffectSourcePrivate::update()
    ritual = 'ritual_ZN26QWidgetEffectSourcePrivate6updateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QWidgetEffectSourcePrivate6updateEv'
    self.uglySide.call(ritual)

  def effectBoundingRectChanged(self) -> None:
    """
    Calls Qt's 'void
    QWidgetEffectSourcePrivate::effectBoundingRectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgeteffectsourceprivate.html
    """
    #  void QWidgetEffectSourcePrivate::effectBoundingRectChanged()
    ritual = (
        'ritual_ZN26QWidgetEffectSourcePrivate25effectBoundingRectChangedEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QWidgetEffectSourcePrivate25effectBoundingRectCha'
          'ngedEv')
    self.uglySide.call(ritual)

  @overload(QPainter)
  @overload(NoneType)
  def draw(self, p: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QWidgetEffectSourcePrivate::draw(QPainter *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgeteffectsourceprivate.html#draw

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetEffectSourcePrivate::draw(QPainter *p)
    ritual = 'ritual_ZN26QWidgetEffectSourcePrivate4drawEP8QPainter'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QWidgetEffectSourcePrivate4drawEP8QPainter'
    self.uglySide.call(ritual, self._addressOf(p))
