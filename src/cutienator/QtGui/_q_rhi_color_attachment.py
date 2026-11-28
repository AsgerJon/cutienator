"""
QRhiColorAttachment binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QRhiRenderBuffer, QRhiTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiRenderBuffer = WAIT['QRhiRenderBuffer']
  QRhiTexture = WAIT['QRhiTexture']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRhiColorAttachment(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRhiColorAttachment: a plain Python object standing
  in front of one C++ QRhiColorAttachment.

  C++ hands a QRhiColorAttachment around as a copy, so every C++
  QRhiColorAttachment behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QRhiColorAttachment that has a ritual and that
  Python can call so far, 16 names in all: 'texture', 'setTexture',
  'renderBuffer', 'setRenderBuffer', 'layer', 'setLayer', 'level',
  'setLevel', 'resolveTexture', 'setResolveTexture', 'resolveLayer',
  'setResolveLayer', 'resolveLevel', 'setResolveLevel', 'multiViewCount',
  'setMultiViewCount'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRhiColorAttachment::~QRhiColorAttachment()': the destructor:
    Python removes its C++ QRhiColorAttachment by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QRhiColorAttachment is created at the first use, not by
    'QRhiColorAttachment(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRhiColorAttachment back gives a copy the ritual made
    for Python, in a new cute QRhiColorAttachment.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiColorAttachment'

  #  Qt's '~QRhiColorAttachment()'. Naming it makes this a value class:
  #  Python owns every C++ QRhiColorAttachment behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QRhiColorAttachmentD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def texture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QRhiColorAttachment::texture() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhicolorattachment.html#texture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QRhiColorAttachment::texture() const
    address = self.uglySide.call('ritual_ZNK19QRhiColorAttachment7textureEv')
    from . import QRhiTexture
    return QRhiTexture._cuteAt(address)

  def renderBuffer(self) -> Optional[QRhiRenderBuffer]:
    """
    Calls Qt's 'QRhiRenderBuffer *QRhiColorAttachment::renderBuffer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicolorattachment.html#renderBuffer

    Returns
    -------

    Optional[QRhiRenderBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderBuffer *QRhiColorAttachment::renderBuffer() const
    address = self.uglySide.call(
        'ritual_ZNK19QRhiColorAttachment12renderBufferEv',
    )
    from . import QRhiRenderBuffer
    return QRhiRenderBuffer._cuteAt(address)

  def layer(self) -> int:
    """
    Calls Qt's 'int QRhiColorAttachment::layer() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhicolorattachment.html#layer
    """
    #  int QRhiColorAttachment::layer() const
    return self.uglySide.call('ritual_ZNK19QRhiColorAttachment5layerEv')

  def level(self) -> int:
    """
    Calls Qt's 'int QRhiColorAttachment::level() const'.

    Qt's own words: https://doc.qt.io/qt-6/qrhicolorattachment.html#level
    """
    #  int QRhiColorAttachment::level() const
    return self.uglySide.call('ritual_ZNK19QRhiColorAttachment5levelEv')

  def resolveTexture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture *QRhiColorAttachment::resolveTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicolorattachment.html#resolveTexture

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QRhiColorAttachment::resolveTexture() const
    address = self.uglySide.call(
        'ritual_ZNK19QRhiColorAttachment14resolveTextureEv',
    )
    from . import QRhiTexture
    return QRhiTexture._cuteAt(address)

  def resolveLayer(self) -> int:
    """
    Calls Qt's 'int QRhiColorAttachment::resolveLayer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicolorattachment.html#resolveLayer
    """
    #  int QRhiColorAttachment::resolveLayer() const
    return self.uglySide.call(
        'ritual_ZNK19QRhiColorAttachment12resolveLayerEv',
    )

  def resolveLevel(self) -> int:
    """
    Calls Qt's 'int QRhiColorAttachment::resolveLevel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicolorattachment.html#resolveLevel
    """
    #  int QRhiColorAttachment::resolveLevel() const
    return self.uglySide.call(
        'ritual_ZNK19QRhiColorAttachment12resolveLevelEv',
    )

  def multiViewCount(self) -> int:
    """
    Calls Qt's 'int QRhiColorAttachment::multiViewCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicolorattachment.html#multiViewCount
    """
    #  int QRhiColorAttachment::multiViewCount() const
    return self.uglySide.call(
        'ritual_ZNK19QRhiColorAttachment14multiViewCountEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRhiTexture)
  @overload(NoneType)
  def setTexture(self, tex: Optional[QRhiTexture]) -> None:
    """
    Calls Qt's 'void QRhiColorAttachment::setTexture(QRhiTexture *tex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicolorattachment.html#setTexture

    Parameters
    ----------

    tex : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiColorAttachment::setTexture(QRhiTexture *tex)
    self.uglySide.call(
        'ritual_ZN19QRhiColorAttachment10setTextureEP11QRhiTexture',
        self._addressOf(tex),
    )

  @overload(QRhiRenderBuffer)
  @overload(NoneType)
  def setRenderBuffer(self, rb: Optional[QRhiRenderBuffer]) -> None:
    """
    Calls Qt's 'void QRhiColorAttachment::setRenderBuffer(QRhiRenderBuffer
    *rb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicolorattachment.html#setRenderBuffer

    Parameters
    ----------

    rb : Optional[QRhiRenderBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiColorAttachment::setRenderBuffer(QRhiRenderBuffer *rb)
    self.uglySide.call(
        'ritual_ZN19QRhiColorAttachment15setRenderBufferEP16QRhiRenderBuffe'
        'r',
        self._addressOf(rb),
    )

  @overload(int)
  def setLayer(self, layer: int) -> None:
    """
    Calls Qt's 'void QRhiColorAttachment::setLayer(int layer)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhicolorattachment.html#setLayer

    Parameters
    ----------

    layer : int
      Passed on as it is.
    """
    #  void QRhiColorAttachment::setLayer(int layer)
    self.uglySide.call('ritual_ZN19QRhiColorAttachment8setLayerEi', layer)

  @overload(int)
  def setLevel(self, level: int) -> None:
    """
    Calls Qt's 'void QRhiColorAttachment::setLevel(int level)'.

    Qt's own words: https://doc.qt.io/qt-6/qrhicolorattachment.html#setLevel

    Parameters
    ----------

    level : int
      Passed on as it is.
    """
    #  void QRhiColorAttachment::setLevel(int level)
    self.uglySide.call('ritual_ZN19QRhiColorAttachment8setLevelEi', level)

  @overload(QRhiTexture)
  @overload(NoneType)
  def setResolveTexture(self, tex: Optional[QRhiTexture]) -> None:
    """
    Calls Qt's 'void QRhiColorAttachment::setResolveTexture(QRhiTexture
    *tex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicolorattachment.html#setResolveTexture

    Parameters
    ----------

    tex : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiColorAttachment::setResolveTexture(QRhiTexture *tex)
    self.uglySide.call(
        'ritual_ZN19QRhiColorAttachment17setResolveTextureEP11QRhiTexture',
        self._addressOf(tex),
    )

  @overload(int)
  def setResolveLayer(self, layer: int) -> None:
    """
    Calls Qt's 'void QRhiColorAttachment::setResolveLayer(int layer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicolorattachment.html#setResolveLayer

    Parameters
    ----------

    layer : int
      Passed on as it is.
    """
    #  void QRhiColorAttachment::setResolveLayer(int layer)
    self.uglySide.call(
        'ritual_ZN19QRhiColorAttachment15setResolveLayerEi', layer,
    )

  @overload(int)
  def setResolveLevel(self, level: int) -> None:
    """
    Calls Qt's 'void QRhiColorAttachment::setResolveLevel(int level)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicolorattachment.html#setResolveLevel

    Parameters
    ----------

    level : int
      Passed on as it is.
    """
    #  void QRhiColorAttachment::setResolveLevel(int level)
    self.uglySide.call(
        'ritual_ZN19QRhiColorAttachment15setResolveLevelEi', level,
    )

  @overload(int)
  def setMultiViewCount(self, count: int) -> None:
    """
    Calls Qt's 'void QRhiColorAttachment::setMultiViewCount(int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicolorattachment.html#setMultiViewCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QRhiColorAttachment::setMultiViewCount(int count)
    self.uglySide.call(
        'ritual_ZN19QRhiColorAttachment17setMultiViewCountEi', count,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QRhiColorAttachment::QRhiColorAttachment()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicolorattachment.html#QRhiColorAttachment
    """
    #  QRhiColorAttachment::QRhiColorAttachment()
    self._noteCreation(QRhiColorAttachment, lambda: Rituals.call(
        'ritual_ZN19QRhiColorAttachmentC1Ev',
    ))

  @overload(QRhiTexture)
  @overload(NoneType)
  def __init__(self, texture: Optional[QRhiTexture]) -> None:
    """
    Notes what was given, for Qt's
    'QRhiColorAttachment::QRhiColorAttachment(QRhiTexture *texture)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicolorattachment.html#QRhiColorAttachment

    Parameters
    ----------

    texture : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QRhiColorAttachment::QRhiColorAttachment(QRhiTexture *texture)
    self._noteCreation(QRhiColorAttachment, lambda: Rituals.call(
        'ritual_ZN19QRhiColorAttachmentC1EP11QRhiTexture',
        self._addressOf(texture),
    ))

  @overload(QRhiRenderBuffer)
  def __init__(self, renderBuffer: Optional[QRhiRenderBuffer]) -> None:
    """
    Notes what was given, for Qt's
    'QRhiColorAttachment::QRhiColorAttachment(QRhiRenderBuffer
    *renderBuffer)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhicolorattachment.html#QRhiColorAttachment

    Parameters
    ----------

    renderBuffer : Optional[QRhiRenderBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QRhiColorAttachment::QRhiColorAttachment(QRhiRenderBuffer
    #      *renderBuffer)
    self._noteCreation(QRhiColorAttachment, lambda: Rituals.call(
        'ritual_ZN19QRhiColorAttachmentC1EP16QRhiRenderBuffer',
        self._addressOf(renderBuffer),
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
