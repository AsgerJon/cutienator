"""
QGeoTiledMapTileContainerNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qgeotiledmapscene_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGeoTiledMapTileContainerNode to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtQuick import QSGTransformNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtQuick import QSGImageNode
  from . import QGeoTileSpec
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoTileSpec = WAIT['QGeoTileSpec']
  QSGImageNode = WAIT['QSGImageNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeoTiledMapTileContainerNode(QSGTransformNode):
  """
  The cute side of Qt's QGeoTiledMapTileContainerNode: a plain Python object
  standing in front of one C++ QGeoTiledMapTileContainerNode.

  It is built on the cute 'QSGTransformNode', as Qt's
  QGeoTiledMapTileContainerNode is built on Qt's QSGTransformNode, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGeoTiledMapTileContainerNode that has a ritual and
  that Python can call so far, 1 name in all: 'addChild'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What to expect
  --------------

  - The C++ QGeoTiledMapTileContainerNode is created at the first use, not by
    'QGeoTiledMapTileContainerNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGeoTiledMapTileContainerNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGeoTiledMapTileContainerNode'

  #  A C++ QGeoTiledMapTileContainerNode Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGeoTiledMapTileContainerNode'

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload(QGeoTileSpec, QSGImageNode)
  @overload(QGeoTileSpec, NoneType)
  def addChild(
      self,
      spec: QGeoTileSpec,
      node: Optional[QSGImageNode],
  ) -> None:
    """
    Calls Qt's 'void QGeoTiledMapTileContainerNode::addChild(const
    QGeoTileSpec &spec, QSGImageNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgeotiledmaptilecontainernode.html#addChild

    Parameters
    ----------

    spec : QGeoTileSpec
      Passed on as a value: Qt reads the C++ QGeoTileSpec, which stays
      Python's own.

    node : Optional[QSGImageNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGeoTiledMapTileContainerNode::addChild(const QGeoTileSpec &spec,
    #      QSGImageNode *node)
    self.uglySide.call(
        'ritual_ZN29QGeoTiledMapTileContainerNode8addChildERK12QGeoTileSpec'
        'P12QSGImageNode',
        self._valueOf(spec), self._addressOf(node),
    )
