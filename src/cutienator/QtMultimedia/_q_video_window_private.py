"""
QVideoWindowPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qvideowindow_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QVideoWindowPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QSize
  from ..QtGui import QRhi, QRhiResourceUpdateBatch
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRhiResourceUpdateBatch = WAIT['QRhiResourceUpdateBatch']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QVideoWindowPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QVideoWindowPrivate: a plain Python object standing
  in front of one C++ QVideoWindowPrivate.

  What exists
  -----------

  Every function of Qt's QVideoWindowPrivate that has a ritual and that
  Python can call so far, 8 names in all: 'canRender', 'rhi', 'init',
  'render', 'resizeSwapChain', 'releaseSwapChain', 'updateTextures',
  'updateSubtitle'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVideoWindowPrivate::~QVideoWindowPrivate()': the destructor:
    Python never removes a C++ QVideoWindowPrivate.

  What has no ritual
  ------------------

  3 of the 12 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QVideoWindowPrivate is created at the first use, not by
    'QVideoWindowPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVideoWindowPrivate.
  - Each name of Qt's QVideoWindowPrivate that has no cute function yet,
    '__init__', 'initRhi', 'setupGraphicsPipeline', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVideoWindowPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def canRender(self) -> bool:
    """
    Calls Qt's 'bool QVideoWindowPrivate::canRender() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideowindowprivate.html#canRender
    """
    #  bool QVideoWindowPrivate::canRender() const
    return self.uglySide.call('ritual_ZNK19QVideoWindowPrivate9canRenderEv')

  def rhi(self) -> Optional[QRhi]:
    """
    Calls Qt's 'QRhi *QVideoWindowPrivate::rhi() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideowindowprivate.html#rhi

    Returns
    -------

    Optional[QRhi]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhi *QVideoWindowPrivate::rhi() const
    address = self.uglySide.call('ritual_ZNK19QVideoWindowPrivate3rhiEv')
    from ..QtGui import QRhi
    return QRhi._cuteAt(address)

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
    Qt's 'QVideoWindowPrivate::QVideoWindowPrivate(QVideoWindow *q)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: no member named 'platformSurfaceType' in the global
    namespace; did you mean 'QPlatformSurface'?.
    """
    raise NotImplementedError(
        "'QVideoWindowPrivate.__init__' has no cute function yet. Qt's "
        "'QVideoWindowPrivate::QVideoWindowPrivate(QVideoWindow *q)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: no member named 'platformSurfaceType' "
        "in the global namespace; did you mean 'QPlatformSurface'?.")

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

  def init(self) -> None:
    """
    Calls Qt's 'void QVideoWindowPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qvideowindowprivate.html#init
    """
    #  void QVideoWindowPrivate::init()
    self.uglySide.call('ritual_ZN19QVideoWindowPrivate4initEv')

  def render(self) -> None:
    """
    Calls Qt's 'void QVideoWindowPrivate::render()'.

    Qt's own words: https://doc.qt.io/qt-6/qvideowindowprivate.html#render
    """
    #  void QVideoWindowPrivate::render()
    self.uglySide.call('ritual_ZN19QVideoWindowPrivate6renderEv')

  def resizeSwapChain(self) -> None:
    """
    Calls Qt's 'void QVideoWindowPrivate::resizeSwapChain()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideowindowprivate.html#resizeSwapChain
    """
    #  void QVideoWindowPrivate::resizeSwapChain()
    self.uglySide.call('ritual_ZN19QVideoWindowPrivate15resizeSwapChainEv')

  def releaseSwapChain(self) -> None:
    """
    Calls Qt's 'void QVideoWindowPrivate::releaseSwapChain()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideowindowprivate.html#releaseSwapChain
    """
    #  void QVideoWindowPrivate::releaseSwapChain()
    self.uglySide.call('ritual_ZN19QVideoWindowPrivate16releaseSwapChainEv')

  @overload(QRhiResourceUpdateBatch)
  @overload(NoneType)
  def updateTextures(self, rub: Optional[QRhiResourceUpdateBatch]) -> None:
    """
    Calls Qt's 'void
    QVideoWindowPrivate::updateTextures(QRhiResourceUpdateBatch *rub)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideowindowprivate.html#updateTextures

    Parameters
    ----------

    rub : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QVideoWindowPrivate::updateTextures(QRhiResourceUpdateBatch *rub)
    self.uglySide.call(
        'ritual_ZN19QVideoWindowPrivate14updateTexturesEP23QRhiResourceUpda'
        'teBatch',
        self._addressOf(rub),
    )

  @overload(QRhiResourceUpdateBatch, QSize)
  @overload(NoneType, QSize)
  def updateSubtitle(
      self,
      rub: Optional[QRhiResourceUpdateBatch],
      frameSize: QSize,
  ) -> None:
    """
    Calls Qt's 'void
    QVideoWindowPrivate::updateSubtitle(QRhiResourceUpdateBatch *rub, const
    QSize &frameSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideowindowprivate.html#updateSubtitle

    Parameters
    ----------

    rub : Optional[QRhiResourceUpdateBatch]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    frameSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QVideoWindowPrivate::updateSubtitle(QRhiResourceUpdateBatch *rub,
    #      const QSize &frameSize)
    self.uglySide.call(
        'ritual_ZN19QVideoWindowPrivate14updateSubtitleEP23QRhiResourceUpda'
        'teBatchRK5QSize',
        self._addressOf(rub), self._valueOf(frameSize),
    )

  @staticmethod
  def initRhi(*__, **_) -> Never:
    """
    Qt's 'void QVideoWindowPrivate::initRhi()': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'g_vw_quad'.
    """
    raise NotImplementedError(
        "'QVideoWindowPrivate.initRhi' has no cute function yet. Qt's 'void "
        "QVideoWindowPrivate::initRhi()': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'g_vw_quad'.")

  @staticmethod
  def setupGraphicsPipeline(*__, **_) -> Never:
    """
    Qt's 'void
    QVideoWindowPrivate::setupGraphicsPipeline(QRhiGraphicsPipeline
    *pipeline, QRhiShaderResourceBindings *bindings, const QVideoFrameFormat
    &fmt)': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'vwGetShader'.
    """
    raise NotImplementedError(
        "'QVideoWindowPrivate.setupGraphicsPipeline' has no cute function "
        "yet. Qt's 'void "
        "QVideoWindowPrivate::setupGraphicsPipeline(QRhiGraphicsPipeline "
        "*pipeline, QRhiShaderResourceBindings *bindings, const "
        "QVideoFrameFormat &fmt)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'vwGetShader'.")
