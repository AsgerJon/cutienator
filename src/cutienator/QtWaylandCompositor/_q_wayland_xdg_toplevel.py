"""
QWaylandXdgToplevel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandxdgshell.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint, QPointF, QSize, QSizeF
  from . import QWaylandOutput, QWaylandSeat, QWaylandSurfaceRole
  from . import QWaylandXdgSurface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QSize = WAIT['QSize']
  QSizeF = WAIT['QSizeF']
  QWaylandOutput = WAIT['QWaylandOutput']
  QWaylandSeat = WAIT['QWaylandSeat']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandXdgToplevel(QObject):
  """
  The cute side of Qt's QWaylandXdgToplevel: a plain Python object standing
  in front of one C++ QWaylandXdgToplevel.

  It is built on the cute 'QObject', as Qt's QWaylandXdgToplevel is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandXdgToplevel that has a ritual and that
  Python can call so far, 42 names in all: 'metaObject', 'tr', 'xdgSurface',
  'parentToplevel', 'title', 'appId', 'maxSize', 'minSize', 'maximized',
  'fullscreen', 'resizing', 'activated', 'decorationMode', 'sizeForResize',
  'sendClose', 'sendMaximized', 'sendUnmaximized', 'sendFullscreen',
  'sendResizing', 'role', 'isModal', 'parentToplevelChanged', 'titleChanged',
  'appIdChanged', 'maxSizeChanged', 'minSizeChanged', 'startMove',
  'startResize', 'statesChanged', 'maximizedChanged', 'fullscreenChanged',
  'resizingChanged', 'activatedChanged', 'showWindowMenu', 'setMaximized',
  'unsetMaximized', 'setFullscreen', 'unsetFullscreen', 'setMinimized',
  'decorationModeChanged', 'modalChanged', 'setModal'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandXdgToplevel::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QWaylandXdgToplevel::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandXdgToplevelPrivate *QWaylandXdgToplevel::d_func()': gives
    'QWaylandXdgToplevelPrivate', which has no cute class yet.
  - Qt's 'const QWaylandXdgToplevelPrivate *QWaylandXdgToplevel::d_func()
    const': gives 'QWaylandXdgToplevelPrivate', which has no cute class yet.
  - Qt's 'QWaylandXdgToplevel::QWaylandXdgToplevel(QWaylandXdgSurface
    *xdgSurface, QWaylandResource &resource)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QWaylandXdgToplevel::~QWaylandXdgToplevel()': the destructor:
    Python never removes a C++ QWaylandXdgToplevel.
  - Qt's 'QList<QWaylandXdgToplevel::State> QWaylandXdgToplevel::states()
    const': gives a type Python has no way to take yet.
  - Qt's 'uint QWaylandXdgToplevel::sendConfigure(const QSize &size, const
    QList<State> &states)': takes a type Python has no way to hand over yet.
  - Qt's 'uint QWaylandXdgToplevel::sendConfigure(const QSize &size, const
    QList<int> &states)': takes a type Python has no way to hand over yet.
  - Qt's 'QWaylandXdgToplevel
    *QWaylandXdgToplevel::fromResource(::wl_resource *resource)': names
    '::wl_resource', which has no cute class yet.
  - Qt's 'QList<int> QWaylandXdgToplevel::statesAsInts() const': gives a type
    Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 55 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandXdgToplevel is created at the first use, not by
    'QWaylandXdgToplevel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandXdgToplevel.
  - Qt tells when it has removed the C++ QWaylandXdgToplevel. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWaylandXdgToplevel that has no cute function yet,
    '__init__', 'fromResource', 'sendConfigure', 'states', 'statesAsInts',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QWaylandXdgToplevel, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class DecorationMode(CuteNum):
    """
    The enum 'QWaylandXdgToplevel::DecorationMode' of Qt, with the 2 names Qt
    gives in it.
    """

    ClientSideDecoration = Kee[int](1)
    ServerSideDecoration = Kee[int](2)

  class State(CuteNum):
    """
    The enum 'QWaylandXdgToplevel::State' of Qt, with the 4 names Qt gives in
    it.
    """

    MaximizedState = Kee[int](1)
    FullscreenState = Kee[int](2)
    ResizingState = Kee[int](3)
    ActivatedState = Kee[int](4)

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
    Calls Qt's 'QString QWaylandXdgToplevel::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#tr

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
    #  QString QWaylandXdgToplevel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QWaylandXdgToplevel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def role() -> Optional[QWaylandSurfaceRole]:
    """
    Calls Qt's 'QWaylandSurfaceRole *QWaylandXdgToplevel::role()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#role

    Returns
    -------

    Optional[QWaylandSurfaceRole]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandSurfaceRole *QWaylandXdgToplevel::role()
    address = Rituals.call('ritual_ZN19QWaylandXdgToplevel4roleEv')
    from . import QWaylandSurfaceRole
    return QWaylandSurfaceRole._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandXdgToplevel'

  #  A C++ QWaylandXdgToplevel Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandXdgToplevel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWaylandXdgToplevel::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandXdgToplevel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QWaylandXdgToplevel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def xdgSurface(self) -> Optional[QWaylandXdgSurface]:
    """
    Calls Qt's 'QWaylandXdgSurface *QWaylandXdgToplevel::xdgSurface() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#xdgSurface

    Returns
    -------

    Optional[QWaylandXdgSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandXdgSurface *QWaylandXdgToplevel::xdgSurface() const
    address = self.uglySide.call(
        'ritual_ZNK19QWaylandXdgToplevel10xdgSurfaceEv',
    )
    from . import QWaylandXdgSurface
    return QWaylandXdgSurface._cuteAt(address)

  def parentToplevel(self) -> Optional[QWaylandXdgToplevel]:
    """
    Calls Qt's 'QWaylandXdgToplevel *QWaylandXdgToplevel::parentToplevel()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#parentToplevel

    Returns
    -------

    Optional[QWaylandXdgToplevel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandXdgToplevel *QWaylandXdgToplevel::parentToplevel() const
    address = self.uglySide.call(
        'ritual_ZNK19QWaylandXdgToplevel14parentToplevelEv',
    )
    return QWaylandXdgToplevel._cuteAt(address)

  def title(self) -> str:
    """
    Calls Qt's 'QString QWaylandXdgToplevel::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWaylandXdgToplevel::title() const
    return self.uglySide.call('ritual_ZNK19QWaylandXdgToplevel5titleEv')

  def appId(self) -> str:
    """
    Calls Qt's 'QString QWaylandXdgToplevel::appId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#appId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWaylandXdgToplevel::appId() const
    return self.uglySide.call('ritual_ZNK19QWaylandXdgToplevel5appIdEv')

  def maxSize(self) -> QSize:
    """
    Calls Qt's 'QSize QWaylandXdgToplevel::maxSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#maxSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWaylandXdgToplevel::maxSize() const
    address = self.uglySide.call('ritual_ZNK19QWaylandXdgToplevel7maxSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minSize(self) -> QSize:
    """
    Calls Qt's 'QSize QWaylandXdgToplevel::minSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#minSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWaylandXdgToplevel::minSize() const
    address = self.uglySide.call('ritual_ZNK19QWaylandXdgToplevel7minSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def maximized(self) -> bool:
    """
    Calls Qt's 'bool QWaylandXdgToplevel::maximized() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#maximized
    """
    #  bool QWaylandXdgToplevel::maximized() const
    return self.uglySide.call('ritual_ZNK19QWaylandXdgToplevel9maximizedEv')

  def fullscreen(self) -> bool:
    """
    Calls Qt's 'bool QWaylandXdgToplevel::fullscreen() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#fullscreen
    """
    #  bool QWaylandXdgToplevel::fullscreen() const
    return self.uglySide.call(
        'ritual_ZNK19QWaylandXdgToplevel10fullscreenEv',
    )

  def resizing(self) -> bool:
    """
    Calls Qt's 'bool QWaylandXdgToplevel::resizing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#resizing
    """
    #  bool QWaylandXdgToplevel::resizing() const
    return self.uglySide.call('ritual_ZNK19QWaylandXdgToplevel8resizingEv')

  def activated(self) -> bool:
    """
    Calls Qt's 'bool QWaylandXdgToplevel::activated() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#activated
    """
    #  bool QWaylandXdgToplevel::activated() const
    return self.uglySide.call('ritual_ZNK19QWaylandXdgToplevel9activatedEv')

  def decorationMode(self) -> DecorationMode:
    """
    Calls Qt's 'DecorationMode QWaylandXdgToplevel::decorationMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#decorationMode

    Returns
    -------

    DecorationMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'DecorationMode(number)'
      gives.
    """
    #  DecorationMode QWaylandXdgToplevel::decorationMode() const
    return QWaylandXdgToplevel.DecorationMode(self.uglySide.call(
        'ritual_ZNK19QWaylandXdgToplevel14decorationModeEv',
    ))

  @overload(QSizeF, QPointF, Qt.Edges)
  def sizeForResize(
      self,
      size: QSizeF,
      delta: QPointF,
      edges: Qt.Edges,
  ) -> QSize:
    """
    Calls Qt's 'QSize QWaylandXdgToplevel::sizeForResize(const QSizeF &size,
    const QPointF &delta, Qt::Edges edges) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#sizeForResize

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.

    delta : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    edges : Qt.Edges
      Passed on as its number.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWaylandXdgToplevel::sizeForResize(const QSizeF &size, const
    #      QPointF &delta, Qt::Edges edges) const
    address = self.uglySide.call(
        'ritual_ZNK19QWaylandXdgToplevel13sizeForResizeERK6QSizeFRK7QPointF'
        '6QFlagsIN2Qt4EdgeEE',
        self._valueOf(size), self._valueOf(delta, 'QPointF'), edges.value,
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def isModal(self) -> bool:
    """
    Calls Qt's 'bool QWaylandXdgToplevel::isModal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#isModal
    """
    #  bool QWaylandXdgToplevel::isModal() const
    return self.uglySide.call('ritual_ZNK19QWaylandXdgToplevel7isModalEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setMaximized(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgToplevel::setMaximized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#setMaximized
    """
    #  void QWaylandXdgToplevel::setMaximized()
    self.uglySide.call('ritual_ZN19QWaylandXdgToplevel12setMaximizedEv')

  @overload(QWaylandOutput)
  @overload(NoneType)
  def setFullscreen(self, output: Optional[QWaylandOutput]) -> None:
    """
    Calls Qt's 'void QWaylandXdgToplevel::setFullscreen(QWaylandOutput
    *output)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#setFullscreen

    Parameters
    ----------

    output : Optional[QWaylandOutput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandXdgToplevel::setFullscreen(QWaylandOutput *output)
    self.uglySide.call(
        'ritual_ZN19QWaylandXdgToplevel13setFullscreenEP14QWaylandOutput',
        self._addressOf(output),
    )

  def setMinimized(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgToplevel::setMinimized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#setMinimized
    """
    #  void QWaylandXdgToplevel::setMinimized()
    self.uglySide.call('ritual_ZN19QWaylandXdgToplevel12setMinimizedEv')

  @overload(bool)
  def setModal(self, newModal: bool) -> None:
    """
    Calls Qt's 'void QWaylandXdgToplevel::setModal(bool newModal)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#setModal

    Parameters
    ----------

    newModal : bool
      Passed on as it is.
    """
    #  void QWaylandXdgToplevel::setModal(bool newModal)
    self.uglySide.call('ritual_ZN19QWaylandXdgToplevel8setModalEb', newModal)

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
    Qt's 'QWaylandXdgToplevel::QWaylandXdgToplevel(QWaylandXdgSurface
    *xdgSurface, QWaylandResource &resource)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'QWaylandXdgToplevel.__init__' has no cute function yet. Qt's "
        "'QWaylandXdgToplevel::QWaylandXdgToplevel(QWaylandXdgSurface "
        "*xdgSurface, QWaylandResource &resource)': takes a type Python has "
        "no way to hand over yet.")

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

  def sendClose(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgToplevel::sendClose()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#sendClose
    """
    #  void QWaylandXdgToplevel::sendClose()
    self.uglySide.call('ritual_ZN19QWaylandXdgToplevel9sendCloseEv')

  @overload(QSize)
  def sendMaximized(self, size: QSize) -> int:
    """
    Calls Qt's 'uint QWaylandXdgToplevel::sendMaximized(const QSize &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#sendMaximized

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  uint QWaylandXdgToplevel::sendMaximized(const QSize &size)
    return self.uglySide.call(
        'ritual_ZN19QWaylandXdgToplevel13sendMaximizedERK5QSize',
        self._valueOf(size),
    )

  @overload()
  @overload(QSize)
  def sendUnmaximized(self, size: Optional[QSize] = None) -> int:
    """
    Calls Qt's 'uint QWaylandXdgToplevel::sendUnmaximized(const QSize
    &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#sendUnmaximized

    Parameters
    ----------

    size : Optional[QSize]
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
      May be left out, as in Qt: a new 'QSize(0, 0)' is then passed on.
    """
    #  uint QWaylandXdgToplevel::sendUnmaximized(const QSize &size)
    if size is None:
      from ..QtCore import QSize
      size = QSize(0, 0)
    return self.uglySide.call(
        'ritual_ZN19QWaylandXdgToplevel15sendUnmaximizedERK5QSize',
        self._valueOf(size),
    )

  @overload(QSize)
  def sendFullscreen(self, size: QSize) -> int:
    """
    Calls Qt's 'uint QWaylandXdgToplevel::sendFullscreen(const QSize &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#sendFullscreen

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  uint QWaylandXdgToplevel::sendFullscreen(const QSize &size)
    return self.uglySide.call(
        'ritual_ZN19QWaylandXdgToplevel14sendFullscreenERK5QSize',
        self._valueOf(size),
    )

  @overload(QSize)
  def sendResizing(self, size: QSize) -> int:
    """
    Calls Qt's 'uint QWaylandXdgToplevel::sendResizing(const QSize &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#sendResizing

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  uint QWaylandXdgToplevel::sendResizing(const QSize &size)
    return self.uglySide.call(
        'ritual_ZN19QWaylandXdgToplevel12sendResizingERK5QSize',
        self._valueOf(size),
    )

  def parentToplevelChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgToplevel::parentToplevelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#parentToplevelChanged
    """
    #  void QWaylandXdgToplevel::parentToplevelChanged()
    self.uglySide.call(
        'ritual_ZN19QWaylandXdgToplevel21parentToplevelChangedEv',
    )

  def titleChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgToplevel::titleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#titleChanged
    """
    #  void QWaylandXdgToplevel::titleChanged()
    self.uglySide.call('ritual_ZN19QWaylandXdgToplevel12titleChangedEv')

  def appIdChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgToplevel::appIdChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#appIdChanged
    """
    #  void QWaylandXdgToplevel::appIdChanged()
    self.uglySide.call('ritual_ZN19QWaylandXdgToplevel12appIdChangedEv')

  def maxSizeChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgToplevel::maxSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#maxSizeChanged
    """
    #  void QWaylandXdgToplevel::maxSizeChanged()
    self.uglySide.call('ritual_ZN19QWaylandXdgToplevel14maxSizeChangedEv')

  def minSizeChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgToplevel::minSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#minSizeChanged
    """
    #  void QWaylandXdgToplevel::minSizeChanged()
    self.uglySide.call('ritual_ZN19QWaylandXdgToplevel14minSizeChangedEv')

  @overload(QWaylandSeat)
  @overload(NoneType)
  def startMove(self, seat: Optional[QWaylandSeat]) -> None:
    """
    Calls Qt's 'void QWaylandXdgToplevel::startMove(QWaylandSeat *seat)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#startMove

    Parameters
    ----------

    seat : Optional[QWaylandSeat]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandXdgToplevel::startMove(QWaylandSeat *seat)
    self.uglySide.call(
        'ritual_ZN19QWaylandXdgToplevel9startMoveEP12QWaylandSeat',
        self._addressOf(seat),
    )

  @overload(QWaylandSeat, Qt.Edges)
  @overload(NoneType, Qt.Edges)
  def startResize(
      self,
      seat: Optional[QWaylandSeat],
      edges: Qt.Edges,
  ) -> None:
    """
    Calls Qt's 'void QWaylandXdgToplevel::startResize(QWaylandSeat *seat,
    Qt::Edges edges)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#startResize

    Parameters
    ----------

    seat : Optional[QWaylandSeat]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    edges : Qt.Edges
      Passed on as its number.
    """
    #  void QWaylandXdgToplevel::startResize(QWaylandSeat *seat, Qt::Edges
    #      edges)
    self.uglySide.call(
        'ritual_ZN19QWaylandXdgToplevel11startResizeEP12QWaylandSeat6QFlags'
        'IN2Qt4EdgeEE',
        self._addressOf(seat), edges.value,
    )

  def statesChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgToplevel::statesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#statesChanged
    """
    #  void QWaylandXdgToplevel::statesChanged()
    self.uglySide.call('ritual_ZN19QWaylandXdgToplevel13statesChangedEv')

  def maximizedChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgToplevel::maximizedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#maximizedChanged
    """
    #  void QWaylandXdgToplevel::maximizedChanged()
    self.uglySide.call('ritual_ZN19QWaylandXdgToplevel16maximizedChangedEv')

  def fullscreenChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgToplevel::fullscreenChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#fullscreenChanged
    """
    #  void QWaylandXdgToplevel::fullscreenChanged()
    self.uglySide.call('ritual_ZN19QWaylandXdgToplevel17fullscreenChangedEv')

  def resizingChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgToplevel::resizingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#resizingChanged
    """
    #  void QWaylandXdgToplevel::resizingChanged()
    self.uglySide.call('ritual_ZN19QWaylandXdgToplevel15resizingChangedEv')

  def activatedChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgToplevel::activatedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#activatedChanged
    """
    #  void QWaylandXdgToplevel::activatedChanged()
    self.uglySide.call('ritual_ZN19QWaylandXdgToplevel16activatedChangedEv')

  @overload(QWaylandSeat, QPoint)
  @overload(NoneType, QPoint)
  def showWindowMenu(
      self,
      seat: Optional[QWaylandSeat],
      localSurfacePosition: QPoint,
  ) -> None:
    """
    Calls Qt's 'void QWaylandXdgToplevel::showWindowMenu(QWaylandSeat *seat,
    const QPoint &localSurfacePosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#showWindowMenu

    Parameters
    ----------

    seat : Optional[QWaylandSeat]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    localSurfacePosition : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QWaylandXdgToplevel::showWindowMenu(QWaylandSeat *seat, const
    #      QPoint &localSurfacePosition)
    self.uglySide.call(
        'ritual_ZN19QWaylandXdgToplevel14showWindowMenuEP12QWaylandSeatRK6Q'
        'Point',
        self._addressOf(seat), self._valueOf(localSurfacePosition),
    )

  def unsetMaximized(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgToplevel::unsetMaximized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#unsetMaximized
    """
    #  void QWaylandXdgToplevel::unsetMaximized()
    self.uglySide.call('ritual_ZN19QWaylandXdgToplevel14unsetMaximizedEv')

  def unsetFullscreen(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgToplevel::unsetFullscreen()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#unsetFullscreen
    """
    #  void QWaylandXdgToplevel::unsetFullscreen()
    self.uglySide.call('ritual_ZN19QWaylandXdgToplevel15unsetFullscreenEv')

  def decorationModeChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgToplevel::decorationModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#decorationModeChanged
    """
    #  void QWaylandXdgToplevel::decorationModeChanged()
    self.uglySide.call(
        'ritual_ZN19QWaylandXdgToplevel21decorationModeChangedEv',
    )

  def modalChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgToplevel::modalChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgtoplevel.html#modalChanged
    """
    #  void QWaylandXdgToplevel::modalChanged()
    self.uglySide.call('ritual_ZN19QWaylandXdgToplevel12modalChangedEv')

  @staticmethod
  def fromResource(*__, **_) -> Never:
    """
    Qt's 'QWaylandXdgToplevel
    *QWaylandXdgToplevel::fromResource(::wl_resource *resource)': names
    '::wl_resource', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandXdgToplevel.fromResource' has no cute function yet. Qt's "
        "'QWaylandXdgToplevel "
        "*QWaylandXdgToplevel::fromResource(::wl_resource *resource)': "
        "names '::wl_resource', which has no cute class yet.")

  @staticmethod
  def sendConfigure(*__, **_) -> Never:
    """
    - Qt's 'uint QWaylandXdgToplevel::sendConfigure(const QSize &size, const
      QList<State> &states)': takes a type Python has no way to hand over
      yet.
    - Qt's 'uint QWaylandXdgToplevel::sendConfigure(const QSize &size, const
      QList<int> &states)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWaylandXdgToplevel.sendConfigure' has no cute function yet. Qt's "
        "'uint QWaylandXdgToplevel::sendConfigure(const QSize &size, const "
        "QList<State> &states)': takes a type Python has no way to hand "
        "over yet. Qt's 'uint QWaylandXdgToplevel::sendConfigure(const "
        "QSize &size, const QList<int> &states)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def states(*__, **_) -> Never:
    """
    Qt's 'QList<QWaylandXdgToplevel::State> QWaylandXdgToplevel::states()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QWaylandXdgToplevel.states' has no cute function yet. Qt's "
        "'QList<QWaylandXdgToplevel::State> QWaylandXdgToplevel::states() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def statesAsInts(*__, **_) -> Never:
    """
    Qt's 'QList<int> QWaylandXdgToplevel::statesAsInts() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QWaylandXdgToplevel.statesAsInts' has no cute function yet. Qt's "
        "'QList<int> QWaylandXdgToplevel::statesAsInts() const': gives a "
        "type Python has no way to take yet.")
