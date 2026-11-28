"""
Qt3DRender::QSetFence binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qsetfence.h, Qt 6.12.0. Changes made here are lost.
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


class QSetFence(Qt3DRender.QFrameGraphNode):
  """
  The cute side of Qt's Qt3DRender::QSetFence: a plain Python object standing
  in front of one C++ Qt3DRender::QSetFence.

  It is built on the cute 'Qt3DRender::QFrameGraphNode', as Qt's
  Qt3DRender::QSetFence is built on Qt's Qt3DRender::QFrameGraphNode, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QSetFence that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'tr', 'handleType',
  'handle', 'handleTypeChanged', 'handleChanged', 'd_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QSetFence::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DRender::QSetFence::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QSetFence::~QSetFence()': the destructor: Python never
    removes a C++ Qt3DRender::QSetFence.
  - Qt's 'Qt3DRender::QSetFence::QSetFence(QSetFencePrivate &dd,
    Qt3DCore::QNode *parent)': takes a type Python has no way to hand over
    yet.
  - Qt's 'const QSetFencePrivate *Qt3DRender::QSetFence::d_func() const':
    takes in Python what 'QSetFencePrivate *Qt3DRender::QSetFence::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QSetFence is created at the first use, not by
    'Qt3DRender::QSetFence(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QSetFence.
  - Qt tells when it has removed the C++ Qt3DRender::QSetFence. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QSetFence, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class HandleType(CuteNum):
    """
    The enum 'Qt3DRender::QSetFence::HandleType' of Qt, with the 2 names Qt
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
    Calls Qt's 'QString Qt3DRender::QSetFence::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qsetfence.html#tr

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
    #  QString Qt3DRender::QSetFence::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender9QSetFence2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QSetFence'

  #  A C++ Qt3DRender::QSetFence Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QSetFence'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QSetFence::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsetfence.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QSetFence::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender9QSetFence10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def handleType(self) -> HandleType:
    """
    Calls Qt's 'HandleType Qt3DRender::QSetFence::handleType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsetfence.html#handleType

    Returns
    -------

    HandleType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'HandleType(number)'
      gives.
    """
    #  HandleType Qt3DRender::QSetFence::handleType() const
    return QSetFence.HandleType(self.uglySide.call(
        'ritual_ZNK10Qt3DRender9QSetFence10handleTypeEv',
    ))

  def handle(self) -> QVariant:
    """
    Calls Qt's 'QVariant Qt3DRender::QSetFence::handle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qsetfence.html#handle

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DRender::QSetFence::handle() const
    address = self.uglySide.call('ritual_ZNK10Qt3DRender9QSetFence6handleEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QSetFence::QSetFence(Qt3DCore::QNode *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsetfence.html#QSetFence

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QSetFence::QSetFence(Qt3DCore::QNode *parent)
    self._noteCreation(QSetFence, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender9QSetFenceC1EPN8Qt3DCore5QNodeE',
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

  @overload(HandleType)
  def handleTypeChanged(self, handleType: HandleType) -> None:
    """
    Calls Qt's 'void Qt3DRender::QSetFence::handleTypeChanged(HandleType
    handleType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsetfence.html#handleTypeChanged

    Parameters
    ----------

    handleType : HandleType
      Passed on as its number.
    """
    #  void Qt3DRender::QSetFence::handleTypeChanged(HandleType handleType)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender9QSetFence17handleTypeChangedENS0_10HandleTyp'
        'eE',
        handleType.value,
    )

  @overload(QVariant)
  def handleChanged(self, handle: QVariant) -> None:
    """
    Calls Qt's 'void Qt3DRender::QSetFence::handleChanged(QVariant handle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsetfence.html#handleChanged

    Parameters
    ----------

    handle : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void Qt3DRender::QSetFence::handleChanged(QVariant handle)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender9QSetFence13handleChangedE8QVariant',
        self._valueOf(handle),
    )

  def d_func(self) -> Optional[Qt3DRender.QSetFencePrivate]:
    """
    Calls Qt's 'QSetFencePrivate *Qt3DRender::QSetFence::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qsetfence.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QSetFencePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSetFencePrivate *Qt3DRender::QSetFence::d_func()
    address = self.uglySide.call('ritual_ZN10Qt3DRender9QSetFence6d_funcEv')
    return Qt3DRender.QSetFencePrivate._cuteAt(address)
