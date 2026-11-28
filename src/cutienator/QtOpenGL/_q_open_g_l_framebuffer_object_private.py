"""
QOpenGLFramebufferObjectPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/6.12.0/QtOpenGL/private/qopenglframebufferobject_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QOpenGLFramebufferObjectPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QSize
  from ..QtGui import QOpenGLContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpenGLContext = WAIT['QOpenGLContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLFramebufferObjectPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLFramebufferObjectPrivate: a plain Python
  object standing in front of one C++ QOpenGLFramebufferObjectPrivate.

  C++ hands a QOpenGLFramebufferObjectPrivate around as a copy, so every C++
  QOpenGLFramebufferObjectPrivate behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QOpenGLFramebufferObjectPrivate that has a ritual
  and that Python can call so far, 2 names in all: 'checkFramebufferStatus',
  'fbo'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QOpenGLFramebufferObjectPrivate::~QOpenGLFramebufferObjectPrivate()':
    the destructor: Python removes its C++ QOpenGLFramebufferObjectPrivate by
    it, and has no other use for it.

  What has no ritual
  ------------------

  4 of the 8 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 cannot be
  called and cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QOpenGLFramebufferObjectPrivate is created at the first use, not
    by 'QOpenGLFramebufferObjectPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGLFramebufferObjectPrivate back gives a copy the
    ritual made for Python, in a new cute QOpenGLFramebufferObjectPrivate.
  - Each name of Qt's QOpenGLFramebufferObjectPrivate that has no cute
    function yet, 'init', 'initColorBuffer', 'initDepthStencilAttachments',
    'initTexture', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The classes Qt writes inside QOpenGLFramebufferObjectPrivate, each a
  #  class in here as in C++.

  class ColorAttachment(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QOpenGLFramebufferObjectPrivate::ColorAttachment: a
    plain Python object standing in front of one C++
    QOpenGLFramebufferObjectPrivate::ColorAttachment.

    C++ hands a QOpenGLFramebufferObjectPrivate::ColorAttachment around as a
    copy, so every C++ QOpenGLFramebufferObjectPrivate::ColorAttachment
    behind a cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QOpenGLFramebufferObjectPrivate::ColorAttachment yet.
    It can be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QOpenGLFramebufferObjectPrivate::ColorAttachment::~ColorAttachment()':
      the destructor: Python removes its C++
      QOpenGLFramebufferObjectPrivate::ColorAttachment by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QOpenGLFramebufferObjectPrivate::ColorAttachment is created at
      the first use, not by
      'QOpenGLFramebufferObjectPrivate::ColorAttachment(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QOpenGLFramebufferObjectPrivate::ColorAttachment
      back gives a copy the ritual made for Python, in a new cute
      QOpenGLFramebufferObjectPrivate::ColorAttachment.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QSize = WAIT['QSize']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QOpenGLFramebufferObjectPrivate::ColorAttachment'

    #  Qt's '~QOpenGLFramebufferObjectPrivate::ColorAttachment()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QOpenGLFramebufferObjectPrivate::ColorAttachment behind a cute one,
    #  and removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN31QOpenGLFramebufferObjectPrivate15ColorAttachmentD1Ev')

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QOpenGLFramebufferObjectPrivate::ColorAttachment::ColorAttachment()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qopenglframebufferobjectprivate-colorattachment.html
      """
      #  QOpenGLFramebufferObjectPrivate::ColorAttachment::ColorAttachment()
      self._noteCreation(
          QOpenGLFramebufferObjectPrivate.ColorAttachment, lambda: Rituals.call(
              'ritual_ZN31QOpenGLFramebufferObjectPrivate15ColorAttachmentC'
              '1Ev',
          ))

    @overload(QSize, int)
    def __init__(self, size: QSize, internalFormat: int) -> None:
      """
      Notes what was given, for Qt's
      'QOpenGLFramebufferObjectPrivate::ColorAttachment::ColorAttachment(
      const QSize &size, GLenum internalFormat)', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qopenglframebufferobjectprivate-colorattachment.html

      Parameters
      ----------

      size : QSize
        Passed on as a value: Qt reads the C++ QSize, which stays Python's
        own.

      internalFormat : int
        Passed on as it is.
      """
      #  QOpenGLFramebufferObjectPrivate::ColorAttachment::
      #      ColorAttachment(const QSize &size, GLenum internalFormat)
      self._noteCreation(
          QOpenGLFramebufferObjectPrivate.ColorAttachment, lambda: Rituals.call(
              'ritual_ZN31QOpenGLFramebufferObjectPrivate15ColorAttachmentC'
              '1ERK5QSizej',
              self._valueOf(size), internalFormat,
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
  __qt_class__ = 'QOpenGLFramebufferObjectPrivate'

  #  Qt's '~QOpenGLFramebufferObjectPrivate()'. Naming it makes this a value
  #  class: Python owns every C++ QOpenGLFramebufferObjectPrivate behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN31QOpenGLFramebufferObjectPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QOpenGLContext)
  @overload(NoneType)
  def checkFramebufferStatus(self, ctx: Optional[QOpenGLContext]) -> bool:
    """
    Calls Qt's 'bool
    QOpenGLFramebufferObjectPrivate::checkFramebufferStatus(QOpenGLContext
    *ctx) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobjectprivate.html

    Parameters
    ----------

    ctx : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QOpenGLFramebufferObjectPrivate::checkFramebufferStatus(
    #      QOpenGLContext *ctx) const
    return self.uglySide.call(
        'ritual_ZNK31QOpenGLFramebufferObjectPrivate22checkFramebufferStatu'
        'sEP14QOpenGLContext',
        self._addressOf(ctx),
    )

  def fbo(self) -> int:
    """
    Calls Qt's 'GLuint QOpenGLFramebufferObjectPrivate::fbo() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobjectprivate.html#fbo
    """
    #  GLuint QOpenGLFramebufferObjectPrivate::fbo() const
    return self.uglySide.call(
        'ritual_ZNK31QOpenGLFramebufferObjectPrivate3fboEv',
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
    'QOpenGLFramebufferObjectPrivate::QOpenGLFramebufferObjectPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobjectprivate.html
    """
    #  QOpenGLFramebufferObjectPrivate::QOpenGLFramebufferObjectPrivate()
    self._noteCreation(QOpenGLFramebufferObjectPrivate, lambda: Rituals.call(
        'ritual_ZN31QOpenGLFramebufferObjectPrivateC1Ev',
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

  @staticmethod
  def init(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFramebufferObjectPrivate::init(QOpenGLFramebufferObject
    *q, const QSize &size, QOpenGLFramebufferObject::Attachment attachment,
    GLenum texture_target, GLenum internal_format, GLint samples, bool
    mipmap)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QOpenGLFramebufferObjectPrivate.init' has no cute function yet. "
        "Qt's 'void "
        "QOpenGLFramebufferObjectPrivate::init(QOpenGLFramebufferObject *q, "
        "const QSize &size, QOpenGLFramebufferObject::Attachment "
        "attachment, GLenum texture_target, GLenum internal_format, GLint "
        "samples, bool mipmap)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def initColorBuffer(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFramebufferObjectPrivate::initColorBuffer(int idx,
    GLint *samples)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'QT_CHECK_GLERROR'.
    """
    raise NotImplementedError(
        "'QOpenGLFramebufferObjectPrivate.initColorBuffer' has no cute "
        "function yet. Qt's 'void "
        "QOpenGLFramebufferObjectPrivate::initColorBuffer(int idx, GLint "
        "*samples)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'QT_CHECK_GLERROR'.")

  @staticmethod
  def initDepthStencilAttachments(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFramebufferObjectPrivate::initDepthStencilAttachments(
    QOpenGLContext *ctx, QOpenGLFramebufferObject::Attachment attachment)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'freeRenderbufferFunc'.
    """
    raise NotImplementedError(
        "'QOpenGLFramebufferObjectPrivate.initDepthStencilAttachments' has "
        "no cute function yet. Qt's 'void "
        "QOpenGLFramebufferObjectPrivate::initDepthStencilAttachments(QOpenG"
        "LContext *ctx, QOpenGLFramebufferObject::Attachment attachment)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'freeRenderbufferFunc'.")

  @staticmethod
  def initTexture(*__, **_) -> Never:
    """
    Qt's 'void QOpenGLFramebufferObjectPrivate::initTexture(int idx)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'QT_CHECK_GLERROR'.
    """
    raise NotImplementedError(
        "'QOpenGLFramebufferObjectPrivate.initTexture' has no cute function "
        "yet. Qt's 'void QOpenGLFramebufferObjectPrivate::initTexture(int "
        "idx)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'QT_CHECK_GLERROR'.")
