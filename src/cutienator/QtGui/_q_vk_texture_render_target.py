"""
QVkTextureRenderTarget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qrhivulkan_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QVkTextureRenderTarget to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QRhiTextureRenderTarget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QSize
  from . import QRhiRenderPassDescriptor


class QVkTextureRenderTarget(QRhiTextureRenderTarget):
  """
  The cute side of Qt's QVkTextureRenderTarget: a plain Python object
  standing in front of one C++ QVkTextureRenderTarget.

  It is built on the cute 'QRhiTextureRenderTarget', as Qt's
  QVkTextureRenderTarget is built on Qt's QRhiTextureRenderTarget, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QVkTextureRenderTarget that has a ritual and that
  Python can call so far, 6 names in all: 'destroy', 'pixelSize',
  'devicePixelRatio', 'sampleCount', 'newCompatibleRenderPassDescriptor',
  'create'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVkTextureRenderTarget::~QVkTextureRenderTarget()': the destructor:
    Python never removes a C++ QVkTextureRenderTarget.

  What has no ritual
  ------------------

  1 of the 8 functions Qt declares: 1 leans on 'QVkTextureRenderTarget.

  What to expect
  --------------

  - The C++ QVkTextureRenderTarget is created at the first use, not by
    'QVkTextureRenderTarget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVkTextureRenderTarget.
  - Each name of Qt's QVkTextureRenderTarget that has no cute function yet,
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
  __qt_class__ = 'QVkTextureRenderTarget'

  #  A C++ QVkTextureRenderTarget Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVkTextureRenderTarget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def pixelSize(self) -> QSize:
    """
    Calls Qt's 'QSize QVkTextureRenderTarget::pixelSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvktexturerendertarget.html#pixelSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QVkTextureRenderTarget::pixelSize() const
    ritual = 'ritual_ZNK22QVkTextureRenderTarget9pixelSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QVkTextureRenderTarget9pixelSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def devicePixelRatio(self) -> float:
    """
    Calls Qt's 'float QVkTextureRenderTarget::devicePixelRatio() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvktexturerendertarget.html#devicePixelRatio
    """
    #  float QVkTextureRenderTarget::devicePixelRatio() const
    ritual = 'ritual_ZNK22QVkTextureRenderTarget16devicePixelRatioEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QVkTextureRenderTarget16devicePixelRatioEv'
    return self.uglySide.call(ritual)

  def sampleCount(self) -> int:
    """
    Calls Qt's 'int QVkTextureRenderTarget::sampleCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvktexturerendertarget.html#sampleCount
    """
    #  int QVkTextureRenderTarget::sampleCount() const
    ritual = 'ritual_ZNK22QVkTextureRenderTarget11sampleCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QVkTextureRenderTarget11sampleCountEv'
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
    Qt's 'QVkTextureRenderTarget::QVkTextureRenderTarget(QRhiImplementation
    *rhi, const QRhiTextureRenderTargetDescription &desc, Flags flags)':
    leans on 'QVkTextureRenderTarget::create()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QVkTextureRenderTarget.__init__' has no cute function yet. Qt's "
        "'QVkTextureRenderTarget::QVkTextureRenderTarget(QRhiImplementation "
        "*rhi, const QRhiTextureRenderTargetDescription &desc, Flags "
        "flags)': leans on 'QVkTextureRenderTarget::create()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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
    Calls Qt's 'void QVkTextureRenderTarget::destroy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvktexturerendertarget.html#destroy
    """
    #  void QVkTextureRenderTarget::destroy()
    ritual = 'ritual_ZN22QVkTextureRenderTarget7destroyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QVkTextureRenderTarget7destroyEv'
    self.uglySide.call(ritual)

  def newCompatibleRenderPassDescriptor(
      self,
  ) -> Optional[QRhiRenderPassDescriptor]:
    """
    Calls Qt's 'QRhiRenderPassDescriptor
    *QVkTextureRenderTarget::newCompatibleRenderPassDescriptor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvktexturerendertarget.html

    Returns
    -------

    Optional[QRhiRenderPassDescriptor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderPassDescriptor
    #      *QVkTextureRenderTarget::newCompatibleRenderPassDescriptor()
    address = self.uglySide.call(
        'ritual_ZN22QVkTextureRenderTarget33newCompatibleRenderPassDescript'
        'orEv',
    )
    from . import QRhiRenderPassDescriptor
    return QRhiRenderPassDescriptor._cuteAt(address)

  def create(self) -> bool:
    """
    Calls Qt's 'bool QVkTextureRenderTarget::create()'.

    Qt's own words: https://doc.qt.io/qt-6/qvktexturerendertarget.html#create
    """
    #  bool QVkTextureRenderTarget::create()
    return self.uglySide.call('ritual_ZN22QVkTextureRenderTarget6createEv')
