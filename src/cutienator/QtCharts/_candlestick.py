"""
Candlestick binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/candlestick_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Candlestick to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtWidgets import QGraphicsObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF
  from ..QtGui import QBrush, QColor, QPainter, QPen
  from ..QtWidgets import QGraphicsSceneHoverEvent, QGraphicsSceneMouseEvent
  from ..QtWidgets import QStyleOptionGraphicsItem, QWidget
  from . import AbstractDomain, CandlestickData, QCandlestickSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  AbstractDomain = WAIT['AbstractDomain']
  CandlestickData = WAIT['CandlestickData']
  QBrush = WAIT['QBrush']
  QCandlestickSet = WAIT['QCandlestickSet']
  QColor = WAIT['QColor']
  QGraphicsSceneHoverEvent = WAIT['QGraphicsSceneHoverEvent']
  QGraphicsSceneMouseEvent = WAIT['QGraphicsSceneMouseEvent']
  QPainter = WAIT['QPainter']
  QPen = WAIT['QPen']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Candlestick(QGraphicsObject):
  """
  The cute side of Qt's Candlestick: a plain Python object standing in front
  of one C++ Candlestick.

  It is built on the cute 'QGraphicsObject', as Qt's Candlestick is built on
  Qt's QGraphicsObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Candlestick that has a ritual and that Python can
  call so far, 27 names in all: 'metaObject', 'tr', 'setTimePeriod',
  'setMaximumColumnWidth', 'setMinimumColumnWidth', 'setBodyWidth',
  'setBodyOutlineVisible', 'setCapsWidth', 'setCapsVisible',
  'setIncreasingColor', 'setDecreasingColor', 'setBrush', 'setPen',
  'setLayout', 'mousePressEvent', 'hoverEnterEvent', 'hoverLeaveEvent',
  'mouseReleaseEvent', 'mouseDoubleClickEvent', 'boundingRect', 'paint',
  'clicked', 'hovered', 'pressed', 'released', 'doubleClicked',
  'updateGeometry'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Candlestick::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int Candlestick::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'Candlestick::~Candlestick()': the destructor: Python never removes
    a C++ Candlestick.

  What has no ritual
  ------------------

  2 of the 33 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Candlestick is created at the first use, not by
    'Candlestick(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Candlestick.
  - Qt tells when it has removed the C++ Candlestick. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString Candlestick::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/candlestick.html#tr

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
    #  QString Candlestick::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11Candlestick2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Candlestick'

  #  A C++ Candlestick Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Candlestick'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Candlestick::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/candlestick.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Candlestick::metaObject() const
    address = self.uglySide.call('ritual_ZNK11Candlestick10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF Candlestick::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/candlestick.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF Candlestick::boundingRect() const
    ritual = 'ritual_ZNK11Candlestick12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11Candlestick12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setTimePeriod(self, timePeriod: float) -> None:
    """
    Calls Qt's 'void Candlestick::setTimePeriod(qreal timePeriod)'.

    Qt's own words: https://doc.qt.io/qt-6/candlestick.html#setTimePeriod

    Parameters
    ----------

    timePeriod : float
      Passed on as it is.
    """
    #  void Candlestick::setTimePeriod(qreal timePeriod)
    self.uglySide.call('ritual_ZN11Candlestick13setTimePeriodEd', timePeriod)

  @overload(float)
  def setMaximumColumnWidth(self, maximumColumnWidth: float) -> None:
    """
    Calls Qt's 'void Candlestick::setMaximumColumnWidth(qreal
    maximumColumnWidth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/candlestick.html#setMaximumColumnWidth

    Parameters
    ----------

    maximumColumnWidth : float
      Passed on as it is.
    """
    #  void Candlestick::setMaximumColumnWidth(qreal maximumColumnWidth)
    self.uglySide.call(
        'ritual_ZN11Candlestick21setMaximumColumnWidthEd',
        maximumColumnWidth,
    )

  @overload(float)
  def setMinimumColumnWidth(self, minimumColumnWidth: float) -> None:
    """
    Calls Qt's 'void Candlestick::setMinimumColumnWidth(qreal
    minimumColumnWidth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/candlestick.html#setMinimumColumnWidth

    Parameters
    ----------

    minimumColumnWidth : float
      Passed on as it is.
    """
    #  void Candlestick::setMinimumColumnWidth(qreal minimumColumnWidth)
    self.uglySide.call(
        'ritual_ZN11Candlestick21setMinimumColumnWidthEd',
        minimumColumnWidth,
    )

  @overload(float)
  def setBodyWidth(self, bodyWidth: float) -> None:
    """
    Calls Qt's 'void Candlestick::setBodyWidth(qreal bodyWidth)'.

    Qt's own words: https://doc.qt.io/qt-6/candlestick.html#setBodyWidth

    Parameters
    ----------

    bodyWidth : float
      Passed on as it is.
    """
    #  void Candlestick::setBodyWidth(qreal bodyWidth)
    self.uglySide.call('ritual_ZN11Candlestick12setBodyWidthEd', bodyWidth)

  @overload(bool)
  def setBodyOutlineVisible(self, bodyOutlineVisible: bool) -> None:
    """
    Calls Qt's 'void Candlestick::setBodyOutlineVisible(bool
    bodyOutlineVisible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/candlestick.html#setBodyOutlineVisible

    Parameters
    ----------

    bodyOutlineVisible : bool
      Passed on as it is.
    """
    #  void Candlestick::setBodyOutlineVisible(bool bodyOutlineVisible)
    self.uglySide.call(
        'ritual_ZN11Candlestick21setBodyOutlineVisibleEb',
        bodyOutlineVisible,
    )

  @overload(float)
  def setCapsWidth(self, capsWidth: float) -> None:
    """
    Calls Qt's 'void Candlestick::setCapsWidth(qreal capsWidth)'.

    Qt's own words: https://doc.qt.io/qt-6/candlestick.html#setCapsWidth

    Parameters
    ----------

    capsWidth : float
      Passed on as it is.
    """
    #  void Candlestick::setCapsWidth(qreal capsWidth)
    self.uglySide.call('ritual_ZN11Candlestick12setCapsWidthEd', capsWidth)

  @overload(bool)
  def setCapsVisible(self, capsVisible: bool) -> None:
    """
    Calls Qt's 'void Candlestick::setCapsVisible(bool capsVisible)'.

    Qt's own words: https://doc.qt.io/qt-6/candlestick.html#setCapsVisible

    Parameters
    ----------

    capsVisible : bool
      Passed on as it is.
    """
    #  void Candlestick::setCapsVisible(bool capsVisible)
    self.uglySide.call(
        'ritual_ZN11Candlestick14setCapsVisibleEb', capsVisible,
    )

  @overload(QColor)
  def setIncreasingColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void Candlestick::setIncreasingColor(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/candlestick.html#setIncreasingColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Candlestick::setIncreasingColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN11Candlestick18setIncreasingColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QColor)
  def setDecreasingColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void Candlestick::setDecreasingColor(const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/candlestick.html#setDecreasingColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void Candlestick::setDecreasingColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN11Candlestick18setDecreasingColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QBrush)
  def setBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void Candlestick::setBrush(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/candlestick.html#setBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void Candlestick::setBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN11Candlestick8setBrushERK6QBrush', self._valueOf(brush),
    )

  @overload(QPen)
  def setPen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void Candlestick::setPen(const QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/candlestick.html#setPen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void Candlestick::setPen(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN11Candlestick6setPenERK4QPen', self._valueOf(pen),
    )

  @overload(CandlestickData)
  def setLayout(self, data: CandlestickData) -> None:
    """
    Calls Qt's 'void Candlestick::setLayout(const CandlestickData &data)'.

    Qt's own words: https://doc.qt.io/qt-6/candlestick.html#setLayout

    Parameters
    ----------

    data : CandlestickData
      Passed on as a value: Qt reads the C++ CandlestickData, which stays
      Python's own.
    """
    #  void Candlestick::setLayout(const CandlestickData &data)
    self.uglySide.call(
        'ritual_ZN11Candlestick9setLayoutERK15CandlestickData',
        self._valueOf(data),
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

  @overload(QCandlestickSet, AbstractDomain, QGraphicsObject)
  @overload(QCandlestickSet, AbstractDomain, NoneType)
  @overload(QCandlestickSet, NoneType, QGraphicsObject)
  @overload(QCandlestickSet, NoneType, NoneType)
  @overload(NoneType, AbstractDomain, QGraphicsObject)
  @overload(NoneType, AbstractDomain, NoneType)
  @overload(NoneType, NoneType, QGraphicsObject)
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      set: Optional[QCandlestickSet],
      domain: Optional[AbstractDomain],
      parent: Optional[QGraphicsObject],
  ) -> None:
    """
    Notes what was given, for Qt's 'Candlestick::Candlestick(QCandlestickSet
    *set, AbstractDomain *domain, QGraphicsObject *parent)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/candlestick.html#Candlestick

    Parameters
    ----------

    set : Optional[QCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    domain : Optional[AbstractDomain]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QGraphicsObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  Candlestick::Candlestick(QCandlestickSet *set, AbstractDomain *domain,
    #      QGraphicsObject *parent)
    self._noteCreation(Candlestick, lambda: Rituals.call(
        'ritual_ZN11CandlestickC1EP15QCandlestickSetP14AbstractDomainP15QGr'
        'aphicsObject',
        self._addressOf(set), self._addressOf(domain),
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

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mousePressEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void Candlestick::mousePressEvent(QGraphicsSceneMouseEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/candlestick.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Candlestick::mousePressEvent(QGraphicsSceneMouseEvent *event)
    ritual = (
        'ritual_ZN11Candlestick15mousePressEventEP24QGraphicsSceneMouseEven'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11Candlestick15mousePressEventEP24QGraphicsSceneMou'
          'seEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverEnterEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void Candlestick::hoverEnterEvent(QGraphicsSceneHoverEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/candlestick.html#hoverEnterEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Candlestick::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
    ritual = (
        'ritual_ZN11Candlestick15hoverEnterEventEP24QGraphicsSceneHoverEven'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11Candlestick15hoverEnterEventEP24QGraphicsSceneHov'
          'erEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void Candlestick::hoverLeaveEvent(QGraphicsSceneHoverEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/candlestick.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Candlestick::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
    ritual = (
        'ritual_ZN11Candlestick15hoverLeaveEventEP24QGraphicsSceneHoverEven'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11Candlestick15hoverLeaveEventEP24QGraphicsSceneHov'
          'erEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void Candlestick::mouseReleaseEvent(QGraphicsSceneMouseEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/candlestick.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Candlestick::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
    ritual = (
        'ritual_ZN11Candlestick17mouseReleaseEventEP24QGraphicsSceneMouseEv'
        'ent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11Candlestick17mouseReleaseEventEP24QGraphicsSceneM'
          'ouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void
    Candlestick::mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/candlestick.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Candlestick::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
    #      *event)
    ritual = (
        'ritual_ZN11Candlestick21mouseDoubleClickEventEP24QGraphicsSceneMou'
        'seEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11Candlestick21mouseDoubleClickEventEP24QGraphicsSc'
          'eneMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QPainter, QStyleOptionGraphicsItem)
  @overload(QPainter, NoneType)
  @overload(NoneType, QStyleOptionGraphicsItem)
  @overload(NoneType, NoneType)
  @overload(QPainter, QStyleOptionGraphicsItem, QWidget)
  @overload(QPainter, QStyleOptionGraphicsItem, NoneType)
  @overload(QPainter, NoneType, QWidget)
  @overload(QPainter, NoneType, NoneType)
  @overload(NoneType, QStyleOptionGraphicsItem, QWidget)
  @overload(NoneType, QStyleOptionGraphicsItem, NoneType)
  @overload(NoneType, NoneType, QWidget)
  @overload(NoneType, NoneType, NoneType)
  def paint(
      self,
      painter: Optional[QPainter],
      option: Optional[QStyleOptionGraphicsItem],
      widget: Optional[QWidget] = None,
  ) -> None:
    """
    Calls Qt's 'void Candlestick::paint(QPainter *painter, const
    QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/candlestick.html#paint

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    option : Optional[QStyleOptionGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void Candlestick::paint(QPainter *painter, const
    #      QStyleOptionGraphicsItem *option, QWidget *widget)
    ritual = (
        'ritual_ZN11Candlestick5paintEP8QPainterPK24QStyleOptionGraphicsIte'
        'mP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11Candlestick5paintEP8QPainterPK24QStyleOptionGraph'
          'icsItemP7QWidget')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )

  @overload(QCandlestickSet)
  @overload(NoneType)
  def clicked(self, set: Optional[QCandlestickSet]) -> None:
    """
    Calls Qt's 'void Candlestick::clicked(QCandlestickSet *set)'.

    Qt's own words: https://doc.qt.io/qt-6/candlestick.html#clicked

    Parameters
    ----------

    set : Optional[QCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Candlestick::clicked(QCandlestickSet *set)
    self.uglySide.call(
        'ritual_ZN11Candlestick7clickedEP15QCandlestickSet',
        self._addressOf(set),
    )

  @overload(bool, QCandlestickSet)
  @overload(bool, NoneType)
  def hovered(self, status: bool, set: Optional[QCandlestickSet]) -> None:
    """
    Calls Qt's 'void Candlestick::hovered(bool status, QCandlestickSet
    *set)'.

    Qt's own words: https://doc.qt.io/qt-6/candlestick.html#hovered

    Parameters
    ----------

    status : bool
      Passed on as it is.

    set : Optional[QCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Candlestick::hovered(bool status, QCandlestickSet *set)
    self.uglySide.call(
        'ritual_ZN11Candlestick7hoveredEbP15QCandlestickSet',
        status, self._addressOf(set),
    )

  @overload(QCandlestickSet)
  @overload(NoneType)
  def pressed(self, set: Optional[QCandlestickSet]) -> None:
    """
    Calls Qt's 'void Candlestick::pressed(QCandlestickSet *set)'.

    Qt's own words: https://doc.qt.io/qt-6/candlestick.html#pressed

    Parameters
    ----------

    set : Optional[QCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Candlestick::pressed(QCandlestickSet *set)
    self.uglySide.call(
        'ritual_ZN11Candlestick7pressedEP15QCandlestickSet',
        self._addressOf(set),
    )

  @overload(QCandlestickSet)
  @overload(NoneType)
  def released(self, set: Optional[QCandlestickSet]) -> None:
    """
    Calls Qt's 'void Candlestick::released(QCandlestickSet *set)'.

    Qt's own words: https://doc.qt.io/qt-6/candlestick.html#released

    Parameters
    ----------

    set : Optional[QCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Candlestick::released(QCandlestickSet *set)
    self.uglySide.call(
        'ritual_ZN11Candlestick8releasedEP15QCandlestickSet',
        self._addressOf(set),
    )

  @overload(QCandlestickSet)
  @overload(NoneType)
  def doubleClicked(self, set: Optional[QCandlestickSet]) -> None:
    """
    Calls Qt's 'void Candlestick::doubleClicked(QCandlestickSet *set)'.

    Qt's own words: https://doc.qt.io/qt-6/candlestick.html#doubleClicked

    Parameters
    ----------

    set : Optional[QCandlestickSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Candlestick::doubleClicked(QCandlestickSet *set)
    self.uglySide.call(
        'ritual_ZN11Candlestick13doubleClickedEP15QCandlestickSet',
        self._addressOf(set),
    )

  @overload(AbstractDomain)
  @overload(NoneType)
  def updateGeometry(self, domain: Optional[AbstractDomain]) -> None:
    """
    Calls Qt's 'void Candlestick::updateGeometry(AbstractDomain *domain)'.

    Qt's own words: https://doc.qt.io/qt-6/candlestick.html#updateGeometry

    Parameters
    ----------

    domain : Optional[AbstractDomain]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Candlestick::updateGeometry(AbstractDomain *domain)
    self.uglySide.call(
        'ritual_ZN11Candlestick14updateGeometryEP14AbstractDomain',
        self._addressOf(domain),
    )
