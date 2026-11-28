"""
QOpenGLEngineShaderManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/6.12.0/QtOpenGL/private/qopenglengineshadermanager_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QOpenGLEngineShaderManager to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtGui import QPainter, QTransform

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QOpenGLContext
  from . import QOpenGLCustomShaderStage, QOpenGLShaderProgram
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpenGLContext = WAIT['QOpenGLContext']
  QOpenGLCustomShaderStage = WAIT['QOpenGLCustomShaderStage']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLEngineShaderManager(QObject):
  """
  The cute side of Qt's QOpenGLEngineShaderManager: a plain Python object
  standing in front of one C++ QOpenGLEngineShaderManager.

  It is built on the cute 'QObject', as Qt's QOpenGLEngineShaderManager is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGLEngineShaderManager that has a ritual and
  that Python can call so far, 19 names in all: 'metaObject', 'tr',
  'optimiseForBrushTransform', 'setSrcPixelType', 'setOpacityMode',
  'setMaskType', 'setCompositionMode', 'setCustomStage', 'removeCustomStage',
  'getUniformLocation', 'setDirty', 'useCorrectShaderProg',
  'useSimpleProgram', 'useBlitProgram', 'setHasComplexGeometry',
  'hasComplexGeometry', 'currentProgram', 'simpleProgram', 'blitProgram'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QOpenGLEngineShaderManager::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QOpenGLEngineShaderManager::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QOpenGLEngineShaderManager::~QOpenGLEngineShaderManager()': the
    destructor: Python never removes a C++ QOpenGLEngineShaderManager.

  What has no ritual
  ------------------

  2 of the 26 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QOpenGLEngineShaderManager is created at the first use, not by
    'QOpenGLEngineShaderManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLEngineShaderManager.
  - Qt tells when it has removed the C++ QOpenGLEngineShaderManager. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QOpenGLEngineShaderManager, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class MaskType(CuteNum):
    """
    The enum 'QOpenGLEngineShaderManager::MaskType' of Qt, with the 5 names
    Qt gives in it.
    """

    NoMask = Kee[int](0)
    PixelMask = Kee[int](1)
    SubPixelMaskPass1 = Kee[int](2)
    SubPixelMaskPass2 = Kee[int](3)
    SubPixelWithGammaMask = Kee[int](4)

  class OpacityMode(CuteNum):
    """
    The enum 'QOpenGLEngineShaderManager::OpacityMode' of Qt, with the 3
    names Qt gives in it.
    """

    NoOpacity = Kee[int](0)
    UniformOpacity = Kee[int](1)
    AttributeOpacity = Kee[int](2)

  class PixelSrcType(CuteNum):
    """
    The enum 'QOpenGLEngineShaderManager::PixelSrcType' of Qt, with the 6
    names Qt gives in it.
    """

    ImageSrc = Kee[int](25)
    NonPremultipliedImageSrc = Kee[int](26)
    PatternSrc = Kee[int](27)
    TextureSrcWithPattern = Kee[int](28)
    GrayscaleImageSrc = Kee[int](29)
    AlphaImageSrc = Kee[int](30)

  class Uniform(CuteNum):
    """
    The enum 'QOpenGLEngineShaderManager::Uniform' of Qt, with the 19 names
    Qt gives in it.
    """

    ImageTexture = Kee[int](0)
    PatternColor = Kee[int](1)
    GlobalOpacity = Kee[int](2)
    Depth = Kee[int](3)
    MaskTexture = Kee[int](4)
    FragmentColor = Kee[int](5)
    LinearData = Kee[int](6)
    Angle = Kee[int](7)
    HalfViewportSize = Kee[int](8)
    Fmp = Kee[int](9)
    Fmp2MRadius2 = Kee[int](10)
    Inverse2Fmp2MRadius2 = Kee[int](11)
    SqrFr = Kee[int](12)
    BRadius = Kee[int](13)
    InvertedTextureSize = Kee[int](14)
    BrushTransform = Kee[int](15)
    BrushTexture = Kee[int](16)
    Matrix = Kee[int](17)
    NumUniforms = Kee[int](18)

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
    Calls Qt's 'QString QOpenGLEngineShaderManager::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglengineshadermanager.html#tr

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
    #  QString QOpenGLEngineShaderManager::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QOpenGLEngineShaderManager2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLEngineShaderManager'

  #  A C++ QOpenGLEngineShaderManager Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGLEngineShaderManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QOpenGLEngineShaderManager::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglengineshadermanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOpenGLEngineShaderManager::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QOpenGLEngineShaderManager10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def hasComplexGeometry(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLEngineShaderManager::hasComplexGeometry() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglengineshadermanager.html#hasComplexGeometry
    """
    #  bool QOpenGLEngineShaderManager::hasComplexGeometry() const
    return self.uglySide.call(
        'ritual_ZNK26QOpenGLEngineShaderManager18hasComplexGeometryEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.BrushStyle)
  def setSrcPixelType(self, a0: Qt.BrushStyle) -> None:
    """
    Calls Qt's 'void
    QOpenGLEngineShaderManager::setSrcPixelType(Qt::BrushStyle a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglengineshadermanager.html#setSrcPixelType

    Parameters
    ----------

    a0 : Qt.BrushStyle
      Passed on as its number.
    """
    #  void QOpenGLEngineShaderManager::setSrcPixelType(Qt::BrushStyle a0)
    self.uglySide.call(
        'ritual_ZN26QOpenGLEngineShaderManager15setSrcPixelTypeEN2Qt10Brush'
        'StyleE',
        a0.value,
    )

  @overload(PixelSrcType)
  def setSrcPixelType(self, a0: PixelSrcType) -> None:
    """
    Calls Qt's 'void QOpenGLEngineShaderManager::setSrcPixelType(PixelSrcType
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglengineshadermanager.html#setSrcPixelType

    Parameters
    ----------

    a0 : PixelSrcType
      Passed on as its number.
    """
    #  void QOpenGLEngineShaderManager::setSrcPixelType(PixelSrcType a0)
    self.uglySide.call(
        'ritual_ZN26QOpenGLEngineShaderManager15setSrcPixelTypeENS_12PixelS'
        'rcTypeE',
        a0.value,
    )

  @overload(OpacityMode)
  def setOpacityMode(self, a0: OpacityMode) -> None:
    """
    Calls Qt's 'void QOpenGLEngineShaderManager::setOpacityMode(OpacityMode
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglengineshadermanager.html#setOpacityMode

    Parameters
    ----------

    a0 : OpacityMode
      Passed on as its number.
    """
    #  void QOpenGLEngineShaderManager::setOpacityMode(OpacityMode a0)
    self.uglySide.call(
        'ritual_ZN26QOpenGLEngineShaderManager14setOpacityModeENS_11Opacity'
        'ModeE',
        a0.value,
    )

  @overload(MaskType)
  def setMaskType(self, a0: MaskType) -> None:
    """
    Calls Qt's 'void QOpenGLEngineShaderManager::setMaskType(MaskType a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglengineshadermanager.html#setMaskType

    Parameters
    ----------

    a0 : MaskType
      Passed on as its number.
    """
    #  void QOpenGLEngineShaderManager::setMaskType(MaskType a0)
    self.uglySide.call(
        'ritual_ZN26QOpenGLEngineShaderManager11setMaskTypeENS_8MaskTypeE',
        a0.value,
    )

  @overload(QPainter.CompositionMode)
  def setCompositionMode(self, a0: QPainter.CompositionMode) -> None:
    """
    Calls Qt's 'void
    QOpenGLEngineShaderManager::setCompositionMode(QPainter::CompositionMode
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglengineshadermanager.html#setCompositionMode

    Parameters
    ----------

    a0 : QPainter.CompositionMode
      Passed on as its number.
    """
    #  void QOpenGLEngineShaderManager::setCompositionMode(QPainter::
    #      CompositionMode a0)
    self.uglySide.call(
        'ritual_ZN26QOpenGLEngineShaderManager18setCompositionModeEN8QPaint'
        'er15CompositionModeE',
        a0.value,
    )

  @overload(QOpenGLCustomShaderStage)
  @overload(NoneType)
  def setCustomStage(
      self,
      stage: Optional[QOpenGLCustomShaderStage],
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLEngineShaderManager::setCustomStage(QOpenGLCustomShaderStage
    *stage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglengineshadermanager.html#setCustomStage

    Parameters
    ----------

    stage : Optional[QOpenGLCustomShaderStage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLEngineShaderManager::setCustomStage(
    #      QOpenGLCustomShaderStage *stage)
    self.uglySide.call(
        'ritual_ZN26QOpenGLEngineShaderManager14setCustomStageEP24QOpenGLCu'
        'stomShaderStage',
        self._addressOf(stage),
    )

  def setDirty(self) -> None:
    """
    Calls Qt's 'void QOpenGLEngineShaderManager::setDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglengineshadermanager.html#setDirty
    """
    #  void QOpenGLEngineShaderManager::setDirty()
    self.uglySide.call('ritual_ZN26QOpenGLEngineShaderManager8setDirtyEv')

  @overload(bool)
  def setHasComplexGeometry(self, hasComplexGeometry: bool) -> None:
    """
    Calls Qt's 'void QOpenGLEngineShaderManager::setHasComplexGeometry(bool
    hasComplexGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglengineshadermanager.html

    Parameters
    ----------

    hasComplexGeometry : bool
      Passed on as it is.
    """
    #  void QOpenGLEngineShaderManager::setHasComplexGeometry(bool
    #      hasComplexGeometry)
    self.uglySide.call(
        'ritual_ZN26QOpenGLEngineShaderManager21setHasComplexGeometryEb',
        hasComplexGeometry,
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

  @overload(QOpenGLContext)
  @overload(NoneType)
  def __init__(self, context: Optional[QOpenGLContext]) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLEngineShaderManager::QOpenGLEngineShaderManager(QOpenGLContext
    *context)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglengineshadermanager.html

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOpenGLEngineShaderManager::QOpenGLEngineShaderManager(QOpenGLContext
    #      *context)
    self._noteCreation(QOpenGLEngineShaderManager, lambda: Rituals.call(
        'ritual_ZN26QOpenGLEngineShaderManagerC1EP14QOpenGLContext',
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

  @overload(QTransform.TransformationType)
  def optimiseForBrushTransform(
      self,
      transformType: QTransform.TransformationType,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLEngineShaderManager::optimiseForBrushTransform(QTransform::
    TransformationType transformType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglengineshadermanager.html

    Parameters
    ----------

    transformType : QTransform.TransformationType
      Passed on as its number.
    """
    #  void QOpenGLEngineShaderManager::optimiseForBrushTransform(
    #      QTransform::TransformationType transformType)
    self.uglySide.call(
        'ritual_ZN26QOpenGLEngineShaderManager25optimiseForBrushTransformEN'
        '10QTransform18TransformationTypeE',
        transformType.value,
    )

  def removeCustomStage(self) -> None:
    """
    Calls Qt's 'void QOpenGLEngineShaderManager::removeCustomStage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglengineshadermanager.html#removeCustomStage
    """
    #  void QOpenGLEngineShaderManager::removeCustomStage()
    self.uglySide.call(
        'ritual_ZN26QOpenGLEngineShaderManager17removeCustomStageEv',
    )

  @overload(Uniform)
  def getUniformLocation(self, id: Uniform) -> int:
    """
    Calls Qt's 'GLuint QOpenGLEngineShaderManager::getUniformLocation(Uniform
    id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglengineshadermanager.html#getUniformLocation

    Parameters
    ----------

    id : Uniform
      Passed on as its number.
    """
    #  GLuint QOpenGLEngineShaderManager::getUniformLocation(Uniform id)
    return self.uglySide.call(
        'ritual_ZN26QOpenGLEngineShaderManager18getUniformLocationENS_7Unif'
        'ormE',
        id.value,
    )

  def useCorrectShaderProg(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLEngineShaderManager::useCorrectShaderProg()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglengineshadermanager.html
    """
    #  bool QOpenGLEngineShaderManager::useCorrectShaderProg()
    return self.uglySide.call(
        'ritual_ZN26QOpenGLEngineShaderManager20useCorrectShaderProgEv',
    )

  def useSimpleProgram(self) -> None:
    """
    Calls Qt's 'void QOpenGLEngineShaderManager::useSimpleProgram()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglengineshadermanager.html#useSimpleProgram
    """
    #  void QOpenGLEngineShaderManager::useSimpleProgram()
    self.uglySide.call(
        'ritual_ZN26QOpenGLEngineShaderManager16useSimpleProgramEv',
    )

  def useBlitProgram(self) -> None:
    """
    Calls Qt's 'void QOpenGLEngineShaderManager::useBlitProgram()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglengineshadermanager.html#useBlitProgram
    """
    #  void QOpenGLEngineShaderManager::useBlitProgram()
    self.uglySide.call(
        'ritual_ZN26QOpenGLEngineShaderManager14useBlitProgramEv',
    )

  def currentProgram(self) -> Optional[QOpenGLShaderProgram]:
    """
    Calls Qt's 'QOpenGLShaderProgram
    *QOpenGLEngineShaderManager::currentProgram()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglengineshadermanager.html#currentProgram

    Returns
    -------

    Optional[QOpenGLShaderProgram]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLShaderProgram *QOpenGLEngineShaderManager::currentProgram()
    address = self.uglySide.call(
        'ritual_ZN26QOpenGLEngineShaderManager14currentProgramEv',
    )
    from . import QOpenGLShaderProgram
    return QOpenGLShaderProgram._cuteAt(address)

  def simpleProgram(self) -> Optional[QOpenGLShaderProgram]:
    """
    Calls Qt's 'QOpenGLShaderProgram
    *QOpenGLEngineShaderManager::simpleProgram()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglengineshadermanager.html#simpleProgram

    Returns
    -------

    Optional[QOpenGLShaderProgram]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLShaderProgram *QOpenGLEngineShaderManager::simpleProgram()
    address = self.uglySide.call(
        'ritual_ZN26QOpenGLEngineShaderManager13simpleProgramEv',
    )
    from . import QOpenGLShaderProgram
    return QOpenGLShaderProgram._cuteAt(address)

  def blitProgram(self) -> Optional[QOpenGLShaderProgram]:
    """
    Calls Qt's 'QOpenGLShaderProgram
    *QOpenGLEngineShaderManager::blitProgram()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglengineshadermanager.html#blitProgram

    Returns
    -------

    Optional[QOpenGLShaderProgram]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLShaderProgram *QOpenGLEngineShaderManager::blitProgram()
    address = self.uglySide.call(
        'ritual_ZN26QOpenGLEngineShaderManager11blitProgramEv',
    )
    from . import QOpenGLShaderProgram
    return QOpenGLShaderProgram._cuteAt(address)
