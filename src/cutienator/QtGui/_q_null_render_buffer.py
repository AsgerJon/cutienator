"""
QNullRenderBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhinull_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QNullRenderBuffer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QRhiRenderBuffer, QRhiTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from . import QRhiImplementation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiImplementation = WAIT['QRhiImplementation']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNullRenderBuffer(QRhiRenderBuffer):
  """
  The cute side of Qt's QNullRenderBuffer: a plain Python object standing in
  front of one C++ QNullRenderBuffer.

  It is built on the cute 'QRhiRenderBuffer', as Qt's QNullRenderBuffer is
  built on Qt's QRhiRenderBuffer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNullRenderBuffer that has a ritual and that Python
  can call so far, 3 names in all: 'destroy', 'create', 'backingFormat'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNullRenderBuffer::~QNullRenderBuffer()': the destructor: Python
    never removes a C++ QNullRenderBuffer.

  What to expect
  --------------

  - The C++ QNullRenderBuffer is created at the first use, not by
    'QNullRenderBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNullRenderBuffer.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNullRenderBuffer'

  #  A C++ QNullRenderBuffer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNullRenderBuffer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def backingFormat(self) -> QRhiTexture.Format:
    """
    Calls Qt's 'QRhiTexture::Format QNullRenderBuffer::backingFormat()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnullrenderbuffer.html#backingFormat

    Returns
    -------

    QRhiTexture.Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhiTexture.Format(number)' gives.
    """
    #  QRhiTexture::Format QNullRenderBuffer::backingFormat() const
    ritual = 'ritual_ZNK17QNullRenderBuffer13backingFormatEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QNullRenderBuffer13backingFormatEv'
    return QRhiTexture.Format(self.uglySide.call(ritual))

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

  @overload(
      QRhiImplementation, QRhiRenderBuffer.Type, QSize, int,
      QRhiRenderBuffer.Flags, QRhiTexture.Format,
  )
  @overload(
      NoneType, QRhiRenderBuffer.Type, QSize, int, QRhiRenderBuffer.Flags,
      QRhiTexture.Format,
  )
  def __init__(
      self,
      rhi: Optional[QRhiImplementation],
      type: QRhiRenderBuffer.Type,
      pixelSize: QSize,
      sampleCount: int,
      flags: QRhiRenderBuffer.Flags,
      backingFormatHint: QRhiTexture.Format,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QNullRenderBuffer::QNullRenderBuffer(QRhiImplementation *rhi, Type type,
    const QSize &pixelSize, int sampleCount, QRhiRenderBuffer::Flags flags,
    QRhiTexture::Format backingFormatHint)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnullrenderbuffer.html#QNullRenderBuffer

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : QRhiRenderBuffer.Type
      Passed on as its number.

    pixelSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    sampleCount : int
      Passed on as it is.

    flags : QRhiRenderBuffer.Flags
      Passed on as its number.

    backingFormatHint : QRhiTexture.Format
      Passed on as its number.
    """
    #  QNullRenderBuffer::QNullRenderBuffer(QRhiImplementation *rhi, Type
    #      type, const QSize &pixelSize, int sampleCount,
    #      QRhiRenderBuffer::Flags flags, QRhiTexture::Format
    #      backingFormatHint)
    self._noteCreation(QNullRenderBuffer, lambda: Rituals.call(
        'ritual_ZN17QNullRenderBufferC1EP18QRhiImplementationN16QRhiRenderB'
        'uffer4TypeERK5QSizei6QFlagsINS2_4FlagEEN11QRhiTexture6FormatE',
        self._addressOf(rhi), type.value, self._valueOf(pixelSize),
        sampleCount, flags.value, backingFormatHint.value,
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

  def destroy(self) -> None:
    """
    Calls Qt's 'void QNullRenderBuffer::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qnullrenderbuffer.html#destroy
    """
    #  void QNullRenderBuffer::destroy()
    ritual = 'ritual_ZN17QNullRenderBuffer7destroyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QNullRenderBuffer7destroyEv'
    self.uglySide.call(ritual)

  def create(self) -> bool:
    """
    Calls Qt's 'bool QNullRenderBuffer::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qnullrenderbuffer.html#create
    """
    #  bool QNullRenderBuffer::create()
    ritual = 'ritual_ZN17QNullRenderBuffer6createEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QNullRenderBuffer6createEv'
    return self.uglySide.call(ritual)
