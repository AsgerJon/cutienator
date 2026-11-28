"""
QSSGRenderRay binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderray_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderRay to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtGui import QMatrix4x4, QVector2D, QVector3D
  from ..QtQuick3DUtils import QSSGBounds3
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QSSGBounds3 = WAIT['QSSGBounds3']
  QVector3D = WAIT['QVector3D']


class QSSGRenderRay(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRenderRay: a plain Python object standing in
  front of one C++ QSSGRenderRay.

  C++ hands a QSSGRenderRay around as a copy, so every C++ QSSGRenderRay
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGRenderRay that has a ritual and that Python can
  call so far, 3 names in all: 'createRayData', 'createIntersectionResult',
  'intersectWithAABBv2'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'std::optional<QVector3D> QSSGRenderRay::intersect(const QSSGPlane
    &inPlane, const QSSGRenderRay &ray)': gives a type Python has no way to
    take yet.
  - Qt's 'bool QSSGRenderRay::triangleIntersect(const QSSGRenderRay &ray,
    const QVector3D &v0, const QVector3D &v1, const QVector3D &v2, float &u,
    float &v, QVector3D &normal, QSSGCullFaceMode cullMode)': takes a number
    to change where it is.
  - Qt's 'void QSSGRenderRay::intersectWithBVH(const RayData &data, const
    QSSGMeshBVHNode *bvh, const QSSGRenderMesh *mesh,
    QVector<IntersectionResult> &intersections, QSSGCullFaceMode cullMode,
    int depth)': takes a type Python has no way to hand over yet.
  - Qt's 'QVector<IntersectionResult>
    QSSGRenderRay::intersectWithBVHTriangles(const RayData &data, const
    std::vector<QSSGMeshBVHTriangle> &bvhTriangles, int triangleOffset, int
    triangleCount, QSSGCullFaceMode cullMode)': takes a type Python has no
    way to hand over yet.
  - Qt's 'std::optional<QVector2D> QSSGRenderRay::relative(const QMatrix4x4
    &inGlobalTransform, const QSSGBounds3 &inBounds, QSSGRenderBasisPlanes
    inPlane) const': names the enum 'QSSGRenderBasisPlanes', whose class
    cannot be named here.
  - Qt's 'std::optional<QVector2D> QSSGRenderRay::relativeXY(const QMatrix4x4
    &inGlobalTransform, const QSSGBounds3 &inBounds) const': gives a type
    Python has no way to take yet.
  - Qt's 'QSSGRenderRay::~QSSGRenderRay()': the destructor: Python removes
    its C++ QSSGRenderRay by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QSSGRenderRay is created at the first use, not by
    'QSSGRenderRay(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGRenderRay back gives a copy the ritual made for
    Python, in a new cute QSSGRenderRay.
  - Each name of Qt's QSSGRenderRay that has no cute function yet,
    'intersect', 'intersectWithBVH', 'intersectWithBVHTriangles', 'relative',
    'relativeXY', 'triangleIntersect', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QSSGRenderRay, each a class in here as in
  #  C++.

  class HitResult(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGRenderRay::HitResult: a plain Python object
    standing in front of one C++ QSSGRenderRay::HitResult.

    C++ hands a QSSGRenderRay::HitResult around as a copy, so every C++
    QSSGRenderRay::HitResult behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QSSGRenderRay::HitResult that has a ritual and
    that Python can call so far, 1 name in all: 'intersects'. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGRenderRay::HitResult::~HitResult()': the destructor: Python
      removes its C++ QSSGRenderRay::HitResult by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QSSGRenderRay::HitResult is created at the first use, not by
      'QSSGRenderRay::HitResult(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGRenderRay::HitResult back gives a copy the
      ritual made for Python, in a new cute QSSGRenderRay::HitResult.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGRenderRay::HitResult'

    #  Qt's '~QSSGRenderRay::HitResult()'. Naming it makes this a value
    #  class: Python owns every C++ QSSGRenderRay::HitResult behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN13QSSGRenderRay9HitResultD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def intersects(self) -> bool:
      """
      Calls Qt's 'bool QSSGRenderRay::HitResult::intersects() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgrenderray-hitresult.html#intersects
      """
      #  bool QSSGRenderRay::HitResult::intersects() const
      return self.uglySide.call(
          'ritual_ZNK13QSSGRenderRay9HitResult10intersectsEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class IntersectionResult(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGRenderRay::IntersectionResult: a plain Python
    object standing in front of one C++ QSSGRenderRay::IntersectionResult.

    C++ hands a QSSGRenderRay::IntersectionResult around as a copy, so every
    C++ QSSGRenderRay::IntersectionResult behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QSSGRenderRay::IntersectionResult yet. It can be made
    from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGRenderRay::IntersectionResult::~IntersectionResult()': the
      destructor: Python removes its C++ QSSGRenderRay::IntersectionResult by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QSSGRenderRay::IntersectionResult is created at the first use,
      not by 'QSSGRenderRay::IntersectionResult(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGRenderRay::IntersectionResult back gives a copy
      the ritual made for Python, in a new cute
      QSSGRenderRay::IntersectionResult.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QVector2D = WAIT['QVector2D']
      QVector3D = WAIT['QVector3D']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGRenderRay::IntersectionResult'

    #  Qt's '~QSSGRenderRay::IntersectionResult()'. Naming it makes this a
    #  value class: Python owns every C++ QSSGRenderRay::IntersectionResult
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN13QSSGRenderRay18IntersectionResultD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QSSGRenderRay::IntersectionResult::IntersectionResult()', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgrenderray-intersectionresult.html
      """
      #  QSSGRenderRay::IntersectionResult::IntersectionResult()
      self._noteCreation(
          QSSGRenderRay.IntersectionResult, lambda: Rituals.call(
              'ritual_ZN13QSSGRenderRay18IntersectionResultC1Ev',
          ))

    @overload(float, QVector2D, QVector3D, QVector3D, QVector3D, QVector3D)
    def __init__(
        self,
        rl: float,
        relxy: QVector2D,
        scenePosition: QVector3D,
        localPosition: QVector3D,
        normal: QVector3D,
        sceneNormal: QVector3D,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QSSGRenderRay::IntersectionResult::IntersectionResult(float rl, const
      QVector2D &relxy, const QVector3D &scenePosition, const QVector3D
      &localPosition, const QVector3D &normal, const QVector3D
      &sceneNormal)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgrenderray-intersectionresult.html

      Parameters
      ----------

      rl : float
        Passed on as it is.

      relxy : QVector2D
        Passed on as a value: Qt reads the C++ QVector2D, which stays
        Python's own.

      scenePosition : QVector3D
        Passed on as a value: Qt reads the C++ QVector3D, which stays
        Python's own.

      localPosition : QVector3D
        Passed on as a value: Qt reads the C++ QVector3D, which stays
        Python's own.

      normal : QVector3D
        Passed on as a value: Qt reads the C++ QVector3D, which stays
        Python's own.

      sceneNormal : QVector3D
        Passed on as a value: Qt reads the C++ QVector3D, which stays
        Python's own.
      """
      #  QSSGRenderRay::IntersectionResult::IntersectionResult(float rl,
      #      const QVector2D &relxy, const QVector3D &scenePosition, const
      #      QVector3D &localPosition, const QVector3D &normal, const
      #      QVector3D &sceneNormal)
      self._noteCreation(
          QSSGRenderRay.IntersectionResult, lambda: Rituals.call(
              'ritual_ZN13QSSGRenderRay18IntersectionResultC1EfRK9QVector2D'
              'RK9QVector3DS6_S6_S6_',
              rl, self._valueOf(relxy), self._valueOf(scenePosition),
              self._valueOf(localPosition), self._valueOf(normal),
              self._valueOf(sceneNormal),
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class RayData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGRenderRay::RayData: a plain Python object
    standing in front of one C++ QSSGRenderRay::RayData.

    C++ hands a QSSGRenderRay::RayData around as a copy, so every C++
    QSSGRenderRay::RayData behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QSSGRenderRay::RayData yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGRenderRay::RayData::~RayData()': the destructor: Python
      removes its C++ QSSGRenderRay::RayData by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QSSGRenderRay::RayData is created at the first use, not by
      'QSSGRenderRay::RayData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGRenderRay::RayData back gives a copy the ritual
      made for Python, in a new cute QSSGRenderRay::RayData.
    """

    #  The enums Qt writes inside QSSGRenderRay::RayData, each a class in
    #  here as in C++, and the names Qt has for the combinations of its flags
    #  enums.

    class DirectionOp(CuteNum, scoped=True):
      """
      The enum 'QSSGRenderRay::RayData::DirectionOp' of Qt, with the 3 names
      Qt gives in it. C++ keeps these names inside the enum, so the class
      that holds the enum does not have them.
      """

      Normal = Kee[int](0)
      Swap = Kee[int](1)
      Zero = Kee[int](16)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGRenderRay::RayData'

    #  Qt's '~QSSGRenderRay::RayData()'. Naming it makes this a value class:
    #  Python owns every C++ QSSGRenderRay::RayData behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN13QSSGRenderRay7RayDataD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QMatrix4x4, THIS)
  def createRayData(
      globalTransform: QMatrix4x4,
      ray: QSSGRenderRay,
  ) -> RayData:
    """
    Calls Qt's 'RayData QSSGRenderRay::createRayData(const QMatrix4x4
    &globalTransform, const QSSGRenderRay &ray)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderray.html#createRayData

    Parameters
    ----------

    globalTransform : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    ray : QSSGRenderRay
      Passed on as a value: Qt reads the C++ QSSGRenderRay, which stays
      Python's own.

    Returns
    -------

    RayData
      A new cute QSSGRenderRay::RayData around the copy Qt gave back. Python
      owns it.
    """
    #  RayData QSSGRenderRay::createRayData(const QMatrix4x4
    #      &globalTransform, const QSSGRenderRay &ray)
    address = Rituals.call(
        'ritual_ZN13QSSGRenderRay13createRayDataERK10QMatrix4x4RKS_',
        CuteMixin._valueOf(globalTransform), CuteMixin._valueOf(ray),
    )
    return QSSGRenderRay.RayData._cuteOwning(address)

  @staticmethod
  @overload(RayData, HitResult)
  def createIntersectionResult(
      data: RayData,
      hit: HitResult,
  ) -> IntersectionResult:
    """
    Calls Qt's 'IntersectionResult
    QSSGRenderRay::createIntersectionResult(const RayData &data, const
    HitResult &hit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderray.html#createIntersectionResult

    Parameters
    ----------

    data : RayData
      Passed on as a value: Qt reads the C++ QSSGRenderRay::RayData, which
      stays Python's own.

    hit : HitResult
      Passed on as a value: Qt reads the C++ QSSGRenderRay::HitResult, which
      stays Python's own.

    Returns
    -------

    IntersectionResult
      A new cute QSSGRenderRay::IntersectionResult around the copy Qt gave
      back. Python owns it.
    """
    #  IntersectionResult QSSGRenderRay::createIntersectionResult(const
    #      RayData &data, const HitResult &hit)
    address = Rituals.call(
        'ritual_ZN13QSSGRenderRay24createIntersectionResultERKNS_7RayDataER'
        'KNS_9HitResultE',
        CuteMixin._valueOf(data), CuteMixin._valueOf(hit),
    )
    return QSSGRenderRay.IntersectionResult._cuteOwning(address)

  @staticmethod
  @overload(RayData, QSSGBounds3)
  def intersectWithAABBv2(data: RayData, bounds: QSSGBounds3) -> HitResult:
    """
    Calls Qt's 'HitResult QSSGRenderRay::intersectWithAABBv2(const RayData
    &data, const QSSGBounds3 &bounds)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderray.html#intersectWithAABBv2

    Parameters
    ----------

    data : RayData
      Passed on as a value: Qt reads the C++ QSSGRenderRay::RayData, which
      stays Python's own.

    bounds : QSSGBounds3
      Passed on as a value: Qt reads the C++ QSSGBounds3, which stays
      Python's own.

    Returns
    -------

    HitResult
      A new cute QSSGRenderRay::HitResult around the copy Qt gave back.
      Python owns it.
    """
    #  HitResult QSSGRenderRay::intersectWithAABBv2(const RayData &data,
    #      const QSSGBounds3 &bounds)
    address = Rituals.call(
        'ritual_ZN13QSSGRenderRay19intersectWithAABBv2ERKNS_7RayDataERK11QS'
        'SGBounds3',
        CuteMixin._valueOf(data), CuteMixin._valueOf(bounds),
    )
    return QSSGRenderRay.HitResult._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderRay'

  #  Qt's '~QSSGRenderRay()'. Naming it makes this a value class: Python owns
  #  every C++ QSSGRenderRay behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13QSSGRenderRayD1Ev'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QSSGRenderRay::QSSGRenderRay()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderray.html#QSSGRenderRay
    """
    #  QSSGRenderRay::QSSGRenderRay()
    self._noteCreation(QSSGRenderRay, lambda: Rituals.call(
        'ritual_ZN13QSSGRenderRayC1Ev',
    ))

  @overload(QVector3D, QVector3D)
  def __init__(self, inOrigin: QVector3D, inDirection: QVector3D) -> None:
    """
    Notes what was given, for Qt's 'QSSGRenderRay::QSSGRenderRay(const
    QVector3D &inOrigin, const QVector3D &inDirection)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderray.html#QSSGRenderRay

    Parameters
    ----------

    inOrigin : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    inDirection : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  QSSGRenderRay::QSSGRenderRay(const QVector3D &inOrigin, const
    #      QVector3D &inDirection)
    self._noteCreation(QSSGRenderRay, lambda: Rituals.call(
        'ritual_ZN13QSSGRenderRayC1ERK9QVector3DS2_',
        self._valueOf(inOrigin), self._valueOf(inDirection),
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
  def intersect(*__, **_) -> Never:
    """
    Qt's 'std::optional<QVector3D> QSSGRenderRay::intersect(const QSSGPlane
    &inPlane, const QSSGRenderRay &ray)': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QSSGRenderRay.intersect' has no cute function yet. Qt's "
        "'std::optional<QVector3D> QSSGRenderRay::intersect(const QSSGPlane "
        "&inPlane, const QSSGRenderRay &ray)': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def intersectWithBVH(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderRay::intersectWithBVH(const RayData &data, const
    QSSGMeshBVHNode *bvh, const QSSGRenderMesh *mesh,
    QVector<IntersectionResult> &intersections, QSSGCullFaceMode cullMode,
    int depth)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderRay.intersectWithBVH' has no cute function yet. Qt's "
        "'void QSSGRenderRay::intersectWithBVH(const RayData &data, const "
        "QSSGMeshBVHNode *bvh, const QSSGRenderMesh *mesh, "
        "QVector<IntersectionResult> &intersections, QSSGCullFaceMode "
        "cullMode, int depth)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def intersectWithBVHTriangles(*__, **_) -> Never:
    """
    Qt's 'QVector<IntersectionResult>
    QSSGRenderRay::intersectWithBVHTriangles(const RayData &data, const
    std::vector<QSSGMeshBVHTriangle> &bvhTriangles, int triangleOffset, int
    triangleCount, QSSGCullFaceMode cullMode)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderRay.intersectWithBVHTriangles' has no cute function "
        "yet. Qt's 'QVector<IntersectionResult> "
        "QSSGRenderRay::intersectWithBVHTriangles(const RayData &data, "
        "const std::vector<QSSGMeshBVHTriangle> &bvhTriangles, int "
        "triangleOffset, int triangleCount, QSSGCullFaceMode cullMode)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def relative(*__, **_) -> Never:
    """
    Qt's 'std::optional<QVector2D> QSSGRenderRay::relative(const QMatrix4x4
    &inGlobalTransform, const QSSGBounds3 &inBounds, QSSGRenderBasisPlanes
    inPlane) const': names the enum 'QSSGRenderBasisPlanes', whose class
    cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGRenderRay.relative' has no cute function yet. Qt's "
        "'std::optional<QVector2D> QSSGRenderRay::relative(const QMatrix4x4 "
        "&inGlobalTransform, const QSSGBounds3 &inBounds, "
        "QSSGRenderBasisPlanes inPlane) const': names the enum "
        "'QSSGRenderBasisPlanes', whose class cannot be named here.")

  @staticmethod
  def relativeXY(*__, **_) -> Never:
    """
    Qt's 'std::optional<QVector2D> QSSGRenderRay::relativeXY(const QMatrix4x4
    &inGlobalTransform, const QSSGBounds3 &inBounds) const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSSGRenderRay.relativeXY' has no cute function yet. Qt's "
        "'std::optional<QVector2D> QSSGRenderRay::relativeXY(const "
        "QMatrix4x4 &inGlobalTransform, const QSSGBounds3 &inBounds) "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def triangleIntersect(*__, **_) -> Never:
    """
    Qt's 'bool QSSGRenderRay::triangleIntersect(const QSSGRenderRay &ray,
    const QVector3D &v0, const QVector3D &v1, const QVector3D &v2, float &u,
    float &v, QVector3D &normal, QSSGCullFaceMode cullMode)': takes a number
    to change where it is.
    """
    raise NotImplementedError(
        "'QSSGRenderRay.triangleIntersect' has no cute function yet. Qt's "
        "'bool QSSGRenderRay::triangleIntersect(const QSSGRenderRay &ray, "
        "const QVector3D &v0, const QVector3D &v1, const QVector3D &v2, "
        "float &u, float &v, QVector3D &normal, QSSGCullFaceMode "
        "cullMode)': takes a number to change where it is.")
