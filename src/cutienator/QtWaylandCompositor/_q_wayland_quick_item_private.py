"""
QWaylandQuickItemPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandquickitem_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QWaylandQuickItemPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF
  from . import QWaylandQuickItem, QWaylandSeat, QWaylandSurface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QWaylandQuickItem = WAIT['QWaylandQuickItem']
  QWaylandSeat = WAIT['QWaylandSeat']
  QWaylandSurface = WAIT['QWaylandSurface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandQuickItemPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWaylandQuickItemPrivate: a plain Python object
  standing in front of one C++ QWaylandQuickItemPrivate.

  What exists
  -----------

  Every function of Qt's QWaylandQuickItemPrivate that has a ritual and that
  Python can call so far, 14 names in all: 'q_func', 'get',
  'setInputEventsEnabled', 'handleDragEnded', 'handleDragUpdate',
  'shouldSendInputEvents', 'scaleFactor', 'findSibling', 'placeAboveSibling',
  'placeBelowSibling', 'placeAboveParent', 'placeBelowParent', 'raise_',
  'lower'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QWaylandQuickItem *QWaylandQuickItemPrivate::q_func() const':
    takes in Python what 'QWaylandQuickItem
    *QWaylandQuickItemPrivate::q_func()' takes.

  What has no ritual
  ------------------

  1 of the 17 functions Qt declares: 1 leans on 'QWaylandQuickItemPrivate.

  What to expect
  --------------

  - The C++ QWaylandQuickItemPrivate is created at the first use, not by
    'QWaylandQuickItemPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandQuickItemPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QWaylandQuickItem)
  @overload(NoneType)
  def get(
      item: Optional[QWaylandQuickItem],
  ) -> Optional[QWaylandQuickItemPrivate]:
    """
    Calls Qt's 'const QWaylandQuickItemPrivate
    *QWaylandQuickItemPrivate::get(const QWaylandQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandquickitemprivate.html#get

    Parameters
    ----------

    item : Optional[QWaylandQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWaylandQuickItemPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QWaylandQuickItemPrivate *QWaylandQuickItemPrivate::get(const
    #      QWaylandQuickItem *item)
    address = Rituals.call(
        'ritual_ZN24QWaylandQuickItemPrivate3getEPK17QWaylandQuickItem',
        CuteMixin._addressOf(item),
    )
    return QWaylandQuickItemPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandQuickItemPrivate'

  #  A C++ QWaylandQuickItemPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandQuickItemPrivate'

  #  The functions Qt calls itself that QWaylandQuickItemPrivate is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'raise': (
          ('_ZN24QWaylandQuickItemPrivate5raiseEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'lower': (
          ('_ZN24QWaylandQuickItemPrivate5lowerEv',
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

  def shouldSendInputEvents(self) -> bool:
    """
    Calls Qt's 'bool QWaylandQuickItemPrivate::shouldSendInputEvents()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitemprivate.html
    """
    #  bool QWaylandQuickItemPrivate::shouldSendInputEvents() const
    return self.uglySide.call(
        'ritual_ZNK24QWaylandQuickItemPrivate21shouldSendInputEventsEv',
    )

  def scaleFactor(self) -> float:
    """
    Calls Qt's 'qreal QWaylandQuickItemPrivate::scaleFactor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitemprivate.html#scaleFactor
    """
    #  qreal QWaylandQuickItemPrivate::scaleFactor() const
    return self.uglySide.call(
        'ritual_ZNK24QWaylandQuickItemPrivate11scaleFactorEv',
    )

  @overload(QWaylandSurface)
  @overload(NoneType)
  def findSibling(
      self,
      surface: Optional[QWaylandSurface],
  ) -> Optional[QWaylandQuickItem]:
    """
    Calls Qt's 'QWaylandQuickItem
    *QWaylandQuickItemPrivate::findSibling(QWaylandSurface *surface) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitemprivate.html#findSibling

    Parameters
    ----------

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWaylandQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandQuickItem
    #      *QWaylandQuickItemPrivate::findSibling(QWaylandSurface *surface)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK24QWaylandQuickItemPrivate11findSiblingEP15QWaylandSurfa'
        'ce',
        self._addressOf(surface),
    )
    from . import QWaylandQuickItem
    return QWaylandQuickItem._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setInputEventsEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QWaylandQuickItemPrivate::setInputEventsEnabled(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitemprivate.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QWaylandQuickItemPrivate::setInputEventsEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN24QWaylandQuickItemPrivate21setInputEventsEnabledEb',
        enable,
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
    'QWaylandQuickItemPrivate::QWaylandQuickItemPrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitemprivate.html
    """
    #  QWaylandQuickItemPrivate::QWaylandQuickItemPrivate()
    self._noteCreation(QWaylandQuickItemPrivate, lambda: Rituals.call(
        'ritual_ZN24QWaylandQuickItemPrivateC1Ev',
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

  def q_func(self) -> Optional[QWaylandQuickItem]:
    """
    Calls Qt's 'QWaylandQuickItem *QWaylandQuickItemPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitemprivate.html#q_func

    Returns
    -------

    Optional[QWaylandQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandQuickItem *QWaylandQuickItemPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN24QWaylandQuickItemPrivate6q_funcEv',
    )
    from . import QWaylandQuickItem
    return QWaylandQuickItem._cuteAt(address)

  @overload(QWaylandSeat)
  @overload(NoneType)
  def handleDragEnded(self, seat: Optional[QWaylandSeat]) -> None:
    """
    Calls Qt's 'void QWaylandQuickItemPrivate::handleDragEnded(QWaylandSeat
    *seat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitemprivate.html#handleDragEnded

    Parameters
    ----------

    seat : Optional[QWaylandSeat]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandQuickItemPrivate::handleDragEnded(QWaylandSeat *seat)
    self.uglySide.call(
        'ritual_ZN24QWaylandQuickItemPrivate15handleDragEndedEP12QWaylandSe'
        'at',
        self._addressOf(seat),
    )

  @overload(QWaylandSeat, QPointF)
  @overload(NoneType, QPointF)
  def handleDragUpdate(
      self,
      seat: Optional[QWaylandSeat],
      globalPosition: QPointF,
  ) -> None:
    """
    Calls Qt's 'void QWaylandQuickItemPrivate::handleDragUpdate(QWaylandSeat
    *seat, const QPointF &globalPosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitemprivate.html#handleDragUpdate

    Parameters
    ----------

    seat : Optional[QWaylandSeat]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    globalPosition : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QWaylandQuickItemPrivate::handleDragUpdate(QWaylandSeat *seat,
    #      const QPointF &globalPosition)
    self.uglySide.call(
        'ritual_ZN24QWaylandQuickItemPrivate16handleDragUpdateEP12QWaylandS'
        'eatRK7QPointF',
        self._addressOf(seat), self._valueOf(globalPosition, 'QPointF'),
    )

  @overload(QWaylandQuickItem)
  @overload(NoneType)
  def placeAboveSibling(self, sibling: Optional[QWaylandQuickItem]) -> None:
    """
    Calls Qt's 'void
    QWaylandQuickItemPrivate::placeAboveSibling(QWaylandQuickItem *sibling)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitemprivate.html#placeAboveSibling

    Parameters
    ----------

    sibling : Optional[QWaylandQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandQuickItemPrivate::placeAboveSibling(QWaylandQuickItem
    #      *sibling)
    self.uglySide.call(
        'ritual_ZN24QWaylandQuickItemPrivate17placeAboveSiblingEP17QWayland'
        'QuickItem',
        self._addressOf(sibling),
    )

  @overload(QWaylandQuickItem)
  @overload(NoneType)
  def placeBelowSibling(self, sibling: Optional[QWaylandQuickItem]) -> None:
    """
    Calls Qt's 'void
    QWaylandQuickItemPrivate::placeBelowSibling(QWaylandQuickItem *sibling)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitemprivate.html#placeBelowSibling

    Parameters
    ----------

    sibling : Optional[QWaylandQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandQuickItemPrivate::placeBelowSibling(QWaylandQuickItem
    #      *sibling)
    self.uglySide.call(
        'ritual_ZN24QWaylandQuickItemPrivate17placeBelowSiblingEP17QWayland'
        'QuickItem',
        self._addressOf(sibling),
    )

  def placeAboveParent(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItemPrivate::placeAboveParent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitemprivate.html#placeAboveParent
    """
    #  void QWaylandQuickItemPrivate::placeAboveParent()
    self.uglySide.call(
        'ritual_ZN24QWaylandQuickItemPrivate16placeAboveParentEv',
    )

  def placeBelowParent(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItemPrivate::placeBelowParent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitemprivate.html#placeBelowParent
    """
    #  void QWaylandQuickItemPrivate::placeBelowParent()
    self.uglySide.call(
        'ritual_ZN24QWaylandQuickItemPrivate16placeBelowParentEv',
    )

  def raise_(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItemPrivate::raise()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitemprivate.html#raise
    """
    #  void QWaylandQuickItemPrivate::raise()
    ritual = 'ritual_ZN24QWaylandQuickItemPrivate5raiseEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QWaylandQuickItemPrivate5raiseEv'
    self.uglySide.call(ritual)

  def lower(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickItemPrivate::lower()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickitemprivate.html#lower
    """
    #  void QWaylandQuickItemPrivate::lower()
    ritual = 'ritual_ZN24QWaylandQuickItemPrivate5lowerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QWaylandQuickItemPrivate5lowerEv'
    self.uglySide.call(ritual)
