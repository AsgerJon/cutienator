"""
Qt3DRender::QDispatchCompute binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qdispatchcompute.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDispatchCompute(Qt3DRender.QFrameGraphNode):
  """
  The cute side of Qt's Qt3DRender::QDispatchCompute: a plain Python object
  standing in front of one C++ Qt3DRender::QDispatchCompute.

  It is built on the cute 'Qt3DRender::QFrameGraphNode', as Qt's
  Qt3DRender::QDispatchCompute is built on Qt's Qt3DRender::QFrameGraphNode,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QDispatchCompute that has a ritual and
  that Python can call so far, 12 names in all: 'metaObject', 'tr',
  'workGroupX', 'workGroupY', 'workGroupZ', 'setWorkGroupX', 'setWorkGroupY',
  'setWorkGroupZ', 'workGroupXChanged', 'workGroupYChanged',
  'workGroupZChanged', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QDispatchCompute::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QDispatchCompute::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QDispatchCompute::~QDispatchCompute()': the destructor:
    Python never removes a C++ Qt3DRender::QDispatchCompute.
  - Qt's 'const QDispatchComputePrivate
    *Qt3DRender::QDispatchCompute::d_func() const': takes in Python what
    'QDispatchComputePrivate *Qt3DRender::QDispatchCompute::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QDispatchCompute is created at the first use, not by
    'Qt3DRender::QDispatchCompute(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QDispatchCompute.
  - Qt tells when it has removed the C++ Qt3DRender::QDispatchCompute. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString Qt3DRender::QDispatchCompute::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qdispatchcompute.html#tr

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
    #  QString Qt3DRender::QDispatchCompute::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender16QDispatchCompute2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QDispatchCompute'

  #  A C++ Qt3DRender::QDispatchCompute Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QDispatchCompute'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QDispatchCompute::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qdispatchcompute.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QDispatchCompute::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QDispatchCompute10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def workGroupX(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QDispatchCompute::workGroupX() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qdispatchcompute.html#workGroupX
    """
    #  int Qt3DRender::QDispatchCompute::workGroupX() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QDispatchCompute10workGroupXEv',
    )

  def workGroupY(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QDispatchCompute::workGroupY() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qdispatchcompute.html#workGroupY
    """
    #  int Qt3DRender::QDispatchCompute::workGroupY() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QDispatchCompute10workGroupYEv',
    )

  def workGroupZ(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::QDispatchCompute::workGroupZ() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qdispatchcompute.html#workGroupZ
    """
    #  int Qt3DRender::QDispatchCompute::workGroupZ() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender16QDispatchCompute10workGroupZEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setWorkGroupX(self, workGroupX: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QDispatchCompute::setWorkGroupX(int
    workGroupX)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qdispatchcompute.html#setWorkGroupX

    Parameters
    ----------

    workGroupX : int
      Passed on as it is.
    """
    #  void Qt3DRender::QDispatchCompute::setWorkGroupX(int workGroupX)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QDispatchCompute13setWorkGroupXEi',
        workGroupX,
    )

  @overload(int)
  def setWorkGroupY(self, workGroupY: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QDispatchCompute::setWorkGroupY(int
    workGroupY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qdispatchcompute.html#setWorkGroupY

    Parameters
    ----------

    workGroupY : int
      Passed on as it is.
    """
    #  void Qt3DRender::QDispatchCompute::setWorkGroupY(int workGroupY)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QDispatchCompute13setWorkGroupYEi',
        workGroupY,
    )

  @overload(int)
  def setWorkGroupZ(self, workGroupZ: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QDispatchCompute::setWorkGroupZ(int
    workGroupZ)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qdispatchcompute.html#setWorkGroupZ

    Parameters
    ----------

    workGroupZ : int
      Passed on as it is.
    """
    #  void Qt3DRender::QDispatchCompute::setWorkGroupZ(int workGroupZ)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QDispatchCompute13setWorkGroupZEi',
        workGroupZ,
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
    'Qt3DRender::QDispatchCompute::QDispatchCompute(Qt3DCore::QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qdispatchcompute.html#QDispatchCompute

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QDispatchCompute::QDispatchCompute(Qt3DCore::QNode
    #      *parent)
    self._noteCreation(QDispatchCompute, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender16QDispatchComputeC1EPN8Qt3DCore5QNodeE',
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

  def workGroupXChanged(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QDispatchCompute::workGroupXChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qdispatchcompute.html#workGroupXChanged
    """
    #  void Qt3DRender::QDispatchCompute::workGroupXChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QDispatchCompute17workGroupXChangedEv',
    )

  def workGroupYChanged(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QDispatchCompute::workGroupYChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qdispatchcompute.html#workGroupYChanged
    """
    #  void Qt3DRender::QDispatchCompute::workGroupYChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QDispatchCompute17workGroupYChangedEv',
    )

  def workGroupZChanged(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QDispatchCompute::workGroupZChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qdispatchcompute.html#workGroupZChanged
    """
    #  void Qt3DRender::QDispatchCompute::workGroupZChanged()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender16QDispatchCompute17workGroupZChangedEv',
    )

  def d_func(self) -> Optional[Qt3DRender.QDispatchComputePrivate]:
    """
    Calls Qt's 'QDispatchComputePrivate
    *Qt3DRender::QDispatchCompute::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qdispatchcompute.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QDispatchComputePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDispatchComputePrivate *Qt3DRender::QDispatchCompute::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender16QDispatchCompute6d_funcEv',
    )
    return Qt3DRender.QDispatchComputePrivate._cuteAt(address)
