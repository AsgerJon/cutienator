"""
QRhiWidgetPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qrhiwidget_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QRhiWidgetPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtGui import QPlatformTextureList
from . import QWidgetPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QImage, QPlatformBackingStoreRhiConfig
  from ..QtGui import QRhiCommandBuffer
  from . import QRhiWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiCommandBuffer = WAIT['QRhiCommandBuffer']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRhiWidgetPrivate(QWidgetPrivate):
  """
  The cute side of Qt's QRhiWidgetPrivate: a plain Python object standing in
  front of one C++ QRhiWidgetPrivate.

  It is built on the cute 'QWidgetPrivate', as Qt's QRhiWidgetPrivate is
  built on Qt's QWidgetPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRhiWidgetPrivate that has a ritual and that Python
  can call so far, 12 names in all: 'q_func', 'texture', 'textureListFlags',
  'rhiConfig', 'endCompose', 'grabFramebuffer', 'init', 'ensureRhi',
  'invokeInitialize', 'resetColorBufferObjects', 'resetRenderTargetObjects',
  'releaseResources'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QRhiWidget *QRhiWidgetPrivate::q_func() const': takes in
    Python what 'QRhiWidget *QRhiWidgetPrivate::q_func()' takes.
  - Qt's 'void QRhiWidgetPrivate::ensureTexture(bool *changed)': takes a
    number to change where it is.

  What to expect
  --------------

  - The C++ QRhiWidgetPrivate is created at the first use, not by
    'QRhiWidgetPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRhiWidgetPrivate.
  - Each name of Qt's QRhiWidgetPrivate that has no cute function yet,
    'ensureTexture', holds a function that raises 'NotImplementedError', and
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
  __qt_class__ = 'QRhiWidgetPrivate'

  #  A C++ QRhiWidgetPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRhiWidgetPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def texture(self) -> QWidgetPrivate.TextureData:
    """
    Calls Qt's 'TextureData QRhiWidgetPrivate::texture() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidgetprivate.html#texture

    Returns
    -------

    QWidgetPrivate.TextureData
      A new cute QWidgetPrivate::TextureData around the copy Qt gave back.
      Python owns it.
    """
    #  TextureData QRhiWidgetPrivate::texture() const
    ritual = 'ritual_ZNK17QRhiWidgetPrivate7textureEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QRhiWidgetPrivate7textureEv'
    address = self.uglySide.call(ritual)
    return QWidgetPrivate.TextureData._cuteOwning(address)

  def rhiConfig(self) -> QPlatformBackingStoreRhiConfig:
    """
    Calls Qt's 'QPlatformBackingStoreRhiConfig QRhiWidgetPrivate::rhiConfig()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidgetprivate.html#rhiConfig

    Returns
    -------

    QPlatformBackingStoreRhiConfig
      A new cute QPlatformBackingStoreRhiConfig around the copy Qt gave back.
      Python owns it.
    """
    #  QPlatformBackingStoreRhiConfig QRhiWidgetPrivate::rhiConfig() const
    ritual = 'ritual_ZNK17QRhiWidgetPrivate9rhiConfigEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QRhiWidgetPrivate9rhiConfigEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPlatformBackingStoreRhiConfig
    return QPlatformBackingStoreRhiConfig._cuteOwning(address)

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

  def q_func(self) -> Optional[QRhiWidget]:
    """
    Calls Qt's 'QRhiWidget *QRhiWidgetPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidgetprivate.html#q_func

    Returns
    -------

    Optional[QRhiWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiWidget *QRhiWidgetPrivate::q_func()
    address = self.uglySide.call('ritual_ZN17QRhiWidgetPrivate6q_funcEv')
    from . import QRhiWidget
    return QRhiWidget._cuteAt(address)

  def textureListFlags(self) -> QPlatformTextureList.Flags:
    """
    Calls Qt's 'QPlatformTextureList::Flags
    QRhiWidgetPrivate::textureListFlags()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiwidgetprivate.html#textureListFlags

    Returns
    -------

    QPlatformTextureList.Flags
      The value standing for the combination Qt gave back.
    """
    #  QPlatformTextureList::Flags QRhiWidgetPrivate::textureListFlags()
    ritual = 'ritual_ZN17QRhiWidgetPrivate16textureListFlagsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QRhiWidgetPrivate16textureListFlagsEv'
    return QPlatformTextureList.Flags(self.uglySide.call(ritual))

  def endCompose(self) -> None:
    """
    Calls Qt's 'void QRhiWidgetPrivate::endCompose()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidgetprivate.html#endCompose
    """
    #  void QRhiWidgetPrivate::endCompose()
    ritual = 'ritual_ZN17QRhiWidgetPrivate10endComposeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QRhiWidgetPrivate10endComposeEv'
    self.uglySide.call(ritual)

  def grabFramebuffer(self) -> QImage:
    """
    Calls Qt's 'QImage QRhiWidgetPrivate::grabFramebuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiwidgetprivate.html#grabFramebuffer

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QRhiWidgetPrivate::grabFramebuffer()
    ritual = 'ritual_ZN17QRhiWidgetPrivate15grabFramebufferEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QRhiWidgetPrivate15grabFramebufferEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QRhiWidgetPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidgetprivate.html#init
    """
    #  void QRhiWidgetPrivate::init()
    self.uglySide.call('ritual_ZN17QRhiWidgetPrivate4initEv')

  def ensureRhi(self) -> None:
    """
    Calls Qt's 'void QRhiWidgetPrivate::ensureRhi()'.

    Qt's own words: https://doc.qt.io/qt-6/qrhiwidgetprivate.html#ensureRhi
    """
    #  void QRhiWidgetPrivate::ensureRhi()
    self.uglySide.call('ritual_ZN17QRhiWidgetPrivate9ensureRhiEv')

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def invokeInitialize(self, cb: Optional[QRhiCommandBuffer]) -> bool:
    """
    Calls Qt's 'bool QRhiWidgetPrivate::invokeInitialize(QRhiCommandBuffer
    *cb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiwidgetprivate.html#invokeInitialize

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QRhiWidgetPrivate::invokeInitialize(QRhiCommandBuffer *cb)
    return self.uglySide.call(
        'ritual_ZN17QRhiWidgetPrivate16invokeInitializeEP17QRhiCommandBuffe'
        'r',
        self._addressOf(cb),
    )

  def resetColorBufferObjects(self) -> None:
    """
    Calls Qt's 'void QRhiWidgetPrivate::resetColorBufferObjects()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiwidgetprivate.html#resetColorBufferObjects
    """
    #  void QRhiWidgetPrivate::resetColorBufferObjects()
    self.uglySide.call(
        'ritual_ZN17QRhiWidgetPrivate23resetColorBufferObjectsEv',
    )

  def resetRenderTargetObjects(self) -> None:
    """
    Calls Qt's 'void QRhiWidgetPrivate::resetRenderTargetObjects()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiwidgetprivate.html#resetRenderTargetObjects
    """
    #  void QRhiWidgetPrivate::resetRenderTargetObjects()
    self.uglySide.call(
        'ritual_ZN17QRhiWidgetPrivate24resetRenderTargetObjectsEv',
    )

  def releaseResources(self) -> None:
    """
    Calls Qt's 'void QRhiWidgetPrivate::releaseResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhiwidgetprivate.html#releaseResources
    """
    #  void QRhiWidgetPrivate::releaseResources()
    self.uglySide.call('ritual_ZN17QRhiWidgetPrivate16releaseResourcesEv')

  @staticmethod
  def ensureTexture(*__, **_) -> Never:
    """
    Qt's 'void QRhiWidgetPrivate::ensureTexture(bool *changed)': takes a
    number to change where it is.
    """
    raise NotImplementedError(
        "'QRhiWidgetPrivate.ensureTexture' has no cute function yet. Qt's "
        "'void QRhiWidgetPrivate::ensureTexture(bool *changed)': takes a "
        "number to change where it is.")
