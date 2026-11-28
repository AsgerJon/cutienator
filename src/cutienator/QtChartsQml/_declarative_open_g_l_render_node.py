"""
DeclarativeOpenGLRenderNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtChartsQml/6.12.0/QtChartsQml/private/declarativeopenglrendernode_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means DeclarativeOpenGLRenderNode to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList, QObject
from ..QtGui import QOpenGLFunctions
from . import DeclarativeAbstractRenderNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRectF, QSize
  from ..QtGui import QMouseEvent
  from ..QtCharts import QXYSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMouseEvent = WAIT['QMouseEvent']
  QRectF = WAIT['QRectF']
  QSize = WAIT['QSize']
  QXYSeries = WAIT['QtCharts:QXYSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DeclarativeOpenGLRenderNode(QObject, DeclarativeAbstractRenderNode, QOpenGLFunctions):
  """
  The cute side of Qt's DeclarativeOpenGLRenderNode: a plain Python object
  standing in front of one C++ DeclarativeOpenGLRenderNode.

  It is built on the cute 'QObject', as Qt's DeclarativeOpenGLRenderNode is
  built on Qt's QObject, and has everything that class has. It is built on
  the cute 'DeclarativeAbstractRenderNode' as well, as Qt's
  DeclarativeOpenGLRenderNode is built on Qt's DeclarativeAbstractRenderNode
  too, and has everything that class has. It is built on the cute
  'QOpenGLFunctions' as well, as Qt's DeclarativeOpenGLRenderNode is built on
  Qt's QOpenGLFunctions too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's DeclarativeOpenGLRenderNode that has a ritual and
  that Python can call so far, 15 names in all: 'metaObject', 'initGL',
  'textureSize', 'setTextureSize', 'setRect', 'setAntialiasing',
  'addMouseEvents', 'render', 'renderGL', 'renderSelection', 'renderVisual',
  'recreateFBO', 'cleanXYSeriesResources', 'handleMouseEvents',
  'findSeriesAtEvent'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *DeclarativeOpenGLRenderNode::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int DeclarativeOpenGLRenderNode::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'DeclarativeOpenGLRenderNode::~DeclarativeOpenGLRenderNode()': the
    destructor: Python never removes a C++ DeclarativeOpenGLRenderNode.
  - Qt's 'void DeclarativeOpenGLRenderNode::setSeriesData(bool mapDirty,
    const GLXYDataMap &dataMap)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void DeclarativeOpenGLRenderNode::takeMouseEventResponses(
    QList<MouseEventResponse> &responses)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  4 of the 24 functions Qt declares: 2 not a gap; 2 leans on
  'DeclarativeOpenGLRenderNode.

  What to expect
  --------------

  - The C++ DeclarativeOpenGLRenderNode is created at the first use, not by
    'DeclarativeOpenGLRenderNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DeclarativeOpenGLRenderNode.
  - Qt tells when it has removed the C++ DeclarativeOpenGLRenderNode. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's DeclarativeOpenGLRenderNode that has no cute function
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
  __qt_class__ = 'DeclarativeOpenGLRenderNode'

  #  Qt's DeclarativeOpenGLRenderNode is built on more than one class. The
  #  part of a C++ DeclarativeOpenGLRenderNode that belongs to a class after
  #  the first begins somewhere inside the object, and the ritual named for
  #  that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'DeclarativeAbstractRenderNode':
          'ritual_cast_DeclarativeOpenGLRenderNode_DeclarativeAbstractRenderNode',
      'QOpenGLFunctions':
          'ritual_cast_DeclarativeOpenGLRenderNode_QOpenGLFunctions',
  }

  #  A C++ DeclarativeOpenGLRenderNode Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_DeclarativeOpenGLRenderNode'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *DeclarativeOpenGLRenderNode::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeopenglrendernode.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *DeclarativeOpenGLRenderNode::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27DeclarativeOpenGLRenderNode10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def textureSize(self) -> QSize:
    """
    Calls Qt's 'QSize DeclarativeOpenGLRenderNode::textureSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeopenglrendernode.html#textureSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize DeclarativeOpenGLRenderNode::textureSize() const
    ritual = 'ritual_ZNK27DeclarativeOpenGLRenderNode11textureSizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK27DeclarativeOpenGLRenderNode11textureSizeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSize)
  def setTextureSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void DeclarativeOpenGLRenderNode::setTextureSize(const QSize
    &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeopenglrendernode.html#setTextureSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void DeclarativeOpenGLRenderNode::setTextureSize(const QSize &size)
    ritual = (
        'ritual_ZN27DeclarativeOpenGLRenderNode14setTextureSizeERK5QSize')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27DeclarativeOpenGLRenderNode14setTextureSizeERK5QS'
          'ize')
    self.uglySide.call(ritual, self._valueOf(size))

  @overload(QRectF)
  def setRect(self, rect: QRectF) -> None:
    """
    Calls Qt's 'void DeclarativeOpenGLRenderNode::setRect(const QRectF
    &rect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeopenglrendernode.html#setRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void DeclarativeOpenGLRenderNode::setRect(const QRectF &rect)
    ritual = 'ritual_ZN27DeclarativeOpenGLRenderNode7setRectERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27DeclarativeOpenGLRenderNode7setRectERK6QRectF'
    self.uglySide.call(ritual, self._valueOf(rect))

  @overload(bool)
  def setAntialiasing(self, enable: bool) -> None:
    """
    Calls Qt's 'void DeclarativeOpenGLRenderNode::setAntialiasing(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeopenglrendernode.html#setAntialiasing

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void DeclarativeOpenGLRenderNode::setAntialiasing(bool enable)
    ritual = 'ritual_ZN27DeclarativeOpenGLRenderNode15setAntialiasingEb'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27DeclarativeOpenGLRenderNode15setAntialiasingEb')
    self.uglySide.call(ritual, enable)

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
    'DeclarativeOpenGLRenderNode::DeclarativeOpenGLRenderNode(QQuickWindow
    *window)': leans on
    'DeclarativeOpenGLRenderNode::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'DeclarativeOpenGLRenderNode.__init__' has no cute function yet. "
        "Qt's "
        "'DeclarativeOpenGLRenderNode::DeclarativeOpenGLRenderNode(QQuickWin"
        "dow *window)': leans on "
        "'DeclarativeOpenGLRenderNode::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def initGL(self) -> None:
    """
    Calls Qt's 'void DeclarativeOpenGLRenderNode::initGL()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeopenglrendernode.html#initGL
    """
    #  void DeclarativeOpenGLRenderNode::initGL()
    self.uglySide.call('ritual_ZN27DeclarativeOpenGLRenderNode6initGLEv')

  @overload(QList[QMouseEvent])
  def addMouseEvents(self, events: QList[QMouseEvent]) -> None:
    """
    Calls Qt's 'void DeclarativeOpenGLRenderNode::addMouseEvents(const
    QList<QMouseEvent *> &events)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeopenglrendernode.html#addMouseEvents

    Parameters
    ----------

    events : QList[QMouseEvent]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DeclarativeOpenGLRenderNode::addMouseEvents(const
    #      QList<QMouseEvent *> &events)
    self.uglySide.call(
        'ritual_ZN27DeclarativeOpenGLRenderNode14addMouseEventsERK5QListIP1'
        '1QMouseEventE',
        self._valueOf(events),
    )

  def render(self) -> None:
    """
    Calls Qt's 'void DeclarativeOpenGLRenderNode::render()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeopenglrendernode.html#render
    """
    #  void DeclarativeOpenGLRenderNode::render()
    self.uglySide.call('ritual_ZN27DeclarativeOpenGLRenderNode6renderEv')

  @overload(bool)
  def renderGL(self, selection: bool) -> None:
    """
    Calls Qt's 'void DeclarativeOpenGLRenderNode::renderGL(bool selection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeopenglrendernode.html#renderGL

    Parameters
    ----------

    selection : bool
      Passed on as it is.
    """
    #  void DeclarativeOpenGLRenderNode::renderGL(bool selection)
    self.uglySide.call(
        'ritual_ZN27DeclarativeOpenGLRenderNode8renderGLEb', selection,
    )

  def renderSelection(self) -> None:
    """
    Calls Qt's 'void DeclarativeOpenGLRenderNode::renderSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeopenglrendernode.html#renderSelection
    """
    #  void DeclarativeOpenGLRenderNode::renderSelection()
    self.uglySide.call(
        'ritual_ZN27DeclarativeOpenGLRenderNode15renderSelectionEv',
    )

  def renderVisual(self) -> None:
    """
    Calls Qt's 'void DeclarativeOpenGLRenderNode::renderVisual()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeopenglrendernode.html#renderVisual
    """
    #  void DeclarativeOpenGLRenderNode::renderVisual()
    self.uglySide.call(
        'ritual_ZN27DeclarativeOpenGLRenderNode12renderVisualEv',
    )

  def recreateFBO(self) -> None:
    """
    Calls Qt's 'void DeclarativeOpenGLRenderNode::recreateFBO()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeopenglrendernode.html#recreateFBO
    """
    #  void DeclarativeOpenGLRenderNode::recreateFBO()
    self.uglySide.call(
        'ritual_ZN27DeclarativeOpenGLRenderNode11recreateFBOEv',
    )

  @overload(QXYSeries)
  @overload(NoneType)
  def cleanXYSeriesResources(self, series: Optional[QXYSeries]) -> None:
    """
    Calls Qt's 'void
    DeclarativeOpenGLRenderNode::cleanXYSeriesResources(const QXYSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeopenglrendernode.html

    Parameters
    ----------

    series : Optional[QXYSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DeclarativeOpenGLRenderNode::cleanXYSeriesResources(const
    #      QXYSeries *series)
    self.uglySide.call(
        'ritual_ZN27DeclarativeOpenGLRenderNode22cleanXYSeriesResourcesEPK9'
        'QXYSeries',
        self._addressOf(series),
    )

  def handleMouseEvents(self) -> None:
    """
    Calls Qt's 'void DeclarativeOpenGLRenderNode::handleMouseEvents()'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeopenglrendernode.html#handleMouseEvents
    """
    #  void DeclarativeOpenGLRenderNode::handleMouseEvents()
    self.uglySide.call(
        'ritual_ZN27DeclarativeOpenGLRenderNode17handleMouseEventsEv',
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def findSeriesAtEvent(
      self,
      event: Optional[QMouseEvent],
  ) -> Optional[QXYSeries]:
    """
    Calls Qt's 'const QXYSeries
    *DeclarativeOpenGLRenderNode::findSeriesAtEvent(const QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/declarativeopenglrendernode.html#findSeriesAtEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QXYSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QXYSeries *DeclarativeOpenGLRenderNode::findSeriesAtEvent(const
    #      QMouseEvent *event)
    address = self.uglySide.call(
        'ritual_ZN27DeclarativeOpenGLRenderNode17findSeriesAtEventEPK11QMou'
        'seEvent',
        self._addressOf(event),
    )
    from ..QtCharts import QXYSeries
    return QXYSeries._cuteAt(address)
