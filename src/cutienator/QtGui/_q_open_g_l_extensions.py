"""
QOpenGLExtensions binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qopenglextensions_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QOpenGLExtensions to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from . import QOpenGLExtraFunctions

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QOpenGLContext, QOpenGLExtensionsPrivate
  from . import QOpenGLFunctionsPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpenGLContext = WAIT['QOpenGLContext']
  QOpenGLFunctionsPrivate = WAIT['QOpenGLFunctionsPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLExtensions(QOpenGLExtraFunctions):
  """
  The cute side of Qt's QOpenGLExtensions: a plain Python object standing in
  front of one C++ QOpenGLExtensions.

  It is built on the cute 'QOpenGLExtraFunctions', as Qt's QOpenGLExtensions
  is built on Qt's QOpenGLExtraFunctions, and has everything that class has.

  C++ hands a QOpenGLExtensions around as a copy, so every C++
  QOpenGLExtensions behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpenGLExtensions that has a ritual and that Python
  can call so far, 6 names in all: 'd_func', 'openGLExtensions',
  'hasOpenGLExtension', 'flushShared', 'd', 'isInitialized'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QOpenGLExtensionsPrivate *QOpenGLExtensions::d_func() const':
    takes in Python what 'QOpenGLExtensionsPrivate
    *QOpenGLExtensions::d_func()' takes.
  - Qt's 'QOpenGLExtensions::~QOpenGLExtensions()': the destructor: Python
    removes its C++ QOpenGLExtensions by it, and has no other use for it.
  - Qt's 'GLvoid *QOpenGLExtensions::glMapBuffer(GLenum target, GLenum
    access)': gives 'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLExtensions::glGetBufferSubData(GLenum target,
    qopengl_GLintptr offset, qopengl_GLsizeiptr size, GLvoid *data)': names
    'GLvoid', which has no cute class yet.
  - Qt's 'void QOpenGLExtensions::discardFramebuffer(GLenum target, GLsizei
    numAttachments, const GLenum *attachments)': names 'GLenum', which has no
    cute class yet.

  What to expect
  --------------

  - The C++ QOpenGLExtensions is created at the first use, not by
    'QOpenGLExtensions(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGLExtensions back gives a copy the ritual made
    for Python, in a new cute QOpenGLExtensions.
  - Each name of Qt's QOpenGLExtensions that has no cute function yet,
    'discardFramebuffer', 'glGetBufferSubData', 'glMapBuffer', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QOpenGLExtensions, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class OpenGLExtension(CuteFlags):
    """
    The flags enum 'QOpenGLExtensions::OpenGLExtension' of Qt, with the 31
    names Qt gives in it. Qt names the type of its combinations
    'QOpenGLExtensions::OpenGLExtensions'.
    """

    TextureRectangle = 0x1
    GenerateMipmap = 0x2
    TextureCompression = 0x4
    MirroredRepeat = 0x8
    FramebufferMultisample = 0x10
    StencilTwoSide = 0x20
    StencilWrap = 0x40
    PackedDepthStencil = 0x80
    NVFloatBuffer = 0x100
    PixelBufferObject = 0x200
    FramebufferBlit = 0x400
    BGRATextureFormat = 0x800
    DDSTextureCompression = 0x1000
    ETC1TextureCompression = 0x2000
    PVRTCTextureCompression = 0x4000
    ElementIndexUint = 0x8000
    Depth24 = 0x10000
    SRGBFrameBuffer = 0x20000
    MapBuffer = 0x40000
    GeometryShaders = 0x80000
    MapBufferRange = 0x100000
    Sized8Formats = 0x200000
    DiscardFramebuffer = 0x400000
    Sized16Formats = 0x800000
    TextureSwizzle = 0x1000000
    StandardDerivatives = 0x2000000
    ASTCTextureCompression = 0x4000000
    ETC2TextureCompression = 0x8000000
    HalfFloatVertex = 0x10000000
    MultiView = 0x20000000
    MultiViewExtended = 0x40000000

  OpenGLExtensions = OpenGLExtension

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QOpenGLFunctionsPrivate)
  @overload(NoneType)
  def isInitialized(d: Optional[QOpenGLFunctionsPrivate]) -> bool:
    """
    Calls Qt's 'bool QOpenGLExtensions::isInitialized(const
    QOpenGLFunctionsPrivate *d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextensions.html#isInitialized

    Parameters
    ----------

    d : Optional[QOpenGLFunctionsPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QOpenGLExtensions::isInitialized(const QOpenGLFunctionsPrivate
    #      *d)
    return Rituals.call(
        'ritual_ZN17QOpenGLExtensions13isInitializedEPK23QOpenGLFunctionsPr'
        'ivate',
        CuteMixin._addressOf(d),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLExtensions'

  #  Qt's '~QOpenGLExtensions()'. Naming it makes this a value class: Python
  #  owns every C++ QOpenGLExtensions behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QOpenGLExtensionsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(OpenGLExtension)
  def hasOpenGLExtension(self, extension: OpenGLExtension) -> bool:
    """
    Calls Qt's 'bool
    QOpenGLExtensions::hasOpenGLExtension(QOpenGLExtensions::OpenGLExtension
    extension) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextensions.html#hasOpenGLExtension

    Parameters
    ----------

    extension : OpenGLExtension
      Passed on as its number.
    """
    #  bool QOpenGLExtensions::hasOpenGLExtension(QOpenGLExtensions::
    #      OpenGLExtension extension) const
    return self.uglySide.call(
        'ritual_ZNK17QOpenGLExtensions18hasOpenGLExtensionENS_15OpenGLExten'
        'sionE',
        extension.value,
    )

  def d(self) -> Optional[QOpenGLExtensionsPrivate]:
    """
    Calls Qt's 'QOpenGLExtensionsPrivate *QOpenGLExtensions::d() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglextensions.html#d

    Returns
    -------

    Optional[QOpenGLExtensionsPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLExtensionsPrivate *QOpenGLExtensions::d() const
    address = self.uglySide.call('ritual_ZNK17QOpenGLExtensions1dEv')
    from . import QOpenGLExtensionsPrivate
    return QOpenGLExtensionsPrivate._cuteAt(address)

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
    Notes what was given, for Qt's 'QOpenGLExtensions::QOpenGLExtensions()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextensions.html#QOpenGLExtensions
    """
    #  QOpenGLExtensions::QOpenGLExtensions()
    self._noteCreation(QOpenGLExtensions, lambda: Rituals.call(
        'ritual_ZN17QOpenGLExtensionsC1Ev',
    ))

  @overload(QOpenGLContext)
  @overload(NoneType)
  def __init__(self, context: Optional[QOpenGLContext]) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLExtensions::QOpenGLExtensions(QOpenGLContext *context)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextensions.html#QOpenGLExtensions

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOpenGLExtensions::QOpenGLExtensions(QOpenGLContext *context)
    self._noteCreation(QOpenGLExtensions, lambda: Rituals.call(
        'ritual_ZN17QOpenGLExtensionsC1EP14QOpenGLContext',
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

  def d_func(self) -> Optional[QOpenGLExtensionsPrivate]:
    """
    Calls Qt's 'QOpenGLExtensionsPrivate *QOpenGLExtensions::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglextensions.html#d_func

    Returns
    -------

    Optional[QOpenGLExtensionsPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLExtensionsPrivate *QOpenGLExtensions::d_func()
    address = self.uglySide.call('ritual_ZN17QOpenGLExtensions6d_funcEv')
    from . import QOpenGLExtensionsPrivate
    return QOpenGLExtensionsPrivate._cuteAt(address)

  def openGLExtensions(self) -> OpenGLExtensions:
    """
    Calls Qt's 'OpenGLExtensions QOpenGLExtensions::openGLExtensions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglextensions.html#openGLExtensions

    Returns
    -------

    OpenGLExtensions
      The value standing for the combination Qt gave back.
    """
    #  OpenGLExtensions QOpenGLExtensions::openGLExtensions()
    return QOpenGLExtensions.OpenGLExtensions(self.uglySide.call(
        'ritual_ZN17QOpenGLExtensions16openGLExtensionsEv',
    ))

  def flushShared(self) -> None:
    """
    Calls Qt's 'void QOpenGLExtensions::flushShared()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglextensions.html#flushShared
    """
    #  void QOpenGLExtensions::flushShared()
    self.uglySide.call('ritual_ZN17QOpenGLExtensions11flushSharedEv')

  @staticmethod
  def discardFramebuffer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLExtensions::discardFramebuffer(GLenum target, GLsizei
    numAttachments, const GLenum *attachments)': names 'GLenum', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLExtensions.discardFramebuffer' has no cute function yet. "
        "Qt's 'void QOpenGLExtensions::discardFramebuffer(GLenum target, "
        "GLsizei numAttachments, const GLenum *attachments)': names "
        "'GLenum', which has no cute class yet.")

  @staticmethod
  def glGetBufferSubData(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLExtensions::glGetBufferSubData(GLenum target,
    qopengl_GLintptr offset, qopengl_GLsizeiptr size, GLvoid *data)': names
    'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLExtensions.glGetBufferSubData' has no cute function yet. "
        "Qt's 'void QOpenGLExtensions::glGetBufferSubData(GLenum target, "
        "qopengl_GLintptr offset, qopengl_GLsizeiptr size, GLvoid *data)': "
        "names 'GLvoid', which has no cute class yet.")

  @staticmethod
  def glMapBuffer(*__, **_) -> Never:
    """
    Qt's 'GLvoid *QOpenGLExtensions::glMapBuffer(GLenum target, GLenum
    access)': gives 'GLvoid', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QOpenGLExtensions.glMapBuffer' has no cute function yet. Qt's "
        "'GLvoid *QOpenGLExtensions::glMapBuffer(GLenum target, GLenum "
        "access)': gives 'GLvoid', which has no cute class yet.")
