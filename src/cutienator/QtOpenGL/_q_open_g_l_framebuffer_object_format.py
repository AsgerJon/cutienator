"""
QOpenGLFramebufferObjectFormat binding of the Qt C++
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

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QOpenGLFramebufferObject


class QOpenGLFramebufferObjectFormat(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLFramebufferObjectFormat: a plain Python object
  standing in front of one C++ QOpenGLFramebufferObjectFormat.

  C++ hands a QOpenGLFramebufferObjectFormat around as a copy, so every C++
  QOpenGLFramebufferObjectFormat behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QOpenGLFramebufferObjectFormat that has a ritual and
  that Python can call so far, 13 names in all: 'setSamples', 'samples',
  'setMipmap', 'mipmap', 'setAttachment', 'attachment', 'setTextureTarget',
  'textureTarget', 'setInternalTextureFormat', 'internalTextureFormat',
  '__eq__', '__ne__', 'detach'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLFramebufferObjectFormat
    &QOpenGLFramebufferObjectFormat::operator=(const
    QOpenGLFramebufferObjectFormat &other)': assignment: Python binds a name
    and has no operator for it.
  - Qt's 'QOpenGLFramebufferObjectFormat::~QOpenGLFramebufferObjectFormat()':
    the destructor: Python removes its C++ QOpenGLFramebufferObjectFormat by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QOpenGLFramebufferObjectFormat is created at the first use, not
    by 'QOpenGLFramebufferObjectFormat(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpenGLFramebufferObjectFormat back gives a copy the
    ritual made for Python, in a new cute QOpenGLFramebufferObjectFormat.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLFramebufferObjectFormat'

  #  Qt's '~QOpenGLFramebufferObjectFormat()'. Naming it makes this a value
  #  class: Python owns every C++ QOpenGLFramebufferObjectFormat behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN30QOpenGLFramebufferObjectFormatD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def samples(self) -> int:
    """
    Calls Qt's 'int QOpenGLFramebufferObjectFormat::samples() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobjectformat.html#samples
    """
    #  int QOpenGLFramebufferObjectFormat::samples() const
    return self.uglySide.call(
        'ritual_ZNK30QOpenGLFramebufferObjectFormat7samplesEv',
    )

  def mipmap(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLFramebufferObjectFormat::mipmap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobjectformat.html#mipmap
    """
    #  bool QOpenGLFramebufferObjectFormat::mipmap() const
    return self.uglySide.call(
        'ritual_ZNK30QOpenGLFramebufferObjectFormat6mipmapEv',
    )

  def attachment(self) -> QOpenGLFramebufferObject.Attachment:
    """
    Calls Qt's 'QOpenGLFramebufferObject::Attachment
    QOpenGLFramebufferObjectFormat::attachment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobjectformat.html#attachment

    Returns
    -------

    QOpenGLFramebufferObject.Attachment
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QOpenGLFramebufferObject.Attachment(number)' gives.
    """
    #  QOpenGLFramebufferObject::Attachment
    #      QOpenGLFramebufferObjectFormat::attachment() const
    return QOpenGLFramebufferObject.Attachment(self.uglySide.call(
        'ritual_ZNK30QOpenGLFramebufferObjectFormat10attachmentEv',
    ))

  def textureTarget(self) -> int:
    """
    Calls Qt's 'GLenum QOpenGLFramebufferObjectFormat::textureTarget()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobjectformat.html#textureTarget
    """
    #  GLenum QOpenGLFramebufferObjectFormat::textureTarget() const
    return self.uglySide.call(
        'ritual_ZNK30QOpenGLFramebufferObjectFormat13textureTargetEv',
    )

  def internalTextureFormat(self) -> int:
    """
    Calls Qt's 'GLenum
    QOpenGLFramebufferObjectFormat::internalTextureFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobjectformat.html
    """
    #  GLenum QOpenGLFramebufferObjectFormat::internalTextureFormat() const
    return self.uglySide.call(
        'ritual_ZNK30QOpenGLFramebufferObjectFormat21internalTextureFormatE'
        'v',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setSamples(self, samples: int) -> None:
    """
    Calls Qt's 'void QOpenGLFramebufferObjectFormat::setSamples(int
    samples)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobjectformat.html#setSamples

    Parameters
    ----------

    samples : int
      Passed on as it is.
    """
    #  void QOpenGLFramebufferObjectFormat::setSamples(int samples)
    self.uglySide.call(
        'ritual_ZN30QOpenGLFramebufferObjectFormat10setSamplesEi', samples,
    )

  @overload(bool)
  def setMipmap(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QOpenGLFramebufferObjectFormat::setMipmap(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobjectformat.html#setMipmap

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QOpenGLFramebufferObjectFormat::setMipmap(bool enabled)
    self.uglySide.call(
        'ritual_ZN30QOpenGLFramebufferObjectFormat9setMipmapEb', enabled,
    )

  @overload(QOpenGLFramebufferObject.Attachment)
  def setAttachment(
      self,
      attachment: QOpenGLFramebufferObject.Attachment,
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLFramebufferObjectFormat::setAttachment(QOpenGLFramebufferObject::
    Attachment attachment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobjectformat.html#setAttachment

    Parameters
    ----------

    attachment : QOpenGLFramebufferObject.Attachment
      Passed on as its number.
    """
    #  void QOpenGLFramebufferObjectFormat::setAttachment(
    #      QOpenGLFramebufferObject::Attachment attachment)
    self.uglySide.call(
        'ritual_ZN30QOpenGLFramebufferObjectFormat13setAttachmentEN24QOpenG'
        'LFramebufferObject10AttachmentE',
        attachment.value,
    )

  @overload(int)
  def setTextureTarget(self, target: int) -> None:
    """
    Calls Qt's 'void QOpenGLFramebufferObjectFormat::setTextureTarget(GLenum
    target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobjectformat.html

    Parameters
    ----------

    target : int
      Passed on as it is.
    """
    #  void QOpenGLFramebufferObjectFormat::setTextureTarget(GLenum target)
    self.uglySide.call(
        'ritual_ZN30QOpenGLFramebufferObjectFormat16setTextureTargetEj',
        target,
    )

  @overload(int)
  def setInternalTextureFormat(self, internalTextureFormat: int) -> None:
    """
    Calls Qt's 'void
    QOpenGLFramebufferObjectFormat::setInternalTextureFormat(GLenum
    internalTextureFormat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobjectformat.html

    Parameters
    ----------

    internalTextureFormat : int
      Passed on as it is.
    """
    #  void QOpenGLFramebufferObjectFormat::setInternalTextureFormat(GLenum
    #      internalTextureFormat)
    self.uglySide.call(
        'ritual_ZN30QOpenGLFramebufferObjectFormat24setInternalTextureForma'
        'tEj',
        internalTextureFormat,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QOpenGLFramebufferObjectFormat) -> bool:
    """
    Calls Qt's 'bool QOpenGLFramebufferObjectFormat::operator==(const
    QOpenGLFramebufferObjectFormat &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobjectformat.html#operator==

    Parameters
    ----------

    other : QOpenGLFramebufferObjectFormat
      Passed on as a value: Qt reads the C++ QOpenGLFramebufferObjectFormat,
      which stays Python's own.
    """
    #  bool QOpenGLFramebufferObjectFormat::operator==(const
    #      QOpenGLFramebufferObjectFormat &other) const
    return self.uglySide.call(
        'ritual_ZNK30QOpenGLFramebufferObjectFormateqERKS_',
        self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, other: QOpenGLFramebufferObjectFormat) -> bool:
    """
    Calls Qt's 'bool QOpenGLFramebufferObjectFormat::operator!=(const
    QOpenGLFramebufferObjectFormat &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobjectformat.html#operator!=

    Parameters
    ----------

    other : QOpenGLFramebufferObjectFormat
      Passed on as a value: Qt reads the C++ QOpenGLFramebufferObjectFormat,
      which stays Python's own.
    """
    #  bool QOpenGLFramebufferObjectFormat::operator!=(const
    #      QOpenGLFramebufferObjectFormat &other) const
    return self.uglySide.call(
        'ritual_ZNK30QOpenGLFramebufferObjectFormatneERKS_',
        self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLFramebufferObjectFormat::QOpenGLFramebufferObjectFormat()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobjectformat.html
    """
    #  QOpenGLFramebufferObjectFormat::QOpenGLFramebufferObjectFormat()
    self._noteCreation(QOpenGLFramebufferObjectFormat, lambda: Rituals.call(
        'ritual_ZN30QOpenGLFramebufferObjectFormatC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QOpenGLFramebufferObjectFormat) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLFramebufferObjectFormat::QOpenGLFramebufferObjectFormat(const
    QOpenGLFramebufferObjectFormat &other)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobjectformat.html

    Parameters
    ----------

    other : QOpenGLFramebufferObjectFormat
      Passed on as a value: Qt reads the C++ QOpenGLFramebufferObjectFormat,
      which stays Python's own.
    """
    #  QOpenGLFramebufferObjectFormat::QOpenGLFramebufferObjectFormat(const
    #      QOpenGLFramebufferObjectFormat &other)
    self._noteCreation(QOpenGLFramebufferObjectFormat, lambda: Rituals.call(
        'ritual_ZN30QOpenGLFramebufferObjectFormatC1ERKS_',
        self._valueOf(other),
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

  def detach(self) -> None:
    """
    Calls Qt's 'void QOpenGLFramebufferObjectFormat::detach()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglframebufferobjectformat.html#detach
    """
    #  void QOpenGLFramebufferObjectFormat::detach()
    self.uglySide.call('ritual_ZN30QOpenGLFramebufferObjectFormat6detachEv')
