"""
QNativeInterface::Private::QWaylandWindow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformwindow_p.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMargins, QMetaObject, QRect
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMargins = WAIT['QMargins']
  QRect = WAIT['QRect']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandWindow(QObject):
  """
  The cute side of Qt's QNativeInterface::Private::QWaylandWindow: a plain
  Python object standing in front of one C++
  QNativeInterface::Private::QWaylandWindow.

  It is built on the cute 'QObject', as Qt's
  QNativeInterface::Private::QWaylandWindow is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QNativeInterface::Private::QWaylandWindow that has a
  ritual and that Python can call so far, 12 names in all: 'metaObject',
  'tr', 'setCustomMargins', 'requestXdgActivationToken',
  'setSessionRestoreId', 'setExtendedWindowType', 'setParentControlGeometry',
  'surfaceCreated', 'surfaceDestroyed', 'surfaceRoleCreated',
  'surfaceRoleDestroyed', 'xdgActivationTokenCreated'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNativeInterface::Private::QWaylandWindow::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QNativeInterface::Private::QWaylandWindow::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QNativeInterface::Private::QWaylandWindow::~QWaylandWindow()': the
    destructor: Python never removes a C++
    QNativeInterface::Private::QWaylandWindow.
  - Qt's 'wl_surface *QNativeInterface::Private::QWaylandWindow::surface()
    const': gives 'wl_surface', which has no cute class yet.
  - Qt's 'std::any QNativeInterface::Private::QWaylandWindow::_surfaceRole()
    const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  8 of the 25 functions Qt declares: 4 forbidden; 2 not a gap; 1 the class is
  abstract, so C++ cannot make one, and the C++ class of ours does not fill
  in every function it leaves open; 1 a template.

  What to expect
  --------------

  - The C++ QNativeInterface::Private::QWaylandWindow is created at the first
    use, not by 'QNativeInterface::Private::QWaylandWindow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNativeInterface::Private::QWaylandWindow.
  - Qt tells when it has removed the C++
    QNativeInterface::Private::QWaylandWindow. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
  - Each name of Qt's QNativeInterface::Private::QWaylandWindow that has no
    cute function yet, '__init__', '_surfaceRole', 'surface', 'surfaceRole',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QNativeInterface::Private::QWaylandWindow,
  #  each a class in here as in C++, and the names Qt has for the
  #  combinations of its flags enums.

  class WindowType(CuteNum):
    """
    The enum 'QNativeInterface::Private::QWaylandWindow::WindowType' of Qt,
    with the 5 names Qt gives in it.
    """

    Default = Kee[int](0)
    ToolTip = Kee[int](1)
    ComboBox = Kee[int](2)
    Menu = Kee[int](3)
    SubMenu = Kee[int](4)

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
    Calls Qt's 'QString QNativeInterface::Private::QWaylandWindow::tr(const
    char *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-private-qwaylandwindow.html#tr

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
    #  QString QNativeInterface::Private::QWaylandWindow::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QNativeInterface7Private14QWaylandWindow2trEPKcS3_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNativeInterface::Private::QWaylandWindow'

  #  A C++ QNativeInterface::Private::QWaylandWindow Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNativeInterface_Private_QWaylandWindow'

  #  The functions Qt calls itself that
  #  QNativeInterface::Private::QWaylandWindow is the first to declare and
  #  that cannot be handed to Python yet, each as Qt declares it. A class of
  #  a program that writes one of them anew is refused, since Qt would never
  #  call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'surface': (
          'wl_surface '
          '*QNativeInterface::Private::QWaylandWindow::surface() const',
      ),
      '_surfaceRole': (
          'std::any '
          'QNativeInterface::Private::QWaylandWindow::_surfaceRole() const',
      ),
  }

  #  The functions Qt calls itself that
  #  QNativeInterface::Private::QWaylandWindow is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'setCustomMargins': (
          ('_ZN16QNativeInterface7Private14QWaylandWindow16setCustomMargins'
           'ERK8QMargins',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QMargins'),
           )),
      ),
      'requestXdgActivationToken': (
          ('_ZN16QNativeInterface7Private14QWaylandWindow25requestXdgActiva'
           'tionTokenEj',
           ('nothing', 'nothing', ''),
           (
               ('unsigned int', 'number', ''),
           )),
      ),
      'setSessionRestoreId': (
          ('_ZN16QNativeInterface7Private14QWaylandWindow19setSessionRestor'
           'eIdERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'setExtendedWindowType': (
          ('_ZN16QNativeInterface7Private14QWaylandWindow21setExtendedWindo'
           'wTypeENS1_10WindowTypeE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtGui:QNativeInterface.Private.QWaylandWindow.WindowType'),
           )),
      ),
      'setParentControlGeometry': (
          ('_ZN16QNativeInterface7Private14QWaylandWindow24setParentControl'
           'GeometryERK5QRect',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QRect'),
           )),
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
    Calls Qt's 'const QMetaObject
    *QNativeInterface::Private::QWaylandWindow::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-private-qwaylandwindow.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QNativeInterface::Private::QWaylandWindow::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QNativeInterface7Private14QWaylandWindow10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMargins)
  def setCustomMargins(self, margins: QMargins) -> None:
    """
    Calls Qt's 'void
    QNativeInterface::Private::QWaylandWindow::setCustomMargins(const
    QMargins &margins)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-private-qwaylandwindow.html

    Parameters
    ----------

    margins : QMargins
      Passed on as a value: Qt reads the C++ QMargins, which stays Python's
      own.
    """
    #  void QNativeInterface::Private::QWaylandWindow::setCustomMargins(const
    #      QMargins &margins)
    self.uglySide.call(
        'ritual_ZN16QNativeInterface7Private14QWaylandWindow16setCustomMarg'
        'insERK8QMargins',
        self._valueOf(margins, 'QMargins'),
    )

  @overload(str)
  def setSessionRestoreId(self, role: str) -> None:
    """
    Calls Qt's 'void
    QNativeInterface::Private::QWaylandWindow::setSessionRestoreId(const
    QString &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-private-qwaylandwindow.html

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNativeInterface::Private::QWaylandWindow::setSessionRestoreId(
    #      const QString &role)
    self.uglySide.call(
        'ritual_ZN16QNativeInterface7Private14QWaylandWindow19setSessionRes'
        'toreIdERK7QString',
        role,
    )

  @overload(WindowType)
  def setExtendedWindowType(self, windowType: WindowType) -> None:
    """
    Calls Qt's 'void
    QNativeInterface::Private::QWaylandWindow::setExtendedWindowType(
    WindowType windowType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-private-qwaylandwindow.html

    Parameters
    ----------

    windowType : WindowType
      Passed on as its number.
    """
    #  void QNativeInterface::Private::QWaylandWindow::setExtendedWindowType(
    #      WindowType windowType)
    self.uglySide.call(
        'ritual_ZN16QNativeInterface7Private14QWaylandWindow21setExtendedWi'
        'ndowTypeENS1_10WindowTypeE',
        windowType.value,
    )

  @overload(QRect)
  def setParentControlGeometry(self, parentAnchor: QRect) -> None:
    """
    Calls Qt's 'void
    QNativeInterface::Private::QWaylandWindow::setParentControlGeometry(const
    QRect &parentAnchor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-private-qwaylandwindow.html

    Parameters
    ----------

    parentAnchor : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void QNativeInterface::Private::QWaylandWindow::
    #      setParentControlGeometry(const QRect &parentAnchor)
    self.uglySide.call(
        'ritual_ZN16QNativeInterface7Private14QWaylandWindow24setParentCont'
        'rolGeometryERK5QRect',
        self._valueOf(parentAnchor),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QNativeInterface::Private::QWaylandWindow::QWaylandWindow()': the
    class is abstract, so C++ cannot make one, and the C++ class of ours does
    not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QNativeInterface.Private.QWaylandWindow.__init__' has no cute "
        "function yet. Qt's "
        "'QNativeInterface::Private::QWaylandWindow::QWaylandWindow()': the "
        "class is abstract, so C++ cannot make one, and the C++ class of "
        "ours does not fill in every function it leaves open.")

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

  @overload(int)
  def requestXdgActivationToken(self, serial: int) -> None:
    """
    Calls Qt's 'void
    QNativeInterface::Private::QWaylandWindow::requestXdgActivationToken(uint
    serial)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-private-qwaylandwindow.html

    Parameters
    ----------

    serial : int
      Passed on as it is.
    """
    #  void QNativeInterface::Private::QWaylandWindow::
    #      requestXdgActivationToken(uint serial)
    self.uglySide.call(
        'ritual_ZN16QNativeInterface7Private14QWaylandWindow25requestXdgAct'
        'ivationTokenEj',
        serial,
    )

  def surfaceCreated(self) -> None:
    """
    Calls Qt's 'void
    QNativeInterface::Private::QWaylandWindow::surfaceCreated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-private-qwaylandwindow.html
    """
    #  void QNativeInterface::Private::QWaylandWindow::surfaceCreated()
    self.uglySide.call(
        'ritual_ZN16QNativeInterface7Private14QWaylandWindow14surfaceCreate'
        'dEv',
    )

  def surfaceDestroyed(self) -> None:
    """
    Calls Qt's 'void
    QNativeInterface::Private::QWaylandWindow::surfaceDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-private-qwaylandwindow.html
    """
    #  void QNativeInterface::Private::QWaylandWindow::surfaceDestroyed()
    self.uglySide.call(
        'ritual_ZN16QNativeInterface7Private14QWaylandWindow16surfaceDestro'
        'yedEv',
    )

  def surfaceRoleCreated(self) -> None:
    """
    Calls Qt's 'void
    QNativeInterface::Private::QWaylandWindow::surfaceRoleCreated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-private-qwaylandwindow.html
    """
    #  void QNativeInterface::Private::QWaylandWindow::surfaceRoleCreated()
    self.uglySide.call(
        'ritual_ZN16QNativeInterface7Private14QWaylandWindow18surfaceRoleCr'
        'eatedEv',
    )

  def surfaceRoleDestroyed(self) -> None:
    """
    Calls Qt's 'void
    QNativeInterface::Private::QWaylandWindow::surfaceRoleDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-private-qwaylandwindow.html
    """
    #  void QNativeInterface::Private::QWaylandWindow::surfaceRoleDestroyed()
    self.uglySide.call(
        'ritual_ZN16QNativeInterface7Private14QWaylandWindow20surfaceRoleDe'
        'stroyedEv',
    )

  @overload(str)
  def xdgActivationTokenCreated(self, token: str) -> None:
    """
    Calls Qt's 'void
    QNativeInterface::Private::QWaylandWindow::xdgActivationTokenCreated(
    const QString &token)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnativeinterface-private-qwaylandwindow.html

    Parameters
    ----------

    token : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QNativeInterface::Private::QWaylandWindow::
    #      xdgActivationTokenCreated(const QString &token)
    self.uglySide.call(
        'ritual_ZN16QNativeInterface7Private14QWaylandWindow25xdgActivation'
        'TokenCreatedERK7QString',
        token,
    )

  @staticmethod
  def _surfaceRole(*__, **_) -> Never:
    """
    Qt's 'std::any QNativeInterface::Private::QWaylandWindow::_surfaceRole()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QNativeInterface.Private.QWaylandWindow._surfaceRole' has no cute "
        "function yet. Qt's 'std::any "
        "QNativeInterface::Private::QWaylandWindow::_surfaceRole() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def surface(*__, **_) -> Never:
    """
    Qt's 'wl_surface *QNativeInterface::Private::QWaylandWindow::surface()
    const': gives 'wl_surface', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QNativeInterface.Private.QWaylandWindow.surface' has no cute "
        "function yet. Qt's 'wl_surface "
        "*QNativeInterface::Private::QWaylandWindow::surface() const': "
        "gives 'wl_surface', which has no cute class yet.")

  @staticmethod
  def surfaceRole(*__, **_) -> Never:
    """
    Qt's 'QNativeInterface::Private::QWaylandWindow::surfaceRole': a
    template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QNativeInterface.Private.QWaylandWindow.surfaceRole' has no cute "
        "function yet. Qt's "
        "'QNativeInterface::Private::QWaylandWindow::surfaceRole': a "
        "template: a pattern and no single function.")
