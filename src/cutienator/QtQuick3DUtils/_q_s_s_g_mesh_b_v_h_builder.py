"""
QSSGMeshBVHBuilder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgmeshbvhbuilder_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QSSGMeshBVHBuilder to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QSSGMesh

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QSSGBounds3, QSSGMeshBVH
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSSGMeshBVH = WAIT['QSSGMeshBVH']


class QSSGMeshBVHBuilder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGMeshBVHBuilder: a plain Python object standing in
  front of one C++ QSSGMeshBVHBuilder.

  C++ hands a QSSGMeshBVHBuilder around as a copy, so every C++
  QSSGMeshBVHBuilder behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGMeshBVHBuilder that has a ritual and that Python
  can call so far, 1 name in all: 'getBounds'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGMeshBVHBuilder::QSSGMeshBVHBuilder(const QByteArray
    &vertexBuffer, int stride, int posOffset, bool hasUV, int uvOffset, bool
    hasIndexBuffer, const QByteArray &indexBuffer, QSSGRenderComponentType
    indexBufferType)': names the enum 'QSSGRenderComponentType', whose class
    cannot be named here.
  - Qt's 'std::unique_ptr<QSSGMeshBVH> QSSGMeshBVHBuilder::buildTree()':
    gives a type Python has no way to take yet.
  - Qt's 'QSSGMeshBVHTriangles
    QSSGMeshBVHBuilder::calculateTriangleBounds(quint32 indexOffset, quint32
    indexCount) const': gives a type Python has no way to take yet.
  - Qt's 'QSSGMeshBVHNode::Handle QSSGMeshBVHBuilder::splitNode(QSSGMeshBVH
    &bvh, QSSGMeshBVHNode::Handle node, quint32 offset, quint32 count,
    quint32 depth)': takes a type Python has no way to hand over yet.
  - Qt's 'Split QSSGMeshBVHBuilder::getOptimalSplit(const QSSGMeshBVH &bvh,
    const QSSGBounds3 &nodeBounds, quint32 offset, quint32 count)': gives a
    type Python has no way to take yet.
  - Qt's 'Axis QSSGMeshBVHBuilder::getLongestDimension(const QSSGBounds3
    &nodeBounds)': gives the enum 'QSSGMeshBVHBuilder::Axis', whose class
    cannot be named here.
  - Qt's 'float QSSGMeshBVHBuilder::getAverageValue(const QSSGMeshBVH &bvh,
    quint32 offset, quint32 count, Axis axis)': names the enum
    'QSSGMeshBVHBuilder::Axis', whose class cannot be named here.
  - Qt's 'quint32 QSSGMeshBVHBuilder::partition(QSSGMeshBVH &bvh, quint32
    offset, quint32 count, const Split &split)': takes a type Python has no
    way to hand over yet.
  - Qt's 'QSSGMeshBVHBuilder::~QSSGMeshBVHBuilder()': the destructor: Python
    removes its C++ QSSGMeshBVHBuilder by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSSGMeshBVHBuilder is created at the first use, not by
    'QSSGMeshBVHBuilder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGMeshBVHBuilder back gives a copy the ritual made
    for Python, in a new cute QSSGMeshBVHBuilder.
  - Each name of Qt's QSSGMeshBVHBuilder that has no cute function yet,
    'buildTree', 'calculateTriangleBounds', 'getAverageValue',
    'getLongestDimension', 'getOptimalSplit', 'partition', 'splitNode', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QSSGMeshBVH, int, int)
  def getBounds(bvh: QSSGMeshBVH, offset: int, count: int) -> QSSGBounds3:
    """
    Calls Qt's 'QSSGBounds3 QSSGMeshBVHBuilder::getBounds(const QSSGMeshBVH
    &bvh, quint32 offset, quint32 count)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgmeshbvhbuilder.html#getBounds

    Parameters
    ----------

    bvh : QSSGMeshBVH
      Passed on as a value: Qt reads the C++ QSSGMeshBVH, which stays
      Python's own.

    offset : int
      Passed on as it is.

    count : int
      Passed on as it is.

    Returns
    -------

    QSSGBounds3
      A new cute QSSGBounds3 around the copy Qt gave back. Python owns it.
    """
    #  QSSGBounds3 QSSGMeshBVHBuilder::getBounds(const QSSGMeshBVH &bvh,
    #      quint32 offset, quint32 count)
    address = Rituals.call(
        'ritual_ZN18QSSGMeshBVHBuilder9getBoundsERK11QSSGMeshBVHjj',
        CuteMixin._valueOf(bvh), offset, count,
    )
    from . import QSSGBounds3
    return QSSGBounds3._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGMeshBVHBuilder'

  #  Qt's '~QSSGMeshBVHBuilder()'. Naming it makes this a value class: Python
  #  owns every C++ QSSGMeshBVHBuilder behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QSSGMeshBVHBuilderD1Ev'

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

  @overload(WAIT['QSSGMesh.Mesh'])
  def __init__(self, mesh: QSSGMesh.Mesh) -> None:
    """
    Notes what was given, for Qt's
    'QSSGMeshBVHBuilder::QSSGMeshBVHBuilder(const QSSGMesh::Mesh &mesh)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgmeshbvhbuilder.html#QSSGMeshBVHBuilder

    Parameters
    ----------

    mesh : QSSGMesh.Mesh
      Passed on as a value: Qt reads the C++ QSSGMesh::Mesh, which stays
      Python's own.
    """
    #  QSSGMeshBVHBuilder::QSSGMeshBVHBuilder(const QSSGMesh::Mesh &mesh)
    self._noteCreation(QSSGMeshBVHBuilder, lambda: Rituals.call(
        'ritual_ZN18QSSGMeshBVHBuilderC1ERKN8QSSGMesh4MeshE',
        self._valueOf(mesh),
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

  @staticmethod
  def buildTree(*__, **_) -> Never:
    """
    Qt's 'std::unique_ptr<QSSGMeshBVH> QSSGMeshBVHBuilder::buildTree()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGMeshBVHBuilder.buildTree' has no cute function yet. Qt's "
        "'std::unique_ptr<QSSGMeshBVH> QSSGMeshBVHBuilder::buildTree()': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def calculateTriangleBounds(*__, **_) -> Never:
    """
    Qt's 'QSSGMeshBVHTriangles
    QSSGMeshBVHBuilder::calculateTriangleBounds(quint32 indexOffset, quint32
    indexCount) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGMeshBVHBuilder.calculateTriangleBounds' has no cute function "
        "yet. Qt's 'QSSGMeshBVHTriangles "
        "QSSGMeshBVHBuilder::calculateTriangleBounds(quint32 indexOffset, "
        "quint32 indexCount) const': gives a type Python has no way to take "
        "yet.")

  @staticmethod
  def getAverageValue(*__, **_) -> Never:
    """
    Qt's 'float QSSGMeshBVHBuilder::getAverageValue(const QSSGMeshBVH &bvh,
    quint32 offset, quint32 count, Axis axis)': names the enum
    'QSSGMeshBVHBuilder::Axis', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGMeshBVHBuilder.getAverageValue' has no cute function yet. "
        "Qt's 'float QSSGMeshBVHBuilder::getAverageValue(const QSSGMeshBVH "
        "&bvh, quint32 offset, quint32 count, Axis axis)': names the enum "
        "'QSSGMeshBVHBuilder::Axis', whose class cannot be named here.")

  @staticmethod
  def getLongestDimension(*__, **_) -> Never:
    """
    Qt's 'Axis QSSGMeshBVHBuilder::getLongestDimension(const QSSGBounds3
    &nodeBounds)': gives the enum 'QSSGMeshBVHBuilder::Axis', whose class
    cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGMeshBVHBuilder.getLongestDimension' has no cute function yet. "
        "Qt's 'Axis QSSGMeshBVHBuilder::getLongestDimension(const "
        "QSSGBounds3 &nodeBounds)': gives the enum "
        "'QSSGMeshBVHBuilder::Axis', whose class cannot be named here.")

  @staticmethod
  def getOptimalSplit(*__, **_) -> Never:
    """
    Qt's 'Split QSSGMeshBVHBuilder::getOptimalSplit(const QSSGMeshBVH &bvh,
    const QSSGBounds3 &nodeBounds, quint32 offset, quint32 count)': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGMeshBVHBuilder.getOptimalSplit' has no cute function yet. "
        "Qt's 'Split QSSGMeshBVHBuilder::getOptimalSplit(const QSSGMeshBVH "
        "&bvh, const QSSGBounds3 &nodeBounds, quint32 offset, quint32 "
        "count)': gives a type Python has no way to take yet.")

  @staticmethod
  def partition(*__, **_) -> Never:
    """
    Qt's 'quint32 QSSGMeshBVHBuilder::partition(QSSGMeshBVH &bvh, quint32
    offset, quint32 count, const Split &split)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGMeshBVHBuilder.partition' has no cute function yet. Qt's "
        "'quint32 QSSGMeshBVHBuilder::partition(QSSGMeshBVH &bvh, quint32 "
        "offset, quint32 count, const Split &split)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def splitNode(*__, **_) -> Never:
    """
    Qt's 'QSSGMeshBVHNode::Handle QSSGMeshBVHBuilder::splitNode(QSSGMeshBVH
    &bvh, QSSGMeshBVHNode::Handle node, quint32 offset, quint32 count,
    quint32 depth)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGMeshBVHBuilder.splitNode' has no cute function yet. Qt's "
        "'QSSGMeshBVHNode::Handle QSSGMeshBVHBuilder::splitNode(QSSGMeshBVH "
        "&bvh, QSSGMeshBVHNode::Handle node, quint32 offset, quint32 count, "
        "quint32 depth)': takes a type Python has no way to hand over yet.")
