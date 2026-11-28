"""
QSSGRenderCamera binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercamera_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderCamera to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtGui import QVector2D
from . import QSSGRenderGraphObject, QSSGRenderNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QRectF
  from ..QtGui import QMatrix4x4, QVector3D
  from . import QSSGRenderCameraConfiguration, QSSGRenderRay
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QRectF = WAIT['QRectF']
  QSSGRenderCameraConfiguration = WAIT['QSSGRenderCameraConfiguration']
  QVector2D = WAIT['QVector2D']
  QVector3D = WAIT['QVector3D']


class QSSGRenderCamera(QSSGRenderNode):
  """
  The cute side of Qt's QSSGRenderCamera: a plain Python object standing in
  front of one C++ QSSGRenderCamera.

  It is built on the cute 'QSSGRenderNode', as Qt's QSSGRenderCamera is built
  on Qt's QSSGRenderNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSSGRenderCamera that has a ritual and that Python
  can call so far, 8 names in all: 'lookAt', 'calculateProjection',
  'unproject', 'isDirty', 'markDirty', 'clearDirty',
  'getLevelOfDetailMultiplier', 'getDpr'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QSSGRenderCamera::calculateProjectionInternal(QSSGRenderCamera
    &camera, const QRectF &inViewport, Configuration config)': takes a type
    Python has no way to hand over yet.
  - Qt's 'bool QSSGRenderCamera::computeFrustumOrtho(QRectF inViewport,
    QSSGRenderCamera::ClipPlanes clipPlanes, QSSGRenderCamera::Magnification
    magnification, Configuration config, QMatrix4x4 &outProjection)': takes a
    type Python has no way to hand over yet.
  - Qt's 'bool QSSGRenderCamera::computeFrustumPerspective(QRectF inViewport,
    FieldOfView fov, QSSGRenderCamera::ClipPlanes clipPlanes, QMatrix4x4
    &outProjection)': takes a type Python has no way to hand over yet.
  - Qt's 'bool
    QSSGRenderCamera::computeCustomFrustum(QSSGRenderCamera::Frustum frustum,
    QSSGRenderCamera::ClipPlanes clipPlanes, QMatrix4x4 &outProjection)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGRenderCamera::calculateViewProjectionMatrix(const
    QMatrix4x4 &globalTransform, const QMatrix4x4 &projection, QMatrix4x4
    &outMatrix)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSSGRenderCamera::calculateViewProjectionMatrix(const
    QMatrix4x4 &globalTransform, QMatrix4x4 &outMatrix) const': takes a type
    Python has no way to hand over yet.
  - Qt's 'void
    QSSGRenderCamera::calculateViewProjectionWithoutTranslation(const
    QMatrix4x4 &globalTransform, float near, float far, QMatrix4x4
    &outMatrix) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  1 of the 17 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QSSGRenderCamera is created at the first use, not by
    'QSSGRenderCamera(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRenderCamera.
  - Each name of Qt's QSSGRenderCamera that has no cute function yet,
    'calculateProjectionInternal', 'calculateViewProjectionMatrix',
    'calculateViewProjectionWithoutTranslation', 'computeCustomFrustum',
    'computeFrustumOrtho', 'computeFrustumPerspective',
    'setCustomProjection', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSSGRenderCamera, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class DirtyFlag(CuteNum, scoped=True):
    """
    The enum 'QSSGRenderCamera::DirtyFlag' of Qt, with the 2 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    CameraDirty = Kee[int](1)
    LayerMaskDirty = Kee[int](2)

  #  The classes Qt writes inside QSSGRenderCamera, each a class in here as
  #  in C++.

  class ClipPlanes(QVector2D):
    """
    The cute side of Qt's QSSGRenderCamera::ClipPlanes: a plain Python object
    standing in front of one C++ QSSGRenderCamera::ClipPlanes.

    It is built on the cute 'QVector2D', as Qt's QSSGRenderCamera::ClipPlanes
    is built on Qt's QVector2D, and has everything that class has.

    C++ hands a QSSGRenderCamera::ClipPlanes around as a copy, so every C++
    QSSGRenderCamera::ClipPlanes behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QSSGRenderCamera::ClipPlanes that has a ritual and
    that Python can call so far, 4 names in all: 'clipNear', 'clipFar',
    'setClipNear', 'setClipFar'. It can be made from Python, in 2 ways; see
    '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGRenderCamera::ClipPlanes::~ClipPlanes()': the destructor:
      Python removes its C++ QSSGRenderCamera::ClipPlanes by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QSSGRenderCamera::ClipPlanes is created at the first use, not
      by 'QSSGRenderCamera::ClipPlanes(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGRenderCamera::ClipPlanes back gives a copy the
      ritual made for Python, in a new cute QSSGRenderCamera::ClipPlanes.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGRenderCamera::ClipPlanes'

    #  Qt's '~QSSGRenderCamera::ClipPlanes()'. Naming it makes this a value
    #  class: Python owns every C++ QSSGRenderCamera::ClipPlanes behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QSSGRenderCamera10ClipPlanesD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def clipNear(self) -> float:
      """
      Calls Qt's 'float QSSGRenderCamera::ClipPlanes::clipNear() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgrendercamera-clipplanes.html#clipNear
      """
      #  float QSSGRenderCamera::ClipPlanes::clipNear() const
      return self.uglySide.call(
          'ritual_ZNK16QSSGRenderCamera10ClipPlanes8clipNearEv',
      )

    def clipFar(self) -> float:
      """
      Calls Qt's 'float QSSGRenderCamera::ClipPlanes::clipFar() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgrendercamera-clipplanes.html#clipFar
      """
      #  float QSSGRenderCamera::ClipPlanes::clipFar() const
      return self.uglySide.call(
          'ritual_ZNK16QSSGRenderCamera10ClipPlanes7clipFarEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(float)
    def setClipNear(self, n: float) -> None:
      """
      Calls Qt's 'void QSSGRenderCamera::ClipPlanes::setClipNear(float n)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgrendercamera-clipplanes.html#setClipNear

      Parameters
      ----------

      n : float
        Passed on as it is.
      """
      #  void QSSGRenderCamera::ClipPlanes::setClipNear(float n)
      self.uglySide.call(
          'ritual_ZN16QSSGRenderCamera10ClipPlanes11setClipNearEf', n,
      )

    @overload(float)
    def setClipFar(self, f: float) -> None:
      """
      Calls Qt's 'void QSSGRenderCamera::ClipPlanes::setClipFar(float f)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgrendercamera-clipplanes.html#setClipFar

      Parameters
      ----------

      f : float
        Passed on as it is.
      """
      #  void QSSGRenderCamera::ClipPlanes::setClipFar(float f)
      self.uglySide.call(
          'ritual_ZN16QSSGRenderCamera10ClipPlanes10setClipFarEf', f,
      )

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
      'QSSGRenderCamera::ClipPlanes::ClipPlanes()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgrendercamera-clipplanes.html#ClipPlanes
      """
      #  QSSGRenderCamera::ClipPlanes::ClipPlanes()
      self._noteCreation(QSSGRenderCamera.ClipPlanes, lambda: Rituals.call(
          'ritual_ZN16QSSGRenderCamera10ClipPlanesC1Ev',
      ))

    @overload(float, float)
    def __init__(self, n: float, f: float) -> None:
      """
      Notes what was given, for Qt's
      'QSSGRenderCamera::ClipPlanes::ClipPlanes(float n, float f)', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgrendercamera-clipplanes.html#ClipPlanes

      Parameters
      ----------

      n : float
        Passed on as it is.

      f : float
        Passed on as it is.
      """
      #  QSSGRenderCamera::ClipPlanes::ClipPlanes(float n, float f)
      self._noteCreation(QSSGRenderCamera.ClipPlanes, lambda: Rituals.call(
          'ritual_ZN16QSSGRenderCamera10ClipPlanesC1Eff', n, f,
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

  class Frustum(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSSGRenderCamera::Frustum: a plain Python object
    standing in front of one C++ QSSGRenderCamera::Frustum.

    C++ hands a QSSGRenderCamera::Frustum around as a copy, so every C++
    QSSGRenderCamera::Frustum behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QSSGRenderCamera::Frustum yet. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGRenderCamera::Frustum::~Frustum()': the destructor: Python
      removes its C++ QSSGRenderCamera::Frustum by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QSSGRenderCamera::Frustum is created at the first use, not by
      'QSSGRenderCamera::Frustum(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGRenderCamera::Frustum back gives a copy the
      ritual made for Python, in a new cute QSSGRenderCamera::Frustum.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGRenderCamera::Frustum'

    #  Qt's '~QSSGRenderCamera::Frustum()'. Naming it makes this a value
    #  class: Python owns every C++ QSSGRenderCamera::Frustum behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QSSGRenderCamera7FrustumD1Ev'

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

  class Magnification(QVector2D):
    """
    The cute side of Qt's QSSGRenderCamera::Magnification: a plain Python
    object standing in front of one C++ QSSGRenderCamera::Magnification.

    It is built on the cute 'QVector2D', as Qt's
    QSSGRenderCamera::Magnification is built on Qt's QVector2D, and has
    everything that class has.

    C++ hands a QSSGRenderCamera::Magnification around as a copy, so every
    C++ QSSGRenderCamera::Magnification behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QSSGRenderCamera::Magnification that has a ritual
    and that Python can call so far, 4 names in all: 'horizontal',
    'vertical', 'setHorizontal', 'setVertical'. It can be made from Python,
    in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSSGRenderCamera::Magnification::~Magnification()': the
      destructor: Python removes its C++ QSSGRenderCamera::Magnification by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QSSGRenderCamera::Magnification is created at the first use,
      not by 'QSSGRenderCamera::Magnification(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSSGRenderCamera::Magnification back gives a copy
      the ritual made for Python, in a new cute
      QSSGRenderCamera::Magnification.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSSGRenderCamera::Magnification'

    #  Qt's '~QSSGRenderCamera::Magnification()'. Naming it makes this a
    #  value class: Python owns every C++ QSSGRenderCamera::Magnification
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QSSGRenderCamera13MagnificationD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def horizontal(self) -> float:
      """
      Calls Qt's 'float QSSGRenderCamera::Magnification::horizontal() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgrendercamera-magnification.html#horizontal
      """
      #  float QSSGRenderCamera::Magnification::horizontal() const
      return self.uglySide.call(
          'ritual_ZNK16QSSGRenderCamera13Magnification10horizontalEv',
      )

    def vertical(self) -> float:
      """
      Calls Qt's 'float QSSGRenderCamera::Magnification::vertical() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgrendercamera-magnification.html#vertical
      """
      #  float QSSGRenderCamera::Magnification::vertical() const
      return self.uglySide.call(
          'ritual_ZNK16QSSGRenderCamera13Magnification8verticalEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(float)
    def setHorizontal(self, h: float) -> None:
      """
      Calls Qt's 'void QSSGRenderCamera::Magnification::setHorizontal(float
      h)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgrendercamera-magnification.html

      Parameters
      ----------

      h : float
        Passed on as it is.
      """
      #  void QSSGRenderCamera::Magnification::setHorizontal(float h)
      self.uglySide.call(
          'ritual_ZN16QSSGRenderCamera13Magnification13setHorizontalEf', h,
      )

    @overload(float)
    def setVertical(self, v: float) -> None:
      """
      Calls Qt's 'void QSSGRenderCamera::Magnification::setVertical(float
      v)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgrendercamera-magnification.html#setVertical

      Parameters
      ----------

      v : float
        Passed on as it is.
      """
      #  void QSSGRenderCamera::Magnification::setVertical(float v)
      self.uglySide.call(
          'ritual_ZN16QSSGRenderCamera13Magnification11setVerticalEf', v,
      )

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
      'QSSGRenderCamera::Magnification::Magnification()', which is called at
      the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgrendercamera-magnification.html
      """
      #  QSSGRenderCamera::Magnification::Magnification()
      self._noteCreation(
          QSSGRenderCamera.Magnification, lambda: Rituals.call(
              'ritual_ZN16QSSGRenderCamera13MagnificationC1Ev',
          ))

    @overload(float, float)
    def __init__(self, h: float, v: float) -> None:
      """
      Notes what was given, for Qt's
      'QSSGRenderCamera::Magnification::Magnification(float h, float v)',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qssgrendercamera-magnification.html

      Parameters
      ----------

      h : float
        Passed on as it is.

      v : float
        Passed on as it is.
      """
      #  QSSGRenderCamera::Magnification::Magnification(float h, float v)
      self._noteCreation(
          QSSGRenderCamera.Magnification, lambda: Rituals.call(
              'ritual_ZN16QSSGRenderCamera13MagnificationC1Eff', h, v,
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderCamera'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMatrix4x4, QVector2D, QRectF)
  def unproject(
      self,
      globalTransform: QMatrix4x4,
      inLayerRelativeMouseCoords: QVector2D,
      inViewport: QRectF,
  ) -> QSSGRenderRay:
    """
    Calls Qt's 'QSSGRenderRay QSSGRenderCamera::unproject(const QMatrix4x4
    &globalTransform, const QVector2D &inLayerRelativeMouseCoords, const
    QRectF &inViewport) const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendercamera.html#unproject

    Parameters
    ----------

    globalTransform : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    inLayerRelativeMouseCoords : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.

    inViewport : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QSSGRenderRay
      A new cute QSSGRenderRay around the copy Qt gave back. Python owns it.
    """
    #  QSSGRenderRay QSSGRenderCamera::unproject(const QMatrix4x4
    #      &globalTransform, const QVector2D &inLayerRelativeMouseCoords,
    #      const QRectF &inViewport) const
    address = self.uglySide.call(
        'ritual_ZNK16QSSGRenderCamera9unprojectERK10QMatrix4x4RK9QVector2DR'
        'K6QRectF',
        self._valueOf(globalTransform),
        self._valueOf(inLayerRelativeMouseCoords), self._valueOf(inViewport),
    )
    from . import QSSGRenderRay
    return QSSGRenderRay._cuteOwning(address)

  @overload(DirtyFlag)
  def isDirty(self, dirtyFlag: DirtyFlag) -> bool:
    """
    Calls Qt's 'bool QSSGRenderCamera::isDirty(DirtyFlag dirtyFlag) const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendercamera.html#isDirty

    Parameters
    ----------

    dirtyFlag : DirtyFlag
      Passed on as its number.
    """
    #  bool QSSGRenderCamera::isDirty(DirtyFlag dirtyFlag) const
    return self.uglySide.call(
        'ritual_ZNK16QSSGRenderCamera7isDirtyENS_9DirtyFlagE',
        dirtyFlag.value,
    )

  def getLevelOfDetailMultiplier(self) -> float:
    """
    Calls Qt's 'float QSSGRenderCamera::getLevelOfDetailMultiplier() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendercamera.html#getLevelOfDetailMultiplier
    """
    #  float QSSGRenderCamera::getLevelOfDetailMultiplier() const
    return self.uglySide.call(
        'ritual_ZNK16QSSGRenderCamera26getLevelOfDetailMultiplierEv',
    )

  def getDpr(self) -> float:
    """
    Calls Qt's 'float QSSGRenderCamera::getDpr() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendercamera.html#getDpr
    """
    #  float QSSGRenderCamera::getDpr() const
    return self.uglySide.call('ritual_ZNK16QSSGRenderCamera6getDprEv')

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

  @overload(QSSGRenderGraphObject.Type)
  def __init__(self, type: QSSGRenderGraphObject.Type) -> None:
    """
    Notes what was given, for Qt's
    'QSSGRenderCamera::QSSGRenderCamera(QSSGRenderGraphObject::Type type)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendercamera.html#QSSGRenderCamera

    Parameters
    ----------

    type : QSSGRenderGraphObject.Type
      Passed on as its number.
    """
    #  QSSGRenderCamera::QSSGRenderCamera(QSSGRenderGraphObject::Type type)
    self._noteCreation(QSSGRenderCamera, lambda: Rituals.call(
        'ritual_ZN16QSSGRenderCameraC1EN21QSSGRenderGraphObject4TypeE',
        type.value,
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

  @overload(QVector3D, QVector3D, QVector3D, QVector3D)
  def lookAt(
      self,
      inCameraPos: QVector3D,
      inUpDir: QVector3D,
      inTargetPos: QVector3D,
      pivot: QVector3D,
  ) -> None:
    """
    Calls Qt's 'void QSSGRenderCamera::lookAt(const QVector3D &inCameraPos,
    const QVector3D &inUpDir, const QVector3D &inTargetPos, const QVector3D
    &pivot)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendercamera.html#lookAt

    Parameters
    ----------

    inCameraPos : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    inUpDir : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    inTargetPos : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    pivot : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QSSGRenderCamera::lookAt(const QVector3D &inCameraPos, const
    #      QVector3D &inUpDir, const QVector3D &inTargetPos, const QVector3D
    #      &pivot)
    self.uglySide.call(
        'ritual_ZN16QSSGRenderCamera6lookAtERK9QVector3DS2_S2_S2_',
        self._valueOf(inCameraPos), self._valueOf(inUpDir),
        self._valueOf(inTargetPos), self._valueOf(pivot),
    )

  @overload(QRectF, QSSGRenderCameraConfiguration)
  def calculateProjection(
      self,
      inViewport: QRectF,
      config: QSSGRenderCameraConfiguration,
  ) -> bool:
    """
    Calls Qt's 'bool QSSGRenderCamera::calculateProjection(const QRectF
    &inViewport, Configuration config)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendercamera.html#calculateProjection

    Parameters
    ----------

    inViewport : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    config : QSSGRenderCameraConfiguration
      Passed on as a value: Qt reads the C++ QSSGRenderCameraConfiguration,
      which stays Python's own.
    """
    #  bool QSSGRenderCamera::calculateProjection(const QRectF &inViewport,
    #      Configuration config)
    return self.uglySide.call(
        'ritual_ZN16QSSGRenderCamera19calculateProjectionERK6QRectF29QSSGRe'
        'nderCameraConfiguration',
        self._valueOf(inViewport), self._valueOf(config),
    )

  @overload(DirtyFlag)
  def markDirty(self, dirtyFlag: DirtyFlag) -> None:
    """
    Calls Qt's 'void QSSGRenderCamera::markDirty(DirtyFlag dirtyFlag)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendercamera.html#markDirty

    Parameters
    ----------

    dirtyFlag : DirtyFlag
      Passed on as its number.
    """
    #  void QSSGRenderCamera::markDirty(DirtyFlag dirtyFlag)
    self.uglySide.call(
        'ritual_ZN16QSSGRenderCamera9markDirtyENS_9DirtyFlagE',
        dirtyFlag.value,
    )

  @overload(DirtyFlag)
  def clearDirty(self, dirtyFlag: DirtyFlag) -> None:
    """
    Calls Qt's 'void QSSGRenderCamera::clearDirty(DirtyFlag dirtyFlag)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendercamera.html#clearDirty

    Parameters
    ----------

    dirtyFlag : DirtyFlag
      Passed on as its number.
    """
    #  void QSSGRenderCamera::clearDirty(DirtyFlag dirtyFlag)
    self.uglySide.call(
        'ritual_ZN16QSSGRenderCamera10clearDirtyENS_9DirtyFlagE',
        dirtyFlag.value,
    )

  @staticmethod
  def calculateProjectionInternal(*__, **_) -> Never:
    """
    Qt's 'bool QSSGRenderCamera::calculateProjectionInternal(QSSGRenderCamera
    &camera, const QRectF &inViewport, Configuration config)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderCamera.calculateProjectionInternal' has no cute "
        "function yet. Qt's 'bool "
        "QSSGRenderCamera::calculateProjectionInternal(QSSGRenderCamera "
        "&camera, const QRectF &inViewport, Configuration config)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def calculateViewProjectionMatrix(*__, **_) -> Never:
    """
    - Qt's 'void QSSGRenderCamera::calculateViewProjectionMatrix(const
      QMatrix4x4 &globalTransform, const QMatrix4x4 &projection, QMatrix4x4
      &outMatrix)': takes a type Python has no way to hand over yet.
    - Qt's 'void QSSGRenderCamera::calculateViewProjectionMatrix(const
      QMatrix4x4 &globalTransform, QMatrix4x4 &outMatrix) const': takes a
      type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderCamera.calculateViewProjectionMatrix' has no cute "
        "function yet. Qt's 'void "
        "QSSGRenderCamera::calculateViewProjectionMatrix(const QMatrix4x4 "
        "&globalTransform, const QMatrix4x4 &projection, QMatrix4x4 "
        "&outMatrix)': takes a type Python has no way to hand over yet. "
        "Qt's 'void QSSGRenderCamera::calculateViewProjectionMatrix(const "
        "QMatrix4x4 &globalTransform, QMatrix4x4 &outMatrix) const': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def calculateViewProjectionWithoutTranslation(*__, **_) -> Never:
    """
    Qt's 'void
    QSSGRenderCamera::calculateViewProjectionWithoutTranslation(const
    QMatrix4x4 &globalTransform, float near, float far, QMatrix4x4
    &outMatrix) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderCamera.calculateViewProjectionWithoutTranslation' has "
        "no cute function yet. Qt's 'void "
        "QSSGRenderCamera::calculateViewProjectionWithoutTranslation(const "
        "QMatrix4x4 &globalTransform, float near, float far, QMatrix4x4 "
        "&outMatrix) const': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def computeCustomFrustum(*__, **_) -> Never:
    """
    Qt's 'bool
    QSSGRenderCamera::computeCustomFrustum(QSSGRenderCamera::Frustum frustum,
    QSSGRenderCamera::ClipPlanes clipPlanes, QMatrix4x4 &outProjection)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderCamera.computeCustomFrustum' has no cute function yet. "
        "Qt's 'bool "
        "QSSGRenderCamera::computeCustomFrustum(QSSGRenderCamera::Frustum "
        "frustum, QSSGRenderCamera::ClipPlanes clipPlanes, QMatrix4x4 "
        "&outProjection)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def computeFrustumOrtho(*__, **_) -> Never:
    """
    Qt's 'bool QSSGRenderCamera::computeFrustumOrtho(QRectF inViewport,
    QSSGRenderCamera::ClipPlanes clipPlanes, QSSGRenderCamera::Magnification
    magnification, Configuration config, QMatrix4x4 &outProjection)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderCamera.computeFrustumOrtho' has no cute function yet. "
        "Qt's 'bool QSSGRenderCamera::computeFrustumOrtho(QRectF "
        "inViewport, QSSGRenderCamera::ClipPlanes clipPlanes, "
        "QSSGRenderCamera::Magnification magnification, Configuration "
        "config, QMatrix4x4 &outProjection)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def computeFrustumPerspective(*__, **_) -> Never:
    """
    Qt's 'bool QSSGRenderCamera::computeFrustumPerspective(QRectF inViewport,
    FieldOfView fov, QSSGRenderCamera::ClipPlanes clipPlanes, QMatrix4x4
    &outProjection)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSSGRenderCamera.computeFrustumPerspective' has no cute function "
        "yet. Qt's 'bool QSSGRenderCamera::computeFrustumPerspective(QRectF "
        "inViewport, FieldOfView fov, QSSGRenderCamera::ClipPlanes "
        "clipPlanes, QMatrix4x4 &outProjection)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def setCustomProjection(*__, **_) -> Never:
    """
    Qt's 'void QSSGRenderCamera::setCustomProjection(const QMatrix4x4
    &proj)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QSSGRenderCamera.setCustomProjection' has no cute function yet. "
        "Qt's 'void QSSGRenderCamera::setCustomProjection(const QMatrix4x4 "
        "&proj)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
