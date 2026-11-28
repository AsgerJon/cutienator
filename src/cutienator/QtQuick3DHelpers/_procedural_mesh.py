"""
ProceduralMesh binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/proceduralmesh_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means ProceduralMesh to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QObject
  from ..QtGui import QVector2D, QVector3D, QVector4D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QVector2D = WAIT['QVector2D']
  QVector3D = WAIT['QVector3D']
  QVector4D = WAIT['QVector4D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ProceduralMesh(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's ProceduralMesh: a plain Python object standing in
  front of one C++ ProceduralMesh.

  What exists
  -----------

  Every function of Qt's ProceduralMesh that has a ritual and that Python can
  call so far, 37 names in all: 'metaObject', 'tr', 'positions',
  'setPositions', 'primitiveMode', 'setPrimitiveMode', 'normals',
  'setNormals', 'tangents', 'setTangents', 'binormals', 'setBinormals',
  'uv0s', 'setUv0s', 'uv1s', 'setUv1s', 'colors', 'setColors', 'joints',
  'setJoints', 'weights', 'setWeights', 'positionsChanged',
  'primitiveModeChanged', 'indexesChanged', 'normalsChanged',
  'tangentsChanged', 'binormalsChanged', 'uv0sChanged', 'uv1sChanged',
  'colorsChanged', 'jointsChanged', 'weightsChanged', 'requestUpdate',
  'updateGeometry', 'subsetDestroyed', 'supportsTriangleFanPrimitive'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *ProceduralMesh::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int ProceduralMesh::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QList<unsigned int> ProceduralMesh::indexes() const': gives a type
    Python has no way to take yet.
  - Qt's 'void ProceduralMesh::setIndexes(const QList<unsigned int>
    &newIndexes)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlListProperty<ProceduralMeshSubset> ProceduralMesh::subsets()':
    gives a type Python has no way to take yet.
  - Qt's 'void ProceduralMesh::qmlAppendProceduralMeshSubset(
    QQmlListProperty<ProceduralMeshSubset> *list, ProceduralMeshSubset
    *subset)': names 'QQmlListProperty<ProceduralMeshSubset>', which has no
    cute class yet.
  - Qt's 'ProceduralMeshSubset *ProceduralMesh::qmlProceduralMeshSubsetAt(
    QQmlListProperty<ProceduralMeshSubset> *list, qsizetype index)': names
    'QQmlListProperty<ProceduralMeshSubset>', which has no cute class yet.
  - Qt's 'qsizetype ProceduralMesh::qmlProceduralMeshSubsetCount(
    QQmlListProperty<ProceduralMeshSubset> *list)': names
    'QQmlListProperty<ProceduralMeshSubset>', which has no cute class yet.
  - Qt's 'void ProceduralMesh::qmlClearProceduralMeshSubset(
    QQmlListProperty<ProceduralMeshSubset> *list)': names
    'QQmlListProperty<ProceduralMeshSubset>', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 49 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ ProceduralMesh is created at the first use, not by
    'ProceduralMesh(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ ProceduralMesh.
  - Qt tells when it has removed the C++ ProceduralMesh. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's ProceduralMesh that has no cute function yet,
    'indexes', 'qmlAppendProceduralMeshSubset',
    'qmlClearProceduralMeshSubset', 'qmlProceduralMeshSubsetAt',
    'qmlProceduralMeshSubsetCount', 'setIndexes', 'subsets', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside ProceduralMesh, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class PrimitiveMode(CuteNum):
    """
    The enum 'ProceduralMesh::PrimitiveMode' of Qt, with the 6 names Qt gives
    in it.
    """

    Points = Kee[int](0)
    LineStrip = Kee[int](1)
    Lines = Kee[int](2)
    TriangleStrip = Kee[int](3)
    TriangleFan = Kee[int](4)
    Triangles = Kee[int](5)

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
    Calls Qt's 'QString ProceduralMesh::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#tr

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
    #  QString ProceduralMesh::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14ProceduralMesh2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ProceduralMesh'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *ProceduralMesh::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *ProceduralMesh::metaObject() const
    address = self.uglySide.call('ritual_ZNK14ProceduralMesh10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def positions(self) -> QList[QVector3D]:
    """
    Calls Qt's 'QList<QVector3D> ProceduralMesh::positions() const'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#positions

    Returns
    -------

    QList[QVector3D]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QVector3D> ProceduralMesh::positions() const
    address = self.uglySide.call('ritual_ZNK14ProceduralMesh9positionsEv')
    from ..QtGui import QVector3D
    return QList[QVector3D]._cuteOwning(address)

  def primitiveMode(self) -> PrimitiveMode:
    """
    Calls Qt's 'PrimitiveMode ProceduralMesh::primitiveMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#primitiveMode

    Returns
    -------

    PrimitiveMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PrimitiveMode(number)'
      gives.
    """
    #  PrimitiveMode ProceduralMesh::primitiveMode() const
    return ProceduralMesh.PrimitiveMode(self.uglySide.call(
        'ritual_ZNK14ProceduralMesh13primitiveModeEv',
    ))

  def normals(self) -> QList[QVector3D]:
    """
    Calls Qt's 'QList<QVector3D> ProceduralMesh::normals() const'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#normals

    Returns
    -------

    QList[QVector3D]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QVector3D> ProceduralMesh::normals() const
    address = self.uglySide.call('ritual_ZNK14ProceduralMesh7normalsEv')
    from ..QtGui import QVector3D
    return QList[QVector3D]._cuteOwning(address)

  def tangents(self) -> QList[QVector3D]:
    """
    Calls Qt's 'QList<QVector3D> ProceduralMesh::tangents() const'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#tangents

    Returns
    -------

    QList[QVector3D]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QVector3D> ProceduralMesh::tangents() const
    address = self.uglySide.call('ritual_ZNK14ProceduralMesh8tangentsEv')
    from ..QtGui import QVector3D
    return QList[QVector3D]._cuteOwning(address)

  def binormals(self) -> QList[QVector3D]:
    """
    Calls Qt's 'QList<QVector3D> ProceduralMesh::binormals() const'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#binormals

    Returns
    -------

    QList[QVector3D]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QVector3D> ProceduralMesh::binormals() const
    address = self.uglySide.call('ritual_ZNK14ProceduralMesh9binormalsEv')
    from ..QtGui import QVector3D
    return QList[QVector3D]._cuteOwning(address)

  def uv0s(self) -> QList[QVector2D]:
    """
    Calls Qt's 'QList<QVector2D> ProceduralMesh::uv0s() const'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#uv0s

    Returns
    -------

    QList[QVector2D]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QVector2D> ProceduralMesh::uv0s() const
    address = self.uglySide.call('ritual_ZNK14ProceduralMesh4uv0sEv')
    from ..QtGui import QVector2D
    return QList[QVector2D]._cuteOwning(address)

  def uv1s(self) -> QList[QVector2D]:
    """
    Calls Qt's 'QList<QVector2D> ProceduralMesh::uv1s() const'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#uv1s

    Returns
    -------

    QList[QVector2D]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QVector2D> ProceduralMesh::uv1s() const
    address = self.uglySide.call('ritual_ZNK14ProceduralMesh4uv1sEv')
    from ..QtGui import QVector2D
    return QList[QVector2D]._cuteOwning(address)

  def colors(self) -> QList[QVector4D]:
    """
    Calls Qt's 'QList<QVector4D> ProceduralMesh::colors() const'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#colors

    Returns
    -------

    QList[QVector4D]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QVector4D> ProceduralMesh::colors() const
    address = self.uglySide.call('ritual_ZNK14ProceduralMesh6colorsEv')
    from ..QtGui import QVector4D
    return QList[QVector4D]._cuteOwning(address)

  def joints(self) -> QList[QVector4D]:
    """
    Calls Qt's 'QList<QVector4D> ProceduralMesh::joints() const'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#joints

    Returns
    -------

    QList[QVector4D]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QVector4D> ProceduralMesh::joints() const
    address = self.uglySide.call('ritual_ZNK14ProceduralMesh6jointsEv')
    from ..QtGui import QVector4D
    return QList[QVector4D]._cuteOwning(address)

  def weights(self) -> QList[QVector4D]:
    """
    Calls Qt's 'QList<QVector4D> ProceduralMesh::weights() const'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#weights

    Returns
    -------

    QList[QVector4D]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QVector4D> ProceduralMesh::weights() const
    address = self.uglySide.call('ritual_ZNK14ProceduralMesh7weightsEv')
    from ..QtGui import QVector4D
    return QList[QVector4D]._cuteOwning(address)

  def supportsTriangleFanPrimitive(self) -> bool:
    """
    Calls Qt's 'bool ProceduralMesh::supportsTriangleFanPrimitive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralmesh.html#supportsTriangleFanPrimitive
    """
    #  bool ProceduralMesh::supportsTriangleFanPrimitive() const
    return self.uglySide.call(
        'ritual_ZNK14ProceduralMesh28supportsTriangleFanPrimitiveEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QVector3D])
  def setPositions(self, newPositions: QList[QVector3D]) -> None:
    """
    Calls Qt's 'void ProceduralMesh::setPositions(const QList<QVector3D>
    &newPositions)'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#setPositions

    Parameters
    ----------

    newPositions : QList[QVector3D]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void ProceduralMesh::setPositions(const QList<QVector3D>
    #      &newPositions)
    self.uglySide.call(
        'ritual_ZN14ProceduralMesh12setPositionsERK5QListI9QVector3DE',
        self._valueOf(newPositions),
    )

  @overload(PrimitiveMode)
  def setPrimitiveMode(self, newPrimitiveMode: PrimitiveMode) -> None:
    """
    Calls Qt's 'void ProceduralMesh::setPrimitiveMode(PrimitiveMode
    newPrimitiveMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralmesh.html#setPrimitiveMode

    Parameters
    ----------

    newPrimitiveMode : PrimitiveMode
      Passed on as its number.
    """
    #  void ProceduralMesh::setPrimitiveMode(PrimitiveMode newPrimitiveMode)
    self.uglySide.call(
        'ritual_ZN14ProceduralMesh16setPrimitiveModeENS_13PrimitiveModeE',
        newPrimitiveMode.value,
    )

  @overload(QList[QVector3D])
  def setNormals(self, newNormals: QList[QVector3D]) -> None:
    """
    Calls Qt's 'void ProceduralMesh::setNormals(const QList<QVector3D>
    &newNormals)'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#setNormals

    Parameters
    ----------

    newNormals : QList[QVector3D]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void ProceduralMesh::setNormals(const QList<QVector3D> &newNormals)
    self.uglySide.call(
        'ritual_ZN14ProceduralMesh10setNormalsERK5QListI9QVector3DE',
        self._valueOf(newNormals),
    )

  @overload(QList[QVector3D])
  def setTangents(self, newTangents: QList[QVector3D]) -> None:
    """
    Calls Qt's 'void ProceduralMesh::setTangents(const QList<QVector3D>
    &newTangents)'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#setTangents

    Parameters
    ----------

    newTangents : QList[QVector3D]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void ProceduralMesh::setTangents(const QList<QVector3D> &newTangents)
    self.uglySide.call(
        'ritual_ZN14ProceduralMesh11setTangentsERK5QListI9QVector3DE',
        self._valueOf(newTangents),
    )

  @overload(QList[QVector3D])
  def setBinormals(self, newBinormals: QList[QVector3D]) -> None:
    """
    Calls Qt's 'void ProceduralMesh::setBinormals(const QList<QVector3D>
    &newBinormals)'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#setBinormals

    Parameters
    ----------

    newBinormals : QList[QVector3D]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void ProceduralMesh::setBinormals(const QList<QVector3D>
    #      &newBinormals)
    self.uglySide.call(
        'ritual_ZN14ProceduralMesh12setBinormalsERK5QListI9QVector3DE',
        self._valueOf(newBinormals),
    )

  @overload(QList[QVector2D])
  def setUv0s(self, newUv0s: QList[QVector2D]) -> None:
    """
    Calls Qt's 'void ProceduralMesh::setUv0s(const QList<QVector2D>
    &newUv0s)'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#setUv0s

    Parameters
    ----------

    newUv0s : QList[QVector2D]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void ProceduralMesh::setUv0s(const QList<QVector2D> &newUv0s)
    self.uglySide.call(
        'ritual_ZN14ProceduralMesh7setUv0sERK5QListI9QVector2DE',
        self._valueOf(newUv0s),
    )

  @overload(QList[QVector2D])
  def setUv1s(self, newUv1s: QList[QVector2D]) -> None:
    """
    Calls Qt's 'void ProceduralMesh::setUv1s(const QList<QVector2D>
    &newUv1s)'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#setUv1s

    Parameters
    ----------

    newUv1s : QList[QVector2D]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void ProceduralMesh::setUv1s(const QList<QVector2D> &newUv1s)
    self.uglySide.call(
        'ritual_ZN14ProceduralMesh7setUv1sERK5QListI9QVector2DE',
        self._valueOf(newUv1s),
    )

  @overload(QList[QVector4D])
  def setColors(self, newColors: QList[QVector4D]) -> None:
    """
    Calls Qt's 'void ProceduralMesh::setColors(const QList<QVector4D>
    &newColors)'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#setColors

    Parameters
    ----------

    newColors : QList[QVector4D]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void ProceduralMesh::setColors(const QList<QVector4D> &newColors)
    self.uglySide.call(
        'ritual_ZN14ProceduralMesh9setColorsERK5QListI9QVector4DE',
        self._valueOf(newColors),
    )

  @overload(QList[QVector4D])
  def setJoints(self, newJoints: QList[QVector4D]) -> None:
    """
    Calls Qt's 'void ProceduralMesh::setJoints(const QList<QVector4D>
    &newJoints)'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#setJoints

    Parameters
    ----------

    newJoints : QList[QVector4D]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void ProceduralMesh::setJoints(const QList<QVector4D> &newJoints)
    self.uglySide.call(
        'ritual_ZN14ProceduralMesh9setJointsERK5QListI9QVector4DE',
        self._valueOf(newJoints),
    )

  @overload(QList[QVector4D])
  def setWeights(self, newWeights: QList[QVector4D]) -> None:
    """
    Calls Qt's 'void ProceduralMesh::setWeights(const QList<QVector4D>
    &newWeights)'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#setWeights

    Parameters
    ----------

    newWeights : QList[QVector4D]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void ProceduralMesh::setWeights(const QList<QVector4D> &newWeights)
    self.uglySide.call(
        'ritual_ZN14ProceduralMesh10setWeightsERK5QListI9QVector4DE',
        self._valueOf(newWeights),
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
    Notes what was given, for Qt's 'ProceduralMesh::ProceduralMesh()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#ProceduralMesh
    """
    #  ProceduralMesh::ProceduralMesh()
    self._noteCreation(ProceduralMesh, lambda: Rituals.call(
        'ritual_ZN14ProceduralMeshC1Ev',
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

  def positionsChanged(self) -> None:
    """
    Calls Qt's 'void ProceduralMesh::positionsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralmesh.html#positionsChanged
    """
    #  void ProceduralMesh::positionsChanged()
    self.uglySide.call('ritual_ZN14ProceduralMesh16positionsChangedEv')

  def primitiveModeChanged(self) -> None:
    """
    Calls Qt's 'void ProceduralMesh::primitiveModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralmesh.html#primitiveModeChanged
    """
    #  void ProceduralMesh::primitiveModeChanged()
    self.uglySide.call('ritual_ZN14ProceduralMesh20primitiveModeChangedEv')

  def indexesChanged(self) -> None:
    """
    Calls Qt's 'void ProceduralMesh::indexesChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#indexesChanged
    """
    #  void ProceduralMesh::indexesChanged()
    self.uglySide.call('ritual_ZN14ProceduralMesh14indexesChangedEv')

  def normalsChanged(self) -> None:
    """
    Calls Qt's 'void ProceduralMesh::normalsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#normalsChanged
    """
    #  void ProceduralMesh::normalsChanged()
    self.uglySide.call('ritual_ZN14ProceduralMesh14normalsChangedEv')

  def tangentsChanged(self) -> None:
    """
    Calls Qt's 'void ProceduralMesh::tangentsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralmesh.html#tangentsChanged
    """
    #  void ProceduralMesh::tangentsChanged()
    self.uglySide.call('ritual_ZN14ProceduralMesh15tangentsChangedEv')

  def binormalsChanged(self) -> None:
    """
    Calls Qt's 'void ProceduralMesh::binormalsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralmesh.html#binormalsChanged
    """
    #  void ProceduralMesh::binormalsChanged()
    self.uglySide.call('ritual_ZN14ProceduralMesh16binormalsChangedEv')

  def uv0sChanged(self) -> None:
    """
    Calls Qt's 'void ProceduralMesh::uv0sChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#uv0sChanged
    """
    #  void ProceduralMesh::uv0sChanged()
    self.uglySide.call('ritual_ZN14ProceduralMesh11uv0sChangedEv')

  def uv1sChanged(self) -> None:
    """
    Calls Qt's 'void ProceduralMesh::uv1sChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#uv1sChanged
    """
    #  void ProceduralMesh::uv1sChanged()
    self.uglySide.call('ritual_ZN14ProceduralMesh11uv1sChangedEv')

  def colorsChanged(self) -> None:
    """
    Calls Qt's 'void ProceduralMesh::colorsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#colorsChanged
    """
    #  void ProceduralMesh::colorsChanged()
    self.uglySide.call('ritual_ZN14ProceduralMesh13colorsChangedEv')

  def jointsChanged(self) -> None:
    """
    Calls Qt's 'void ProceduralMesh::jointsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#jointsChanged
    """
    #  void ProceduralMesh::jointsChanged()
    self.uglySide.call('ritual_ZN14ProceduralMesh13jointsChangedEv')

  def weightsChanged(self) -> None:
    """
    Calls Qt's 'void ProceduralMesh::weightsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#weightsChanged
    """
    #  void ProceduralMesh::weightsChanged()
    self.uglySide.call('ritual_ZN14ProceduralMesh14weightsChangedEv')

  def requestUpdate(self) -> None:
    """
    Calls Qt's 'void ProceduralMesh::requestUpdate()'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#requestUpdate
    """
    #  void ProceduralMesh::requestUpdate()
    self.uglySide.call('ritual_ZN14ProceduralMesh13requestUpdateEv')

  def updateGeometry(self) -> None:
    """
    Calls Qt's 'void ProceduralMesh::updateGeometry()'.

    Qt's own words: https://doc.qt.io/qt-6/proceduralmesh.html#updateGeometry
    """
    #  void ProceduralMesh::updateGeometry()
    self.uglySide.call('ritual_ZN14ProceduralMesh14updateGeometryEv')

  @overload(QObject)
  @overload(NoneType)
  def subsetDestroyed(self, subset: Optional[QObject]) -> None:
    """
    Calls Qt's 'void ProceduralMesh::subsetDestroyed(QObject *subset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/proceduralmesh.html#subsetDestroyed

    Parameters
    ----------

    subset : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void ProceduralMesh::subsetDestroyed(QObject *subset)
    self.uglySide.call(
        'ritual_ZN14ProceduralMesh15subsetDestroyedEP7QObject',
        self._addressOf(subset, 'QObject'),
    )

  @staticmethod
  def indexes(*__, **_) -> Never:
    """
    Qt's 'QList<unsigned int> ProceduralMesh::indexes() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'ProceduralMesh.indexes' has no cute function yet. Qt's "
        "'QList<unsigned int> ProceduralMesh::indexes() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def qmlAppendProceduralMeshSubset(*__, **_) -> Never:
    """
    Qt's 'void ProceduralMesh::qmlAppendProceduralMeshSubset(
    QQmlListProperty<ProceduralMeshSubset> *list, ProceduralMeshSubset
    *subset)': names 'QQmlListProperty<ProceduralMeshSubset>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'ProceduralMesh.qmlAppendProceduralMeshSubset' has no cute "
        "function yet. Qt's 'void "
        "ProceduralMesh::qmlAppendProceduralMeshSubset(QQmlListProperty<Proc"
        "eduralMeshSubset> *list, ProceduralMeshSubset *subset)': names "
        "'QQmlListProperty<ProceduralMeshSubset>', which has no cute class "
        "yet.")

  @staticmethod
  def qmlClearProceduralMeshSubset(*__, **_) -> Never:
    """
    Qt's 'void ProceduralMesh::qmlClearProceduralMeshSubset(
    QQmlListProperty<ProceduralMeshSubset> *list)': names
    'QQmlListProperty<ProceduralMeshSubset>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'ProceduralMesh.qmlClearProceduralMeshSubset' has no cute function "
        "yet. Qt's 'void "
        "ProceduralMesh::qmlClearProceduralMeshSubset(QQmlListProperty<Proce"
        "duralMeshSubset> *list)': names "
        "'QQmlListProperty<ProceduralMeshSubset>', which has no cute class "
        "yet.")

  @staticmethod
  def qmlProceduralMeshSubsetAt(*__, **_) -> Never:
    """
    Qt's 'ProceduralMeshSubset *ProceduralMesh::qmlProceduralMeshSubsetAt(
    QQmlListProperty<ProceduralMeshSubset> *list, qsizetype index)': names
    'QQmlListProperty<ProceduralMeshSubset>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'ProceduralMesh.qmlProceduralMeshSubsetAt' has no cute function "
        "yet. Qt's 'ProceduralMeshSubset "
        "*ProceduralMesh::qmlProceduralMeshSubsetAt(QQmlListProperty<Procedu"
        "ralMeshSubset> *list, qsizetype index)': names "
        "'QQmlListProperty<ProceduralMeshSubset>', which has no cute class "
        "yet.")

  @staticmethod
  def qmlProceduralMeshSubsetCount(*__, **_) -> Never:
    """
    Qt's 'qsizetype ProceduralMesh::qmlProceduralMeshSubsetCount(
    QQmlListProperty<ProceduralMeshSubset> *list)': names
    'QQmlListProperty<ProceduralMeshSubset>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'ProceduralMesh.qmlProceduralMeshSubsetCount' has no cute function "
        "yet. Qt's 'qsizetype "
        "ProceduralMesh::qmlProceduralMeshSubsetCount(QQmlListProperty<Proce"
        "duralMeshSubset> *list)': names "
        "'QQmlListProperty<ProceduralMeshSubset>', which has no cute class "
        "yet.")

  @staticmethod
  def setIndexes(*__, **_) -> Never:
    """
    Qt's 'void ProceduralMesh::setIndexes(const QList<unsigned int>
    &newIndexes)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'ProceduralMesh.setIndexes' has no cute function yet. Qt's 'void "
        "ProceduralMesh::setIndexes(const QList<unsigned int> "
        "&newIndexes)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def subsets(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<ProceduralMeshSubset> ProceduralMesh::subsets()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'ProceduralMesh.subsets' has no cute function yet. Qt's "
        "'QQmlListProperty<ProceduralMeshSubset> "
        "ProceduralMesh::subsets()': gives a type Python has no way to take "
        "yet.")
