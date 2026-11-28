"""
Qt3DCore::QSkeletonLoader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/qskeletonloader.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSkeletonLoader(Qt3DCore.QAbstractSkeleton):
  """
  The cute side of Qt's Qt3DCore::QSkeletonLoader: a plain Python object
  standing in front of one C++ Qt3DCore::QSkeletonLoader.

  It is built on the cute 'Qt3DCore::QAbstractSkeleton', as Qt's
  Qt3DCore::QSkeletonLoader is built on Qt's Qt3DCore::QAbstractSkeleton, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QSkeletonLoader that has a ritual and that
  Python can call so far, 14 names in all: 'metaObject', 'tr', 'source',
  'status', 'isCreateJointsEnabled', 'rootJoint', 'setSource',
  'setCreateJointsEnabled', 'sourceChanged', 'statusChanged',
  'createJointsEnabledChanged', 'rootJointChanged', 'd_func', 'setRootJoint'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::QSkeletonLoader::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DCore::QSkeletonLoader::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DCore::QSkeletonLoader::~QSkeletonLoader()': the destructor:
    Python never removes a C++ Qt3DCore::QSkeletonLoader.
  - Qt's 'Qt3DCore::QSkeletonLoader::QSkeletonLoader(QSkeletonLoaderPrivate
    &dd, Qt3DCore::QNode *parent)': takes a type Python has no way to hand
    over yet.
  - Qt's 'const QSkeletonLoaderPrivate *Qt3DCore::QSkeletonLoader::d_func()
    const': takes in Python what 'QSkeletonLoaderPrivate
    *Qt3DCore::QSkeletonLoader::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DCore::QSkeletonLoader is created at the first use, not by
    'Qt3DCore::QSkeletonLoader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QSkeletonLoader.
  - Qt tells when it has removed the C++ Qt3DCore::QSkeletonLoader. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DCore::QSkeletonLoader, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Status(CuteNum):
    """
    The enum 'Qt3DCore::QSkeletonLoader::Status' of Qt, with the 3 names Qt
    gives in it.
    """

    NotReady = Kee[int](0)
    Ready = Kee[int](1)
    Error = Kee[int](2)

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
    Calls Qt's 'QString Qt3DCore::QSkeletonLoader::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qskeletonloader.html#tr

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
    #  QString Qt3DCore::QSkeletonLoader::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore15QSkeletonLoader2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QSkeletonLoader'

  #  A C++ Qt3DCore::QSkeletonLoader Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QSkeletonLoader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DCore::QSkeletonLoader::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qskeletonloader.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::QSkeletonLoader::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore15QSkeletonLoader10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl Qt3DCore::QSkeletonLoader::source() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qskeletonloader.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl Qt3DCore::QSkeletonLoader::source() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore15QSkeletonLoader6sourceEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def status(self) -> Status:
    """
    Calls Qt's 'Status Qt3DCore::QSkeletonLoader::status() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qskeletonloader.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status Qt3DCore::QSkeletonLoader::status() const
    return QSkeletonLoader.Status(self.uglySide.call(
        'ritual_ZNK8Qt3DCore15QSkeletonLoader6statusEv',
    ))

  def isCreateJointsEnabled(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::QSkeletonLoader::isCreateJointsEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qskeletonloader.html
    """
    #  bool Qt3DCore::QSkeletonLoader::isCreateJointsEnabled() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore15QSkeletonLoader21isCreateJointsEnabledEv',
    )

  def rootJoint(self) -> Optional[Qt3DCore.QJoint]:
    """
    Calls Qt's 'Qt3DCore::QJoint *Qt3DCore::QSkeletonLoader::rootJoint()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qskeletonloader.html#rootJoint

    Returns
    -------

    Optional[Qt3DCore.QJoint]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QJoint *Qt3DCore::QSkeletonLoader::rootJoint() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore15QSkeletonLoader9rootJointEv',
    )
    return Qt3DCore.QJoint._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, source: QUrl) -> None:
    """
    Calls Qt's 'void Qt3DCore::QSkeletonLoader::setSource(const QUrl
    &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qskeletonloader.html#setSource

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void Qt3DCore::QSkeletonLoader::setSource(const QUrl &source)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore15QSkeletonLoader9setSourceERK4QUrl',
        self._valueOf(source),
    )

  @overload(bool)
  def setCreateJointsEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void Qt3DCore::QSkeletonLoader::setCreateJointsEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qskeletonloader.html

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Qt3DCore::QSkeletonLoader::setCreateJointsEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore15QSkeletonLoader22setCreateJointsEnabledEb',
        enabled,
    )

  @overload(WAIT['Qt3DCore.QJoint'])
  @overload(NoneType)
  def setRootJoint(self, rootJoint: Optional[Qt3DCore.QJoint]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QSkeletonLoader::setRootJoint(QJoint
    *rootJoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qskeletonloader.html#setRootJoint

    Parameters
    ----------

    rootJoint : Optional[Qt3DCore.QJoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QSkeletonLoader::setRootJoint(QJoint *rootJoint)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore15QSkeletonLoader12setRootJointEPNS_6QJointE',
        self._addressOf(rootJoint),
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::QSkeletonLoader::QSkeletonLoader(Qt3DCore::QNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qskeletonloader.html#QSkeletonLoader

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::QSkeletonLoader::QSkeletonLoader(Qt3DCore::QNode *parent)
    self._noteCreation(QSkeletonLoader, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore15QSkeletonLoaderC1EPNS_5QNodeE',
        self._addressOf(parent),
    ))

  @overload(QUrl)
  @overload(QUrl, Qt3DCore.QNode)
  @overload(QUrl, NoneType)
  def __init__(
      self,
      source: QUrl,
      parent: Optional[Qt3DCore.QNode] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::QSkeletonLoader::QSkeletonLoader(const QUrl &source,
    Qt3DCore::QNode *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qskeletonloader.html#QSkeletonLoader

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::QSkeletonLoader::QSkeletonLoader(const QUrl &source,
    #      Qt3DCore::QNode *parent)
    self._noteCreation(QSkeletonLoader, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore15QSkeletonLoaderC1ERK4QUrlPNS_5QNodeE',
        self._valueOf(source), self._addressOf(parent),
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

  @overload(QUrl)
  def sourceChanged(self, source: QUrl) -> None:
    """
    Calls Qt's 'void Qt3DCore::QSkeletonLoader::sourceChanged(const QUrl
    &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qskeletonloader.html#sourceChanged

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void Qt3DCore::QSkeletonLoader::sourceChanged(const QUrl &source)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore15QSkeletonLoader13sourceChangedERK4QUrl',
        self._valueOf(source),
    )

  @overload(Status)
  def statusChanged(self, status: Status) -> None:
    """
    Calls Qt's 'void Qt3DCore::QSkeletonLoader::statusChanged(Status
    status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qskeletonloader.html#statusChanged

    Parameters
    ----------

    status : Status
      Passed on as its number.
    """
    #  void Qt3DCore::QSkeletonLoader::statusChanged(Status status)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore15QSkeletonLoader13statusChangedENS0_6StatusE',
        status.value,
    )

  @overload(bool)
  def createJointsEnabledChanged(self, createJointsEnabled: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QSkeletonLoader::createJointsEnabledChanged(bool
    createJointsEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qskeletonloader.html

    Parameters
    ----------

    createJointsEnabled : bool
      Passed on as it is.
    """
    #  void Qt3DCore::QSkeletonLoader::createJointsEnabledChanged(bool
    #      createJointsEnabled)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore15QSkeletonLoader26createJointsEnabledChangedEb',
        createJointsEnabled,
    )

  @overload(WAIT['Qt3DCore.QJoint'])
  @overload(NoneType)
  def rootJointChanged(self, rootJoint: Optional[Qt3DCore.QJoint]) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QSkeletonLoader::rootJointChanged(Qt3DCore::QJoint
    *rootJoint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qskeletonloader.html#rootJointChanged

    Parameters
    ----------

    rootJoint : Optional[Qt3DCore.QJoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QSkeletonLoader::rootJointChanged(Qt3DCore::QJoint
    #      *rootJoint)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore15QSkeletonLoader16rootJointChangedEPNS_6QJointE',
        self._addressOf(rootJoint),
    )

  def d_func(self) -> Optional[Qt3DCore.QSkeletonLoaderPrivate]:
    """
    Calls Qt's 'QSkeletonLoaderPrivate *Qt3DCore::QSkeletonLoader::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qskeletonloader.html#d_func

    Returns
    -------

    Optional[Qt3DCore.QSkeletonLoaderPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSkeletonLoaderPrivate *Qt3DCore::QSkeletonLoader::d_func()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore15QSkeletonLoader6d_funcEv',
    )
    return Qt3DCore.QSkeletonLoaderPrivate._cuteAt(address)
