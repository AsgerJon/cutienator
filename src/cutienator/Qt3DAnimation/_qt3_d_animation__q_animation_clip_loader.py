"""
Qt3DAnimation::QAnimationClipLoader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/qanimationcliploader.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DAnimation

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


class QAnimationClipLoader(Qt3DAnimation.QAbstractAnimationClip):
  """
  The cute side of Qt's Qt3DAnimation::QAnimationClipLoader: a plain Python
  object standing in front of one C++ Qt3DAnimation::QAnimationClipLoader.

  It is built on the cute 'Qt3DAnimation::QAbstractAnimationClip', as Qt's
  Qt3DAnimation::QAnimationClipLoader is built on Qt's
  Qt3DAnimation::QAbstractAnimationClip, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QAnimationClipLoader that has a
  ritual and that Python can call so far, 8 names in all: 'metaObject', 'tr',
  'source', 'status', 'setSource', 'sourceChanged', 'statusChanged',
  'd_func'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DAnimation::QAnimationClipLoader::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DAnimation::QAnimationClipLoader::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DAnimation::QAnimationClipLoader::~QAnimationClipLoader()': the
    destructor: Python never removes a C++
    Qt3DAnimation::QAnimationClipLoader.
  - Qt's 'Qt3DAnimation::QAnimationClipLoader::QAnimationClipLoader(
    QAnimationClipLoaderPrivate &dd, Qt3DCore::QNode *parent)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QAnimationClipLoaderPrivate
    *Qt3DAnimation::QAnimationClipLoader::d_func() const': takes in Python
    what 'QAnimationClipLoaderPrivate
    *Qt3DAnimation::QAnimationClipLoader::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QAnimationClipLoader is created at the first use,
    not by 'Qt3DAnimation::QAnimationClipLoader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::QAnimationClipLoader.
  - Qt tells when it has removed the C++ Qt3DAnimation::QAnimationClipLoader.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DAnimation::QAnimationClipLoader, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class Status(CuteNum):
    """
    The enum 'Qt3DAnimation::QAnimationClipLoader::Status' of Qt, with the 3
    names Qt gives in it.
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
    Calls Qt's 'QString Qt3DAnimation::QAnimationClipLoader::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcliploader.html#tr

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
    #  QString Qt3DAnimation::QAnimationClipLoader::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN13Qt3DAnimation20QAnimationClipLoader2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QAnimationClipLoader'

  #  A C++ Qt3DAnimation::QAnimationClipLoader Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DAnimation_QAnimationClipLoader'

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
    *Qt3DAnimation::QAnimationClipLoader::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcliploader.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DAnimation::QAnimationClipLoader::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation20QAnimationClipLoader10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl Qt3DAnimation::QAnimationClipLoader::source() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcliploader.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl Qt3DAnimation::QAnimationClipLoader::source() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation20QAnimationClipLoader6sourceEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def status(self) -> Status:
    """
    Calls Qt's 'Status Qt3DAnimation::QAnimationClipLoader::status() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcliploader.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status Qt3DAnimation::QAnimationClipLoader::status() const
    return QAnimationClipLoader.Status(self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation20QAnimationClipLoader6statusEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, source: QUrl) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QAnimationClipLoader::setSource(const
    QUrl &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcliploader.html#setSource

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void Qt3DAnimation::QAnimationClipLoader::setSource(const QUrl
    #      &source)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation20QAnimationClipLoader9setSourceERK4QUrl',
        self._valueOf(source),
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
    'Qt3DAnimation::QAnimationClipLoader::QAnimationClipLoader(Qt3DCore::
    QNode *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcliploader.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DAnimation::QAnimationClipLoader::QAnimationClipLoader(
    #      Qt3DCore::QNode *parent)
    self._noteCreation(QAnimationClipLoader, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation20QAnimationClipLoaderC1EPN8Qt3DCore5QNode'
        'E',
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
    'Qt3DAnimation::QAnimationClipLoader::QAnimationClipLoader(const QUrl
    &source, Qt3DCore::QNode *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcliploader.html

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DAnimation::QAnimationClipLoader::QAnimationClipLoader(const QUrl
    #      &source, Qt3DCore::QNode *parent)
    self._noteCreation(QAnimationClipLoader, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation20QAnimationClipLoaderC1ERK4QUrlPN8Qt3DCor'
        'e5QNodeE',
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
    Calls Qt's 'void Qt3DAnimation::QAnimationClipLoader::sourceChanged(const
    QUrl &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcliploader.html

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void Qt3DAnimation::QAnimationClipLoader::sourceChanged(const QUrl
    #      &source)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation20QAnimationClipLoader13sourceChangedERK4Q'
        'Url',
        self._valueOf(source),
    )

  @overload(Status)
  def statusChanged(self, status: Status) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAnimationClipLoader::statusChanged(Status status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcliploader.html

    Parameters
    ----------

    status : Status
      Passed on as its number.
    """
    #  void Qt3DAnimation::QAnimationClipLoader::statusChanged(Status status)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation20QAnimationClipLoader13statusChangedENS0_'
        '6StatusE',
        status.value,
    )

  def d_func(self) -> Optional[Qt3DAnimation.QAnimationClipLoaderPrivate]:
    """
    Calls Qt's 'QAnimationClipLoaderPrivate
    *Qt3DAnimation::QAnimationClipLoader::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcliploader.html#d_func

    Returns
    -------

    Optional[Qt3DAnimation.QAnimationClipLoaderPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAnimationClipLoaderPrivate
    #      *Qt3DAnimation::QAnimationClipLoader::d_func()
    address = self.uglySide.call(
        'ritual_ZN13Qt3DAnimation20QAnimationClipLoader6d_funcEv',
    )
    return Qt3DAnimation.QAnimationClipLoaderPrivate._cuteAt(address)
