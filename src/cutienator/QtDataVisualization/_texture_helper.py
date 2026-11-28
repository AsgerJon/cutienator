"""
TextureHelper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/texturehelper_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means TextureHelper to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtGui import QOpenGLFunctions

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtGui import QImage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']


class TextureHelper(QOpenGLFunctions):
  """
  The cute side of Qt's TextureHelper: a plain Python object standing in
  front of one C++ TextureHelper.

  It is built on the cute 'QOpenGLFunctions', as Qt's TextureHelper is built
  on Qt's QOpenGLFunctions, and has everything that class has.

  C++ hands a TextureHelper around as a copy, so every C++ TextureHelper
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's TextureHelper that has a ritual and that Python can
  call so far, 2 names in all: 'createCubeMapTexture', 'convertToGLFormat'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'TextureHelper::~TextureHelper()': the destructor: Python removes
    its C++ TextureHelper by it, and has no other use for it.
  - Qt's 'GLuint TextureHelper::createCursorPositionTexture(const QSize
    &size, GLuint &frameBuffer)': takes a number to change where it is.
  - Qt's 'void TextureHelper::deleteTexture(GLuint *texture)': takes a number
    to change where it is.
  - Qt's 'void TextureHelper::convertToGLFormatHelper(QImage &dstImage, const
    QImage &srcImage, GLenum texture_format)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QRgb TextureHelper::qt_gl_convertToGLFormatHelper(QRgb src_pixel,
    GLenum texture_format)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  8 of the 15 functions Qt declares: 7 leans on 'Utils; 1 Qt's library has no
  name for it, and its code in Qt's source does not compile apart from its
  file.

  What to expect
  --------------

  - The C++ TextureHelper is created at the first use, not by
    'TextureHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a TextureHelper back gives a copy the ritual made for
    Python, in a new cute TextureHelper.
  - Each name of Qt's TextureHelper that has no cute function yet,
    '__init__', 'convertToGLFormatHelper', 'create2DTexture',
    'create3DTexture', 'createCursorPositionTexture', 'createDepthTexture',
    'createDepthTextureFrameBuffer', 'createGradientTexture',
    'createSelectionTexture', 'createUniformTexture', 'deleteTexture', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'TextureHelper'

  #  Qt's '~TextureHelper()'. Naming it makes this a value class: Python owns
  #  every C++ TextureHelper behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN13TextureHelperD1Ev'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'TextureHelper::TextureHelper()': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'discardDebugMsgs'.
    """
    raise NotImplementedError(
        "'TextureHelper.__init__' has no cute function yet. Qt's "
        "'TextureHelper::TextureHelper()': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'discardDebugMsgs'.")

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

  @overload(QImage)
  @overload(QImage, bool)
  def createCubeMapTexture(
      self,
      image: QImage,
      useTrilinearFiltering: bool = False,
  ) -> int:
    """
    Calls Qt's 'GLuint TextureHelper::createCubeMapTexture(const QImage
    &image, bool useTrilinearFiltering)'.

    Qt's own words:
    https://doc.qt.io/qt-6/texturehelper.html#createCubeMapTexture

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    useTrilinearFiltering : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  GLuint TextureHelper::createCubeMapTexture(const QImage &image, bool
    #      useTrilinearFiltering)
    return self.uglySide.call(
        'ritual_ZN13TextureHelper20createCubeMapTextureERK6QImageb',
        self._valueOf(image), useTrilinearFiltering,
    )

  @overload(QImage)
  def convertToGLFormat(self, srcImage: QImage) -> QImage:
    """
    Calls Qt's 'QImage TextureHelper::convertToGLFormat(const QImage
    &srcImage)'.

    Qt's own words:
    https://doc.qt.io/qt-6/texturehelper.html#convertToGLFormat

    Parameters
    ----------

    srcImage : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage TextureHelper::convertToGLFormat(const QImage &srcImage)
    address = self.uglySide.call(
        'ritual_ZN13TextureHelper17convertToGLFormatERK6QImage',
        self._valueOf(srcImage),
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  @staticmethod
  def convertToGLFormatHelper(*__, **_) -> Never:
    """
    Qt's 'void TextureHelper::convertToGLFormatHelper(QImage &dstImage, const
    QImage &srcImage, GLenum texture_format)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'TextureHelper.convertToGLFormatHelper' has no cute function yet. "
        "Qt's 'void TextureHelper::convertToGLFormatHelper(QImage "
        "&dstImage, const QImage &srcImage, GLenum texture_format)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def create2DTexture(*__, **_) -> Never:
    """
    Qt's 'GLuint TextureHelper::create2DTexture(const QImage &image, bool
    useTrilinearFiltering, bool convert, bool smoothScale, bool clampY)':
    leans on 'Utils::isOpenGLES()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'TextureHelper.create2DTexture' has no cute function yet. Qt's "
        "'GLuint TextureHelper::create2DTexture(const QImage &image, bool "
        "useTrilinearFiltering, bool convert, bool smoothScale, bool "
        "clampY)': leans on 'Utils::isOpenGLES()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def create3DTexture(*__, **_) -> Never:
    """
    Qt's 'GLuint TextureHelper::create3DTexture(const QList<uchar> *data, int
    width, int height, int depth, QImage::Format dataFormat)': leans on
    'Utils::isOpenGLES()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'TextureHelper.create3DTexture' has no cute function yet. Qt's "
        "'GLuint TextureHelper::create3DTexture(const QList<uchar> *data, "
        "int width, int height, int depth, QImage::Format dataFormat)': "
        "leans on 'Utils::isOpenGLES()', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def createCursorPositionTexture(*__, **_) -> Never:
    """
    Qt's 'GLuint TextureHelper::createCursorPositionTexture(const QSize
    &size, GLuint &frameBuffer)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'TextureHelper.createCursorPositionTexture' has no cute function "
        "yet. Qt's 'GLuint TextureHelper::createCursorPositionTexture(const "
        "QSize &size, GLuint &frameBuffer)': takes a number to change where "
        "it is.")

  @staticmethod
  def createDepthTexture(*__, **_) -> Never:
    """
    Qt's 'GLuint TextureHelper::createDepthTexture(const QSize &size, GLuint
    textureSize)': leans on 'Utils::isOpenGLES()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'TextureHelper.createDepthTexture' has no cute function yet. Qt's "
        "'GLuint TextureHelper::createDepthTexture(const QSize &size, "
        "GLuint textureSize)': leans on 'Utils::isOpenGLES()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def createDepthTextureFrameBuffer(*__, **_) -> Never:
    """
    Qt's 'GLuint TextureHelper::createDepthTextureFrameBuffer(const QSize
    &size, GLuint &frameBuffer, GLuint textureSize)': leans on
    'Utils::isOpenGLES()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'TextureHelper.createDepthTextureFrameBuffer' has no cute function "
        "yet. Qt's 'GLuint "
        "TextureHelper::createDepthTextureFrameBuffer(const QSize &size, "
        "GLuint &frameBuffer, GLuint textureSize)': leans on "
        "'Utils::isOpenGLES()', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def createGradientTexture(*__, **_) -> Never:
    """
    Qt's 'GLuint TextureHelper::createGradientTexture(const QLinearGradient
    &gradient)': leans on 'Utils::isOpenGLES()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'TextureHelper.createGradientTexture' has no cute function yet. "
        "Qt's 'GLuint TextureHelper::createGradientTexture(const "
        "QLinearGradient &gradient)': leans on 'Utils::isOpenGLES()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def createSelectionTexture(*__, **_) -> Never:
    """
    Qt's 'GLuint TextureHelper::createSelectionTexture(const QSize &size,
    GLuint &frameBuffer, GLuint &depthBuffer)': leans on
    'Utils::isOpenGLES()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'TextureHelper.createSelectionTexture' has no cute function yet. "
        "Qt's 'GLuint TextureHelper::createSelectionTexture(const QSize "
        "&size, GLuint &frameBuffer, GLuint &depthBuffer)': leans on "
        "'Utils::isOpenGLES()', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

  @staticmethod
  def createUniformTexture(*__, **_) -> Never:
    """
    Qt's 'GLuint TextureHelper::createUniformTexture(const QColor &color)':
    leans on 'Utils::isOpenGLES()', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'TextureHelper.createUniformTexture' has no cute function yet. "
        "Qt's 'GLuint TextureHelper::createUniformTexture(const QColor "
        "&color)': leans on 'Utils::isOpenGLES()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def deleteTexture(*__, **_) -> Never:
    """
    Qt's 'void TextureHelper::deleteTexture(GLuint *texture)': takes a number
    to change where it is.
    """
    raise NotImplementedError(
        "'TextureHelper.deleteTexture' has no cute function yet. Qt's 'void "
        "TextureHelper::deleteTexture(GLuint *texture)': takes a number to "
        "change where it is.")
