"""
Bar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/bar_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means Bar to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtWidgets import QGraphicsItem, QGraphicsRectItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QPainter
  from ..QtWidgets import QGraphicsSceneHoverEvent, QGraphicsSceneMouseEvent
  from ..QtWidgets import QGraphicsTextItem, QStyleOptionGraphicsItem
  from ..QtWidgets import QWidget
  from . import QBarSet
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBarSet = WAIT['QtCharts:QBarSet']
  QGraphicsSceneHoverEvent = WAIT['QGraphicsSceneHoverEvent']
  QGraphicsSceneMouseEvent = WAIT['QGraphicsSceneMouseEvent']
  QGraphicsTextItem = WAIT['QGraphicsTextItem']
  QPainter = WAIT['QPainter']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Bar(QObject, QGraphicsRectItem):
  """
  The cute side of Qt's Bar: a plain Python object standing in front of one
  C++ Bar.

  It is built on the cute 'QObject', as Qt's Bar is built on Qt's QObject,
  and has everything that class has. It is built on the cute
  'QGraphicsRectItem' as well, as Qt's Bar is built on Qt's QGraphicsRectItem
  too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Bar that has a ritual and that Python can call so
  far, 23 names in all: 'metaObject', 'tr', 'mousePressEvent',
  'hoverEnterEvent', 'hoverLeaveEvent', 'mouseReleaseEvent',
  'mouseDoubleClickEvent', 'paint', 'setVisualsDirty', 'visualsDirty',
  'setLabelDirty', 'labelDirty', 'setLabelItem', 'labelItem', 'setIndex',
  'index', 'setLayoutIndex', 'layoutIndex', 'clicked', 'hovered', 'pressed',
  'released', 'doubleClicked'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Bar::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int Bar::qt_metacall(QMetaObject::Call a0, int a1, void **a2)': one
    of Qt's own inner workings.
  - Qt's 'Bar::~Bar()': the destructor: Python never removes a C++ Bar.

  What has no ritual
  ------------------

  2 of the 29 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Bar is created at the first use, not by 'Bar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Bar.
  - Qt tells when it has removed the C++ Bar. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
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
    Calls Qt's 'QString Bar::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/bar.html#tr

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
    #  QString Bar::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN3Bar2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Bar'

  #  Qt's Bar is built on more than one class. The part of a C++ Bar that
  #  belongs to a class after the first begins somewhere inside the object,
  #  and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QGraphicsRectItem': 'ritual_cast_Bar_QGraphicsRectItem',
  }

  #  A C++ Bar Python makes is of a C++ class of ours, in which Python can
  #  take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Bar'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Bar::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/bar.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Bar::metaObject() const
    address = self.uglySide.call('ritual_ZNK3Bar10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def visualsDirty(self) -> bool:
    """
    Calls Qt's 'bool Bar::visualsDirty() const'.

    Qt's own words: https://doc.qt.io/qt-6/bar.html#visualsDirty
    """
    #  bool Bar::visualsDirty() const
    return self.uglySide.call('ritual_ZNK3Bar12visualsDirtyEv')

  def labelDirty(self) -> bool:
    """
    Calls Qt's 'bool Bar::labelDirty() const'.

    Qt's own words: https://doc.qt.io/qt-6/bar.html#labelDirty
    """
    #  bool Bar::labelDirty() const
    return self.uglySide.call('ritual_ZNK3Bar10labelDirtyEv')

  def labelItem(self) -> Optional[QGraphicsTextItem]:
    """
    Calls Qt's 'QGraphicsTextItem *Bar::labelItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/bar.html#labelItem

    Returns
    -------

    Optional[QGraphicsTextItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsTextItem *Bar::labelItem() const
    address = self.uglySide.call('ritual_ZNK3Bar9labelItemEv')
    from ..QtWidgets import QGraphicsTextItem
    return QGraphicsTextItem._cuteAt(address)

  def index(self) -> int:
    """
    Calls Qt's 'int Bar::index() const'.

    Qt's own words: https://doc.qt.io/qt-6/bar.html#index
    """
    #  int Bar::index() const
    return self.uglySide.call('ritual_ZNK3Bar5indexEv')

  def layoutIndex(self) -> int:
    """
    Calls Qt's 'int Bar::layoutIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/bar.html#layoutIndex
    """
    #  int Bar::layoutIndex() const
    return self.uglySide.call('ritual_ZNK3Bar11layoutIndexEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setVisualsDirty(self, dirty: bool) -> None:
    """
    Calls Qt's 'void Bar::setVisualsDirty(bool dirty)'.

    Qt's own words: https://doc.qt.io/qt-6/bar.html#setVisualsDirty

    Parameters
    ----------

    dirty : bool
      Passed on as it is.
    """
    #  void Bar::setVisualsDirty(bool dirty)
    self.uglySide.call('ritual_ZN3Bar15setVisualsDirtyEb', dirty)

  @overload(bool)
  def setLabelDirty(self, dirty: bool) -> None:
    """
    Calls Qt's 'void Bar::setLabelDirty(bool dirty)'.

    Qt's own words: https://doc.qt.io/qt-6/bar.html#setLabelDirty

    Parameters
    ----------

    dirty : bool
      Passed on as it is.
    """
    #  void Bar::setLabelDirty(bool dirty)
    self.uglySide.call('ritual_ZN3Bar13setLabelDirtyEb', dirty)

  @overload(QGraphicsTextItem)
  @overload(NoneType)
  def setLabelItem(self, labelItem: Optional[QGraphicsTextItem]) -> None:
    """
    Calls Qt's 'void Bar::setLabelItem(QGraphicsTextItem *labelItem)'.

    Qt's own words: https://doc.qt.io/qt-6/bar.html#setLabelItem

    Parameters
    ----------

    labelItem : Optional[QGraphicsTextItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Bar::setLabelItem(QGraphicsTextItem *labelItem)
    self.uglySide.call(
        'ritual_ZN3Bar12setLabelItemEP17QGraphicsTextItem',
        self._addressOf(labelItem),
    )

  @overload(int)
  def setIndex(self, index: int) -> None:
    """
    Calls Qt's 'void Bar::setIndex(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/bar.html#setIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void Bar::setIndex(int index)
    self.uglySide.call('ritual_ZN3Bar8setIndexEi', index)

  @overload(int)
  def setLayoutIndex(self, index: int) -> None:
    """
    Calls Qt's 'void Bar::setLayoutIndex(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/bar.html#setLayoutIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void Bar::setLayoutIndex(int index)
    self.uglySide.call('ritual_ZN3Bar14setLayoutIndexEi', index)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QBarSet)
  @overload(NoneType)
  @overload(QBarSet, QGraphicsItem)
  @overload(QBarSet, NoneType)
  @overload(NoneType, QGraphicsItem)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      barset: Optional[QBarSet],
      parent: Optional[QGraphicsItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'Bar::Bar(QBarSet *barset, QGraphicsItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/bar.html#Bar

    Parameters
    ----------

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Bar::Bar(QBarSet *barset, QGraphicsItem *parent)
    self._noteCreation(Bar, lambda: Rituals.call(
        'ritual_ZN3BarC1EP7QBarSetP13QGraphicsItem',
        self._addressOf(barset), self._addressOf(parent, 'QGraphicsItem'),
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
    Calls Qt's 'void Bar::mousePressEvent(QGraphicsSceneMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/bar.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Bar::mousePressEvent(QGraphicsSceneMouseEvent *event)
    ritual = 'ritual_ZN3Bar15mousePressEventEP24QGraphicsSceneMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3Bar15mousePressEventEP24QGraphicsSceneMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverEnterEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void Bar::hoverEnterEvent(QGraphicsSceneHoverEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/bar.html#hoverEnterEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Bar::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
    ritual = 'ritual_ZN3Bar15hoverEnterEventEP24QGraphicsSceneHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3Bar15hoverEnterEventEP24QGraphicsSceneHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(
      self,
      event: Optional[QGraphicsSceneHoverEvent],
  ) -> None:
    """
    Calls Qt's 'void Bar::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/bar.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Bar::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
    ritual = 'ritual_ZN3Bar15hoverLeaveEventEP24QGraphicsSceneHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3Bar15hoverLeaveEventEP24QGraphicsSceneHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void Bar::mouseReleaseEvent(QGraphicsSceneMouseEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/bar.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Bar::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
    ritual = 'ritual_ZN3Bar17mouseReleaseEventEP24QGraphicsSceneMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3Bar17mouseReleaseEventEP24QGraphicsSceneMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QGraphicsSceneMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(
      self,
      event: Optional[QGraphicsSceneMouseEvent],
  ) -> None:
    """
    Calls Qt's 'void Bar::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/bar.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QGraphicsSceneMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Bar::mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event)
    ritual = (
        'ritual_ZN3Bar21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3Bar21mouseDoubleClickEventEP24QGraphicsSceneMouseE'
          'vent')
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
    Calls Qt's 'void Bar::paint(QPainter *painter, const
    QStyleOptionGraphicsItem *option, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/bar.html#paint

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
    #  void Bar::paint(QPainter *painter, const QStyleOptionGraphicsItem
    #      *option, QWidget *widget)
    ritual = (
        'ritual_ZN3Bar5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidge'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN3Bar5paintEP8QPainterPK24QStyleOptionGraphicsItemP7'
          'QWidget')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._addressOf(option),
        self._addressOf(widget),
    )

  @overload(int, QBarSet)
  @overload(int, NoneType)
  def clicked(self, index: int, barset: Optional[QBarSet]) -> None:
    """
    Calls Qt's 'void Bar::clicked(int index, QBarSet *barset)'.

    Qt's own words: https://doc.qt.io/qt-6/bar.html#clicked

    Parameters
    ----------

    index : int
      Passed on as it is.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Bar::clicked(int index, QBarSet *barset)
    self.uglySide.call(
        'ritual_ZN3Bar7clickedEiP7QBarSet', index, self._addressOf(barset),
    )

  @overload(bool, int, QBarSet)
  @overload(bool, int, NoneType)
  def hovered(
      self,
      status: bool,
      index: int,
      barset: Optional[QBarSet],
  ) -> None:
    """
    Calls Qt's 'void Bar::hovered(bool status, int index, QBarSet *barset)'.

    Qt's own words: https://doc.qt.io/qt-6/bar.html#hovered

    Parameters
    ----------

    status : bool
      Passed on as it is.

    index : int
      Passed on as it is.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Bar::hovered(bool status, int index, QBarSet *barset)
    self.uglySide.call(
        'ritual_ZN3Bar7hoveredEbiP7QBarSet',
        status, index, self._addressOf(barset),
    )

  @overload(int, QBarSet)
  @overload(int, NoneType)
  def pressed(self, index: int, barset: Optional[QBarSet]) -> None:
    """
    Calls Qt's 'void Bar::pressed(int index, QBarSet *barset)'.

    Qt's own words: https://doc.qt.io/qt-6/bar.html#pressed

    Parameters
    ----------

    index : int
      Passed on as it is.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Bar::pressed(int index, QBarSet *barset)
    self.uglySide.call(
        'ritual_ZN3Bar7pressedEiP7QBarSet', index, self._addressOf(barset),
    )

  @overload(int, QBarSet)
  @overload(int, NoneType)
  def released(self, index: int, barset: Optional[QBarSet]) -> None:
    """
    Calls Qt's 'void Bar::released(int index, QBarSet *barset)'.

    Qt's own words: https://doc.qt.io/qt-6/bar.html#released

    Parameters
    ----------

    index : int
      Passed on as it is.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Bar::released(int index, QBarSet *barset)
    self.uglySide.call(
        'ritual_ZN3Bar8releasedEiP7QBarSet', index, self._addressOf(barset),
    )

  @overload(int, QBarSet)
  @overload(int, NoneType)
  def doubleClicked(self, index: int, barset: Optional[QBarSet]) -> None:
    """
    Calls Qt's 'void Bar::doubleClicked(int index, QBarSet *barset)'.

    Qt's own words: https://doc.qt.io/qt-6/bar.html#doubleClicked

    Parameters
    ----------

    index : int
      Passed on as it is.

    barset : Optional[QBarSet]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Bar::doubleClicked(int index, QBarSet *barset)
    self.uglySide.call(
        'ritual_ZN3Bar13doubleClickedEiP7QBarSet',
        index, self._addressOf(barset),
    )
