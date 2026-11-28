"""
QWaylandXdgShell binding of the Qt C++
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

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject
  from . import QWaylandClient, QWaylandCompositor, QWaylandSeat
  from . import QWaylandSurface, QWaylandXdgPopup, QWaylandXdgSurface
  from . import QWaylandXdgToplevel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWaylandClient = WAIT['QWaylandClient']
  QWaylandCompositor = WAIT['QWaylandCompositor']
  QWaylandSeat = WAIT['QWaylandSeat']
  QWaylandSurface = WAIT['QWaylandSurface']
  QWaylandXdgPopup = WAIT['QWaylandXdgPopup']
  QWaylandXdgSurface = WAIT['QWaylandXdgSurface']
  QWaylandXdgToplevel = WAIT['QWaylandXdgToplevel']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandXdgShell(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWaylandXdgShell: a plain Python object standing in
  front of one C++ QWaylandXdgShell.

  What exists
  -----------

  Every function of Qt's QWaylandXdgShell that has a ritual and that Python
  can call so far, 11 names in all: 'metaObject', 'tr', 'initialize',
  'interfaceName', 'ping', 'xdgSurfaceCreated', 'toplevelCreated',
  'popupCreated', 'pong', 'handleSeatChanged', 'handleFocusChanged'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandXdgShell::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QWaylandXdgShell::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandXdgShellPrivate *QWaylandXdgShell::d_func()': gives
    'QWaylandXdgShellPrivate', which has no cute class yet.
  - Qt's 'const QWaylandXdgShellPrivate *QWaylandXdgShell::d_func() const':
    gives 'QWaylandXdgShellPrivate', which has no cute class yet.
  - Qt's 'const struct wl_interface *QWaylandXdgShell::interface()': gives
    'struct wl_interface', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandXdgShell is created at the first use, not by
    'QWaylandXdgShell(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandXdgShell.
  - Each name of Qt's QWaylandXdgShell that has no cute function yet,
    'd_func', 'interface', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QWaylandXdgShell::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgshell.html#tr

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
    #  QString QWaylandXdgShell::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QWaylandXdgShell2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def interfaceName() -> QByteArray:
    """
    Calls Qt's 'QByteArray QWaylandXdgShell::interfaceName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgshell.html#interfaceName

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QWaylandXdgShell::interfaceName()
    address = Rituals.call('ritual_ZN16QWaylandXdgShell13interfaceNameEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandXdgShell'

  #  The functions Qt calls itself that QWaylandXdgShell is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'initialize': (
          ('_ZN16QWaylandXdgShell10initializeEv',
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
    Calls Qt's 'const QMetaObject *QWaylandXdgShell::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgshell.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandXdgShell::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QWaylandXdgShell10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Notes what was given, for Qt's 'QWaylandXdgShell::QWaylandXdgShell()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgshell.html#QWaylandXdgShell
    """
    #  QWaylandXdgShell::QWaylandXdgShell()
    self._noteCreation(QWaylandXdgShell, lambda: Rituals.call(
        'ritual_ZN16QWaylandXdgShellC1Ev',
    ))

  @overload(QWaylandCompositor)
  @overload(NoneType)
  def __init__(self, compositor: Optional[QWaylandCompositor]) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandXdgShell::QWaylandXdgShell(QWaylandCompositor *compositor)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgshell.html#QWaylandXdgShell

    Parameters
    ----------

    compositor : Optional[QWaylandCompositor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWaylandXdgShell::QWaylandXdgShell(QWaylandCompositor *compositor)
    self._noteCreation(QWaylandXdgShell, lambda: Rituals.call(
        'ritual_ZN16QWaylandXdgShellC1EP18QWaylandCompositor',
        self._addressOf(compositor),
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

  def initialize(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgShell::initialize()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgshell.html#initialize
    """
    #  void QWaylandXdgShell::initialize()
    ritual = 'ritual_ZN16QWaylandXdgShell10initializeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QWaylandXdgShell10initializeEv'
    self.uglySide.call(ritual)

  @overload(QWaylandClient)
  @overload(NoneType)
  def ping(self, client: Optional[QWaylandClient]) -> int:
    """
    Calls Qt's 'uint QWaylandXdgShell::ping(QWaylandClient *client)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgshell.html#ping

    Parameters
    ----------

    client : Optional[QWaylandClient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  uint QWaylandXdgShell::ping(QWaylandClient *client)
    return self.uglySide.call(
        'ritual_ZN16QWaylandXdgShell4pingEP14QWaylandClient',
        self._addressOf(client),
    )

  @overload(QWaylandXdgSurface)
  @overload(NoneType)
  def xdgSurfaceCreated(
      self,
      xdgSurface: Optional[QWaylandXdgSurface],
  ) -> None:
    """
    Calls Qt's 'void QWaylandXdgShell::xdgSurfaceCreated(QWaylandXdgSurface
    *xdgSurface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgshell.html#xdgSurfaceCreated

    Parameters
    ----------

    xdgSurface : Optional[QWaylandXdgSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandXdgShell::xdgSurfaceCreated(QWaylandXdgSurface
    #      *xdgSurface)
    self.uglySide.call(
        'ritual_ZN16QWaylandXdgShell17xdgSurfaceCreatedEP18QWaylandXdgSurfa'
        'ce',
        self._addressOf(xdgSurface),
    )

  @overload(QWaylandXdgToplevel, QWaylandXdgSurface)
  @overload(QWaylandXdgToplevel, NoneType)
  @overload(NoneType, QWaylandXdgSurface)
  @overload(NoneType, NoneType)
  def toplevelCreated(
      self,
      toplevel: Optional[QWaylandXdgToplevel],
      xdgSurface: Optional[QWaylandXdgSurface],
  ) -> None:
    """
    Calls Qt's 'void QWaylandXdgShell::toplevelCreated(QWaylandXdgToplevel
    *toplevel, QWaylandXdgSurface *xdgSurface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgshell.html#toplevelCreated

    Parameters
    ----------

    toplevel : Optional[QWaylandXdgToplevel]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    xdgSurface : Optional[QWaylandXdgSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandXdgShell::toplevelCreated(QWaylandXdgToplevel *toplevel,
    #      QWaylandXdgSurface *xdgSurface)
    self.uglySide.call(
        'ritual_ZN16QWaylandXdgShell15toplevelCreatedEP19QWaylandXdgTopleve'
        'lP18QWaylandXdgSurface',
        self._addressOf(toplevel), self._addressOf(xdgSurface),
    )

  @overload(QWaylandXdgPopup, QWaylandXdgSurface)
  @overload(QWaylandXdgPopup, NoneType)
  @overload(NoneType, QWaylandXdgSurface)
  @overload(NoneType, NoneType)
  def popupCreated(
      self,
      popup: Optional[QWaylandXdgPopup],
      xdgSurface: Optional[QWaylandXdgSurface],
  ) -> None:
    """
    Calls Qt's 'void QWaylandXdgShell::popupCreated(QWaylandXdgPopup *popup,
    QWaylandXdgSurface *xdgSurface)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgshell.html#popupCreated

    Parameters
    ----------

    popup : Optional[QWaylandXdgPopup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    xdgSurface : Optional[QWaylandXdgSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandXdgShell::popupCreated(QWaylandXdgPopup *popup,
    #      QWaylandXdgSurface *xdgSurface)
    self.uglySide.call(
        'ritual_ZN16QWaylandXdgShell12popupCreatedEP16QWaylandXdgPopupP18QW'
        'aylandXdgSurface',
        self._addressOf(popup), self._addressOf(xdgSurface),
    )

  @overload(int)
  def pong(self, serial: int) -> None:
    """
    Calls Qt's 'void QWaylandXdgShell::pong(uint serial)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgshell.html#pong

    Parameters
    ----------

    serial : int
      Passed on as it is.
    """
    #  void QWaylandXdgShell::pong(uint serial)
    self.uglySide.call('ritual_ZN16QWaylandXdgShell4pongEj', serial)

  @overload(QWaylandSeat, QWaylandSeat)
  @overload(QWaylandSeat, NoneType)
  @overload(NoneType, QWaylandSeat)
  @overload(NoneType, NoneType)
  def handleSeatChanged(
      self,
      newSeat: Optional[QWaylandSeat],
      oldSeat: Optional[QWaylandSeat],
  ) -> None:
    """
    Calls Qt's 'void QWaylandXdgShell::handleSeatChanged(QWaylandSeat
    *newSeat, QWaylandSeat *oldSeat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgshell.html#handleSeatChanged

    Parameters
    ----------

    newSeat : Optional[QWaylandSeat]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldSeat : Optional[QWaylandSeat]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandXdgShell::handleSeatChanged(QWaylandSeat *newSeat,
    #      QWaylandSeat *oldSeat)
    self.uglySide.call(
        'ritual_ZN16QWaylandXdgShell17handleSeatChangedEP12QWaylandSeatS1_',
        self._addressOf(newSeat), self._addressOf(oldSeat),
    )

  @overload(QWaylandSurface, QWaylandSurface)
  @overload(QWaylandSurface, NoneType)
  @overload(NoneType, QWaylandSurface)
  @overload(NoneType, NoneType)
  def handleFocusChanged(
      self,
      newSurface: Optional[QWaylandSurface],
      oldSurface: Optional[QWaylandSurface],
  ) -> None:
    """
    Calls Qt's 'void QWaylandXdgShell::handleFocusChanged(QWaylandSurface
    *newSurface, QWaylandSurface *oldSurface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgshell.html#handleFocusChanged

    Parameters
    ----------

    newSurface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldSurface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandXdgShell::handleFocusChanged(QWaylandSurface *newSurface,
    #      QWaylandSurface *oldSurface)
    self.uglySide.call(
        'ritual_ZN16QWaylandXdgShell18handleFocusChangedEP15QWaylandSurface'
        'S1_',
        self._addressOf(newSurface), self._addressOf(oldSurface),
    )

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QWaylandXdgShellPrivate *QWaylandXdgShell::d_func()': gives
      'QWaylandXdgShellPrivate', which has no cute class yet.
    - Qt's 'const QWaylandXdgShellPrivate *QWaylandXdgShell::d_func() const':
      gives 'QWaylandXdgShellPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandXdgShell.d_func' has no cute function yet. Qt's "
        "'QWaylandXdgShellPrivate *QWaylandXdgShell::d_func()': gives "
        "'QWaylandXdgShellPrivate', which has no cute class yet. Qt's "
        "'const QWaylandXdgShellPrivate *QWaylandXdgShell::d_func() const': "
        "gives 'QWaylandXdgShellPrivate', which has no cute class yet.")

  @staticmethod
  def interface(*__, **_) -> Never:
    """
    Qt's 'const struct wl_interface *QWaylandXdgShell::interface()': gives
    'struct wl_interface', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandXdgShell.interface' has no cute function yet. Qt's 'const "
        "struct wl_interface *QWaylandXdgShell::interface()': gives 'struct "
        "wl_interface', which has no cute class yet.")
