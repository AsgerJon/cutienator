"""
QSGGeometryNode binding of the Qt C++
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
from . import QSGBasicGeometryNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSGMaterial
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSGMaterial = WAIT['QSGMaterial']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGGeometryNode(QSGBasicGeometryNode):
  """
  The cute side of Qt's QSGGeometryNode: a plain Python object standing in
  front of one C++ QSGGeometryNode.

  It is built on the cute 'QSGBasicGeometryNode', as Qt's QSGGeometryNode is
  built on Qt's QSGBasicGeometryNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGGeometryNode that has a ritual and that Python
  can call so far, 9 names in all: 'setMaterial', 'material',
  'setOpaqueMaterial', 'opaqueMaterial', 'activeMaterial', 'setRenderOrder',
  'renderOrder', 'setInheritedOpacity', 'inheritedOpacity'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGGeometryNode::~QSGGeometryNode()': the destructor: Python never
    removes a C++ QSGGeometryNode.
  - Qt's 'QSGGeometryNode::QSGGeometryNode(QSGGeometryNodePrivate &dd)':
    takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSGGeometryNode is created at the first use, not by
    'QSGGeometryNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGGeometryNode.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGGeometryNode'

  #  A C++ QSGGeometryNode Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGGeometryNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def material(self) -> Optional[QSGMaterial]:
    """
    Calls Qt's 'QSGMaterial *QSGGeometryNode::material() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsggeometrynode.html#material

    Returns
    -------

    Optional[QSGMaterial]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterial *QSGGeometryNode::material() const
    address = self._callAs(
        'QSGGeometryNode', 'ritual_ZNK15QSGGeometryNode8materialEv',
    )
    from . import QSGMaterial
    return QSGMaterial._cuteAt(address)

  def opaqueMaterial(self) -> Optional[QSGMaterial]:
    """
    Calls Qt's 'QSGMaterial *QSGGeometryNode::opaqueMaterial() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsggeometrynode.html#opaqueMaterial

    Returns
    -------

    Optional[QSGMaterial]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterial *QSGGeometryNode::opaqueMaterial() const
    address = self._callAs(
        'QSGGeometryNode', 'ritual_ZNK15QSGGeometryNode14opaqueMaterialEv',
    )
    from . import QSGMaterial
    return QSGMaterial._cuteAt(address)

  def activeMaterial(self) -> Optional[QSGMaterial]:
    """
    Calls Qt's 'QSGMaterial *QSGGeometryNode::activeMaterial() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsggeometrynode.html#activeMaterial

    Returns
    -------

    Optional[QSGMaterial]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterial *QSGGeometryNode::activeMaterial() const
    address = self._callAs(
        'QSGGeometryNode', 'ritual_ZNK15QSGGeometryNode14activeMaterialEv',
    )
    from . import QSGMaterial
    return QSGMaterial._cuteAt(address)

  def renderOrder(self) -> int:
    """
    Calls Qt's 'int QSGGeometryNode::renderOrder() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsggeometrynode.html#renderOrder
    """
    #  int QSGGeometryNode::renderOrder() const
    return self._callAs(
        'QSGGeometryNode', 'ritual_ZNK15QSGGeometryNode11renderOrderEv',
    )

  def inheritedOpacity(self) -> float:
    """
    Calls Qt's 'qreal QSGGeometryNode::inheritedOpacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsggeometrynode.html#inheritedOpacity
    """
    #  qreal QSGGeometryNode::inheritedOpacity() const
    return self._callAs(
        'QSGGeometryNode', 'ritual_ZNK15QSGGeometryNode16inheritedOpacityEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSGMaterial)
  @overload(NoneType)
  def setMaterial(self, material: Optional[QSGMaterial]) -> None:
    """
    Calls Qt's 'void QSGGeometryNode::setMaterial(QSGMaterial *material)'.

    Qt's own words: https://doc.qt.io/qt-6/qsggeometrynode.html#setMaterial

    Parameters
    ----------

    material : Optional[QSGMaterial]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGGeometryNode::setMaterial(QSGMaterial *material)
    self._callAs(
        'QSGGeometryNode',
        'ritual_ZN15QSGGeometryNode11setMaterialEP11QSGMaterial',
        self._addressOf(material),
    )

  @overload(QSGMaterial)
  @overload(NoneType)
  def setOpaqueMaterial(self, material: Optional[QSGMaterial]) -> None:
    """
    Calls Qt's 'void QSGGeometryNode::setOpaqueMaterial(QSGMaterial
    *material)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsggeometrynode.html#setOpaqueMaterial

    Parameters
    ----------

    material : Optional[QSGMaterial]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGGeometryNode::setOpaqueMaterial(QSGMaterial *material)
    self._callAs(
        'QSGGeometryNode',
        'ritual_ZN15QSGGeometryNode17setOpaqueMaterialEP11QSGMaterial',
        self._addressOf(material),
    )

  @overload(int)
  def setRenderOrder(self, order: int) -> None:
    """
    Calls Qt's 'void QSGGeometryNode::setRenderOrder(int order)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsggeometrynode.html#setRenderOrder

    Parameters
    ----------

    order : int
      Passed on as it is.
    """
    #  void QSGGeometryNode::setRenderOrder(int order)
    self._callAs(
        'QSGGeometryNode', 'ritual_ZN15QSGGeometryNode14setRenderOrderEi',
        order,
    )

  @overload(float)
  def setInheritedOpacity(self, opacity: float) -> None:
    """
    Calls Qt's 'void QSGGeometryNode::setInheritedOpacity(qreal opacity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsggeometrynode.html#setInheritedOpacity

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  void QSGGeometryNode::setInheritedOpacity(qreal opacity)
    self._callAs(
        'QSGGeometryNode',
        'ritual_ZN15QSGGeometryNode19setInheritedOpacityEd',
        opacity,
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
    Notes what was given, for Qt's 'QSGGeometryNode::QSGGeometryNode()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsggeometrynode.html#QSGGeometryNode
    """
    #  QSGGeometryNode::QSGGeometryNode()
    self._noteCreation(QSGGeometryNode, lambda: Rituals.call(
        'ritual_ZN15QSGGeometryNodeC1Ev',
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
