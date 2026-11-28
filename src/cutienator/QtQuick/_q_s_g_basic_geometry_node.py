"""
QSGBasicGeometryNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qsgnode.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSGNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QMatrix4x4
  from . import QSGClipNode, QSGGeometry
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QSGClipNode = WAIT['QSGClipNode']
  QSGGeometry = WAIT['QSGGeometry']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGBasicGeometryNode(QSGNode):
  """
  The cute side of Qt's QSGBasicGeometryNode: a plain Python object standing
  in front of one C++ QSGBasicGeometryNode.

  It is built on the cute 'QSGNode', as Qt's QSGBasicGeometryNode is built on
  Qt's QSGNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGBasicGeometryNode that has a ritual and that
  Python can call so far, 6 names in all: 'setGeometry', 'geometry',
  'matrix', 'clipList', 'setRendererMatrix', 'setRendererClipList'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGBasicGeometryNode::~QSGBasicGeometryNode()': the destructor:
    Python never removes a C++ QSGBasicGeometryNode.
  - Qt's 'QSGGeometry *QSGBasicGeometryNode::geometry()': takes in Python
    what 'const QSGGeometry *QSGBasicGeometryNode::geometry() const' takes.
  - Qt's
    'QSGBasicGeometryNode::QSGBasicGeometryNode(QSGBasicGeometryNodePrivate
    &dd, NodeType type)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSGBasicGeometryNode is created at the first use, not by
    'QSGBasicGeometryNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGBasicGeometryNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGBasicGeometryNode'

  #  A C++ QSGBasicGeometryNode Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGBasicGeometryNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def geometry(self) -> Optional[QSGGeometry]:
    """
    Calls Qt's 'const QSGGeometry *QSGBasicGeometryNode::geometry() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgbasicgeometrynode.html#geometry

    Returns
    -------

    Optional[QSGGeometry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QSGGeometry *QSGBasicGeometryNode::geometry() const
    address = self._callAs(
        'QSGBasicGeometryNode',
        'ritual_ZNK20QSGBasicGeometryNode8geometryEv',
    )
    from . import QSGGeometry
    return QSGGeometry._cuteAt(address)

  def matrix(self) -> Optional[QMatrix4x4]:
    """
    Calls Qt's 'const QMatrix4x4 *QSGBasicGeometryNode::matrix() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgbasicgeometrynode.html#matrix

    Returns
    -------

    Optional[QMatrix4x4]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMatrix4x4 *QSGBasicGeometryNode::matrix() const
    address = self._callAs(
        'QSGBasicGeometryNode', 'ritual_ZNK20QSGBasicGeometryNode6matrixEv',
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteAt(address)

  def clipList(self) -> Optional[QSGClipNode]:
    """
    Calls Qt's 'const QSGClipNode *QSGBasicGeometryNode::clipList() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgbasicgeometrynode.html#clipList

    Returns
    -------

    Optional[QSGClipNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QSGClipNode *QSGBasicGeometryNode::clipList() const
    address = self._callAs(
        'QSGBasicGeometryNode',
        'ritual_ZNK20QSGBasicGeometryNode8clipListEv',
    )
    from . import QSGClipNode
    return QSGClipNode._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSGGeometry)
  @overload(NoneType)
  def setGeometry(self, geometry: Optional[QSGGeometry]) -> None:
    """
    Calls Qt's 'void QSGBasicGeometryNode::setGeometry(QSGGeometry
    *geometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicgeometrynode.html#setGeometry

    Parameters
    ----------

    geometry : Optional[QSGGeometry]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGBasicGeometryNode::setGeometry(QSGGeometry *geometry)
    self._callAs(
        'QSGBasicGeometryNode',
        'ritual_ZN20QSGBasicGeometryNode11setGeometryEP11QSGGeometry',
        self._addressOf(geometry),
    )

  @overload(QMatrix4x4)
  @overload(NoneType)
  def setRendererMatrix(self, m: Optional[QMatrix4x4]) -> None:
    """
    Calls Qt's 'void QSGBasicGeometryNode::setRendererMatrix(const QMatrix4x4
    *m)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicgeometrynode.html#setRendererMatrix

    Parameters
    ----------

    m : Optional[QMatrix4x4]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGBasicGeometryNode::setRendererMatrix(const QMatrix4x4 *m)
    self._callAs(
        'QSGBasicGeometryNode',
        'ritual_ZN20QSGBasicGeometryNode17setRendererMatrixEPK10QMatrix4x4',
        self._addressOf(m),
    )

  @overload(QSGClipNode)
  @overload(NoneType)
  def setRendererClipList(self, c: Optional[QSGClipNode]) -> None:
    """
    Calls Qt's 'void QSGBasicGeometryNode::setRendererClipList(const
    QSGClipNode *c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicgeometrynode.html#setRendererClipList

    Parameters
    ----------

    c : Optional[QSGClipNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGBasicGeometryNode::setRendererClipList(const QSGClipNode *c)
    self._callAs(
        'QSGBasicGeometryNode',
        'ritual_ZN20QSGBasicGeometryNode19setRendererClipListEPK11QSGClipNo'
        'de',
        self._addressOf(c),
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

  @overload(QSGNode.NodeType)
  def __init__(self, type: QSGNode.NodeType) -> None:
    """
    Notes what was given, for Qt's
    'QSGBasicGeometryNode::QSGBasicGeometryNode(NodeType type)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgbasicgeometrynode.html#QSGBasicGeometryNode

    Parameters
    ----------

    type : QSGNode.NodeType
      Passed on as its number.
    """
    #  QSGBasicGeometryNode::QSGBasicGeometryNode(NodeType type)
    self._noteCreation(QSGBasicGeometryNode, lambda: Rituals.call(
        'ritual_ZN20QSGBasicGeometryNodeC1EN7QSGNode8NodeTypeE', type.value,
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
