"""
Qt3DRender::QStencilMask binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qstencilmask.h, Qt 6.12.0. Changes made here are lost.
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


class QStencilMask(Qt3DRender.QRenderState):
  """
  The cute side of Qt's Qt3DRender::QStencilMask: a plain Python object
  standing in front of one C++ Qt3DRender::QStencilMask.

  It is built on the cute 'Qt3DRender::QRenderState', as Qt's
  Qt3DRender::QStencilMask is built on Qt's Qt3DRender::QRenderState, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QStencilMask that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr',
  'frontOutputMask', 'backOutputMask', 'setFrontOutputMask',
  'setBackOutputMask', 'frontOutputMaskChanged', 'backOutputMaskChanged',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QStencilMask::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QStencilMask::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QStencilMask::~QStencilMask()': the destructor: Python
    never removes a C++ Qt3DRender::QStencilMask.
  - Qt's 'const QStencilMaskPrivate *Qt3DRender::QStencilMask::d_func()
    const': takes in Python what 'QStencilMaskPrivate
    *Qt3DRender::QStencilMask::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QStencilMask is created at the first use, not by
    'Qt3DRender::QStencilMask(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QStencilMask.
  - Qt tells when it has removed the C++ Qt3DRender::QStencilMask. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString Qt3DRender::QStencilMask::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qstencilmask.html#tr

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
    #  QString Qt3DRender::QStencilMask::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender12QStencilMask2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QStencilMask'

  #  A C++ Qt3DRender::QStencilMask Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QStencilMask'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QStencilMask::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstencilmask.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QStencilMask::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QStencilMask10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def frontOutputMask(self) -> int:
    """
    Calls Qt's 'uint Qt3DRender::QStencilMask::frontOutputMask() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstencilmask.html#frontOutputMask
    """
    #  uint Qt3DRender::QStencilMask::frontOutputMask() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QStencilMask15frontOutputMaskEv',
    )

  def backOutputMask(self) -> int:
    """
    Calls Qt's 'uint Qt3DRender::QStencilMask::backOutputMask() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstencilmask.html#backOutputMask
    """
    #  uint Qt3DRender::QStencilMask::backOutputMask() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QStencilMask14backOutputMaskEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setFrontOutputMask(self, frontOutputMask: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QStencilMask::setFrontOutputMask(uint
    frontOutputMask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstencilmask.html#setFrontOutputMask

    Parameters
    ----------

    frontOutputMask : int
      Passed on as it is.
    """
    #  void Qt3DRender::QStencilMask::setFrontOutputMask(uint
    #      frontOutputMask)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QStencilMask18setFrontOutputMaskEj',
        frontOutputMask,
    )

  @overload(int)
  def setBackOutputMask(self, backOutputMask: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QStencilMask::setBackOutputMask(uint
    backOutputMask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstencilmask.html#setBackOutputMask

    Parameters
    ----------

    backOutputMask : int
      Passed on as it is.
    """
    #  void Qt3DRender::QStencilMask::setBackOutputMask(uint backOutputMask)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QStencilMask17setBackOutputMaskEj',
        backOutputMask,
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
    'Qt3DRender::QStencilMask::QStencilMask(Qt3DCore::QNode *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstencilmask.html#QStencilMask

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QStencilMask::QStencilMask(Qt3DCore::QNode *parent)
    self._noteCreation(QStencilMask, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender12QStencilMaskC1EPN8Qt3DCore5QNodeE',
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

  @overload(int)
  def frontOutputMaskChanged(self, frontOutputMask: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QStencilMask::frontOutputMaskChanged(uint
    frontOutputMask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstencilmask.html

    Parameters
    ----------

    frontOutputMask : int
      Passed on as it is.
    """
    #  void Qt3DRender::QStencilMask::frontOutputMaskChanged(uint
    #      frontOutputMask)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QStencilMask22frontOutputMaskChangedEj',
        frontOutputMask,
    )

  @overload(int)
  def backOutputMaskChanged(self, backOutputMask: int) -> None:
    """
    Calls Qt's 'void Qt3DRender::QStencilMask::backOutputMaskChanged(uint
    backOutputMask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstencilmask.html#backOutputMaskChanged

    Parameters
    ----------

    backOutputMask : int
      Passed on as it is.
    """
    #  void Qt3DRender::QStencilMask::backOutputMaskChanged(uint
    #      backOutputMask)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QStencilMask21backOutputMaskChangedEj',
        backOutputMask,
    )

  def d_func(self) -> Optional[Qt3DRender.QStencilMaskPrivate]:
    """
    Calls Qt's 'QStencilMaskPrivate *Qt3DRender::QStencilMask::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qstencilmask.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QStencilMaskPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStencilMaskPrivate *Qt3DRender::QStencilMask::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender12QStencilMask6d_funcEv',
    )
    return Qt3DRender.QStencilMaskPrivate._cuteAt(address)
