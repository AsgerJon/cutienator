"""
QSSGClippingFrustum binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderclippingfrustum_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGClippingFrustum to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtGui import QMatrix4x4, QVector3D
  from ..QtQuick3DUtils import QSSGBounds3
  from . import QSSGClipPlane
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QSSGBounds3 = WAIT['QSSGBounds3']
  QSSGClipPlane = WAIT['QSSGClipPlane']
  QVector3D = WAIT['QVector3D']


class QSSGClippingFrustum(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGClippingFrustum: a plain Python object standing
  in front of one C++ QSSGClippingFrustum.

  C++ hands a QSSGClippingFrustum around as a copy, so every C++
  QSSGClippingFrustum behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSSGClippingFrustum that has a ritual and that
  Python can call so far, 1 name in all: 'intersectsWith'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGClippingFrustum::~QSSGClippingFrustum()': the destructor:
    Python removes its C++ QSSGClippingFrustum by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QSSGClippingFrustum is created at the first use, not by
    'QSSGClippingFrustum(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGClippingFrustum back gives a copy the ritual made
    for Python, in a new cute QSSGClippingFrustum.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGClippingFrustum'

  #  Qt's '~QSSGClippingFrustum()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGClippingFrustum behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QSSGClippingFrustumD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSSGBounds3)
  def intersectsWith(self, bounds: QSSGBounds3) -> bool:
    """
    Calls Qt's 'bool QSSGClippingFrustum::intersectsWith(const QSSGBounds3
    &bounds) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgclippingfrustum.html#intersectsWith

    Parameters
    ----------

    bounds : QSSGBounds3
      Passed on as a value: Qt reads the C++ QSSGBounds3, which stays
      Python's own.
    """
    #  bool QSSGClippingFrustum::intersectsWith(const QSSGBounds3 &bounds)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QSSGClippingFrustum14intersectsWithERK11QSSGBounds3',
        self._valueOf(bounds),
    )

  @overload(QVector3D)
  @overload(QVector3D, float)
  def intersectsWith(self, point: QVector3D, radius: float = 0.0) -> bool:
    """
    Calls Qt's 'bool QSSGClippingFrustum::intersectsWith(const QVector3D
    &point, float radius) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgclippingfrustum.html#intersectsWith

    Parameters
    ----------

    point : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    radius : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  bool QSSGClippingFrustum::intersectsWith(const QVector3D &point, float
    #      radius) const
    return self.uglySide.call(
        'ritual_ZNK19QSSGClippingFrustum14intersectsWithERK9QVector3Df',
        self._valueOf(point), radius,
    )

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
    Notes what was given, for Qt's
    'QSSGClippingFrustum::QSSGClippingFrustum()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgclippingfrustum.html#QSSGClippingFrustum
    """
    #  QSSGClippingFrustum::QSSGClippingFrustum()
    self._noteCreation(QSSGClippingFrustum, lambda: Rituals.call(
        'ritual_ZN19QSSGClippingFrustumC1Ev',
    ))

  @overload(QMatrix4x4, QSSGClipPlane)
  def __init__(
      self,
      modelviewprojection: QMatrix4x4,
      nearPlane: QSSGClipPlane,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSSGClippingFrustum::QSSGClippingFrustum(const QMatrix4x4
    &modelviewprojection, const QSSGClipPlane &nearPlane)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgclippingfrustum.html#QSSGClippingFrustum

    Parameters
    ----------

    modelviewprojection : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    nearPlane : QSSGClipPlane
      Passed on as a value: Qt reads the C++ QSSGClipPlane, which stays
      Python's own.
    """
    #  QSSGClippingFrustum::QSSGClippingFrustum(const QMatrix4x4
    #      &modelviewprojection, const QSSGClipPlane &nearPlane)
    self._noteCreation(QSSGClippingFrustum, lambda: Rituals.call(
        'ritual_ZN19QSSGClippingFrustumC1ERK10QMatrix4x4RK13QSSGClipPlane',
        self._valueOf(modelviewprojection), self._valueOf(nearPlane),
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
