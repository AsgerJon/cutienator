"""
QWaylandWlShell binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandwlshell.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject
  from . import QWaylandClient, QWaylandCompositor, QWaylandResource
  from . import QWaylandSurface, QWaylandWlShellSurface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWaylandClient = WAIT['QWaylandClient']
  QWaylandCompositor = WAIT['QWaylandCompositor']
  QWaylandResource = WAIT['QWaylandResource']
  QWaylandSurface = WAIT['QWaylandSurface']
  QWaylandWlShellSurface = WAIT['QWaylandWlShellSurface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandWlShell(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWaylandWlShell: a plain Python object standing in
  front of one C++ QWaylandWlShell.

  What exists
  -----------

  Every function of Qt's QWaylandWlShell that has a ritual and that Python
  can call so far, 11 names in all: 'metaObject', 'tr', 'initialize',
  'shellSurfaces', 'shellSurfacesForClient', 'mappedPopups', 'popupClient',
  'interfaceName', 'closeAllPopups', 'wlShellSurfaceRequested',
  'wlShellSurfaceCreated'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandWlShell::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QWaylandWlShell::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandWlShellPrivate *QWaylandWlShell::d_func()': gives
    'QWaylandWlShellPrivate', which has no cute class yet.
  - Qt's 'const QWaylandWlShellPrivate *QWaylandWlShell::d_func() const':
    gives 'QWaylandWlShellPrivate', which has no cute class yet.
  - Qt's 'const struct wl_interface *QWaylandWlShell::interface()': gives
    'struct wl_interface', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandWlShell is created at the first use, not by
    'QWaylandWlShell(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandWlShell.
  - Each name of Qt's QWaylandWlShell that has no cute function yet,
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
    Calls Qt's 'QString QWaylandWlShell::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandwlshell.html#tr

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
    #  QString QWaylandWlShell::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QWaylandWlShell2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def interfaceName() -> QByteArray:
    """
    Calls Qt's 'QByteArray QWaylandWlShell::interfaceName()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandwlshell.html#interfaceName

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QWaylandWlShell::interfaceName()
    address = Rituals.call('ritual_ZN15QWaylandWlShell13interfaceNameEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandWlShell'

  #  A C++ QWaylandWlShell Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandWlShell'

  #  The functions Qt calls itself that QWaylandWlShell is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'initialize': (
          ('_ZN15QWaylandWlShell10initializeEv',
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
    Calls Qt's 'const QMetaObject *QWaylandWlShell::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandwlshell.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandWlShell::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QWaylandWlShell10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def shellSurfaces(self) -> QList[QWaylandWlShellSurface]:
    """
    Calls Qt's 'QList<QWaylandWlShellSurface *>
    QWaylandWlShell::shellSurfaces() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandwlshell.html#shellSurfaces

    Returns
    -------

    QList[QWaylandWlShellSurface]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QWaylandWlShellSurface *> QWaylandWlShell::shellSurfaces() const
    address = self.uglySide.call(
        'ritual_ZNK15QWaylandWlShell13shellSurfacesEv',
    )
    from . import QWaylandWlShellSurface
    return QList[QWaylandWlShellSurface]._cuteOwning(address)

  @overload(QWaylandClient)
  @overload(NoneType)
  def shellSurfacesForClient(
      self,
      client: Optional[QWaylandClient],
  ) -> QList[QWaylandWlShellSurface]:
    """
    Calls Qt's 'QList<QWaylandWlShellSurface *>
    QWaylandWlShell::shellSurfacesForClient(QWaylandClient *client) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshell.html#shellSurfacesForClient

    Parameters
    ----------

    client : Optional[QWaylandClient]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QWaylandWlShellSurface]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QWaylandWlShellSurface *>
    #      QWaylandWlShell::shellSurfacesForClient(QWaylandClient *client)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK15QWaylandWlShell22shellSurfacesForClientEP14QWaylandCli'
        'ent',
        self._addressOf(client),
    )
    from . import QWaylandWlShellSurface
    return QList[QWaylandWlShellSurface]._cuteOwning(address)

  def mappedPopups(self) -> QList[QWaylandWlShellSurface]:
    """
    Calls Qt's 'QList<QWaylandWlShellSurface *>
    QWaylandWlShell::mappedPopups() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandwlshell.html#mappedPopups

    Returns
    -------

    QList[QWaylandWlShellSurface]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QWaylandWlShellSurface *> QWaylandWlShell::mappedPopups() const
    address = self.uglySide.call(
        'ritual_ZNK15QWaylandWlShell12mappedPopupsEv',
    )
    from . import QWaylandWlShellSurface
    return QList[QWaylandWlShellSurface]._cuteOwning(address)

  def popupClient(self) -> Optional[QWaylandClient]:
    """
    Calls Qt's 'QWaylandClient *QWaylandWlShell::popupClient() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandwlshell.html#popupClient

    Returns
    -------

    Optional[QWaylandClient]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandClient *QWaylandWlShell::popupClient() const
    address = self.uglySide.call(
        'ritual_ZNK15QWaylandWlShell11popupClientEv',
    )
    from . import QWaylandClient
    return QWaylandClient._cuteAt(address)

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
    Notes what was given, for Qt's 'QWaylandWlShell::QWaylandWlShell()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshell.html#QWaylandWlShell
    """
    #  QWaylandWlShell::QWaylandWlShell()
    self._noteCreation(QWaylandWlShell, lambda: Rituals.call(
        'ritual_ZN15QWaylandWlShellC1Ev',
    ))

  @overload(QWaylandCompositor)
  @overload(NoneType)
  def __init__(self, compositor: Optional[QWaylandCompositor]) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandWlShell::QWaylandWlShell(QWaylandCompositor *compositor)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshell.html#QWaylandWlShell

    Parameters
    ----------

    compositor : Optional[QWaylandCompositor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWaylandWlShell::QWaylandWlShell(QWaylandCompositor *compositor)
    self._noteCreation(QWaylandWlShell, lambda: Rituals.call(
        'ritual_ZN15QWaylandWlShellC1EP18QWaylandCompositor',
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
    Calls Qt's 'void QWaylandWlShell::initialize()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandwlshell.html#initialize
    """
    #  void QWaylandWlShell::initialize()
    ritual = 'ritual_ZN15QWaylandWlShell10initializeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QWaylandWlShell10initializeEv'
    self.uglySide.call(ritual)

  def closeAllPopups(self) -> None:
    """
    Calls Qt's 'void QWaylandWlShell::closeAllPopups()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshell.html#closeAllPopups
    """
    #  void QWaylandWlShell::closeAllPopups()
    self.uglySide.call('ritual_ZN15QWaylandWlShell14closeAllPopupsEv')

  @overload(QWaylandSurface, QWaylandResource)
  @overload(NoneType, QWaylandResource)
  def wlShellSurfaceRequested(
      self,
      surface: Optional[QWaylandSurface],
      resource: QWaylandResource,
  ) -> None:
    """
    Calls Qt's 'void QWaylandWlShell::wlShellSurfaceRequested(QWaylandSurface
    *surface, const QWaylandResource &resource)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshell.html#wlShellSurfaceRequested

    Parameters
    ----------

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    resource : QWaylandResource
      Passed on as a value: Qt reads the C++ QWaylandResource, which stays
      Python's own.
    """
    #  void QWaylandWlShell::wlShellSurfaceRequested(QWaylandSurface
    #      *surface, const QWaylandResource &resource)
    self.uglySide.call(
        'ritual_ZN15QWaylandWlShell23wlShellSurfaceRequestedEP15QWaylandSur'
        'faceRK16QWaylandResource',
        self._addressOf(surface), self._valueOf(resource),
    )

  @overload(QWaylandWlShellSurface)
  @overload(NoneType)
  def wlShellSurfaceCreated(
      self,
      shellSurface: Optional[QWaylandWlShellSurface],
  ) -> None:
    """
    Calls Qt's 'void
    QWaylandWlShell::wlShellSurfaceCreated(QWaylandWlShellSurface
    *shellSurface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandwlshell.html#wlShellSurfaceCreated

    Parameters
    ----------

    shellSurface : Optional[QWaylandWlShellSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandWlShell::wlShellSurfaceCreated(QWaylandWlShellSurface
    #      *shellSurface)
    self.uglySide.call(
        'ritual_ZN15QWaylandWlShell21wlShellSurfaceCreatedEP22QWaylandWlShe'
        'llSurface',
        self._addressOf(shellSurface),
    )

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QWaylandWlShellPrivate *QWaylandWlShell::d_func()': gives
      'QWaylandWlShellPrivate', which has no cute class yet.
    - Qt's 'const QWaylandWlShellPrivate *QWaylandWlShell::d_func() const':
      gives 'QWaylandWlShellPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandWlShell.d_func' has no cute function yet. Qt's "
        "'QWaylandWlShellPrivate *QWaylandWlShell::d_func()': gives "
        "'QWaylandWlShellPrivate', which has no cute class yet. Qt's 'const "
        "QWaylandWlShellPrivate *QWaylandWlShell::d_func() const': gives "
        "'QWaylandWlShellPrivate', which has no cute class yet.")

  @staticmethod
  def interface(*__, **_) -> Never:
    """
    Qt's 'const struct wl_interface *QWaylandWlShell::interface()': gives
    'struct wl_interface', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandWlShell.interface' has no cute function yet. Qt's 'const "
        "struct wl_interface *QWaylandWlShell::interface()': gives 'struct "
        "wl_interface', which has no cute class yet.")
