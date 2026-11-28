"""
QGles2RenderBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhigles2_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QGles2RenderBuffer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QRhiRenderBuffer, QRhiTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QGles2RenderBuffer(QRhiRenderBuffer):
  """
  The cute side of Qt's QGles2RenderBuffer: a plain Python object standing in
  front of one C++ QGles2RenderBuffer.

  It is built on the cute 'QRhiRenderBuffer', as Qt's QGles2RenderBuffer is
  built on Qt's QRhiRenderBuffer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGles2RenderBuffer that has a ritual and that Python
  can call so far, 4 names in all: 'destroy', 'create', 'createFrom',
  'backingFormat'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGles2RenderBuffer::~QGles2RenderBuffer()': the destructor: Python
    never removes a C++ QGles2RenderBuffer.

  What has no ritual
  ------------------

  1 of the 6 functions Qt declares: 1 leans on 'QRHI_LOG_INFO()', which Qt's
  source does not mark for use from outside Qt and has no code for that could
  be taken.

  What to expect
  --------------

  - The C++ QGles2RenderBuffer is created at the first use, not by
    'QGles2RenderBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGles2RenderBuffer.
  - Each name of Qt's QGles2RenderBuffer that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGles2RenderBuffer'

  #  A C++ QGles2RenderBuffer Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGles2RenderBuffer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def backingFormat(self) -> QRhiTexture.Format:
    """
    Calls Qt's 'QRhiTexture::Format QGles2RenderBuffer::backingFormat()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2renderbuffer.html#backingFormat

    Returns
    -------

    QRhiTexture.Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhiTexture.Format(number)' gives.
    """
    #  QRhiTexture::Format QGles2RenderBuffer::backingFormat() const
    ritual = 'ritual_ZNK18QGles2RenderBuffer13backingFormatEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QGles2RenderBuffer13backingFormatEv'
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QGles2RenderBuffer::QGles2RenderBuffer(QRhiImplementation *rhi,
    Type type, const QSize &pixelSize, int sampleCount,
    QRhiRenderBuffer::Flags flags, QRhiTexture::Format backingFormatHint)':
    leans on 'QRHI_LOG_INFO()', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGles2RenderBuffer.__init__' has no cute function yet. Qt's "
        "'QGles2RenderBuffer::QGles2RenderBuffer(QRhiImplementation *rhi, "
        "Type type, const QSize &pixelSize, int sampleCount, "
        "QRhiRenderBuffer::Flags flags, QRhiTexture::Format "
        "backingFormatHint)': leans on 'QRHI_LOG_INFO()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

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
    Calls Qt's 'void QGles2RenderBuffer::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qgles2renderbuffer.html#destroy
    """
    #  void QGles2RenderBuffer::destroy()
    ritual = 'ritual_ZN18QGles2RenderBuffer7destroyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QGles2RenderBuffer7destroyEv'
    self.uglySide.call(ritual)

  def create(self) -> bool:
    """
    Calls Qt's 'bool QGles2RenderBuffer::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qgles2renderbuffer.html#create
    """
    #  bool QGles2RenderBuffer::create()
    return self.uglySide.call('ritual_ZN18QGles2RenderBuffer6createEv')

  @overload(QRhiRenderBuffer.NativeRenderBuffer)
  def createFrom(self, src: QRhiRenderBuffer.NativeRenderBuffer) -> bool:
    """
    Calls Qt's 'bool QGles2RenderBuffer::createFrom(NativeRenderBuffer src)'.

    Qt's own words: https://doc.qt.io/qt-6/qgles2renderbuffer.html#createFrom

    Parameters
    ----------

    src : QRhiRenderBuffer.NativeRenderBuffer
      Passed on as a value: Qt reads the C++
      QRhiRenderBuffer::NativeRenderBuffer, which stays Python's own.
    """
    #  bool QGles2RenderBuffer::createFrom(NativeRenderBuffer src)
    return self.uglySide.call(
        'ritual_ZN18QGles2RenderBuffer10createFromEN16QRhiRenderBuffer18Nat'
        'iveRenderBufferE',
        self._valueOf(src),
    )
