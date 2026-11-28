"""
QQuick3DParticleSceneShape binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlesceneshape_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DParticleSceneShape to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QQuick3DParticleAbstractShape

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QVector3D
  from ..QtQuick3D import QQuick3DGeometry, QQuick3DModel, QQuick3DNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DModel = WAIT['QQuick3DModel']
  QQuick3DNode = WAIT['QQuick3DNode']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DParticleSceneShape(QQuick3DParticleAbstractShape):
  """
  The cute side of Qt's QQuick3DParticleSceneShape: a plain Python object
  standing in front of one C++ QQuick3DParticleSceneShape.

  It is built on the cute 'QQuick3DParticleAbstractShape', as Qt's
  QQuick3DParticleSceneShape is built on Qt's QQuick3DParticleAbstractShape,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DParticleSceneShape that has a ritual and
  that Python can call so far, 30 names in all: 'metaObject', 'tr', 'scene',
  'sceneCenter', 'sceneExtents', 'shapeResolution', 'geometry',
  'excludedNodes', 'setScene', 'setSceneCenter', 'setSceneExtents',
  'setShapeResolution', 'setExcludedNodes', 'getPosition',
  'getSurfaceNormal', 'sceneChanged', 'sceneCenterChanged',
  'sceneExtentsChanged', 'shapeResolutionChanged', 'geometryChanged',
  'excludedNodesChanged', 'randomPositionModel', 'createShapeData',
  'clearModelVertexPositions', 'calculateModelVertexPositions',
  'excludeTriangles', 'updateGeometry', 'isVisibleRecursive', 'isExcluded',
  'markDirty'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DParticleSceneShape::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuick3DParticleSceneShape::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DParticleSceneShape::~QQuick3DParticleSceneShape()': the
    destructor: Python never removes a C++ QQuick3DParticleSceneShape.

  What has no ritual
  ------------------

  2 of the 36 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DParticleSceneShape is created at the first use, not by
    'QQuick3DParticleSceneShape(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DParticleSceneShape.
  - Qt tells when it has removed the C++ QQuick3DParticleSceneShape. Every
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
    Calls Qt's 'QString QQuick3DParticleSceneShape::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html#tr

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
    #  QString QQuick3DParticleSceneShape::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QQuick3DParticleSceneShape2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DParticleSceneShape'

  #  A C++ QQuick3DParticleSceneShape Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DParticleSceneShape'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DParticleSceneShape::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DParticleSceneShape::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DParticleSceneShape10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def scene(self) -> Optional[QQuick3DNode]:
    """
    Calls Qt's 'QQuick3DNode *QQuick3DParticleSceneShape::scene() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html#scene

    Returns
    -------

    Optional[QQuick3DNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DNode *QQuick3DParticleSceneShape::scene() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DParticleSceneShape5sceneEv',
    )
    from ..QtQuick3D import QQuick3DNode
    return QQuick3DNode._cuteAt(address)

  def sceneCenter(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DParticleSceneShape::sceneCenter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html#sceneCenter

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleSceneShape::sceneCenter() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DParticleSceneShape11sceneCenterEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def sceneExtents(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DParticleSceneShape::sceneExtents() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html#sceneExtents

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleSceneShape::sceneExtents() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DParticleSceneShape12sceneExtentsEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def shapeResolution(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleSceneShape::shapeResolution() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html#shapeResolution
    """
    #  float QQuick3DParticleSceneShape::shapeResolution() const
    return self.uglySide.call(
        'ritual_ZNK26QQuick3DParticleSceneShape15shapeResolutionEv',
    )

  def geometry(self) -> Optional[QQuick3DGeometry]:
    """
    Calls Qt's 'QQuick3DGeometry *QQuick3DParticleSceneShape::geometry()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html#geometry

    Returns
    -------

    Optional[QQuick3DGeometry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DGeometry *QQuick3DParticleSceneShape::geometry() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DParticleSceneShape8geometryEv',
    )
    from ..QtQuick3D import QQuick3DGeometry
    return QQuick3DGeometry._cuteAt(address)

  def excludedNodes(self) -> QList[QQuick3DNode]:
    """
    Calls Qt's 'QList<QQuick3DNode *>
    QQuick3DParticleSceneShape::excludedNodes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html#excludedNodes

    Returns
    -------

    QList[QQuick3DNode]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuick3DNode *> QQuick3DParticleSceneShape::excludedNodes()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK26QQuick3DParticleSceneShape13excludedNodesEv',
    )
    from ..QtQuick3D import QQuick3DNode
    return QList[QQuick3DNode]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuick3DNode)
  @overload(NoneType)
  def setScene(self, scene: Optional[QQuick3DNode]) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSceneShape::setScene(QQuick3DNode
    *scene)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html#setScene

    Parameters
    ----------

    scene : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleSceneShape::setScene(QQuick3DNode *scene)
    self.uglySide.call(
        'ritual_ZN26QQuick3DParticleSceneShape8setSceneEP12QQuick3DNode',
        self._addressOf(scene),
    )

  @overload(QVector3D)
  def setSceneCenter(self, extents: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSceneShape::setSceneCenter(const
    QVector3D &extents)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html#setSceneCenter

    Parameters
    ----------

    extents : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DParticleSceneShape::setSceneCenter(const QVector3D
    #      &extents)
    self.uglySide.call(
        'ritual_ZN26QQuick3DParticleSceneShape14setSceneCenterERK9QVector3D',
        self._valueOf(extents),
    )

  @overload(QVector3D)
  def setSceneExtents(self, extents: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSceneShape::setSceneExtents(const
    QVector3D &extents)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html#setSceneExtents

    Parameters
    ----------

    extents : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DParticleSceneShape::setSceneExtents(const QVector3D
    #      &extents)
    self.uglySide.call(
        'ritual_ZN26QQuick3DParticleSceneShape15setSceneExtentsERK9QVector3'
        'D',
        self._valueOf(extents),
    )

  @overload(float)
  def setShapeResolution(self, resolution: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSceneShape::setShapeResolution(float
    resolution)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html#setShapeResolution

    Parameters
    ----------

    resolution : float
      Passed on as it is.
    """
    #  void QQuick3DParticleSceneShape::setShapeResolution(float resolution)
    self.uglySide.call(
        'ritual_ZN26QQuick3DParticleSceneShape18setShapeResolutionEf',
        resolution,
    )

  @overload(QList[QQuick3DNode])
  def setExcludedNodes(self, nodes: QList[QQuick3DNode]) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSceneShape::setExcludedNodes(const
    QList<QQuick3DNode *> &nodes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html#setExcludedNodes

    Parameters
    ----------

    nodes : QList[QQuick3DNode]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuick3DParticleSceneShape::setExcludedNodes(const
    #      QList<QQuick3DNode *> &nodes)
    self.uglySide.call(
        'ritual_ZN26QQuick3DParticleSceneShape16setExcludedNodesERK5QListIP'
        '12QQuick3DNodeE',
        self._valueOf(nodes),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DParticleSceneShape::QQuick3DParticleSceneShape(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DParticleSceneShape::QQuick3DParticleSceneShape(QObject
    #      *parent)
    self._noteCreation(QQuick3DParticleSceneShape, lambda: Rituals.call(
        'ritual_ZN26QQuick3DParticleSceneShapeC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(int)
  def getPosition(self, particleIndex: int) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DParticleSceneShape::getPosition(int
    particleIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html#getPosition

    Parameters
    ----------

    particleIndex : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleSceneShape::getPosition(int particleIndex)
    ritual = 'ritual_ZN26QQuick3DParticleSceneShape11getPositionEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QQuick3DParticleSceneShape11getPositionEi'
    address = self.uglySide.call(ritual, particleIndex)
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(int)
  def getSurfaceNormal(self, particleIndex: int) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DParticleSceneShape::getSurfaceNormal(int
    particleIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html#getSurfaceNormal

    Parameters
    ----------

    particleIndex : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleSceneShape::getSurfaceNormal(int
    #      particleIndex)
    ritual = 'ritual_ZN26QQuick3DParticleSceneShape16getSurfaceNormalEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuick3DParticleSceneShape16getSurfaceNormalEi')
    address = self.uglySide.call(ritual, particleIndex)
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def sceneChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSceneShape::sceneChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html#sceneChanged
    """
    #  void QQuick3DParticleSceneShape::sceneChanged()
    self.uglySide.call(
        'ritual_ZN26QQuick3DParticleSceneShape12sceneChangedEv',
    )

  def sceneCenterChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSceneShape::sceneCenterChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html#sceneCenterChanged
    """
    #  void QQuick3DParticleSceneShape::sceneCenterChanged()
    self.uglySide.call(
        'ritual_ZN26QQuick3DParticleSceneShape18sceneCenterChangedEv',
    )

  def sceneExtentsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSceneShape::sceneExtentsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html
    """
    #  void QQuick3DParticleSceneShape::sceneExtentsChanged()
    self.uglySide.call(
        'ritual_ZN26QQuick3DParticleSceneShape19sceneExtentsChangedEv',
    )

  def shapeResolutionChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSceneShape::shapeResolutionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html
    """
    #  void QQuick3DParticleSceneShape::shapeResolutionChanged()
    self.uglySide.call(
        'ritual_ZN26QQuick3DParticleSceneShape22shapeResolutionChangedEv',
    )

  def geometryChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSceneShape::geometryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html#geometryChanged
    """
    #  void QQuick3DParticleSceneShape::geometryChanged()
    self.uglySide.call(
        'ritual_ZN26QQuick3DParticleSceneShape15geometryChangedEv',
    )

  def excludedNodesChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSceneShape::excludedNodesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html
    """
    #  void QQuick3DParticleSceneShape::excludedNodesChanged()
    self.uglySide.call(
        'ritual_ZN26QQuick3DParticleSceneShape20excludedNodesChangedEv',
    )

  @overload(int)
  def randomPositionModel(self, particleIndex: int) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DParticleSceneShape::randomPositionModel(int
    particleIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html

    Parameters
    ----------

    particleIndex : int
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleSceneShape::randomPositionModel(int
    #      particleIndex)
    address = self.uglySide.call(
        'ritual_ZN26QQuick3DParticleSceneShape19randomPositionModelEi',
        particleIndex,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def createShapeData(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSceneShape::createShapeData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html#createShapeData
    """
    #  void QQuick3DParticleSceneShape::createShapeData()
    self.uglySide.call(
        'ritual_ZN26QQuick3DParticleSceneShape15createShapeDataEv',
    )

  def clearModelVertexPositions(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleSceneShape::clearModelVertexPositions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html
    """
    #  void QQuick3DParticleSceneShape::clearModelVertexPositions()
    self.uglySide.call(
        'ritual_ZN26QQuick3DParticleSceneShape25clearModelVertexPositionsEv',
    )

  def calculateModelVertexPositions(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleSceneShape::calculateModelVertexPositions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html
    """
    #  void QQuick3DParticleSceneShape::calculateModelVertexPositions()
    self.uglySide.call(
        'ritual_ZN26QQuick3DParticleSceneShape29calculateModelVertexPositio'
        'nsEv',
    )

  @overload(QList[QVector3D])
  def excludeTriangles(self, list: QList[QVector3D]) -> QList[QVector3D]:
    """
    Calls Qt's 'QList<QVector3D>
    QQuick3DParticleSceneShape::excludeTriangles(const QList<QVector3D>
    &list)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html#excludeTriangles

    Parameters
    ----------

    list : QList[QVector3D]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QList[QVector3D]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QVector3D> QQuick3DParticleSceneShape::excludeTriangles(const
    #      QList<QVector3D> &list)
    address = self.uglySide.call(
        'ritual_ZN26QQuick3DParticleSceneShape16excludeTrianglesERK5QListI9'
        'QVector3DE',
        self._valueOf(list),
    )
    from ..QtGui import QVector3D
    return QList[QVector3D]._cuteOwning(address)

  def updateGeometry(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSceneShape::updateGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html#updateGeometry
    """
    #  void QQuick3DParticleSceneShape::updateGeometry()
    self.uglySide.call(
        'ritual_ZN26QQuick3DParticleSceneShape14updateGeometryEv',
    )

  @overload(QQuick3DNode)
  @overload(NoneType)
  def isVisibleRecursive(self, node: Optional[QQuick3DNode]) -> bool:
    """
    Calls Qt's 'bool
    QQuick3DParticleSceneShape::isVisibleRecursive(QQuick3DNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html#isVisibleRecursive

    Parameters
    ----------

    node : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuick3DParticleSceneShape::isVisibleRecursive(QQuick3DNode
    #      *node)
    return self.uglySide.call(
        'ritual_ZN26QQuick3DParticleSceneShape18isVisibleRecursiveEP12QQuic'
        'k3DNode',
        self._addressOf(node),
    )

  @overload(QQuick3DModel)
  @overload(NoneType)
  def isExcluded(self, model: Optional[QQuick3DModel]) -> bool:
    """
    Calls Qt's 'bool QQuick3DParticleSceneShape::isExcluded(QQuick3DModel
    *model)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html#isExcluded

    Parameters
    ----------

    model : Optional[QQuick3DModel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuick3DParticleSceneShape::isExcluded(QQuick3DModel *model)
    return self.uglySide.call(
        'ritual_ZN26QQuick3DParticleSceneShape10isExcludedEP13QQuick3DModel',
        self._addressOf(model),
    )

  @overload()
  @overload(bool)
  @overload(bool, bool)
  def markDirty(
      self,
      dirty: bool = True,
      excludeDirty: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSceneShape::markDirty(bool dirty, bool
    excludeDirty)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesceneshape.html#markDirty

    Parameters
    ----------

    dirty : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    excludeDirty : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuick3DParticleSceneShape::markDirty(bool dirty, bool
    #      excludeDirty)
    self.uglySide.call(
        'ritual_ZN26QQuick3DParticleSceneShape9markDirtyEbb',
        dirty, excludeDirty,
    )
