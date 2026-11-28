"""
QWaylandXdgSurface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandxdgshell.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QRect
  from . import QWaylandQuickShellIntegration, QWaylandQuickShellSurfaceItem
  from . import QWaylandResource, QWaylandSurface, QWaylandXdgPopup
  from . import QWaylandXdgShell, QWaylandXdgToplevel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWaylandQuickShellSurfaceItem = WAIT['QWaylandQuickShellSurfaceItem']
  QWaylandResource = WAIT['QWaylandResource']
  QWaylandSurface = WAIT['QWaylandSurface']
  QWaylandXdgShell = WAIT['QWaylandXdgShell']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandXdgSurface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWaylandXdgSurface: a plain Python object standing in
  front of one C++ QWaylandXdgSurface.

  What exists
  -----------

  Every function of Qt's QWaylandXdgSurface that has a ritual and that Python
  can call so far, 18 names in all: 'metaObject', 'tr', 'initialize',
  'windowType', 'shell', 'surface', 'toplevel', 'popup', 'windowGeometry',
  'interfaceName', 'createIntegration', 'shellChanged', 'surfaceChanged',
  'toplevelCreated', 'popupCreated', 'windowGeometryChanged',
  'handleSurfaceSizeChanged', 'handleBufferScaleChanged'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandXdgSurface::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QWaylandXdgSurface::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandXdgSurfacePrivate *QWaylandXdgSurface::d_func()': gives
    'QWaylandXdgSurfacePrivate', which has no cute class yet.
  - Qt's 'const QWaylandXdgSurfacePrivate *QWaylandXdgSurface::d_func()
    const': gives 'QWaylandXdgSurfacePrivate', which has no cute class yet.
  - Qt's 'QQmlListProperty<QObject> QWaylandXdgSurface::data()': gives a type
    Python has no way to take yet.
  - Qt's 'void QWaylandXdgSurface::appendFunction(QQmlListProperty<QObject>
    *list, QObject *object)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
  - Qt's 'qsizetype
    QWaylandXdgSurface::countFunction(QQmlListProperty<QObject> *list)':
    names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'QObject *QWaylandXdgSurface::atFunction(QQmlListProperty<QObject>
    *list, qsizetype index)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
  - Qt's 'void QWaylandXdgSurface::clearFunction(QQmlListProperty<QObject>
    *list)': names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'const struct wl_interface *QWaylandXdgSurface::interface()': gives
    'struct wl_interface', which has no cute class yet.
  - Qt's 'QWaylandXdgSurface *QWaylandXdgSurface::fromResource(::wl_resource
    *resource)': names '::wl_resource', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 34 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandXdgSurface is created at the first use, not by
    'QWaylandXdgSurface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandXdgSurface.
  - Each name of Qt's QWaylandXdgSurface that has no cute function yet,
    'appendFunction', 'atFunction', 'clearFunction', 'countFunction',
    'd_func', 'data', 'fromResource', 'interface', holds a function that
    raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QWaylandXdgSurface::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgsurface.html#tr

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
    #  QString QWaylandXdgSurface::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QWaylandXdgSurface2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def interfaceName() -> QByteArray:
    """
    Calls Qt's 'QByteArray QWaylandXdgSurface::interfaceName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgsurface.html#interfaceName

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QWaylandXdgSurface::interfaceName()
    address = Rituals.call('ritual_ZN18QWaylandXdgSurface13interfaceNameEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandXdgSurface'

  #  The functions Qt calls itself that QWaylandXdgSurface is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'windowType': (
          ('_ZNK18QWaylandXdgSurface10windowTypeEv',
           ('int', 'enum', 'QtCore:Qt.WindowType'),
           ()),
      ),
      'createIntegration': (
          ('_ZN18QWaylandXdgSurface17createIntegrationEP29QWaylandQuickShel'
           'lSurfaceItem',
           ('address', 'address',
            'QtWaylandCompositor:QWaylandQuickShellIntegration'),
           (
               ('address', 'address',
                'QtWaylandCompositor:QWaylandQuickShellSurfaceItem'),
           )),
      ),
      'initialize': (
          ('_ZN18QWaylandXdgSurface10initializeEv',
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
    Calls Qt's 'const QMetaObject *QWaylandXdgSurface::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgsurface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandXdgSurface::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QWaylandXdgSurface10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def windowType(self) -> Qt.WindowType:
    """
    Calls Qt's 'Qt::WindowType QWaylandXdgSurface::windowType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgsurface.html#windowType

    Returns
    -------

    Qt.WindowType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.WindowType(number)'
      gives.
    """
    #  Qt::WindowType QWaylandXdgSurface::windowType() const
    ritual = 'ritual_ZNK18QWaylandXdgSurface10windowTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QWaylandXdgSurface10windowTypeEv'
    return Qt.WindowType(self.uglySide.call(ritual))

  def shell(self) -> Optional[QWaylandXdgShell]:
    """
    Calls Qt's 'QWaylandXdgShell *QWaylandXdgSurface::shell() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgsurface.html#shell

    Returns
    -------

    Optional[QWaylandXdgShell]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandXdgShell *QWaylandXdgSurface::shell() const
    address = self.uglySide.call('ritual_ZNK18QWaylandXdgSurface5shellEv')
    from . import QWaylandXdgShell
    return QWaylandXdgShell._cuteAt(address)

  def surface(self) -> Optional[QWaylandSurface]:
    """
    Calls Qt's 'QWaylandSurface *QWaylandXdgSurface::surface() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgsurface.html#surface

    Returns
    -------

    Optional[QWaylandSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandSurface *QWaylandXdgSurface::surface() const
    address = self.uglySide.call('ritual_ZNK18QWaylandXdgSurface7surfaceEv')
    from . import QWaylandSurface
    return QWaylandSurface._cuteAt(address)

  def toplevel(self) -> Optional[QWaylandXdgToplevel]:
    """
    Calls Qt's 'QWaylandXdgToplevel *QWaylandXdgSurface::toplevel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgsurface.html#toplevel

    Returns
    -------

    Optional[QWaylandXdgToplevel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandXdgToplevel *QWaylandXdgSurface::toplevel() const
    address = self.uglySide.call('ritual_ZNK18QWaylandXdgSurface8toplevelEv')
    from . import QWaylandXdgToplevel
    return QWaylandXdgToplevel._cuteAt(address)

  def popup(self) -> Optional[QWaylandXdgPopup]:
    """
    Calls Qt's 'QWaylandXdgPopup *QWaylandXdgSurface::popup() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgsurface.html#popup

    Returns
    -------

    Optional[QWaylandXdgPopup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandXdgPopup *QWaylandXdgSurface::popup() const
    address = self.uglySide.call('ritual_ZNK18QWaylandXdgSurface5popupEv')
    from . import QWaylandXdgPopup
    return QWaylandXdgPopup._cuteAt(address)

  def windowGeometry(self) -> QRect:
    """
    Calls Qt's 'QRect QWaylandXdgSurface::windowGeometry() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgsurface.html#windowGeometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWaylandXdgSurface::windowGeometry() const
    address = self.uglySide.call(
        'ritual_ZNK18QWaylandXdgSurface14windowGeometryEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

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
    'QWaylandXdgSurface::QWaylandXdgSurface()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgsurface.html#QWaylandXdgSurface
    """
    #  QWaylandXdgSurface::QWaylandXdgSurface()
    self._noteCreation(QWaylandXdgSurface, lambda: Rituals.call(
        'ritual_ZN18QWaylandXdgSurfaceC1Ev',
    ))

  @overload(QWaylandXdgShell, QWaylandSurface, QWaylandResource)
  @overload(QWaylandXdgShell, NoneType, QWaylandResource)
  @overload(NoneType, QWaylandSurface, QWaylandResource)
  @overload(NoneType, NoneType, QWaylandResource)
  def __init__(
      self,
      xdgShell: Optional[QWaylandXdgShell],
      surface: Optional[QWaylandSurface],
      resource: QWaylandResource,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandXdgSurface::QWaylandXdgSurface(QWaylandXdgShell *xdgShell,
    QWaylandSurface *surface, const QWaylandResource &resource)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgsurface.html#QWaylandXdgSurface

    Parameters
    ----------

    xdgShell : Optional[QWaylandXdgShell]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resource : QWaylandResource
      Passed on as a value: Qt reads the C++ QWaylandResource, which stays
      Python's own.
    """
    #  QWaylandXdgSurface::QWaylandXdgSurface(QWaylandXdgShell *xdgShell,
    #      QWaylandSurface *surface, const QWaylandResource &resource)
    self._noteCreation(QWaylandXdgSurface, lambda: Rituals.call(
        'ritual_ZN18QWaylandXdgSurfaceC1EP16QWaylandXdgShellP15QWaylandSurf'
        'aceRK16QWaylandResource',
        self._addressOf(xdgShell), self._addressOf(surface),
        self._valueOf(resource),
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

  @overload(QWaylandXdgShell, QWaylandSurface, QWaylandResource)
  @overload(QWaylandXdgShell, NoneType, QWaylandResource)
  @overload(NoneType, QWaylandSurface, QWaylandResource)
  @overload(NoneType, NoneType, QWaylandResource)
  def initialize(
      self,
      xdgShell: Optional[QWaylandXdgShell],
      surface: Optional[QWaylandSurface],
      resource: QWaylandResource,
  ) -> None:
    """
    Calls Qt's 'void QWaylandXdgSurface::initialize(QWaylandXdgShell
    *xdgShell, QWaylandSurface *surface, const QWaylandResource &resource)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgsurface.html#initialize

    Parameters
    ----------

    xdgShell : Optional[QWaylandXdgShell]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resource : QWaylandResource
      Passed on as a value: Qt reads the C++ QWaylandResource, which stays
      Python's own.
    """
    #  void QWaylandXdgSurface::initialize(QWaylandXdgShell *xdgShell,
    #      QWaylandSurface *surface, const QWaylandResource &resource)
    self.uglySide.call(
        'ritual_ZN18QWaylandXdgSurface10initializeEP16QWaylandXdgShellP15QW'
        'aylandSurfaceRK16QWaylandResource',
        self._addressOf(xdgShell), self._addressOf(surface),
        self._valueOf(resource),
    )

  @overload()
  def initialize(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgSurface::initialize()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgsurface.html#initialize
    """
    #  void QWaylandXdgSurface::initialize()
    ritual = 'ritual_ZN18QWaylandXdgSurface10initializeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QWaylandXdgSurface10initializeEv'
    self.uglySide.call(ritual)

  @overload(QWaylandQuickShellSurfaceItem)
  @overload(NoneType)
  def createIntegration(
      self,
      item: Optional[QWaylandQuickShellSurfaceItem],
  ) -> Optional[QWaylandQuickShellIntegration]:
    """
    Calls Qt's 'QWaylandQuickShellIntegration
    *QWaylandXdgSurface::createIntegration(QWaylandQuickShellSurfaceItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgsurface.html#createIntegration

    Parameters
    ----------

    item : Optional[QWaylandQuickShellSurfaceItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWaylandQuickShellIntegration]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandQuickShellIntegration *QWaylandXdgSurface::createIntegration(
    #      QWaylandQuickShellSurfaceItem *item)
    ritual = (
        'ritual_ZN18QWaylandXdgSurface17createIntegrationEP29QWaylandQuickS'
        'hellSurfaceItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QWaylandXdgSurface17createIntegrationEP29QWayland'
          'QuickShellSurfaceItem')
    address = self.uglySide.call(ritual, self._addressOf(item))
    from . import QWaylandQuickShellIntegration
    return QWaylandQuickShellIntegration._cuteAt(address)

  def shellChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgSurface::shellChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgsurface.html#shellChanged
    """
    #  void QWaylandXdgSurface::shellChanged()
    self.uglySide.call('ritual_ZN18QWaylandXdgSurface12shellChangedEv')

  def surfaceChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgSurface::surfaceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgsurface.html#surfaceChanged
    """
    #  void QWaylandXdgSurface::surfaceChanged()
    self.uglySide.call('ritual_ZN18QWaylandXdgSurface14surfaceChangedEv')

  def toplevelCreated(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgSurface::toplevelCreated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgsurface.html#toplevelCreated
    """
    #  void QWaylandXdgSurface::toplevelCreated()
    self.uglySide.call('ritual_ZN18QWaylandXdgSurface15toplevelCreatedEv')

  def popupCreated(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgSurface::popupCreated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgsurface.html#popupCreated
    """
    #  void QWaylandXdgSurface::popupCreated()
    self.uglySide.call('ritual_ZN18QWaylandXdgSurface12popupCreatedEv')

  def windowGeometryChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgSurface::windowGeometryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgsurface.html#windowGeometryChanged
    """
    #  void QWaylandXdgSurface::windowGeometryChanged()
    self.uglySide.call(
        'ritual_ZN18QWaylandXdgSurface21windowGeometryChangedEv',
    )

  def handleSurfaceSizeChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgSurface::handleSurfaceSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgsurface.html#handleSurfaceSizeChanged
    """
    #  void QWaylandXdgSurface::handleSurfaceSizeChanged()
    self.uglySide.call(
        'ritual_ZN18QWaylandXdgSurface24handleSurfaceSizeChangedEv',
    )

  def handleBufferScaleChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgSurface::handleBufferScaleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgsurface.html#handleBufferScaleChanged
    """
    #  void QWaylandXdgSurface::handleBufferScaleChanged()
    self.uglySide.call(
        'ritual_ZN18QWaylandXdgSurface24handleBufferScaleChangedEv',
    )

  @staticmethod
  def appendFunction(*__, **_) -> Never:
    """
    Qt's 'void QWaylandXdgSurface::appendFunction(QQmlListProperty<QObject>
    *list, QObject *object)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandXdgSurface.appendFunction' has no cute function yet. Qt's "
        "'void QWaylandXdgSurface::appendFunction(QQmlListProperty<QObject> "
        "*list, QObject *object)': names 'QQmlListProperty<QObject>', which "
        "has no cute class yet.")

  @staticmethod
  def atFunction(*__, **_) -> Never:
    """
    Qt's 'QObject *QWaylandXdgSurface::atFunction(QQmlListProperty<QObject>
    *list, qsizetype index)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandXdgSurface.atFunction' has no cute function yet. Qt's "
        "'QObject *QWaylandXdgSurface::atFunction(QQmlListProperty<QObject> "
        "*list, qsizetype index)': names 'QQmlListProperty<QObject>', which "
        "has no cute class yet.")

  @staticmethod
  def clearFunction(*__, **_) -> Never:
    """
    Qt's 'void QWaylandXdgSurface::clearFunction(QQmlListProperty<QObject>
    *list)': names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandXdgSurface.clearFunction' has no cute function yet. Qt's "
        "'void QWaylandXdgSurface::clearFunction(QQmlListProperty<QObject> "
        "*list)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def countFunction(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QWaylandXdgSurface::countFunction(QQmlListProperty<QObject> *list)':
    names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandXdgSurface.countFunction' has no cute function yet. Qt's "
        "'qsizetype "
        "QWaylandXdgSurface::countFunction(QQmlListProperty<QObject> "
        "*list)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QWaylandXdgSurfacePrivate *QWaylandXdgSurface::d_func()': gives
      'QWaylandXdgSurfacePrivate', which has no cute class yet.
    - Qt's 'const QWaylandXdgSurfacePrivate *QWaylandXdgSurface::d_func()
      const': gives 'QWaylandXdgSurfacePrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandXdgSurface.d_func' has no cute function yet. Qt's "
        "'QWaylandXdgSurfacePrivate *QWaylandXdgSurface::d_func()': gives "
        "'QWaylandXdgSurfacePrivate', which has no cute class yet. Qt's "
        "'const QWaylandXdgSurfacePrivate *QWaylandXdgSurface::d_func() "
        "const': gives 'QWaylandXdgSurfacePrivate', which has no cute class "
        "yet.")

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QWaylandXdgSurface::data()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QWaylandXdgSurface.data' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QWaylandXdgSurface::data()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def fromResource(*__, **_) -> Never:
    """
    Qt's 'QWaylandXdgSurface *QWaylandXdgSurface::fromResource(::wl_resource
    *resource)': names '::wl_resource', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandXdgSurface.fromResource' has no cute function yet. Qt's "
        "'QWaylandXdgSurface "
        "*QWaylandXdgSurface::fromResource(::wl_resource *resource)': names "
        "'::wl_resource', which has no cute class yet.")

  @staticmethod
  def interface(*__, **_) -> Never:
    """
    Qt's 'const struct wl_interface *QWaylandXdgSurface::interface()': gives
    'struct wl_interface', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandXdgSurface.interface' has no cute function yet. Qt's "
        "'const struct wl_interface *QWaylandXdgSurface::interface()': "
        "gives 'struct wl_interface', which has no cute class yet.")
