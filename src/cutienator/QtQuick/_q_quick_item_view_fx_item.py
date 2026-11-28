"""
QQuickItemViewFxItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickitemviewfxitem_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickItemViewFxItem to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQuickItemViewTransitioner

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF, QRectF
  from . import QQuickItem, QQuickItemChangeListener
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QQuickItem = WAIT['QQuickItem']
  QQuickItemChangeListener = WAIT['QQuickItemChangeListener']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickItemViewFxItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickItemViewFxItem: a plain Python object standing
  in front of one C++ QQuickItemViewFxItem.

  What exists
  -----------

  Every function of Qt's QQuickItemViewFxItem that has a ritual and that
  Python can call so far, 21 names in all: 'itemX', 'itemY', 'itemWidth',
  'itemHeight', 'moveTo', 'setVisible', 'trackGeometry', 'geometry',
  'setGeometry', 'scheduledTransitionType', 'transitionScheduledOrRunning',
  'transitionRunning', 'isPendingRemoval', 'transitionNextReposition',
  'prepareTransition', 'startTransition', 'position', 'endPosition', 'size',
  'sectionSize', 'contains'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickItemViewFxItem::~QQuickItemViewFxItem()': the destructor:
    Python never removes a C++ QQuickItemViewFxItem.

  What to expect
  --------------

  - The C++ QQuickItemViewFxItem is created at the first use, not by
    'QQuickItemViewFxItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickItemViewFxItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickItemViewFxItem'

  #  A C++ QQuickItemViewFxItem Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickItemViewFxItem'

  #  The functions Qt calls itself that QQuickItemViewFxItem is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'position': (
          ('_ZNK20QQuickItemViewFxItem8positionEv',
           ('double', 'number', ''),
           ()),
      ),
      'endPosition': (
          ('_ZNK20QQuickItemViewFxItem11endPositionEv',
           ('double', 'number', ''),
           ()),
      ),
      'size': (
          ('_ZNK20QQuickItemViewFxItem4sizeEv',
           ('double', 'number', ''),
           ()),
      ),
      'sectionSize': (
          ('_ZNK20QQuickItemViewFxItem11sectionSizeEv',
           ('double', 'number', ''),
           ()),
      ),
      'contains': (
          ('_ZNK20QQuickItemViewFxItem8containsEdd',
           ('bool', 'number', ''),
           (
               ('double', 'number', ''),
               ('double', 'number', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def itemX(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemViewFxItem::itemX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemviewfxitem.html#itemX
    """
    #  qreal QQuickItemViewFxItem::itemX() const
    return self.uglySide.call('ritual_ZNK20QQuickItemViewFxItem5itemXEv')

  def itemY(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemViewFxItem::itemY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemviewfxitem.html#itemY
    """
    #  qreal QQuickItemViewFxItem::itemY() const
    return self.uglySide.call('ritual_ZNK20QQuickItemViewFxItem5itemYEv')

  def itemWidth(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemViewFxItem::itemWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewfxitem.html#itemWidth
    """
    #  qreal QQuickItemViewFxItem::itemWidth() const
    return self.uglySide.call('ritual_ZNK20QQuickItemViewFxItem9itemWidthEv')

  def itemHeight(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemViewFxItem::itemHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewfxitem.html#itemHeight
    """
    #  qreal QQuickItemViewFxItem::itemHeight() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickItemViewFxItem10itemHeightEv',
    )

  def geometry(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickItemViewFxItem::geometry() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemviewfxitem.html#geometry

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickItemViewFxItem::geometry() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickItemViewFxItem8geometryEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def scheduledTransitionType(
      self,
  ) -> QQuickItemViewTransitioner.TransitionType:
    """
    Calls Qt's 'QQuickItemViewTransitioner::TransitionType
    QQuickItemViewFxItem::scheduledTransitionType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewfxitem.html#scheduledTransitionType

    Returns
    -------

    QQuickItemViewTransitioner.TransitionType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickItemViewTransitioner.TransitionType(number)' gives.
    """
    #  QQuickItemViewTransitioner::TransitionType
    #      QQuickItemViewFxItem::scheduledTransitionType() const
    return QQuickItemViewTransitioner.TransitionType(self.uglySide.call(
        'ritual_ZNK20QQuickItemViewFxItem23scheduledTransitionTypeEv',
    ))

  def transitionScheduledOrRunning(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemViewFxItem::transitionScheduledOrRunning()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewfxitem.html
    """
    #  bool QQuickItemViewFxItem::transitionScheduledOrRunning() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickItemViewFxItem28transitionScheduledOrRunningEv',
    )

  def transitionRunning(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemViewFxItem::transitionRunning() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewfxitem.html#transitionRunning
    """
    #  bool QQuickItemViewFxItem::transitionRunning() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickItemViewFxItem17transitionRunningEv',
    )

  def isPendingRemoval(self) -> bool:
    """
    Calls Qt's 'bool QQuickItemViewFxItem::isPendingRemoval() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewfxitem.html#isPendingRemoval
    """
    #  bool QQuickItemViewFxItem::isPendingRemoval() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickItemViewFxItem16isPendingRemovalEv',
    )

  def position(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemViewFxItem::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemviewfxitem.html#position
    """
    #  qreal QQuickItemViewFxItem::position() const
    return self.uglySide.call('ritual_ZNK20QQuickItemViewFxItem8positionEv')

  def endPosition(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemViewFxItem::endPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewfxitem.html#endPosition
    """
    #  qreal QQuickItemViewFxItem::endPosition() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickItemViewFxItem11endPositionEv',
    )

  def size(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemViewFxItem::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemviewfxitem.html#size
    """
    #  qreal QQuickItemViewFxItem::size() const
    return self.uglySide.call('ritual_ZNK20QQuickItemViewFxItem4sizeEv')

  def sectionSize(self) -> float:
    """
    Calls Qt's 'qreal QQuickItemViewFxItem::sectionSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewfxitem.html#sectionSize
    """
    #  qreal QQuickItemViewFxItem::sectionSize() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickItemViewFxItem11sectionSizeEv',
    )

  @overload(float, float)
  def contains(self, x: float, y: float) -> bool:
    """
    Calls Qt's 'bool QQuickItemViewFxItem::contains(qreal x, qreal y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemviewfxitem.html#contains

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  bool QQuickItemViewFxItem::contains(qreal x, qreal y) const
    return self.uglySide.call(
        'ritual_ZNK20QQuickItemViewFxItem8containsEdd', x, y,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QQuickItemViewFxItem::setVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewfxitem.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QQuickItemViewFxItem::setVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN20QQuickItemViewFxItem10setVisibleEb', visible,
    )

  @overload(QRectF)
  def setGeometry(self, geometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickItemViewFxItem::setGeometry(const QRectF
    &geometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewfxitem.html#setGeometry

    Parameters
    ----------

    geometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickItemViewFxItem::setGeometry(const QRectF &geometry)
    self.uglySide.call(
        'ritual_ZN20QQuickItemViewFxItem11setGeometryERK6QRectF',
        self._valueOf(geometry),
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

  @overload(QQuickItem, bool, QQuickItemChangeListener)
  @overload(QQuickItem, bool, NoneType)
  @overload(NoneType, bool, QQuickItemChangeListener)
  @overload(NoneType, bool, NoneType)
  def __init__(
      self,
      item: Optional[QQuickItem],
      ownItem: bool,
      changeListener: Optional[QQuickItemChangeListener],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickItemViewFxItem::QQuickItemViewFxItem(QQuickItem *item, bool
    ownItem, QQuickItemChangeListener *changeListener)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewfxitem.html#QQuickItemViewFxItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ownItem : bool
      Passed on as it is.

    changeListener : Optional[QQuickItemChangeListener]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickItemViewFxItem::QQuickItemViewFxItem(QQuickItem *item, bool
    #      ownItem, QQuickItemChangeListener *changeListener)
    self._noteCreation(QQuickItemViewFxItem, lambda: Rituals.call(
        'ritual_ZN20QQuickItemViewFxItemC1EP10QQuickItembP24QQuickItemChang'
        'eListener',
        self._addressOf(item), ownItem, self._addressOf(changeListener,
        'QQuickItemChangeListener'),
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

  @overload(QPointF, bool)
  def moveTo(self, pos: QPointF, immediate: bool) -> None:
    """
    Calls Qt's 'void QQuickItemViewFxItem::moveTo(const QPointF &pos, bool
    immediate)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickitemviewfxitem.html#moveTo

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    immediate : bool
      Passed on as it is.
    """
    #  void QQuickItemViewFxItem::moveTo(const QPointF &pos, bool immediate)
    self.uglySide.call(
        'ritual_ZN20QQuickItemViewFxItem6moveToERK7QPointFb',
        self._valueOf(pos, 'QPointF'), immediate,
    )

  @overload(bool)
  def trackGeometry(self, track: bool) -> None:
    """
    Calls Qt's 'void QQuickItemViewFxItem::trackGeometry(bool track)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewfxitem.html#trackGeometry

    Parameters
    ----------

    track : bool
      Passed on as it is.
    """
    #  void QQuickItemViewFxItem::trackGeometry(bool track)
    self.uglySide.call(
        'ritual_ZN20QQuickItemViewFxItem13trackGeometryEb', track,
    )

  @overload(
      QQuickItemViewTransitioner, QQuickItemViewTransitioner.TransitionType,
      bool,
  )
  @overload(NoneType, QQuickItemViewTransitioner.TransitionType, bool)
  def transitionNextReposition(
      self,
      transitioner: Optional[QQuickItemViewTransitioner],
      type: QQuickItemViewTransitioner.TransitionType,
      asTarget: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickItemViewFxItem::transitionNextReposition(QQuickItemViewTransitioner
    *transitioner, QQuickItemViewTransitioner::TransitionType type, bool
    asTarget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewfxitem.html#transitionNextReposition

    Parameters
    ----------

    transitioner : Optional[QQuickItemViewTransitioner]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : QQuickItemViewTransitioner.TransitionType
      Passed on as its number.

    asTarget : bool
      Passed on as it is.
    """
    #  void QQuickItemViewFxItem::transitionNextReposition(
    #      QQuickItemViewTransitioner *transitioner,
    #      QQuickItemViewTransitioner::TransitionType type, bool asTarget)
    self.uglySide.call(
        'ritual_ZN20QQuickItemViewFxItem24transitionNextRepositionEP26QQuic'
        'kItemViewTransitionerNS0_14TransitionTypeEb',
        self._addressOf(transitioner), type.value, asTarget,
    )

  @overload(QQuickItemViewTransitioner, QRectF)
  @overload(NoneType, QRectF)
  def prepareTransition(
      self,
      transitioner: Optional[QQuickItemViewTransitioner],
      viewBounds: QRectF,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickItemViewFxItem::prepareTransition(QQuickItemViewTransitioner
    *transitioner, const QRectF &viewBounds)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewfxitem.html#prepareTransition

    Parameters
    ----------

    transitioner : Optional[QQuickItemViewTransitioner]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    viewBounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  bool
    #      QQuickItemViewFxItem::prepareTransition(QQuickItemViewTransitioner
    #      *transitioner, const QRectF &viewBounds)
    return self.uglySide.call(
        'ritual_ZN20QQuickItemViewFxItem17prepareTransitionEP26QQuickItemVi'
        'ewTransitionerRK6QRectF',
        self._addressOf(transitioner), self._valueOf(viewBounds),
    )

  @overload(QQuickItemViewTransitioner)
  @overload(NoneType)
  def startTransition(
      self,
      transitioner: Optional[QQuickItemViewTransitioner],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickItemViewFxItem::startTransition(QQuickItemViewTransitioner
    *transitioner)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickitemviewfxitem.html#startTransition

    Parameters
    ----------

    transitioner : Optional[QQuickItemViewTransitioner]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickItemViewFxItem::startTransition(QQuickItemViewTransitioner
    #      *transitioner)
    self.uglySide.call(
        'ritual_ZN20QQuickItemViewFxItem15startTransitionEP26QQuickItemView'
        'Transitioner',
        self._addressOf(transitioner),
    )
