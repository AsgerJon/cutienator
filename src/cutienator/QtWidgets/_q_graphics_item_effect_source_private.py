"""
QGraphicsItemEffectSourcePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicsitem_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QGraphicsItemEffectSourcePrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import Qt
from . import QGraphicsEffect, QGraphicsEffectSourcePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint, QRect, QRectF
  from ..QtGui import QPainter, QPixmap
  from . import QGraphicsItem, QStyleOption, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QPoint = WAIT['QPoint']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsItemEffectSourcePrivate(QGraphicsEffectSourcePrivate):
  """
  The cute side of Qt's QGraphicsItemEffectSourcePrivate: a plain Python
  object standing in front of one C++ QGraphicsItemEffectSourcePrivate.

  It is built on the cute 'QGraphicsEffectSourcePrivate', as Qt's
  QGraphicsItemEffectSourcePrivate is built on Qt's
  QGraphicsEffectSourcePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsItemEffectSourcePrivate that has a ritual
  and that Python can call so far, 11 names in all: 'detach', 'graphicsItem',
  'widget', 'update', 'effectBoundingRectChanged', 'isPixmap', 'styleOption',
  'deviceRect', 'boundingRect', 'draw', 'pixmap'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRectF
    QGraphicsItemEffectSourcePrivate::paddedEffectRect(Qt::CoordinateSystem
    system, QGraphicsEffect::PixmapPadMode mode, const QRectF &sourceRect,
    bool *unpadded) const': takes a number to change where it is.

  What has no ritual
  ------------------

  1 of the 13 functions Qt declares: 1 leans on 'QGraphicsScenePrivate.

  What to expect
  --------------

  - The C++ QGraphicsItemEffectSourcePrivate is created at the first use, not
    by 'QGraphicsItemEffectSourcePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsItemEffectSourcePrivate.
  - Each name of Qt's QGraphicsItemEffectSourcePrivate that has no cute
    function yet, '__init__', 'paddedEffectRect', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsItemEffectSourcePrivate'

  #  A C++ QGraphicsItemEffectSourcePrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsItemEffectSourcePrivate'

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
    *QGraphicsItemEffectSourcePrivate::graphicsItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemeffectsourceprivate.html#graphicsItem

    Returns
    -------

    Optional[QGraphicsItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QGraphicsItem *QGraphicsItemEffectSourcePrivate::graphicsItem()
    #      const
    ritual = 'ritual_ZNK32QGraphicsItemEffectSourcePrivate12graphicsItemEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK32QGraphicsItemEffectSourcePrivate12graphicsItemEv')
    address = self.uglySide.call(ritual)
    from . import QGraphicsItem
    return QGraphicsItem._cuteAt(address)

  def widget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'const QWidget *QGraphicsItemEffectSourcePrivate::widget()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemeffectsourceprivate.html#widget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QWidget *QGraphicsItemEffectSourcePrivate::widget() const
    ritual = 'ritual_ZNK32QGraphicsItemEffectSourcePrivate6widgetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK32QGraphicsItemEffectSourcePrivate6widgetEv'
    address = self.uglySide.call(ritual)
    from . import QWidget
    return QWidget._cuteAt(address)

  def isPixmap(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsItemEffectSourcePrivate::isPixmap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemeffectsourceprivate.html#isPixmap
    """
    #  bool QGraphicsItemEffectSourcePrivate::isPixmap() const
    ritual = 'ritual_ZNK32QGraphicsItemEffectSourcePrivate8isPixmapEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK32QGraphicsItemEffectSourcePrivate8isPixmapEv'
    return self.uglySide.call(ritual)

  def styleOption(self) -> Optional[QStyleOption]:
    """
    Calls Qt's 'const QStyleOption
    *QGraphicsItemEffectSourcePrivate::styleOption() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemeffectsourceprivate.html#styleOption

    Returns
    -------

    Optional[QStyleOption]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QStyleOption *QGraphicsItemEffectSourcePrivate::styleOption()
    #      const
    ritual = 'ritual_ZNK32QGraphicsItemEffectSourcePrivate11styleOptionEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK32QGraphicsItemEffectSourcePrivate11styleOptionEv')
    address = self.uglySide.call(ritual)
    from . import QStyleOption
    return QStyleOption._cuteAt(address)

  def deviceRect(self) -> QRect:
    """
    Calls Qt's 'QRect QGraphicsItemEffectSourcePrivate::deviceRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemeffectsourceprivate.html#deviceRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QGraphicsItemEffectSourcePrivate::deviceRect() const
    ritual = 'ritual_ZNK32QGraphicsItemEffectSourcePrivate10deviceRectEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK32QGraphicsItemEffectSourcePrivate10deviceRectEv')
    address = self.uglySide.call(ritual)
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(Qt.CoordinateSystem)
  def boundingRect(self, system: Qt.CoordinateSystem) -> QRectF:
    """
    Calls Qt's 'QRectF
    QGraphicsItemEffectSourcePrivate::boundingRect(Qt::CoordinateSystem
    system) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemeffectsourceprivate.html#boundingRect

    Parameters
    ----------

    system : Qt.CoordinateSystem
      Passed on as its number.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsItemEffectSourcePrivate::boundingRect(Qt::
    #      CoordinateSystem system) const
    ritual = (
        'ritual_ZNK32QGraphicsItemEffectSourcePrivate12boundingRectEN2Qt16C'
        'oordinateSystemE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK32QGraphicsItemEffectSourcePrivate12boundingRectEN'
          '2Qt16CoordinateSystemE')
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
    QGraphicsItemEffectSourcePrivate::pixmap(Qt::CoordinateSystem system,
    QPoint *offset, QGraphicsEffect::PixmapPadMode mode) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemeffectsourceprivate.html#pixmap

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
    #  QPixmap QGraphicsItemEffectSourcePrivate::pixmap(Qt::CoordinateSystem
    #      system, QPoint *offset, QGraphicsEffect::PixmapPadMode mode) const
    address = self.uglySide.call(
        'ritual_ZNK32QGraphicsItemEffectSourcePrivate6pixmapEN2Qt16Coordina'
        'teSystemEP6QPointN15QGraphicsEffect13PixmapPadModeE',
        system.value, self._addressOf(offset), mode.value,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QGraphicsItemEffectSourcePrivate::QGraphicsItemEffectSourcePrivate(
    QGraphicsItem *i)': leans on 'QGraphicsScenePrivate::draw(QGraphicsItem*,
    QPainter*, QTransform const*, QTransform const*, QRegion*, QWidget*,
    double, QTransform const*, bool, bool)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGraphicsItemEffectSourcePrivate.__init__' has no cute function "
        "yet. Qt's "
        "'QGraphicsItemEffectSourcePrivate::QGraphicsItemEffectSourcePrivate"
        "(QGraphicsItem *i)': leans on "
        "'QGraphicsScenePrivate::draw(QGraphicsItem*, QPainter*, QTransform "
        "const*, QTransform const*, QRegion*, QWidget*, double, QTransform "
        "const*, bool, bool)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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
    Calls Qt's 'void QGraphicsItemEffectSourcePrivate::detach()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemeffectsourceprivate.html#detach
    """
    #  void QGraphicsItemEffectSourcePrivate::detach()
    ritual = 'ritual_ZN32QGraphicsItemEffectSourcePrivate6detachEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN32QGraphicsItemEffectSourcePrivate6detachEv'
    self.uglySide.call(ritual)

  def update(self) -> None:
    """
    Calls Qt's 'void QGraphicsItemEffectSourcePrivate::update()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemeffectsourceprivate.html#update
    """
    #  void QGraphicsItemEffectSourcePrivate::update()
    ritual = 'ritual_ZN32QGraphicsItemEffectSourcePrivate6updateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN32QGraphicsItemEffectSourcePrivate6updateEv'
    self.uglySide.call(ritual)

  def effectBoundingRectChanged(self) -> None:
    """
    Calls Qt's 'void
    QGraphicsItemEffectSourcePrivate::effectBoundingRectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemeffectsourceprivate.html
    """
    #  void QGraphicsItemEffectSourcePrivate::effectBoundingRectChanged()
    ritual = (
        'ritual_ZN32QGraphicsItemEffectSourcePrivate25effectBoundingRectCha'
        'ngedEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN32QGraphicsItemEffectSourcePrivate25effectBoundingR'
          'ectChangedEv')
    self.uglySide.call(ritual)

  @overload(QPainter)
  @overload(NoneType)
  def draw(self, a0: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QGraphicsItemEffectSourcePrivate::draw(QPainter *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemeffectsourceprivate.html#draw

    Parameters
    ----------

    a0 : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItemEffectSourcePrivate::draw(QPainter *a0)
    self.uglySide.call(
        'ritual_ZN32QGraphicsItemEffectSourcePrivate4drawEP8QPainter',
        self._addressOf(a0),
    )

  @staticmethod
  def paddedEffectRect(*__, **_) -> Never:
    """
    Qt's 'QRectF
    QGraphicsItemEffectSourcePrivate::paddedEffectRect(Qt::CoordinateSystem
    system, QGraphicsEffect::PixmapPadMode mode, const QRectF &sourceRect,
    bool *unpadded) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QGraphicsItemEffectSourcePrivate.paddedEffectRect' has no cute "
        "function yet. Qt's 'QRectF "
        "QGraphicsItemEffectSourcePrivate::paddedEffectRect(Qt::CoordinateSy"
        "stem system, QGraphicsEffect::PixmapPadMode mode, const QRectF "
        "&sourceRect, bool *unpadded) const': takes a number to change "
        "where it is.")
