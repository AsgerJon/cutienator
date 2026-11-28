"""
QOpenGLTextureHelper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/6.12.0/QtOpenGL/private/qopengltexturehelper_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QOpenGLTextureHelper to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QOpenGLContext
  from . import QOpenGLPixelTransferOptions
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpenGLContext = WAIT['QOpenGLContext']
  QOpenGLPixelTransferOptions = WAIT['QOpenGLPixelTransferOptions']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLTextureHelper(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLTextureHelper: a plain Python object standing
  in front of one C++ QOpenGLTextureHelper.

  C++ hands a QOpenGLTextureHelper around as a copy, so every C++
  QOpenGLTextureHelper behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpenGLTextureHelper that has a ritual and that
  Python can call so far, 33 names in all: 'glTextureParameteri',
  'glTextureParameterf', 'glGenerateTextureMipmap', 'glTextureStorage3D',
  'glTextureStorage2D', 'glTextureStorage1D',
  'glTextureStorage3DMultisample', 'glTextureStorage2DMultisample',
  'glTextureImage3DMultisample', 'glTextureImage2DMultisample',
  'dsa_TextureParameteri', 'dsa_TextureParameterf',
  'dsa_GenerateTextureMipmap', 'dsa_TextureStorage3D',
  'dsa_TextureStorage2D', 'dsa_TextureStorage1D',
  'dsa_TextureStorage3DMultisample', 'dsa_TextureStorage2DMultisample',
  'dsa_TextureImage3DMultisample', 'dsa_TextureImage2DMultisample',
  'glActiveTexture', 'glGenerateMipmap', 'glTexImage3DMultisample',
  'glTexImage2DMultisample', 'glTexStorage3D', 'glTexStorage2D',
  'glTexStorage1D', 'glTexStorage3DMultisample', 'glTexStorage2DMultisample',
  'glTexBufferRange', 'glTextureView', 'savePixelUploadOptions',
  'setPixelUploadOptions'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QOpenGLTextureHelper::glTextureParameteriv(GLuint texture,
    GLenum target, GLenum bindingTarget, GLenum pname, const GLint *params)':
    names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::glTextureParameterfv(GLuint texture,
    GLenum target, GLenum bindingTarget, GLenum pname, const GLfloat
    *params)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::glTextureImage3D(GLuint texture, GLenum
    target, GLenum bindingTarget, GLint level, GLenum internalFormat, GLsizei
    width, GLsizei height, GLsizei depth, GLint border, GLenum format, GLenum
    type, const GLvoid *pixels)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void QOpenGLTextureHelper::glTextureImage2D(GLuint texture, GLenum
    target, GLenum bindingTarget, GLint level, GLenum internalFormat, GLsizei
    width, GLsizei height, GLint border, GLenum format, GLenum type, const
    GLvoid *pixels)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::glTextureImage1D(GLuint texture, GLenum
    target, GLenum bindingTarget, GLint level, GLenum internalFormat, GLsizei
    width, GLint border, GLenum format, GLenum type, const GLvoid *pixels)':
    names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::glTextureSubImage3D(GLuint texture,
    GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLint
    yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth,
    GLenum format, GLenum type, const GLvoid *pixels, const
    QOpenGLPixelTransferOptions *const options)': names 'GLvoid', which has
    no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::glTextureSubImage2D(GLuint texture,
    GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLint
    yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const
    GLvoid *pixels, const QOpenGLPixelTransferOptions *const options)': names
    'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::glTextureSubImage1D(GLuint texture,
    GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLsizei
    width, GLenum format, GLenum type, const GLvoid *pixels, const
    QOpenGLPixelTransferOptions *const options)': names 'GLvoid', which has
    no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::glCompressedTextureSubImage1D(GLuint
    texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset,
    GLsizei width, GLenum format, GLsizei imageSize, const GLvoid *bits,
    const QOpenGLPixelTransferOptions *const options)': names 'GLvoid', which
    has no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::glCompressedTextureSubImage2D(GLuint
    texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset,
    GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei
    imageSize, const GLvoid *bits, const QOpenGLPixelTransferOptions *const
    options)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::glCompressedTextureSubImage3D(GLuint
    texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset,
    GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei
    depth, GLenum format, GLsizei imageSize, const GLvoid *bits, const
    QOpenGLPixelTransferOptions *const options)': names 'GLvoid', which has
    no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::glCompressedTextureImage1D(GLuint
    texture, GLenum target, GLenum bindingTarget, GLint level, GLenum
    internalFormat, GLsizei width, GLint border, GLsizei imageSize, const
    GLvoid *bits, const QOpenGLPixelTransferOptions *const options)': names
    'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::glCompressedTextureImage2D(GLuint
    texture, GLenum target, GLenum bindingTarget, GLint level, GLenum
    internalFormat, GLsizei width, GLsizei height, GLint border, GLsizei
    imageSize, const GLvoid *bits, const QOpenGLPixelTransferOptions *const
    options)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::glCompressedTextureImage3D(GLuint
    texture, GLenum target, GLenum bindingTarget, GLint level, GLenum
    internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLint
    border, GLsizei imageSize, const GLvoid *bits, const
    QOpenGLPixelTransferOptions *const options)': names 'GLvoid', which has
    no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::dsa_TextureParameteriv(GLuint texture,
    GLenum target, GLenum bindingTarget, GLenum pname, const GLint *params)':
    names 'GLint', which has no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::dsa_TextureParameterfv(GLuint texture,
    GLenum target, GLenum bindingTarget, GLenum pname, const GLfloat
    *params)': names 'GLfloat', which has no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::dsa_TextureImage3D(GLuint texture,
    GLenum target, GLenum bindingTarget, GLint level, GLenum internalFormat,
    GLsizei width, GLsizei height, GLsizei depth, GLint border, GLenum
    format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which has no
    cute class yet.
  - Qt's 'void QOpenGLTextureHelper::dsa_TextureImage2D(GLuint texture,
    GLenum target, GLenum bindingTarget, GLint level, GLenum internalFormat,
    GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type,
    const GLvoid *pixels)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::dsa_TextureImage1D(GLuint texture,
    GLenum target, GLenum bindingTarget, GLint level, GLenum internalFormat,
    GLsizei width, GLint border, GLenum format, GLenum type, const GLvoid
    *pixels)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::dsa_TextureSubImage3D(GLuint texture,
    GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLint
    yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth,
    GLenum format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which
    has no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::dsa_TextureSubImage2D(GLuint texture,
    GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLint
    yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const
    GLvoid *pixels)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::dsa_TextureSubImage1D(GLuint texture,
    GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLsizei
    width, GLenum format, GLenum type, const GLvoid *pixels)': names
    'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::dsa_CompressedTextureSubImage1D(GLuint
    texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset,
    GLsizei width, GLenum format, GLsizei imageSize, const GLvoid *bits)':
    names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::dsa_CompressedTextureSubImage2D(GLuint
    texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset,
    GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei
    imageSize, const GLvoid *bits)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void QOpenGLTextureHelper::dsa_CompressedTextureSubImage3D(GLuint
    texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset,
    GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei
    depth, GLenum format, GLsizei imageSize, const GLvoid *bits)': names
    'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::dsa_CompressedTextureImage1D(GLuint
    texture, GLenum target, GLenum bindingTarget, GLint level, GLenum
    internalFormat, GLsizei width, GLint border, GLsizei imageSize, const
    GLvoid *bits)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::dsa_CompressedTextureImage2D(GLuint
    texture, GLenum target, GLenum bindingTarget, GLint level, GLenum
    internalFormat, GLsizei width, GLsizei height, GLint border, GLsizei
    imageSize, const GLvoid *bits)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void QOpenGLTextureHelper::dsa_CompressedTextureImage3D(GLuint
    texture, GLenum target, GLenum bindingTarget, GLint level, GLenum
    internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLint
    border, GLsizei imageSize, const GLvoid *bits)': names 'GLvoid', which
    has no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::qt_TextureParameteri(GLuint texture,
    GLenum target, GLenum bindingTarget, GLenum pname, GLint param)': one of
    Qt's own inner workings.
  - Qt's 'void QOpenGLTextureHelper::glTexImage1D(GLenum target, GLint level,
    GLint internalFormat, GLsizei width, GLint border, GLenum format, GLenum
    type, const GLvoid *pixels)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void QOpenGLTextureHelper::glTexSubImage1D(GLenum target, GLint
    level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const
    GLvoid *pixels)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::glTexImage3D(GLenum target, GLint level,
    GLint internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLint
    border, GLenum format, GLenum type, const GLvoid *pixels)': names
    'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::glTexSubImage3D(GLenum target, GLint
    level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth, GLenum format, GLenum type, const GLvoid
    *pixels)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::glGetCompressedTexImage(GLenum target,
    GLint level, GLvoid *img)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::glCompressedTexSubImage1D(GLenum target,
    GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei
    imageSize, const GLvoid *data)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void QOpenGLTextureHelper::glCompressedTexSubImage2D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
    GLenum format, GLsizei imageSize, const GLvoid *data)': names 'GLvoid',
    which has no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::glCompressedTexSubImage3D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const
    GLvoid *data)': names 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::glCompressedTexImage1D(GLenum target,
    GLint level, GLenum internalFormat, GLsizei width, GLint border, GLsizei
    imageSize, const GLvoid *data)': names 'GLvoid', which has no cute class
    yet.
  - Qt's 'void QOpenGLTextureHelper::glCompressedTexImage2D(GLenum target,
    GLint level, GLenum internalFormat, GLsizei width, GLsizei height, GLint
    border, GLsizei imageSize, const GLvoid *data)': names 'GLvoid', which
    has no cute class yet.
  - Qt's 'void QOpenGLTextureHelper::glCompressedTexImage3D(GLenum target,
    GLint level, GLenum internalFormat, GLsizei width, GLsizei height,
    GLsizei depth, GLint border, GLsizei imageSize, const GLvoid *data)':
    names 'GLvoid', which has no cute class yet.
  - Qt's 'QOpenGLTextureHelper::~QOpenGLTextureHelper()': the destructor:
    Python removes its C++ QOpenGLTextureHelper by it, and has no other use
    for it.

  What has no ritual
  ------------------

  23 of the 98 functions Qt declares: 23 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QOpenGLTextureHelper is created at the first use, not by
    'QOpenGLTextureHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGLTextureHelper back gives a copy the ritual
    made for Python, in a new cute QOpenGLTextureHelper.
  - Each name of Qt's QOpenGLTextureHelper that has no cute function yet,
    'dsa_CompressedTextureImage1D', 'dsa_CompressedTextureImage2D',
    'dsa_CompressedTextureImage3D', 'dsa_CompressedTextureSubImage1D',
    'dsa_CompressedTextureSubImage2D', 'dsa_CompressedTextureSubImage3D',
    'dsa_TextureImage1D', 'dsa_TextureImage2D', 'dsa_TextureImage3D',
    'dsa_TextureParameterfv', 'dsa_TextureParameteriv',
    'dsa_TextureSubImage1D', 'dsa_TextureSubImage2D',
    'dsa_TextureSubImage3D', 'glCompressedTexImage1D',
    'glCompressedTexImage2D', 'glCompressedTexImage3D',
    'glCompressedTexSubImage1D', 'glCompressedTexSubImage2D',
    'glCompressedTexSubImage3D', 'glCompressedTextureImage1D',
    'glCompressedTextureImage2D', 'glCompressedTextureImage3D',
    'glCompressedTextureSubImage1D', 'glCompressedTextureSubImage2D',
    'glCompressedTextureSubImage3D', 'glGetCompressedTexImage',
    'glTexImage1D', 'glTexImage3D', 'glTexSubImage1D', 'glTexSubImage3D',
    'glTextureImage1D', 'glTextureImage2D', 'glTextureImage3D',
    'glTextureParameterfv', 'glTextureParameteriv', 'glTextureSubImage1D',
    'glTextureSubImage2D', 'glTextureSubImage3D', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLTextureHelper'

  #  Qt's '~QOpenGLTextureHelper()'. Naming it makes this a value class:
  #  Python owns every C++ QOpenGLTextureHelper behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QOpenGLTextureHelperD1Ev'

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

  @overload(QOpenGLPixelTransferOptions)
  def setPixelUploadOptions(
      self,
      options: QOpenGLPixelTransferOptions,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTextureHelper::setPixelUploadOptions(const
    QOpenGLPixelTransferOptions &options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html#setPixelUploadOptions

    Parameters
    ----------

    options : QOpenGLPixelTransferOptions
      Passed on as a value: Qt reads the C++ QOpenGLPixelTransferOptions,
      which stays Python's own.
    """
    #  void QOpenGLTextureHelper::setPixelUploadOptions(const
    #      QOpenGLPixelTransferOptions &options)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper21setPixelUploadOptionsERK27QOpenGL'
        'PixelTransferOptions',
        self._valueOf(options),
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
    'QOpenGLTextureHelper::QOpenGLTextureHelper(QOpenGLContext *context)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html#QOpenGLTextureHelper

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOpenGLTextureHelper::QOpenGLTextureHelper(QOpenGLContext *context)
    self._noteCreation(QOpenGLTextureHelper, lambda: Rituals.call(
        'ritual_ZN20QOpenGLTextureHelperC1EP14QOpenGLContext',
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

  @overload(int, int, int, int, int)
  def glTextureParameteri(
      self,
      texture: int,
      target: int,
      bindingTarget: int,
      pname: int,
      param: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTextureHelper::glTextureParameteri(GLuint
    texture, GLenum target, GLenum bindingTarget, GLenum pname, GLint
    param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html#glTextureParameteri

    Parameters
    ----------

    texture : int
      Passed on as it is.

    target : int
      Passed on as it is.

    bindingTarget : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::glTextureParameteri(GLuint texture, GLenum
    #      target, GLenum bindingTarget, GLenum pname, GLint param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper19glTextureParameteriEjjjji',
        texture, target, bindingTarget, pname, param,
    )

  @overload(int, int, int, int, float)
  def glTextureParameterf(
      self,
      texture: int,
      target: int,
      bindingTarget: int,
      pname: int,
      param: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTextureHelper::glTextureParameterf(GLuint
    texture, GLenum target, GLenum bindingTarget, GLenum pname, GLfloat
    param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html#glTextureParameterf

    Parameters
    ----------

    texture : int
      Passed on as it is.

    target : int
      Passed on as it is.

    bindingTarget : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::glTextureParameterf(GLuint texture, GLenum
    #      target, GLenum bindingTarget, GLenum pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper19glTextureParameterfEjjjjf',
        texture, target, bindingTarget, pname, param,
    )

  @overload(int, int, int)
  def glGenerateTextureMipmap(
      self,
      texture: int,
      target: int,
      bindingTarget: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTextureHelper::glGenerateTextureMipmap(GLuint
    texture, GLenum target, GLenum bindingTarget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html#glGenerateTextureMipmap

    Parameters
    ----------

    texture : int
      Passed on as it is.

    target : int
      Passed on as it is.

    bindingTarget : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::glGenerateTextureMipmap(GLuint texture,
    #      GLenum target, GLenum bindingTarget)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper23glGenerateTextureMipmapEjjj',
        texture, target, bindingTarget,
    )

  @overload(int, int, int, int, int, int, int, int)
  def glTextureStorage3D(
      self,
      texture: int,
      target: int,
      bindingTarget: int,
      levels: int,
      internalFormat: int,
      width: int,
      height: int,
      depth: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTextureHelper::glTextureStorage3D(GLuint texture,
    GLenum target, GLenum bindingTarget, GLsizei levels, GLenum
    internalFormat, GLsizei width, GLsizei height, GLsizei depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html#glTextureStorage3D

    Parameters
    ----------

    texture : int
      Passed on as it is.

    target : int
      Passed on as it is.

    bindingTarget : int
      Passed on as it is.

    levels : int
      Passed on as it is.

    internalFormat : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    depth : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::glTextureStorage3D(GLuint texture, GLenum
    #      target, GLenum bindingTarget, GLsizei levels, GLenum
    #      internalFormat, GLsizei width, GLsizei height, GLsizei depth)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper18glTextureStorage3DEjjjijiii',
        texture, target, bindingTarget, levels, internalFormat, width,
        height, depth,
    )

  @overload(int, int, int, int, int, int, int)
  def glTextureStorage2D(
      self,
      texture: int,
      target: int,
      bindingTarget: int,
      levels: int,
      internalFormat: int,
      width: int,
      height: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTextureHelper::glTextureStorage2D(GLuint texture,
    GLenum target, GLenum bindingTarget, GLsizei levels, GLenum
    internalFormat, GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html#glTextureStorage2D

    Parameters
    ----------

    texture : int
      Passed on as it is.

    target : int
      Passed on as it is.

    bindingTarget : int
      Passed on as it is.

    levels : int
      Passed on as it is.

    internalFormat : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::glTextureStorage2D(GLuint texture, GLenum
    #      target, GLenum bindingTarget, GLsizei levels, GLenum
    #      internalFormat, GLsizei width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper18glTextureStorage2DEjjjijii',
        texture, target, bindingTarget, levels, internalFormat, width,
        height,
    )

  @overload(int, int, int, int, int, int)
  def glTextureStorage1D(
      self,
      texture: int,
      target: int,
      bindingTarget: int,
      levels: int,
      internalFormat: int,
      width: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTextureHelper::glTextureStorage1D(GLuint texture,
    GLenum target, GLenum bindingTarget, GLsizei levels, GLenum
    internalFormat, GLsizei width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html#glTextureStorage1D

    Parameters
    ----------

    texture : int
      Passed on as it is.

    target : int
      Passed on as it is.

    bindingTarget : int
      Passed on as it is.

    levels : int
      Passed on as it is.

    internalFormat : int
      Passed on as it is.

    width : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::glTextureStorage1D(GLuint texture, GLenum
    #      target, GLenum bindingTarget, GLsizei levels, GLenum
    #      internalFormat, GLsizei width)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper18glTextureStorage1DEjjjiji',
        texture, target, bindingTarget, levels, internalFormat, width,
    )

  @overload(int, int, int, int, int, int, int, int, int)
  def glTextureStorage3DMultisample(
      self,
      texture: int,
      target: int,
      bindingTarget: int,
      samples: int,
      internalFormat: int,
      width: int,
      height: int,
      depth: int,
      fixedSampleLocations: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLTextureHelper::glTextureStorage3DMultisample(GLuint texture,
    GLenum target, GLenum bindingTarget, GLsizei samples, GLenum
    internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLboolean
    fixedSampleLocations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html

    Parameters
    ----------

    texture : int
      Passed on as it is.

    target : int
      Passed on as it is.

    bindingTarget : int
      Passed on as it is.

    samples : int
      Passed on as it is.

    internalFormat : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    depth : int
      Passed on as it is.

    fixedSampleLocations : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::glTextureStorage3DMultisample(GLuint
    #      texture, GLenum target, GLenum bindingTarget, GLsizei samples,
    #      GLenum internalFormat, GLsizei width, GLsizei height, GLsizei
    #      depth, GLboolean fixedSampleLocations)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper29glTextureStorage3DMultisampleEjjj'
        'ijiiih',
        texture, target, bindingTarget, samples, internalFormat, width,
        height, depth, fixedSampleLocations,
    )

  @overload(int, int, int, int, int, int, int, int)
  def glTextureStorage2DMultisample(
      self,
      texture: int,
      target: int,
      bindingTarget: int,
      samples: int,
      internalFormat: int,
      width: int,
      height: int,
      fixedSampleLocations: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLTextureHelper::glTextureStorage2DMultisample(GLuint texture,
    GLenum target, GLenum bindingTarget, GLsizei samples, GLenum
    internalFormat, GLsizei width, GLsizei height, GLboolean
    fixedSampleLocations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html

    Parameters
    ----------

    texture : int
      Passed on as it is.

    target : int
      Passed on as it is.

    bindingTarget : int
      Passed on as it is.

    samples : int
      Passed on as it is.

    internalFormat : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    fixedSampleLocations : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::glTextureStorage2DMultisample(GLuint
    #      texture, GLenum target, GLenum bindingTarget, GLsizei samples,
    #      GLenum internalFormat, GLsizei width, GLsizei height, GLboolean
    #      fixedSampleLocations)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper29glTextureStorage2DMultisampleEjjj'
        'ijiih',
        texture, target, bindingTarget, samples, internalFormat, width,
        height, fixedSampleLocations,
    )

  @overload(int, int, int, int, int, int, int, int, int)
  def glTextureImage3DMultisample(
      self,
      texture: int,
      target: int,
      bindingTarget: int,
      samples: int,
      internalFormat: int,
      width: int,
      height: int,
      depth: int,
      fixedSampleLocations: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTextureHelper::glTextureImage3DMultisample(GLuint
    texture, GLenum target, GLenum bindingTarget, GLsizei samples, GLint
    internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLboolean
    fixedSampleLocations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html

    Parameters
    ----------

    texture : int
      Passed on as it is.

    target : int
      Passed on as it is.

    bindingTarget : int
      Passed on as it is.

    samples : int
      Passed on as it is.

    internalFormat : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    depth : int
      Passed on as it is.

    fixedSampleLocations : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::glTextureImage3DMultisample(GLuint texture,
    #      GLenum target, GLenum bindingTarget, GLsizei samples, GLint
    #      internalFormat, GLsizei width, GLsizei height, GLsizei depth,
    #      GLboolean fixedSampleLocations)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper27glTextureImage3DMultisampleEjjjii'
        'iiih',
        texture, target, bindingTarget, samples, internalFormat, width,
        height, depth, fixedSampleLocations,
    )

  @overload(int, int, int, int, int, int, int, int)
  def glTextureImage2DMultisample(
      self,
      texture: int,
      target: int,
      bindingTarget: int,
      samples: int,
      internalFormat: int,
      width: int,
      height: int,
      fixedSampleLocations: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTextureHelper::glTextureImage2DMultisample(GLuint
    texture, GLenum target, GLenum bindingTarget, GLsizei samples, GLint
    internalFormat, GLsizei width, GLsizei height, GLboolean
    fixedSampleLocations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html

    Parameters
    ----------

    texture : int
      Passed on as it is.

    target : int
      Passed on as it is.

    bindingTarget : int
      Passed on as it is.

    samples : int
      Passed on as it is.

    internalFormat : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    fixedSampleLocations : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::glTextureImage2DMultisample(GLuint texture,
    #      GLenum target, GLenum bindingTarget, GLsizei samples, GLint
    #      internalFormat, GLsizei width, GLsizei height, GLboolean
    #      fixedSampleLocations)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper27glTextureImage2DMultisampleEjjjii'
        'iih',
        texture, target, bindingTarget, samples, internalFormat, width,
        height, fixedSampleLocations,
    )

  @overload(int, int, int, int, int)
  def dsa_TextureParameteri(
      self,
      texture: int,
      target: int,
      bindingTarget: int,
      pname: int,
      param: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTextureHelper::dsa_TextureParameteri(GLuint
    texture, GLenum target, GLenum bindingTarget, GLenum pname, GLint
    param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html#dsa_TextureParameteri

    Parameters
    ----------

    texture : int
      Passed on as it is.

    target : int
      Passed on as it is.

    bindingTarget : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::dsa_TextureParameteri(GLuint texture,
    #      GLenum target, GLenum bindingTarget, GLenum pname, GLint param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper21dsa_TextureParameteriEjjjji',
        texture, target, bindingTarget, pname, param,
    )

  @overload(int, int, int, int, float)
  def dsa_TextureParameterf(
      self,
      texture: int,
      target: int,
      bindingTarget: int,
      pname: int,
      param: float,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTextureHelper::dsa_TextureParameterf(GLuint
    texture, GLenum target, GLenum bindingTarget, GLenum pname, GLfloat
    param)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html#dsa_TextureParameterf

    Parameters
    ----------

    texture : int
      Passed on as it is.

    target : int
      Passed on as it is.

    bindingTarget : int
      Passed on as it is.

    pname : int
      Passed on as it is.

    param : float
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::dsa_TextureParameterf(GLuint texture,
    #      GLenum target, GLenum bindingTarget, GLenum pname, GLfloat param)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper21dsa_TextureParameterfEjjjjf',
        texture, target, bindingTarget, pname, param,
    )

  @overload(int, int, int)
  def dsa_GenerateTextureMipmap(
      self,
      texture: int,
      target: int,
      bindingTarget: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTextureHelper::dsa_GenerateTextureMipmap(GLuint
    texture, GLenum target, GLenum bindingTarget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html

    Parameters
    ----------

    texture : int
      Passed on as it is.

    target : int
      Passed on as it is.

    bindingTarget : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::dsa_GenerateTextureMipmap(GLuint texture,
    #      GLenum target, GLenum bindingTarget)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper25dsa_GenerateTextureMipmapEjjj',
        texture, target, bindingTarget,
    )

  @overload(int, int, int, int, int, int, int, int)
  def dsa_TextureStorage3D(
      self,
      texture: int,
      target: int,
      bindingTarget: int,
      levels: int,
      internalFormat: int,
      width: int,
      height: int,
      depth: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTextureHelper::dsa_TextureStorage3D(GLuint
    texture, GLenum target, GLenum bindingTarget, GLsizei levels, GLenum
    internalFormat, GLsizei width, GLsizei height, GLsizei depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html#dsa_TextureStorage3D

    Parameters
    ----------

    texture : int
      Passed on as it is.

    target : int
      Passed on as it is.

    bindingTarget : int
      Passed on as it is.

    levels : int
      Passed on as it is.

    internalFormat : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    depth : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::dsa_TextureStorage3D(GLuint texture, GLenum
    #      target, GLenum bindingTarget, GLsizei levels, GLenum
    #      internalFormat, GLsizei width, GLsizei height, GLsizei depth)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper20dsa_TextureStorage3DEjjjijiii',
        texture, target, bindingTarget, levels, internalFormat, width,
        height, depth,
    )

  @overload(int, int, int, int, int, int, int)
  def dsa_TextureStorage2D(
      self,
      texture: int,
      target: int,
      bindingTarget: int,
      levels: int,
      internalFormat: int,
      width: int,
      height: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTextureHelper::dsa_TextureStorage2D(GLuint
    texture, GLenum target, GLenum bindingTarget, GLsizei levels, GLenum
    internalFormat, GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html#dsa_TextureStorage2D

    Parameters
    ----------

    texture : int
      Passed on as it is.

    target : int
      Passed on as it is.

    bindingTarget : int
      Passed on as it is.

    levels : int
      Passed on as it is.

    internalFormat : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::dsa_TextureStorage2D(GLuint texture, GLenum
    #      target, GLenum bindingTarget, GLsizei levels, GLenum
    #      internalFormat, GLsizei width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper20dsa_TextureStorage2DEjjjijii',
        texture, target, bindingTarget, levels, internalFormat, width,
        height,
    )

  @overload(int, int, int, int, int, int)
  def dsa_TextureStorage1D(
      self,
      texture: int,
      target: int,
      bindingTarget: int,
      levels: int,
      internalFormat: int,
      width: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTextureHelper::dsa_TextureStorage1D(GLuint
    texture, GLenum target, GLenum bindingTarget, GLsizei levels, GLenum
    internalFormat, GLsizei width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html#dsa_TextureStorage1D

    Parameters
    ----------

    texture : int
      Passed on as it is.

    target : int
      Passed on as it is.

    bindingTarget : int
      Passed on as it is.

    levels : int
      Passed on as it is.

    internalFormat : int
      Passed on as it is.

    width : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::dsa_TextureStorage1D(GLuint texture, GLenum
    #      target, GLenum bindingTarget, GLsizei levels, GLenum
    #      internalFormat, GLsizei width)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper20dsa_TextureStorage1DEjjjiji',
        texture, target, bindingTarget, levels, internalFormat, width,
    )

  @overload(int, int, int, int, int, int, int, int, int)
  def dsa_TextureStorage3DMultisample(
      self,
      texture: int,
      target: int,
      bindingTarget: int,
      samples: int,
      internalFormat: int,
      width: int,
      height: int,
      depth: int,
      fixedSampleLocations: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLTextureHelper::dsa_TextureStorage3DMultisample(GLuint texture,
    GLenum target, GLenum bindingTarget, GLsizei samples, GLenum
    internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLboolean
    fixedSampleLocations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html

    Parameters
    ----------

    texture : int
      Passed on as it is.

    target : int
      Passed on as it is.

    bindingTarget : int
      Passed on as it is.

    samples : int
      Passed on as it is.

    internalFormat : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    depth : int
      Passed on as it is.

    fixedSampleLocations : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::dsa_TextureStorage3DMultisample(GLuint
    #      texture, GLenum target, GLenum bindingTarget, GLsizei samples,
    #      GLenum internalFormat, GLsizei width, GLsizei height, GLsizei
    #      depth, GLboolean fixedSampleLocations)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper31dsa_TextureStorage3DMultisampleEj'
        'jjijiiih',
        texture, target, bindingTarget, samples, internalFormat, width,
        height, depth, fixedSampleLocations,
    )

  @overload(int, int, int, int, int, int, int, int)
  def dsa_TextureStorage2DMultisample(
      self,
      texture: int,
      target: int,
      bindingTarget: int,
      samples: int,
      internalFormat: int,
      width: int,
      height: int,
      fixedSampleLocations: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLTextureHelper::dsa_TextureStorage2DMultisample(GLuint texture,
    GLenum target, GLenum bindingTarget, GLsizei samples, GLenum
    internalFormat, GLsizei width, GLsizei height, GLboolean
    fixedSampleLocations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html

    Parameters
    ----------

    texture : int
      Passed on as it is.

    target : int
      Passed on as it is.

    bindingTarget : int
      Passed on as it is.

    samples : int
      Passed on as it is.

    internalFormat : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    fixedSampleLocations : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::dsa_TextureStorage2DMultisample(GLuint
    #      texture, GLenum target, GLenum bindingTarget, GLsizei samples,
    #      GLenum internalFormat, GLsizei width, GLsizei height, GLboolean
    #      fixedSampleLocations)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper31dsa_TextureStorage2DMultisampleEj'
        'jjijiih',
        texture, target, bindingTarget, samples, internalFormat, width,
        height, fixedSampleLocations,
    )

  @overload(int, int, int, int, int, int, int, int, int)
  def dsa_TextureImage3DMultisample(
      self,
      texture: int,
      target: int,
      bindingTarget: int,
      samples: int,
      internalFormat: int,
      width: int,
      height: int,
      depth: int,
      fixedSampleLocations: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLTextureHelper::dsa_TextureImage3DMultisample(GLuint texture,
    GLenum target, GLenum bindingTarget, GLsizei samples, GLint
    internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLboolean
    fixedSampleLocations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html

    Parameters
    ----------

    texture : int
      Passed on as it is.

    target : int
      Passed on as it is.

    bindingTarget : int
      Passed on as it is.

    samples : int
      Passed on as it is.

    internalFormat : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    depth : int
      Passed on as it is.

    fixedSampleLocations : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::dsa_TextureImage3DMultisample(GLuint
    #      texture, GLenum target, GLenum bindingTarget, GLsizei samples,
    #      GLint internalFormat, GLsizei width, GLsizei height, GLsizei
    #      depth, GLboolean fixedSampleLocations)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper29dsa_TextureImage3DMultisampleEjjj'
        'iiiiih',
        texture, target, bindingTarget, samples, internalFormat, width,
        height, depth, fixedSampleLocations,
    )

  @overload(int, int, int, int, int, int, int, int)
  def dsa_TextureImage2DMultisample(
      self,
      texture: int,
      target: int,
      bindingTarget: int,
      samples: int,
      internalFormat: int,
      width: int,
      height: int,
      fixedSampleLocations: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLTextureHelper::dsa_TextureImage2DMultisample(GLuint texture,
    GLenum target, GLenum bindingTarget, GLsizei samples, GLint
    internalFormat, GLsizei width, GLsizei height, GLboolean
    fixedSampleLocations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html

    Parameters
    ----------

    texture : int
      Passed on as it is.

    target : int
      Passed on as it is.

    bindingTarget : int
      Passed on as it is.

    samples : int
      Passed on as it is.

    internalFormat : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    fixedSampleLocations : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::dsa_TextureImage2DMultisample(GLuint
    #      texture, GLenum target, GLenum bindingTarget, GLsizei samples,
    #      GLint internalFormat, GLsizei width, GLsizei height, GLboolean
    #      fixedSampleLocations)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper29dsa_TextureImage2DMultisampleEjjj'
        'iiiih',
        texture, target, bindingTarget, samples, internalFormat, width,
        height, fixedSampleLocations,
    )

  @overload(int)
  def glActiveTexture(self, texture: int) -> None:
    """
    Calls Qt's 'void QOpenGLTextureHelper::glActiveTexture(GLenum texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html#glActiveTexture

    Parameters
    ----------

    texture : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::glActiveTexture(GLenum texture)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper15glActiveTextureEj', texture,
    )

  @overload(int)
  def glGenerateMipmap(self, target: int) -> None:
    """
    Calls Qt's 'void QOpenGLTextureHelper::glGenerateMipmap(GLenum target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html#glGenerateMipmap

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::glGenerateMipmap(GLenum target)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper16glGenerateMipmapEj', target,
    )

  @overload(int, int, int, int, int, int, int)
  def glTexImage3DMultisample(
      self,
      target: int,
      samples: int,
      internalFormat: int,
      width: int,
      height: int,
      depth: int,
      fixedSampleLocations: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTextureHelper::glTexImage3DMultisample(GLenum
    target, GLsizei samples, GLint internalFormat, GLsizei width, GLsizei
    height, GLsizei depth, GLboolean fixedSampleLocations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html#glTexImage3DMultisample

    Parameters
    ----------

    target : int
      Passed on as it is.

    samples : int
      Passed on as it is.

    internalFormat : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    depth : int
      Passed on as it is.

    fixedSampleLocations : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::glTexImage3DMultisample(GLenum target,
    #      GLsizei samples, GLint internalFormat, GLsizei width, GLsizei
    #      height, GLsizei depth, GLboolean fixedSampleLocations)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper23glTexImage3DMultisampleEjiiiiih',
        target, samples, internalFormat, width, height, depth,
        fixedSampleLocations,
    )

  @overload(int, int, int, int, int, int)
  def glTexImage2DMultisample(
      self,
      target: int,
      samples: int,
      internalFormat: int,
      width: int,
      height: int,
      fixedSampleLocations: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTextureHelper::glTexImage2DMultisample(GLenum
    target, GLsizei samples, GLint internalFormat, GLsizei width, GLsizei
    height, GLboolean fixedSampleLocations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html#glTexImage2DMultisample

    Parameters
    ----------

    target : int
      Passed on as it is.

    samples : int
      Passed on as it is.

    internalFormat : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    fixedSampleLocations : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::glTexImage2DMultisample(GLenum target,
    #      GLsizei samples, GLint internalFormat, GLsizei width, GLsizei
    #      height, GLboolean fixedSampleLocations)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper23glTexImage2DMultisampleEjiiiih',
        target, samples, internalFormat, width, height, fixedSampleLocations,
    )

  @overload(int, int, int, int, int, int)
  def glTexStorage3D(
      self,
      target: int,
      levels: int,
      internalFormat: int,
      width: int,
      height: int,
      depth: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTextureHelper::glTexStorage3D(GLenum target,
    GLsizei levels, GLenum internalFormat, GLsizei width, GLsizei height,
    GLsizei depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html#glTexStorage3D

    Parameters
    ----------

    target : int
      Passed on as it is.

    levels : int
      Passed on as it is.

    internalFormat : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    depth : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::glTexStorage3D(GLenum target, GLsizei
    #      levels, GLenum internalFormat, GLsizei width, GLsizei height,
    #      GLsizei depth)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper14glTexStorage3DEjijiii',
        target, levels, internalFormat, width, height, depth,
    )

  @overload(int, int, int, int, int)
  def glTexStorage2D(
      self,
      target: int,
      levels: int,
      internalFormat: int,
      width: int,
      height: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTextureHelper::glTexStorage2D(GLenum target,
    GLsizei levels, GLenum internalFormat, GLsizei width, GLsizei height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html#glTexStorage2D

    Parameters
    ----------

    target : int
      Passed on as it is.

    levels : int
      Passed on as it is.

    internalFormat : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::glTexStorage2D(GLenum target, GLsizei
    #      levels, GLenum internalFormat, GLsizei width, GLsizei height)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper14glTexStorage2DEjijii',
        target, levels, internalFormat, width, height,
    )

  @overload(int, int, int, int)
  def glTexStorage1D(
      self,
      target: int,
      levels: int,
      internalFormat: int,
      width: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTextureHelper::glTexStorage1D(GLenum target,
    GLsizei levels, GLenum internalFormat, GLsizei width)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html#glTexStorage1D

    Parameters
    ----------

    target : int
      Passed on as it is.

    levels : int
      Passed on as it is.

    internalFormat : int
      Passed on as it is.

    width : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::glTexStorage1D(GLenum target, GLsizei
    #      levels, GLenum internalFormat, GLsizei width)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper14glTexStorage1DEjiji',
        target, levels, internalFormat, width,
    )

  @overload(int, int, int, int, int, int, int)
  def glTexStorage3DMultisample(
      self,
      target: int,
      samples: int,
      internalFormat: int,
      width: int,
      height: int,
      depth: int,
      fixedSampleLocations: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTextureHelper::glTexStorage3DMultisample(GLenum
    target, GLsizei samples, GLenum internalFormat, GLsizei width, GLsizei
    height, GLsizei depth, GLboolean fixedSampleLocations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    samples : int
      Passed on as it is.

    internalFormat : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    depth : int
      Passed on as it is.

    fixedSampleLocations : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::glTexStorage3DMultisample(GLenum target,
    #      GLsizei samples, GLenum internalFormat, GLsizei width, GLsizei
    #      height, GLsizei depth, GLboolean fixedSampleLocations)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper25glTexStorage3DMultisampleEjijiiih',
        target, samples, internalFormat, width, height, depth,
        fixedSampleLocations,
    )

  @overload(int, int, int, int, int, int)
  def glTexStorage2DMultisample(
      self,
      target: int,
      samples: int,
      internalFormat: int,
      width: int,
      height: int,
      fixedSampleLocations: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTextureHelper::glTexStorage2DMultisample(GLenum
    target, GLsizei samples, GLenum internalFormat, GLsizei width, GLsizei
    height, GLboolean fixedSampleLocations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html

    Parameters
    ----------

    target : int
      Passed on as it is.

    samples : int
      Passed on as it is.

    internalFormat : int
      Passed on as it is.

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    fixedSampleLocations : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::glTexStorage2DMultisample(GLenum target,
    #      GLsizei samples, GLenum internalFormat, GLsizei width, GLsizei
    #      height, GLboolean fixedSampleLocations)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper25glTexStorage2DMultisampleEjijiih',
        target, samples, internalFormat, width, height, fixedSampleLocations,
    )

  @overload(int, int, int, int, int)
  def glTexBufferRange(
      self,
      target: int,
      internalFormat: int,
      buffer: int,
      offset: int,
      size: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTextureHelper::glTexBufferRange(GLenum target,
    GLenum internalFormat, GLuint buffer, GLintptr offset, GLsizeiptr size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html#glTexBufferRange

    Parameters
    ----------

    target : int
      Passed on as it is.

    internalFormat : int
      Passed on as it is.

    buffer : int
      Passed on as it is.

    offset : int
      Passed on as it is.

    size : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::glTexBufferRange(GLenum target, GLenum
    #      internalFormat, GLuint buffer, GLintptr offset, GLsizeiptr size)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper16glTexBufferRangeEjjjll',
        target, internalFormat, buffer, offset, size,
    )

  @overload(int, int, int, int, int, int, int, int)
  def glTextureView(
      self,
      texture: int,
      target: int,
      origTexture: int,
      internalFormat: int,
      minLevel: int,
      numLevels: int,
      minLayer: int,
      numLayers: int,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLTextureHelper::glTextureView(GLuint texture,
    GLenum target, GLuint origTexture, GLenum internalFormat, GLuint
    minLevel, GLuint numLevels, GLuint minLayer, GLuint numLayers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html#glTextureView

    Parameters
    ----------

    texture : int
      Passed on as it is.

    target : int
      Passed on as it is.

    origTexture : int
      Passed on as it is.

    internalFormat : int
      Passed on as it is.

    minLevel : int
      Passed on as it is.

    numLevels : int
      Passed on as it is.

    minLayer : int
      Passed on as it is.

    numLayers : int
      Passed on as it is.
    """
    #  void QOpenGLTextureHelper::glTextureView(GLuint texture, GLenum
    #      target, GLuint origTexture, GLenum internalFormat, GLuint
    #      minLevel, GLuint numLevels, GLuint minLayer, GLuint numLayers)
    self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper13glTextureViewEjjjjjjjj',
        texture, target, origTexture, internalFormat, minLevel, numLevels,
        minLayer, numLayers,
    )

  def savePixelUploadOptions(self) -> QOpenGLPixelTransferOptions:
    """
    Calls Qt's 'QOpenGLPixelTransferOptions
    QOpenGLTextureHelper::savePixelUploadOptions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopengltexturehelper.html#savePixelUploadOptions

    Returns
    -------

    QOpenGLPixelTransferOptions
      A new cute QOpenGLPixelTransferOptions around the copy Qt gave back.
      Python owns it.
    """
    #  QOpenGLPixelTransferOptions
    #      QOpenGLTextureHelper::savePixelUploadOptions()
    address = self.uglySide.call(
        'ritual_ZN20QOpenGLTextureHelper22savePixelUploadOptionsEv',
    )
    from . import QOpenGLPixelTransferOptions
    return QOpenGLPixelTransferOptions._cuteOwning(address)

  @staticmethod
  def dsa_CompressedTextureImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::dsa_CompressedTextureImage1D(GLuint
    texture, GLenum target, GLenum bindingTarget, GLint level, GLenum
    internalFormat, GLsizei width, GLint border, GLsizei imageSize, const
    GLvoid *bits)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.dsa_CompressedTextureImage1D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLTextureHelper::dsa_CompressedTextureImage1D(GLuint texture, "
        "GLenum target, GLenum bindingTarget, GLint level, GLenum "
        "internalFormat, GLsizei width, GLint border, GLsizei imageSize, "
        "const GLvoid *bits)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def dsa_CompressedTextureImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::dsa_CompressedTextureImage2D(GLuint
    texture, GLenum target, GLenum bindingTarget, GLint level, GLenum
    internalFormat, GLsizei width, GLsizei height, GLint border, GLsizei
    imageSize, const GLvoid *bits)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.dsa_CompressedTextureImage2D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLTextureHelper::dsa_CompressedTextureImage2D(GLuint texture, "
        "GLenum target, GLenum bindingTarget, GLint level, GLenum "
        "internalFormat, GLsizei width, GLsizei height, GLint border, "
        "GLsizei imageSize, const GLvoid *bits)': names 'GLvoid', which has "
        "no cute class yet.")

  @staticmethod
  def dsa_CompressedTextureImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::dsa_CompressedTextureImage3D(GLuint
    texture, GLenum target, GLenum bindingTarget, GLint level, GLenum
    internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLint
    border, GLsizei imageSize, const GLvoid *bits)': names 'GLvoid', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.dsa_CompressedTextureImage3D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLTextureHelper::dsa_CompressedTextureImage3D(GLuint texture, "
        "GLenum target, GLenum bindingTarget, GLint level, GLenum "
        "internalFormat, GLsizei width, GLsizei height, GLsizei depth, "
        "GLint border, GLsizei imageSize, const GLvoid *bits)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def dsa_CompressedTextureSubImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::dsa_CompressedTextureSubImage1D(GLuint
    texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset,
    GLsizei width, GLenum format, GLsizei imageSize, const GLvoid *bits)':
    names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.dsa_CompressedTextureSubImage1D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLTextureHelper::dsa_CompressedTextureSubImage1D(GLuint "
        "texture, GLenum target, GLenum bindingTarget, GLint level, GLint "
        "xoffset, GLsizei width, GLenum format, GLsizei imageSize, const "
        "GLvoid *bits)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def dsa_CompressedTextureSubImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::dsa_CompressedTextureSubImage2D(GLuint
    texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset,
    GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei
    imageSize, const GLvoid *bits)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.dsa_CompressedTextureSubImage2D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLTextureHelper::dsa_CompressedTextureSubImage2D(GLuint "
        "texture, GLenum target, GLenum bindingTarget, GLint level, GLint "
        "xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum "
        "format, GLsizei imageSize, const GLvoid *bits)': names 'GLvoid', "
        "which has no cute class yet.")

  @staticmethod
  def dsa_CompressedTextureSubImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::dsa_CompressedTextureSubImage3D(GLuint
    texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset,
    GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei
    depth, GLenum format, GLsizei imageSize, const GLvoid *bits)': names
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.dsa_CompressedTextureSubImage3D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLTextureHelper::dsa_CompressedTextureSubImage3D(GLuint "
        "texture, GLenum target, GLenum bindingTarget, GLint level, GLint "
        "xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei "
        "height, GLsizei depth, GLenum format, GLsizei imageSize, const "
        "GLvoid *bits)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def dsa_TextureImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::dsa_TextureImage1D(GLuint texture,
    GLenum target, GLenum bindingTarget, GLint level, GLenum internalFormat,
    GLsizei width, GLint border, GLenum format, GLenum type, const GLvoid
    *pixels)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.dsa_TextureImage1D' has no cute function "
        "yet. Qt's 'void QOpenGLTextureHelper::dsa_TextureImage1D(GLuint "
        "texture, GLenum target, GLenum bindingTarget, GLint level, GLenum "
        "internalFormat, GLsizei width, GLint border, GLenum format, GLenum "
        "type, const GLvoid *pixels)': names 'GLvoid', which has no cute "
        "class yet.")

  @staticmethod
  def dsa_TextureImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::dsa_TextureImage2D(GLuint texture,
    GLenum target, GLenum bindingTarget, GLint level, GLenum internalFormat,
    GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type,
    const GLvoid *pixels)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.dsa_TextureImage2D' has no cute function "
        "yet. Qt's 'void QOpenGLTextureHelper::dsa_TextureImage2D(GLuint "
        "texture, GLenum target, GLenum bindingTarget, GLint level, GLenum "
        "internalFormat, GLsizei width, GLsizei height, GLint border, "
        "GLenum format, GLenum type, const GLvoid *pixels)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def dsa_TextureImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::dsa_TextureImage3D(GLuint texture,
    GLenum target, GLenum bindingTarget, GLint level, GLenum internalFormat,
    GLsizei width, GLsizei height, GLsizei depth, GLint border, GLenum
    format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.dsa_TextureImage3D' has no cute function "
        "yet. Qt's 'void QOpenGLTextureHelper::dsa_TextureImage3D(GLuint "
        "texture, GLenum target, GLenum bindingTarget, GLint level, GLenum "
        "internalFormat, GLsizei width, GLsizei height, GLsizei depth, "
        "GLint border, GLenum format, GLenum type, const GLvoid *pixels)': "
        "names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def dsa_TextureParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::dsa_TextureParameterfv(GLuint texture,
    GLenum target, GLenum bindingTarget, GLenum pname, const GLfloat
    *params)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.dsa_TextureParameterfv' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLTextureHelper::dsa_TextureParameterfv(GLuint texture, "
        "GLenum target, GLenum bindingTarget, GLenum pname, const GLfloat "
        "*params)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def dsa_TextureParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::dsa_TextureParameteriv(GLuint texture,
    GLenum target, GLenum bindingTarget, GLenum pname, const GLint *params)':
    names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.dsa_TextureParameteriv' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLTextureHelper::dsa_TextureParameteriv(GLuint texture, "
        "GLenum target, GLenum bindingTarget, GLenum pname, const GLint "
        "*params)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def dsa_TextureSubImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::dsa_TextureSubImage1D(GLuint texture,
    GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLsizei
    width, GLenum format, GLenum type, const GLvoid *pixels)': names
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.dsa_TextureSubImage1D' has no cute function "
        "yet. Qt's 'void QOpenGLTextureHelper::dsa_TextureSubImage1D(GLuint "
        "texture, GLenum target, GLenum bindingTarget, GLint level, GLint "
        "xoffset, GLsizei width, GLenum format, GLenum type, const GLvoid "
        "*pixels)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def dsa_TextureSubImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::dsa_TextureSubImage2D(GLuint texture,
    GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLint
    yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const
    GLvoid *pixels)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.dsa_TextureSubImage2D' has no cute function "
        "yet. Qt's 'void QOpenGLTextureHelper::dsa_TextureSubImage2D(GLuint "
        "texture, GLenum target, GLenum bindingTarget, GLint level, GLint "
        "xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum "
        "format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which "
        "has no cute class yet.")

  @staticmethod
  def dsa_TextureSubImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::dsa_TextureSubImage3D(GLuint texture,
    GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLint
    yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth,
    GLenum format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.dsa_TextureSubImage3D' has no cute function "
        "yet. Qt's 'void QOpenGLTextureHelper::dsa_TextureSubImage3D(GLuint "
        "texture, GLenum target, GLenum bindingTarget, GLint level, GLint "
        "xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei "
        "height, GLsizei depth, GLenum format, GLenum type, const GLvoid "
        "*pixels)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glCompressedTexImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::glCompressedTexImage1D(GLenum target,
    GLint level, GLenum internalFormat, GLsizei width, GLint border, GLsizei
    imageSize, const GLvoid *data)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.glCompressedTexImage1D' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLTextureHelper::glCompressedTexImage1D(GLenum target, GLint "
        "level, GLenum internalFormat, GLsizei width, GLint border, GLsizei "
        "imageSize, const GLvoid *data)': names 'GLvoid', which has no cute "
        "class yet.")

  @staticmethod
  def glCompressedTexImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::glCompressedTexImage2D(GLenum target,
    GLint level, GLenum internalFormat, GLsizei width, GLsizei height, GLint
    border, GLsizei imageSize, const GLvoid *data)': names 'GLvoid', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.glCompressedTexImage2D' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLTextureHelper::glCompressedTexImage2D(GLenum target, GLint "
        "level, GLenum internalFormat, GLsizei width, GLsizei height, GLint "
        "border, GLsizei imageSize, const GLvoid *data)': names 'GLvoid', "
        "which has no cute class yet.")

  @staticmethod
  def glCompressedTexImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::glCompressedTexImage3D(GLenum target,
    GLint level, GLenum internalFormat, GLsizei width, GLsizei height,
    GLsizei depth, GLint border, GLsizei imageSize, const GLvoid *data)':
    names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.glCompressedTexImage3D' has no cute function "
        "yet. Qt's 'void "
        "QOpenGLTextureHelper::glCompressedTexImage3D(GLenum target, GLint "
        "level, GLenum internalFormat, GLsizei width, GLsizei height, "
        "GLsizei depth, GLint border, GLsizei imageSize, const GLvoid "
        "*data)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glCompressedTexSubImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::glCompressedTexSubImage1D(GLenum target,
    GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei
    imageSize, const GLvoid *data)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.glCompressedTexSubImage1D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLTextureHelper::glCompressedTexSubImage1D(GLenum target, "
        "GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei "
        "imageSize, const GLvoid *data)': names 'GLvoid', which has no cute "
        "class yet.")

  @staticmethod
  def glCompressedTexSubImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::glCompressedTexSubImage2D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height,
    GLenum format, GLsizei imageSize, const GLvoid *data)': names 'GLvoid',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.glCompressedTexSubImage2D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLTextureHelper::glCompressedTexSubImage2D(GLenum target, "
        "GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei "
        "height, GLenum format, GLsizei imageSize, const GLvoid *data)': "
        "names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glCompressedTexSubImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::glCompressedTexSubImage3D(GLenum target,
    GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const
    GLvoid *data)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.glCompressedTexSubImage3D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLTextureHelper::glCompressedTexSubImage3D(GLenum target, "
        "GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei "
        "width, GLsizei height, GLsizei depth, GLenum format, GLsizei "
        "imageSize, const GLvoid *data)': names 'GLvoid', which has no cute "
        "class yet.")

  @staticmethod
  def glCompressedTextureImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::glCompressedTextureImage1D(GLuint
    texture, GLenum target, GLenum bindingTarget, GLint level, GLenum
    internalFormat, GLsizei width, GLint border, GLsizei imageSize, const
    GLvoid *bits, const QOpenGLPixelTransferOptions *const options)': names
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.glCompressedTextureImage1D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLTextureHelper::glCompressedTextureImage1D(GLuint texture, "
        "GLenum target, GLenum bindingTarget, GLint level, GLenum "
        "internalFormat, GLsizei width, GLint border, GLsizei imageSize, "
        "const GLvoid *bits, const QOpenGLPixelTransferOptions *const "
        "options)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glCompressedTextureImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::glCompressedTextureImage2D(GLuint
    texture, GLenum target, GLenum bindingTarget, GLint level, GLenum
    internalFormat, GLsizei width, GLsizei height, GLint border, GLsizei
    imageSize, const GLvoid *bits, const QOpenGLPixelTransferOptions *const
    options)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.glCompressedTextureImage2D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLTextureHelper::glCompressedTextureImage2D(GLuint texture, "
        "GLenum target, GLenum bindingTarget, GLint level, GLenum "
        "internalFormat, GLsizei width, GLsizei height, GLint border, "
        "GLsizei imageSize, const GLvoid *bits, const "
        "QOpenGLPixelTransferOptions *const options)': names 'GLvoid', "
        "which has no cute class yet.")

  @staticmethod
  def glCompressedTextureImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::glCompressedTextureImage3D(GLuint
    texture, GLenum target, GLenum bindingTarget, GLint level, GLenum
    internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLint
    border, GLsizei imageSize, const GLvoid *bits, const
    QOpenGLPixelTransferOptions *const options)': names 'GLvoid', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.glCompressedTextureImage3D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLTextureHelper::glCompressedTextureImage3D(GLuint texture, "
        "GLenum target, GLenum bindingTarget, GLint level, GLenum "
        "internalFormat, GLsizei width, GLsizei height, GLsizei depth, "
        "GLint border, GLsizei imageSize, const GLvoid *bits, const "
        "QOpenGLPixelTransferOptions *const options)': names 'GLvoid', "
        "which has no cute class yet.")

  @staticmethod
  def glCompressedTextureSubImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::glCompressedTextureSubImage1D(GLuint
    texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset,
    GLsizei width, GLenum format, GLsizei imageSize, const GLvoid *bits,
    const QOpenGLPixelTransferOptions *const options)': names 'GLvoid', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.glCompressedTextureSubImage1D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLTextureHelper::glCompressedTextureSubImage1D(GLuint "
        "texture, GLenum target, GLenum bindingTarget, GLint level, GLint "
        "xoffset, GLsizei width, GLenum format, GLsizei imageSize, const "
        "GLvoid *bits, const QOpenGLPixelTransferOptions *const options)': "
        "names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glCompressedTextureSubImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::glCompressedTextureSubImage2D(GLuint
    texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset,
    GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei
    imageSize, const GLvoid *bits, const QOpenGLPixelTransferOptions *const
    options)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.glCompressedTextureSubImage2D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLTextureHelper::glCompressedTextureSubImage2D(GLuint "
        "texture, GLenum target, GLenum bindingTarget, GLint level, GLint "
        "xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum "
        "format, GLsizei imageSize, const GLvoid *bits, const "
        "QOpenGLPixelTransferOptions *const options)': names 'GLvoid', "
        "which has no cute class yet.")

  @staticmethod
  def glCompressedTextureSubImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::glCompressedTextureSubImage3D(GLuint
    texture, GLenum target, GLenum bindingTarget, GLint level, GLint xoffset,
    GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei
    depth, GLenum format, GLsizei imageSize, const GLvoid *bits, const
    QOpenGLPixelTransferOptions *const options)': names 'GLvoid', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.glCompressedTextureSubImage3D' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLTextureHelper::glCompressedTextureSubImage3D(GLuint "
        "texture, GLenum target, GLenum bindingTarget, GLint level, GLint "
        "xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei "
        "height, GLsizei depth, GLenum format, GLsizei imageSize, const "
        "GLvoid *bits, const QOpenGLPixelTransferOptions *const options)': "
        "names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glGetCompressedTexImage(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::glGetCompressedTexImage(GLenum target,
    GLint level, GLvoid *img)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.glGetCompressedTexImage' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLTextureHelper::glGetCompressedTexImage(GLenum target, GLint "
        "level, GLvoid *img)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glTexImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::glTexImage1D(GLenum target, GLint level,
    GLint internalFormat, GLsizei width, GLint border, GLenum format, GLenum
    type, const GLvoid *pixels)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.glTexImage1D' has no cute function yet. Qt's "
        "'void QOpenGLTextureHelper::glTexImage1D(GLenum target, GLint "
        "level, GLint internalFormat, GLsizei width, GLint border, GLenum "
        "format, GLenum type, const GLvoid *pixels)': names 'GLvoid', which "
        "has no cute class yet.")

  @staticmethod
  def glTexImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::glTexImage3D(GLenum target, GLint level,
    GLint internalFormat, GLsizei width, GLsizei height, GLsizei depth, GLint
    border, GLenum format, GLenum type, const GLvoid *pixels)': names
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.glTexImage3D' has no cute function yet. Qt's "
        "'void QOpenGLTextureHelper::glTexImage3D(GLenum target, GLint "
        "level, GLint internalFormat, GLsizei width, GLsizei height, "
        "GLsizei depth, GLint border, GLenum format, GLenum type, const "
        "GLvoid *pixels)': names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glTexSubImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::glTexSubImage1D(GLenum target, GLint
    level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const
    GLvoid *pixels)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.glTexSubImage1D' has no cute function yet. "
        "Qt's 'void QOpenGLTextureHelper::glTexSubImage1D(GLenum target, "
        "GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum "
        "type, const GLvoid *pixels)': names 'GLvoid', which has no cute "
        "class yet.")

  @staticmethod
  def glTexSubImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::glTexSubImage3D(GLenum target, GLint
    level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width,
    GLsizei height, GLsizei depth, GLenum format, GLenum type, const GLvoid
    *pixels)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.glTexSubImage3D' has no cute function yet. "
        "Qt's 'void QOpenGLTextureHelper::glTexSubImage3D(GLenum target, "
        "GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei "
        "width, GLsizei height, GLsizei depth, GLenum format, GLenum type, "
        "const GLvoid *pixels)': names 'GLvoid', which has no cute class "
        "yet.")

  @staticmethod
  def glTextureImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::glTextureImage1D(GLuint texture, GLenum
    target, GLenum bindingTarget, GLint level, GLenum internalFormat, GLsizei
    width, GLint border, GLenum format, GLenum type, const GLvoid *pixels)':
    names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.glTextureImage1D' has no cute function yet. "
        "Qt's 'void QOpenGLTextureHelper::glTextureImage1D(GLuint texture, "
        "GLenum target, GLenum bindingTarget, GLint level, GLenum "
        "internalFormat, GLsizei width, GLint border, GLenum format, GLenum "
        "type, const GLvoid *pixels)': names 'GLvoid', which has no cute "
        "class yet.")

  @staticmethod
  def glTextureImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::glTextureImage2D(GLuint texture, GLenum
    target, GLenum bindingTarget, GLint level, GLenum internalFormat, GLsizei
    width, GLsizei height, GLint border, GLenum format, GLenum type, const
    GLvoid *pixels)': names 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.glTextureImage2D' has no cute function yet. "
        "Qt's 'void QOpenGLTextureHelper::glTextureImage2D(GLuint texture, "
        "GLenum target, GLenum bindingTarget, GLint level, GLenum "
        "internalFormat, GLsizei width, GLsizei height, GLint border, "
        "GLenum format, GLenum type, const GLvoid *pixels)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glTextureImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::glTextureImage3D(GLuint texture, GLenum
    target, GLenum bindingTarget, GLint level, GLenum internalFormat, GLsizei
    width, GLsizei height, GLsizei depth, GLint border, GLenum format, GLenum
    type, const GLvoid *pixels)': names 'GLvoid', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.glTextureImage3D' has no cute function yet. "
        "Qt's 'void QOpenGLTextureHelper::glTextureImage3D(GLuint texture, "
        "GLenum target, GLenum bindingTarget, GLint level, GLenum "
        "internalFormat, GLsizei width, GLsizei height, GLsizei depth, "
        "GLint border, GLenum format, GLenum type, const GLvoid *pixels)': "
        "names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glTextureParameterfv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::glTextureParameterfv(GLuint texture,
    GLenum target, GLenum bindingTarget, GLenum pname, const GLfloat
    *params)': names 'GLfloat', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.glTextureParameterfv' has no cute function "
        "yet. Qt's 'void QOpenGLTextureHelper::glTextureParameterfv(GLuint "
        "texture, GLenum target, GLenum bindingTarget, GLenum pname, const "
        "GLfloat *params)': names 'GLfloat', which has no cute class yet.")

  @staticmethod
  def glTextureParameteriv(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::glTextureParameteriv(GLuint texture,
    GLenum target, GLenum bindingTarget, GLenum pname, const GLint *params)':
    names 'GLint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.glTextureParameteriv' has no cute function "
        "yet. Qt's 'void QOpenGLTextureHelper::glTextureParameteriv(GLuint "
        "texture, GLenum target, GLenum bindingTarget, GLenum pname, const "
        "GLint *params)': names 'GLint', which has no cute class yet.")

  @staticmethod
  def glTextureSubImage1D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::glTextureSubImage1D(GLuint texture,
    GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLsizei
    width, GLenum format, GLenum type, const GLvoid *pixels, const
    QOpenGLPixelTransferOptions *const options)': names 'GLvoid', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.glTextureSubImage1D' has no cute function "
        "yet. Qt's 'void QOpenGLTextureHelper::glTextureSubImage1D(GLuint "
        "texture, GLenum target, GLenum bindingTarget, GLint level, GLint "
        "xoffset, GLsizei width, GLenum format, GLenum type, const GLvoid "
        "*pixels, const QOpenGLPixelTransferOptions *const options)': names "
        "'GLvoid', which has no cute class yet.")

  @staticmethod
  def glTextureSubImage2D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::glTextureSubImage2D(GLuint texture,
    GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLint
    yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const
    GLvoid *pixels, const QOpenGLPixelTransferOptions *const options)': names
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.glTextureSubImage2D' has no cute function "
        "yet. Qt's 'void QOpenGLTextureHelper::glTextureSubImage2D(GLuint "
        "texture, GLenum target, GLenum bindingTarget, GLint level, GLint "
        "xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum "
        "format, GLenum type, const GLvoid *pixels, const "
        "QOpenGLPixelTransferOptions *const options)': names 'GLvoid', "
        "which has no cute class yet.")

  @staticmethod
  def glTextureSubImage3D(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLTextureHelper::glTextureSubImage3D(GLuint texture,
    GLenum target, GLenum bindingTarget, GLint level, GLint xoffset, GLint
    yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth,
    GLenum format, GLenum type, const GLvoid *pixels, const
    QOpenGLPixelTransferOptions *const options)': names 'GLvoid', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLTextureHelper.glTextureSubImage3D' has no cute function "
        "yet. Qt's 'void QOpenGLTextureHelper::glTextureSubImage3D(GLuint "
        "texture, GLenum target, GLenum bindingTarget, GLint level, GLint "
        "xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei "
        "height, GLsizei depth, GLenum format, GLenum type, const GLvoid "
        "*pixels, const QOpenGLPixelTransferOptions *const options)': names "
        "'GLvoid', which has no cute class yet.")
