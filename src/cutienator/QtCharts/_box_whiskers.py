"""
BoxWhiskers binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/boxwhiskers_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means BoxWhiskers to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtWidgets import QGraphicsObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF, QSizeF
  from ..QtGui import QBrush, QPainter, QPen
  from ..QtWidgets import QGraphicsSceneHoverEvent, QGraphicsSceneMouseEvent
  from ..QtWidgets import QStyleOptionGraphicsItem, QWidget
  from . import AbstractDomain, BoxWhiskersData, QBoxSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  AbstractDomain = WAIT['AbstractDomain']
  BoxWhiskersData = WAIT['BoxWhiskersData']
  QBoxSet = WAIT['QBoxSet']
  QBrush = WAIT['QBrush']
  QGraphicsSceneHoverEvent = WAIT['QGraphicsSceneHoverEvent']
  QGraphicsSceneMouseEvent = WAIT['QGraphicsSceneMouseEvent']
  QPainter = WAIT['QPainter']
  QPen = WAIT['QPen']
  QRectF = WAIT['QRectF']
  QSizeF = WAIT['QSizeF']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class BoxWhiskers(QGraphicsObject):
  """
  The cute side of Qt's BoxWhiskers: a plain Python object standing in front
  of one C++ BoxWhiskers.

  It is built on the cute 'QGraphicsObject', as Qt's BoxWhiskers is built on
  Qt's QGraphicsObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's BoxWhiskers that has a ritual and that Python can
  call so far, 22 names in all: 'metaObject', 'tr', 'setBrush', 'setPen',
  'setLayout', 'setBoxOutlined', 'setBoxWidth', 'mousePressEvent',
  'hoverEnterEvent', 'hoverLeaveEvent', 'mouseReleaseEvent',
  'mouseDoubleClickEvent', 'boundingRect', 'paint', 'updateGeometry',
  'sizeHint', 'setGeometry', 'clicked', 'hovered', 'pressed', 'released',
  'doubleClicked'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *BoxWhiskers::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int BoxWhiskers::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'BoxWhiskers::~BoxWhiskers()': the destructor: Python never removes
    a C++ BoxWhiskers.

  What has no ritual
  ------------------

  2 of the 28 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ BoxWhiskers is created at the first use, not by
    'BoxWhiskers(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ BoxWhiskers.
  - Qt tells when it has removed the C++ BoxWhiskers. Every call on the cute
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
    Calls Qt's 'QString BoxWhiskers::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/boxwhiskers.html#tr

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
    #  QString BoxWhiskers::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11BoxWhiskers2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'BoxWhiskers'

  #  A C++ BoxWhiskers Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_BoxWhiskers'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *BoxWhiskers::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/boxwhiskers.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *BoxWhiskers::metaObject() const
    address = self.uglySide.call('ritual_ZNK11BoxWhiskers10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF BoxWhiskers::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/boxwhiskers.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF BoxWhiskers::boundingRect() const
    ritual = 'ritual_ZNK11BoxWhiskers12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11BoxWhiskers12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(Qt.SizeHint, QSizeF)
  def sizeHint(self, which: Qt.SizeHint, constraint: QSizeF) -> QSizeF:
    """
    Calls Qt's 'QSizeF BoxWhiskers::sizeHint(Qt::SizeHint which, const QSizeF
    &constraint) const'.

    Qt's own words: https://doc.qt.io/qt-6/boxwhiskers.html#sizeHint

    Parameters
    ----------

    which : Qt.SizeHint
      Passed on as its number.

    constraint : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF BoxWhiskers::sizeHint(Qt::SizeHint which, const QSizeF
    #      &constraint) const
    address = self.uglySide.call(
        'ritual_ZNK11BoxWhiskers8sizeHintEN2Qt8SizeHintERK6QSizeF',
        which.value, self._valueOf(constraint),
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QBrush)
  def setBrush(self, brush: QBrush) -> None:
    """
    Calls Qt's 'void BoxWhiskers::setBrush(const QBrush &brush)'.

    Qt's own words: https://doc.qt.io/qt-6/boxwhiskers.html#setBrush

    Parameters
    ----------

    brush : QBrush
      Passed on as a value: Qt reads the C++ QBrush, which stays Python's
      own.
    """
    #  void BoxWhiskers::setBrush(const QBrush &brush)
    self.uglySide.call(
        'ritual_ZN11BoxWhiskers8setBrushERK6QBrush', self._valueOf(brush),
    )

  @overload(QPen)
  def setPen(self, pen: QPen) -> None:
    """
    Calls Qt's 'void BoxWhiskers::setPen(const QPen &pen)'.

    Qt's own words: https://doc.qt.io/qt-6/boxwhiskers.html#setPen

    Parameters
    ----------

    pen : QPen
      Passed on as a value: Qt reads the C++ QPen, which stays Python's own.
    """
    #  void BoxWhiskers::setPen(const QPen &pen)
    self.uglySide.call(
        'ritual_ZN11BoxWhiskers6setPenERK4QPen', self._valueOf(pen),
    )

  @overload(BoxWhiskersData)
  def setLayout(self, data: BoxWhiskersData) -> None:
    """
    Calls Qt's 'void BoxWhiskers::setLayout(const BoxWhiskersData &data)'.

    Qt's own words: https://doc.qt.io/qt-6/boxwhiskers.html#setLayout

    Parameters
    ----------

    data : BoxWhiskersData
      Passed on as a value: Qt reads the C++ BoxWhiskersData, which stays
      Python's own.
    """
    #  void BoxWhiskers::setLayout(const BoxWhiskersData &data)
    self.uglySide.call(
        'ritual_ZN11BoxWhiskers9setLayoutERK15BoxWhiskersData',
        self._valueOf(data),
    )

  @overload(bool)
  def setBoxOutlined(self, outlined: bool) -> None:
    """
    Calls Qt's 'void BoxWhiskers::setBoxOutlined(const bool outlined)'.

    Qt's own words: https://doc.qt.io/qt-6/boxwhiskers.html#setBoxOutlined

    Parameters
    ----------

    outlined : bool
      Passed on as it is.
    """
    #  void BoxWhiskers::setBoxOutlined(const bool outlined)
    self.uglySide.call('ritual_ZN11BoxWhiskers14setBoxOutlinedEb', outlined)

  @overload(float)
  def setBoxWidth(self, width: float) -> None:
    """
    Calls Qt's 'void BoxWhiskers::setBoxWidth(const qreal width)'.

    Qt's own words: https://doc.qt.io/qt-6/boxwhiskers.html#setBoxWidth

    Parameters
    ----------

    width : float
      Passed on as it is.
    """
    #  void BoxWhiskers::setBoxWidth(const qreal width)
    self.uglySide.call('ritual_ZN11BoxWhiskers11setBoxWidthEd', width)

  @overload(QRectF)
  def setGeometry(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void BoxWhiskers::setGeometry(const QRectF &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/boxwhiskers.html#setGeometry

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void BoxWhiskers::setGeometry(const QRectF &rect)
    self.uglySide.call(
        'ritual_ZN11BoxWhiskers11setGeometryERK6QRectF', self._valueOf(rect),
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

  @overload(QBoxSet, AbstractDomain, QGraphicsObject)
  @overload(QBoxSet, AbstractDomain, NoneType)
  @overload(QBoxSet, NoneType, QGraphicsObject)
  @overload(QBoxSet, NoneType, NoneType)
  @overload(NoneType, AbstractDomain, QGraphicsObject)
  @overload(NoneType, AbstractDomain, NoneType)
  @overload(NoneType, NoneType, QGraphicsObject)
  @overload(NoneType, NoneType, NoneType)
  def __init__(
      self,
      set: Optional[QBoxSet],
      domain: Optional[AbstractDomain],
      parent: Optional[QGraphicsObject],
  ) -> None:
    """
    Notes what was given, for Qt's 'BoxWhiskers::BoxWhiskers(QBoxSet *set,
    AbstractDomain *domain, QGraphicsObject *parent)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/boxwhiskers.html#BoxWhiskers

    Parameters
    ----------

    set : Optional[QBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    domain : Optional[AbstractDomain]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QGraphicsObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  BoxWhiskers::BoxWhiskers(QBoxSet *set, AbstractDomain *domain,
    #      QGraphicsObject *parent)
    self._noteCreation(BoxWhiskers, lambda: Rituals.call(
        'ritual_ZN11BoxWhiskersC1EP7QBoxSetP14AbstractDomainP15QGraphicsObj'
        'ect',
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
    Calls Qt's 'void BoxWhiskers::mousePressEvent(QGraphicsSceneMouseEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/boxwhiskers.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void BoxWhiskers::mousePressEvent(QGraphicsSceneMouseEvent *event)
    ritual = (
        'ritual_ZN11BoxWhiskers15mousePressEventEP24QGraphicsSceneMouseEven'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11BoxWhiskers15mousePressEventEP24QGraphicsSceneMou'
          'seEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverEnterEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void BoxWhiskers::hoverEnterEvent(QGraphicsSceneHoverEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/boxwhiskers.html#hoverEnterEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void BoxWhiskers::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
    ritual = (
        'ritual_ZN11BoxWhiskers15hoverEnterEventEP24QGraphicsSceneHoverEven'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11BoxWhiskers15hoverEnterEventEP24QGraphicsSceneHov'
          'erEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void BoxWhiskers::hoverLeaveEvent(QGraphicsSceneHoverEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/boxwhiskers.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void BoxWhiskers::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
    ritual = (
        'ritual_ZN11BoxWhiskers15hoverLeaveEventEP24QGraphicsSceneHoverEven'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11BoxWhiskers15hoverLeaveEventEP24QGraphicsSceneHov'
          'erEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void BoxWhiskers::mouseReleaseEvent(QGraphicsSceneMouseEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/boxwhiskers.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void BoxWhiskers::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
    ritual = (
        'ritual_ZN11BoxWhiskers17mouseReleaseEventEP24QGraphicsSceneMouseEv'
        'ent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11BoxWhiskers17mouseReleaseEventEP24QGraphicsSceneM'
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
    BoxWhiskers::mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/boxwhiskers.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void BoxWhiskers::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
    #      *event)
    ritual = (
        'ritual_ZN11BoxWhiskers21mouseDoubleClickEventEP24QGraphicsSceneMou'
        'seEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11BoxWhiskers21mouseDoubleClickEventEP24QGraphicsSc'
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
    Calls Qt's 'void BoxWhiskers::paint(QPainter *painter, const
    QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/boxwhiskers.html#paint

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
    #  void BoxWhiskers::paint(QPainter *painter, const
    #      QStyleOptionGraphicsItem *option, QWidget *widget)
    ritual = (
        'ritual_ZN11BoxWhiskers5paintEP8QPainterPK24QStyleOptionGraphicsIte'
        'mP7QWidget')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11BoxWhiskers5paintEP8QPainterPK24QStyleOptionGraph'
          'icsItemP7QWidget')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )

  @overload(AbstractDomain)
  @overload(NoneType)
  def updateGeometry(self, domain: Optional[AbstractDomain]) -> None:
    """
    Calls Qt's 'void BoxWhiskers::updateGeometry(AbstractDomain *domain)'.

    Qt's own words: https://doc.qt.io/qt-6/boxwhiskers.html#updateGeometry

    Parameters
    ----------

    domain : Optional[AbstractDomain]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void BoxWhiskers::updateGeometry(AbstractDomain *domain)
    self.uglySide.call(
        'ritual_ZN11BoxWhiskers14updateGeometryEP14AbstractDomain',
        self._addressOf(domain),
    )

  @overload(QBoxSet)
  @overload(NoneType)
  def clicked(self, boxset: Optional[QBoxSet]) -> None:
    """
    Calls Qt's 'void BoxWhiskers::clicked(QBoxSet *boxset)'.

    Qt's own words: https://doc.qt.io/qt-6/boxwhiskers.html#clicked

    Parameters
    ----------

    boxset : Optional[QBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void BoxWhiskers::clicked(QBoxSet *boxset)
    self.uglySide.call(
        'ritual_ZN11BoxWhiskers7clickedEP7QBoxSet', self._addressOf(boxset),
    )

  @overload(bool, QBoxSet)
  @overload(bool, NoneType)
  def hovered(self, status: bool, boxset: Optional[QBoxSet]) -> None:
    """
    Calls Qt's 'void BoxWhiskers::hovered(bool status, QBoxSet *boxset)'.

    Qt's own words: https://doc.qt.io/qt-6/boxwhiskers.html#hovered

    Parameters
    ----------

    status : bool
      Passed on as it is.

    boxset : Optional[QBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void BoxWhiskers::hovered(bool status, QBoxSet *boxset)
    self.uglySide.call(
        'ritual_ZN11BoxWhiskers7hoveredEbP7QBoxSet',
        status, self._addressOf(boxset),
    )

  @overload(QBoxSet)
  @overload(NoneType)
  def pressed(self, boxset: Optional[QBoxSet]) -> None:
    """
    Calls Qt's 'void BoxWhiskers::pressed(QBoxSet *boxset)'.

    Qt's own words: https://doc.qt.io/qt-6/boxwhiskers.html#pressed

    Parameters
    ----------

    boxset : Optional[QBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void BoxWhiskers::pressed(QBoxSet *boxset)
    self.uglySide.call(
        'ritual_ZN11BoxWhiskers7pressedEP7QBoxSet', self._addressOf(boxset),
    )

  @overload(QBoxSet)
  @overload(NoneType)
  def released(self, boxset: Optional[QBoxSet]) -> None:
    """
    Calls Qt's 'void BoxWhiskers::released(QBoxSet *boxset)'.

    Qt's own words: https://doc.qt.io/qt-6/boxwhiskers.html#released

    Parameters
    ----------

    boxset : Optional[QBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void BoxWhiskers::released(QBoxSet *boxset)
    self.uglySide.call(
        'ritual_ZN11BoxWhiskers8releasedEP7QBoxSet', self._addressOf(boxset),
    )

  @overload(QBoxSet)
  @overload(NoneType)
  def doubleClicked(self, boxset: Optional[QBoxSet]) -> None:
    """
    Calls Qt's 'void BoxWhiskers::doubleClicked(QBoxSet *boxset)'.

    Qt's own words: https://doc.qt.io/qt-6/boxwhiskers.html#doubleClicked

    Parameters
    ----------

    boxset : Optional[QBoxSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void BoxWhiskers::doubleClicked(QBoxSet *boxset)
    self.uglySide.call(
        'ritual_ZN11BoxWhiskers13doubleClickedEP7QBoxSet',
        self._addressOf(boxset),
    )
