"""
QOpenGLFramebufferObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopenglframebufferobject.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRect, QSize
  from ..QtGui import QImage
  from . import QOpenGLFramebufferObjectFormat
  from . import QOpenGLFramebufferObjectPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpenGLFramebufferObjectFormat = WAIT['QOpenGLFramebufferObjectFormat']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLFramebufferObject(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLFramebufferObject: a plain Python object
  standing in front of one C++ QOpenGLFramebufferObject.

  What exists
  -----------

  Every function of Qt's QOpenGLFramebufferObject that has a ritual and that
  Python can call so far, 21 names in all: 'd_func', 'addColorAttachment',
  'format', 'isValid', 'isBound', 'bind', 'release', 'width', 'height',
  'texture', 'takeTexture', 'size', 'sizes', 'toImage', 'attachment',
  'setAttachment', 'handle', 'bindDefault', 'hasOpenGLFramebufferObjects',
  'hasOpenGLFramebufferBlit', 'blitFramebuffer'. It can be made from Python,
  in 6 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QOpenGLFramebufferObjectPrivate
    *QOpenGLFramebufferObject::d_func() const': takes in Python what
    'QOpenGLFramebufferObjectPrivate *QOpenGLFramebufferObject::d_func()'
    takes.
  - Qt's 'QOpenGLFramebufferObject::~QOpenGLFramebufferObject()': the
    destructor: Python never removes a C++ QOpenGLFramebufferObject.
  - Qt's 'QList<GLuint> QOpenGLFramebufferObject::textures() const': gives a
    type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 38 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QOpenGLFramebufferObject is created at the first use, not by
    'QOpenGLFramebufferObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLFramebufferObject.
  - Each name of Qt's QOpenGLFramebufferObject that has no cute function yet,
    'textures', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QOpenGLFramebufferObject, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Attachment(CuteNum):
    """
    The enum 'QOpenGLFramebufferObject::Attachment' of Qt, with the 3 names
    Qt gives in it.
    """

    NoAttachment = Kee[int](0)
    CombinedDepthStencil = Kee[int](1)
    Depth = Kee[int](2)

  class FramebufferRestorePolicy(CuteNum):
    """
    The enum 'QOpenGLFramebufferObject::FramebufferRestorePolicy' of Qt, with
    the 3 names Qt gives in it.
    """

    DontRestoreFramebufferBinding = Kee[int](0)
    RestoreFramebufferBindingToDefault = Kee[int](1)
    RestoreFrameBufferBinding = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def bindDefault() -> bool:
    """
    Calls Qt's 'bool QOpenGLFramebufferObject::bindDefault()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html#bindDefault
    """
    #  bool QOpenGLFramebufferObject::bindDefault()
    return Rituals.call('ritual_ZN24QOpenGLFramebufferObject11bindDefaultEv')

  @staticmethod
  def hasOpenGLFramebufferObjects() -> bool:
    """
    Calls Qt's 'bool
    QOpenGLFramebufferObject::hasOpenGLFramebufferObjects()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html
    """
    #  bool QOpenGLFramebufferObject::hasOpenGLFramebufferObjects()
    return Rituals.call(
        'ritual_ZN24QOpenGLFramebufferObject27hasOpenGLFramebufferObjectsEv',
    )

  @staticmethod
  def hasOpenGLFramebufferBlit() -> bool:
    """
    Calls Qt's 'bool QOpenGLFramebufferObject::hasOpenGLFramebufferBlit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html
    """
    #  bool QOpenGLFramebufferObject::hasOpenGLFramebufferBlit()
    return Rituals.call(
        'ritual_ZN24QOpenGLFramebufferObject24hasOpenGLFramebufferBlitEv',
    )

  @staticmethod
  @overload(
      THIS, QRect, THIS, QRect, int, int, int, int, FramebufferRestorePolicy,
  )
  @overload(
      THIS, QRect, NoneType, QRect, int, int, int, int,
      FramebufferRestorePolicy,
  )
  @overload(
      NoneType, QRect, THIS, QRect, int, int, int, int,
      FramebufferRestorePolicy,
  )
  @overload(
      NoneType, QRect, NoneType, QRect, int, int, int, int,
      FramebufferRestorePolicy,
  )
  def blitFramebuffer(
      target: Optional[QOpenGLFramebufferObject],
      targetRect: QRect,
      source: Optional[QOpenGLFramebufferObject],
      sourceRect: QRect,
      buffers: int,
      filter: int,
      readColorAttachmentIndex: int,
      drawColorAttachmentIndex: int,
      restorePolicy: FramebufferRestorePolicy,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFramebufferObject::blitFramebuffer(QOpenGLFramebufferObject
    *target, const QRect &targetRect, QOpenGLFramebufferObject *source, const
    QRect &sourceRect, GLbitfield buffers, GLenum filter, int
    readColorAttachmentIndex, int drawColorAttachmentIndex,
    FramebufferRestorePolicy restorePolicy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html#blitFramebuffer

    Parameters
    ----------

    target : Optional[QOpenGLFramebufferObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    targetRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    source : Optional[QOpenGLFramebufferObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sourceRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    buffers : int
      Passed on as it is.

    filter : int
      Passed on as it is.

    readColorAttachmentIndex : int
      Passed on as it is.

    drawColorAttachmentIndex : int
      Passed on as it is.

    restorePolicy : FramebufferRestorePolicy
      Passed on as its number.
    """
    #  void
    #      QOpenGLFramebufferObject::blitFramebuffer(QOpenGLFramebufferObject
    #      *target, const QRect &targetRect, QOpenGLFramebufferObject
    #      *source, const QRect &sourceRect, GLbitfield buffers, GLenum
    #      filter, int readColorAttachmentIndex, int
    #      drawColorAttachmentIndex, FramebufferRestorePolicy restorePolicy)
    Rituals.call(
        'ritual_ZN24QOpenGLFramebufferObject15blitFramebufferEPS_RK5QRectS0'
        '_S3_jjiiNS_24FramebufferRestorePolicyE',
        CuteMixin._addressOf(target), CuteMixin._valueOf(targetRect),
        CuteMixin._addressOf(source), CuteMixin._valueOf(sourceRect),
        buffers, filter, readColorAttachmentIndex, drawColorAttachmentIndex,
        restorePolicy.value,
    )

  @staticmethod
  @overload(THIS, QRect, THIS, QRect, int, int, int, int)
  @overload(THIS, QRect, NoneType, QRect, int, int, int, int)
  @overload(NoneType, QRect, THIS, QRect, int, int, int, int)
  @overload(NoneType, QRect, NoneType, QRect, int, int, int, int)
  def blitFramebuffer(
      target: Optional[QOpenGLFramebufferObject],
      targetRect: QRect,
      source: Optional[QOpenGLFramebufferObject],
      sourceRect: QRect,
      buffers: int,
      filter: int,
      readColorAttachmentIndex: int,
      drawColorAttachmentIndex: int,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFramebufferObject::blitFramebuffer(QOpenGLFramebufferObject
    *target, const QRect &targetRect, QOpenGLFramebufferObject *source, const
    QRect &sourceRect, GLbitfield buffers, GLenum filter, int
    readColorAttachmentIndex, int drawColorAttachmentIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html#blitFramebuffer

    Parameters
    ----------

    target : Optional[QOpenGLFramebufferObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    targetRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    source : Optional[QOpenGLFramebufferObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sourceRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    buffers : int
      Passed on as it is.

    filter : int
      Passed on as it is.

    readColorAttachmentIndex : int
      Passed on as it is.

    drawColorAttachmentIndex : int
      Passed on as it is.
    """
    #  void
    #      QOpenGLFramebufferObject::blitFramebuffer(QOpenGLFramebufferObject
    #      *target, const QRect &targetRect, QOpenGLFramebufferObject
    #      *source, const QRect &sourceRect, GLbitfield buffers, GLenum
    #      filter, int readColorAttachmentIndex, int
    #      drawColorAttachmentIndex)
    Rituals.call(
        'ritual_ZN24QOpenGLFramebufferObject15blitFramebufferEPS_RK5QRectS0'
        '_S3_jjii',
        CuteMixin._addressOf(target), CuteMixin._valueOf(targetRect),
        CuteMixin._addressOf(source), CuteMixin._valueOf(sourceRect),
        buffers, filter, readColorAttachmentIndex, drawColorAttachmentIndex,
    )

  @staticmethod
  @overload(THIS, QRect, THIS, QRect)
  @overload(THIS, QRect, NoneType, QRect)
  @overload(NoneType, QRect, THIS, QRect)
  @overload(NoneType, QRect, NoneType, QRect)
  @overload(THIS, QRect, THIS, QRect, int)
  @overload(THIS, QRect, NoneType, QRect, int)
  @overload(NoneType, QRect, THIS, QRect, int)
  @overload(NoneType, QRect, NoneType, QRect, int)
  @overload(THIS, QRect, THIS, QRect, int, int)
  @overload(THIS, QRect, NoneType, QRect, int, int)
  @overload(NoneType, QRect, THIS, QRect, int, int)
  @overload(NoneType, QRect, NoneType, QRect, int, int)
  def blitFramebuffer(
      target: Optional[QOpenGLFramebufferObject],
      targetRect: QRect,
      source: Optional[QOpenGLFramebufferObject],
      sourceRect: QRect,
      buffers: int = 16384,
      filter: int = 9728,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFramebufferObject::blitFramebuffer(QOpenGLFramebufferObject
    *target, const QRect &targetRect, QOpenGLFramebufferObject *source, const
    QRect &sourceRect, GLbitfield buffers, GLenum filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html#blitFramebuffer

    Parameters
    ----------

    target : Optional[QOpenGLFramebufferObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    targetRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    source : Optional[QOpenGLFramebufferObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sourceRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    buffers : int
      Passed on as it is. May be left out, as in Qt: it is then 16384.

    filter : int
      Passed on as it is. May be left out, as in Qt: it is then 9728.
    """
    #  void
    #      QOpenGLFramebufferObject::blitFramebuffer(QOpenGLFramebufferObject
    #      *target, const QRect &targetRect, QOpenGLFramebufferObject
    #      *source, const QRect &sourceRect, GLbitfield buffers, GLenum
    #      filter)
    Rituals.call(
        'ritual_ZN24QOpenGLFramebufferObject15blitFramebufferEPS_RK5QRectS0'
        '_S3_jj',
        CuteMixin._addressOf(target), CuteMixin._valueOf(targetRect),
        CuteMixin._addressOf(source), CuteMixin._valueOf(sourceRect),
        buffers, filter,
    )

  @staticmethod
  @overload(THIS, THIS)
  @overload(THIS, NoneType)
  @overload(NoneType, THIS)
  @overload(NoneType, NoneType)
  @overload(THIS, THIS, int)
  @overload(THIS, NoneType, int)
  @overload(NoneType, THIS, int)
  @overload(NoneType, NoneType, int)
  @overload(THIS, THIS, int, int)
  @overload(THIS, NoneType, int, int)
  @overload(NoneType, THIS, int, int)
  @overload(NoneType, NoneType, int, int)
  def blitFramebuffer(
      target: Optional[QOpenGLFramebufferObject],
      source: Optional[QOpenGLFramebufferObject],
      buffers: int = 16384,
      filter: int = 9728,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFramebufferObject::blitFramebuffer(QOpenGLFramebufferObject
    *target, QOpenGLFramebufferObject *source, GLbitfield buffers, GLenum
    filter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html#blitFramebuffer

    Parameters
    ----------

    target : Optional[QOpenGLFramebufferObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    source : Optional[QOpenGLFramebufferObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    buffers : int
      Passed on as it is. May be left out, as in Qt: it is then 16384.

    filter : int
      Passed on as it is. May be left out, as in Qt: it is then 9728.
    """
    #  void
    #      QOpenGLFramebufferObject::blitFramebuffer(QOpenGLFramebufferObject
    #      *target, QOpenGLFramebufferObject *source, GLbitfield buffers,
    #      GLenum filter)
    Rituals.call(
        'ritual_ZN24QOpenGLFramebufferObject15blitFramebufferEPS_S0_jj',
        CuteMixin._addressOf(target), CuteMixin._addressOf(source), buffers,
        filter,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLFramebufferObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def format(self) -> QOpenGLFramebufferObjectFormat:
    """
    Calls Qt's 'QOpenGLFramebufferObjectFormat
    QOpenGLFramebufferObject::format() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html#format

    Returns
    -------

    QOpenGLFramebufferObjectFormat
      A new cute QOpenGLFramebufferObjectFormat around the copy Qt gave back.
      Python owns it.
    """
    #  QOpenGLFramebufferObjectFormat QOpenGLFramebufferObject::format()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK24QOpenGLFramebufferObject6formatEv',
    )
    from . import QOpenGLFramebufferObjectFormat
    return QOpenGLFramebufferObjectFormat._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLFramebufferObject::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html#isValid
    """
    #  bool QOpenGLFramebufferObject::isValid() const
    return self.uglySide.call(
        'ritual_ZNK24QOpenGLFramebufferObject7isValidEv',
    )

  def isBound(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLFramebufferObject::isBound() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html#isBound
    """
    #  bool QOpenGLFramebufferObject::isBound() const
    return self.uglySide.call(
        'ritual_ZNK24QOpenGLFramebufferObject7isBoundEv',
    )

  def width(self) -> int:
    """
    Calls Qt's 'int QOpenGLFramebufferObject::width() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html#width
    """
    #  int QOpenGLFramebufferObject::width() const
    return self.uglySide.call('ritual_ZNK24QOpenGLFramebufferObject5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int QOpenGLFramebufferObject::height() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html#height
    """
    #  int QOpenGLFramebufferObject::height() const
    return self.uglySide.call(
        'ritual_ZNK24QOpenGLFramebufferObject6heightEv',
    )

  def texture(self) -> int:
    """
    Calls Qt's 'GLuint QOpenGLFramebufferObject::texture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html#texture
    """
    #  GLuint QOpenGLFramebufferObject::texture() const
    return self.uglySide.call(
        'ritual_ZNK24QOpenGLFramebufferObject7textureEv',
    )

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QOpenGLFramebufferObject::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglframebufferobject.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QOpenGLFramebufferObject::size() const
    address = self.uglySide.call(
        'ritual_ZNK24QOpenGLFramebufferObject4sizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def sizes(self) -> QList[QSize]:
    """
    Calls Qt's 'QList<QSize> QOpenGLFramebufferObject::sizes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html#sizes

    Returns
    -------

    QList[QSize]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QSize> QOpenGLFramebufferObject::sizes() const
    address = self.uglySide.call(
        'ritual_ZNK24QOpenGLFramebufferObject5sizesEv',
    )
    from ..QtCore import QSize
    return QList[QSize]._cuteOwning(address)

  @overload()
  @overload(bool)
  def toImage(self, flipped: bool = True) -> QImage:
    """
    Calls Qt's 'QImage QOpenGLFramebufferObject::toImage(bool flipped)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html#toImage

    Parameters
    ----------

    flipped : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QOpenGLFramebufferObject::toImage(bool flipped) const
    address = self.uglySide.call(
        'ritual_ZNK24QOpenGLFramebufferObject7toImageEb', flipped,
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  @overload(bool, int)
  def toImage(self, flipped: bool, colorAttachmentIndex: int) -> QImage:
    """
    Calls Qt's 'QImage QOpenGLFramebufferObject::toImage(bool flipped, int
    colorAttachmentIndex) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html#toImage

    Parameters
    ----------

    flipped : bool
      Passed on as it is.

    colorAttachmentIndex : int
      Passed on as it is.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QOpenGLFramebufferObject::toImage(bool flipped, int
    #      colorAttachmentIndex) const
    address = self.uglySide.call(
        'ritual_ZNK24QOpenGLFramebufferObject7toImageEbi',
        flipped, colorAttachmentIndex,
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def attachment(self) -> Attachment:
    """
    Calls Qt's 'Attachment QOpenGLFramebufferObject::attachment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html#attachment

    Returns
    -------

    Attachment
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Attachment(number)'
      gives.
    """
    #  Attachment QOpenGLFramebufferObject::attachment() const
    return QOpenGLFramebufferObject.Attachment(self.uglySide.call(
        'ritual_ZNK24QOpenGLFramebufferObject10attachmentEv',
    ))

  def handle(self) -> int:
    """
    Calls Qt's 'GLuint QOpenGLFramebufferObject::handle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html#handle
    """
    #  GLuint QOpenGLFramebufferObject::handle() const
    return self.uglySide.call(
        'ritual_ZNK24QOpenGLFramebufferObject6handleEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Attachment)
  def setAttachment(self, attachment: Attachment) -> None:
    """
    Calls Qt's 'void QOpenGLFramebufferObject::setAttachment(Attachment
    attachment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html#setAttachment

    Parameters
    ----------

    attachment : Attachment
      Passed on as its number.
    """
    #  void QOpenGLFramebufferObject::setAttachment(Attachment attachment)
    self.uglySide.call(
        'ritual_ZN24QOpenGLFramebufferObject13setAttachmentENS_10Attachment'
        'E',
        attachment.value,
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

  @overload(QSize)
  @overload(QSize, int)
  def __init__(self, size: QSize, target: int = 3553) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLFramebufferObject::QOpenGLFramebufferObject(const QSize &size,
    GLenum target)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    target : int
      Passed on as it is. May be left out, as in Qt: it is then 3553.
    """
    #  QOpenGLFramebufferObject::QOpenGLFramebufferObject(const QSize &size,
    #      GLenum target)
    self._noteCreation(QOpenGLFramebufferObject, lambda: Rituals.call(
        'ritual_ZN24QOpenGLFramebufferObjectC1ERK5QSizej',
        self._valueOf(size), target,
    ))

  @overload(int, int)
  @overload(int, int, int)
  def __init__(self, width: int, height: int, target: int = 3553) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLFramebufferObject::QOpenGLFramebufferObject(int width, int
    height, GLenum target)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    target : int
      Passed on as it is. May be left out, as in Qt: it is then 3553.
    """
    #  QOpenGLFramebufferObject::QOpenGLFramebufferObject(int width, int
    #      height, GLenum target)
    self._noteCreation(QOpenGLFramebufferObject, lambda: Rituals.call(
        'ritual_ZN24QOpenGLFramebufferObjectC1Eiij', width, height, target,
    ))

  @overload(QSize, Attachment)
  @overload(QSize, Attachment, int)
  @overload(QSize, Attachment, int, int)
  def __init__(
      self,
      size: QSize,
      attachment: Attachment,
      target: int = 3553,
      internalFormat: int = 0,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLFramebufferObject::QOpenGLFramebufferObject(const QSize &size,
    Attachment attachment, GLenum target, GLenum internalFormat)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    attachment : Attachment
      Passed on as its number.

    target : int
      Passed on as it is. May be left out, as in Qt: it is then 3553.

    internalFormat : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QOpenGLFramebufferObject::QOpenGLFramebufferObject(const QSize &size,
    #      Attachment attachment, GLenum target, GLenum internalFormat)
    self._noteCreation(QOpenGLFramebufferObject, lambda: Rituals.call(
        'ritual_ZN24QOpenGLFramebufferObjectC1ERK5QSizeNS_10AttachmentEjj',
        self._valueOf(size), attachment.value, target, internalFormat,
    ))

  @overload(int, int, Attachment)
  @overload(int, int, Attachment, int)
  @overload(int, int, Attachment, int, int)
  def __init__(
      self,
      width: int,
      height: int,
      attachment: Attachment,
      target: int = 3553,
      internalFormat: int = 0,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLFramebufferObject::QOpenGLFramebufferObject(int width, int
    height, Attachment attachment, GLenum target, GLenum internalFormat)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    attachment : Attachment
      Passed on as its number.

    target : int
      Passed on as it is. May be left out, as in Qt: it is then 3553.

    internalFormat : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QOpenGLFramebufferObject::QOpenGLFramebufferObject(int width, int
    #      height, Attachment attachment, GLenum target, GLenum
    #      internalFormat)
    self._noteCreation(QOpenGLFramebufferObject, lambda: Rituals.call(
        'ritual_ZN24QOpenGLFramebufferObjectC1EiiNS_10AttachmentEjj',
        width, height, attachment.value, target, internalFormat,
    ))

  @overload(QSize, QOpenGLFramebufferObjectFormat)
  def __init__(
      self,
      size: QSize,
      format: QOpenGLFramebufferObjectFormat,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLFramebufferObject::QOpenGLFramebufferObject(const QSize &size,
    const QOpenGLFramebufferObjectFormat &format)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    format : QOpenGLFramebufferObjectFormat
      Passed on as a value: Qt reads the C++ QOpenGLFramebufferObjectFormat,
      which stays Python's own.
    """
    #  QOpenGLFramebufferObject::QOpenGLFramebufferObject(const QSize &size,
    #      const QOpenGLFramebufferObjectFormat &format)
    self._noteCreation(QOpenGLFramebufferObject, lambda: Rituals.call(
        'ritual_ZN24QOpenGLFramebufferObjectC1ERK5QSizeRK30QOpenGLFramebuff'
        'erObjectFormat',
        self._valueOf(size), self._valueOf(format),
    ))

  @overload(int, int, QOpenGLFramebufferObjectFormat)
  def __init__(
      self,
      width: int,
      height: int,
      format: QOpenGLFramebufferObjectFormat,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLFramebufferObject::QOpenGLFramebufferObject(int width, int
    height, const QOpenGLFramebufferObjectFormat &format)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    format : QOpenGLFramebufferObjectFormat
      Passed on as a value: Qt reads the C++ QOpenGLFramebufferObjectFormat,
      which stays Python's own.
    """
    #  QOpenGLFramebufferObject::QOpenGLFramebufferObject(int width, int
    #      height, const QOpenGLFramebufferObjectFormat &format)
    self._noteCreation(QOpenGLFramebufferObject, lambda: Rituals.call(
        'ritual_ZN24QOpenGLFramebufferObjectC1EiiRK30QOpenGLFramebufferObje'
        'ctFormat',
        width, height, self._valueOf(format),
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

  def d_func(self) -> Optional[QOpenGLFramebufferObjectPrivate]:
    """
    Calls Qt's 'QOpenGLFramebufferObjectPrivate
    *QOpenGLFramebufferObject::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html#d_func

    Returns
    -------

    Optional[QOpenGLFramebufferObjectPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLFramebufferObjectPrivate *QOpenGLFramebufferObject::d_func()
    address = self.uglySide.call(
        'ritual_ZN24QOpenGLFramebufferObject6d_funcEv',
    )
    from . import QOpenGLFramebufferObjectPrivate
    return QOpenGLFramebufferObjectPrivate._cuteAt(address)

  @overload(QSize)
  @overload(QSize, int)
  def addColorAttachment(self, size: QSize, internalFormat: int = 0) -> None:
    """
    Calls Qt's 'void QOpenGLFramebufferObject::addColorAttachment(const QSize
    &size, GLenum internalFormat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html#addColorAttachment

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    internalFormat : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QOpenGLFramebufferObject::addColorAttachment(const QSize &size,
    #      GLenum internalFormat)
    self.uglySide.call(
        'ritual_ZN24QOpenGLFramebufferObject18addColorAttachmentERK5QSizej',
        self._valueOf(size), internalFormat,
    )

  @overload(int, int)
  @overload(int, int, int)
  def addColorAttachment(
      self,
      width: int,
      height: int,
      internalFormat: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QOpenGLFramebufferObject::addColorAttachment(int width,
    int height, GLenum internalFormat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html#addColorAttachment

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    internalFormat : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QOpenGLFramebufferObject::addColorAttachment(int width, int
    #      height, GLenum internalFormat)
    self.uglySide.call(
        'ritual_ZN24QOpenGLFramebufferObject18addColorAttachmentEiij',
        width, height, internalFormat,
    )

  def bind(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLFramebufferObject::bind()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglframebufferobject.html#bind
    """
    #  bool QOpenGLFramebufferObject::bind()
    return self.uglySide.call('ritual_ZN24QOpenGLFramebufferObject4bindEv')

  def release(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLFramebufferObject::release()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html#release
    """
    #  bool QOpenGLFramebufferObject::release()
    return self.uglySide.call(
        'ritual_ZN24QOpenGLFramebufferObject7releaseEv',
    )

  @overload()
  def takeTexture(self) -> int:
    """
    Calls Qt's 'GLuint QOpenGLFramebufferObject::takeTexture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html#takeTexture
    """
    #  GLuint QOpenGLFramebufferObject::takeTexture()
    return self.uglySide.call(
        'ritual_ZN24QOpenGLFramebufferObject11takeTextureEv',
    )

  @overload(int)
  def takeTexture(self, colorAttachmentIndex: int) -> int:
    """
    Calls Qt's 'GLuint QOpenGLFramebufferObject::takeTexture(int
    colorAttachmentIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobject.html#takeTexture

    Parameters
    ----------

    colorAttachmentIndex : int
      Passed on as it is.
    """
    #  GLuint QOpenGLFramebufferObject::takeTexture(int colorAttachmentIndex)
    return self.uglySide.call(
        'ritual_ZN24QOpenGLFramebufferObject11takeTextureEi',
        colorAttachmentIndex,
    )

  @staticmethod
  def textures(*__, **_) -> Never:
    """
    Qt's 'QList<GLuint> QOpenGLFramebufferObject::textures() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpenGLFramebufferObject.textures' has no cute function yet. Qt's "
        "'QList<GLuint> QOpenGLFramebufferObject::textures() const': gives "
        "a type Python has no way to take yet.")
