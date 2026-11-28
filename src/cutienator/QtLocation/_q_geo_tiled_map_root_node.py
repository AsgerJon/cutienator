"""
QGeoTiledMapRootNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeotiledmapscene_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoTiledMapRootNode to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtQuick import QSGClipNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QRect
  from ..QtQuick import QQuickWindow
  from . import QGeoTiledMapScenePrivate, QGeoTiledMapTileContainerNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoTiledMapScenePrivate = WAIT['QGeoTiledMapScenePrivate']
  QGeoTiledMapTileContainerNode = WAIT['QGeoTiledMapTileContainerNode']
  QQuickWindow = WAIT['QQuickWindow']
  QRect = WAIT['QRect']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoTiledMapRootNode(QSGClipNode):
  """
  The cute side of Qt's QGeoTiledMapRootNode: a plain Python object standing
  in front of one C++ QGeoTiledMapRootNode.

  It is built on the cute 'QSGClipNode', as Qt's QGeoTiledMapRootNode is
  built on Qt's QSGClipNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoTiledMapRootNode that has a ritual and that
  Python can call so far, 2 names in all: 'setClipRect', 'updateTiles'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGeoTiledMapRootNode::~QGeoTiledMapRootNode()': the destructor:
    Python never removes a C++ QGeoTiledMapRootNode.

  What to expect
  --------------

  - The C++ QGeoTiledMapRootNode is created at the first use, not by
    'QGeoTiledMapRootNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoTiledMapRootNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoTiledMapRootNode'

  #  A C++ QGeoTiledMapRootNode Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoTiledMapRootNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRect)
  def setClipRect(self, rect: QRect) -> None:
    """
    Calls Qt's 'void QGeoTiledMapRootNode::setClipRect(const QRect &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmaprootnode.html#setClipRect

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QGeoTiledMapRootNode::setClipRect(const QRect &rect)
    self.uglySide.call(
        'ritual_ZN20QGeoTiledMapRootNode11setClipRectERK5QRect',
        self._valueOf(rect),
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
    'QGeoTiledMapRootNode::QGeoTiledMapRootNode()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmaprootnode.html#QGeoTiledMapRootNode
    """
    #  QGeoTiledMapRootNode::QGeoTiledMapRootNode()
    self._noteCreation(QGeoTiledMapRootNode, lambda: Rituals.call(
        'ritual_ZN20QGeoTiledMapRootNodeC1Ev',
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

  @overload(
      QGeoTiledMapTileContainerNode, QGeoTiledMapScenePrivate, float,
      QQuickWindow,
  )
  @overload(
      QGeoTiledMapTileContainerNode, QGeoTiledMapScenePrivate, float,
      NoneType,
  )
  @overload(QGeoTiledMapTileContainerNode, NoneType, float, QQuickWindow)
  @overload(QGeoTiledMapTileContainerNode, NoneType, float, NoneType)
  @overload(NoneType, QGeoTiledMapScenePrivate, float, QQuickWindow)
  @overload(NoneType, QGeoTiledMapScenePrivate, float, NoneType)
  @overload(NoneType, NoneType, float, QQuickWindow)
  @overload(NoneType, NoneType, float, NoneType)
  def updateTiles(
      self,
      root: Optional[QGeoTiledMapTileContainerNode],
      d: Optional[QGeoTiledMapScenePrivate],
      camAdjust: float,
      window: Optional[QQuickWindow],
  ) -> None:
    """
    Calls Qt's 'void
    QGeoTiledMapRootNode::updateTiles(QGeoTiledMapTileContainerNode *root,
    QGeoTiledMapScenePrivate *d, double camAdjust, QQuickWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmaprootnode.html#updateTiles

    Parameters
    ----------

    root : Optional[QGeoTiledMapTileContainerNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    d : Optional[QGeoTiledMapScenePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    camAdjust : float
      Passed on as it is.

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGeoTiledMapRootNode::updateTiles(QGeoTiledMapTileContainerNode
    #      *root, QGeoTiledMapScenePrivate *d, double camAdjust, QQuickWindow
    #      *window)
    self.uglySide.call(
        'ritual_ZN20QGeoTiledMapRootNode11updateTilesEP29QGeoTiledMapTileCo'
        'ntainerNodeP24QGeoTiledMapScenePrivatedP12QQuickWindow',
        self._addressOf(root), self._addressOf(d), camAdjust,
        self._addressOf(window),
    )
