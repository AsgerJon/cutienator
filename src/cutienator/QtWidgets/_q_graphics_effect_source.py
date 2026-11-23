"""
QGraphicsEffectSource binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicseffect_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QGraphicsEffectSource to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QGraphicsEffect

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPoint, QRectF
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


class QGraphicsEffectSource(QObject):
  """
  The cute side of Qt's QGraphicsEffectSource: a plain Python object standing
  in front of one C++ QGraphicsEffectSource.

  It is built on the cute 'QObject', as Qt's QGraphicsEffectSource is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGraphicsEffectSource that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'tr',
  'graphicsItem', 'widget', 'styleOption', 'isPixmap', 'draw', 'update',
  'boundingRect', 'pixmap'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGraphicsEffectSource::~QGraphicsEffectSource()': the destructor:
    Python never removes a C++ QGraphicsEffectSource.

  What has no ritual
  ------------------

  12 of the 23 functions Qt declares: 5 takes or gives a type that cannot be
  passed yet; 4 forbidden; 2 declared and nowhere to be found; 1 a template.

  What to expect
  --------------

  - The C++ QGraphicsEffectSource is created at the first use, not by
    'QGraphicsEffectSource(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGraphicsEffectSource.
  - Qt tells when it has removed the C++ QGraphicsEffectSource. Every call on
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
    Calls Qt's 'QString QGraphicsEffectSource::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicseffectsource.html#tr

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
    #  QString QGraphicsEffectSource::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QGraphicsEffectSource2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsEffectSource'

  #  A C++ QGraphicsEffectSource Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsEffectSource'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGraphicsEffectSource::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicseffectsource.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGraphicsEffectSource::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QGraphicsEffectSource10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def graphicsItem(self) -> Optional[QGraphicsItem]:
    """
    Calls Qt's 'const QGraphicsItem *QGraphicsEffectSource::graphicsItem()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicseffectsource.html#graphicsItem

    Returns
    -------

    Optional[QGraphicsItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QGraphicsItem *QGraphicsEffectSource::graphicsItem() const
    address = self.uglySide.call(
        'ritual_ZNK21QGraphicsEffectSource12graphicsItemEv',
    )
    from . import QGraphicsItem
    return QGraphicsItem._cuteAt(address)

  def widget(self) -> Optional[QWidget]:
    """
    Calls Qt's 'const QWidget *QGraphicsEffectSource::widget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicseffectsource.html#widget

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QWidget *QGraphicsEffectSource::widget() const
    address = self.uglySide.call(
        'ritual_ZNK21QGraphicsEffectSource6widgetEv',
    )
    from . import QWidget
    return QWidget._cuteAt(address)

  def styleOption(self) -> Optional[QStyleOption]:
    """
    Calls Qt's 'const QStyleOption *QGraphicsEffectSource::styleOption()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicseffectsource.html#styleOption

    Returns
    -------

    Optional[QStyleOption]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QStyleOption *QGraphicsEffectSource::styleOption() const
    address = self.uglySide.call(
        'ritual_ZNK21QGraphicsEffectSource11styleOptionEv',
    )
    from . import QStyleOption
    return QStyleOption._cuteAt(address)

  def isPixmap(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsEffectSource::isPixmap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicseffectsource.html#isPixmap
    """
    #  bool QGraphicsEffectSource::isPixmap() const
    return self.uglySide.call('ritual_ZNK21QGraphicsEffectSource8isPixmapEv')

  @overload()
  @overload(Qt.CoordinateSystem)
  def boundingRect(
      self,
      coordinateSystem: Qt.CoordinateSystem = (
          Qt.CoordinateSystem.LogicalCoordinates),
  ) -> QRectF:
    """
    Calls Qt's 'QRectF
    QGraphicsEffectSource::boundingRect(Qt::CoordinateSystem
    coordinateSystem) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicseffectsource.html#boundingRect

    Parameters
    ----------

    coordinateSystem : Qt.CoordinateSystem
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CoordinateSystem.LogicalCoordinates.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsEffectSource::boundingRect(Qt::CoordinateSystem
    #      coordinateSystem) const
    address = self.uglySide.call(
        'ritual_ZNK21QGraphicsEffectSource12boundingRectEN2Qt16CoordinateSy'
        'stemE',
        coordinateSystem.value,
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload()
  @overload(Qt.CoordinateSystem)
  @overload(Qt.CoordinateSystem, QPoint)
  @overload(Qt.CoordinateSystem, NoneType)
  @overload(Qt.CoordinateSystem, QPoint, QGraphicsEffect.PixmapPadMode)
  @overload(Qt.CoordinateSystem, NoneType, QGraphicsEffect.PixmapPadMode)
  def pixmap(
      self,
      system: Qt.CoordinateSystem = Qt.CoordinateSystem.LogicalCoordinates,
      offset: Optional[QPoint] = None,
      mode: QGraphicsEffect.PixmapPadMode = (
          QGraphicsEffect.PixmapPadMode.PadToEffectiveBoundingRect),
  ) -> QPixmap:
    """
    Calls Qt's 'QPixmap QGraphicsEffectSource::pixmap(Qt::CoordinateSystem
    system, QPoint *offset, QGraphicsEffect::PixmapPadMode mode) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicseffectsource.html#pixmap

    Parameters
    ----------

    system : Qt.CoordinateSystem
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.CoordinateSystem.LogicalCoordinates.

    offset : Optional[QPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    mode : QGraphicsEffect.PixmapPadMode
      Passed on as its number. May be left out, as in Qt: it is then
      QGraphicsEffect.PixmapPadMode.PadToEffectiveBoundingRect.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QGraphicsEffectSource::pixmap(Qt::CoordinateSystem system,
    #      QPoint *offset, QGraphicsEffect::PixmapPadMode mode) const
    address = self.uglySide.call(
        'ritual_ZNK21QGraphicsEffectSource6pixmapEN2Qt16CoordinateSystemEP6'
        'QPointN15QGraphicsEffect13PixmapPadModeE',
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

  @overload(QPainter)
  @overload(NoneType)
  def draw(self, painter: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QGraphicsEffectSource::draw(QPainter *painter)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicseffectsource.html#draw

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsEffectSource::draw(QPainter *painter)
    self.uglySide.call(
        'ritual_ZN21QGraphicsEffectSource4drawEP8QPainter',
        self._addressOf(painter),
    )

  def update(self) -> None:
    """
    Calls Qt's 'void QGraphicsEffectSource::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicseffectsource.html#update
    """
    #  void QGraphicsEffectSource::update()
    self.uglySide.call('ritual_ZN21QGraphicsEffectSource6updateEv')
