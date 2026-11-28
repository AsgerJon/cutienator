"""
Qt3DRender::QWaitFence binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qwaitfence.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaitFence(Qt3DRender.QFrameGraphNode):
  """
  The cute side of Qt's Qt3DRender::QWaitFence: a plain Python object
  standing in front of one C++ Qt3DRender::QWaitFence.

  It is built on the cute 'Qt3DRender::QFrameGraphNode', as Qt's
  Qt3DRender::QWaitFence is built on Qt's Qt3DRender::QFrameGraphNode, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QWaitFence that has a ritual and that
  Python can call so far, 15 names in all: 'metaObject', 'tr',
  'setHandleType', 'setHandle', 'handleType', 'handle', 'waitOnCPU',
  'setWaitOnCPU', 'timeout', 'setTimeout', 'waitOnCPUChanged',
  'timeoutChanged', 'handleTypeChanged', 'handleChanged', 'd_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QWaitFence::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DRender::QWaitFence::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QWaitFence::~QWaitFence()': the destructor: Python
    never removes a C++ Qt3DRender::QWaitFence.
  - Qt's 'Qt3DRender::QWaitFence::QWaitFence(QWaitFencePrivate &dd,
    Qt3DCore::QNode *parent)': takes a type Python has no way to hand over
    yet.
  - Qt's 'const QWaitFencePrivate *Qt3DRender::QWaitFence::d_func() const':
    takes in Python what 'QWaitFencePrivate
    *Qt3DRender::QWaitFence::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QWaitFence is created at the first use, not by
    'Qt3DRender::QWaitFence(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QWaitFence.
  - Qt tells when it has removed the C++ Qt3DRender::QWaitFence. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QWaitFence, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class HandleType(CuteNum):
    """
    The enum 'Qt3DRender::QWaitFence::HandleType' of Qt, with the 2 names Qt
    gives in it.
    """

    NoHandle = Kee[int](0)
    OpenGLFenceId = Kee[int](1)

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
    Calls Qt's 'QString Qt3DRender::QWaitFence::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qwaitfence.html#tr

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
    #  QString Qt3DRender::QWaitFence::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender10QWaitFence2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QWaitFence'

  #  A C++ Qt3DRender::QWaitFence Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QWaitFence'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QWaitFence::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qwaitfence.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QWaitFence::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QWaitFence10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def handleType(self) -> HandleType:
    """
    Calls Qt's 'HandleType Qt3DRender::QWaitFence::handleType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qwaitfence.html#handleType

    Returns
    -------

    HandleType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'HandleType(number)'
      gives.
    """
    #  HandleType Qt3DRender::QWaitFence::handleType() const
    return QWaitFence.HandleType(self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QWaitFence10handleTypeEv',
    ))

  def handle(self) -> QVariant:
    """
    Calls Qt's 'QVariant Qt3DRender::QWaitFence::handle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qwaitfence.html#handle

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DRender::QWaitFence::handle() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QWaitFence6handleEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def waitOnCPU(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QWaitFence::waitOnCPU() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qwaitfence.html#waitOnCPU
    """
    #  bool Qt3DRender::QWaitFence::waitOnCPU() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender10QWaitFence9waitOnCPUEv',
    )

  def timeout(self) -> int:
    """
    Calls Qt's 'quint64 Qt3DRender::QWaitFence::timeout() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qwaitfence.html#timeout
    """
    #  quint64 Qt3DRender::QWaitFence::timeout() const
    return self.uglySide.call('ritual_ZNK10Qt3DRender10QWaitFence7timeoutEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(HandleType)
  def setHandleType(self, type: HandleType) -> None:
    """
    Calls Qt's 'void Qt3DRender::QWaitFence::setHandleType(HandleType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qwaitfence.html#setHandleType

    Parameters
    ----------

    type : HandleType
      Passed on as its number.
    """
    #  void Qt3DRender::QWaitFence::setHandleType(HandleType type)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QWaitFence13setHandleTypeENS0_10HandleTypeE',
        type.value,
    )

  @overload(QVariant)
  def setHandle(self, handle: QVariant) -> None:
    """
    Calls Qt's 'void Qt3DRender::QWaitFence::setHandle(QVariant handle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qwaitfence.html#setHandle

    Parameters
    ----------

    handle : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DRender::QWaitFence::setHandle(QVariant handle)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QWaitFence9setHandleE8QVariant',
        self._valueOf(handle),
    )

  @overload(bool)
  def setWaitOnCPU(self, waitOnCPU: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::QWaitFence::setWaitOnCPU(bool waitOnCPU)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qwaitfence.html#setWaitOnCPU

    Parameters
    ----------

    waitOnCPU : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QWaitFence::setWaitOnCPU(bool waitOnCPU)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QWaitFence12setWaitOnCPUEb', waitOnCPU,
    )

  @overload(int)
  def setTimeout(self, timeout: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QWaitFence::setTimeout(quint64 timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qwaitfence.html#setTimeout

    Parameters
    ----------

    timeout : int
      Passed on as it is.
    """
    #  void Qt3DRender::QWaitFence::setTimeout(quint64 timeout)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QWaitFence10setTimeoutEy', timeout,
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
    'Qt3DRender::QWaitFence::QWaitFence(Qt3DCore::QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qwaitfence.html#QWaitFence

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QWaitFence::QWaitFence(Qt3DCore::QNode *parent)
    self._noteCreation(QWaitFence, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender10QWaitFenceC1EPN8Qt3DCore5QNodeE',
        self._addressOf(parent),
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

  @overload(bool)
  def waitOnCPUChanged(self, waitOnCPU: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::QWaitFence::waitOnCPUChanged(bool
    waitOnCPU)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qwaitfence.html#waitOnCPUChanged

    Parameters
    ----------

    waitOnCPU : bool
      Passed on as it is.
    """
    #  void Qt3DRender::QWaitFence::waitOnCPUChanged(bool waitOnCPU)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QWaitFence16waitOnCPUChangedEb', waitOnCPU,
    )

  @overload(int)
  def timeoutChanged(self, timeoutChanged: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QWaitFence::timeoutChanged(quint64
    timeoutChanged)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qwaitfence.html#timeoutChanged

    Parameters
    ----------

    timeoutChanged : int
      Passed on as it is.
    """
    #  void Qt3DRender::QWaitFence::timeoutChanged(quint64 timeoutChanged)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QWaitFence14timeoutChangedEy',
        timeoutChanged,
    )

  @overload(HandleType)
  def handleTypeChanged(self, handleType: HandleType) -> None:
    """
    Calls Qt's 'void Qt3DRender::QWaitFence::handleTypeChanged(HandleType
    handleType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qwaitfence.html#handleTypeChanged

    Parameters
    ----------

    handleType : HandleType
      Passed on as its number.
    """
    #  void Qt3DRender::QWaitFence::handleTypeChanged(HandleType handleType)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QWaitFence17handleTypeChangedENS0_10HandleT'
        'ypeE',
        handleType.value,
    )

  @overload(QVariant)
  def handleChanged(self, handle: QVariant) -> None:
    """
    Calls Qt's 'void Qt3DRender::QWaitFence::handleChanged(QVariant handle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qwaitfence.html#handleChanged

    Parameters
    ----------

    handle : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DRender::QWaitFence::handleChanged(QVariant handle)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender10QWaitFence13handleChangedE8QVariant',
        self._valueOf(handle),
    )

  def d_func(self) -> Optional[Qt3DRender.QWaitFencePrivate]:
    """
    Calls Qt's 'QWaitFencePrivate *Qt3DRender::QWaitFence::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qwaitfence.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QWaitFencePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaitFencePrivate *Qt3DRender::QWaitFence::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender10QWaitFence6d_funcEv',
    )
    return Qt3DRender.QWaitFencePrivate._cuteAt(address)
