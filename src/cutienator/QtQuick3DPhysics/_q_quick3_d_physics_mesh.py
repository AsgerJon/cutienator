"""
QQuick3DPhysicsMesh binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qphysicsmeshutils_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DPhysicsMesh to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtQuick3D import QQuick3DGeometry
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DGeometry = WAIT['QQuick3DGeometry']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DPhysicsMesh(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuick3DPhysicsMesh: a plain Python object standing
  in front of one C++ QQuick3DPhysicsMesh.

  C++ hands a QQuick3DPhysicsMesh around as a copy, so every C++
  QQuick3DPhysicsMesh behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuick3DPhysicsMesh that has a ritual and that
  Python can call so far, 2 names in all: 'ref', 'deref'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuick3DPhysicsMesh::~QQuick3DPhysicsMesh()': the destructor:
    Python removes its C++ QQuick3DPhysicsMesh by it, and has no other use
    for it.

  What has no ritual
  ------------------

  9 of the 14 functions Qt declares: 4 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 leans on
  'lcQuick3dPhysics()', which Qt's source does not mark for use from outside
  Qt and has no code for that could be taken; 2 leans on
  'QQuick3DPhysicsMesh; 1 cannot be called and cannot be called through the
  meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QQuick3DPhysicsMesh is created at the first use, not by
    'QQuick3DPhysicsMesh(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuick3DPhysicsMesh back gives a copy the ritual made
    for Python, in a new cute QQuick3DPhysicsMesh.
  - Each name of Qt's QQuick3DPhysicsMesh that has no cute function yet,
    'bounds', 'convexMesh', 'convexMeshGeometrySource',
    'convexMeshQmlSource', 'loadSsgMesh', 'positions', 'triangleMesh',
    'triangleMeshGeometrySource', 'triangleMeshQmlSource', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuick3DPhysicsMesh, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class MeshType(CuteNum):
    """
    The enum 'QQuick3DPhysicsMesh::MeshType' of Qt, with the 2 names Qt gives
    in it.
    """

    Convex = Kee[int](0)
    Triangle = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DPhysicsMesh'

  #  Qt's '~QQuick3DPhysicsMesh()'. Naming it makes this a value class:
  #  Python owns every C++ QQuick3DPhysicsMesh behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QQuick3DPhysicsMeshD1Ev'

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

  @overload(str)
  def __init__(self, qmlSource: str) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DPhysicsMesh::QQuick3DPhysicsMesh(const QString &qmlSource)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dphysicsmesh.html#QQuick3DPhysicsMesh

    Parameters
    ----------

    qmlSource : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QQuick3DPhysicsMesh::QQuick3DPhysicsMesh(const QString &qmlSource)
    self._noteCreation(QQuick3DPhysicsMesh, lambda: Rituals.call(
        'ritual_ZN19QQuick3DPhysicsMeshC1ERK7QString', qmlSource,
    ))

  @overload(QQuick3DGeometry)
  @overload(NoneType)
  def __init__(self, geometrySource: Optional[QQuick3DGeometry]) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DPhysicsMesh::QQuick3DPhysicsMesh(const QQuick3DGeometry
    *geometrySource)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dphysicsmesh.html#QQuick3DPhysicsMesh

    Parameters
    ----------

    geometrySource : Optional[QQuick3DGeometry]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuick3DPhysicsMesh::QQuick3DPhysicsMesh(const QQuick3DGeometry
    #      *geometrySource)
    self._noteCreation(QQuick3DPhysicsMesh, lambda: Rituals.call(
        'ritual_ZN19QQuick3DPhysicsMeshC1EPK16QQuick3DGeometry',
        self._addressOf(geometrySource),
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

  def ref(self) -> None:
    """
    Calls Qt's 'void QQuick3DPhysicsMesh::ref()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dphysicsmesh.html#ref
    """
    #  void QQuick3DPhysicsMesh::ref()
    self.uglySide.call('ritual_ZN19QQuick3DPhysicsMesh3refEv')

  def deref(self) -> int:
    """
    Calls Qt's 'int QQuick3DPhysicsMesh::deref()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dphysicsmesh.html#deref
    """
    #  int QQuick3DPhysicsMesh::deref()
    return self.uglySide.call('ritual_ZN19QQuick3DPhysicsMesh5derefEv')

  @staticmethod
  def bounds(*__, **_) -> Never:
    """
    Qt's 'QPair<QVector3D, QVector3D> QQuick3DPhysicsMesh::bounds()': leans
    on 'lcQuick3dPhysics()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DPhysicsMesh.bounds' has no cute function yet. Qt's "
        "'QPair<QVector3D, QVector3D> QQuick3DPhysicsMesh::bounds()': leans "
        "on 'lcQuick3dPhysics()', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def convexMesh(*__, **_) -> Never:
    """
    Qt's 'physx::PxConvexMesh *QQuick3DPhysicsMesh::convexMesh()': leans on
    'QQuick3DPhysicsMesh::convexMeshQmlSource()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DPhysicsMesh.convexMesh' has no cute function yet. Qt's "
        "'physx::PxConvexMesh *QQuick3DPhysicsMesh::convexMesh()': leans on "
        "'QQuick3DPhysicsMesh::convexMeshQmlSource()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def convexMeshGeometrySource(*__, **_) -> Never:
    """
    Qt's 'physx::PxConvexMesh
    *QQuick3DPhysicsMesh::convexMeshGeometrySource()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'isValidPositionLayout'.
    """
    raise NotImplementedError(
        "'QQuick3DPhysicsMesh.convexMeshGeometrySource' has no cute "
        "function yet. Qt's 'physx::PxConvexMesh "
        "*QQuick3DPhysicsMesh::convexMeshGeometrySource()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'isValidPositionLayout'.")

  @staticmethod
  def convexMeshQmlSource(*__, **_) -> Never:
    """
    Qt's 'physx::PxConvexMesh *QQuick3DPhysicsMesh::convexMeshQmlSource()':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: no type named 'PxConvexMeshDesc' in
    namespace 'physx'; did you mean 'PxConvexMesh'?.
    """
    raise NotImplementedError(
        "'QQuick3DPhysicsMesh.convexMeshQmlSource' has no cute function "
        "yet. Qt's 'physx::PxConvexMesh "
        "*QQuick3DPhysicsMesh::convexMeshQmlSource()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: no type named 'PxConvexMeshDesc' in namespace "
        "'physx'; did you mean 'PxConvexMesh'?.")

  @staticmethod
  def loadSsgMesh(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DPhysicsMesh::loadSsgMesh()': leans on
    'lcQuick3dPhysics()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DPhysicsMesh.loadSsgMesh' has no cute function yet. Qt's "
        "'void QQuick3DPhysicsMesh::loadSsgMesh()': leans on "
        "'lcQuick3dPhysics()', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def positions(*__, **_) -> Never:
    """
    Qt's 'QList<QVector3D> QQuick3DPhysicsMesh::positions()': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QQuick3DPhysicsMesh.positions' has no cute function yet. Qt's "
        "'QList<QVector3D> QQuick3DPhysicsMesh::positions()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def triangleMesh(*__, **_) -> Never:
    """
    Qt's 'physx::PxTriangleMesh *QQuick3DPhysicsMesh::triangleMesh()': leans
    on 'QQuick3DPhysicsMesh::triangleMeshQmlSource()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DPhysicsMesh.triangleMesh' has no cute function yet. Qt's "
        "'physx::PxTriangleMesh *QQuick3DPhysicsMesh::triangleMesh()': "
        "leans on 'QQuick3DPhysicsMesh::triangleMeshQmlSource()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def triangleMeshGeometrySource(*__, **_) -> Never:
    """
    Qt's 'physx::PxTriangleMesh
    *QQuick3DPhysicsMesh::triangleMeshGeometrySource()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'attributeBySemantic'.
    """
    raise NotImplementedError(
        "'QQuick3DPhysicsMesh.triangleMeshGeometrySource' has no cute "
        "function yet. Qt's 'physx::PxTriangleMesh "
        "*QQuick3DPhysicsMesh::triangleMeshGeometrySource()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier "
        "'attributeBySemantic'.")

  @staticmethod
  def triangleMeshQmlSource(*__, **_) -> Never:
    """
    Qt's 'physx::PxTriangleMesh
    *QQuick3DPhysicsMesh::triangleMeshQmlSource()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'isValidPositionLayout'.
    """
    raise NotImplementedError(
        "'QQuick3DPhysicsMesh.triangleMeshQmlSource' has no cute function "
        "yet. Qt's 'physx::PxTriangleMesh "
        "*QQuick3DPhysicsMesh::triangleMeshQmlSource()': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier "
        "'isValidPositionLayout'.")
