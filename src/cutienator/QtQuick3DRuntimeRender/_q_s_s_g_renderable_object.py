"""
QSSGRenderableObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderableobjects_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderableObject to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtGui import QVector3D
  from ..QtQuick3DUtils import QSSGBounds3
  from . import QSSGRenderableObjectFlags
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSSGBounds3 = WAIT['QSSGBounds3']
  QSSGRenderableObjectFlags = WAIT['QSSGRenderableObjectFlags']
  QVector3D = WAIT['QVector3D']


class QSSGRenderableObject(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRenderableObject: a plain Python object standing
  in front of one C++ QSSGRenderableObject.

  What exists
  -----------

  No function of Qt's QSSGRenderableObject yet. It can be made from Python,
  in 1 way; see '__init__'.

  What has no ritual
  ------------------

  4 of the 5 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QSSGRenderableObject is created at the first use, not by
    'QSSGRenderableObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRenderableObject.
  """

  #  The enums Qt writes inside QSSGRenderableObject, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Type(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderableObject::Type' of Qt, with the 3 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    DefaultMaterialMeshSubset = Kee[int](0)
    CustomMaterialMeshSubset = Kee[int](1)
    Particles = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderableObject'

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

  @overload(Type, QSSGRenderableObjectFlags, QVector3D, QSSGBounds3, float)
  @overload(
      Type, QSSGRenderableObjectFlags, QVector3D, QSSGBounds3, float, float,
  )
  @overload(
      Type, QSSGRenderableObjectFlags, QVector3D, QSSGBounds3, float, float,
      float,
  )
  def __init__(
      self,
      ty: Type,
      inFlags: QSSGRenderableObjectFlags,
      inWorldCenterPt: QVector3D,
      inBounds: QSSGBounds3,
      inDepthBias: float,
      inMinThreshold: float = -1.0,
      inMaxThreshold: float = -1.0,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSSGRenderableObject::QSSGRenderableObject(Type ty,
    QSSGRenderableObjectFlags inFlags, const QVector3D &inWorldCenterPt,
    const QSSGBounds3 &inBounds, float inDepthBias, float inMinThreshold,
    float inMaxThreshold)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobject.html#QSSGRenderableObject

    Parameters
    ----------

    ty : Type
      Passed on as its number.

    inFlags : QSSGRenderableObjectFlags
      Passed on as a value: Qt reads the C++ QSSGRenderableObjectFlags, which
      stays Python's own.

    inWorldCenterPt : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    inBounds : QSSGBounds3
      Passed on as a value: Qt reads the C++ QSSGBounds3, which stays
      Python's own.

    inDepthBias : float
      Passed on as it is.

    inMinThreshold : float
      Passed on as it is. May be left out, as in Qt: it is then -1.0.

    inMaxThreshold : float
      Passed on as it is. May be left out, as in Qt: it is then -1.0.
    """
    #  QSSGRenderableObject::QSSGRenderableObject(Type ty,
    #      QSSGRenderableObjectFlags inFlags, const QVector3D
    #      &inWorldCenterPt, const QSSGBounds3 &inBounds, float inDepthBias,
    #      float inMinThreshold, float inMaxThreshold)
    self._noteCreation(QSSGRenderableObject, lambda: Rituals.call(
        'ritual_ZN20QSSGRenderableObjectC1ENS_4TypeE25QSSGRenderableObjectF'
        'lagsRK9QVector3DRK11QSSGBounds3fff',
        ty.value, self._valueOf(inFlags), self._valueOf(inWorldCenterPt),
        self._valueOf(inBounds), inDepthBias, inMinThreshold, inMaxThreshold,
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
