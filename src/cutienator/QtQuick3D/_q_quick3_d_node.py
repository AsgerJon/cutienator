"""
QQuick3DNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dnode_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuick3DNode to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QQuick3DObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaMethod, QMetaObject
  from ..QtGui import QMatrix4x4, QQuaternion, QVector3D
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
  from . import QQuick3DNodePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaMethod = WAIT['QMetaMethod']
  QQuaternion = WAIT['QQuaternion']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DNode(QQuick3DObject):
  """
  The cute side of Qt's QQuick3DNode: a plain Python object standing in front
  of one C++ QQuick3DNode.

  It is built on the cute 'QQuick3DObject', as Qt's QQuick3DNode is built on
  Qt's QQuick3DObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DNode that has a ritual and that Python can
  call so far, 69 names in all: 'metaObject', 'tr', 'x', 'y', 'z',
  'rotation', 'eulerRotation', 'position', 'scale', 'pivot', 'localOpacity',
  'visible', 'staticFlags', 'parentNode', 'forward', 'up', 'right',
  'scenePosition', 'sceneRotation', 'sceneScale', 'sceneTransform', 'rotate',
  'mapPositionToScene', 'mapPositionFromScene', 'mapPositionToNode',
  'mapPositionFromNode', 'mapDirectionToScene', 'mapDirectionFromScene',
  'mapDirectionToNode', 'mapDirectionFromNode', 'markAllDirty', 'layers',
  'connectNotify', 'disconnectNotify', 'componentComplete', 'setX', 'setY',
  'setZ', 'setRotation', 'setEulerRotation', 'setPosition', 'setScale',
  'setPivot', 'setLocalOpacity', 'setVisible', 'setStaticFlags', 'setLayers',
  'xChanged', 'yChanged', 'zChanged', 'rotationChanged',
  'eulerRotationChanged', 'positionChanged', 'scaleChanged', 'pivotChanged',
  'localOpacityChanged', 'visibleChanged', 'forwardChanged', 'upChanged',
  'rightChanged', 'sceneTransformChanged', 'scenePositionChanged',
  'sceneRotationChanged', 'sceneScaleChanged', 'staticFlagsChanged',
  'layersChanged', 'updateSpatialNode', 'itemChange', 'd_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DNode::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuick3DNode::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DNode::~QQuick3DNode()': the destructor: Python never
    removes a C++ QQuick3DNode.
  - Qt's 'QQuick3DNode::QQuick3DNode(QQuick3DNodePrivate &dd, QQuick3DNode
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QQuick3DNodePrivate *QQuick3DNode::d_func() const': takes in
    Python what 'QQuick3DNodePrivate *QQuick3DNode::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 79 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuick3DNode is created at the first use, not by
    'QQuick3DNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DNode.
  - Qt tells when it has removed the C++ QQuick3DNode. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuick3DNode, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class StaticFlags(CuteNum):
    """
    The enum 'QQuick3DNode::StaticFlags' of Qt, with the 1 names Qt gives in
    it.
    """

    NULL = Kee[int](0)

  class TransformSpace(CuteNum):
    """
    The enum 'QQuick3DNode::TransformSpace' of Qt, with the 3 names Qt gives
    in it.
    """

    LocalSpace = Kee[int](0)
    ParentSpace = Kee[int](1)
    SceneSpace = Kee[int](2)

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
    Calls Qt's 'QString QQuick3DNode::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#tr

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
    #  QString QQuick3DNode::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QQuick3DNode2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DNode'

  #  A C++ QQuick3DNode Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DNode::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DNode::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QQuick3DNode10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def x(self) -> float:
    """
    Calls Qt's 'float QQuick3DNode::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#x
    """
    #  float QQuick3DNode::x() const
    return self.uglySide.call('ritual_ZNK12QQuick3DNode1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'float QQuick3DNode::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#y
    """
    #  float QQuick3DNode::y() const
    return self.uglySide.call('ritual_ZNK12QQuick3DNode1yEv')

  def z(self) -> float:
    """
    Calls Qt's 'float QQuick3DNode::z() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#z
    """
    #  float QQuick3DNode::z() const
    return self.uglySide.call('ritual_ZNK12QQuick3DNode1zEv')

  def rotation(self) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuick3DNode::rotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#rotation

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuick3DNode::rotation() const
    address = self.uglySide.call('ritual_ZNK12QQuick3DNode8rotationEv')
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  def eulerRotation(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DNode::eulerRotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#eulerRotation

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DNode::eulerRotation() const
    address = self.uglySide.call('ritual_ZNK12QQuick3DNode13eulerRotationEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def position(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DNode::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#position

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DNode::position() const
    address = self.uglySide.call('ritual_ZNK12QQuick3DNode8positionEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def scale(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DNode::scale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#scale

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DNode::scale() const
    address = self.uglySide.call('ritual_ZNK12QQuick3DNode5scaleEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def pivot(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DNode::pivot() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#pivot

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DNode::pivot() const
    address = self.uglySide.call('ritual_ZNK12QQuick3DNode5pivotEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def localOpacity(self) -> float:
    """
    Calls Qt's 'float QQuick3DNode::localOpacity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#localOpacity
    """
    #  float QQuick3DNode::localOpacity() const
    return self.uglySide.call('ritual_ZNK12QQuick3DNode12localOpacityEv')

  def visible(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DNode::visible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#visible
    """
    #  bool QQuick3DNode::visible() const
    return self.uglySide.call('ritual_ZNK12QQuick3DNode7visibleEv')

  def staticFlags(self) -> int:
    """
    Calls Qt's 'int QQuick3DNode::staticFlags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#staticFlags
    """
    #  int QQuick3DNode::staticFlags() const
    return self.uglySide.call('ritual_ZNK12QQuick3DNode11staticFlagsEv')

  def parentNode(self) -> Optional[QQuick3DNode]:
    """
    Calls Qt's 'QQuick3DNode *QQuick3DNode::parentNode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#parentNode

    Returns
    -------

    Optional[QQuick3DNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DNode *QQuick3DNode::parentNode() const
    address = self.uglySide.call('ritual_ZNK12QQuick3DNode10parentNodeEv')
    return QQuick3DNode._cuteAt(address)

  def forward(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DNode::forward() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#forward

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DNode::forward() const
    address = self.uglySide.call('ritual_ZNK12QQuick3DNode7forwardEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def up(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DNode::up() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#up

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DNode::up() const
    address = self.uglySide.call('ritual_ZNK12QQuick3DNode2upEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def right(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DNode::right() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#right

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DNode::right() const
    address = self.uglySide.call('ritual_ZNK12QQuick3DNode5rightEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def scenePosition(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DNode::scenePosition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#scenePosition

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DNode::scenePosition() const
    address = self.uglySide.call('ritual_ZNK12QQuick3DNode13scenePositionEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def sceneRotation(self) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuick3DNode::sceneRotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#sceneRotation

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuick3DNode::sceneRotation() const
    address = self.uglySide.call('ritual_ZNK12QQuick3DNode13sceneRotationEv')
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  def sceneScale(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DNode::sceneScale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#sceneScale

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DNode::sceneScale() const
    address = self.uglySide.call('ritual_ZNK12QQuick3DNode10sceneScaleEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def sceneTransform(self) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 QQuick3DNode::sceneTransform() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#sceneTransform

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QQuick3DNode::sceneTransform() const
    address = self.uglySide.call(
        'ritual_ZNK12QQuick3DNode14sceneTransformEv',
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  @overload(QVector3D)
  def mapPositionToScene(self, localPosition: QVector3D) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DNode::mapPositionToScene(const QVector3D
    &localPosition) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dnode.html#mapPositionToScene

    Parameters
    ----------

    localPosition : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DNode::mapPositionToScene(const QVector3D
    #      &localPosition) const
    address = self.uglySide.call(
        'ritual_ZNK12QQuick3DNode18mapPositionToSceneERK9QVector3D',
        self._valueOf(localPosition),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(QVector3D)
  def mapPositionFromScene(self, scenePosition: QVector3D) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DNode::mapPositionFromScene(const QVector3D
    &scenePosition) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dnode.html#mapPositionFromScene

    Parameters
    ----------

    scenePosition : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DNode::mapPositionFromScene(const QVector3D
    #      &scenePosition) const
    address = self.uglySide.call(
        'ritual_ZNK12QQuick3DNode20mapPositionFromSceneERK9QVector3D',
        self._valueOf(scenePosition),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(THIS, QVector3D)
  @overload(NoneType, QVector3D)
  def mapPositionToNode(
      self,
      node: Optional[QQuick3DNode],
      localPosition: QVector3D,
  ) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DNode::mapPositionToNode(const QQuick3DNode
    *node, const QVector3D &localPosition) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dnode.html#mapPositionToNode

    Parameters
    ----------

    node : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    localPosition : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DNode::mapPositionToNode(const QQuick3DNode *node,
    #      const QVector3D &localPosition) const
    address = self.uglySide.call(
        'ritual_ZNK12QQuick3DNode17mapPositionToNodeEPKS_RK9QVector3D',
        self._addressOf(node), self._valueOf(localPosition),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(THIS, QVector3D)
  @overload(NoneType, QVector3D)
  def mapPositionFromNode(
      self,
      node: Optional[QQuick3DNode],
      localPosition: QVector3D,
  ) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DNode::mapPositionFromNode(const
    QQuick3DNode *node, const QVector3D &localPosition) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dnode.html#mapPositionFromNode

    Parameters
    ----------

    node : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    localPosition : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DNode::mapPositionFromNode(const QQuick3DNode *node,
    #      const QVector3D &localPosition) const
    address = self.uglySide.call(
        'ritual_ZNK12QQuick3DNode19mapPositionFromNodeEPKS_RK9QVector3D',
        self._addressOf(node), self._valueOf(localPosition),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(QVector3D)
  def mapDirectionToScene(self, localDirection: QVector3D) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DNode::mapDirectionToScene(const QVector3D
    &localDirection) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dnode.html#mapDirectionToScene

    Parameters
    ----------

    localDirection : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DNode::mapDirectionToScene(const QVector3D
    #      &localDirection) const
    address = self.uglySide.call(
        'ritual_ZNK12QQuick3DNode19mapDirectionToSceneERK9QVector3D',
        self._valueOf(localDirection),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(QVector3D)
  def mapDirectionFromScene(self, sceneDirection: QVector3D) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DNode::mapDirectionFromScene(const QVector3D
    &sceneDirection) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dnode.html#mapDirectionFromScene

    Parameters
    ----------

    sceneDirection : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DNode::mapDirectionFromScene(const QVector3D
    #      &sceneDirection) const
    address = self.uglySide.call(
        'ritual_ZNK12QQuick3DNode21mapDirectionFromSceneERK9QVector3D',
        self._valueOf(sceneDirection),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(THIS, QVector3D)
  @overload(NoneType, QVector3D)
  def mapDirectionToNode(
      self,
      node: Optional[QQuick3DNode],
      localDirection: QVector3D,
  ) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DNode::mapDirectionToNode(const QQuick3DNode
    *node, const QVector3D &localDirection) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dnode.html#mapDirectionToNode

    Parameters
    ----------

    node : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    localDirection : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DNode::mapDirectionToNode(const QQuick3DNode *node,
    #      const QVector3D &localDirection) const
    address = self.uglySide.call(
        'ritual_ZNK12QQuick3DNode18mapDirectionToNodeEPKS_RK9QVector3D',
        self._addressOf(node), self._valueOf(localDirection),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(THIS, QVector3D)
  @overload(NoneType, QVector3D)
  def mapDirectionFromNode(
      self,
      node: Optional[QQuick3DNode],
      localDirection: QVector3D,
  ) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DNode::mapDirectionFromNode(const
    QQuick3DNode *node, const QVector3D &localDirection) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dnode.html#mapDirectionFromNode

    Parameters
    ----------

    node : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    localDirection : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DNode::mapDirectionFromNode(const QQuick3DNode *node,
    #      const QVector3D &localDirection) const
    address = self.uglySide.call(
        'ritual_ZNK12QQuick3DNode20mapDirectionFromNodeEPKS_RK9QVector3D',
        self._addressOf(node), self._valueOf(localDirection),
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def layers(self) -> int:
    """
    Calls Qt's 'int QQuick3DNode::layers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#layers
    """
    #  int QQuick3DNode::layers() const
    return self.uglySide.call('ritual_ZNK12QQuick3DNode6layersEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setX(self, x: float) -> None:
    """
    Calls Qt's 'void QQuick3DNode::setX(float x)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#setX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QQuick3DNode::setX(float x)
    self.uglySide.call('ritual_ZN12QQuick3DNode4setXEf', x)

  @overload(float)
  def setY(self, y: float) -> None:
    """
    Calls Qt's 'void QQuick3DNode::setY(float y)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#setY

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QQuick3DNode::setY(float y)
    self.uglySide.call('ritual_ZN12QQuick3DNode4setYEf', y)

  @overload(float)
  def setZ(self, z: float) -> None:
    """
    Calls Qt's 'void QQuick3DNode::setZ(float z)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#setZ

    Parameters
    ----------

    z : float
      Passed on as it is.
    """
    #  void QQuick3DNode::setZ(float z)
    self.uglySide.call('ritual_ZN12QQuick3DNode4setZEf', z)

  @overload(QQuaternion)
  def setRotation(self, rotation: QQuaternion) -> None:
    """
    Calls Qt's 'void QQuick3DNode::setRotation(const QQuaternion &rotation)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#setRotation

    Parameters
    ----------

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void QQuick3DNode::setRotation(const QQuaternion &rotation)
    self.uglySide.call(
        'ritual_ZN12QQuick3DNode11setRotationERK11QQuaternion',
        self._valueOf(rotation),
    )

  @overload(QVector3D)
  def setEulerRotation(self, eulerRotation: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DNode::setEulerRotation(const QVector3D
    &eulerRotation)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#setEulerRotation

    Parameters
    ----------

    eulerRotation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DNode::setEulerRotation(const QVector3D &eulerRotation)
    self.uglySide.call(
        'ritual_ZN12QQuick3DNode16setEulerRotationERK9QVector3D',
        self._valueOf(eulerRotation),
    )

  @overload(QVector3D)
  def setPosition(self, position: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DNode::setPosition(const QVector3D &position)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#setPosition

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DNode::setPosition(const QVector3D &position)
    self.uglySide.call(
        'ritual_ZN12QQuick3DNode11setPositionERK9QVector3D',
        self._valueOf(position),
    )

  @overload(QVector3D)
  def setScale(self, scale: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DNode::setScale(const QVector3D &scale)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#setScale

    Parameters
    ----------

    scale : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DNode::setScale(const QVector3D &scale)
    self.uglySide.call(
        'ritual_ZN12QQuick3DNode8setScaleERK9QVector3D',
        self._valueOf(scale),
    )

  @overload(QVector3D)
  def setPivot(self, pivot: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DNode::setPivot(const QVector3D &pivot)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#setPivot

    Parameters
    ----------

    pivot : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DNode::setPivot(const QVector3D &pivot)
    self.uglySide.call(
        'ritual_ZN12QQuick3DNode8setPivotERK9QVector3D',
        self._valueOf(pivot),
    )

  @overload(float)
  def setLocalOpacity(self, opacity: float) -> None:
    """
    Calls Qt's 'void QQuick3DNode::setLocalOpacity(float opacity)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#setLocalOpacity

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  void QQuick3DNode::setLocalOpacity(float opacity)
    self.uglySide.call('ritual_ZN12QQuick3DNode15setLocalOpacityEf', opacity)

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QQuick3DNode::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QQuick3DNode::setVisible(bool visible)
    self.uglySide.call('ritual_ZN12QQuick3DNode10setVisibleEb', visible)

  @overload(int)
  def setStaticFlags(self, staticFlags: int) -> None:
    """
    Calls Qt's 'void QQuick3DNode::setStaticFlags(int staticFlags)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#setStaticFlags

    Parameters
    ----------

    staticFlags : int
      Passed on as it is.
    """
    #  void QQuick3DNode::setStaticFlags(int staticFlags)
    self.uglySide.call(
        'ritual_ZN12QQuick3DNode14setStaticFlagsEi', staticFlags,
    )

  @overload(int)
  def setLayers(self, newLayers: int) -> None:
    """
    Calls Qt's 'void QQuick3DNode::setLayers(int newLayers)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#setLayers

    Parameters
    ----------

    newLayers : int
      Passed on as it is.
    """
    #  void QQuick3DNode::setLayers(int newLayers)
    self.uglySide.call('ritual_ZN12QQuick3DNode9setLayersEi', newLayers)

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
  @overload(THIS)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DNode] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuick3DNode::QQuick3DNode(QQuick3DNode
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#QQuick3DNode

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DNode::QQuick3DNode(QQuick3DNode *parent)
    self._noteCreation(QQuick3DNode, lambda: Rituals.call(
        'ritual_ZN12QQuick3DNodeC1EPS_', self._addressOf(parent),
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

  @overload(float, QVector3D, TransformSpace)
  def rotate(
      self,
      degrees: float,
      axis: QVector3D,
      space: TransformSpace,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DNode::rotate(qreal degrees, const QVector3D
    &axis, QQuick3DNode::TransformSpace space)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#rotate

    Parameters
    ----------

    degrees : float
      Passed on as it is.

    axis : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    space : TransformSpace
      Passed on as its number.
    """
    #  void QQuick3DNode::rotate(qreal degrees, const QVector3D &axis,
    #      QQuick3DNode::TransformSpace space)
    self.uglySide.call(
        'ritual_ZN12QQuick3DNode6rotateEdRK9QVector3DNS_14TransformSpaceE',
        degrees, self._valueOf(axis), space.value,
    )

  def markAllDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DNode::markAllDirty()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#markAllDirty
    """
    #  void QQuick3DNode::markAllDirty()
    ritual = 'ritual_ZN12QQuick3DNode12markAllDirtyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuick3DNode12markAllDirtyEv'
    self.uglySide.call(ritual)

  @overload(QMetaMethod)
  def connectNotify(self, signal: QMetaMethod) -> None:
    """
    Calls Qt's 'void QQuick3DNode::connectNotify(const QMetaMethod &signal)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#connectNotify

    Parameters
    ----------

    signal : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.
    """
    #  void QQuick3DNode::connectNotify(const QMetaMethod &signal)
    ritual = 'ritual_ZN12QQuick3DNode13connectNotifyERK11QMetaMethod'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuick3DNode13connectNotifyERK11QMetaMethod'
    self.uglySide.call(ritual, self._valueOf(signal))

  @overload(QMetaMethod)
  def disconnectNotify(self, signal: QMetaMethod) -> None:
    """
    Calls Qt's 'void QQuick3DNode::disconnectNotify(const QMetaMethod
    &signal)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#disconnectNotify

    Parameters
    ----------

    signal : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.
    """
    #  void QQuick3DNode::disconnectNotify(const QMetaMethod &signal)
    ritual = 'ritual_ZN12QQuick3DNode16disconnectNotifyERK11QMetaMethod'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QQuick3DNode16disconnectNotifyERK11QMetaMethod')
    self.uglySide.call(ritual, self._valueOf(signal))

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuick3DNode::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dnode.html#componentComplete
    """
    #  void QQuick3DNode::componentComplete()
    ritual = 'ritual_ZN12QQuick3DNode17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuick3DNode17componentCompleteEv'
    self.uglySide.call(ritual)

  def xChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DNode::xChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#xChanged
    """
    #  void QQuick3DNode::xChanged()
    self.uglySide.call('ritual_ZN12QQuick3DNode8xChangedEv')

  def yChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DNode::yChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#yChanged
    """
    #  void QQuick3DNode::yChanged()
    self.uglySide.call('ritual_ZN12QQuick3DNode8yChangedEv')

  def zChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DNode::zChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#zChanged
    """
    #  void QQuick3DNode::zChanged()
    self.uglySide.call('ritual_ZN12QQuick3DNode8zChangedEv')

  def rotationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DNode::rotationChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#rotationChanged
    """
    #  void QQuick3DNode::rotationChanged()
    self.uglySide.call('ritual_ZN12QQuick3DNode15rotationChangedEv')

  def eulerRotationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DNode::eulerRotationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dnode.html#eulerRotationChanged
    """
    #  void QQuick3DNode::eulerRotationChanged()
    self.uglySide.call('ritual_ZN12QQuick3DNode20eulerRotationChangedEv')

  def positionChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DNode::positionChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#positionChanged
    """
    #  void QQuick3DNode::positionChanged()
    self.uglySide.call('ritual_ZN12QQuick3DNode15positionChangedEv')

  def scaleChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DNode::scaleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#scaleChanged
    """
    #  void QQuick3DNode::scaleChanged()
    self.uglySide.call('ritual_ZN12QQuick3DNode12scaleChangedEv')

  def pivotChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DNode::pivotChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#pivotChanged
    """
    #  void QQuick3DNode::pivotChanged()
    self.uglySide.call('ritual_ZN12QQuick3DNode12pivotChangedEv')

  def localOpacityChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DNode::localOpacityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dnode.html#localOpacityChanged
    """
    #  void QQuick3DNode::localOpacityChanged()
    self.uglySide.call('ritual_ZN12QQuick3DNode19localOpacityChangedEv')

  def visibleChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DNode::visibleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#visibleChanged
    """
    #  void QQuick3DNode::visibleChanged()
    self.uglySide.call('ritual_ZN12QQuick3DNode14visibleChangedEv')

  def forwardChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DNode::forwardChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#forwardChanged
    """
    #  void QQuick3DNode::forwardChanged()
    self.uglySide.call('ritual_ZN12QQuick3DNode14forwardChangedEv')

  def upChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DNode::upChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#upChanged
    """
    #  void QQuick3DNode::upChanged()
    self.uglySide.call('ritual_ZN12QQuick3DNode9upChangedEv')

  def rightChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DNode::rightChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#rightChanged
    """
    #  void QQuick3DNode::rightChanged()
    self.uglySide.call('ritual_ZN12QQuick3DNode12rightChangedEv')

  def sceneTransformChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DNode::sceneTransformChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dnode.html#sceneTransformChanged
    """
    #  void QQuick3DNode::sceneTransformChanged()
    self.uglySide.call('ritual_ZN12QQuick3DNode21sceneTransformChangedEv')

  def scenePositionChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DNode::scenePositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dnode.html#scenePositionChanged
    """
    #  void QQuick3DNode::scenePositionChanged()
    self.uglySide.call('ritual_ZN12QQuick3DNode20scenePositionChangedEv')

  def sceneRotationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DNode::sceneRotationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dnode.html#sceneRotationChanged
    """
    #  void QQuick3DNode::sceneRotationChanged()
    self.uglySide.call('ritual_ZN12QQuick3DNode20sceneRotationChangedEv')

  def sceneScaleChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DNode::sceneScaleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dnode.html#sceneScaleChanged
    """
    #  void QQuick3DNode::sceneScaleChanged()
    self.uglySide.call('ritual_ZN12QQuick3DNode17sceneScaleChangedEv')

  def staticFlagsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DNode::staticFlagsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dnode.html#staticFlagsChanged
    """
    #  void QQuick3DNode::staticFlagsChanged()
    self.uglySide.call('ritual_ZN12QQuick3DNode18staticFlagsChangedEv')

  def layersChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DNode::layersChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#layersChanged
    """
    #  void QQuick3DNode::layersChanged()
    self.uglySide.call('ritual_ZN12QQuick3DNode13layersChangedEv')

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DNode::updateSpatialNode(QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dnode.html#updateSpatialNode

    Parameters
    ----------

    node : Optional[QSSGRenderGraphObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSSGRenderGraphObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderGraphObject
    #      *QQuick3DNode::updateSpatialNode(QSSGRenderGraphObject *node)
    ritual = (
        'ritual_ZN12QQuick3DNode17updateSpatialNodeEP21QSSGRenderGraphObjec'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QQuick3DNode17updateSpatialNodeEP21QSSGRenderGrap'
          'hObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  @overload(QQuick3DObject.ItemChange, QQuick3DObject.ItemChangeData)
  def itemChange(
      self,
      a0: QQuick3DObject.ItemChange,
      a1: QQuick3DObject.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DNode::itemChange(ItemChange a0, const
    ItemChangeData &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#itemChange

    Parameters
    ----------

    a0 : QQuick3DObject.ItemChange
      Passed on as its number.

    a1 : QQuick3DObject.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuick3DObject::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuick3DNode::itemChange(ItemChange a0, const ItemChangeData &a1)
    ritual = (
        'ritual_ZN12QQuick3DNode10itemChangeEN14QQuick3DObject10ItemChangeE'
        'RKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QQuick3DNode10itemChangeEN14QQuick3DObject10ItemC'
          'hangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, a0.value, self._valueOf(a1))

  def d_func(self) -> Optional[QQuick3DNodePrivate]:
    """
    Calls Qt's 'QQuick3DNodePrivate *QQuick3DNode::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dnode.html#d_func

    Returns
    -------

    Optional[QQuick3DNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DNodePrivate *QQuick3DNode::d_func()
    address = self.uglySide.call('ritual_ZN12QQuick3DNode6d_funcEv')
    from . import QQuick3DNodePrivate
    return QQuick3DNodePrivate._cuteAt(address)


#  Qt's 'QList<QQuick3DNode *>': the list of QQuick3DNode, which
#  'QList[QQuick3DNode]' gives. It is made here, so that there is one as soon
#  as there can be a QQuick3DNode.
QList.createKind(
    QQuick3DNode, 'address',
    make='ritual_list_make_QQuick3DNode_ptr',
    add='ritual_list_add_QQuick3DNode_ptr',
    size='ritual_list_size_QQuick3DNode_ptr',
    at='ritual_list_at_QQuick3DNode_ptr',
    drop='ritual_list_drop_QQuick3DNode_ptr',
)
