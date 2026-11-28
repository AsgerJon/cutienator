"""
QWaylandIviSurface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandivisurface.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QSize
  from . import QWaylandIviApplication, QWaylandQuickShellIntegration
  from . import QWaylandQuickShellSurfaceItem, QWaylandResource
  from . import QWaylandSurface, QWaylandSurfaceRole
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSize = WAIT['QSize']
  QWaylandIviApplication = WAIT['QWaylandIviApplication']
  QWaylandQuickShellSurfaceItem = WAIT['QWaylandQuickShellSurfaceItem']
  QWaylandResource = WAIT['QWaylandResource']
  QWaylandSurface = WAIT['QWaylandSurface']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandIviSurface(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWaylandIviSurface: a plain Python object standing in
  front of one C++ QWaylandIviSurface.

  What exists
  -----------

  Every function of Qt's QWaylandIviSurface that has a ritual and that Python
  can call so far, 11 names in all: 'metaObject', 'tr', 'initialize',
  'surface', 'iviId', 'interfaceName', 'role', 'sendConfigure',
  'createIntegration', 'surfaceChanged', 'iviIdChanged'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandIviSurface::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QWaylandIviSurface::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandIviSurfacePrivate *QWaylandIviSurface::d_func()': gives
    'QWaylandIviSurfacePrivate', which has no cute class yet.
  - Qt's 'const QWaylandIviSurfacePrivate *QWaylandIviSurface::d_func()
    const': gives 'QWaylandIviSurfacePrivate', which has no cute class yet.
  - Qt's 'QQmlListProperty<QObject> QWaylandIviSurface::data()': gives a type
    Python has no way to take yet.
  - Qt's 'void QWaylandIviSurface::appendFunction(QQmlListProperty<QObject>
    *list, QObject *object)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
  - Qt's 'qsizetype
    QWaylandIviSurface::countFunction(QQmlListProperty<QObject> *list)':
    names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'QObject *QWaylandIviSurface::atFunction(QQmlListProperty<QObject>
    *list, qsizetype index)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
  - Qt's 'void QWaylandIviSurface::clearFunction(QQmlListProperty<QObject>
    *list)': names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'const struct wl_interface *QWaylandIviSurface::interface()': gives
    'struct wl_interface', which has no cute class yet.
  - Qt's 'QWaylandIviSurface *QWaylandIviSurface::fromResource(::wl_resource
    *resource)': names '::wl_resource', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandIviSurface is created at the first use, not by
    'QWaylandIviSurface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandIviSurface.
  - Each name of Qt's QWaylandIviSurface that has no cute function yet,
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
    Calls Qt's 'QString QWaylandIviSurface::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandivisurface.html#tr

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
    #  QString QWaylandIviSurface::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QWaylandIviSurface2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def interfaceName() -> QByteArray:
    """
    Calls Qt's 'QByteArray QWaylandIviSurface::interfaceName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandivisurface.html#interfaceName

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QWaylandIviSurface::interfaceName()
    address = Rituals.call('ritual_ZN18QWaylandIviSurface13interfaceNameEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @staticmethod
  def role() -> Optional[QWaylandSurfaceRole]:
    """
    Calls Qt's 'QWaylandSurfaceRole *QWaylandIviSurface::role()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandivisurface.html#role

    Returns
    -------

    Optional[QWaylandSurfaceRole]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandSurfaceRole *QWaylandIviSurface::role()
    address = Rituals.call('ritual_ZN18QWaylandIviSurface4roleEv')
    from . import QWaylandSurfaceRole
    return QWaylandSurfaceRole._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandIviSurface'

  #  The functions Qt calls itself that QWaylandIviSurface is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'createIntegration': (
          ('_ZN18QWaylandIviSurface17createIntegrationEP29QWaylandQuickShel'
           'lSurfaceItem',
           ('address', 'address',
            'QtWaylandCompositor:QWaylandQuickShellIntegration'),
           (
               ('address', 'address',
                'QtWaylandCompositor:QWaylandQuickShellSurfaceItem'),
           )),
      ),
      'initialize': (
          ('_ZN18QWaylandIviSurface10initializeEv',
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
    Calls Qt's 'const QMetaObject *QWaylandIviSurface::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandivisurface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandIviSurface::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QWaylandIviSurface10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def surface(self) -> Optional[QWaylandSurface]:
    """
    Calls Qt's 'QWaylandSurface *QWaylandIviSurface::surface() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandivisurface.html#surface

    Returns
    -------

    Optional[QWaylandSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandSurface *QWaylandIviSurface::surface() const
    address = self.uglySide.call('ritual_ZNK18QWaylandIviSurface7surfaceEv')
    from . import QWaylandSurface
    return QWaylandSurface._cuteAt(address)

  def iviId(self) -> int:
    """
    Calls Qt's 'uint QWaylandIviSurface::iviId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandivisurface.html#iviId
    """
    #  uint QWaylandIviSurface::iviId() const
    return self.uglySide.call('ritual_ZNK18QWaylandIviSurface5iviIdEv')

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
    'QWaylandIviSurface::QWaylandIviSurface()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandivisurface.html#QWaylandIviSurface
    """
    #  QWaylandIviSurface::QWaylandIviSurface()
    self._noteCreation(QWaylandIviSurface, lambda: Rituals.call(
        'ritual_ZN18QWaylandIviSurfaceC1Ev',
    ))

  @overload(QWaylandIviApplication, QWaylandSurface, int, QWaylandResource)
  @overload(QWaylandIviApplication, NoneType, int, QWaylandResource)
  @overload(NoneType, QWaylandSurface, int, QWaylandResource)
  @overload(NoneType, NoneType, int, QWaylandResource)
  def __init__(
      self,
      application: Optional[QWaylandIviApplication],
      surface: Optional[QWaylandSurface],
      iviId: int,
      resource: QWaylandResource,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandIviSurface::QWaylandIviSurface(QWaylandIviApplication
    *application, QWaylandSurface *surface, uint iviId, const
    QWaylandResource &resource)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandivisurface.html#QWaylandIviSurface

    Parameters
    ----------

    application : Optional[QWaylandIviApplication]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    iviId : int
      Passed on as it is.

    resource : QWaylandResource
      Passed on as a value: Qt reads the C++ QWaylandResource, which stays
      Python's own.
    """
    #  QWaylandIviSurface::QWaylandIviSurface(QWaylandIviApplication
    #      *application, QWaylandSurface *surface, uint iviId, const
    #      QWaylandResource &resource)
    self._noteCreation(QWaylandIviSurface, lambda: Rituals.call(
        'ritual_ZN18QWaylandIviSurfaceC1EP22QWaylandIviApplicationP15QWayla'
        'ndSurfacejRK16QWaylandResource',
        self._addressOf(application), self._addressOf(surface), iviId,
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

  @overload(QWaylandIviApplication, QWaylandSurface, int, QWaylandResource)
  @overload(QWaylandIviApplication, NoneType, int, QWaylandResource)
  @overload(NoneType, QWaylandSurface, int, QWaylandResource)
  @overload(NoneType, NoneType, int, QWaylandResource)
  def initialize(
      self,
      iviApplication: Optional[QWaylandIviApplication],
      surface: Optional[QWaylandSurface],
      iviId: int,
      resource: QWaylandResource,
  ) -> None:
    """
    Calls Qt's 'void QWaylandIviSurface::initialize(QWaylandIviApplication
    *iviApplication, QWaylandSurface *surface, uint iviId, const
    QWaylandResource &resource)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandivisurface.html#initialize

    Parameters
    ----------

    iviApplication : Optional[QWaylandIviApplication]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    surface : Optional[QWaylandSurface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    iviId : int
      Passed on as it is.

    resource : QWaylandResource
      Passed on as a value: Qt reads the C++ QWaylandResource, which stays
      Python's own.
    """
    #  void QWaylandIviSurface::initialize(QWaylandIviApplication
    #      *iviApplication, QWaylandSurface *surface, uint iviId, const
    #      QWaylandResource &resource)
    self.uglySide.call(
        'ritual_ZN18QWaylandIviSurface10initializeEP22QWaylandIviApplicatio'
        'nP15QWaylandSurfacejRK16QWaylandResource',
        self._addressOf(iviApplication), self._addressOf(surface), iviId,
        self._valueOf(resource),
    )

  @overload()
  def initialize(self) -> None:
    """
    Calls Qt's 'void QWaylandIviSurface::initialize()'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandivisurface.html#initialize
    """
    #  void QWaylandIviSurface::initialize()
    ritual = 'ritual_ZN18QWaylandIviSurface10initializeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QWaylandIviSurface10initializeEv'
    self.uglySide.call(ritual)

  @overload(QSize)
  def sendConfigure(self, size: QSize) -> None:
    """
    Calls Qt's 'void QWaylandIviSurface::sendConfigure(const QSize &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandivisurface.html#sendConfigure

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QWaylandIviSurface::sendConfigure(const QSize &size)
    self.uglySide.call(
        'ritual_ZN18QWaylandIviSurface13sendConfigureERK5QSize',
        self._valueOf(size),
    )

  @overload(QWaylandQuickShellSurfaceItem)
  @overload(NoneType)
  def createIntegration(
      self,
      item: Optional[QWaylandQuickShellSurfaceItem],
  ) -> Optional[QWaylandQuickShellIntegration]:
    """
    Calls Qt's 'QWaylandQuickShellIntegration
    *QWaylandIviSurface::createIntegration(QWaylandQuickShellSurfaceItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandivisurface.html#createIntegration

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
    #  QWaylandQuickShellIntegration *QWaylandIviSurface::createIntegration(
    #      QWaylandQuickShellSurfaceItem *item)
    ritual = (
        'ritual_ZN18QWaylandIviSurface17createIntegrationEP29QWaylandQuickS'
        'hellSurfaceItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QWaylandIviSurface17createIntegrationEP29QWayland'
          'QuickShellSurfaceItem')
    address = self.uglySide.call(ritual, self._addressOf(item))
    from . import QWaylandQuickShellIntegration
    return QWaylandQuickShellIntegration._cuteAt(address)

  def surfaceChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandIviSurface::surfaceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandivisurface.html#surfaceChanged
    """
    #  void QWaylandIviSurface::surfaceChanged()
    self.uglySide.call('ritual_ZN18QWaylandIviSurface14surfaceChangedEv')

  def iviIdChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandIviSurface::iviIdChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandivisurface.html#iviIdChanged
    """
    #  void QWaylandIviSurface::iviIdChanged()
    self.uglySide.call('ritual_ZN18QWaylandIviSurface12iviIdChangedEv')

  @staticmethod
  def appendFunction(*__, **_) -> Never:
    """
    Qt's 'void QWaylandIviSurface::appendFunction(QQmlListProperty<QObject>
    *list, QObject *object)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandIviSurface.appendFunction' has no cute function yet. Qt's "
        "'void QWaylandIviSurface::appendFunction(QQmlListProperty<QObject> "
        "*list, QObject *object)': names 'QQmlListProperty<QObject>', which "
        "has no cute class yet.")

  @staticmethod
  def atFunction(*__, **_) -> Never:
    """
    Qt's 'QObject *QWaylandIviSurface::atFunction(QQmlListProperty<QObject>
    *list, qsizetype index)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandIviSurface.atFunction' has no cute function yet. Qt's "
        "'QObject *QWaylandIviSurface::atFunction(QQmlListProperty<QObject> "
        "*list, qsizetype index)': names 'QQmlListProperty<QObject>', which "
        "has no cute class yet.")

  @staticmethod
  def clearFunction(*__, **_) -> Never:
    """
    Qt's 'void QWaylandIviSurface::clearFunction(QQmlListProperty<QObject>
    *list)': names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandIviSurface.clearFunction' has no cute function yet. Qt's "
        "'void QWaylandIviSurface::clearFunction(QQmlListProperty<QObject> "
        "*list)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def countFunction(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QWaylandIviSurface::countFunction(QQmlListProperty<QObject> *list)':
    names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandIviSurface.countFunction' has no cute function yet. Qt's "
        "'qsizetype "
        "QWaylandIviSurface::countFunction(QQmlListProperty<QObject> "
        "*list)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QWaylandIviSurfacePrivate *QWaylandIviSurface::d_func()': gives
      'QWaylandIviSurfacePrivate', which has no cute class yet.
    - Qt's 'const QWaylandIviSurfacePrivate *QWaylandIviSurface::d_func()
      const': gives 'QWaylandIviSurfacePrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandIviSurface.d_func' has no cute function yet. Qt's "
        "'QWaylandIviSurfacePrivate *QWaylandIviSurface::d_func()': gives "
        "'QWaylandIviSurfacePrivate', which has no cute class yet. Qt's "
        "'const QWaylandIviSurfacePrivate *QWaylandIviSurface::d_func() "
        "const': gives 'QWaylandIviSurfacePrivate', which has no cute class "
        "yet.")

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QWaylandIviSurface::data()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QWaylandIviSurface.data' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QWaylandIviSurface::data()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def fromResource(*__, **_) -> Never:
    """
    Qt's 'QWaylandIviSurface *QWaylandIviSurface::fromResource(::wl_resource
    *resource)': names '::wl_resource', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandIviSurface.fromResource' has no cute function yet. Qt's "
        "'QWaylandIviSurface "
        "*QWaylandIviSurface::fromResource(::wl_resource *resource)': names "
        "'::wl_resource', which has no cute class yet.")

  @staticmethod
  def interface(*__, **_) -> Never:
    """
    Qt's 'const struct wl_interface *QWaylandIviSurface::interface()': gives
    'struct wl_interface', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandIviSurface.interface' has no cute function yet. Qt's "
        "'const struct wl_interface *QWaylandIviSurface::interface()': "
        "gives 'struct wl_interface', which has no cute class yet.")
