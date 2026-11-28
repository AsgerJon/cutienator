"""
QCanvasPainterWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/qcanvaspainterwidget.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtGui import QColor, QRhiCommandBuffer
  from . import QCanvasPainter
  from ..QtWidgets import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCanvasPainter = WAIT['QCanvasPainter']
  QColor = WAIT['QColor']
  QEvent = WAIT['QEvent']
  QRhiCommandBuffer = WAIT['QRhiCommandBuffer']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCanvasPainterWidget(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCanvasPainterWidget: a plain Python object standing
  in front of one C++ QCanvasPainterWidget.

  What exists
  -----------

  Every function of Qt's QCanvasPainterWidget that has a ritual and that
  Python can call so far, 15 names in all: 'metaObject', 'tr', 'fillColor',
  'setFillColor', 'hasSharedPainter', 'setSharedPainter',
  'initializeResources', 'prePaint', 'paint', 'graphicsResourcesInvalidated',
  'initialize', 'render', 'releaseResources', 'event', 'endCanvasPainting'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCanvasPainterWidget::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QCanvasPainterWidget::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QCanvasPainterWidget::~QCanvasPainterWidget()': the destructor:
    Python never removes a C++ QCanvasPainterWidget.
  - Qt's 'void
    QCanvasPainterWidget::beginCanvasPainting(QCanvasOffscreenCanvas
    &canvas)': takes a type Python has no way to hand over yet.
  - Qt's 'QCanvasPainterWidgetPrivate *QCanvasPainterWidget::d_func()': gives
    'QCanvasPainterWidgetPrivate', which has no cute class yet.
  - Qt's 'const QCanvasPainterWidgetPrivate *QCanvasPainterWidget::d_func()
    const': gives 'QCanvasPainterWidgetPrivate', which has no cute class yet.
  - Qt's 'void QCanvasPainterWidget::grabCanvasImpl(const
    QCanvasOffscreenCanvas &canvas, const QObject *context,
    QtPrivate::QSlotObjectBase *slotObj)': names
    'QtPrivate::QSlotObjectBase', which has no cute class yet.

  What has no ritual
  ------------------

  3 of the 26 functions Qt declares: 2 not a gap; 1 a template.

  What to expect
  --------------

  - The C++ QCanvasPainterWidget is created at the first use, not by
    'QCanvasPainterWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCanvasPainterWidget.
  - Qt tells when it has removed the C++ QCanvasPainterWidget. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QCanvasPainterWidget that has no cute function yet,
    'beginCanvasPainting', 'grabCanvas', 'grabCanvasImpl', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QCanvasPainterWidget::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainterwidget.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCanvasPainterWidget::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QCanvasPainterWidget2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanvasPainterWidget'

  #  A C++ QCanvasPainterWidget Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCanvasPainterWidget'

  #  The functions Qt calls itself that QCanvasPainterWidget is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'initializeResources': (
          ('_ZN20QCanvasPainterWidget19initializeResourcesEP14QCanvasPainte'
           'r',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCanvasPainter:QCanvasPainter'),
           )),
      ),
      'prePaint': (
          ('_ZN20QCanvasPainterWidget8prePaintEP14QCanvasPainter',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCanvasPainter:QCanvasPainter'),
           )),
      ),
      'paint': (
          ('_ZN20QCanvasPainterWidget5paintEP14QCanvasPainter',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCanvasPainter:QCanvasPainter'),
           )),
      ),
      'graphicsResourcesInvalidated': (
          ('_ZN20QCanvasPainterWidget28graphicsResourcesInvalidatedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCanvasPainterWidget::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterwidget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCanvasPainterWidget::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QCanvasPainterWidget10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def fillColor(self) -> QColor:
    """
    Calls Qt's 'QColor QCanvasPainterWidget::fillColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterwidget.html#fillColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QCanvasPainterWidget::fillColor() const
    address = self.uglySide.call(
        'ritual_ZNK20QCanvasPainterWidget9fillColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def hasSharedPainter(self) -> bool:
    """
    Calls Qt's 'bool QCanvasPainterWidget::hasSharedPainter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterwidget.html#hasSharedPainter
    """
    #  bool QCanvasPainterWidget::hasSharedPainter() const
    return self.uglySide.call(
        'ritual_ZNK20QCanvasPainterWidget16hasSharedPainterEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setFillColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QCanvasPainterWidget::setFillColor(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterwidget.html#setFillColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QCanvasPainterWidget::setFillColor(QColor color)
    self.uglySide.call(
        'ritual_ZN20QCanvasPainterWidget12setFillColorE6QColor',
        self._valueOf(color),
    )

  @overload(bool)
  def setSharedPainter(self, enable: bool) -> None:
    """
    Calls Qt's 'void QCanvasPainterWidget::setSharedPainter(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterwidget.html#setSharedPainter

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QCanvasPainterWidget::setSharedPainter(bool enable)
    self.uglySide.call(
        'ritual_ZN20QCanvasPainterWidget16setSharedPainterEb', enable,
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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasPainterWidget::QCanvasPainterWidget(QWidget *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterwidget.html#QCanvasPainterWidget

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCanvasPainterWidget::QCanvasPainterWidget(QWidget *parent)
    self._noteCreation(QCanvasPainterWidget, lambda: Rituals.call(
        'ritual_ZN20QCanvasPainterWidgetC1EP7QWidget',
        self._addressOf(parent),
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
    Calls Qt's 'void QCanvasPainterWidget::initializeResources(QCanvasPainter
    *painter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterwidget.html#initializeResources

    Parameters
    ----------

    painter : Optional[QCanvasPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCanvasPainterWidget::initializeResources(QCanvasPainter
    #      *painter)
    ritual = (
        'ritual_ZN20QCanvasPainterWidget19initializeResourcesEP14QCanvasPai'
        'nter')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QCanvasPainterWidget19initializeResourcesEP14QCan'
          'vasPainter')
    self.uglySide.call(ritual, self._addressOf(painter))

  @overload(QCanvasPainter)
  @overload(NoneType)
  def prePaint(self, painter: Optional[QCanvasPainter]) -> None:
    """
    Calls Qt's 'void QCanvasPainterWidget::prePaint(QCanvasPainter
    *painter)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainterwidget.html#prePaint

    Parameters
    ----------

    painter : Optional[QCanvasPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCanvasPainterWidget::prePaint(QCanvasPainter *painter)
    ritual = 'ritual_ZN20QCanvasPainterWidget8prePaintEP14QCanvasPainter'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QCanvasPainterWidget8prePaintEP14QCanvasPainter')
    self.uglySide.call(ritual, self._addressOf(painter))

  @overload(QCanvasPainter)
  @overload(NoneType)
  def paint(self, painter: Optional[QCanvasPainter]) -> None:
    """
    Calls Qt's 'void QCanvasPainterWidget::paint(QCanvasPainter *painter)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainterwidget.html#paint

    Parameters
    ----------

    painter : Optional[QCanvasPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCanvasPainterWidget::paint(QCanvasPainter *painter)
    ritual = 'ritual_ZN20QCanvasPainterWidget5paintEP14QCanvasPainter'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QCanvasPainterWidget5paintEP14QCanvasPainter'
    self.uglySide.call(ritual, self._addressOf(painter))

  def graphicsResourcesInvalidated(self) -> None:
    """
    Calls Qt's 'void QCanvasPainterWidget::graphicsResourcesInvalidated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterwidget.html
    """
    #  void QCanvasPainterWidget::graphicsResourcesInvalidated()
    ritual = (
        'ritual_ZN20QCanvasPainterWidget28graphicsResourcesInvalidatedEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QCanvasPainterWidget28graphicsResourcesInvalidate'
          'dEv')
    self.uglySide.call(ritual)

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def initialize(self, cb: Optional[QRhiCommandBuffer]) -> None:
    """
    Calls Qt's 'void QCanvasPainterWidget::initialize(QRhiCommandBuffer
    *cb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterwidget.html#initialize

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCanvasPainterWidget::initialize(QRhiCommandBuffer *cb)
    ritual = (
        'ritual_ZN20QCanvasPainterWidget10initializeEP17QRhiCommandBuffer')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QCanvasPainterWidget10initializeEP17QRhiCommandBu'
          'ffer')
    self.uglySide.call(ritual, self._addressOf(cb))

  @overload(QRhiCommandBuffer)
  @overload(NoneType)
  def render(self, cb: Optional[QRhiCommandBuffer]) -> None:
    """
    Calls Qt's 'void QCanvasPainterWidget::render(QRhiCommandBuffer *cb)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainterwidget.html#render

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCanvasPainterWidget::render(QRhiCommandBuffer *cb)
    ritual = 'ritual_ZN20QCanvasPainterWidget6renderEP17QRhiCommandBuffer'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QCanvasPainterWidget6renderEP17QRhiCommandBuffer')
    self.uglySide.call(ritual, self._addressOf(cb))

  def releaseResources(self) -> None:
    """
    Calls Qt's 'void QCanvasPainterWidget::releaseResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterwidget.html#releaseResources
    """
    #  void QCanvasPainterWidget::releaseResources()
    ritual = 'ritual_ZN20QCanvasPainterWidget16releaseResourcesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QCanvasPainterWidget16releaseResourcesEv'
    self.uglySide.call(ritual)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QCanvasPainterWidget::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanvaspainterwidget.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCanvasPainterWidget::event(QEvent *event)
    ritual = 'ritual_ZN20QCanvasPainterWidget5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QCanvasPainterWidget5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  def endCanvasPainting(self) -> None:
    """
    Calls Qt's 'void QCanvasPainterWidget::endCanvasPainting()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvaspainterwidget.html#endCanvasPainting
    """
    #  void QCanvasPainterWidget::endCanvasPainting()
    self.uglySide.call(
        'ritual_ZN20QCanvasPainterWidget17endCanvasPaintingEv',
    )

  @staticmethod
  def beginCanvasPainting(*__, **_) -> Never:
    """
    Qt's 'void
    QCanvasPainterWidget::beginCanvasPainting(QCanvasOffscreenCanvas
    &canvas)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCanvasPainterWidget.beginCanvasPainting' has no cute function "
        "yet. Qt's 'void "
        "QCanvasPainterWidget::beginCanvasPainting(QCanvasOffscreenCanvas "
        "&canvas)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def grabCanvas(*__, **_) -> Never:
    """
    Qt's 'QCanvasPainterWidget::grabCanvas': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QCanvasPainterWidget.grabCanvas' has no cute function yet. Qt's "
        "'QCanvasPainterWidget::grabCanvas': a template: a pattern and no "
        "single function.")

  @staticmethod
  def grabCanvasImpl(*__, **_) -> Never:
    """
    Qt's 'void QCanvasPainterWidget::grabCanvasImpl(const
    QCanvasOffscreenCanvas &canvas, const QObject *context,
    QtPrivate::QSlotObjectBase *slotObj)': names
    'QtPrivate::QSlotObjectBase', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QCanvasPainterWidget.grabCanvasImpl' has no cute function yet. "
        "Qt's 'void QCanvasPainterWidget::grabCanvasImpl(const "
        "QCanvasOffscreenCanvas &canvas, const QObject *context, "
        "QtPrivate::QSlotObjectBase *slotObj)': names "
        "'QtPrivate::QSlotObjectBase', which has no cute class yet.")
