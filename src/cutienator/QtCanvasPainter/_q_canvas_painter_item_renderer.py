"""
QCanvasPainterItemRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/qcanvaspainteritemrenderer.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QColor, QRhiCommandBuffer
  from . import QCanvasPainter, QCanvasPainterItem
  from ..QtQuick import QQuickRhiItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCanvasPainter = WAIT['QCanvasPainter']
  QCanvasPainterItem = WAIT['QCanvasPainterItem']
  QQuickRhiItem = WAIT['QQuickRhiItem']
  QRhiCommandBuffer = WAIT['QRhiCommandBuffer']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCanvasPainterItemRenderer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCanvasPainterItemRenderer: a plain Python object
  standing in front of one C++ QCanvasPainterItemRenderer.

  What exists
  -----------

  Every function of Qt's QCanvasPainterItemRenderer that has a ritual and
  that Python can call so far, 14 names in all: 'fillColor', 'painter',
  'width', 'height', 'hasSharedPainter', 'setSharedPainter',
  'initializeResources', 'prePaint', 'paint', 'synchronizeData',
  'initialize', 'render', 'synchronize', 'endCanvasPainting'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCanvasPainterItemRenderer::~QCanvasPainterItemRenderer()': the
    destructor: Python never removes a C++ QCanvasPainterItemRenderer.
  - Qt's 'void
    QCanvasPainterItemRenderer::beginCanvasPainting(QCanvasOffscreenCanvas
    &canvas)': takes a type Python has no way to hand over yet.
  - Qt's 'QCanvasPainterItemRendererPrivate
    *QCanvasPainterItemRenderer::d_func()': gives
    'QCanvasPainterItemRendererPrivate', which has no cute class yet.
  - Qt's 'const QCanvasPainterItemRendererPrivate
    *QCanvasPainterItemRenderer::d_func() const': gives
    'QCanvasPainterItemRendererPrivate', which has no cute class yet.
  - Qt's 'void QCanvasPainterItemRenderer::grabCanvasImpl(const
    QCanvasOffscreenCanvas &canvas, const QObject *context,
    QtPrivate::QSlotObjectBase *slotObj)': names
    'QtPrivate::QSlotObjectBase', which has no cute class yet.

  What has no ritual
  ------------------

  1 of the 21 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QCanvasPainterItemRenderer is created at the first use, not by
    'QCanvasPainterItemRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCanvasPainterItemRenderer.
  - Each name of Qt's QCanvasPainterItemRenderer that has no cute function
    yet, 'beginCanvasPainting', 'd_func', 'grabCanvas', 'grabCanvasImpl',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanvasPainterItemRenderer'

  #  A C++ QCanvasPainterItemRenderer Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCanvasPainterItemRenderer'

  #  The functions Qt calls itself that QCanvasPainterItemRenderer is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'initializeResources': (
          ('_ZN26QCanvasPainterItemRenderer19initializeResourcesEP14QCanvas'
           'Painter',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCanvasPainter:QCanvasPainter'),
           )),
      ),
      'prePaint': (
          ('_ZN26QCanvasPainterItemRenderer8prePaintEP14QCanvasPainter',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCanvasPainter:QCanvasPainter'),
           )),
      ),
      'paint': (
          ('_ZN26QCanvasPainterItemRenderer5paintEP14QCanvasPainter',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCanvasPainter:QCanvasPainter'),
           )),
      ),
      'synchronizeData': (
          ('_ZN26QCanvasPainterItemRenderer15synchronizeDataEP18QCanvasPain'
           'terItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCanvasPainter:QCanvasPainterItem'),
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

  def fillColor(self) -> QColor:
    """
    Calls Qt's 'QColor QCanvasPainterItemRenderer::fillColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainteritemrenderer.html#fillColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QCanvasPainterItemRenderer::fillColor() const
    address = self.uglySide.call(
        'ritual_ZNK26QCanvasPainterItemRenderer9fillColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def painter(self) -> Optional[QCanvasPainter]:
    """
    Calls Qt's 'QCanvasPainter *QCanvasPainterItemRenderer::painter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainteritemrenderer.html#painter

    Returns
    -------

    Optional[QCanvasPainter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCanvasPainter *QCanvasPainterItemRenderer::painter() const
    address = self.uglySide.call(
        'ritual_ZNK26QCanvasPainterItemRenderer7painterEv',
    )
    from . import QCanvasPainter
    return QCanvasPainter._cuteAt(address)

  def width(self) -> float:
    """
    Calls Qt's 'qreal QCanvasPainterItemRenderer::width() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainteritemrenderer.html#width
    """
    #  qreal QCanvasPainterItemRenderer::width() const
    return self.uglySide.call(
        'ritual_ZNK26QCanvasPainterItemRenderer5widthEv',
    )

  def height(self) -> float:
    """
    Calls Qt's 'qreal QCanvasPainterItemRenderer::height() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainteritemrenderer.html#height
    """
    #  qreal QCanvasPainterItemRenderer::height() const
    return self.uglySide.call(
        'ritual_ZNK26QCanvasPainterItemRenderer6heightEv',
    )

  def hasSharedPainter(self) -> bool:
    """
    Calls Qt's 'bool QCanvasPainterItemRenderer::hasSharedPainter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainteritemrenderer.html#hasSharedPainter
    """
    #  bool QCanvasPainterItemRenderer::hasSharedPainter() const
    return self.uglySide.call(
        'ritual_ZNK26QCanvasPainterItemRenderer16hasSharedPainterEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setSharedPainter(self, enable: bool) -> None:
    """
    Calls Qt's 'void QCanvasPainterItemRenderer::setSharedPainter(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainteritemrenderer.html#setSharedPainter

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QCanvasPainterItemRenderer::setSharedPainter(bool enable)
    self.uglySide.call(
        'ritual_ZN26QCanvasPainterItemRenderer16setSharedPainterEb', enable,
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
    'QCanvasPainterItemRenderer::QCanvasPainterItemRenderer()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainteritemrenderer.html
    """
    #  QCanvasPainterItemRenderer::QCanvasPainterItemRenderer()
    self._noteCreation(QCanvasPainterItemRenderer, lambda: Rituals.call(
        'ritual_ZN26QCanvasPainterItemRendererC1Ev',
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

  @overload(QCanvasPainter)
  @overload(NoneType)
  def initializeResources(self, painter: Optional[QCanvasPainter]) -> None:
    """
    Calls Qt's 'void
    QCanvasPainterItemRenderer::initializeResources(QCanvasPainter
    *painter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainteritemrenderer.html

    Parameters
    ----------

    painter : Optional[QCanvasPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCanvasPainterItemRenderer::initializeResources(QCanvasPainter
    #      *painter)
    ritual = (
        'ritual_ZN26QCanvasPainterItemRenderer19initializeResourcesEP14QCan'
        'vasPainter')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QCanvasPainterItemRenderer19initializeResourcesEP'
          '14QCanvasPainter')
    self.uglySide.call(ritual, self._addressOf(painter))

  @overload(QCanvasPainter)
  @overload(NoneType)
  def prePaint(self, painter: Optional[QCanvasPainter]) -> None:
    """
    Calls Qt's 'void QCanvasPainterItemRenderer::prePaint(QCanvasPainter
    *painter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainteritemrenderer.html#prePaint

    Parameters
    ----------

    painter : Optional[QCanvasPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCanvasPainterItemRenderer::prePaint(QCanvasPainter *painter)
    ritual = (
        'ritual_ZN26QCanvasPainterItemRenderer8prePaintEP14QCanvasPainter')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QCanvasPainterItemRenderer8prePaintEP14QCanvasPai'
          'nter')
    self.uglySide.call(ritual, self._addressOf(painter))

  @overload(QCanvasPainter)
  @overload(NoneType)
  def paint(self, painter: Optional[QCanvasPainter]) -> None:
    """
    Calls Qt's 'void QCanvasPainterItemRenderer::paint(QCanvasPainter
    *painter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainteritemrenderer.html#paint

    Parameters
    ----------

    painter : Optional[QCanvasPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCanvasPainterItemRenderer::paint(QCanvasPainter *painter)
    ritual = 'ritual_ZN26QCanvasPainterItemRenderer5paintEP14QCanvasPainter'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QCanvasPainterItemRenderer5paintEP14QCanvasPainte'
          'r')
    self.uglySide.call(ritual, self._addressOf(painter))

  @overload(QCanvasPainterItem)
  @overload(NoneType)
  def synchronizeData(self, item: Optional[QCanvasPainterItem]) -> None:
    """
    Calls Qt's 'void
    QCanvasPainterItemRenderer::synchronizeData(QCanvasPainterItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainteritemrenderer.html#synchronizeData

    Parameters
    ----------

    item : Optional[QCanvasPainterItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCanvasPainterItemRenderer::synchronizeData(QCanvasPainterItem
    #      *item)
    ritual = (
        'ritual_ZN26QCanvasPainterItemRenderer15synchronizeDataEP18QCanvasP'
        'ainterItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QCanvasPainterItemRenderer15synchronizeDataEP18QC'
          'anvasPainterItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def initialize(self, cb: Optional[QRhiCommandBuffer]) -> None:
    """
    Calls Qt's 'void QCanvasPainterItemRenderer::initialize(QRhiCommandBuffer
    *cb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainteritemrenderer.html#initialize

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCanvasPainterItemRenderer::initialize(QRhiCommandBuffer *cb)
    ritual = (
        'ritual_ZN26QCanvasPainterItemRenderer10initializeEP17QRhiCommandBu'
        'ffer')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QCanvasPainterItemRenderer10initializeEP17QRhiCom'
          'mandBuffer')
    self.uglySide.call(ritual, self._addressOf(cb))

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def render(self, cb: Optional[QRhiCommandBuffer]) -> None:
    """
    Calls Qt's 'void QCanvasPainterItemRenderer::render(QRhiCommandBuffer
    *cb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainteritemrenderer.html#render

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCanvasPainterItemRenderer::render(QRhiCommandBuffer *cb)
    ritual = (
        'ritual_ZN26QCanvasPainterItemRenderer6renderEP17QRhiCommandBuffer')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QCanvasPainterItemRenderer6renderEP17QRhiCommandB'
          'uffer')
    self.uglySide.call(ritual, self._addressOf(cb))

  @overload(QQuickRhiItem)
  @overload(NoneType)
  def synchronize(self, item: Optional[QQuickRhiItem]) -> None:
    """
    Calls Qt's 'void QCanvasPainterItemRenderer::synchronize(QQuickRhiItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainteritemrenderer.html#synchronize

    Parameters
    ----------

    item : Optional[QQuickRhiItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCanvasPainterItemRenderer::synchronize(QQuickRhiItem *item)
    ritual = (
        'ritual_ZN26QCanvasPainterItemRenderer11synchronizeEP13QQuickRhiIte'
        'm')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QCanvasPainterItemRenderer11synchronizeEP13QQuick'
          'RhiItem')
    self.uglySide.call(ritual, self._addressOf(item))

  def endCanvasPainting(self) -> None:
    """
    Calls Qt's 'void QCanvasPainterItemRenderer::endCanvasPainting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainteritemrenderer.html#endCanvasPainting
    """
    #  void QCanvasPainterItemRenderer::endCanvasPainting()
    self.uglySide.call(
        'ritual_ZN26QCanvasPainterItemRenderer17endCanvasPaintingEv',
    )

  @staticmethod
  def beginCanvasPainting(*__, **_) -> Never:
    """
    Qt's 'void
    QCanvasPainterItemRenderer::beginCanvasPainting(QCanvasOffscreenCanvas
    &canvas)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCanvasPainterItemRenderer.beginCanvasPainting' has no cute "
        "function yet. Qt's 'void "
        "QCanvasPainterItemRenderer::beginCanvasPainting(QCanvasOffscreenCan"
        "vas &canvas)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QCanvasPainterItemRendererPrivate
      *QCanvasPainterItemRenderer::d_func()': gives
      'QCanvasPainterItemRendererPrivate', which has no cute class yet.
    - Qt's 'const QCanvasPainterItemRendererPrivate
      *QCanvasPainterItemRenderer::d_func() const': gives
      'QCanvasPainterItemRendererPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QCanvasPainterItemRenderer.d_func' has no cute function yet. Qt's "
        "'QCanvasPainterItemRendererPrivate "
        "*QCanvasPainterItemRenderer::d_func()': gives "
        "'QCanvasPainterItemRendererPrivate', which has no cute class yet. "
        "Qt's 'const QCanvasPainterItemRendererPrivate "
        "*QCanvasPainterItemRenderer::d_func() const': gives "
        "'QCanvasPainterItemRendererPrivate', which has no cute class yet.")

  @staticmethod
  def grabCanvas(*__, **_) -> Never:
    """
    Qt's 'QCanvasPainterItemRenderer::grabCanvas': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QCanvasPainterItemRenderer.grabCanvas' has no cute function yet. "
        "Qt's 'QCanvasPainterItemRenderer::grabCanvas': a template: a "
        "pattern and no single function.")

  @staticmethod
  def grabCanvasImpl(*__, **_) -> Never:
    """
    Qt's 'void QCanvasPainterItemRenderer::grabCanvasImpl(const
    QCanvasOffscreenCanvas &canvas, const QObject *context,
    QtPrivate::QSlotObjectBase *slotObj)': names
    'QtPrivate::QSlotObjectBase', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QCanvasPainterItemRenderer.grabCanvasImpl' has no cute function "
        "yet. Qt's 'void QCanvasPainterItemRenderer::grabCanvasImpl(const "
        "QCanvasOffscreenCanvas &canvas, const QObject *context, "
        "QtPrivate::QSlotObjectBase *slotObj)': names "
        "'QtPrivate::QSlotObjectBase', which has no cute class yet.")
