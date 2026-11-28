"""
QDeclarativeRouteMapItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativeroutemapitem_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativeRouteMapItem to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtQuick import QQuickItem
from . import QDeclarativePolylineMapItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtPositioning import QGeoCoordinate
  from . import QGeoRoute
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoCoordinate = WAIT['QGeoCoordinate']
  QGeoRoute = WAIT['QGeoRoute']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativeRouteMapItem(QDeclarativePolylineMapItem):
  """
  The cute side of Qt's QDeclarativeRouteMapItem: a plain Python object
  standing in front of one C++ QDeclarativeRouteMapItem.

  It is built on the cute 'QDeclarativePolylineMapItem', as Qt's
  QDeclarativeRouteMapItem is built on Qt's QDeclarativePolylineMapItem, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativeRouteMapItem that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'tr', 'route',
  'setRoute', 'routeChanged', 'updateRoutePath', 'setPath'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativeRouteMapItem::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QDeclarativeRouteMapItem::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDeclarativeRouteMapItem::~QDeclarativeRouteMapItem()': the
    destructor: Python never removes a C++ QDeclarativeRouteMapItem.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDeclarativeRouteMapItem is created at the first use, not by
    'QDeclarativeRouteMapItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativeRouteMapItem.
  - Qt tells when it has removed the C++ QDeclarativeRouteMapItem. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QDeclarativeRouteMapItem::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativeroutemapitem.html#tr

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
    #  QString QDeclarativeRouteMapItem::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QDeclarativeRouteMapItem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativeRouteMapItem'

  #  A C++ QDeclarativeRouteMapItem Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativeRouteMapItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDeclarativeRouteMapItem::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeroutemapitem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDeclarativeRouteMapItem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QDeclarativeRouteMapItem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def route(self) -> QGeoRoute:
    """
    Calls Qt's 'QGeoRoute QDeclarativeRouteMapItem::route() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeroutemapitem.html#route

    Returns
    -------

    QGeoRoute
      A new cute QGeoRoute around the copy Qt gave back. Python owns it.
    """
    #  QGeoRoute QDeclarativeRouteMapItem::route() const
    address = self.uglySide.call(
        'ritual_ZNK24QDeclarativeRouteMapItem5routeEv',
    )
    from . import QGeoRoute
    return QGeoRoute._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QGeoRoute)
  def setRoute(self, route: QGeoRoute) -> None:
    """
    Calls Qt's 'void QDeclarativeRouteMapItem::setRoute(const QGeoRoute
    &route)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeroutemapitem.html#setRoute

    Parameters
    ----------

    route : QGeoRoute
      Passed on as a value: Qt reads the C++ QGeoRoute, which stays Python's
      own.
    """
    #  void QDeclarativeRouteMapItem::setRoute(const QGeoRoute &route)
    self.uglySide.call(
        'ritual_ZN24QDeclarativeRouteMapItem8setRouteERK9QGeoRoute',
        self._valueOf(route),
    )

  @overload(QList[QGeoCoordinate])
  def setPath(self, value: QList[QGeoCoordinate]) -> None:
    """
    Calls Qt's 'void QDeclarativeRouteMapItem::setPath(const
    QList<QGeoCoordinate> &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeroutemapitem.html#setPath

    Parameters
    ----------

    value : QList[QGeoCoordinate]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QDeclarativeRouteMapItem::setPath(const QList<QGeoCoordinate>
    #      &value)
    self.uglySide.call(
        'ritual_ZN24QDeclarativeRouteMapItem7setPathERK5QListI14QGeoCoordin'
        'ateE',
        self._valueOf(value),
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
    'QDeclarativeRouteMapItem::QDeclarativeRouteMapItem(QQuickItem *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeroutemapitem.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativeRouteMapItem::QDeclarativeRouteMapItem(QQuickItem *parent)
    self._noteCreation(QDeclarativeRouteMapItem, lambda: Rituals.call(
        'ritual_ZN24QDeclarativeRouteMapItemC1EP10QQuickItem',
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

  @overload(QGeoRoute)
  def routeChanged(self, route: QGeoRoute) -> None:
    """
    Calls Qt's 'void QDeclarativeRouteMapItem::routeChanged(const QGeoRoute
    &route)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeroutemapitem.html#routeChanged

    Parameters
    ----------

    route : QGeoRoute
      Passed on as a value: Qt reads the C++ QGeoRoute, which stays Python's
      own.
    """
    #  void QDeclarativeRouteMapItem::routeChanged(const QGeoRoute &route)
    self.uglySide.call(
        'ritual_ZN24QDeclarativeRouteMapItem12routeChangedERK9QGeoRoute',
        self._valueOf(route),
    )

  def updateRoutePath(self) -> None:
    """
    Calls Qt's 'void QDeclarativeRouteMapItem::updateRoutePath()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeroutemapitem.html#updateRoutePath
    """
    #  void QDeclarativeRouteMapItem::updateRoutePath()
    self.uglySide.call(
        'ritual_ZN24QDeclarativeRouteMapItem15updateRoutePathEv',
    )
