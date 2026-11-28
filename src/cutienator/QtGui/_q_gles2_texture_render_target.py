"""
QGles2TextureRenderTarget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhigles2_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QGles2TextureRenderTarget to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QRhiTextureRenderTarget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QSize
  from . import QRhiRenderPassDescriptor


class QGles2TextureRenderTarget(QRhiTextureRenderTarget):
  """
  The cute side of Qt's QGles2TextureRenderTarget: a plain Python object
  standing in front of one C++ QGles2TextureRenderTarget.

  It is built on the cute 'QRhiTextureRenderTarget', as Qt's
  QGles2TextureRenderTarget is built on Qt's QRhiTextureRenderTarget, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGles2TextureRenderTarget that has a ritual and that
  Python can call so far, 6 names in all: 'destroy', 'pixelSize',
  'devicePixelRatio', 'sampleCount', 'newCompatibleRenderPassDescriptor',
  'create'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGles2TextureRenderTarget::~QGles2TextureRenderTarget()': the
    destructor: Python never removes a C++ QGles2TextureRenderTarget.

  What has no ritual
  ------------------

  1 of the 8 functions Qt declares: 1 leans on 'QRhiGles2.

  What to expect
  --------------

  - The C++ QGles2TextureRenderTarget is created at the first use, not by
    'QGles2TextureRenderTarget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGles2TextureRenderTarget.
  - Each name of Qt's QGles2TextureRenderTarget that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGles2TextureRenderTarget'

  #  A C++ QGles2TextureRenderTarget Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGles2TextureRenderTarget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def pixelSize(self) -> QSize:
    """
    Calls Qt's 'QSize QGles2TextureRenderTarget::pixelSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2texturerendertarget.html#pixelSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QGles2TextureRenderTarget::pixelSize() const
    ritual = 'ritual_ZNK25QGles2TextureRenderTarget9pixelSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QGles2TextureRenderTarget9pixelSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def devicePixelRatio(self) -> float:
    """
    Calls Qt's 'float QGles2TextureRenderTarget::devicePixelRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2texturerendertarget.html#devicePixelRatio
    """
    #  float QGles2TextureRenderTarget::devicePixelRatio() const
    ritual = 'ritual_ZNK25QGles2TextureRenderTarget16devicePixelRatioEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK25QGles2TextureRenderTarget16devicePixelRatioEv')
    return self.uglySide.call(ritual)

  def sampleCount(self) -> int:
    """
    Calls Qt's 'int QGles2TextureRenderTarget::sampleCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2texturerendertarget.html#sampleCount
    """
    #  int QGles2TextureRenderTarget::sampleCount() const
    ritual = 'ritual_ZNK25QGles2TextureRenderTarget11sampleCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QGles2TextureRenderTarget11sampleCountEv'
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'QGles2TextureRenderTarget::QGles2TextureRenderTarget(QRhiImplementation
    *rhi, const QRhiTextureRenderTargetDescription &desc, Flags flags)':
    leans on 'QRhiGles2::ensureContext(QSurface*) const', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QGles2TextureRenderTarget.__init__' has no cute function yet. "
        "Qt's "
        "'QGles2TextureRenderTarget::QGles2TextureRenderTarget(QRhiImplement"
        "ation *rhi, const QRhiTextureRenderTargetDescription &desc, Flags "
        "flags)': leans on 'QRhiGles2::ensureContext(QSurface*) const', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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
    Calls Qt's 'void QGles2TextureRenderTarget::destroy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2texturerendertarget.html#destroy
    """
    #  void QGles2TextureRenderTarget::destroy()
    ritual = 'ritual_ZN25QGles2TextureRenderTarget7destroyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QGles2TextureRenderTarget7destroyEv'
    self.uglySide.call(ritual)

  def newCompatibleRenderPassDescriptor(
      self,
  ) -> Optional[QRhiRenderPassDescriptor]:
    """
    Calls Qt's 'QRhiRenderPassDescriptor
    *QGles2TextureRenderTarget::newCompatibleRenderPassDescriptor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2texturerendertarget.html

    Returns
    -------

    Optional[QRhiRenderPassDescriptor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderPassDescriptor
    #      *QGles2TextureRenderTarget::newCompatibleRenderPassDescriptor()
    ritual = (
        'ritual_ZN25QGles2TextureRenderTarget33newCompatibleRenderPassDescr'
        'iptorEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QGles2TextureRenderTarget33newCompatibleRenderPas'
          'sDescriptorEv')
    address = self.uglySide.call(ritual)
    from . import QRhiRenderPassDescriptor
    return QRhiRenderPassDescriptor._cuteAt(address)

  def create(self) -> bool:
    """
    Calls Qt's 'bool QGles2TextureRenderTarget::create()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgles2texturerendertarget.html#create
    """
    #  bool QGles2TextureRenderTarget::create()
    return self.uglySide.call(
        'ritual_ZN25QGles2TextureRenderTarget6createEv',
    )
