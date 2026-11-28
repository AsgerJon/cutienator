"""
QDeclarativePolygonMapItemPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativepolygonmapitem_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativePolygonMapItemPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
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


class QDeclarativePolygonMapItemPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDeclarativePolygonMapItemPrivate: a plain Python
  object standing in front of one C++ QDeclarativePolygonMapItemPrivate.

  What exists
  -----------

  Every function of Qt's QDeclarativePolygonMapItemPrivate that has a ritual
  and that Python can call so far, 10 names in all:
  'onLinePropertiesChanged', 'markSourceDirtyAndUpdate', 'onMapSet',
  'onGeoGeometryChanged', 'onGeoGeometryUpdated', 'onItemGeometryChanged',
  'updatePolish', 'afterViewportChanged', 'updateMapItemPaintNode',
  'contains'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QDeclarativePolygonMapItemPrivate::QDeclarativePolygonMapItemPrivate(
    QDeclarativePolygonMapItem &polygon)': takes a type Python has no way to
    hand over yet.
  - Qt's
    'QDeclarativePolygonMapItemPrivate::~QDeclarativePolygonMapItemPrivate(
    )': the destructor: Python never removes a C++
    QDeclarativePolygonMapItemPrivate.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QDeclarativePolygonMapItemPrivate is created at the first use,
    not by 'QDeclarativePolygonMapItemPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativePolygonMapItemPrivate.
  - Each name of Qt's QDeclarativePolygonMapItemPrivate that has no cute
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
  __qt_class__ = 'QDeclarativePolygonMapItemPrivate'

  #  A C++ QDeclarativePolygonMapItemPrivate Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativePolygonMapItemPrivate'

  #  The functions Qt calls itself that QDeclarativePolygonMapItemPrivate is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'onLinePropertiesChanged': (
          ('_ZN33QDeclarativePolygonMapItemPrivate23onLinePropertiesChanged'
           'Ev',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'markSourceDirtyAndUpdate': (
          ('_ZN33QDeclarativePolygonMapItemPrivate24markSourceDirtyAndUpdat'
           'eEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'onMapSet': (
          ('_ZN33QDeclarativePolygonMapItemPrivate8onMapSetEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'onGeoGeometryChanged': (
          ('_ZN33QDeclarativePolygonMapItemPrivate20onGeoGeometryChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'onGeoGeometryUpdated': (
          ('_ZN33QDeclarativePolygonMapItemPrivate20onGeoGeometryUpdatedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'onItemGeometryChanged': (
          ('_ZN33QDeclarativePolygonMapItemPrivate21onItemGeometryChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'updatePolish': (
          ('_ZN33QDeclarativePolygonMapItemPrivate12updatePolishEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'afterViewportChanged': (
          ('_ZN33QDeclarativePolygonMapItemPrivate20afterViewportChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'updateMapItemPaintNode': (
          ('_ZN33QDeclarativePolygonMapItemPrivate22updateMapItemPaintNodeE'
           'P7QSGNodePN10QQuickItem19UpdatePaintNodeDataE',
           ('address', 'address', 'QtQuick:QSGNode'),
           (
               ('address', 'address', 'QtQuick:QSGNode'),
               ('address', 'address',
                'QtQuick:QQuickItem.UpdatePaintNodeData'),
           )),
      ),
      'contains': (
          ('_ZNK33QDeclarativePolygonMapItemPrivate8containsERK7QPointF',
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
    Calls Qt's 'bool QDeclarativePolygonMapItemPrivate::contains(const
    QPointF &point) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitemprivate.html#contains

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QDeclarativePolygonMapItemPrivate::contains(const QPointF &point)
    #      const
    return self.uglySide.call(
        'ritual_ZNK33QDeclarativePolygonMapItemPrivate8containsERK7QPointF',
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
    Qt's
    'QDeclarativePolygonMapItemPrivate::QDeclarativePolygonMapItemPrivate(
    QDeclarativePolygonMapItem &polygon)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QDeclarativePolygonMapItemPrivate.__init__' has no cute function "
        "yet. Qt's "
        "'QDeclarativePolygonMapItemPrivate::QDeclarativePolygonMapItemPriva"
        "te(QDeclarativePolygonMapItem &polygon)': takes a type Python has "
        "no way to hand over yet.")

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
    QDeclarativePolygonMapItemPrivate::onLinePropertiesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitemprivate.html
    """
    #  void QDeclarativePolygonMapItemPrivate::onLinePropertiesChanged()
    self.uglySide.call(
        'ritual_ZN33QDeclarativePolygonMapItemPrivate23onLinePropertiesChan'
        'gedEv',
    )

  def markSourceDirtyAndUpdate(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativePolygonMapItemPrivate::markSourceDirtyAndUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitemprivate.html
    """
    #  void QDeclarativePolygonMapItemPrivate::markSourceDirtyAndUpdate()
    self.uglySide.call(
        'ritual_ZN33QDeclarativePolygonMapItemPrivate24markSourceDirtyAndUp'
        'dateEv',
    )

  def onMapSet(self) -> None:
    """
    Calls Qt's 'void QDeclarativePolygonMapItemPrivate::onMapSet()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitemprivate.html#onMapSet
    """
    #  void QDeclarativePolygonMapItemPrivate::onMapSet()
    self.uglySide.call(
        'ritual_ZN33QDeclarativePolygonMapItemPrivate8onMapSetEv',
    )

  def onGeoGeometryChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativePolygonMapItemPrivate::onGeoGeometryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitemprivate.html
    """
    #  void QDeclarativePolygonMapItemPrivate::onGeoGeometryChanged()
    self.uglySide.call(
        'ritual_ZN33QDeclarativePolygonMapItemPrivate20onGeoGeometryChanged'
        'Ev',
    )

  def onGeoGeometryUpdated(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativePolygonMapItemPrivate::onGeoGeometryUpdated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitemprivate.html
    """
    #  void QDeclarativePolygonMapItemPrivate::onGeoGeometryUpdated()
    self.uglySide.call(
        'ritual_ZN33QDeclarativePolygonMapItemPrivate20onGeoGeometryUpdated'
        'Ev',
    )

  def onItemGeometryChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativePolygonMapItemPrivate::onItemGeometryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitemprivate.html
    """
    #  void QDeclarativePolygonMapItemPrivate::onItemGeometryChanged()
    self.uglySide.call(
        'ritual_ZN33QDeclarativePolygonMapItemPrivate21onItemGeometryChange'
        'dEv',
    )

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QDeclarativePolygonMapItemPrivate::updatePolish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitemprivate.html
    """
    #  void QDeclarativePolygonMapItemPrivate::updatePolish()
    self.uglySide.call(
        'ritual_ZN33QDeclarativePolygonMapItemPrivate12updatePolishEv',
    )

  def afterViewportChanged(self) -> None:
    """
    Calls Qt's 'void
    QDeclarativePolygonMapItemPrivate::afterViewportChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitemprivate.html
    """
    #  void QDeclarativePolygonMapItemPrivate::afterViewportChanged()
    self.uglySide.call(
        'ritual_ZN33QDeclarativePolygonMapItemPrivate20afterViewportChanged'
        'Ev',
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
    *QDeclarativePolygonMapItemPrivate::updateMapItemPaintNode(QSGNode
    *oldNode, QQuickItem::UpdatePaintNodeData *data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativepolygonmapitemprivate.html

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
    #  QSGNode
    #      *QDeclarativePolygonMapItemPrivate::updateMapItemPaintNode(QSGNode
    #      *oldNode, QQuickItem::UpdatePaintNodeData *data)
    address = self.uglySide.call(
        'ritual_ZN33QDeclarativePolygonMapItemPrivate22updateMapItemPaintNo'
        'deEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE',
        self._addressOf(oldNode, 'QSGNode'), self._addressOf(data),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)
