"""
QVkRenderBuffer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhivulkan_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QVkRenderBuffer to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QRhiRenderBuffer, QRhiTexture

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QVkRenderBuffer(QRhiRenderBuffer):
  """
  The cute side of Qt's QVkRenderBuffer: a plain Python object standing in
  front of one C++ QVkRenderBuffer.

  It is built on the cute 'QRhiRenderBuffer', as Qt's QVkRenderBuffer is
  built on Qt's QRhiRenderBuffer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QVkRenderBuffer that has a ritual and that Python
  can call so far, 3 names in all: 'destroy', 'create', 'backingFormat'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVkRenderBuffer::~QVkRenderBuffer()': the destructor: Python never
    removes a C++ QVkRenderBuffer.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 leans on 'QRhiVulkan.

  What to expect
  --------------

  - The C++ QVkRenderBuffer is created at the first use, not by
    'QVkRenderBuffer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVkRenderBuffer.
  - Each name of Qt's QVkRenderBuffer that has no cute function yet,
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
  __qt_class__ = 'QVkRenderBuffer'

  #  A C++ QVkRenderBuffer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVkRenderBuffer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def backingFormat(self) -> QRhiTexture.Format:
    """
    Calls Qt's 'QRhiTexture::Format QVkRenderBuffer::backingFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvkrenderbuffer.html#backingFormat

    Returns
    -------

    QRhiTexture.Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QRhiTexture.Format(number)' gives.
    """
    #  QRhiTexture::Format QVkRenderBuffer::backingFormat() const
    ritual = 'ritual_ZNK15QVkRenderBuffer13backingFormatEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QVkRenderBuffer13backingFormatEv'
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
    Qt's 'QVkRenderBuffer::QVkRenderBuffer(QRhiImplementation *rhi, Type
    type, const QSize &pixelSize, int sampleCount, Flags flags,
    QRhiTexture::Format backingFormatHint)': leans on
    'QRhiVulkan::createTransientImage(VkFormat, QSize const&, unsigned int,
    unsigned int, VkSampleCountFlagBits, VkDeviceMemory_T**, VkImage_T**,
    VkImageView_T**, int)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QVkRenderBuffer.__init__' has no cute function yet. Qt's "
        "'QVkRenderBuffer::QVkRenderBuffer(QRhiImplementation *rhi, Type "
        "type, const QSize &pixelSize, int sampleCount, Flags flags, "
        "QRhiTexture::Format backingFormatHint)': leans on "
        "'QRhiVulkan::createTransientImage(VkFormat, QSize const&, unsigned "
        "int, unsigned int, VkSampleCountFlagBits, VkDeviceMemory_T**, "
        "VkImage_T**, VkImageView_T**, int)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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
    Calls Qt's 'void QVkRenderBuffer::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qvkrenderbuffer.html#destroy
    """
    #  void QVkRenderBuffer::destroy()
    ritual = 'ritual_ZN15QVkRenderBuffer7destroyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QVkRenderBuffer7destroyEv'
    self.uglySide.call(ritual)

  def create(self) -> bool:
    """
    Calls Qt's 'bool QVkRenderBuffer::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qvkrenderbuffer.html#create
    """
    #  bool QVkRenderBuffer::create()
    return self.uglySide.call('ritual_ZN15QVkRenderBuffer6createEv')
