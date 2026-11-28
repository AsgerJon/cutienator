"""
Qt3DRender::QComputeCommand binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qcomputecommand.h, Qt 6.12.0. Changes made here are lost.
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

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QComputeCommand(Qt3DCore.QComponent):
  """
  The cute side of Qt's Qt3DRender::QComputeCommand: a plain Python object
  standing in front of one C++ Qt3DRender::QComputeCommand.

  It is built on the cute 'Qt3DCore::QComponent', as Qt's
  Qt3DRender::QComputeCommand is built on Qt's Qt3DCore::QComponent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QComputeCommand that has a ritual and
  that Python can call so far, 16 names in all: 'metaObject', 'tr',
  'workGroupX', 'workGroupY', 'workGroupZ', 'runType', 'setWorkGroupX',
  'setWorkGroupY', 'setWorkGroupZ', 'setRunType', 'trigger',
  'workGroupXChanged', 'workGroupYChanged', 'workGroupZChanged',
  'runTypeChanged', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QComputeCommand::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QComputeCommand::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QComputeCommand::~QComputeCommand()': the destructor:
    Python never removes a C++ Qt3DRender::QComputeCommand.
  - Qt's 'const QComputeCommandPrivate *Qt3DRender::QComputeCommand::d_func()
    const': takes in Python what 'QComputeCommandPrivate
    *Qt3DRender::QComputeCommand::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 24 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QComputeCommand is created at the first use, not by
    'Qt3DRender::QComputeCommand(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QComputeCommand.
  - Qt tells when it has removed the C++ Qt3DRender::QComputeCommand. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QComputeCommand, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class RunType(CuteNum):
    """
    The enum 'Qt3DRender::QComputeCommand::RunType' of Qt, with the 2 names
    Qt gives in it.
    """

    Continuous = Kee[int](0)
    Manual = Kee[int](1)

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
    Calls Qt's 'QString Qt3DRender::QComputeCommand::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qcomputecommand.html#tr

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
    #  QString Qt3DRender::QComputeCommand::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender15QComputeCommand2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QComputeCommand'

  #  A C++ Qt3DRender::QComputeCommand Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QComputeCommand'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QComputeCommand::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcomputecommand.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QComputeCommand::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender15QComputeCommand10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def workGroupX(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QComputeCommand::workGroupX() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcomputecommand.html#workGroupX
    """
    #  int Qt3DRender::QComputeCommand::workGroupX() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender15QComputeCommand10workGroupXEv',
    )

  def workGroupY(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QComputeCommand::workGroupY() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcomputecommand.html#workGroupY
    """
    #  int Qt3DRender::QComputeCommand::workGroupY() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender15QComputeCommand10workGroupYEv',
    )

  def workGroupZ(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QComputeCommand::workGroupZ() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcomputecommand.html#workGroupZ
    """
    #  int Qt3DRender::QComputeCommand::workGroupZ() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender15QComputeCommand10workGroupZEv',
    )

  def runType(self) -> RunType:
    """
    Calls Qt's 'RunType Qt3DRender::QComputeCommand::runType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcomputecommand.html#runType

    Returns
    -------

    RunType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RunType(number)' gives.
    """
    #  RunType Qt3DRender::QComputeCommand::runType() const
    return QComputeCommand.RunType(self.uglySide.call(
        'ritual_ZNK10Qt3DRender15QComputeCommand7runTypeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setWorkGroupX(self, workGroupX: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QComputeCommand::setWorkGroupX(int
    workGroupX)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcomputecommand.html#setWorkGroupX

    Parameters
    ----------

    workGroupX : int
      Passed on as it is.
    """
    #  void Qt3DRender::QComputeCommand::setWorkGroupX(int workGroupX)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender15QComputeCommand13setWorkGroupXEi',
        workGroupX,
    )

  @overload(int)
  def setWorkGroupY(self, workGroupY: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QComputeCommand::setWorkGroupY(int
    workGroupY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcomputecommand.html#setWorkGroupY

    Parameters
    ----------

    workGroupY : int
      Passed on as it is.
    """
    #  void Qt3DRender::QComputeCommand::setWorkGroupY(int workGroupY)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender15QComputeCommand13setWorkGroupYEi',
        workGroupY,
    )

  @overload(int)
  def setWorkGroupZ(self, workGroupZ: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QComputeCommand::setWorkGroupZ(int
    workGroupZ)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcomputecommand.html#setWorkGroupZ

    Parameters
    ----------

    workGroupZ : int
      Passed on as it is.
    """
    #  void Qt3DRender::QComputeCommand::setWorkGroupZ(int workGroupZ)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender15QComputeCommand13setWorkGroupZEi',
        workGroupZ,
    )

  @overload(RunType)
  def setRunType(self, runType: RunType) -> None:
    """
    Calls Qt's 'void Qt3DRender::QComputeCommand::setRunType(RunType
    runType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcomputecommand.html#setRunType

    Parameters
    ----------

    runType : RunType
      Passed on as its number.
    """
    #  void Qt3DRender::QComputeCommand::setRunType(RunType runType)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender15QComputeCommand10setRunTypeENS0_7RunTypeE',
        runType.value,
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
    'Qt3DRender::QComputeCommand::QComputeCommand(Qt3DCore::QNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcomputecommand.html#QComputeCommand

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QComputeCommand::QComputeCommand(Qt3DCore::QNode *parent)
    self._noteCreation(QComputeCommand, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender15QComputeCommandC1EPN8Qt3DCore5QNodeE',
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

  @overload()
  @overload(int)
  def trigger(self, frameCount: int = 1) -> None:
    """
    Calls Qt's 'void Qt3DRender::QComputeCommand::trigger(int frameCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcomputecommand.html#trigger

    Parameters
    ----------

    frameCount : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void Qt3DRender::QComputeCommand::trigger(int frameCount)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender15QComputeCommand7triggerEi', frameCount,
    )

  @overload(int, int, int)
  @overload(int, int, int, int)
  def trigger(
      self,
      workGroupX: int,
      workGroupY: int,
      workGroupZ: int,
      frameCount: int = 1,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::QComputeCommand::trigger(int workGroupX, int
    workGroupY, int workGroupZ, int frameCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcomputecommand.html#trigger

    Parameters
    ----------

    workGroupX : int
      Passed on as it is.

    workGroupY : int
      Passed on as it is.

    workGroupZ : int
      Passed on as it is.

    frameCount : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void Qt3DRender::QComputeCommand::trigger(int workGroupX, int
    #      workGroupY, int workGroupZ, int frameCount)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender15QComputeCommand7triggerEiiii',
        workGroupX, workGroupY, workGroupZ, frameCount,
    )

  def workGroupXChanged(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QComputeCommand::workGroupXChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcomputecommand.html#workGroupXChanged
    """
    #  void Qt3DRender::QComputeCommand::workGroupXChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender15QComputeCommand17workGroupXChangedEv',
    )

  def workGroupYChanged(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QComputeCommand::workGroupYChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcomputecommand.html#workGroupYChanged
    """
    #  void Qt3DRender::QComputeCommand::workGroupYChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender15QComputeCommand17workGroupYChangedEv',
    )

  def workGroupZChanged(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QComputeCommand::workGroupZChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcomputecommand.html#workGroupZChanged
    """
    #  void Qt3DRender::QComputeCommand::workGroupZChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender15QComputeCommand17workGroupZChangedEv',
    )

  def runTypeChanged(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QComputeCommand::runTypeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcomputecommand.html#runTypeChanged
    """
    #  void Qt3DRender::QComputeCommand::runTypeChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender15QComputeCommand14runTypeChangedEv',
    )

  def d_func(self) -> Optional[Qt3DRender.QComputeCommandPrivate]:
    """
    Calls Qt's 'QComputeCommandPrivate
    *Qt3DRender::QComputeCommand::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qcomputecommand.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QComputeCommandPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QComputeCommandPrivate *Qt3DRender::QComputeCommand::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender15QComputeCommand6d_funcEv',
    )
    return Qt3DRender.QComputeCommandPrivate._cuteAt(address)
