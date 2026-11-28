"""
QNullTextureRenderTarget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhinull_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QNullTextureRenderTarget to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QRhiTextureRenderTarget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from . import QRhiImplementation, QRhiRenderPassDescriptor
  from . import QRhiTextureRenderTargetDescription
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiImplementation = WAIT['QRhiImplementation']
  QRhiTextureRenderTargetDescription = WAIT['QRhiTextureRenderTargetDescription']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNullTextureRenderTarget(QRhiTextureRenderTarget):
  """
  The cute side of Qt's QNullTextureRenderTarget: a plain Python object
  standing in front of one C++ QNullTextureRenderTarget.

  It is built on the cute 'QRhiTextureRenderTarget', as Qt's
  QNullTextureRenderTarget is built on Qt's QRhiTextureRenderTarget, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QNullTextureRenderTarget that has a ritual and that
  Python can call so far, 6 names in all: 'destroy', 'pixelSize',
  'devicePixelRatio', 'sampleCount', 'newCompatibleRenderPassDescriptor',
  'create'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QNullTextureRenderTarget::~QNullTextureRenderTarget()': the
    destructor: Python never removes a C++ QNullTextureRenderTarget.

  What to expect
  --------------

  - The C++ QNullTextureRenderTarget is created at the first use, not by
    'QNullTextureRenderTarget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNullTextureRenderTarget.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNullTextureRenderTarget'

  #  A C++ QNullTextureRenderTarget Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNullTextureRenderTarget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def pixelSize(self) -> QSize:
    """
    Calls Qt's 'QSize QNullTextureRenderTarget::pixelSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnulltexturerendertarget.html#pixelSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QNullTextureRenderTarget::pixelSize() const
    ritual = 'ritual_ZNK24QNullTextureRenderTarget9pixelSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QNullTextureRenderTarget9pixelSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def devicePixelRatio(self) -> float:
    """
    Calls Qt's 'float QNullTextureRenderTarget::devicePixelRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnulltexturerendertarget.html#devicePixelRatio
    """
    #  float QNullTextureRenderTarget::devicePixelRatio() const
    ritual = 'ritual_ZNK24QNullTextureRenderTarget16devicePixelRatioEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QNullTextureRenderTarget16devicePixelRatioEv'
    return self.uglySide.call(ritual)

  def sampleCount(self) -> int:
    """
    Calls Qt's 'int QNullTextureRenderTarget::sampleCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnulltexturerendertarget.html#sampleCount
    """
    #  int QNullTextureRenderTarget::sampleCount() const
    ritual = 'ritual_ZNK24QNullTextureRenderTarget11sampleCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QNullTextureRenderTarget11sampleCountEv'
    return self.uglySide.call(ritual)

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
      QRhiImplementation, QRhiTextureRenderTargetDescription,
      QRhiTextureRenderTarget.Flags,
  )
  @overload(
      NoneType, QRhiTextureRenderTargetDescription,
      QRhiTextureRenderTarget.Flags,
  )
  def __init__(
      self,
      rhi: Optional[QRhiImplementation],
      desc: QRhiTextureRenderTargetDescription,
      flags: QRhiTextureRenderTarget.Flags,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QNullTextureRenderTarget::QNullTextureRenderTarget(QRhiImplementation
    *rhi, const QRhiTextureRenderTargetDescription &desc, Flags flags)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnulltexturerendertarget.html

    Parameters
    ----------

    rhi : Optional[QRhiImplementation]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    desc : QRhiTextureRenderTargetDescription
      Passed on as a value: Qt reads the C++
      QRhiTextureRenderTargetDescription, which stays Python's own.

    flags : QRhiTextureRenderTarget.Flags
      Passed on as its number.
    """
    #  QNullTextureRenderTarget::QNullTextureRenderTarget(QRhiImplementation
    #      *rhi, const QRhiTextureRenderTargetDescription &desc, Flags flags)
    self._noteCreation(QNullTextureRenderTarget, lambda: Rituals.call(
        'ritual_ZN24QNullTextureRenderTargetC1EP18QRhiImplementationRK34QRh'
        'iTextureRenderTargetDescription6QFlagsIN23QRhiTextureRenderTarget4'
        'FlagEE',
        self._addressOf(rhi), self._valueOf(desc), flags.value,
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
    Calls Qt's 'void QNullTextureRenderTarget::destroy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnulltexturerendertarget.html#destroy
    """
    #  void QNullTextureRenderTarget::destroy()
    ritual = 'ritual_ZN24QNullTextureRenderTarget7destroyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QNullTextureRenderTarget7destroyEv'
    self.uglySide.call(ritual)

  def newCompatibleRenderPassDescriptor(
      self,
  ) -> Optional[QRhiRenderPassDescriptor]:
    """
    Calls Qt's 'QRhiRenderPassDescriptor
    *QNullTextureRenderTarget::newCompatibleRenderPassDescriptor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnulltexturerendertarget.html

    Returns
    -------

    Optional[QRhiRenderPassDescriptor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderPassDescriptor
    #      *QNullTextureRenderTarget::newCompatibleRenderPassDescriptor()
    ritual = (
        'ritual_ZN24QNullTextureRenderTarget33newCompatibleRenderPassDescri'
        'ptorEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QNullTextureRenderTarget33newCompatibleRenderPass'
          'DescriptorEv')
    address = self.uglySide.call(ritual)
    from . import QRhiRenderPassDescriptor
    return QRhiRenderPassDescriptor._cuteAt(address)

  def create(self) -> bool:
    """
    Calls Qt's 'bool QNullTextureRenderTarget::create()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnulltexturerendertarget.html#create
    """
    #  bool QNullTextureRenderTarget::create()
    ritual = 'ritual_ZN24QNullTextureRenderTarget6createEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QNullTextureRenderTarget6createEv'
    return self.uglySide.call(ritual)
