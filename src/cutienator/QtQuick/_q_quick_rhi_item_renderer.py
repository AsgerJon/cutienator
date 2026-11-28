"""
QQuickRhiItemRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qquickrhiitem.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QRhi, QRhiCommandBuffer, QRhiRenderBuffer
  from ..QtGui import QRhiRenderTarget, QRhiTexture
  from . import QQuickRhiItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickRhiItem = WAIT['QQuickRhiItem']
  QRhiCommandBuffer = WAIT['QRhiCommandBuffer']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickRhiItemRenderer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickRhiItemRenderer: a plain Python object standing
  in front of one C++ QQuickRhiItemRenderer.

  What exists
  -----------

  Every function of Qt's QQuickRhiItemRenderer that has a ritual and that
  Python can call so far, 10 names in all: 'initialize', 'synchronize',
  'render', 'update', 'rhi', 'colorTexture', 'msaaColorBuffer',
  'resolveTexture', 'depthStencilBuffer', 'renderTarget'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickRhiItemRenderer::~QQuickRhiItemRenderer()': the destructor:
    Python never removes a C++ QQuickRhiItemRenderer.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QQuickRhiItemRenderer is created at the first use, not by
    'QQuickRhiItemRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickRhiItemRenderer.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickRhiItemRenderer'

  #  A C++ QQuickRhiItemRenderer Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickRhiItemRenderer'

  #  The functions Qt calls itself that QQuickRhiItemRenderer is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'initialize': (
          ('_ZN21QQuickRhiItemRenderer10initializeEP17QRhiCommandBuffer',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
           )),
      ),
      'synchronize': (
          ('_ZN21QQuickRhiItemRenderer11synchronizeEP13QQuickRhiItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickRhiItem'),
           )),
      ),
      'render': (
          ('_ZN21QQuickRhiItemRenderer6renderEP17QRhiCommandBuffer',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QRhiCommandBuffer'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def rhi(self) -> Optional[QRhi]:
    """
    Calls Qt's 'QRhi *QQuickRhiItemRenderer::rhi() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrhiitemrenderer.html#rhi

    Returns
    -------

    Optional[QRhi]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhi *QQuickRhiItemRenderer::rhi() const
    address = self.uglySide.call('ritual_ZNK21QQuickRhiItemRenderer3rhiEv')
    from ..QtGui import QRhi
    return QRhi._cuteAt(address)

  def colorTexture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QQuickRhiItemRenderer::colorTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitemrenderer.html#colorTexture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QQuickRhiItemRenderer::colorTexture() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickRhiItemRenderer12colorTextureEv',
    )
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  def msaaColorBuffer(self) -> Optional[QRhiRenderBuffer]:
    """
    Calls Qt's 'QRhiRenderBuffer *QQuickRhiItemRenderer::msaaColorBuffer()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitemrenderer.html#msaaColorBuffer

    Returns
    -------

    Optional[QRhiRenderBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderBuffer *QQuickRhiItemRenderer::msaaColorBuffer() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickRhiItemRenderer15msaaColorBufferEv',
    )
    from ..QtGui import QRhiRenderBuffer
    return QRhiRenderBuffer._cuteAt(address)

  def resolveTexture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QQuickRhiItemRenderer::resolveTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitemrenderer.html#resolveTexture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QQuickRhiItemRenderer::resolveTexture() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickRhiItemRenderer14resolveTextureEv',
    )
    from ..QtGui import QRhiTexture
    return QRhiTexture._cuteAt(address)

  def depthStencilBuffer(self) -> Optional[QRhiRenderBuffer]:
    """
    Calls Qt's 'QRhiRenderBuffer *QQuickRhiItemRenderer::depthStencilBuffer()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitemrenderer.html#depthStencilBuffer

    Returns
    -------

    Optional[QRhiRenderBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderBuffer *QQuickRhiItemRenderer::depthStencilBuffer() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickRhiItemRenderer18depthStencilBufferEv',
    )
    from ..QtGui import QRhiRenderBuffer
    return QRhiRenderBuffer._cuteAt(address)

  def renderTarget(self) -> Optional[QRhiRenderTarget]:
    """
    Calls Qt's 'QRhiRenderTarget *QQuickRhiItemRenderer::renderTarget()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitemrenderer.html#renderTarget

    Returns
    -------

    Optional[QRhiRenderTarget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderTarget *QQuickRhiItemRenderer::renderTarget() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickRhiItemRenderer12renderTargetEv',
    )
    from ..QtGui import QRhiRenderTarget
    return QRhiRenderTarget._cuteAt(address)

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
    'QQuickRhiItemRenderer::QQuickRhiItemRenderer()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitemrenderer.html#QQuickRhiItemRenderer
    """
    #  QQuickRhiItemRenderer::QQuickRhiItemRenderer()
    self._noteCreation(QQuickRhiItemRenderer, lambda: Rituals.call(
        'ritual_ZN21QQuickRhiItemRendererC1Ev',
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

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def initialize(self, cb: Optional[QRhiCommandBuffer]) -> None:
    """
    Calls Qt's 'void QQuickRhiItemRenderer::initialize(QRhiCommandBuffer
    *cb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitemrenderer.html#initialize

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRhiItemRenderer::initialize(QRhiCommandBuffer *cb)
    self.uglySide.call(
        'ritual_ZN21QQuickRhiItemRenderer10initializeEP17QRhiCommandBuffer',
        self._addressOf(cb),
    )

  @overload(QQuickRhiItem)
  @overload(NoneType)
  def synchronize(self, item: Optional[QQuickRhiItem]) -> None:
    """
    Calls Qt's 'void QQuickRhiItemRenderer::synchronize(QQuickRhiItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrhiitemrenderer.html#synchronize

    Parameters
    ----------

    item : Optional[QQuickRhiItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRhiItemRenderer::synchronize(QQuickRhiItem *item)
    self.uglySide.call(
        'ritual_ZN21QQuickRhiItemRenderer11synchronizeEP13QQuickRhiItem',
        self._addressOf(item),
    )

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def render(self, cb: Optional[QRhiCommandBuffer]) -> None:
    """
    Calls Qt's 'void QQuickRhiItemRenderer::render(QRhiCommandBuffer *cb)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrhiitemrenderer.html#render

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRhiItemRenderer::render(QRhiCommandBuffer *cb)
    self.uglySide.call(
        'ritual_ZN21QQuickRhiItemRenderer6renderEP17QRhiCommandBuffer',
        self._addressOf(cb),
    )

  def update(self) -> None:
    """
    Calls Qt's 'void QQuickRhiItemRenderer::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrhiitemrenderer.html#update
    """
    #  void QQuickRhiItemRenderer::update()
    self.uglySide.call('ritual_ZN21QQuickRhiItemRenderer6updateEv')
