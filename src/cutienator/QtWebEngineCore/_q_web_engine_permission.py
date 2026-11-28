"""
QWebEnginePermission binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebenginepermission.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QUrl
  from . import QWebEnginePermissionPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWebEnginePermissionPrivate = WAIT['QWebEnginePermissionPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebEnginePermission(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWebEnginePermission: a plain Python object standing
  in front of one C++ QWebEnginePermission.

  C++ hands a QWebEnginePermission around as a copy, so every C++
  QWebEnginePermission behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QWebEnginePermission that has a ritual and that
  Python can call so far, 11 names in all: 'origin', 'permissionType',
  'state', 'isValid', 'grant', 'deny', 'reset', 'isPersistent', '__eq__',
  '__ne__', 'equals'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWebEnginePermission::QWebEnginePermission(QWebEnginePermission
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QWebEnginePermission::~QWebEnginePermission()': the destructor:
    Python removes its C++ QWebEnginePermission by it, and has no other use
    for it.
  - Qt's 'QWebEnginePermission &QWebEnginePermission::operator=(const
    QWebEnginePermission &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QWebEnginePermission
    &QWebEnginePermission::operator=(QWebEnginePermission &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QWebEnginePermission::swap(QWebEnginePermission &other)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 22 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QWebEnginePermission is created at the first use, not by
    'QWebEnginePermission(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QWebEnginePermission back gives a copy the ritual
    made for Python, in a new cute QWebEnginePermission.
  - Each name of Qt's QWebEnginePermission that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QWebEnginePermission, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class PermissionType(CuteNum, scoped=True):
    """
    The enum 'QWebEnginePermission::PermissionType' of Qt, with the 11 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Unsupported = Kee[int](0)
    MediaAudioCapture = Kee[int](1)
    MediaVideoCapture = Kee[int](2)
    MediaAudioVideoCapture = Kee[int](3)
    DesktopVideoCapture = Kee[int](4)
    DesktopAudioVideoCapture = Kee[int](5)
    MouseLock = Kee[int](6)
    Notifications = Kee[int](7)
    Geolocation = Kee[int](8)
    ClipboardReadWrite = Kee[int](9)
    LocalFontsAccess = Kee[int](10)

  class State(CuteNum, scoped=True):
    """
    The enum 'QWebEnginePermission::State' of Qt, with the 4 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Invalid = Kee[int](0)
    Ask = Kee[int](1)
    Granted = Kee[int](2)
    Denied = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(PermissionType)
  def isPersistent(permissionType: PermissionType) -> bool:
    """
    Calls Qt's 'bool
    QWebEnginePermission::isPersistent(QWebEnginePermission::PermissionType
    permissionType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepermission.html#isPersistent

    Parameters
    ----------

    permissionType : PermissionType
      Passed on as its number.
    """
    #  bool QWebEnginePermission::isPersistent(QWebEnginePermission::
    #      PermissionType permissionType)
    return Rituals.call(
        'ritual_ZN20QWebEnginePermission12isPersistentENS_14PermissionTypeE',
        permissionType.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEnginePermission'

  #  Qt's '~QWebEnginePermission()'. Naming it makes this a value class:
  #  Python owns every C++ QWebEnginePermission behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QWebEnginePermissionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def origin(self) -> QUrl:
    """
    Calls Qt's 'QUrl QWebEnginePermission::origin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepermission.html#origin

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QWebEnginePermission::origin() const
    address = self.uglySide.call('ritual_ZNK20QWebEnginePermission6originEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def permissionType(self) -> PermissionType:
    """
    Calls Qt's 'PermissionType QWebEnginePermission::permissionType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepermission.html#permissionType

    Returns
    -------

    PermissionType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PermissionType(number)'
      gives.
    """
    #  PermissionType QWebEnginePermission::permissionType() const
    return QWebEnginePermission.PermissionType(self.uglySide.call(
        'ritual_ZNK20QWebEnginePermission14permissionTypeEv',
    ))

  def state(self) -> State:
    """
    Calls Qt's 'State QWebEnginePermission::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepermission.html#state

    Returns
    -------

    State
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'State(number)' gives.
    """
    #  State QWebEnginePermission::state() const
    return QWebEnginePermission.State(self.uglySide.call(
        'ritual_ZNK20QWebEnginePermission5stateEv',
    ))

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QWebEnginePermission::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepermission.html#isValid
    """
    #  bool QWebEnginePermission::isValid() const
    return self.uglySide.call('ritual_ZNK20QWebEnginePermission7isValidEv')

  @overload(THIS)
  def equals(self, other: QWebEnginePermission) -> bool:
    """
    Calls Qt's 'bool QWebEnginePermission::equals(const QWebEnginePermission
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepermission.html#equals

    Parameters
    ----------

    other : QWebEnginePermission
      Passed on as a value: Qt reads the C++ QWebEnginePermission, which
      stays Python's own.
    """
    #  bool QWebEnginePermission::equals(const QWebEnginePermission &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK20QWebEnginePermission6equalsERKS_', self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QWebEnginePermission) -> bool:
    """
    Calls Qt's 'bool operator==(const QWebEnginePermission &lhs, const
    QWebEnginePermission &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepermission.html#operator==

    Parameters
    ----------

    rhs : QWebEnginePermission
      Passed on as a value: Qt reads the C++ QWebEnginePermission, which
      stays Python's own.
    """
    #  bool operator==(const QWebEnginePermission &lhs, const
    #      QWebEnginePermission &rhs)
    return Rituals.call(
        'ritual_ZeqRK20QWebEnginePermissionS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QWebEnginePermission) -> bool:
    """
    Calls Qt's 'bool operator!=(const QWebEnginePermission &lhs, const
    QWebEnginePermission &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepermission.html#operator!=

    Parameters
    ----------

    rhs : QWebEnginePermission
      Passed on as a value: Qt reads the C++ QWebEnginePermission, which
      stays Python's own.
    """
    #  bool operator!=(const QWebEnginePermission &lhs, const
    #      QWebEnginePermission &rhs)
    return Rituals.call(
        'ritual_ZneRK20QWebEnginePermissionS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QWebEnginePermission::QWebEnginePermission()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepermission.html#QWebEnginePermission
    """
    #  QWebEnginePermission::QWebEnginePermission()
    self._noteCreation(QWebEnginePermission, lambda: Rituals.call(
        'ritual_ZN20QWebEnginePermissionC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QWebEnginePermission) -> None:
    """
    Notes what was given, for Qt's
    'QWebEnginePermission::QWebEnginePermission(const QWebEnginePermission
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepermission.html#QWebEnginePermission

    Parameters
    ----------

    other : QWebEnginePermission
      Passed on as a value: Qt reads the C++ QWebEnginePermission, which
      stays Python's own.
    """
    #  QWebEnginePermission::QWebEnginePermission(const QWebEnginePermission
    #      &other)
    self._noteCreation(QWebEnginePermission, lambda: Rituals.call(
        'ritual_ZN20QWebEnginePermissionC1ERKS_', self._valueOf(other),
    ))

  @overload(QWebEnginePermissionPrivate)
  @overload(NoneType)
  def __init__(self, pvt: Optional[QWebEnginePermissionPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QWebEnginePermission::QWebEnginePermission(QWebEnginePermissionPrivate
    *pvt)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginepermission.html#QWebEnginePermission

    Parameters
    ----------

    pvt : Optional[QWebEnginePermissionPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWebEnginePermission::QWebEnginePermission(QWebEnginePermissionPrivate
    #      *pvt)
    self._noteCreation(QWebEnginePermission, lambda: Rituals.call(
        'ritual_ZN20QWebEnginePermissionC1EP27QWebEnginePermissionPrivate',
        self._addressOf(pvt),
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

  def grant(self) -> None:
    """
    Calls Qt's 'void QWebEnginePermission::grant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepermission.html#grant
    """
    #  void QWebEnginePermission::grant() const
    self.uglySide.call('ritual_ZNK20QWebEnginePermission5grantEv')

  def deny(self) -> None:
    """
    Calls Qt's 'void QWebEnginePermission::deny() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepermission.html#deny
    """
    #  void QWebEnginePermission::deny() const
    self.uglySide.call('ritual_ZNK20QWebEnginePermission4denyEv')

  def reset(self) -> None:
    """
    Calls Qt's 'void QWebEnginePermission::reset() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginepermission.html#reset
    """
    #  void QWebEnginePermission::reset() const
    self.uglySide.call('ritual_ZNK20QWebEnginePermission5resetEv')

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QWebEnginePermission::swap(QWebEnginePermission &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QWebEnginePermission.swap' has no cute function yet. Qt's 'void "
        "QWebEnginePermission::swap(QWebEnginePermission &other)': takes a "
        "type Python has no way to hand over yet.")


#  Qt's 'QList<QWebEnginePermission>': the list of QWebEnginePermission,
#  which 'QList[QWebEnginePermission]' gives. It is made here, so that there
#  is one as soon as there can be a QWebEnginePermission.
QList.createKind(
    QWebEnginePermission, 'value',
    make='ritual_list_make_QWebEnginePermission',
    add='ritual_list_add_QWebEnginePermission',
    size='ritual_list_size_QWebEnginePermission',
    at='ritual_list_at_QWebEnginePermission',
    drop='ritual_list_drop_QWebEnginePermission',
)
