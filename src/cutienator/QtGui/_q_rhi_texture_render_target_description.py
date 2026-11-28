"""
QRhiTextureRenderTargetDescription binding of the Qt C++
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
  from typing import Never, Optional

  from . import QRhiColorAttachment, QRhiRenderBuffer, QRhiShadingRateMap
  from . import QRhiTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiColorAttachment = WAIT['QRhiColorAttachment']
  QRhiRenderBuffer = WAIT['QRhiRenderBuffer']
  QRhiShadingRateMap = WAIT['QRhiShadingRateMap']
  QRhiTexture = WAIT['QRhiTexture']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRhiTextureRenderTargetDescription(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRhiTextureRenderTargetDescription: a plain Python
  object standing in front of one C++ QRhiTextureRenderTargetDescription.

  C++ hands a QRhiTextureRenderTargetDescription around as a copy, so every
  C++ QRhiTextureRenderTargetDescription behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QRhiTextureRenderTargetDescription that has a ritual
  and that Python can call so far, 14 names in all: 'cbeginColorAttachments',
  'cendColorAttachments', 'colorAttachmentAt', 'colorAttachmentCount',
  'depthStencilBuffer', 'setDepthStencilBuffer', 'depthTexture',
  'setDepthTexture', 'depthLayer', 'setDepthLayer', 'depthResolveTexture',
  'setDepthResolveTexture', 'shadingRateMap', 'setShadingRateMap'. It can be
  made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QRhiTextureRenderTargetDescription::setColorAttachments(std::
    initializer_list<QRhiColorAttachment> list)': takes a type Python has no
    way to hand over yet.
  - Qt's
    'QRhiTextureRenderTargetDescription::~QRhiTextureRenderTargetDescription(
    )': the destructor: Python removes its C++
    QRhiTextureRenderTargetDescription by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 21 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QRhiTextureRenderTargetDescription is created at the first use,
    not by 'QRhiTextureRenderTargetDescription(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QRhiTextureRenderTargetDescription back gives a copy
    the ritual made for Python, in a new cute
    QRhiTextureRenderTargetDescription.
  - Each name of Qt's QRhiTextureRenderTargetDescription that has no cute
    function yet, 'setColorAttachments', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRhiTextureRenderTargetDescription'

  #  Qt's '~QRhiTextureRenderTargetDescription()'. Naming it makes this a
  #  value class: Python owns every C++ QRhiTextureRenderTargetDescription
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN34QRhiTextureRenderTargetDescriptionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def cbeginColorAttachments(self) -> Optional[QRhiColorAttachment]:
    """
    Calls Qt's 'const QRhiColorAttachment
    *QRhiTextureRenderTargetDescription::cbeginColorAttachments() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturerendertargetdescription.html

    Returns
    -------

    Optional[QRhiColorAttachment]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiColorAttachment
    #      *QRhiTextureRenderTargetDescription::cbeginColorAttachments()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK34QRhiTextureRenderTargetDescription22cbeginColorAttachm'
        'entsEv',
    )
    from . import QRhiColorAttachment
    return QRhiColorAttachment._cuteAt(address)

  def cendColorAttachments(self) -> Optional[QRhiColorAttachment]:
    """
    Calls Qt's 'const QRhiColorAttachment
    *QRhiTextureRenderTargetDescription::cendColorAttachments() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturerendertargetdescription.html

    Returns
    -------

    Optional[QRhiColorAttachment]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiColorAttachment
    #      *QRhiTextureRenderTargetDescription::cendColorAttachments() const
    address = self.uglySide.call(
        'ritual_ZNK34QRhiTextureRenderTargetDescription20cendColorAttachmen'
        'tsEv',
    )
    from . import QRhiColorAttachment
    return QRhiColorAttachment._cuteAt(address)

  @overload(int)
  def colorAttachmentAt(self, index: int) -> Optional[QRhiColorAttachment]:
    """
    Calls Qt's 'const QRhiColorAttachment
    *QRhiTextureRenderTargetDescription::colorAttachmentAt(qsizetype index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturerendertargetdescription.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QRhiColorAttachment]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QRhiColorAttachment
    #      *QRhiTextureRenderTargetDescription::colorAttachmentAt(qsizetype
    #      index) const
    address = self.uglySide.call(
        'ritual_ZNK34QRhiTextureRenderTargetDescription17colorAttachmentAtE'
        'x',
        index,
    )
    from . import QRhiColorAttachment
    return QRhiColorAttachment._cuteAt(address)

  def colorAttachmentCount(self) -> int:
    """
    Calls Qt's 'qsizetype
    QRhiTextureRenderTargetDescription::colorAttachmentCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturerendertargetdescription.html
    """
    #  qsizetype QRhiTextureRenderTargetDescription::colorAttachmentCount()
    #      const
    return self.uglySide.call(
        'ritual_ZNK34QRhiTextureRenderTargetDescription20colorAttachmentCou'
        'ntEv',
    )

  def depthStencilBuffer(self) -> Optional[QRhiRenderBuffer]:
    """
    Calls Qt's 'QRhiRenderBuffer
    *QRhiTextureRenderTargetDescription::depthStencilBuffer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturerendertargetdescription.html

    Returns
    -------

    Optional[QRhiRenderBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiRenderBuffer
    #      *QRhiTextureRenderTargetDescription::depthStencilBuffer() const
    address = self.uglySide.call(
        'ritual_ZNK34QRhiTextureRenderTargetDescription18depthStencilBuffer'
        'Ev',
    )
    from . import QRhiRenderBuffer
    return QRhiRenderBuffer._cuteAt(address)

  def depthTexture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture
    *QRhiTextureRenderTargetDescription::depthTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturerendertargetdescription.html

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QRhiTextureRenderTargetDescription::depthTexture() const
    address = self.uglySide.call(
        'ritual_ZNK34QRhiTextureRenderTargetDescription12depthTextureEv',
    )
    from . import QRhiTexture
    return QRhiTexture._cuteAt(address)

  def depthLayer(self) -> int:
    """
    Calls Qt's 'int QRhiTextureRenderTargetDescription::depthLayer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturerendertargetdescription.html#depthLayer
    """
    #  int QRhiTextureRenderTargetDescription::depthLayer() const
    return self.uglySide.call(
        'ritual_ZNK34QRhiTextureRenderTargetDescription10depthLayerEv',
    )

  def depthResolveTexture(self) -> Optional[QRhiTexture]:
    """
    Calls Qt's 'QRhiTexture
    *QRhiTextureRenderTargetDescription::depthResolveTexture() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturerendertargetdescription.html

    Returns
    -------

    Optional[QRhiTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiTexture *QRhiTextureRenderTargetDescription::depthResolveTexture()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK34QRhiTextureRenderTargetDescription19depthResolveTextur'
        'eEv',
    )
    from . import QRhiTexture
    return QRhiTexture._cuteAt(address)

  def shadingRateMap(self) -> Optional[QRhiShadingRateMap]:
    """
    Calls Qt's 'QRhiShadingRateMap
    *QRhiTextureRenderTargetDescription::shadingRateMap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturerendertargetdescription.html

    Returns
    -------

    Optional[QRhiShadingRateMap]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiShadingRateMap
    #      *QRhiTextureRenderTargetDescription::shadingRateMap() const
    address = self.uglySide.call(
        'ritual_ZNK34QRhiTextureRenderTargetDescription14shadingRateMapEv',
    )
    from . import QRhiShadingRateMap
    return QRhiShadingRateMap._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRhiRenderBuffer)
  @overload(NoneType)
  def setDepthStencilBuffer(
      self,
      renderBuffer: Optional[QRhiRenderBuffer],
  ) -> None:
    """
    Calls Qt's 'void
    QRhiTextureRenderTargetDescription::setDepthStencilBuffer(
    QRhiRenderBuffer *renderBuffer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturerendertargetdescription.html

    Parameters
    ----------

    renderBuffer : Optional[QRhiRenderBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiTextureRenderTargetDescription::setDepthStencilBuffer(
    #      QRhiRenderBuffer *renderBuffer)
    self.uglySide.call(
        'ritual_ZN34QRhiTextureRenderTargetDescription21setDepthStencilBuff'
        'erEP16QRhiRenderBuffer',
        self._addressOf(renderBuffer),
    )

  @overload(QRhiTexture)
  @overload(NoneType)
  def setDepthTexture(self, texture: Optional[QRhiTexture]) -> None:
    """
    Calls Qt's 'void
    QRhiTextureRenderTargetDescription::setDepthTexture(QRhiTexture
    *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturerendertargetdescription.html

    Parameters
    ----------

    texture : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiTextureRenderTargetDescription::setDepthTexture(QRhiTexture
    #      *texture)
    self.uglySide.call(
        'ritual_ZN34QRhiTextureRenderTargetDescription15setDepthTextureEP11'
        'QRhiTexture',
        self._addressOf(texture),
    )

  @overload(int)
  def setDepthLayer(self, depthLayer: int) -> None:
    """
    Calls Qt's 'void QRhiTextureRenderTargetDescription::setDepthLayer(int
    depthLayer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturerendertargetdescription.html

    Parameters
    ----------

    depthLayer : int
      Passed on as it is.
    """
    #  void QRhiTextureRenderTargetDescription::setDepthLayer(int depthLayer)
    self.uglySide.call(
        'ritual_ZN34QRhiTextureRenderTargetDescription13setDepthLayerEi',
        depthLayer,
    )

  @overload(QRhiTexture)
  @overload(NoneType)
  def setDepthResolveTexture(self, tex: Optional[QRhiTexture]) -> None:
    """
    Calls Qt's 'void
    QRhiTextureRenderTargetDescription::setDepthResolveTexture(QRhiTexture
    *tex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturerendertargetdescription.html

    Parameters
    ----------

    tex : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiTextureRenderTargetDescription::setDepthResolveTexture(
    #      QRhiTexture *tex)
    self.uglySide.call(
        'ritual_ZN34QRhiTextureRenderTargetDescription22setDepthResolveText'
        'ureEP11QRhiTexture',
        self._addressOf(tex),
    )

  @overload(QRhiShadingRateMap)
  @overload(NoneType)
  def setShadingRateMap(self, map: Optional[QRhiShadingRateMap]) -> None:
    """
    Calls Qt's 'void
    QRhiTextureRenderTargetDescription::setShadingRateMap(QRhiShadingRateMap
    *map)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturerendertargetdescription.html

    Parameters
    ----------

    map : Optional[QRhiShadingRateMap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QRhiTextureRenderTargetDescription::setShadingRateMap(
    #      QRhiShadingRateMap *map)
    self.uglySide.call(
        'ritual_ZN34QRhiTextureRenderTargetDescription17setShadingRateMapEP'
        '18QRhiShadingRateMap',
        self._addressOf(map),
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
    'QRhiTextureRenderTargetDescription::QRhiTextureRenderTargetDescription(
    )', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturerendertargetdescription.html
    """
    #  QRhiTextureRenderTargetDescription::
    #      QRhiTextureRenderTargetDescription()
    self._noteCreation(
        QRhiTextureRenderTargetDescription, lambda: Rituals.call(
            'ritual_ZN34QRhiTextureRenderTargetDescriptionC1Ev',
        ))

  @overload(QRhiColorAttachment)
  def __init__(self, colorAttachment: QRhiColorAttachment) -> None:
    """
    Notes what was given, for Qt's
    'QRhiTextureRenderTargetDescription::QRhiTextureRenderTargetDescription(
    const QRhiColorAttachment &colorAttachment)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturerendertargetdescription.html

    Parameters
    ----------

    colorAttachment : QRhiColorAttachment
      Passed on as a value: Qt reads the C++ QRhiColorAttachment, which stays
      Python's own.
    """
    #  QRhiTextureRenderTargetDescription::
    #      QRhiTextureRenderTargetDescription(const QRhiColorAttachment
    #      &colorAttachment)
    self._noteCreation(
        QRhiTextureRenderTargetDescription, lambda: Rituals.call(
            'ritual_ZN34QRhiTextureRenderTargetDescriptionC1ERK19QRhiColorA'
            'ttachment',
            self._valueOf(colorAttachment),
        ))

  @overload(QRhiColorAttachment, QRhiRenderBuffer)
  @overload(QRhiColorAttachment, NoneType)
  def __init__(
      self,
      colorAttachment: QRhiColorAttachment,
      depthStencilBuffer: Optional[QRhiRenderBuffer],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QRhiTextureRenderTargetDescription::QRhiTextureRenderTargetDescription(
    const QRhiColorAttachment &colorAttachment, QRhiRenderBuffer
    *depthStencilBuffer)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturerendertargetdescription.html

    Parameters
    ----------

    colorAttachment : QRhiColorAttachment
      Passed on as a value: Qt reads the C++ QRhiColorAttachment, which stays
      Python's own.

    depthStencilBuffer : Optional[QRhiRenderBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QRhiTextureRenderTargetDescription::
    #      QRhiTextureRenderTargetDescription(const QRhiColorAttachment
    #      &colorAttachment, QRhiRenderBuffer *depthStencilBuffer)
    self._noteCreation(
        QRhiTextureRenderTargetDescription, lambda: Rituals.call(
            'ritual_ZN34QRhiTextureRenderTargetDescriptionC1ERK19QRhiColorA'
            'ttachmentP16QRhiRenderBuffer',
            self._valueOf(colorAttachment),
            self._addressOf(depthStencilBuffer),
        ))

  @overload(QRhiColorAttachment, QRhiTexture)
  def __init__(
      self,
      colorAttachment: QRhiColorAttachment,
      depthTexture: Optional[QRhiTexture],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QRhiTextureRenderTargetDescription::QRhiTextureRenderTargetDescription(
    const QRhiColorAttachment &colorAttachment, QRhiTexture *depthTexture)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrhitexturerendertargetdescription.html

    Parameters
    ----------

    colorAttachment : QRhiColorAttachment
      Passed on as a value: Qt reads the C++ QRhiColorAttachment, which stays
      Python's own.

    depthTexture : Optional[QRhiTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QRhiTextureRenderTargetDescription::
    #      QRhiTextureRenderTargetDescription(const QRhiColorAttachment
    #      &colorAttachment, QRhiTexture *depthTexture)
    self._noteCreation(
        QRhiTextureRenderTargetDescription, lambda: Rituals.call(
            'ritual_ZN34QRhiTextureRenderTargetDescriptionC1ERK19QRhiColorA'
            'ttachmentP11QRhiTexture',
            self._valueOf(colorAttachment), self._addressOf(depthTexture),
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

  @staticmethod
  def setColorAttachments(*__, **_) -> Never:
    """
    - Qt's 'void
      QRhiTextureRenderTargetDescription::setColorAttachments(std::
      initializer_list<QRhiColorAttachment> list)': takes a type Python has
      no way to hand over yet.
    - Qt's 'QRhiTextureRenderTargetDescription::setColorAttachments': a
      template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QRhiTextureRenderTargetDescription.setColorAttachments' has no "
        "cute function yet. Qt's 'void "
        "QRhiTextureRenderTargetDescription::setColorAttachments(std::initia"
        "lizer_list<QRhiColorAttachment> list)': takes a type Python has no "
        "way to hand over yet. Qt's "
        "'QRhiTextureRenderTargetDescription::setColorAttachments': a "
        "template: a pattern and no single function.")
