"""
QSGMaterialShader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qsgmaterialshader.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QRect
  from ..QtGui import QMatrix4x4, QRhi, QRhiResourceUpdateBatch, QShader
  from . import QSGMaterialShaderPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QShader = WAIT['QShader']


class QSGMaterialShader(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSGMaterialShader: a plain Python object standing in
  front of one C++ QSGMaterialShader.

  What exists
  -----------

  Every function of Qt's QSGMaterialShader that has a ritual and that Python
  can call so far, 7 names in all: 'flags', 'setFlag', 'setFlags',
  'combinedImageSamplerCount', 'd_func', 'setShaderFileName', 'setShader'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGMaterialShader::~QSGMaterialShader()': the destructor: Python
    never removes a C++ QSGMaterialShader.
  - Qt's 'bool QSGMaterialShader::updateUniformData(RenderState &state,
    QSGMaterial *newMaterial, QSGMaterial *oldMaterial)': takes a type Python
    has no way to hand over yet.
  - Qt's 'void QSGMaterialShader::updateSampledImage(RenderState &state, int
    binding, QSGTexture **texture, QSGMaterial *newMaterial, QSGMaterial
    *oldMaterial)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QSGMaterialShader::updateGraphicsPipelineState(RenderState
    &state, GraphicsPipelineState *ps, QSGMaterial *newMaterial, QSGMaterial
    *oldMaterial)': takes a type Python has no way to hand over yet.
  - Qt's 'const QSGMaterialShaderPrivate *QSGMaterialShader::d_func() const':
    takes in Python what 'QSGMaterialShaderPrivate
    *QSGMaterialShader::d_func()' takes.
  - Qt's 'QSGMaterialShader::QSGMaterialShader(QSGMaterialShaderPrivate
    &dd)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QSGMaterialShader is created at the first use, not by
    'QSGMaterialShader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGMaterialShader.
  - Each name of Qt's QSGMaterialShader that has no cute function yet,
    'updateGraphicsPipelineState', 'updateSampledImage', 'updateUniformData',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QSGMaterialShader, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Flag(CuteFlags):
    """
    The flags enum 'QSGMaterialShader::Flag' of Qt, with the 1 names Qt gives
    in it. Qt names the type of its combinations 'QSGMaterialShader::Flags'.
    """

    UpdatesGraphicsPipelineState = 0x1

  Flags = Flag

  class Stage(CuteNum):
    """
    The enum 'QSGMaterialShader::Stage' of Qt, with the 2 names Qt gives in
    it.
    """

    VertexStage = Kee[int](0)
    FragmentStage = Kee[int](1)

  #  The classes Qt writes inside QSGMaterialShader, each a class in here as
  #  in C++.

  class GraphicsPipelineState(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSGMaterialShader::GraphicsPipelineState: a plain
    Python object standing in front of one C++
    QSGMaterialShader::GraphicsPipelineState.

    C++ hands a QSGMaterialShader::GraphicsPipelineState around as a copy, so
    every C++ QSGMaterialShader::GraphicsPipelineState behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QSGMaterialShader::GraphicsPipelineState yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QSGMaterialShader::GraphicsPipelineState::~GraphicsPipelineState()':
      the destructor: Python removes its C++
      QSGMaterialShader::GraphicsPipelineState by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QSGMaterialShader::GraphicsPipelineState is created at the
      first use, not by 'QSGMaterialShader::GraphicsPipelineState(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSGMaterialShader::GraphicsPipelineState back gives
      a copy the ritual made for Python, in a new cute
      QSGMaterialShader::GraphicsPipelineState.
    """

    #  The enums Qt writes inside QSGMaterialShader::GraphicsPipelineState,
    #  each a class in here as in C++, and the names Qt has for the
    #  combinations of its flags enums.

    class BlendFactor(CuteNum):
      """
      The enum 'QSGMaterialShader::GraphicsPipelineState::BlendFactor' of Qt,
      with the 19 names Qt gives in it.
      """

      Zero = Kee[int](0)
      One = Kee[int](1)
      SrcColor = Kee[int](2)
      OneMinusSrcColor = Kee[int](3)
      DstColor = Kee[int](4)
      OneMinusDstColor = Kee[int](5)
      SrcAlpha = Kee[int](6)
      OneMinusSrcAlpha = Kee[int](7)
      DstAlpha = Kee[int](8)
      OneMinusDstAlpha = Kee[int](9)
      ConstantColor = Kee[int](10)
      OneMinusConstantColor = Kee[int](11)
      ConstantAlpha = Kee[int](12)
      OneMinusConstantAlpha = Kee[int](13)
      SrcAlphaSaturate = Kee[int](14)
      Src1Color = Kee[int](15)
      OneMinusSrc1Color = Kee[int](16)
      Src1Alpha = Kee[int](17)
      OneMinusSrc1Alpha = Kee[int](18)

    class BlendOp(CuteNum, scoped=True):
      """
      The enum 'QSGMaterialShader::GraphicsPipelineState::BlendOp' of Qt,
      with the 5 names Qt gives in it. C++ keeps these names inside the enum,
      so the class that holds the enum does not have them.
      """

      Add = Kee[int](0)
      Subtract = Kee[int](1)
      ReverseSubtract = Kee[int](2)
      Min = Kee[int](3)
      Max = Kee[int](4)

    class ColorMaskComponent(CuteFlags):
      """
      The flags enum
      'QSGMaterialShader::GraphicsPipelineState::ColorMaskComponent' of Qt,
      with the 4 names Qt gives in it. Qt names the type of its combinations
      'QSGMaterialShader::GraphicsPipelineState::ColorMask'.
      """

      R = 0x1
      G = 0x2
      B = 0x4
      A = 0x8

    ColorMask = ColorMaskComponent

    class CullMode(CuteNum):
      """
      The enum 'QSGMaterialShader::GraphicsPipelineState::CullMode' of Qt,
      with the 3 names Qt gives in it.
      """

      CullNone = Kee[int](0)
      CullFront = Kee[int](1)
      CullBack = Kee[int](2)

    class PolygonMode(CuteNum):
      """
      The enum 'QSGMaterialShader::GraphicsPipelineState::PolygonMode' of Qt,
      with the 2 names Qt gives in it.
      """

      Fill = Kee[int](0)
      Line = Kee[int](1)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSGMaterialShader::GraphicsPipelineState'

    #  Qt's '~QSGMaterialShader::GraphicsPipelineState()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QSGMaterialShader::GraphicsPipelineState behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN17QSGMaterialShader21GraphicsPipelineStateD1Ev')

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

  class RenderState(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QSGMaterialShader::RenderState: a plain Python
    object standing in front of one C++ QSGMaterialShader::RenderState.

    C++ hands a QSGMaterialShader::RenderState around as a copy, so every C++
    QSGMaterialShader::RenderState behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QSGMaterialShader::RenderState that has a ritual
    and that Python can call so far, 15 names in all: 'dirtyStates',
    'isMatrixDirty', 'isOpacityDirty', 'opacity', 'combinedMatrix',
    'modelViewMatrix', 'projectionMatrix', 'projectionMatrixCount',
    'viewportRect', 'deviceRect', 'determinant', 'devicePixelRatio',
    'uniformData', 'resourceUpdateBatch', 'rhi'. None can be made from
    Python: one comes out of a function of another class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QSGMaterialShader::RenderState::~RenderState()': the destructor:
      Python removes its C++ QSGMaterialShader::RenderState by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QSGMaterialShader::RenderState is created at the first use, not
      by 'QSGMaterialShader::RenderState(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QSGMaterialShader::RenderState back gives a copy
      the ritual made for Python, in a new cute
      QSGMaterialShader::RenderState.
    """

    #  The enums Qt writes inside QSGMaterialShader::RenderState, each a
    #  class in here as in C++, and the names Qt has for the combinations of
    #  its flags enums.

    class DirtyState(CuteFlags):
      """
      The flags enum 'QSGMaterialShader::RenderState::DirtyState' of Qt, with
      the 4 names Qt gives in it. Qt names the type of its combinations
      'QSGMaterialShader::RenderState::DirtyStates'.
      """

      DirtyMatrix = 0x1
      DirtyOpacity = 0x2
      DirtyCachedMaterialData = 0x4
      DirtyAll = 0xffff

    DirtyStates = DirtyState

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QSGMaterialShader::RenderState'

    #  Qt's '~QSGMaterialShader::RenderState()'. Naming it makes this a value
    #  class: Python owns every C++ QSGMaterialShader::RenderState behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN17QSGMaterialShader11RenderStateD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def dirtyStates(self) -> DirtyStates:
      """
      Calls Qt's 'DirtyStates QSGMaterialShader::RenderState::dirtyStates()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgmaterialshader-renderstate.html#dirtyStates

      Returns
      -------

      DirtyStates
        The value standing for the combination Qt gave back.
      """
      #  DirtyStates QSGMaterialShader::RenderState::dirtyStates() const
      return QSGMaterialShader.RenderState.DirtyStates(self.uglySide.call(
          'ritual_ZNK17QSGMaterialShader11RenderState11dirtyStatesEv',
      ))

    def isMatrixDirty(self) -> bool:
      """
      Calls Qt's 'bool QSGMaterialShader::RenderState::isMatrixDirty()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgmaterialshader-renderstate.html#isMatrixDirty
      """
      #  bool QSGMaterialShader::RenderState::isMatrixDirty() const
      return self.uglySide.call(
          'ritual_ZNK17QSGMaterialShader11RenderState13isMatrixDirtyEv',
      )

    def isOpacityDirty(self) -> bool:
      """
      Calls Qt's 'bool QSGMaterialShader::RenderState::isOpacityDirty()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgmaterialshader-renderstate.html
      """
      #  bool QSGMaterialShader::RenderState::isOpacityDirty() const
      return self.uglySide.call(
          'ritual_ZNK17QSGMaterialShader11RenderState14isOpacityDirtyEv',
      )

    def opacity(self) -> float:
      """
      Calls Qt's 'float QSGMaterialShader::RenderState::opacity() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgmaterialshader-renderstate.html#opacity
      """
      #  float QSGMaterialShader::RenderState::opacity() const
      return self.uglySide.call(
          'ritual_ZNK17QSGMaterialShader11RenderState7opacityEv',
      )

    @overload()
    def combinedMatrix(self) -> QMatrix4x4:
      """
      Calls Qt's 'QMatrix4x4 QSGMaterialShader::RenderState::combinedMatrix()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgmaterialshader-renderstate.html

      Returns
      -------

      QMatrix4x4
        A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
      """
      #  QMatrix4x4 QSGMaterialShader::RenderState::combinedMatrix() const
      address = self.uglySide.call(
          'ritual_ZNK17QSGMaterialShader11RenderState14combinedMatrixEv',
      )
      from ..QtGui import QMatrix4x4
      return QMatrix4x4._cuteOwning(address)

    @overload(int)
    def combinedMatrix(self, index: int) -> QMatrix4x4:
      """
      Calls Qt's 'QMatrix4x4
      QSGMaterialShader::RenderState::combinedMatrix(qsizetype index) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgmaterialshader-renderstate.html

      Parameters
      ----------

      index : int
        Passed on as it is.

      Returns
      -------

      QMatrix4x4
        A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
      """
      #  QMatrix4x4 QSGMaterialShader::RenderState::combinedMatrix(qsizetype
      #      index) const
      address = self.uglySide.call(
          'ritual_ZNK17QSGMaterialShader11RenderState14combinedMatrixEx',
          index,
      )
      from ..QtGui import QMatrix4x4
      return QMatrix4x4._cuteOwning(address)

    def modelViewMatrix(self) -> QMatrix4x4:
      """
      Calls Qt's 'QMatrix4x4
      QSGMaterialShader::RenderState::modelViewMatrix() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgmaterialshader-renderstate.html

      Returns
      -------

      QMatrix4x4
        A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
      """
      #  QMatrix4x4 QSGMaterialShader::RenderState::modelViewMatrix() const
      address = self.uglySide.call(
          'ritual_ZNK17QSGMaterialShader11RenderState15modelViewMatrixEv',
      )
      from ..QtGui import QMatrix4x4
      return QMatrix4x4._cuteOwning(address)

    @overload()
    def projectionMatrix(self) -> QMatrix4x4:
      """
      Calls Qt's 'QMatrix4x4
      QSGMaterialShader::RenderState::projectionMatrix() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgmaterialshader-renderstate.html

      Returns
      -------

      QMatrix4x4
        A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
      """
      #  QMatrix4x4 QSGMaterialShader::RenderState::projectionMatrix() const
      address = self.uglySide.call(
          'ritual_ZNK17QSGMaterialShader11RenderState16projectionMatrixEv',
      )
      from ..QtGui import QMatrix4x4
      return QMatrix4x4._cuteOwning(address)

    @overload(int)
    def projectionMatrix(self, index: int) -> QMatrix4x4:
      """
      Calls Qt's 'QMatrix4x4
      QSGMaterialShader::RenderState::projectionMatrix(qsizetype index)
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgmaterialshader-renderstate.html

      Parameters
      ----------

      index : int
        Passed on as it is.

      Returns
      -------

      QMatrix4x4
        A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
      """
      #  QMatrix4x4
      #      QSGMaterialShader::RenderState::projectionMatrix(qsizetype
      #      index) const
      address = self.uglySide.call(
          'ritual_ZNK17QSGMaterialShader11RenderState16projectionMatrixEx',
          index,
      )
      from ..QtGui import QMatrix4x4
      return QMatrix4x4._cuteOwning(address)

    def projectionMatrixCount(self) -> int:
      """
      Calls Qt's 'qsizetype
      QSGMaterialShader::RenderState::projectionMatrixCount() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgmaterialshader-renderstate.html
      """
      #  qsizetype QSGMaterialShader::RenderState::projectionMatrixCount()
      #      const
      return self.uglySide.call(
          'ritual_ZNK17QSGMaterialShader11RenderState21projectionMatrixCoun'
          'tEv',
      )

    def viewportRect(self) -> QRect:
      """
      Calls Qt's 'QRect QSGMaterialShader::RenderState::viewportRect()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgmaterialshader-renderstate.html#viewportRect

      Returns
      -------

      QRect
        A new cute QRect around the copy Qt gave back. Python owns it.
      """
      #  QRect QSGMaterialShader::RenderState::viewportRect() const
      address = self.uglySide.call(
          'ritual_ZNK17QSGMaterialShader11RenderState12viewportRectEv',
      )
      from ..QtCore import QRect
      return QRect._cuteOwning(address)

    def deviceRect(self) -> QRect:
      """
      Calls Qt's 'QRect QSGMaterialShader::RenderState::deviceRect() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgmaterialshader-renderstate.html#deviceRect

      Returns
      -------

      QRect
        A new cute QRect around the copy Qt gave back. Python owns it.
      """
      #  QRect QSGMaterialShader::RenderState::deviceRect() const
      address = self.uglySide.call(
          'ritual_ZNK17QSGMaterialShader11RenderState10deviceRectEv',
      )
      from ..QtCore import QRect
      return QRect._cuteOwning(address)

    def determinant(self) -> float:
      """
      Calls Qt's 'float QSGMaterialShader::RenderState::determinant() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgmaterialshader-renderstate.html#determinant
      """
      #  float QSGMaterialShader::RenderState::determinant() const
      return self.uglySide.call(
          'ritual_ZNK17QSGMaterialShader11RenderState11determinantEv',
      )

    def devicePixelRatio(self) -> float:
      """
      Calls Qt's 'float QSGMaterialShader::RenderState::devicePixelRatio()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgmaterialshader-renderstate.html
      """
      #  float QSGMaterialShader::RenderState::devicePixelRatio() const
      return self.uglySide.call(
          'ritual_ZNK17QSGMaterialShader11RenderState16devicePixelRatioEv',
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

    def uniformData(self) -> Optional[QByteArray]:
      """
      Calls Qt's 'QByteArray *QSGMaterialShader::RenderState::uniformData()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgmaterialshader-renderstate.html#uniformData

      Returns
      -------

      Optional[QByteArray]
        The cute object standing for what Qt gave back. None when Qt gave
        back no object.
      """
      #  QByteArray *QSGMaterialShader::RenderState::uniformData()
      address = self.uglySide.call(
          'ritual_ZN17QSGMaterialShader11RenderState11uniformDataEv',
      )
      from ..QtCore import QByteArray
      return QByteArray._cuteAt(address)

    def resourceUpdateBatch(self) -> Optional[QRhiResourceUpdateBatch]:
      """
      Calls Qt's 'QRhiResourceUpdateBatch
      *QSGMaterialShader::RenderState::resourceUpdateBatch()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgmaterialshader-renderstate.html

      Returns
      -------

      Optional[QRhiResourceUpdateBatch]
        The cute object standing for what Qt gave back. None when Qt gave
        back no object.
      """
      #  QRhiResourceUpdateBatch
      #      *QSGMaterialShader::RenderState::resourceUpdateBatch()
      address = self.uglySide.call(
          'ritual_ZN17QSGMaterialShader11RenderState19resourceUpdateBatchEv',
      )
      from ..QtGui import QRhiResourceUpdateBatch
      return QRhiResourceUpdateBatch._cuteAt(address)

    def rhi(self) -> Optional[QRhi]:
      """
      Calls Qt's 'QRhi *QSGMaterialShader::RenderState::rhi()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qsgmaterialshader-renderstate.html#rhi

      Returns
      -------

      Optional[QRhi]
        The cute object standing for what Qt gave back. None when Qt gave
        back no object.
      """
      #  QRhi *QSGMaterialShader::RenderState::rhi()
      address = self.uglySide.call(
          'ritual_ZN17QSGMaterialShader11RenderState3rhiEv',
      )
      from ..QtGui import QRhi
      return QRhi._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGMaterialShader'

  #  The functions Qt calls itself that QSGMaterialShader is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'updateUniformData': (
          'bool QSGMaterialShader::updateUniformData(RenderState &, '
          'QSGMaterial *, QSGMaterial *)',
      ),
      'updateSampledImage': (
          'void QSGMaterialShader::updateSampledImage(RenderState &, int, '
          'QSGTexture **, QSGMaterial *, QSGMaterial *)',
      ),
      'updateGraphicsPipelineState': (
          'bool QSGMaterialShader::updateGraphicsPipelineState(RenderState '
          '&, GraphicsPipelineState *, QSGMaterial *, QSGMaterial *)',
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def flags(self) -> Flags:
    """
    Calls Qt's 'Flags QSGMaterialShader::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgmaterialshader.html#flags

    Returns
    -------

    Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QSGMaterialShader::flags() const
    return QSGMaterialShader.Flags(self.uglySide.call(
        'ritual_ZNK17QSGMaterialShader5flagsEv',
    ))

  @overload(int)
  def combinedImageSamplerCount(self, binding: int) -> int:
    """
    Calls Qt's 'int QSGMaterialShader::combinedImageSamplerCount(int binding)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgmaterialshader.html#combinedImageSamplerCount

    Parameters
    ----------

    binding : int
      Passed on as it is.
    """
    #  int QSGMaterialShader::combinedImageSamplerCount(int binding) const
    return self.uglySide.call(
        'ritual_ZNK17QSGMaterialShader25combinedImageSamplerCountEi',
        binding,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Flags)
  @overload(Flags, bool)
  def setFlag(self, flags: Flags, on: bool = True) -> None:
    """
    Calls Qt's 'void QSGMaterialShader::setFlag(Flags flags, bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgmaterialshader.html#setFlag

    Parameters
    ----------

    flags : Flags
      Passed on as its number.

    on : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QSGMaterialShader::setFlag(Flags flags, bool on)
    self.uglySide.call(
        'ritual_ZN17QSGMaterialShader7setFlagE6QFlagsINS_4FlagEEb',
        flags.value, on,
    )

  @overload(Flags)
  def setFlags(self, flags: Flags) -> None:
    """
    Calls Qt's 'void QSGMaterialShader::setFlags(Flags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgmaterialshader.html#setFlags

    Parameters
    ----------

    flags : Flags
      Passed on as its number.
    """
    #  void QSGMaterialShader::setFlags(Flags flags)
    self.uglySide.call(
        'ritual_ZN17QSGMaterialShader8setFlagsE6QFlagsINS_4FlagEE',
        flags.value,
    )

  @overload(Stage, str)
  def setShaderFileName(self, stage: Stage, filename: str) -> None:
    """
    Calls Qt's 'void QSGMaterialShader::setShaderFileName(Stage stage, const
    QString &filename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgmaterialshader.html#setShaderFileName

    Parameters
    ----------

    stage : Stage
      Passed on as its number.

    filename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSGMaterialShader::setShaderFileName(Stage stage, const QString
    #      &filename)
    self.uglySide.call(
        'ritual_ZN17QSGMaterialShader17setShaderFileNameENS_5StageERK7QStri'
        'ng',
        stage.value, filename,
    )

  @overload(Stage, str, int)
  def setShaderFileName(
      self,
      stage: Stage,
      filename: str,
      viewCount: int,
  ) -> None:
    """
    Calls Qt's 'void QSGMaterialShader::setShaderFileName(Stage stage, const
    QString &filename, int viewCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgmaterialshader.html#setShaderFileName

    Parameters
    ----------

    stage : Stage
      Passed on as its number.

    filename : str
      Passed on as it is: a QString is made of it for the call.

    viewCount : int
      Passed on as it is.
    """
    #  void QSGMaterialShader::setShaderFileName(Stage stage, const QString
    #      &filename, int viewCount)
    self.uglySide.call(
        'ritual_ZN17QSGMaterialShader17setShaderFileNameENS_5StageERK7QStri'
        'ngi',
        stage.value, filename, viewCount,
    )

  @overload(Stage, QShader)
  def setShader(self, stage: Stage, shader: QShader) -> None:
    """
    Calls Qt's 'void QSGMaterialShader::setShader(Stage stage, const QShader
    &shader)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgmaterialshader.html#setShader

    Parameters
    ----------

    stage : Stage
      Passed on as its number.

    shader : QShader
      Passed on as a value: Qt reads the C++ QShader, which stays Python's
      own.
    """
    #  void QSGMaterialShader::setShader(Stage stage, const QShader &shader)
    self.uglySide.call(
        'ritual_ZN17QSGMaterialShader9setShaderENS_5StageERK7QShader',
        stage.value, self._valueOf(shader),
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
    Notes what was given, for Qt's 'QSGMaterialShader::QSGMaterialShader()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgmaterialshader.html#QSGMaterialShader
    """
    #  QSGMaterialShader::QSGMaterialShader()
    self._noteCreation(QSGMaterialShader, lambda: Rituals.call(
        'ritual_ZN17QSGMaterialShaderC1Ev',
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

  def d_func(self) -> Optional[QSGMaterialShaderPrivate]:
    """
    Calls Qt's 'QSGMaterialShaderPrivate *QSGMaterialShader::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgmaterialshader.html#d_func

    Returns
    -------

    Optional[QSGMaterialShaderPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterialShaderPrivate *QSGMaterialShader::d_func()
    address = self.uglySide.call('ritual_ZN17QSGMaterialShader6d_funcEv')
    from . import QSGMaterialShaderPrivate
    return QSGMaterialShaderPrivate._cuteAt(address)

  @staticmethod
  def updateGraphicsPipelineState(*__, **_) -> Never:
    """
    Qt's 'bool QSGMaterialShader::updateGraphicsPipelineState(RenderState
    &state, GraphicsPipelineState *ps, QSGMaterial *newMaterial, QSGMaterial
    *oldMaterial)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSGMaterialShader.updateGraphicsPipelineState' has no cute "
        "function yet. Qt's 'bool "
        "QSGMaterialShader::updateGraphicsPipelineState(RenderState &state, "
        "GraphicsPipelineState *ps, QSGMaterial *newMaterial, QSGMaterial "
        "*oldMaterial)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def updateSampledImage(*__, **_) -> Never:
    """
    Qt's 'void QSGMaterialShader::updateSampledImage(RenderState &state, int
    binding, QSGTexture **texture, QSGMaterial *newMaterial, QSGMaterial
    *oldMaterial)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSGMaterialShader.updateSampledImage' has no cute function yet. "
        "Qt's 'void QSGMaterialShader::updateSampledImage(RenderState "
        "&state, int binding, QSGTexture **texture, QSGMaterial "
        "*newMaterial, QSGMaterial *oldMaterial)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def updateUniformData(*__, **_) -> Never:
    """
    Qt's 'bool QSGMaterialShader::updateUniformData(RenderState &state,
    QSGMaterial *newMaterial, QSGMaterial *oldMaterial)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSGMaterialShader.updateUniformData' has no cute function yet. "
        "Qt's 'bool QSGMaterialShader::updateUniformData(RenderState "
        "&state, QSGMaterial *newMaterial, QSGMaterial *oldMaterial)': "
        "takes a type Python has no way to hand over yet.")
