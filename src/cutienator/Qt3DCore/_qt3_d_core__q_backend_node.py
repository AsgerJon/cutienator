"""
Qt3DCore::QBackendNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/qbackendnode.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBackendNode(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DCore::QBackendNode: a plain Python object
  standing in front of one C++ Qt3DCore::QBackendNode.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QBackendNode that has a ritual and that
  Python can call so far, 7 names in all: 'peerId', 'setEnabled',
  'isEnabled', 'mode', 'syncFromFrontEnd', 'd_func', 'setPeerId'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DCore::QBackendNode::~QBackendNode()': the destructor: Python
    never removes a C++ Qt3DCore::QBackendNode.
  - Qt's 'const QBackendNodePrivate *Qt3DCore::QBackendNode::d_func() const':
    takes in Python what 'QBackendNodePrivate
    *Qt3DCore::QBackendNode::d_func()' takes.
  - Qt's 'Qt3DCore::QBackendNode::QBackendNode(QBackendNodePrivate &dd)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ Qt3DCore::QBackendNode is created at the first use, not by
    'Qt3DCore::QBackendNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QBackendNode.
  """

  #  The enums Qt writes inside Qt3DCore::QBackendNode, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Mode(CuteNum):
    """
    The enum 'Qt3DCore::QBackendNode::Mode' of Qt, with the 2 names Qt gives
    in it.
    """

    ReadOnly = Kee[int](0)
    ReadWrite = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QBackendNode'

  #  A C++ Qt3DCore::QBackendNode Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QBackendNode'

  #  The functions Qt calls itself that Qt3DCore::QBackendNode is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'syncFromFrontEnd': (
          ('_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'Qt3DCore:Qt3DCore.QNode'),
               ('bool', 'number', ''),
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

  def peerId(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'QNodeId Qt3DCore::QBackendNode::peerId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qbackendnode.html#peerId

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  QNodeId Qt3DCore::QBackendNode::peerId() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore12QBackendNode6peerIdEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::QBackendNode::isEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qbackendnode.html#isEnabled
    """
    #  bool Qt3DCore::QBackendNode::isEnabled() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore12QBackendNode9isEnabledEv',
    )

  def mode(self) -> Mode:
    """
    Calls Qt's 'Mode Qt3DCore::QBackendNode::mode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qbackendnode.html#mode

    Returns
    -------

    Mode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Mode(number)' gives.
    """
    #  Mode Qt3DCore::QBackendNode::mode() const
    return QBackendNode.Mode(self.uglySide.call(
        'ritual_ZNK8Qt3DCore12QBackendNode4modeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void Qt3DCore::QBackendNode::setEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qbackendnode.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Qt3DCore::QBackendNode::setEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore12QBackendNode10setEnabledEb', enabled,
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def setPeerId(self, id: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void Qt3DCore::QBackendNode::setPeerId(QNodeId id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qbackendnode.html#setPeerId

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DCore::QBackendNode::setPeerId(QNodeId id)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore12QBackendNode9setPeerIdENS_7QNodeIdE',
        self._valueOf(id),
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
  @overload(Mode)
  def __init__(self, mode: Mode = Mode.ReadOnly) -> None:
    """
    Notes what was given, for Qt's 'Qt3DCore::QBackendNode::QBackendNode(Mode
    mode)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qbackendnode.html#QBackendNode

    Parameters
    ----------

    mode : Mode
      Passed on as its number. May be left out, as in Qt: it is then
      Mode.ReadOnly.
    """
    #  Qt3DCore::QBackendNode::QBackendNode(Mode mode)
    self._noteCreation(QBackendNode, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore12QBackendNodeC1ENS0_4ModeE', mode.value,
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

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DCore::QBackendNode::syncFromFrontEnd(const QNode
    *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qbackendnode.html#syncFromFrontEnd

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DCore::QBackendNode::syncFromFrontEnd(const QNode *frontEnd,
    #      bool firstTime)
    ritual = (
        'ritual_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNo'
          'deEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  def d_func(self) -> Optional[Qt3DCore.QBackendNodePrivate]:
    """
    Calls Qt's 'QBackendNodePrivate *Qt3DCore::QBackendNode::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qbackendnode.html#d_func

    Returns
    -------

    Optional[Qt3DCore.QBackendNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBackendNodePrivate *Qt3DCore::QBackendNode::d_func()
    address = self.uglySide.call('ritual_ZN8Qt3DCore12QBackendNode6d_funcEv')
    return Qt3DCore.QBackendNodePrivate._cuteAt(address)
