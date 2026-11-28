"""
QOpenGLEngineSharedShaders binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/6.12.0/QtOpenGL/private/qopenglengineshadermanager_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QOpenGLEngineSharedShaders to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray
  from ..QtGui import QOpenGLContext
  from . import QOpenGLCustomShaderStage, QOpenGLEngineShaderProg
  from . import QOpenGLShaderProgram
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpenGLContext = WAIT['QOpenGLContext']
  QOpenGLCustomShaderStage = WAIT['QOpenGLCustomShaderStage']
  QOpenGLEngineShaderProg = WAIT['QOpenGLEngineShaderProg']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLEngineSharedShaders(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLEngineSharedShaders: a plain Python object
  standing in front of one C++ QOpenGLEngineSharedShaders.

  What exists
  -----------

  Every function of Qt's QOpenGLEngineSharedShaders that has a ritual and
  that Python can call so far, 6 names in all: 'snippetNameStr',
  'simpleProgram', 'blitProgram', 'findProgramInCache', 'shadersForContext',
  'cleanupCustomStage'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLEngineSharedShaders::~QOpenGLEngineSharedShaders()': the
    destructor: Python never removes a C++ QOpenGLEngineSharedShaders.

  What has no ritual
  ------------------

  7 of the 15 functions Qt declares: 4 forbidden; 3 not a gap.

  What to expect
  --------------

  - The C++ QOpenGLEngineSharedShaders is created at the first use, not by
    'QOpenGLEngineSharedShaders(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLEngineSharedShaders.
  """

  #  The enums Qt writes inside QOpenGLEngineSharedShaders, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class SnippetName(CuteNum):
    """
    The enum 'QOpenGLEngineSharedShaders::SnippetName' of Qt, with the 54
    names Qt gives in it.
    """

    MainVertexShader = Kee[int](0)
    MainWithTexCoordsVertexShader = Kee[int](1)
    MainWithTexCoordsAndOpacityVertexShader = Kee[int](2)
    UntransformedPositionVertexShader = Kee[int](3)
    PositionOnlyVertexShader = Kee[int](4)
    ComplexGeometryPositionOnlyVertexShader = Kee[int](5)
    PositionWithPatternBrushVertexShader = Kee[int](6)
    PositionWithLinearGradientBrushVertexShader = Kee[int](7)
    PositionWithConicalGradientBrushVertexShader = Kee[int](8)
    PositionWithRadialGradientBrushVertexShader = Kee[int](9)
    PositionWithTextureBrushVertexShader = Kee[int](10)
    AffinePositionWithPatternBrushVertexShader = Kee[int](11)
    AffinePositionWithLinearGradientBrushVertexShader = Kee[int](12)
    AffinePositionWithConicalGradientBrushVertexShader = Kee[int](13)
    AffinePositionWithRadialGradientBrushVertexShader = Kee[int](14)
    AffinePositionWithTextureBrushVertexShader = Kee[int](15)
    MainFragmentShader_MO = Kee[int](16)
    MainFragmentShader_M = Kee[int](17)
    MainFragmentShader_O = Kee[int](18)
    MainFragmentShader = Kee[int](19)
    MainFragmentShader_ImageArrays = Kee[int](20)
    ImageSrcFragmentShader = Kee[int](21)
    ImageSrcWithPatternFragmentShader = Kee[int](22)
    NonPremultipliedImageSrcFragmentShader = Kee[int](23)
    GrayscaleImageSrcFragmentShader = Kee[int](24)
    AlphaImageSrcFragmentShader = Kee[int](25)
    CustomImageSrcFragmentShader = Kee[int](26)
    SolidBrushSrcFragmentShader = Kee[int](27)
    TextureBrushSrcFragmentShader = Kee[int](28)
    TextureBrushSrcWithPatternFragmentShader = Kee[int](29)
    PatternBrushSrcFragmentShader = Kee[int](30)
    LinearGradientBrushSrcFragmentShader = Kee[int](31)
    RadialGradientBrushSrcFragmentShader = Kee[int](32)
    ConicalGradientBrushSrcFragmentShader = Kee[int](33)
    ShockingPinkSrcFragmentShader = Kee[int](34)
    NoMaskFragmentShader = Kee[int](35)
    MaskFragmentShader = Kee[int](36)
    RgbMaskFragmentShaderPass1 = Kee[int](37)
    RgbMaskFragmentShaderPass2 = Kee[int](38)
    RgbMaskWithGammaFragmentShader = Kee[int](39)
    NoCompositionModeFragmentShader = Kee[int](40)
    MultiplyCompositionModeFragmentShader = Kee[int](41)
    ScreenCompositionModeFragmentShader = Kee[int](42)
    OverlayCompositionModeFragmentShader = Kee[int](43)
    DarkenCompositionModeFragmentShader = Kee[int](44)
    LightenCompositionModeFragmentShader = Kee[int](45)
    ColorDodgeCompositionModeFragmentShader = Kee[int](46)
    ColorBurnCompositionModeFragmentShader = Kee[int](47)
    HardLightCompositionModeFragmentShader = Kee[int](48)
    SoftLightCompositionModeFragmentShader = Kee[int](49)
    DifferenceCompositionModeFragmentShader = Kee[int](50)
    ExclusionCompositionModeFragmentShader = Kee[int](51)
    TotalSnippetCount = Kee[int](52)
    InvalidSnippetName = Kee[int](53)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(SnippetName)
  def snippetNameStr(snippetName: SnippetName) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    QOpenGLEngineSharedShaders::snippetNameStr(SnippetName snippetName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglenginesharedshaders.html#snippetNameStr

    Parameters
    ----------

    snippetName : SnippetName
      Passed on as its number.

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QOpenGLEngineSharedShaders::snippetNameStr(SnippetName
    #      snippetName)
    address = Rituals.call(
        'ritual_ZN26QOpenGLEngineSharedShaders14snippetNameStrENS_11Snippet'
        'NameE',
        snippetName.value,
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  @overload(QOpenGLContext)
  @overload(NoneType)
  def shadersForContext(
      context: Optional[QOpenGLContext],
  ) -> Optional[QOpenGLEngineSharedShaders]:
    """
    Calls Qt's 'QOpenGLEngineSharedShaders
    *QOpenGLEngineSharedShaders::shadersForContext(QOpenGLContext *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglenginesharedshaders.html#shadersForContext

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QOpenGLEngineSharedShaders]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLEngineSharedShaders
    #      *QOpenGLEngineSharedShaders::shadersForContext(QOpenGLContext
    #      *context)
    address = Rituals.call(
        'ritual_ZN26QOpenGLEngineSharedShaders17shadersForContextEP14QOpenG'
        'LContext',
        CuteMixin._addressOf(context),
    )
    return QOpenGLEngineSharedShaders._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLEngineSharedShaders'

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

  @overload(QOpenGLContext)
  @overload(NoneType)
  def __init__(self, context: Optional[QOpenGLContext]) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLEngineSharedShaders::QOpenGLEngineSharedShaders(QOpenGLContext
    *context)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglenginesharedshaders.html

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOpenGLEngineSharedShaders::QOpenGLEngineSharedShaders(QOpenGLContext
    #      *context)
    self._noteCreation(QOpenGLEngineSharedShaders, lambda: Rituals.call(
        'ritual_ZN26QOpenGLEngineSharedShadersC1EP14QOpenGLContext',
        self._addressOf(context),
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

  def simpleProgram(self) -> Optional[QOpenGLShaderProgram]:
    """
    Calls Qt's 'QOpenGLShaderProgram
    *QOpenGLEngineSharedShaders::simpleProgram()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglenginesharedshaders.html#simpleProgram

    Returns
    -------

    Optional[QOpenGLShaderProgram]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLShaderProgram *QOpenGLEngineSharedShaders::simpleProgram()
    address = self.uglySide.call(
        'ritual_ZN26QOpenGLEngineSharedShaders13simpleProgramEv',
    )
    from . import QOpenGLShaderProgram
    return QOpenGLShaderProgram._cuteAt(address)

  def blitProgram(self) -> Optional[QOpenGLShaderProgram]:
    """
    Calls Qt's 'QOpenGLShaderProgram
    *QOpenGLEngineSharedShaders::blitProgram()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglenginesharedshaders.html#blitProgram

    Returns
    -------

    Optional[QOpenGLShaderProgram]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLShaderProgram *QOpenGLEngineSharedShaders::blitProgram()
    address = self.uglySide.call(
        'ritual_ZN26QOpenGLEngineSharedShaders11blitProgramEv',
    )
    from . import QOpenGLShaderProgram
    return QOpenGLShaderProgram._cuteAt(address)

  @overload(QOpenGLEngineShaderProg)
  def findProgramInCache(
      self,
      prog: QOpenGLEngineShaderProg,
  ) -> Optional[QOpenGLEngineShaderProg]:
    """
    Calls Qt's 'QOpenGLEngineShaderProg
    *QOpenGLEngineSharedShaders::findProgramInCache(const
    QOpenGLEngineShaderProg &prog)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglenginesharedshaders.html#findProgramInCache

    Parameters
    ----------

    prog : QOpenGLEngineShaderProg
      Passed on as a value: Qt reads the C++ QOpenGLEngineShaderProg, which
      stays Python's own.

    Returns
    -------

    Optional[QOpenGLEngineShaderProg]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLEngineShaderProg
    #      *QOpenGLEngineSharedShaders::findProgramInCache(const
    #      QOpenGLEngineShaderProg &prog)
    address = self.uglySide.call(
        'ritual_ZN26QOpenGLEngineSharedShaders18findProgramInCacheERK23QOpe'
        'nGLEngineShaderProg',
        self._valueOf(prog),
    )
    from . import QOpenGLEngineShaderProg
    return QOpenGLEngineShaderProg._cuteAt(address)

  @overload(QOpenGLCustomShaderStage)
  @overload(NoneType)
  def cleanupCustomStage(
      self,
      stage: Optional[QOpenGLCustomShaderStage],
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLEngineSharedShaders::cleanupCustomStage(QOpenGLCustomShaderStage
    *stage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglenginesharedshaders.html#cleanupCustomStage

    Parameters
    ----------

    stage : Optional[QOpenGLCustomShaderStage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLEngineSharedShaders::cleanupCustomStage(
    #      QOpenGLCustomShaderStage *stage)
    self.uglySide.call(
        'ritual_ZN26QOpenGLEngineSharedShaders18cleanupCustomStageEP24QOpen'
        'GLCustomShaderStage',
        self._addressOf(stage),
    )
