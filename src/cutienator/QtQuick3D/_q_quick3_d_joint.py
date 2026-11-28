"""
QQuick3DJoint binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3djoint_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuick3DJoint to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QQuick3DNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
  from . import QQuick3DSkeleton
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DSkeleton = WAIT['QQuick3DSkeleton']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DJoint(QQuick3DNode):
  """
  The cute side of Qt's QQuick3DJoint: a plain Python object standing in
  front of one C++ QQuick3DJoint.

  It is built on the cute 'QQuick3DNode', as Qt's QQuick3DJoint is built on
  Qt's QQuick3DNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DJoint that has a ritual and that Python can
  call so far, 10 names in all: 'metaObject', 'tr', 'index', 'skeletonRoot',
  'setIndex', 'setSkeletonRoot', 'indexChanged', 'skeletonRootChanged',
  'updateSpatialNode', 'markAllDirty'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DJoint::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuick3DJoint::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DJoint::~QQuick3DJoint()': the destructor: Python never
    removes a C++ QQuick3DJoint.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DJoint is created at the first use, not by
    'QQuick3DJoint(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DJoint.
  - Qt tells when it has removed the C++ QQuick3DJoint. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuick3DJoint::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3djoint.html#tr

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
    #  QString QQuick3DJoint::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QQuick3DJoint2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DJoint'

  #  A C++ QQuick3DJoint Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DJoint'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DJoint::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3djoint.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DJoint::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QQuick3DJoint10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def index(self) -> int:
    """
    Calls Qt's 'qint32 QQuick3DJoint::index() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3djoint.html#index
    """
    #  qint32 QQuick3DJoint::index() const
    return self.uglySide.call('ritual_ZNK13QQuick3DJoint5indexEv')

  def skeletonRoot(self) -> Optional[QQuick3DSkeleton]:
    """
    Calls Qt's 'QQuick3DSkeleton *QQuick3DJoint::skeletonRoot() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3djoint.html#skeletonRoot

    Returns
    -------

    Optional[QQuick3DSkeleton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DSkeleton *QQuick3DJoint::skeletonRoot() const
    address = self.uglySide.call('ritual_ZNK13QQuick3DJoint12skeletonRootEv')
    from . import QQuick3DSkeleton
    return QQuick3DSkeleton._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setIndex(self, index: int) -> None:
    """
    Calls Qt's 'void QQuick3DJoint::setIndex(qint32 index)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3djoint.html#setIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQuick3DJoint::setIndex(qint32 index)
    self.uglySide.call('ritual_ZN13QQuick3DJoint8setIndexEi', index)

  @overload(QQuick3DSkeleton)
  @overload(NoneType)
  def setSkeletonRoot(self, skeleton: Optional[QQuick3DSkeleton]) -> None:
    """
    Calls Qt's 'void QQuick3DJoint::setSkeletonRoot(QQuick3DSkeleton
    *skeleton)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3djoint.html#setSkeletonRoot

    Parameters
    ----------

    skeleton : Optional[QQuick3DSkeleton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DJoint::setSkeletonRoot(QQuick3DSkeleton *skeleton)
    self.uglySide.call(
        'ritual_ZN13QQuick3DJoint15setSkeletonRootEP16QQuick3DSkeleton',
        self._addressOf(skeleton),
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
  @overload(QQuick3DNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DNode] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuick3DJoint::QQuick3DJoint(QQuick3DNode
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquick3djoint.html#QQuick3DJoint

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DJoint::QQuick3DJoint(QQuick3DNode *parent)
    self._noteCreation(QQuick3DJoint, lambda: Rituals.call(
        'ritual_ZN13QQuick3DJointC1EP12QQuick3DNode',
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

  def indexChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DJoint::indexChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3djoint.html#indexChanged
    """
    #  void QQuick3DJoint::indexChanged()
    self.uglySide.call('ritual_ZN13QQuick3DJoint12indexChangedEv')

  def skeletonRootChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DJoint::skeletonRootChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3djoint.html#skeletonRootChanged
    """
    #  void QQuick3DJoint::skeletonRootChanged()
    self.uglySide.call('ritual_ZN13QQuick3DJoint19skeletonRootChangedEv')

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DJoint::updateSpatialNode(QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3djoint.html#updateSpatialNode

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
    #      *QQuick3DJoint::updateSpatialNode(QSSGRenderGraphObject *node)
    ritual = (
        'ritual_ZN13QQuick3DJoint17updateSpatialNodeEP21QSSGRenderGraphObje'
        'ct')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QQuick3DJoint17updateSpatialNodeEP21QSSGRenderGra'
          'phObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  def markAllDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DJoint::markAllDirty()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3djoint.html#markAllDirty
    """
    #  void QQuick3DJoint::markAllDirty()
    ritual = 'ritual_ZN13QQuick3DJoint12markAllDirtyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuick3DJoint12markAllDirtyEv'
    self.uglySide.call(ritual)
