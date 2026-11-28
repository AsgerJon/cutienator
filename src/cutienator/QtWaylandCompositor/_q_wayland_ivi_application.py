"""
QWaylandIviApplication binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandiviapplication.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject
  from . import QWaylandCompositor, QWaylandIviSurface, QWaylandResource
  from . import QWaylandSurface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWaylandCompositor = WAIT['QWaylandCompositor']
  QWaylandIviSurface = WAIT['QWaylandIviSurface']
  QWaylandResource = WAIT['QWaylandResource']
  QWaylandSurface = WAIT['QWaylandSurface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandIviApplication(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWaylandIviApplication: a plain Python object
  standing in front of one C++ QWaylandIviApplication.

  What exists
  -----------

  Every function of Qt's QWaylandIviApplication that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr', 'initialize',
  'interfaceName', 'iviSurfaceRequested', 'iviSurfaceCreated'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandIviApplication::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QWaylandIviApplication::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandIviApplicationPrivate *QWaylandIviApplication::d_func()':
    gives 'QWaylandIviApplicationPrivate', which has no cute class yet.
  - Qt's 'const QWaylandIviApplicationPrivate
    *QWaylandIviApplication::d_func() const': gives
    'QWaylandIviApplicationPrivate', which has no cute class yet.
  - Qt's 'const struct wl_interface *QWaylandIviApplication::interface()':
    gives 'struct wl_interface', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandIviApplication is created at the first use, not by
    'QWaylandIviApplication(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandIviApplication.
  - Each name of Qt's QWaylandIviApplication that has no cute function yet,
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
    Calls Qt's 'QString QWaylandIviApplication::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandiviapplication.html#tr

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
    #  QString QWaylandIviApplication::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QWaylandIviApplication2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def interfaceName() -> QByteArray:
    """
    Calls Qt's 'QByteArray QWaylandIviApplication::interfaceName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandiviapplication.html#interfaceName

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QWaylandIviApplication::interfaceName()
    address = Rituals.call(
        'ritual_ZN22QWaylandIviApplication13interfaceNameEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandIviApplication'

  #  A C++ QWaylandIviApplication Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandIviApplication'

  #  The functions Qt calls itself that QWaylandIviApplication is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'initialize': (
          ('_ZN22QWaylandIviApplication10initializeEv',
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
    Calls Qt's 'const QMetaObject *QWaylandIviApplication::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandiviapplication.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandIviApplication::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QWaylandIviApplication10metaObjectEv',
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
    Notes what was given, for Qt's
    'QWaylandIviApplication::QWaylandIviApplication()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandiviapplication.html#QWaylandIviApplication
    """
    #  QWaylandIviApplication::QWaylandIviApplication()
    self._noteCreation(QWaylandIviApplication, lambda: Rituals.call(
        'ritual_ZN22QWaylandIviApplicationC1Ev',
    ))

  @overload(QWaylandCompositor)
  @overload(NoneType)
  def __init__(self, compositor: Optional[QWaylandCompositor]) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandIviApplication::QWaylandIviApplication(QWaylandCompositor
    *compositor)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandiviapplication.html#QWaylandIviApplication

    Parameters
    ----------

    compositor : Optional[QWaylandCompositor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWaylandIviApplication::QWaylandIviApplication(QWaylandCompositor
    #      *compositor)
    self._noteCreation(QWaylandIviApplication, lambda: Rituals.call(
        'ritual_ZN22QWaylandIviApplicationC1EP18QWaylandCompositor',
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
    Calls Qt's 'void QWaylandIviApplication::initialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandiviapplication.html#initialize
    """
    #  void QWaylandIviApplication::initialize()
    ritual = 'ritual_ZN22QWaylandIviApplication10initializeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QWaylandIviApplication10initializeEv'
    self.uglySide.call(ritual)

  @overload(QWaylandSurface, int, QWaylandResource)
  @overload(NoneType, int, QWaylandResource)
  def iviSurfaceRequested(
      self,
      surface: Optional[QWaylandSurface],
      iviId: int,
      resource: QWaylandResource,
  ) -> None:
    """
    Calls Qt's 'void
    QWaylandIviApplication::iviSurfaceRequested(QWaylandSurface *surface,
    uint iviId, const QWaylandResource &resource)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandiviapplication.html#iviSurfaceRequested

    Parameters
    ----------

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    iviId : int
      Passed on as it is.

    resource : QWaylandResource
      Passed on as a value: Qt reads the C++ QWaylandResource, which stays
      Python's own.
    """
    #  void QWaylandIviApplication::iviSurfaceRequested(QWaylandSurface
    #      *surface, uint iviId, const QWaylandResource &resource)
    self.uglySide.call(
        'ritual_ZN22QWaylandIviApplication19iviSurfaceRequestedEP15QWayland'
        'SurfacejRK16QWaylandResource',
        self._addressOf(surface), iviId, self._valueOf(resource),
    )

  @overload(QWaylandIviSurface)
  @overload(NoneType)
  def iviSurfaceCreated(
      self,
      iviSurface: Optional[QWaylandIviSurface],
  ) -> None:
    """
    Calls Qt's 'void
    QWaylandIviApplication::iviSurfaceCreated(QWaylandIviSurface
    *iviSurface)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandiviapplication.html#iviSurfaceCreated

    Parameters
    ----------

    iviSurface : Optional[QWaylandIviSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWaylandIviApplication::iviSurfaceCreated(QWaylandIviSurface
    #      *iviSurface)
    self.uglySide.call(
        'ritual_ZN22QWaylandIviApplication17iviSurfaceCreatedEP18QWaylandIv'
        'iSurface',
        self._addressOf(iviSurface),
    )

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QWaylandIviApplicationPrivate *QWaylandIviApplication::d_func()':
      gives 'QWaylandIviApplicationPrivate', which has no cute class yet.
    - Qt's 'const QWaylandIviApplicationPrivate
      *QWaylandIviApplication::d_func() const': gives
      'QWaylandIviApplicationPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandIviApplication.d_func' has no cute function yet. Qt's "
        "'QWaylandIviApplicationPrivate *QWaylandIviApplication::d_func()': "
        "gives 'QWaylandIviApplicationPrivate', which has no cute class "
        "yet. Qt's 'const QWaylandIviApplicationPrivate "
        "*QWaylandIviApplication::d_func() const': gives "
        "'QWaylandIviApplicationPrivate', which has no cute class yet.")

  @staticmethod
  def interface(*__, **_) -> Never:
    """
    Qt's 'const struct wl_interface *QWaylandIviApplication::interface()':
    gives 'struct wl_interface', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandIviApplication.interface' has no cute function yet. Qt's "
        "'const struct wl_interface *QWaylandIviApplication::interface()': "
        "gives 'struct wl_interface', which has no cute class yet.")
