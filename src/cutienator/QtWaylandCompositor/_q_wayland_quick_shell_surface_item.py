"""
QWaylandQuickShellSurfaceItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandquickshellsurfaceitem.h, Qt 6.12.0. Changes
#  made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QWaylandQuickItem
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QWaylandQuickShellSurfaceItemPrivate, QWaylandShellSurface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWaylandShellSurface = WAIT['QWaylandShellSurface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandQuickShellSurfaceItem(QWaylandQuickItem):
  """
  The cute side of Qt's QWaylandQuickShellSurfaceItem: a plain Python object
  standing in front of one C++ QWaylandQuickShellSurfaceItem.

  It is built on the cute 'QWaylandQuickItem', as Qt's
  QWaylandQuickShellSurfaceItem is built on Qt's QWaylandQuickItem, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandQuickShellSurfaceItem that has a ritual and
  that Python can call so far, 18 names in all: 'metaObject', 'tr', 'd_func',
  'shellSurface', 'setShellSurface', 'moveItem', 'setMoveItem',
  'autoCreatePopupItems', 'setAutoCreatePopupItems', 'staysOnTop',
  'setStaysOnTop', 'staysOnBottom', 'setStaysOnBottom',
  'shellSurfaceChanged', 'moveItemChanged', 'autoCreatePopupItemsChanged',
  'staysOnTopChanged', 'staysOnBottomChanged'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandQuickShellSurfaceItem::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QWaylandQuickShellSurfaceItem::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QWaylandQuickShellSurfaceItemPrivate
    *QWaylandQuickShellSurfaceItem::d_func() const': takes in Python what
    'QWaylandQuickShellSurfaceItemPrivate
    *QWaylandQuickShellSurfaceItem::d_func()' takes.
  - Qt's 'QWaylandQuickShellSurfaceItem::~QWaylandQuickShellSurfaceItem()':
    the destructor: Python never removes a C++ QWaylandQuickShellSurfaceItem.
  - Qt's 'QWaylandQuickShellSurfaceItem::QWaylandQuickShellSurfaceItem(
    QWaylandQuickShellSurfaceItemPrivate &dd, QQuickItem *parent)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 26 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandQuickShellSurfaceItem is created at the first use, not by
    'QWaylandQuickShellSurfaceItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandQuickShellSurfaceItem.
  - Qt tells when it has removed the C++ QWaylandQuickShellSurfaceItem. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QWaylandQuickShellSurfaceItem::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshellsurfaceitem.html#tr

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
    #  QString QWaylandQuickShellSurfaceItem::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN29QWaylandQuickShellSurfaceItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandQuickShellSurfaceItem'

  #  A C++ QWaylandQuickShellSurfaceItem Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandQuickShellSurfaceItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QWaylandQuickShellSurfaceItem::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshellsurfaceitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandQuickShellSurfaceItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29QWaylandQuickShellSurfaceItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def shellSurface(self) -> Optional[QWaylandShellSurface]:
    """
    Calls Qt's 'QWaylandShellSurface
    *QWaylandQuickShellSurfaceItem::shellSurface() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshellsurfaceitem.html#shellSurface

    Returns
    -------

    Optional[QWaylandShellSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandShellSurface *QWaylandQuickShellSurfaceItem::shellSurface()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK29QWaylandQuickShellSurfaceItem12shellSurfaceEv',
    )
    from . import QWaylandShellSurface
    return QWaylandShellSurface._cuteAt(address)

  def moveItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QWaylandQuickShellSurfaceItem::moveItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshellsurfaceitem.html#moveItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QWaylandQuickShellSurfaceItem::moveItem() const
    address = self.uglySide.call(
        'ritual_ZNK29QWaylandQuickShellSurfaceItem8moveItemEv',
    )
    return QQuickItem._cuteAt(address)

  def staysOnTop(self) -> bool:
    """
    Calls Qt's 'bool QWaylandQuickShellSurfaceItem::staysOnTop() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshellsurfaceitem.html#staysOnTop
    """
    #  bool QWaylandQuickShellSurfaceItem::staysOnTop() const
    return self.uglySide.call(
        'ritual_ZNK29QWaylandQuickShellSurfaceItem10staysOnTopEv',
    )

  def staysOnBottom(self) -> bool:
    """
    Calls Qt's 'bool QWaylandQuickShellSurfaceItem::staysOnBottom() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshellsurfaceitem.html#staysOnBottom
    """
    #  bool QWaylandQuickShellSurfaceItem::staysOnBottom() const
    return self.uglySide.call(
        'ritual_ZNK29QWaylandQuickShellSurfaceItem13staysOnBottomEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWaylandShellSurface)
  @overload(NoneType)
  def setShellSurface(
      self,
      shellSurface: Optional[QWaylandShellSurface],
  ) -> None:
    """
    Calls Qt's 'void
    QWaylandQuickShellSurfaceItem::setShellSurface(QWaylandShellSurface
    *shellSurface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshellsurfaceitem.html#setShellSurface

    Parameters
    ----------

    shellSurface : Optional[QWaylandShellSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandQuickShellSurfaceItem::setShellSurface(
    #      QWaylandShellSurface *shellSurface)
    self.uglySide.call(
        'ritual_ZN29QWaylandQuickShellSurfaceItem15setShellSurfaceEP20QWayl'
        'andShellSurface',
        self._addressOf(shellSurface),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setMoveItem(self, moveItem: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QWaylandQuickShellSurfaceItem::setMoveItem(QQuickItem
    *moveItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshellsurfaceitem.html#setMoveItem

    Parameters
    ----------

    moveItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandQuickShellSurfaceItem::setMoveItem(QQuickItem *moveItem)
    self.uglySide.call(
        'ritual_ZN29QWaylandQuickShellSurfaceItem11setMoveItemEP10QQuickIte'
        'm',
        self._addressOf(moveItem),
    )

  @overload(bool)
  def setAutoCreatePopupItems(self, enabled: bool) -> None:
    """
    Calls Qt's 'void
    QWaylandQuickShellSurfaceItem::setAutoCreatePopupItems(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshellsurfaceitem.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QWaylandQuickShellSurfaceItem::setAutoCreatePopupItems(bool
    #      enabled)
    self.uglySide.call(
        'ritual_ZN29QWaylandQuickShellSurfaceItem23setAutoCreatePopupItemsE'
        'b',
        enabled,
    )

  @overload(bool)
  def setStaysOnTop(self, on: bool) -> None:
    """
    Calls Qt's 'void QWaylandQuickShellSurfaceItem::setStaysOnTop(bool on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshellsurfaceitem.html#setStaysOnTop

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QWaylandQuickShellSurfaceItem::setStaysOnTop(bool on)
    self.uglySide.call(
        'ritual_ZN29QWaylandQuickShellSurfaceItem13setStaysOnTopEb', on,
    )

  @overload(bool)
  def setStaysOnBottom(self, on: bool) -> None:
    """
    Calls Qt's 'void QWaylandQuickShellSurfaceItem::setStaysOnBottom(bool
    on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshellsurfaceitem.html

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QWaylandQuickShellSurfaceItem::setStaysOnBottom(bool on)
    self.uglySide.call(
        'ritual_ZN29QWaylandQuickShellSurfaceItem16setStaysOnBottomEb', on,
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
    'QWaylandQuickShellSurfaceItem::QWaylandQuickShellSurfaceItem(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshellsurfaceitem.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QWaylandQuickShellSurfaceItem::QWaylandQuickShellSurfaceItem(
    #      QQuickItem *parent)
    self._noteCreation(QWaylandQuickShellSurfaceItem, lambda: Rituals.call(
        'ritual_ZN29QWaylandQuickShellSurfaceItemC1EP10QQuickItem',
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

  def d_func(self) -> Optional[QWaylandQuickShellSurfaceItemPrivate]:
    """
    Calls Qt's 'QWaylandQuickShellSurfaceItemPrivate
    *QWaylandQuickShellSurfaceItem::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshellsurfaceitem.html#d_func

    Returns
    -------

    Optional[QWaylandQuickShellSurfaceItemPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandQuickShellSurfaceItemPrivate
    #      *QWaylandQuickShellSurfaceItem::d_func()
    address = self.uglySide.call(
        'ritual_ZN29QWaylandQuickShellSurfaceItem6d_funcEv',
    )
    from . import QWaylandQuickShellSurfaceItemPrivate
    return QWaylandQuickShellSurfaceItemPrivate._cuteAt(address)

  def autoCreatePopupItems(self) -> bool:
    """
    Calls Qt's 'bool QWaylandQuickShellSurfaceItem::autoCreatePopupItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshellsurfaceitem.html
    """
    #  bool QWaylandQuickShellSurfaceItem::autoCreatePopupItems()
    return self.uglySide.call(
        'ritual_ZN29QWaylandQuickShellSurfaceItem20autoCreatePopupItemsEv',
    )

  def shellSurfaceChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickShellSurfaceItem::shellSurfaceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshellsurfaceitem.html
    """
    #  void QWaylandQuickShellSurfaceItem::shellSurfaceChanged()
    self.uglySide.call(
        'ritual_ZN29QWaylandQuickShellSurfaceItem19shellSurfaceChangedEv',
    )

  def moveItemChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickShellSurfaceItem::moveItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshellsurfaceitem.html#moveItemChanged
    """
    #  void QWaylandQuickShellSurfaceItem::moveItemChanged()
    self.uglySide.call(
        'ritual_ZN29QWaylandQuickShellSurfaceItem15moveItemChangedEv',
    )

  def autoCreatePopupItemsChanged(self) -> None:
    """
    Calls Qt's 'void
    QWaylandQuickShellSurfaceItem::autoCreatePopupItemsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshellsurfaceitem.html
    """
    #  void QWaylandQuickShellSurfaceItem::autoCreatePopupItemsChanged()
    self.uglySide.call(
        'ritual_ZN29QWaylandQuickShellSurfaceItem27autoCreatePopupItemsChan'
        'gedEv',
    )

  def staysOnTopChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickShellSurfaceItem::staysOnTopChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshellsurfaceitem.html
    """
    #  void QWaylandQuickShellSurfaceItem::staysOnTopChanged()
    self.uglySide.call(
        'ritual_ZN29QWaylandQuickShellSurfaceItem17staysOnTopChangedEv',
    )

  def staysOnBottomChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandQuickShellSurfaceItem::staysOnBottomChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandquickshellsurfaceitem.html
    """
    #  void QWaylandQuickShellSurfaceItem::staysOnBottomChanged()
    self.uglySide.call(
        'ritual_ZN29QWaylandQuickShellSurfaceItem20staysOnBottomChangedEv',
    )
