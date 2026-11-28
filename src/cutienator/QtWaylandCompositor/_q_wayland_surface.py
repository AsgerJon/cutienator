"""
QWaylandSurface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandsurface.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList
from . import QWaylandObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint, QPointF, QRectF, QSize
  from ..QtGui import QRegion
  from . import QWaylandClient, QWaylandCompositor, QWaylandDrag
  from . import QWaylandInputMethodControl, QWaylandSurfaceRole, QWaylandView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QRegion = WAIT['QRegion']
  QWaylandClient = WAIT['QWaylandClient']
  QWaylandCompositor = WAIT['QWaylandCompositor']
  QWaylandDrag = WAIT['QWaylandDrag']
  QWaylandView = WAIT['QWaylandView']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandSurface(QWaylandObject):
  """
  The cute side of Qt's QWaylandSurface: a plain Python object standing in
  front of one C++ QWaylandSurface.

  It is built on the cute 'QWaylandObject', as Qt's QWaylandSurface is built
  on Qt's QWaylandObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandSurface that has a ritual and that Python
  can call so far, 49 names in all: 'metaObject', 'tr', 'initialize',
  'isInitialized', 'client', 'role', 'hasContent', 'sourceGeometry',
  'destinationSize', 'bufferSize', 'bufferScale', 'contentOrientation',
  'origin', 'compositor', 'inputRegionContains', 'destroy', 'isDestroyed',
  'frameStarted', 'sendFrameCallbacks', 'primaryView', 'setPrimaryView',
  'views', 'markAsCursorSurface', 'isCursorSurface', 'inhibitsIdle',
  'isOpaque', 'inputMethodControl', 'updateSelection', 'hasContentChanged',
  'damaged', 'parentChanged', 'childAdded', 'sourceGeometryChanged',
  'destinationSizeChanged', 'bufferSizeChanged', 'bufferScaleChanged',
  'offsetForNextFrame', 'contentOrientationChanged', 'surfaceDestroyed',
  'originChanged', 'subsurfacePositionChanged', 'subsurfacePlaceAbove',
  'subsurfacePlaceBelow', 'dragStarted', 'cursorSurfaceChanged',
  'inhibitsIdleChanged', 'isOpaqueChanged', 'configure', 'redraw'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandSurface::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QWaylandSurface::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandSurfacePrivate *QWaylandSurface::d_func()': gives
    'QWaylandSurfacePrivate', which has no cute class yet.
  - Qt's 'const QWaylandSurfacePrivate *QWaylandSurface::d_func() const':
    gives 'QWaylandSurfacePrivate', which has no cute class yet.
  - Qt's 'void QWaylandSurface::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QWaylandSurface::~QWaylandSurface()': the destructor: Python never
    removes a C++ QWaylandSurface.
  - Qt's '::wl_client *QWaylandSurface::waylandClient() const': gives
    '::wl_client', which has no cute class yet.
  - Qt's 'bool QWaylandSurface::setRole(QWaylandSurfaceRole *role,
    wl_resource *errorResource, uint32_t errorCode)': names 'wl_resource',
    which has no cute class yet.
  - Qt's 'QWaylandSurface *QWaylandSurface::fromResource(::wl_resource
    *resource)': names '::wl_resource', which has no cute class yet.
  - Qt's 'struct wl_resource *QWaylandSurface::resource() const': gives
    'struct wl_resource', which has no cute class yet.
  - Qt's 'QWaylandSurface::QWaylandSurface(QWaylandSurfacePrivate &dptr)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 65 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandSurface is created at the first use, not by
    'QWaylandSurface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandSurface.
  - Qt tells when it has removed the C++ QWaylandSurface. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWaylandSurface that has no cute function yet,
    'fromResource', 'resource', 'setRole', 'waylandClient', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QWaylandSurface, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Origin(CuteNum):
    """
    The enum 'QWaylandSurface::Origin' of Qt, with the 2 names Qt gives in
    it.
    """

    OriginTopLeft = Kee[int](0)
    OriginBottomLeft = Kee[int](1)

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
    Calls Qt's 'QString QWaylandSurface::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandsurface.html#tr

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
    #  QString QWaylandSurface::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QWaylandSurface2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandSurface'

  #  A C++ QWaylandSurface Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandSurface'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWaylandSurface::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandsurface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandSurface::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QWaylandSurface10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isInitialized(self) -> bool:
    """
    Calls Qt's 'bool QWaylandSurface::isInitialized() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandsurface.html#isInitialized
    """
    #  bool QWaylandSurface::isInitialized() const
    return self.uglySide.call('ritual_ZNK15QWaylandSurface13isInitializedEv')

  def client(self) -> Optional[QWaylandClient]:
    """
    Calls Qt's 'QWaylandClient *QWaylandSurface::client() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandsurface.html#client

    Returns
    -------

    Optional[QWaylandClient]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandClient *QWaylandSurface::client() const
    address = self.uglySide.call('ritual_ZNK15QWaylandSurface6clientEv')
    from . import QWaylandClient
    return QWaylandClient._cuteAt(address)

  def role(self) -> Optional[QWaylandSurfaceRole]:
    """
    Calls Qt's 'QWaylandSurfaceRole *QWaylandSurface::role() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandsurface.html#role

    Returns
    -------

    Optional[QWaylandSurfaceRole]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandSurfaceRole *QWaylandSurface::role() const
    address = self.uglySide.call('ritual_ZNK15QWaylandSurface4roleEv')
    from . import QWaylandSurfaceRole
    return QWaylandSurfaceRole._cuteAt(address)

  def hasContent(self) -> bool:
    """
    Calls Qt's 'bool QWaylandSurface::hasContent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandsurface.html#hasContent
    """
    #  bool QWaylandSurface::hasContent() const
    return self.uglySide.call('ritual_ZNK15QWaylandSurface10hasContentEv')

  def sourceGeometry(self) -> QRectF:
    """
    Calls Qt's 'QRectF QWaylandSurface::sourceGeometry() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurface.html#sourceGeometry

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QWaylandSurface::sourceGeometry() const
    address = self.uglySide.call(
        'ritual_ZNK15QWaylandSurface14sourceGeometryEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def destinationSize(self) -> QSize:
    """
    Calls Qt's 'QSize QWaylandSurface::destinationSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurface.html#destinationSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWaylandSurface::destinationSize() const
    address = self.uglySide.call(
        'ritual_ZNK15QWaylandSurface15destinationSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def bufferSize(self) -> QSize:
    """
    Calls Qt's 'QSize QWaylandSurface::bufferSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandsurface.html#bufferSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWaylandSurface::bufferSize() const
    address = self.uglySide.call('ritual_ZNK15QWaylandSurface10bufferSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def bufferScale(self) -> int:
    """
    Calls Qt's 'int QWaylandSurface::bufferScale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandsurface.html#bufferScale
    """
    #  int QWaylandSurface::bufferScale() const
    return self.uglySide.call('ritual_ZNK15QWaylandSurface11bufferScaleEv')

  def contentOrientation(self) -> Qt.ScreenOrientation:
    """
    Calls Qt's 'Qt::ScreenOrientation QWaylandSurface::contentOrientation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurface.html#contentOrientation

    Returns
    -------

    Qt.ScreenOrientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ScreenOrientation(number)' gives.
    """
    #  Qt::ScreenOrientation QWaylandSurface::contentOrientation() const
    return Qt.ScreenOrientation(self.uglySide.call(
        'ritual_ZNK15QWaylandSurface18contentOrientationEv',
    ))

  def origin(self) -> Origin:
    """
    Calls Qt's 'Origin QWaylandSurface::origin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandsurface.html#origin

    Returns
    -------

    Origin
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Origin(number)' gives.
    """
    #  Origin QWaylandSurface::origin() const
    return QWaylandSurface.Origin(self.uglySide.call(
        'ritual_ZNK15QWaylandSurface6originEv',
    ))

  def compositor(self) -> Optional[QWaylandCompositor]:
    """
    Calls Qt's 'QWaylandCompositor *QWaylandSurface::compositor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandsurface.html#compositor

    Returns
    -------

    Optional[QWaylandCompositor]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandCompositor *QWaylandSurface::compositor() const
    address = self.uglySide.call('ritual_ZNK15QWaylandSurface10compositorEv')
    from . import QWaylandCompositor
    return QWaylandCompositor._cuteAt(address)

  @overload(QPoint)
  def inputRegionContains(self, p: QPoint) -> bool:
    """
    Calls Qt's 'bool QWaylandSurface::inputRegionContains(const QPoint &p)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurface.html#inputRegionContains

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool QWaylandSurface::inputRegionContains(const QPoint &p) const
    return self.uglySide.call(
        'ritual_ZNK15QWaylandSurface19inputRegionContainsERK6QPoint',
        self._valueOf(p),
    )

  @overload(QPointF)
  def inputRegionContains(self, position: QPointF) -> bool:
    """
    Calls Qt's 'bool QWaylandSurface::inputRegionContains(const QPointF
    &position) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurface.html#inputRegionContains

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QWaylandSurface::inputRegionContains(const QPointF &position)
    #      const
    return self.uglySide.call(
        'ritual_ZNK15QWaylandSurface19inputRegionContainsERK7QPointF',
        self._valueOf(position, 'QPointF'),
    )

  def isDestroyed(self) -> bool:
    """
    Calls Qt's 'bool QWaylandSurface::isDestroyed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandsurface.html#isDestroyed
    """
    #  bool QWaylandSurface::isDestroyed() const
    return self.uglySide.call('ritual_ZNK15QWaylandSurface11isDestroyedEv')

  def primaryView(self) -> Optional[QWaylandView]:
    """
    Calls Qt's 'QWaylandView *QWaylandSurface::primaryView() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandsurface.html#primaryView

    Returns
    -------

    Optional[QWaylandView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandView *QWaylandSurface::primaryView() const
    address = self.uglySide.call(
        'ritual_ZNK15QWaylandSurface11primaryViewEv',
    )
    from . import QWaylandView
    return QWaylandView._cuteAt(address)

  def views(self) -> QList[QWaylandView]:
    """
    Calls Qt's 'QList<QWaylandView *> QWaylandSurface::views() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandsurface.html#views

    Returns
    -------

    QList[QWaylandView]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QWaylandView *> QWaylandSurface::views() const
    address = self.uglySide.call('ritual_ZNK15QWaylandSurface5viewsEv')
    from . import QWaylandView
    return QList[QWaylandView]._cuteOwning(address)

  def isCursorSurface(self) -> bool:
    """
    Calls Qt's 'bool QWaylandSurface::isCursorSurface() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurface.html#isCursorSurface
    """
    #  bool QWaylandSurface::isCursorSurface() const
    return self.uglySide.call(
        'ritual_ZNK15QWaylandSurface15isCursorSurfaceEv',
    )

  def inhibitsIdle(self) -> bool:
    """
    Calls Qt's 'bool QWaylandSurface::inhibitsIdle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandsurface.html#inhibitsIdle
    """
    #  bool QWaylandSurface::inhibitsIdle() const
    return self.uglySide.call('ritual_ZNK15QWaylandSurface12inhibitsIdleEv')

  def isOpaque(self) -> bool:
    """
    Calls Qt's 'bool QWaylandSurface::isOpaque() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandsurface.html#isOpaque
    """
    #  bool QWaylandSurface::isOpaque() const
    return self.uglySide.call('ritual_ZNK15QWaylandSurface8isOpaqueEv')

  def inputMethodControl(self) -> Optional[QWaylandInputMethodControl]:
    """
    Calls Qt's 'QWaylandInputMethodControl
    *QWaylandSurface::inputMethodControl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurface.html#inputMethodControl

    Returns
    -------

    Optional[QWaylandInputMethodControl]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandInputMethodControl *QWaylandSurface::inputMethodControl()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK15QWaylandSurface18inputMethodControlEv',
    )
    from . import QWaylandInputMethodControl
    return QWaylandInputMethodControl._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWaylandView)
  @overload(NoneType)
  def setPrimaryView(self, view: Optional[QWaylandView]) -> None:
    """
    Calls Qt's 'void QWaylandSurface::setPrimaryView(QWaylandView *view)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurface.html#setPrimaryView

    Parameters
    ----------

    view : Optional[QWaylandView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandSurface::setPrimaryView(QWaylandView *view)
    self.uglySide.call(
        'ritual_ZN15QWaylandSurface14setPrimaryViewEP12QWaylandView',
        self._addressOf(view),
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
    Notes what was given, for Qt's 'QWaylandSurface::QWaylandSurface()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurface.html#QWaylandSurface
    """
    #  QWaylandSurface::QWaylandSurface()
    self._noteCreation(QWaylandSurface, lambda: Rituals.call(
        'ritual_ZN15QWaylandSurfaceC1Ev',
    ))

  @overload(QWaylandCompositor, QWaylandClient, int, int)
  @overload(QWaylandCompositor, NoneType, int, int)
  @overload(NoneType, QWaylandClient, int, int)
  @overload(NoneType, NoneType, int, int)
  def __init__(
      self,
      compositor: Optional[QWaylandCompositor],
      client: Optional[QWaylandClient],
      id: int,
      version: int,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandSurface::QWaylandSurface(QWaylandCompositor *compositor,
    QWaylandClient *client, uint id, int version)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurface.html#QWaylandSurface

    Parameters
    ----------

    compositor : Optional[QWaylandCompositor]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    client : Optional[QWaylandClient]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : int
      Passed on as it is.

    version : int
      Passed on as it is.
    """
    #  QWaylandSurface::QWaylandSurface(QWaylandCompositor *compositor,
    #      QWaylandClient *client, uint id, int version)
    self._noteCreation(QWaylandSurface, lambda: Rituals.call(
        'ritual_ZN15QWaylandSurfaceC1EP18QWaylandCompositorP14QWaylandClien'
        'tji',
        self._addressOf(compositor), self._addressOf(client), id, version,
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

  @overload(QWaylandCompositor, QWaylandClient, int, int)
  @overload(QWaylandCompositor, NoneType, int, int)
  @overload(NoneType, QWaylandClient, int, int)
  @overload(NoneType, NoneType, int, int)
  def initialize(
      self,
      compositor: Optional[QWaylandCompositor],
      client: Optional[QWaylandClient],
      id: int,
      version: int,
  ) -> None:
    """
    Calls Qt's 'void QWaylandSurface::initialize(QWaylandCompositor
    *compositor, QWaylandClient *client, uint id, int version)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandsurface.html#initialize

    Parameters
    ----------

    compositor : Optional[QWaylandCompositor]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    client : Optional[QWaylandClient]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    id : int
      Passed on as it is.

    version : int
      Passed on as it is.
    """
    #  void QWaylandSurface::initialize(QWaylandCompositor *compositor,
    #      QWaylandClient *client, uint id, int version)
    self.uglySide.call(
        'ritual_ZN15QWaylandSurface10initializeEP18QWaylandCompositorP14QWa'
        'ylandClientji',
        self._addressOf(compositor), self._addressOf(client), id, version,
    )

  def destroy(self) -> None:
    """
    Calls Qt's 'void QWaylandSurface::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandsurface.html#destroy
    """
    #  void QWaylandSurface::destroy()
    self.uglySide.call('ritual_ZN15QWaylandSurface7destroyEv')

  def frameStarted(self) -> None:
    """
    Calls Qt's 'void QWaylandSurface::frameStarted()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandsurface.html#frameStarted
    """
    #  void QWaylandSurface::frameStarted()
    self.uglySide.call('ritual_ZN15QWaylandSurface12frameStartedEv')

  def sendFrameCallbacks(self) -> None:
    """
    Calls Qt's 'void QWaylandSurface::sendFrameCallbacks()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurface.html#sendFrameCallbacks
    """
    #  void QWaylandSurface::sendFrameCallbacks()
    self.uglySide.call('ritual_ZN15QWaylandSurface18sendFrameCallbacksEv')

  @overload(bool)
  def markAsCursorSurface(self, cursorSurface: bool) -> None:
    """
    Calls Qt's 'void QWaylandSurface::markAsCursorSurface(bool
    cursorSurface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurface.html#markAsCursorSurface

    Parameters
    ----------

    cursorSurface : bool
      Passed on as it is.
    """
    #  void QWaylandSurface::markAsCursorSurface(bool cursorSurface)
    self.uglySide.call(
        'ritual_ZN15QWaylandSurface19markAsCursorSurfaceEb', cursorSurface,
    )

  def updateSelection(self) -> None:
    """
    Calls Qt's 'void QWaylandSurface::updateSelection()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurface.html#updateSelection
    """
    #  void QWaylandSurface::updateSelection()
    self.uglySide.call('ritual_ZN15QWaylandSurface15updateSelectionEv')

  def hasContentChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandSurface::hasContentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurface.html#hasContentChanged
    """
    #  void QWaylandSurface::hasContentChanged()
    self.uglySide.call('ritual_ZN15QWaylandSurface17hasContentChangedEv')

  @overload(QRegion)
  def damaged(self, rect: QRegion) -> None:
    """
    Calls Qt's 'void QWaylandSurface::damaged(const QRegion &rect)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandsurface.html#damaged

    Parameters
    ----------

    rect : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QWaylandSurface::damaged(const QRegion &rect)
    self.uglySide.call(
        'ritual_ZN15QWaylandSurface7damagedERK7QRegion', self._valueOf(rect),
    )

  @overload(THIS, THIS)
  @overload(THIS, NoneType)
  @overload(NoneType, THIS)
  @overload(NoneType, NoneType)
  def parentChanged(
      self,
      newParent: Optional[QWaylandSurface],
      oldParent: Optional[QWaylandSurface],
  ) -> None:
    """
    Calls Qt's 'void QWaylandSurface::parentChanged(QWaylandSurface
    *newParent, QWaylandSurface *oldParent)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandsurface.html#parentChanged

    Parameters
    ----------

    newParent : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldParent : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandSurface::parentChanged(QWaylandSurface *newParent,
    #      QWaylandSurface *oldParent)
    self.uglySide.call(
        'ritual_ZN15QWaylandSurface13parentChangedEPS_S0_',
        self._addressOf(newParent), self._addressOf(oldParent),
    )

  @overload(THIS)
  @overload(NoneType)
  def childAdded(self, child: Optional[QWaylandSurface]) -> None:
    """
    Calls Qt's 'void QWaylandSurface::childAdded(QWaylandSurface *child)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandsurface.html#childAdded

    Parameters
    ----------

    child : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandSurface::childAdded(QWaylandSurface *child)
    self.uglySide.call(
        'ritual_ZN15QWaylandSurface10childAddedEPS_', self._addressOf(child),
    )

  def sourceGeometryChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandSurface::sourceGeometryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurface.html#sourceGeometryChanged
    """
    #  void QWaylandSurface::sourceGeometryChanged()
    self.uglySide.call('ritual_ZN15QWaylandSurface21sourceGeometryChangedEv')

  def destinationSizeChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandSurface::destinationSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurface.html#destinationSizeChanged
    """
    #  void QWaylandSurface::destinationSizeChanged()
    self.uglySide.call(
        'ritual_ZN15QWaylandSurface22destinationSizeChangedEv',
    )

  def bufferSizeChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandSurface::bufferSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurface.html#bufferSizeChanged
    """
    #  void QWaylandSurface::bufferSizeChanged()
    self.uglySide.call('ritual_ZN15QWaylandSurface17bufferSizeChangedEv')

  def bufferScaleChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandSurface::bufferScaleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurface.html#bufferScaleChanged
    """
    #  void QWaylandSurface::bufferScaleChanged()
    self.uglySide.call('ritual_ZN15QWaylandSurface18bufferScaleChangedEv')

  @overload(QPoint)
  def offsetForNextFrame(self, offset: QPoint) -> None:
    """
    Calls Qt's 'void QWaylandSurface::offsetForNextFrame(const QPoint
    &offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurface.html#offsetForNextFrame

    Parameters
    ----------

    offset : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QWaylandSurface::offsetForNextFrame(const QPoint &offset)
    self.uglySide.call(
        'ritual_ZN15QWaylandSurface18offsetForNextFrameERK6QPoint',
        self._valueOf(offset),
    )

  def contentOrientationChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandSurface::contentOrientationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurface.html#contentOrientationChanged
    """
    #  void QWaylandSurface::contentOrientationChanged()
    self.uglySide.call(
        'ritual_ZN15QWaylandSurface25contentOrientationChangedEv',
    )

  def surfaceDestroyed(self) -> None:
    """
    Calls Qt's 'void QWaylandSurface::surfaceDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurface.html#surfaceDestroyed
    """
    #  void QWaylandSurface::surfaceDestroyed()
    self.uglySide.call('ritual_ZN15QWaylandSurface16surfaceDestroyedEv')

  def originChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandSurface::originChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandsurface.html#originChanged
    """
    #  void QWaylandSurface::originChanged()
    self.uglySide.call('ritual_ZN15QWaylandSurface13originChangedEv')

  @overload(QPoint)
  def subsurfacePositionChanged(self, position: QPoint) -> None:
    """
    Calls Qt's 'void QWaylandSurface::subsurfacePositionChanged(const QPoint
    &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurface.html#subsurfacePositionChanged

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QWaylandSurface::subsurfacePositionChanged(const QPoint
    #      &position)
    self.uglySide.call(
        'ritual_ZN15QWaylandSurface25subsurfacePositionChangedERK6QPoint',
        self._valueOf(position),
    )

  @overload(THIS)
  @overload(NoneType)
  def subsurfacePlaceAbove(self, sibling: Optional[QWaylandSurface]) -> None:
    """
    Calls Qt's 'void QWaylandSurface::subsurfacePlaceAbove(QWaylandSurface
    *sibling)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurface.html#subsurfacePlaceAbove

    Parameters
    ----------

    sibling : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandSurface::subsurfacePlaceAbove(QWaylandSurface *sibling)
    self.uglySide.call(
        'ritual_ZN15QWaylandSurface20subsurfacePlaceAboveEPS_',
        self._addressOf(sibling),
    )

  @overload(THIS)
  @overload(NoneType)
  def subsurfacePlaceBelow(self, sibling: Optional[QWaylandSurface]) -> None:
    """
    Calls Qt's 'void QWaylandSurface::subsurfacePlaceBelow(QWaylandSurface
    *sibling)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurface.html#subsurfacePlaceBelow

    Parameters
    ----------

    sibling : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandSurface::subsurfacePlaceBelow(QWaylandSurface *sibling)
    self.uglySide.call(
        'ritual_ZN15QWaylandSurface20subsurfacePlaceBelowEPS_',
        self._addressOf(sibling),
    )

  @overload(QWaylandDrag)
  @overload(NoneType)
  def dragStarted(self, drag: Optional[QWaylandDrag]) -> None:
    """
    Calls Qt's 'void QWaylandSurface::dragStarted(QWaylandDrag *drag)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandsurface.html#dragStarted

    Parameters
    ----------

    drag : Optional[QWaylandDrag]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandSurface::dragStarted(QWaylandDrag *drag)
    self.uglySide.call(
        'ritual_ZN15QWaylandSurface11dragStartedEP12QWaylandDrag',
        self._addressOf(drag),
    )

  def cursorSurfaceChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandSurface::cursorSurfaceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurface.html#cursorSurfaceChanged
    """
    #  void QWaylandSurface::cursorSurfaceChanged()
    self.uglySide.call('ritual_ZN15QWaylandSurface20cursorSurfaceChangedEv')

  def inhibitsIdleChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandSurface::inhibitsIdleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurface.html#inhibitsIdleChanged
    """
    #  void QWaylandSurface::inhibitsIdleChanged()
    self.uglySide.call('ritual_ZN15QWaylandSurface19inhibitsIdleChangedEv')

  def isOpaqueChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandSurface::isOpaqueChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandsurface.html#isOpaqueChanged
    """
    #  void QWaylandSurface::isOpaqueChanged()
    self.uglySide.call('ritual_ZN15QWaylandSurface15isOpaqueChangedEv')

  @overload(bool)
  def configure(self, hasBuffer: bool) -> None:
    """
    Calls Qt's 'void QWaylandSurface::configure(bool hasBuffer)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandsurface.html#configure

    Parameters
    ----------

    hasBuffer : bool
      Passed on as it is.
    """
    #  void QWaylandSurface::configure(bool hasBuffer)
    self.uglySide.call('ritual_ZN15QWaylandSurface9configureEb', hasBuffer)

  def redraw(self) -> None:
    """
    Calls Qt's 'void QWaylandSurface::redraw()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandsurface.html#redraw
    """
    #  void QWaylandSurface::redraw()
    self.uglySide.call('ritual_ZN15QWaylandSurface6redrawEv')

  @staticmethod
  def fromResource(*__, **_) -> Never:
    """
    Qt's 'QWaylandSurface *QWaylandSurface::fromResource(::wl_resource
    *resource)': names '::wl_resource', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandSurface.fromResource' has no cute function yet. Qt's "
        "'QWaylandSurface *QWaylandSurface::fromResource(::wl_resource "
        "*resource)': names '::wl_resource', which has no cute class yet.")

  @staticmethod
  def resource(*__, **_) -> Never:
    """
    Qt's 'struct wl_resource *QWaylandSurface::resource() const': gives
    'struct wl_resource', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandSurface.resource' has no cute function yet. Qt's 'struct "
        "wl_resource *QWaylandSurface::resource() const': gives 'struct "
        "wl_resource', which has no cute class yet.")

  @staticmethod
  def setRole(*__, **_) -> Never:
    """
    Qt's 'bool QWaylandSurface::setRole(QWaylandSurfaceRole *role,
    wl_resource *errorResource, uint32_t errorCode)': names 'wl_resource',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandSurface.setRole' has no cute function yet. Qt's 'bool "
        "QWaylandSurface::setRole(QWaylandSurfaceRole *role, wl_resource "
        "*errorResource, uint32_t errorCode)': names 'wl_resource', which "
        "has no cute class yet.")

  @staticmethod
  def waylandClient(*__, **_) -> Never:
    """
    Qt's '::wl_client *QWaylandSurface::waylandClient() const': gives
    '::wl_client', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandSurface.waylandClient' has no cute function yet. Qt's "
        "'::wl_client *QWaylandSurface::waylandClient() const': gives "
        "'::wl_client', which has no cute class yet.")


#  Qt's 'QList<QWaylandSurface *>': the list of QWaylandSurface, which
#  'QList[QWaylandSurface]' gives. It is made here, so that there is one as
#  soon as there can be a QWaylandSurface.
QList.createKind(
    QWaylandSurface, 'address',
    make='ritual_list_make_QWaylandSurface_ptr',
    add='ritual_list_add_QWaylandSurface_ptr',
    size='ritual_list_size_QWaylandSurface_ptr',
    at='ritual_list_at_QWaylandSurface_ptr',
    drop='ritual_list_drop_QWaylandSurface_ptr',
)
