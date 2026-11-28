"""
QSGSoftwareRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgsoftwarerenderer_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSGSoftwareRenderer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSGAbstractSoftwareRenderer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QBackingStore, QPaintDevice, QRegion
  from . import QSGRenderContext
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBackingStore = WAIT['QBackingStore']
  QPaintDevice = WAIT['QPaintDevice']
  QSGRenderContext = WAIT['QSGRenderContext']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGSoftwareRenderer(QSGAbstractSoftwareRenderer):
  """
  The cute side of Qt's QSGSoftwareRenderer: a plain Python object standing
  in front of one C++ QSGSoftwareRenderer.

  It is built on the cute 'QSGAbstractSoftwareRenderer', as Qt's
  QSGSoftwareRenderer is built on Qt's QSGAbstractSoftwareRenderer, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSGSoftwareRenderer that has a ritual and that
  Python can call so far, 6 names in all: 'setCurrentPaintDevice',
  'currentPaintDevice', 'setBackingStore', 'flushRegion', 'renderScene',
  'render'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGSoftwareRenderer::~QSGSoftwareRenderer()': the destructor:
    Python never removes a C++ QSGSoftwareRenderer.

  What to expect
  --------------

  - The C++ QSGSoftwareRenderer is created at the first use, not by
    'QSGSoftwareRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGSoftwareRenderer.
  - Qt tells when it has removed the C++ QSGSoftwareRenderer. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGSoftwareRenderer'

  #  A C++ QSGSoftwareRenderer Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGSoftwareRenderer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def currentPaintDevice(self) -> Optional[QPaintDevice]:
    """
    Calls Qt's 'QPaintDevice *QSGSoftwareRenderer::currentPaintDevice()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderer.html#currentPaintDevice

    Returns
    -------

    Optional[QPaintDevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPaintDevice *QSGSoftwareRenderer::currentPaintDevice() const
    address = self.uglySide.call(
        'ritual_ZNK19QSGSoftwareRenderer18currentPaintDeviceEv',
    )
    from ..QtGui import QPaintDevice
    return QPaintDevice._cuteAt(address)

  def flushRegion(self) -> QRegion:
    """
    Calls Qt's 'QRegion QSGSoftwareRenderer::flushRegion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderer.html#flushRegion

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QSGSoftwareRenderer::flushRegion() const
    address = self.uglySide.call(
        'ritual_ZNK19QSGSoftwareRenderer11flushRegionEv',
    )
    from ..QtGui import QRegion
    return QRegion._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPaintDevice)
  @overload(NoneType)
  def setCurrentPaintDevice(self, device: Optional[QPaintDevice]) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderer::setCurrentPaintDevice(QPaintDevice
    *device)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderer.html#setCurrentPaintDevice

    Parameters
    ----------

    device : Optional[QPaintDevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderer::setCurrentPaintDevice(QPaintDevice *device)
    self.uglySide.call(
        'ritual_ZN19QSGSoftwareRenderer21setCurrentPaintDeviceEP12QPaintDev'
        'ice',
        self._addressOf(device, 'QPaintDevice'),
    )

  @overload(QBackingStore)
  @overload(NoneType)
  def setBackingStore(self, backingStore: Optional[QBackingStore]) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderer::setBackingStore(QBackingStore
    *backingStore)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderer.html#setBackingStore

    Parameters
    ----------

    backingStore : Optional[QBackingStore]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSGSoftwareRenderer::setBackingStore(QBackingStore *backingStore)
    self.uglySide.call(
        'ritual_ZN19QSGSoftwareRenderer15setBackingStoreEP13QBackingStore',
        self._addressOf(backingStore),
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

  @overload(QSGRenderContext)
  @overload(NoneType)
  def __init__(self, context: Optional[QSGRenderContext]) -> None:
    """
    Notes what was given, for Qt's
    'QSGSoftwareRenderer::QSGSoftwareRenderer(QSGRenderContext *context)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderer.html#QSGSoftwareRenderer

    Parameters
    ----------

    context : Optional[QSGRenderContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSGSoftwareRenderer::QSGSoftwareRenderer(QSGRenderContext *context)
    self._noteCreation(QSGSoftwareRenderer, lambda: Rituals.call(
        'ritual_ZN19QSGSoftwareRendererC1EP16QSGRenderContext',
        self._addressOf(context),
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

  def renderScene(self) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderer::renderScene()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsoftwarerenderer.html#renderScene
    """
    #  void QSGSoftwareRenderer::renderScene()
    self.uglySide.call('ritual_ZN19QSGSoftwareRenderer11renderSceneEv')

  def render(self) -> None:
    """
    Calls Qt's 'void QSGSoftwareRenderer::render()'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsoftwarerenderer.html#render
    """
    #  void QSGSoftwareRenderer::render()
    self.uglySide.call('ritual_ZN19QSGSoftwareRenderer6renderEv')
