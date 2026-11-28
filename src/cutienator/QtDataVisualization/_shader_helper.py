"""
ShaderHelper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/shaderhelper_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means ShaderHelper to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from ..QtGui import QMatrix4x4, QVector2D, QVector3D, QVector4D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QObject = WAIT['QObject']
  QVector2D = WAIT['QVector2D']
  QVector3D = WAIT['QVector3D']
  QVector4D = WAIT['QVector4D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ShaderHelper(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's ShaderHelper: a plain Python object standing in front
  of one C++ ShaderHelper.

  C++ hands a ShaderHelper around as a copy, so every C++ ShaderHelper behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's ShaderHelper that has a ritual and that Python can
  call so far, 37 names in all: 'setShaders', 'setTextures', 'initialize',
  'testCompile', 'bind', 'release', 'setUniformValue',
  'setUniformValueArray', 'MVP', 'view', 'model', 'nModel', 'depth',
  'lightP', 'lightS', 'ambientS', 'shadowQ', 'color', 'texture', 'shadow',
  'gradientMin', 'gradientHeight', 'lightColor', 'volumeSliceIndices',
  'colorIndex', 'cameraPositionRelativeToModel', 'color8Bit',
  'textureDimensions', 'sampleCount', 'alphaMultiplier', 'preserveOpacity',
  'maxBounds', 'minBounds', 'sliceFrameWidth', 'posAtt', 'uvAtt',
  'normalAtt'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'ShaderHelper::~ShaderHelper()': the destructor: Python removes its
    C++ ShaderHelper by it, and has no other use for it.

  What to expect
  --------------

  - The C++ ShaderHelper is created at the first use, not by
    'ShaderHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a ShaderHelper back gives a copy the ritual made for
    Python, in a new cute ShaderHelper.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ShaderHelper'

  #  Qt's '~ShaderHelper()'. Naming it makes this a value class: Python owns
  #  every C++ ShaderHelper behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12ShaderHelperD1Ev'

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

  @overload(str, str)
  def setShaders(self, vertexShader: str, fragmentShader: str) -> None:
    """
    Calls Qt's 'void ShaderHelper::setShaders(const QString &vertexShader,
    const QString &fragmentShader)'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#setShaders

    Parameters
    ----------

    vertexShader : str
      Passed on as it is: a QString is made of it for the call.

    fragmentShader : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void ShaderHelper::setShaders(const QString &vertexShader, const
    #      QString &fragmentShader)
    self.uglySide.call(
        'ritual_ZN12ShaderHelper10setShadersERK7QStringS2_',
        vertexShader, fragmentShader,
    )

  @overload(str, str)
  def setTextures(self, texture: str, depthTexture: str) -> None:
    """
    Calls Qt's 'void ShaderHelper::setTextures(const QString &texture, const
    QString &depthTexture)'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#setTextures

    Parameters
    ----------

    texture : str
      Passed on as it is: a QString is made of it for the call.

    depthTexture : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void ShaderHelper::setTextures(const QString &texture, const QString
    #      &depthTexture)
    self.uglySide.call(
        'ritual_ZN12ShaderHelper11setTexturesERK7QStringS2_',
        texture, depthTexture,
    )

  @overload(int, QVector2D)
  def setUniformValue(self, uniform: int, value: QVector2D) -> None:
    """
    Calls Qt's 'void ShaderHelper::setUniformValue(GLint uniform, const
    QVector2D &value)'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#setUniformValue

    Parameters
    ----------

    uniform : int
      Passed on as it is.

    value : QVector2D
      Passed on as a value: Qt reads the C++ QVector2D, which stays Python's
      own.
    """
    #  void ShaderHelper::setUniformValue(GLint uniform, const QVector2D
    #      &value)
    self.uglySide.call(
        'ritual_ZN12ShaderHelper15setUniformValueEiRK9QVector2D',
        uniform, self._valueOf(value),
    )

  @overload(int, QVector3D)
  def setUniformValue(self, uniform: int, value: QVector3D) -> None:
    """
    Calls Qt's 'void ShaderHelper::setUniformValue(GLint uniform, const
    QVector3D &value)'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#setUniformValue

    Parameters
    ----------

    uniform : int
      Passed on as it is.

    value : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void ShaderHelper::setUniformValue(GLint uniform, const QVector3D
    #      &value)
    self.uglySide.call(
        'ritual_ZN12ShaderHelper15setUniformValueEiRK9QVector3D',
        uniform, self._valueOf(value),
    )

  @overload(int, QVector4D)
  def setUniformValue(self, uniform: int, value: QVector4D) -> None:
    """
    Calls Qt's 'void ShaderHelper::setUniformValue(GLint uniform, const
    QVector4D &value)'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#setUniformValue

    Parameters
    ----------

    uniform : int
      Passed on as it is.

    value : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  void ShaderHelper::setUniformValue(GLint uniform, const QVector4D
    #      &value)
    self.uglySide.call(
        'ritual_ZN12ShaderHelper15setUniformValueEiRK9QVector4D',
        uniform, self._valueOf(value),
    )

  @overload(int, QMatrix4x4)
  def setUniformValue(self, uniform: int, value: QMatrix4x4) -> None:
    """
    Calls Qt's 'void ShaderHelper::setUniformValue(GLint uniform, const
    QMatrix4x4 &value)'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#setUniformValue

    Parameters
    ----------

    uniform : int
      Passed on as it is.

    value : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.
    """
    #  void ShaderHelper::setUniformValue(GLint uniform, const QMatrix4x4
    #      &value)
    self.uglySide.call(
        'ritual_ZN12ShaderHelper15setUniformValueEiRK10QMatrix4x4',
        uniform, self._valueOf(value),
    )

  @overload(int, float)
  def setUniformValue(self, uniform: int, value: float) -> None:
    """
    Calls Qt's 'void ShaderHelper::setUniformValue(GLint uniform, GLfloat
    value)'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#setUniformValue

    Parameters
    ----------

    uniform : int
      Passed on as it is.

    value : float
      Passed on as it is.
    """
    #  void ShaderHelper::setUniformValue(GLint uniform, GLfloat value)
    self.uglySide.call(
        'ritual_ZN12ShaderHelper15setUniformValueEif', uniform, value,
    )

  @overload(int, int)
  def setUniformValue(self, uniform: int, value: int) -> None:
    """
    Calls Qt's 'void ShaderHelper::setUniformValue(GLint uniform, GLint
    value)'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#setUniformValue

    Parameters
    ----------

    uniform : int
      Passed on as it is.

    value : int
      Passed on as it is.
    """
    #  void ShaderHelper::setUniformValue(GLint uniform, GLint value)
    self.uglySide.call(
        'ritual_ZN12ShaderHelper15setUniformValueEii', uniform, value,
    )

  @overload(int, QVector4D, int)
  @overload(int, NoneType, int)
  def setUniformValueArray(
      self,
      uniform: int,
      values: Optional[QVector4D],
      count: int,
  ) -> None:
    """
    Calls Qt's 'void ShaderHelper::setUniformValueArray(GLint uniform, const
    QVector4D *values, int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/shaderhelper.html#setUniformValueArray

    Parameters
    ----------

    uniform : int
      Passed on as it is.

    values : Optional[QVector4D]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    count : int
      Passed on as it is.
    """
    #  void ShaderHelper::setUniformValueArray(GLint uniform, const QVector4D
    #      *values, int count)
    self.uglySide.call(
        'ritual_ZN12ShaderHelper20setUniformValueArrayEiPK9QVector4Di',
        uniform, self._addressOf(values), count,
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

  @overload(QObject)
  @overload(NoneType)
  @overload(QObject, str)
  @overload(NoneType, str)
  @overload(QObject, str, str)
  @overload(NoneType, str, str)
  @overload(QObject, str, str, str)
  @overload(NoneType, str, str, str)
  @overload(QObject, str, str, str, str)
  @overload(NoneType, str, str, str, str)
  def __init__(
      self,
      parent: Optional[QObject],
      vertexShader: str = '',
      fragmentShader: str = '',
      texture: str = '',
      depthTexture: str = '',
  ) -> None:
    """
    Notes what was given, for Qt's 'ShaderHelper::ShaderHelper(QObject
    *parent, const QString &vertexShader, const QString &fragmentShader,
    const QString &texture, const QString &depthTexture)', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#ShaderHelper

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    vertexShader : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    fragmentShader : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    texture : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    depthTexture : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  ShaderHelper::ShaderHelper(QObject *parent, const QString
    #      &vertexShader, const QString &fragmentShader, const QString
    #      &texture, const QString &depthTexture)
    self._noteCreation(ShaderHelper, lambda: Rituals.call(
        'ritual_ZN12ShaderHelperC1EP7QObjectRK7QStringS4_S4_S4_',
        self._addressOf(parent, 'QObject'), vertexShader, fragmentShader,
        texture, depthTexture,
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

  def initialize(self) -> None:
    """
    Calls Qt's 'void ShaderHelper::initialize()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#initialize
    """
    #  void ShaderHelper::initialize()
    self.uglySide.call('ritual_ZN12ShaderHelper10initializeEv')

  def testCompile(self) -> bool:
    """
    Calls Qt's 'bool ShaderHelper::testCompile()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#testCompile
    """
    #  bool ShaderHelper::testCompile()
    return self.uglySide.call('ritual_ZN12ShaderHelper11testCompileEv')

  def bind(self) -> None:
    """
    Calls Qt's 'void ShaderHelper::bind()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#bind
    """
    #  void ShaderHelper::bind()
    self.uglySide.call('ritual_ZN12ShaderHelper4bindEv')

  def release(self) -> None:
    """
    Calls Qt's 'void ShaderHelper::release()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#release
    """
    #  void ShaderHelper::release()
    self.uglySide.call('ritual_ZN12ShaderHelper7releaseEv')

  def MVP(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::MVP()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#MVP
    """
    #  GLint ShaderHelper::MVP()
    return self.uglySide.call('ritual_ZN12ShaderHelper3MVPEv')

  def view(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::view()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#view
    """
    #  GLint ShaderHelper::view()
    return self.uglySide.call('ritual_ZN12ShaderHelper4viewEv')

  def model(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::model()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#model
    """
    #  GLint ShaderHelper::model()
    return self.uglySide.call('ritual_ZN12ShaderHelper5modelEv')

  def nModel(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::nModel()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#nModel
    """
    #  GLint ShaderHelper::nModel()
    return self.uglySide.call('ritual_ZN12ShaderHelper6nModelEv')

  def depth(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::depth()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#depth
    """
    #  GLint ShaderHelper::depth()
    return self.uglySide.call('ritual_ZN12ShaderHelper5depthEv')

  def lightP(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::lightP()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#lightP
    """
    #  GLint ShaderHelper::lightP()
    return self.uglySide.call('ritual_ZN12ShaderHelper6lightPEv')

  def lightS(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::lightS()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#lightS
    """
    #  GLint ShaderHelper::lightS()
    return self.uglySide.call('ritual_ZN12ShaderHelper6lightSEv')

  def ambientS(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::ambientS()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#ambientS
    """
    #  GLint ShaderHelper::ambientS()
    return self.uglySide.call('ritual_ZN12ShaderHelper8ambientSEv')

  def shadowQ(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::shadowQ()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#shadowQ
    """
    #  GLint ShaderHelper::shadowQ()
    return self.uglySide.call('ritual_ZN12ShaderHelper7shadowQEv')

  def color(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::color()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#color
    """
    #  GLint ShaderHelper::color()
    return self.uglySide.call('ritual_ZN12ShaderHelper5colorEv')

  def texture(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::texture()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#texture
    """
    #  GLint ShaderHelper::texture()
    return self.uglySide.call('ritual_ZN12ShaderHelper7textureEv')

  def shadow(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::shadow()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#shadow
    """
    #  GLint ShaderHelper::shadow()
    return self.uglySide.call('ritual_ZN12ShaderHelper6shadowEv')

  def gradientMin(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::gradientMin()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#gradientMin
    """
    #  GLint ShaderHelper::gradientMin()
    return self.uglySide.call('ritual_ZN12ShaderHelper11gradientMinEv')

  def gradientHeight(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::gradientHeight()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#gradientHeight
    """
    #  GLint ShaderHelper::gradientHeight()
    return self.uglySide.call('ritual_ZN12ShaderHelper14gradientHeightEv')

  def lightColor(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::lightColor()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#lightColor
    """
    #  GLint ShaderHelper::lightColor()
    return self.uglySide.call('ritual_ZN12ShaderHelper10lightColorEv')

  def volumeSliceIndices(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::volumeSliceIndices()'.

    Qt's own words:
    https://doc.qt.io/qt-6/shaderhelper.html#volumeSliceIndices
    """
    #  GLint ShaderHelper::volumeSliceIndices()
    return self.uglySide.call(
        'ritual_ZN12ShaderHelper18volumeSliceIndicesEv',
    )

  def colorIndex(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::colorIndex()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#colorIndex
    """
    #  GLint ShaderHelper::colorIndex()
    return self.uglySide.call('ritual_ZN12ShaderHelper10colorIndexEv')

  def cameraPositionRelativeToModel(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::cameraPositionRelativeToModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/shaderhelper.html#cameraPositionRelativeToModel
    """
    #  GLint ShaderHelper::cameraPositionRelativeToModel()
    return self.uglySide.call(
        'ritual_ZN12ShaderHelper29cameraPositionRelativeToModelEv',
    )

  def color8Bit(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::color8Bit()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#color8Bit
    """
    #  GLint ShaderHelper::color8Bit()
    return self.uglySide.call('ritual_ZN12ShaderHelper9color8BitEv')

  def textureDimensions(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::textureDimensions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/shaderhelper.html#textureDimensions
    """
    #  GLint ShaderHelper::textureDimensions()
    return self.uglySide.call('ritual_ZN12ShaderHelper17textureDimensionsEv')

  def sampleCount(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::sampleCount()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#sampleCount
    """
    #  GLint ShaderHelper::sampleCount()
    return self.uglySide.call('ritual_ZN12ShaderHelper11sampleCountEv')

  def alphaMultiplier(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::alphaMultiplier()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#alphaMultiplier
    """
    #  GLint ShaderHelper::alphaMultiplier()
    return self.uglySide.call('ritual_ZN12ShaderHelper15alphaMultiplierEv')

  def preserveOpacity(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::preserveOpacity()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#preserveOpacity
    """
    #  GLint ShaderHelper::preserveOpacity()
    return self.uglySide.call('ritual_ZN12ShaderHelper15preserveOpacityEv')

  def maxBounds(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::maxBounds()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#maxBounds
    """
    #  GLint ShaderHelper::maxBounds()
    return self.uglySide.call('ritual_ZN12ShaderHelper9maxBoundsEv')

  def minBounds(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::minBounds()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#minBounds
    """
    #  GLint ShaderHelper::minBounds()
    return self.uglySide.call('ritual_ZN12ShaderHelper9minBoundsEv')

  def sliceFrameWidth(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::sliceFrameWidth()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#sliceFrameWidth
    """
    #  GLint ShaderHelper::sliceFrameWidth()
    return self.uglySide.call('ritual_ZN12ShaderHelper15sliceFrameWidthEv')

  def posAtt(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::posAtt()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#posAtt
    """
    #  GLint ShaderHelper::posAtt()
    return self.uglySide.call('ritual_ZN12ShaderHelper6posAttEv')

  def uvAtt(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::uvAtt()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#uvAtt
    """
    #  GLint ShaderHelper::uvAtt()
    return self.uglySide.call('ritual_ZN12ShaderHelper5uvAttEv')

  def normalAtt(self) -> int:
    """
    Calls Qt's 'GLint ShaderHelper::normalAtt()'.

    Qt's own words: https://doc.qt.io/qt-6/shaderhelper.html#normalAtt
    """
    #  GLint ShaderHelper::normalAtt()
    return self.uglySide.call('ritual_ZN12ShaderHelper9normalAttEv')
