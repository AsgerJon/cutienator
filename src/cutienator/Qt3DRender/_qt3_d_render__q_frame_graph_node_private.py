"""
Qt3DRender::QFrameGraphNodePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qframegraphnode_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::QFrameGraphNodePrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFrameGraphNodePrivate(Qt3DCore.QNodePrivate):
  """
  The cute side of Qt's Qt3DRender::QFrameGraphNodePrivate: a plain Python
  object standing in front of one C++ Qt3DRender::QFrameGraphNodePrivate.

  It is built on the cute 'Qt3DCore::QNodePrivate', as Qt's
  Qt3DRender::QFrameGraphNodePrivate is built on Qt's Qt3DCore::QNodePrivate,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QFrameGraphNodePrivate that has a ritual
  and that Python can call so far, 5 names in all: 'get', 'dumpFrameGraph',
  'dumpFrameGraphPaths', 'dumpFrameGraphFilterState', 'q_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QList<QFrameGraphNode *>
    Qt3DRender::QFrameGraphNodePrivate::childFrameGraphNodes() const': gives
    a type Python has no way to take yet.
  - Qt's 'const QFrameGraphNodePrivate
    *Qt3DRender::QFrameGraphNodePrivate::get(const QFrameGraphNode *node)':
    takes in Python what 'QFrameGraphNodePrivate
    *Qt3DRender::QFrameGraphNodePrivate::get(QFrameGraphNode *node)' takes.
  - Qt's 'const QFrameGraphNode *Qt3DRender::QFrameGraphNodePrivate::q_func()
    const': takes in Python what 'QFrameGraphNode
    *Qt3DRender::QFrameGraphNodePrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DRender::QFrameGraphNodePrivate is created at the first use,
    not by 'Qt3DRender::QFrameGraphNodePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QFrameGraphNodePrivate.
  - Each name of Qt's Qt3DRender::QFrameGraphNodePrivate that has no cute
    function yet, 'childFrameGraphNodes', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['Qt3DRender.QFrameGraphNode'])
  @overload(NoneType)
  def get(
      node: Optional[Qt3DRender.QFrameGraphNode],
  ) -> Optional[QFrameGraphNodePrivate]:
    """
    Calls Qt's 'QFrameGraphNodePrivate
    *Qt3DRender::QFrameGraphNodePrivate::get(QFrameGraphNode *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qframegraphnodeprivate.html#get

    Parameters
    ----------

    node : Optional[Qt3DRender.QFrameGraphNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QFrameGraphNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFrameGraphNodePrivate
    #      *Qt3DRender::QFrameGraphNodePrivate::get(QFrameGraphNode *node)
    address = Rituals.call(
        'ritual_ZN10Qt3DRender22QFrameGraphNodePrivate3getEPNS_15QFrameGrap'
        'hNodeE',
        CuteMixin._addressOf(node),
    )
    return QFrameGraphNodePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QFrameGraphNodePrivate'

  #  A C++ Qt3DRender::QFrameGraphNodePrivate Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QFrameGraphNodePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def dumpFrameGraph(self) -> str:
    """
    Calls Qt's 'QString Qt3DRender::QFrameGraphNodePrivate::dumpFrameGraph()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qframegraphnodeprivate.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DRender::QFrameGraphNodePrivate::dumpFrameGraph() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender22QFrameGraphNodePrivate14dumpFrameGraphEv',
    )

  def dumpFrameGraphPaths(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    Qt3DRender::QFrameGraphNodePrivate::dumpFrameGraphPaths() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qframegraphnodeprivate.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DRender::QFrameGraphNodePrivate::dumpFrameGraphPaths()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender22QFrameGraphNodePrivate19dumpFrameGraphPath'
        'sEv',
    )
    return QStringList._cuteOwning(address)

  def dumpFrameGraphFilterState(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    Qt3DRender::QFrameGraphNodePrivate::dumpFrameGraphFilterState() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qframegraphnodeprivate.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList
    #      Qt3DRender::QFrameGraphNodePrivate::dumpFrameGraphFilterState()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender22QFrameGraphNodePrivate25dumpFrameGraphFilt'
        'erStateEv',
    )
    return QStringList._cuteOwning(address)

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
    'Qt3DRender::QFrameGraphNodePrivate::QFrameGraphNodePrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qframegraphnodeprivate.html
    """
    #  Qt3DRender::QFrameGraphNodePrivate::QFrameGraphNodePrivate()
    self._noteCreation(QFrameGraphNodePrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender22QFrameGraphNodePrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DRender.QFrameGraphNode]:
    """
    Calls Qt's 'QFrameGraphNode
    *Qt3DRender::QFrameGraphNodePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qframegraphnodeprivate.html#q_func

    Returns
    -------

    Optional[Qt3DRender.QFrameGraphNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFrameGraphNode *Qt3DRender::QFrameGraphNodePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender22QFrameGraphNodePrivate6q_funcEv',
    )
    return Qt3DRender.QFrameGraphNode._cuteAt(address)

  @staticmethod
  def childFrameGraphNodes(*__, **_) -> Never:
    """
    Qt's 'QList<QFrameGraphNode *>
    Qt3DRender::QFrameGraphNodePrivate::childFrameGraphNodes() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QFrameGraphNodePrivate.childFrameGraphNodes' has no "
        "cute function yet. Qt's 'QList<QFrameGraphNode *> "
        "Qt3DRender::QFrameGraphNodePrivate::childFrameGraphNodes() const': "
        "gives a type Python has no way to take yet.")
