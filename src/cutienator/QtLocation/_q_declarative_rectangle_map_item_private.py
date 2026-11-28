"""
QDeclarativeRectangleMapItemPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativerectanglemapitem_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativeRectangleMapItemPrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF
  from ..QtQuick import QSGNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QSGNode = WAIT['QSGNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativeRectangleMapItemPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDeclarativeRectangleMapItemPrivate: a plain Python
  object standing in front of one C++ QDeclarativeRectangleMapItemPrivate.

  What exists
  -----------

  Every function of Qt's QDeclarativeRectangleMapItemPrivate that has a
  ritual and that Python can call so far, 9 names in all:
  'onLinePropertiesChanged', 'markSourceDirtyAndUpdate', 'onMapSet',
  'onGeoGeometryChanged', 'onItemGeometryChanged', 'updatePolish',
  'afterViewportChanged', 'updateMapItemPaintNode', 'contains'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDeclarativeRectangleMapItemPrivate::
    QDeclarativeRectangleMapItemPrivate(QDeclarativeRectangleMapItem &rect)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QDeclarativeRectangleMapItemPrivate::
    ~QDeclarativeRectangleMapItemPrivate()': the destructor: Python never
    removes a C++ QDeclarativeRectangleMapItemPrivate.

  What has no ritual
  ------------------

  4 of the 15 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QDeclarativeRectangleMapItemPrivate is created at the first use,
    not by 'QDeclarativeRectangleMapItemPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativeRectangleMapItemPrivate.
  - Each name of Qt's QDeclarativeRectangleMapItemPrivate that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativeRectangleMapItemPrivate'

  #  A C++ QDeclarativeRectangleMapItemPrivate Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativeRectangleMapItemPrivate'

  #  The functions Qt calls itself that QDeclarativeRectangleMapItemPrivate
  #  is the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'onLinePropertiesChanged': (
          ('_ZN35QDeclarativeRectangleMapItemPrivate23onLinePropertiesChang'
           'edEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'markSourceDirtyAndUpdate': (
          ('_ZN35QDeclarativeRectangleMapItemPrivate24markSourceDirtyAndUpd'
           'ateEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'onMapSet': (
          ('_ZN35QDeclarativeRectangleMapItemPrivate8onMapSetEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'onGeoGeometryChanged': (
          ('_ZN35QDeclarativeRectangleMapItemPrivate20onGeoGeometryChangedE'
           'v',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'onItemGeometryChanged': (
          ('_ZN35QDeclarativeRectangleMapItemPrivate21onItemGeometryChanged'
           'Ev',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'updatePolish': (
          ('_ZN35QDeclarativeRectangleMapItemPrivate12updatePolishEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'afterViewportChanged': (
          ('_ZN35QDeclarativeRectangleMapItemPrivate20afterViewportChangedE'
           'v',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'updateMapItemPaintNode': (
          ('_ZN35QDeclarativeRectangleMapItemPrivate22updateMapItemPaintNod'
           'eEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE',
           ('address', 'address', 'QtQuick:QSGNode'),
           (
               ('address', 'address', 'QtQuick:QSGNode'),
               ('address', 'address',
                'QtQuick:QQuickItem.UpdatePaintNodeData'),
           )),
      ),
      'contains': (
          ('_ZNK35QDeclarativeRectangleMapItemPrivate8containsERK7QPointF',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QPointF'),
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

  @overload(QPointF)
  def contains(self, point: QPointF) -> bool:
    """
    Calls Qt's 'bool QDeclarativeRectangleMapItemPrivate::contains(const
    QPointF &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativerectanglemapitemprivate.html#contains

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QDeclarativeRectangleMapItemPrivate::contains(const QPointF
    #      &point) const
    return self.uglySide.call(
        'ritual_ZNK35QDeclarativeRectangleMapItemPrivate8containsERK7QPoint'
        'F',
        self._valueOf(point, 'QPointF'),
    )

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
    Qt's 'QDeclarativeRectangleMapItemPrivate::
    QDeclarativeRectangleMapItemPrivate(QDeclarativeRectangleMapItem &rect)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDeclarativeRectangleMapItemPrivate.__init__' has no cute "
        "function yet. Qt's "
        "'QDeclarativeRectangleMapItemPrivate::QDeclarativeRectangleMapItemP"
        "rivate(QDeclarativeRectangleMapItem &rect)': takes a type Python "
        "has no way to hand over yet.")

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

  def onLinePropertiesChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeRectangleMapItemPrivate::onLinePropertiesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativerectanglemapitemprivate.html
    """
    #  void QDeclarativeRectangleMapItemPrivate::onLinePropertiesChanged()
    self.uglySide.call(
        'ritual_ZN35QDeclarativeRectangleMapItemPrivate23onLinePropertiesCh'
        'angedEv',
    )

  def markSourceDirtyAndUpdate(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeRectangleMapItemPrivate::markSourceDirtyAndUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativerectanglemapitemprivate.html
    """
    #  void QDeclarativeRectangleMapItemPrivate::markSourceDirtyAndUpdate()
    self.uglySide.call(
        'ritual_ZN35QDeclarativeRectangleMapItemPrivate24markSourceDirtyAnd'
        'UpdateEv',
    )

  def onMapSet(self) -> None:
    """
    Calls Qt's 'void QDeclarativeRectangleMapItemPrivate::onMapSet()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativerectanglemapitemprivate.html#onMapSet
    """
    #  void QDeclarativeRectangleMapItemPrivate::onMapSet()
    self.uglySide.call(
        'ritual_ZN35QDeclarativeRectangleMapItemPrivate8onMapSetEv',
    )

  def onGeoGeometryChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeRectangleMapItemPrivate::onGeoGeometryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativerectanglemapitemprivate.html
    """
    #  void QDeclarativeRectangleMapItemPrivate::onGeoGeometryChanged()
    self.uglySide.call(
        'ritual_ZN35QDeclarativeRectangleMapItemPrivate20onGeoGeometryChang'
        'edEv',
    )

  def onItemGeometryChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeRectangleMapItemPrivate::onItemGeometryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativerectanglemapitemprivate.html
    """
    #  void QDeclarativeRectangleMapItemPrivate::onItemGeometryChanged()
    self.uglySide.call(
        'ritual_ZN35QDeclarativeRectangleMapItemPrivate21onItemGeometryChan'
        'gedEv',
    )

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QDeclarativeRectangleMapItemPrivate::updatePolish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativerectanglemapitemprivate.html
    """
    #  void QDeclarativeRectangleMapItemPrivate::updatePolish()
    self.uglySide.call(
        'ritual_ZN35QDeclarativeRectangleMapItemPrivate12updatePolishEv',
    )

  def afterViewportChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativeRectangleMapItemPrivate::afterViewportChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativerectanglemapitemprivate.html
    """
    #  void QDeclarativeRectangleMapItemPrivate::afterViewportChanged()
    self.uglySide.call(
        'ritual_ZN35QDeclarativeRectangleMapItemPrivate20afterViewportChang'
        'edEv',
    )

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updateMapItemPaintNode(
      self,
      oldNode: Optional[QSGNode],
      data: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode
    *QDeclarativeRectangleMapItemPrivate::updateMapItemPaintNode(QSGNode
    *oldNode, QQuickItem::UpdatePaintNodeData *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativerectanglemapitemprivate.html

    Parameters
    ----------

    oldNode : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    data : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QDeclarativeRectangleMapItemPrivate::updateMapItemPaintNode(
    #      QSGNode *oldNode, QQuickItem::UpdatePaintNodeData *data)
    address = self.uglySide.call(
        'ritual_ZN35QDeclarativeRectangleMapItemPrivate22updateMapItemPaint'
        'NodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE',
        self._addressOf(oldNode, 'QSGNode'), self._addressOf(data),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)
