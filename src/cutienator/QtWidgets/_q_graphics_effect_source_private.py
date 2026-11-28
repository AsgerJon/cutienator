"""
QGraphicsEffectSourcePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicseffect_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QGraphicsEffectSourcePrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObjectPrivate
from . import QGraphicsEffect

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPoint, QRect, QRectF
  from ..QtGui import QPainter, QPixmap
  from . import QGraphicsEffectSource, QGraphicsItem, QStyleOption, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPainter = WAIT['QPainter']
  QPoint = WAIT['QPoint']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsEffectSourcePrivate(QObjectPrivate):
  """
  The cute side of Qt's QGraphicsEffectSourcePrivate: a plain Python object
  standing in front of one C++ QGraphicsEffectSourcePrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QGraphicsEffectSourcePrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsEffectSourcePrivate that has a ritual and
  that Python can call so far, 16 names in all: 'q_func', 'detach',
  'boundingRect', 'deviceRect', 'graphicsItem', 'widget', 'styleOption',
  'draw', 'update', 'isPixmap', 'pixmap', 'effectBoundingRectChanged',
  'setCachedOffset', 'invalidateCache', 'currentCachedSystem',
  'currentCachedMode'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QGraphicsEffectSource *QGraphicsEffectSourcePrivate::q_func()
    const': takes in Python what 'QGraphicsEffectSource
    *QGraphicsEffectSourcePrivate::q_func()' takes.
  - Qt's 'QGraphicsEffectSourcePrivate::~QGraphicsEffectSourcePrivate()': the
    destructor: Python never removes a C++ QGraphicsEffectSourcePrivate.

  What to expect
  --------------

  - The C++ QGraphicsEffectSourcePrivate is created at the first use, not by
    'QGraphicsEffectSourcePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsEffectSourcePrivate.
  """

  #  The enums Qt writes inside QGraphicsEffectSourcePrivate, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class InvalidateReason(CuteNum):
    """
    The enum 'QGraphicsEffectSourcePrivate::InvalidateReason' of Qt, with the
    3 names Qt gives in it.
    """

    TransformChanged = Kee[int](0)
    EffectRectChanged = Kee[int](1)
    SourceChanged = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsEffectSourcePrivate'

  #  A C++ QGraphicsEffectSourcePrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsEffectSourcePrivate'

  #  The functions Qt calls itself that QGraphicsEffectSourcePrivate is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'detach': (
          ('_ZN28QGraphicsEffectSourcePrivate6detachEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'boundingRect': (
          ('_ZNK28QGraphicsEffectSourcePrivate12boundingRectEN2Qt16Coordina'
           'teSystemE',
           ('address', 'value', 'QtCore:QRectF'),
           (
               ('int', 'enum', 'QtCore:Qt.CoordinateSystem'),
           )),
      ),
      'deviceRect': (
          ('_ZNK28QGraphicsEffectSourcePrivate10deviceRectEv',
           ('address', 'value', 'QtCore:QRect'),
           ()),
      ),
      'graphicsItem': (
          ('_ZNK28QGraphicsEffectSourcePrivate12graphicsItemEv',
           ('address', 'address', 'QtWidgets:QGraphicsItem'),
           ()),
      ),
      'widget': (
          ('_ZNK28QGraphicsEffectSourcePrivate6widgetEv',
           ('address', 'address', 'QtWidgets:QWidget'),
           ()),
      ),
      'styleOption': (
          ('_ZNK28QGraphicsEffectSourcePrivate11styleOptionEv',
           ('address', 'address', 'QtWidgets:QStyleOption'),
           ()),
      ),
      'draw': (
          ('_ZN28QGraphicsEffectSourcePrivate4drawEP8QPainter',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainter'),
           )),
      ),
      'update': (
          ('_ZN28QGraphicsEffectSourcePrivate6updateEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'isPixmap': (
          ('_ZNK28QGraphicsEffectSourcePrivate8isPixmapEv',
           ('bool', 'number', ''),
           ()),
      ),
      'pixmap': (
          ('_ZNK28QGraphicsEffectSourcePrivate6pixmapEN2Qt16CoordinateSyste'
           'mEP6QPointN15QGraphicsEffect13PixmapPadModeE',
           ('address', 'value', 'QtGui:QPixmap'),
           (
               ('int', 'enum', 'QtCore:Qt.CoordinateSystem'),
               ('address', 'address', 'QtCore:QPoint'),
               ('int', 'enum', 'QtWidgets:QGraphicsEffect.PixmapPadMode'),
           )),
      ),
      'effectBoundingRectChanged': (
          ('_ZN28QGraphicsEffectSourcePrivate25effectBoundingRectChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.CoordinateSystem)
  def boundingRect(self, system: Qt.CoordinateSystem) -> QRectF:
    """
    Calls Qt's 'QRectF
    QGraphicsEffectSourcePrivate::boundingRect(Qt::CoordinateSystem system)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicseffectsourceprivate.html#boundingRect

    Parameters
    ----------

    system : Qt.CoordinateSystem
      Passed on as its number.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsEffectSourcePrivate::boundingRect(Qt::CoordinateSystem
    #      system) const
    address = self.uglySide.call(
        'ritual_ZNK28QGraphicsEffectSourcePrivate12boundingRectEN2Qt16Coord'
        'inateSystemE',
        system.value,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def deviceRect(self) -> QRect:
    """
    Calls Qt's 'QRect QGraphicsEffectSourcePrivate::deviceRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicseffectsourceprivate.html#deviceRect

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QGraphicsEffectSourcePrivate::deviceRect() const
    address = self.uglySide.call(
        'ritual_ZNK28QGraphicsEffectSourcePrivate10deviceRectEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def graphicsItem(self) -> Optional[QGraphicsItem]:
    """
    Calls Qt's 'const QGraphicsItem
    *QGraphicsEffectSourcePrivate::graphicsItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicseffectsourceprivate.html#graphicsItem

    Returns
    -------

    Optional[QGraphicsItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QGraphicsItem *QGraphicsEffectSourcePrivate::graphicsItem()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK28QGraphicsEffectSourcePrivate12graphicsItemEv',
    )
    from . import QGraphicsItem
    return QGraphicsItem._cuteAt(address)

  def widget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'const QWidget *QGraphicsEffectSourcePrivate::widget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicseffectsourceprivate.html#widget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QWidget *QGraphicsEffectSourcePrivate::widget() const
    address = self.uglySide.call(
        'ritual_ZNK28QGraphicsEffectSourcePrivate6widgetEv',
    )
    from . import QWidget
    return QWidget._cuteAt(address)

  def styleOption(self) -> Optional[QStyleOption]:
    """
    Calls Qt's 'const QStyleOption
    *QGraphicsEffectSourcePrivate::styleOption() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicseffectsourceprivate.html#styleOption

    Returns
    -------

    Optional[QStyleOption]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QStyleOption *QGraphicsEffectSourcePrivate::styleOption() const
    address = self.uglySide.call(
        'ritual_ZNK28QGraphicsEffectSourcePrivate11styleOptionEv',
    )
    from . import QStyleOption
    return QStyleOption._cuteAt(address)

  def isPixmap(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsEffectSourcePrivate::isPixmap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicseffectsourceprivate.html#isPixmap
    """
    #  bool QGraphicsEffectSourcePrivate::isPixmap() const
    return self.uglySide.call(
        'ritual_ZNK28QGraphicsEffectSourcePrivate8isPixmapEv',
    )

  @overload(Qt.CoordinateSystem)
  @overload(Qt.CoordinateSystem, QPoint)
  @overload(Qt.CoordinateSystem, NoneType)
  @overload(Qt.CoordinateSystem, QPoint, QGraphicsEffect.PixmapPadMode)
  @overload(Qt.CoordinateSystem, NoneType, QGraphicsEffect.PixmapPadMode)
  def pixmap(
      self,
      system: Qt.CoordinateSystem,
      offset: Optional[QPoint] = None,
      mode: QGraphicsEffect.PixmapPadMode = (
          QGraphicsEffect.PixmapPadMode.PadToTransparentBorder),
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap
    QGraphicsEffectSourcePrivate::pixmap(Qt::CoordinateSystem system, QPoint
    *offset, QGraphicsEffect::PixmapPadMode mode) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicseffectsourceprivate.html#pixmap

    Parameters
    ----------

    system : Qt.CoordinateSystem
      Passed on as its number.

    offset : Optional[QPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    mode : QGraphicsEffect.PixmapPadMode
      Passed on as its number. May be left out, as in Qt: it is then
      QGraphicsEffect.PixmapPadMode.PadToTransparentBorder.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QGraphicsEffectSourcePrivate::pixmap(Qt::CoordinateSystem
    #      system, QPoint *offset, QGraphicsEffect::PixmapPadMode mode) const
    address = self.uglySide.call(
        'ritual_ZNK28QGraphicsEffectSourcePrivate6pixmapEN2Qt16CoordinateSy'
        'stemEP6QPointN15QGraphicsEffect13PixmapPadModeE',
        system.value, self._addressOf(offset), mode.value,
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  def currentCachedSystem(self) -> Qt.CoordinateSystem:
    """
    Calls Qt's 'Qt::CoordinateSystem
    QGraphicsEffectSourcePrivate::currentCachedSystem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicseffectsourceprivate.html

    Returns
    -------

    Qt.CoordinateSystem
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.CoordinateSystem(number)' gives.
    """
    #  Qt::CoordinateSystem
    #      QGraphicsEffectSourcePrivate::currentCachedSystem() const
    return Qt.CoordinateSystem(self.uglySide.call(
        'ritual_ZNK28QGraphicsEffectSourcePrivate19currentCachedSystemEv',
    ))

  def currentCachedMode(self) -> QGraphicsEffect.PixmapPadMode:
    """
    Calls Qt's 'QGraphicsEffect::PixmapPadMode
    QGraphicsEffectSourcePrivate::currentCachedMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicseffectsourceprivate.html

    Returns
    -------

    QGraphicsEffect.PixmapPadMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QGraphicsEffect.PixmapPadMode(number)' gives.
    """
    #  QGraphicsEffect::PixmapPadMode
    #      QGraphicsEffectSourcePrivate::currentCachedMode() const
    return QGraphicsEffect.PixmapPadMode(self.uglySide.call(
        'ritual_ZNK28QGraphicsEffectSourcePrivate17currentCachedModeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPoint)
  def setCachedOffset(self, offset: QPoint) -> None:
    """
    Calls Qt's 'void QGraphicsEffectSourcePrivate::setCachedOffset(const
    QPoint &offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicseffectsourceprivate.html#setCachedOffset

    Parameters
    ----------

    offset : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QGraphicsEffectSourcePrivate::setCachedOffset(const QPoint
    #      &offset)
    self.uglySide.call(
        'ritual_ZN28QGraphicsEffectSourcePrivate15setCachedOffsetERK6QPoint',
        self._valueOf(offset),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QGraphicsEffectSourcePrivate::QGraphicsEffectSourcePrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicseffectsourceprivate.html
    """
    #  QGraphicsEffectSourcePrivate::QGraphicsEffectSourcePrivate()
    self._noteCreation(QGraphicsEffectSourcePrivate, lambda: Rituals.call(
        'ritual_ZN28QGraphicsEffectSourcePrivateC1Ev',
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

  def q_func(self) -> Optional[QGraphicsEffectSource]:
    """
    Calls Qt's 'QGraphicsEffectSource
    *QGraphicsEffectSourcePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicseffectsourceprivate.html#q_func

    Returns
    -------

    Optional[QGraphicsEffectSource]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsEffectSource *QGraphicsEffectSourcePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN28QGraphicsEffectSourcePrivate6q_funcEv',
    )
    from . import QGraphicsEffectSource
    return QGraphicsEffectSource._cuteAt(address)

  def detach(self) -> None:
    """
    Calls Qt's 'void QGraphicsEffectSourcePrivate::detach()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicseffectsourceprivate.html#detach
    """
    #  void QGraphicsEffectSourcePrivate::detach()
    self.uglySide.call('ritual_ZN28QGraphicsEffectSourcePrivate6detachEv')

  @overload(QPainter)
  @overload(NoneType)
  def draw(self, p: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QGraphicsEffectSourcePrivate::draw(QPainter *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicseffectsourceprivate.html#draw

    Parameters
    ----------

    p : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsEffectSourcePrivate::draw(QPainter *p)
    self.uglySide.call(
        'ritual_ZN28QGraphicsEffectSourcePrivate4drawEP8QPainter',
        self._addressOf(p),
    )

  def update(self) -> None:
    """
    Calls Qt's 'void QGraphicsEffectSourcePrivate::update()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicseffectsourceprivate.html#update
    """
    #  void QGraphicsEffectSourcePrivate::update()
    self.uglySide.call('ritual_ZN28QGraphicsEffectSourcePrivate6updateEv')

  def effectBoundingRectChanged(self) -> None:
    """
    Calls Qt's 'void
    QGraphicsEffectSourcePrivate::effectBoundingRectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicseffectsourceprivate.html
    """
    #  void QGraphicsEffectSourcePrivate::effectBoundingRectChanged()
    self.uglySide.call(
        'ritual_ZN28QGraphicsEffectSourcePrivate25effectBoundingRectChanged'
        'Ev',
    )

  @overload()
  @overload(InvalidateReason)
  def invalidateCache(
      self,
      reason: InvalidateReason = InvalidateReason.SourceChanged,
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsEffectSourcePrivate::invalidateCache(InvalidateReason reason)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicseffectsourceprivate.html#invalidateCache

    Parameters
    ----------

    reason : InvalidateReason
      Passed on as its number. May be left out, as in Qt: it is then
      InvalidateReason.SourceChanged.
    """
    #  void QGraphicsEffectSourcePrivate::invalidateCache(InvalidateReason
    #      reason) const
    self.uglySide.call(
        'ritual_ZNK28QGraphicsEffectSourcePrivate15invalidateCacheENS_16Inv'
        'alidateReasonE',
        reason.value,
    )
