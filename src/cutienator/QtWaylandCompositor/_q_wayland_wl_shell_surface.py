"""
QWaylandWlShellSurface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandwlshell.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QPoint, QPointF, QSize
  from ..QtCore import QSizeF
  from . import QWaylandOutput, QWaylandQuickShellIntegration
  from . import QWaylandQuickShellSurfaceItem, QWaylandResource, QWaylandSeat
  from . import QWaylandSurface, QWaylandSurfaceRole, QWaylandWlShell
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QPointF = WAIT['QPointF']
  QSize = WAIT['QSize']
  QSizeF = WAIT['QSizeF']
  QWaylandOutput = WAIT['QWaylandOutput']
  QWaylandQuickShellSurfaceItem = WAIT['QWaylandQuickShellSurfaceItem']
  QWaylandResource = WAIT['QWaylandResource']
  QWaylandSeat = WAIT['QWaylandSeat']
  QWaylandSurface = WAIT['QWaylandSurface']
  QWaylandWlShell = WAIT['QWaylandWlShell']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandWlShellSurface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWaylandWlShellSurface: a plain Python object
  standing in front of one C++ QWaylandWlShellSurface.

  What exists
  -----------

  Every function of Qt's QWaylandWlShellSurface that has a ritual and that
  Python can call so far, 27 names in all: 'metaObject', 'tr', 'initialize',
  'title', 'className', 'surface', 'shell', 'windowType', 'interfaceName',
  'role', 'sizeForResize', 'sendConfigure', 'sendPopupDone',
  'createIntegration', 'ping', 'surfaceChanged', 'shellChanged',
  'titleChanged', 'classNameChanged', 'pong', 'startMove', 'startResize',
  'setDefaultToplevel', 'setTransient', 'setFullScreen', 'setPopup',
  'setMaximized'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandWlShellSurface::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QWaylandWlShellSurface::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandWlShellSurfacePrivate *QWaylandWlShellSurface::d_func()':
    gives 'QWaylandWlShellSurfacePrivate', which has no cute class yet.
  - Qt's 'const QWaylandWlShellSurfacePrivate
    *QWaylandWlShellSurface::d_func() const': gives
    'QWaylandWlShellSurfacePrivate', which has no cute class yet.
  - Qt's 'QQmlListProperty<QObject> QWaylandWlShellSurface::data()': gives a
    type Python has no way to take yet.
  - Qt's 'void
    QWaylandWlShellSurface::appendFunction(QQmlListProperty<QObject> *list,
    QObject *object)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
  - Qt's 'qsizetype
    QWaylandWlShellSurface::countFunction(QQmlListProperty<QObject> *list)':
    names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'QObject
    *QWaylandWlShellSurface::atFunction(QQmlListProperty<QObject> *list,
    qsizetype index)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
  - Qt's 'void
    QWaylandWlShellSurface::clearFunction(QQmlListProperty<QObject> *list)':
    names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'QWaylandWlShellSurface::~QWaylandWlShellSurface()': the destructor:
    Python never removes a C++ QWaylandWlShellSurface.
  - Qt's 'const struct wl_interface *QWaylandWlShellSurface::interface()':
    gives 'struct wl_interface', which has no cute class yet.
  - Qt's 'QWaylandWlShellSurface
    *QWaylandWlShellSurface::fromResource(wl_resource *res)': names
    'wl_resource', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 44 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandWlShellSurface is created at the first use, not by
    'QWaylandWlShellSurface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandWlShellSurface.
  - Each name of Qt's QWaylandWlShellSurface that has no cute function yet,
    'appendFunction', 'atFunction', 'clearFunction', 'countFunction',
    'd_func', 'data', 'fromResource', 'interface', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QWaylandWlShellSurface, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class FullScreenMethod(CuteNum):
    """
    The enum 'QWaylandWlShellSurface::FullScreenMethod' of Qt, with the 4
    names Qt gives in it.
    """

    DefaultFullScreen = Kee[int](0)
    ScaleFullScreen = Kee[int](1)
    DriverFullScreen = Kee[int](2)
    FillFullScreen = Kee[int](3)

  class ResizeEdge(CuteNum):
    """
    The enum 'QWaylandWlShellSurface::ResizeEdge' of Qt, with the 9 names Qt
    gives in it.
    """

    NoneEdge = Kee[int](0)
    TopEdge = Kee[int](1)
    BottomEdge = Kee[int](2)
    LeftEdge = Kee[int](4)
    TopLeftEdge = Kee[int](5)
    BottomLeftEdge = Kee[int](6)
    RightEdge = Kee[int](8)
    TopRightEdge = Kee[int](9)
    BottomRightEdge = Kee[int](10)

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
    Calls Qt's 'QString QWaylandWlShellSurface::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#tr

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
    #  QString QWaylandWlShellSurface::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QWaylandWlShellSurface2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def interfaceName() -> QByteArray:
    """
    Calls Qt's 'QByteArray QWaylandWlShellSurface::interfaceName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#interfaceName

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QWaylandWlShellSurface::interfaceName()
    address = Rituals.call(
        'ritual_ZN22QWaylandWlShellSurface13interfaceNameEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  def role() -> Optional[QWaylandSurfaceRole]:
    """
    Calls Qt's 'QWaylandSurfaceRole *QWaylandWlShellSurface::role()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#role

    Returns
    -------

    Optional[QWaylandSurfaceRole]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandSurfaceRole *QWaylandWlShellSurface::role()
    address = Rituals.call('ritual_ZN22QWaylandWlShellSurface4roleEv')
    from . import QWaylandSurfaceRole
    return QWaylandSurfaceRole._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandWlShellSurface'

  #  A C++ QWaylandWlShellSurface Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandWlShellSurface'

  #  The functions Qt calls itself that QWaylandWlShellSurface is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'windowType': (
          ('_ZNK22QWaylandWlShellSurface10windowTypeEv',
           ('int', 'enum', 'QtCore:Qt.WindowType'),
           ()),
      ),
      'createIntegration': (
          ('_ZN22QWaylandWlShellSurface17createIntegrationEP29QWaylandQuick'
           'ShellSurfaceItem',
           ('address', 'address',
            'QtWaylandCompositor:QWaylandQuickShellIntegration'),
           (
               ('address', 'address',
                'QtWaylandCompositor:QWaylandQuickShellSurfaceItem'),
           )),
      ),
      'initialize': (
          ('_ZN22QWaylandWlShellSurface10initializeEv',
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
    Calls Qt's 'const QMetaObject *QWaylandWlShellSurface::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandWlShellSurface::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QWaylandWlShellSurface10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def title(self) -> str:
    """
    Calls Qt's 'QString QWaylandWlShellSurface::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWaylandWlShellSurface::title() const
    return self.uglySide.call('ritual_ZNK22QWaylandWlShellSurface5titleEv')

  def className(self) -> str:
    """
    Calls Qt's 'QString QWaylandWlShellSurface::className() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#className

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWaylandWlShellSurface::className() const
    return self.uglySide.call(
        'ritual_ZNK22QWaylandWlShellSurface9classNameEv',
    )

  def surface(self) -> Optional[QWaylandSurface]:
    """
    Calls Qt's 'QWaylandSurface *QWaylandWlShellSurface::surface() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#surface

    Returns
    -------

    Optional[QWaylandSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandSurface *QWaylandWlShellSurface::surface() const
    address = self.uglySide.call(
        'ritual_ZNK22QWaylandWlShellSurface7surfaceEv',
    )
    from . import QWaylandSurface
    return QWaylandSurface._cuteAt(address)

  def shell(self) -> Optional[QWaylandWlShell]:
    """
    Calls Qt's 'QWaylandWlShell *QWaylandWlShellSurface::shell() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#shell

    Returns
    -------

    Optional[QWaylandWlShell]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandWlShell *QWaylandWlShellSurface::shell() const
    address = self.uglySide.call(
        'ritual_ZNK22QWaylandWlShellSurface5shellEv',
    )
    from . import QWaylandWlShell
    return QWaylandWlShell._cuteAt(address)

  def windowType(self) -> Qt.WindowType:
    """
    Calls Qt's 'Qt::WindowType QWaylandWlShellSurface::windowType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#windowType

    Returns
    -------

    Qt.WindowType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.WindowType(number)'
      gives.
    """
    #  Qt::WindowType QWaylandWlShellSurface::windowType() const
    ritual = 'ritual_ZNK22QWaylandWlShellSurface10windowTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QWaylandWlShellSurface10windowTypeEv'
    return Qt.WindowType(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setDefaultToplevel(self) -> None:
    """
    Calls Qt's 'void QWaylandWlShellSurface::setDefaultToplevel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#setDefaultToplevel
    """
    #  void QWaylandWlShellSurface::setDefaultToplevel()
    self.uglySide.call(
        'ritual_ZN22QWaylandWlShellSurface18setDefaultToplevelEv',
    )

  @overload(QWaylandSurface, QPoint, bool)
  @overload(NoneType, QPoint, bool)
  def setTransient(
      self,
      parentSurface: Optional[QWaylandSurface],
      relativeToParent: QPoint,
      inactive: bool,
  ) -> None:
    """
    Calls Qt's 'void QWaylandWlShellSurface::setTransient(QWaylandSurface
    *parentSurface, const QPoint &relativeToParent, bool inactive)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#setTransient

    Parameters
    ----------

    parentSurface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    relativeToParent : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    inactive : bool
      Passed on as it is.
    """
    #  void QWaylandWlShellSurface::setTransient(QWaylandSurface
    #      *parentSurface, const QPoint &relativeToParent, bool inactive)
    self.uglySide.call(
        'ritual_ZN22QWaylandWlShellSurface12setTransientEP15QWaylandSurface'
        'RK6QPointb',
        self._addressOf(parentSurface), self._valueOf(relativeToParent),
        inactive,
    )

  @overload(FullScreenMethod, int, QWaylandOutput)
  @overload(FullScreenMethod, int, NoneType)
  def setFullScreen(
      self,
      method: FullScreenMethod,
      framerate: int,
      output: Optional[QWaylandOutput],
  ) -> None:
    """
    Calls Qt's 'void QWaylandWlShellSurface::setFullScreen(FullScreenMethod
    method, uint framerate, QWaylandOutput *output)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#setFullScreen

    Parameters
    ----------

    method : FullScreenMethod
      Passed on as its number.

    framerate : int
      Passed on as it is.

    output : Optional[QWaylandOutput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandWlShellSurface::setFullScreen(FullScreenMethod method,
    #      uint framerate, QWaylandOutput *output)
    self.uglySide.call(
        'ritual_ZN22QWaylandWlShellSurface13setFullScreenENS_16FullScreenMe'
        'thodEjP14QWaylandOutput',
        method.value, framerate, self._addressOf(output),
    )

  @overload(QWaylandSeat, QWaylandSurface, QPoint)
  @overload(QWaylandSeat, NoneType, QPoint)
  @overload(NoneType, QWaylandSurface, QPoint)
  @overload(NoneType, NoneType, QPoint)
  def setPopup(
      self,
      seat: Optional[QWaylandSeat],
      parentSurface: Optional[QWaylandSurface],
      relativeToParent: QPoint,
  ) -> None:
    """
    Calls Qt's 'void QWaylandWlShellSurface::setPopup(QWaylandSeat *seat,
    QWaylandSurface *parentSurface, const QPoint &relativeToParent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#setPopup

    Parameters
    ----------

    seat : Optional[QWaylandSeat]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parentSurface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    relativeToParent : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QWaylandWlShellSurface::setPopup(QWaylandSeat *seat,
    #      QWaylandSurface *parentSurface, const QPoint &relativeToParent)
    self.uglySide.call(
        'ritual_ZN22QWaylandWlShellSurface8setPopupEP12QWaylandSeatP15QWayl'
        'andSurfaceRK6QPoint',
        self._addressOf(seat), self._addressOf(parentSurface),
        self._valueOf(relativeToParent),
    )

  @overload(QWaylandOutput)
  @overload(NoneType)
  def setMaximized(self, output: Optional[QWaylandOutput]) -> None:
    """
    Calls Qt's 'void QWaylandWlShellSurface::setMaximized(QWaylandOutput
    *output)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#setMaximized

    Parameters
    ----------

    output : Optional[QWaylandOutput]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandWlShellSurface::setMaximized(QWaylandOutput *output)
    self.uglySide.call(
        'ritual_ZN22QWaylandWlShellSurface12setMaximizedEP14QWaylandOutput',
        self._addressOf(output),
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
    'QWaylandWlShellSurface::QWaylandWlShellSurface()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#QWaylandWlShellSurface
    """
    #  QWaylandWlShellSurface::QWaylandWlShellSurface()
    self._noteCreation(QWaylandWlShellSurface, lambda: Rituals.call(
        'ritual_ZN22QWaylandWlShellSurfaceC1Ev',
    ))

  @overload(QWaylandWlShell, QWaylandSurface, QWaylandResource)
  @overload(QWaylandWlShell, NoneType, QWaylandResource)
  @overload(NoneType, QWaylandSurface, QWaylandResource)
  @overload(NoneType, NoneType, QWaylandResource)
  def __init__(
      self,
      shell: Optional[QWaylandWlShell],
      surface: Optional[QWaylandSurface],
      resource: QWaylandResource,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandWlShellSurface::QWaylandWlShellSurface(QWaylandWlShell *shell,
    QWaylandSurface *surface, const QWaylandResource &resource)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#QWaylandWlShellSurface

    Parameters
    ----------

    shell : Optional[QWaylandWlShell]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resource : QWaylandResource
      Passed on as a value: Qt reads the C++ QWaylandResource, which stays
      Python's own.
    """
    #  QWaylandWlShellSurface::QWaylandWlShellSurface(QWaylandWlShell *shell,
    #      QWaylandSurface *surface, const QWaylandResource &resource)
    self._noteCreation(QWaylandWlShellSurface, lambda: Rituals.call(
        'ritual_ZN22QWaylandWlShellSurfaceC1EP15QWaylandWlShellP15QWaylandS'
        'urfaceRK16QWaylandResource',
        self._addressOf(shell), self._addressOf(surface),
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

  @overload(QWaylandWlShell, QWaylandSurface, QWaylandResource)
  @overload(QWaylandWlShell, NoneType, QWaylandResource)
  @overload(NoneType, QWaylandSurface, QWaylandResource)
  @overload(NoneType, NoneType, QWaylandResource)
  def initialize(
      self,
      shell: Optional[QWaylandWlShell],
      surface: Optional[QWaylandSurface],
      resource: QWaylandResource,
  ) -> None:
    """
    Calls Qt's 'void QWaylandWlShellSurface::initialize(QWaylandWlShell
    *shell, QWaylandSurface *surface, const QWaylandResource &resource)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#initialize

    Parameters
    ----------

    shell : Optional[QWaylandWlShell]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resource : QWaylandResource
      Passed on as a value: Qt reads the C++ QWaylandResource, which stays
      Python's own.
    """
    #  void QWaylandWlShellSurface::initialize(QWaylandWlShell *shell,
    #      QWaylandSurface *surface, const QWaylandResource &resource)
    self.uglySide.call(
        'ritual_ZN22QWaylandWlShellSurface10initializeEP15QWaylandWlShellP1'
        '5QWaylandSurfaceRK16QWaylandResource',
        self._addressOf(shell), self._addressOf(surface),
        self._valueOf(resource),
    )

  @overload()
  def initialize(self) -> None:
    """
    Calls Qt's 'void QWaylandWlShellSurface::initialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#initialize
    """
    #  void QWaylandWlShellSurface::initialize()
    ritual = 'ritual_ZN22QWaylandWlShellSurface10initializeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QWaylandWlShellSurface10initializeEv'
    self.uglySide.call(ritual)

  @overload(QSizeF, QPointF, ResizeEdge)
  def sizeForResize(
      self,
      size: QSizeF,
      delta: QPointF,
      edges: ResizeEdge,
  ) -> QSize:
    """
    Calls Qt's 'QSize QWaylandWlShellSurface::sizeForResize(const QSizeF
    &size, const QPointF &delta, ResizeEdge edges)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#sizeForResize

    Parameters
    ----------

    size : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.

    delta : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    edges : ResizeEdge
      Passed on as its number.

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWaylandWlShellSurface::sizeForResize(const QSizeF &size, const
    #      QPointF &delta, ResizeEdge edges)
    address = self.uglySide.call(
        'ritual_ZN22QWaylandWlShellSurface13sizeForResizeERK6QSizeFRK7QPoin'
        'tFNS_10ResizeEdgeE',
        self._valueOf(size), self._valueOf(delta, 'QPointF'), edges.value,
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QSize, ResizeEdge)
  def sendConfigure(self, size: QSize, edges: ResizeEdge) -> None:
    """
    Calls Qt's 'void QWaylandWlShellSurface::sendConfigure(const QSize &size,
    ResizeEdge edges)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#sendConfigure

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    edges : ResizeEdge
      Passed on as its number.
    """
    #  void QWaylandWlShellSurface::sendConfigure(const QSize &size,
    #      ResizeEdge edges)
    self.uglySide.call(
        'ritual_ZN22QWaylandWlShellSurface13sendConfigureERK5QSizeNS_10Resi'
        'zeEdgeE',
        self._valueOf(size), edges.value,
    )

  def sendPopupDone(self) -> None:
    """
    Calls Qt's 'void QWaylandWlShellSurface::sendPopupDone()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#sendPopupDone
    """
    #  void QWaylandWlShellSurface::sendPopupDone()
    self.uglySide.call('ritual_ZN22QWaylandWlShellSurface13sendPopupDoneEv')

  @overload(QWaylandQuickShellSurfaceItem)
  @overload(NoneType)
  def createIntegration(
      self,
      item: Optional[QWaylandQuickShellSurfaceItem],
  ) -> Optional[QWaylandQuickShellIntegration]:
    """
    Calls Qt's 'QWaylandQuickShellIntegration
    *QWaylandWlShellSurface::createIntegration(QWaylandQuickShellSurfaceItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#createIntegration

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
    #  QWaylandQuickShellIntegration
    #      *QWaylandWlShellSurface::createIntegration(
    #      QWaylandQuickShellSurfaceItem *item)
    ritual = (
        'ritual_ZN22QWaylandWlShellSurface17createIntegrationEP29QWaylandQu'
        'ickShellSurfaceItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QWaylandWlShellSurface17createIntegrationEP29QWay'
          'landQuickShellSurfaceItem')
    address = self.uglySide.call(ritual, self._addressOf(item))
    from . import QWaylandQuickShellIntegration
    return QWaylandQuickShellIntegration._cuteAt(address)

  def ping(self) -> None:
    """
    Calls Qt's 'void QWaylandWlShellSurface::ping()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#ping
    """
    #  void QWaylandWlShellSurface::ping()
    self.uglySide.call('ritual_ZN22QWaylandWlShellSurface4pingEv')

  def surfaceChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandWlShellSurface::surfaceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#surfaceChanged
    """
    #  void QWaylandWlShellSurface::surfaceChanged()
    self.uglySide.call('ritual_ZN22QWaylandWlShellSurface14surfaceChangedEv')

  def shellChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandWlShellSurface::shellChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#shellChanged
    """
    #  void QWaylandWlShellSurface::shellChanged()
    self.uglySide.call('ritual_ZN22QWaylandWlShellSurface12shellChangedEv')

  def titleChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandWlShellSurface::titleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#titleChanged
    """
    #  void QWaylandWlShellSurface::titleChanged()
    self.uglySide.call('ritual_ZN22QWaylandWlShellSurface12titleChangedEv')

  def classNameChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandWlShellSurface::classNameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#classNameChanged
    """
    #  void QWaylandWlShellSurface::classNameChanged()
    self.uglySide.call(
        'ritual_ZN22QWaylandWlShellSurface16classNameChangedEv',
    )

  def pong(self) -> None:
    """
    Calls Qt's 'void QWaylandWlShellSurface::pong()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#pong
    """
    #  void QWaylandWlShellSurface::pong()
    self.uglySide.call('ritual_ZN22QWaylandWlShellSurface4pongEv')

  @overload(QWaylandSeat)
  @overload(NoneType)
  def startMove(self, seat: Optional[QWaylandSeat]) -> None:
    """
    Calls Qt's 'void QWaylandWlShellSurface::startMove(QWaylandSeat *seat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#startMove

    Parameters
    ----------

    seat : Optional[QWaylandSeat]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandWlShellSurface::startMove(QWaylandSeat *seat)
    self.uglySide.call(
        'ritual_ZN22QWaylandWlShellSurface9startMoveEP12QWaylandSeat',
        self._addressOf(seat),
    )

  @overload(QWaylandSeat, ResizeEdge)
  @overload(NoneType, ResizeEdge)
  def startResize(
      self,
      seat: Optional[QWaylandSeat],
      edges: ResizeEdge,
  ) -> None:
    """
    Calls Qt's 'void QWaylandWlShellSurface::startResize(QWaylandSeat *seat,
    ResizeEdge edges)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshellsurface.html#startResize

    Parameters
    ----------

    seat : Optional[QWaylandSeat]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    edges : ResizeEdge
      Passed on as its number.
    """
    #  void QWaylandWlShellSurface::startResize(QWaylandSeat *seat,
    #      ResizeEdge edges)
    self.uglySide.call(
        'ritual_ZN22QWaylandWlShellSurface11startResizeEP12QWaylandSeatNS_1'
        '0ResizeEdgeE',
        self._addressOf(seat), edges.value,
    )

  @staticmethod
  def appendFunction(*__, **_) -> Never:
    """
    Qt's 'void
    QWaylandWlShellSurface::appendFunction(QQmlListProperty<QObject> *list,
    QObject *object)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QWaylandWlShellSurface.appendFunction' has no cute function yet. "
        "Qt's 'void "
        "QWaylandWlShellSurface::appendFunction(QQmlListProperty<QObject> "
        "*list, QObject *object)': names 'QQmlListProperty<QObject>', which "
        "has no cute class yet.")

  @staticmethod
  def atFunction(*__, **_) -> Never:
    """
    Qt's 'QObject
    *QWaylandWlShellSurface::atFunction(QQmlListProperty<QObject> *list,
    qsizetype index)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QWaylandWlShellSurface.atFunction' has no cute function yet. Qt's "
        "'QObject "
        "*QWaylandWlShellSurface::atFunction(QQmlListProperty<QObject> "
        "*list, qsizetype index)': names 'QQmlListProperty<QObject>', which "
        "has no cute class yet.")

  @staticmethod
  def clearFunction(*__, **_) -> Never:
    """
    Qt's 'void
    QWaylandWlShellSurface::clearFunction(QQmlListProperty<QObject> *list)':
    names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandWlShellSurface.clearFunction' has no cute function yet. "
        "Qt's 'void "
        "QWaylandWlShellSurface::clearFunction(QQmlListProperty<QObject> "
        "*list)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def countFunction(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QWaylandWlShellSurface::countFunction(QQmlListProperty<QObject> *list)':
    names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandWlShellSurface.countFunction' has no cute function yet. "
        "Qt's 'qsizetype "
        "QWaylandWlShellSurface::countFunction(QQmlListProperty<QObject> "
        "*list)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QWaylandWlShellSurfacePrivate *QWaylandWlShellSurface::d_func()':
      gives 'QWaylandWlShellSurfacePrivate', which has no cute class yet.
    - Qt's 'const QWaylandWlShellSurfacePrivate
      *QWaylandWlShellSurface::d_func() const': gives
      'QWaylandWlShellSurfacePrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandWlShellSurface.d_func' has no cute function yet. Qt's "
        "'QWaylandWlShellSurfacePrivate *QWaylandWlShellSurface::d_func()': "
        "gives 'QWaylandWlShellSurfacePrivate', which has no cute class "
        "yet. Qt's 'const QWaylandWlShellSurfacePrivate "
        "*QWaylandWlShellSurface::d_func() const': gives "
        "'QWaylandWlShellSurfacePrivate', which has no cute class yet.")

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QWaylandWlShellSurface::data()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QWaylandWlShellSurface.data' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QWaylandWlShellSurface::data()': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def fromResource(*__, **_) -> Never:
    """
    Qt's 'QWaylandWlShellSurface
    *QWaylandWlShellSurface::fromResource(wl_resource *res)': names
    'wl_resource', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandWlShellSurface.fromResource' has no cute function yet. "
        "Qt's 'QWaylandWlShellSurface "
        "*QWaylandWlShellSurface::fromResource(wl_resource *res)': names "
        "'wl_resource', which has no cute class yet.")

  @staticmethod
  def interface(*__, **_) -> Never:
    """
    Qt's 'const struct wl_interface *QWaylandWlShellSurface::interface()':
    gives 'struct wl_interface', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandWlShellSurface.interface' has no cute function yet. Qt's "
        "'const struct wl_interface *QWaylandWlShellSurface::interface()': "
        "gives 'struct wl_interface', which has no cute class yet.")


#  Qt's 'QList<QWaylandWlShellSurface *>': the list of
#  QWaylandWlShellSurface, which 'QList[QWaylandWlShellSurface]' gives. It is
#  made here, so that there is one as soon as there can be a
#  QWaylandWlShellSurface.
QList.createKind(
    QWaylandWlShellSurface, 'address',
    make='ritual_list_make_QWaylandWlShellSurface_ptr',
    add='ritual_list_add_QWaylandWlShellSurface_ptr',
    size='ritual_list_size_QWaylandWlShellSurface_ptr',
    at='ritual_list_at_QWaylandWlShellSurface_ptr',
    drop='ritual_list_drop_QWaylandWlShellSurface_ptr',
)
