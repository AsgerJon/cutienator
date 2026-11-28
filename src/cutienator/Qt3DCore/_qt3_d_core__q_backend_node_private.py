"""
Qt3DCore::QBackendNodePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qbackendnode_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DCore::QBackendNodePrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBackendNodePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DCore::QBackendNodePrivate: a plain Python object
  standing in front of one C++ Qt3DCore::QBackendNodePrivate.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QBackendNodePrivate that has a ritual and
  that Python can call so far, 7 names in all: 'setEnabled', 'get', 'q_func',
  'addedToEntity', 'removedFromEntity', 'componentAdded', 'componentRemoved'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DCore::QBackendNodePrivate::~QBackendNodePrivate()': the
    destructor: Python never removes a C++ Qt3DCore::QBackendNodePrivate.
  - Qt's 'const QBackendNode *Qt3DCore::QBackendNodePrivate::q_func() const':
    takes in Python what 'QBackendNode
    *Qt3DCore::QBackendNodePrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ Qt3DCore::QBackendNodePrivate is created at the first use, not by
    'Qt3DCore::QBackendNodePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QBackendNodePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['Qt3DCore.QBackendNode'])
  @overload(NoneType)
  def get(
      n: Optional[Qt3DCore.QBackendNode],
  ) -> Optional[QBackendNodePrivate]:
    """
    Calls Qt's 'QBackendNodePrivate
    *Qt3DCore::QBackendNodePrivate::get(QBackendNode *n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qbackendnodeprivate.html#get

    Parameters
    ----------

    n : Optional[Qt3DCore.QBackendNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QBackendNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBackendNodePrivate *Qt3DCore::QBackendNodePrivate::get(QBackendNode
    #      *n)
    address = Rituals.call(
        'ritual_ZN8Qt3DCore19QBackendNodePrivate3getEPNS_12QBackendNodeE',
        CuteMixin._addressOf(n),
    )
    return QBackendNodePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QBackendNodePrivate'

  #  A C++ Qt3DCore::QBackendNodePrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QBackendNodePrivate'

  #  The functions Qt calls itself that Qt3DCore::QBackendNodePrivate is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'addedToEntity': (
          ('_ZN8Qt3DCore19QBackendNodePrivate13addedToEntityEPNS_5QNodeE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'Qt3DCore:Qt3DCore.QNode'),
           )),
      ),
      'removedFromEntity': (
          ('_ZN8Qt3DCore19QBackendNodePrivate17removedFromEntityEPNS_5QNode'
           'E',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'Qt3DCore:Qt3DCore.QNode'),
           )),
      ),
      'componentAdded': (
          ('_ZN8Qt3DCore19QBackendNodePrivate14componentAddedEPNS_5QNodeE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'Qt3DCore:Qt3DCore.QNode'),
           )),
      ),
      'componentRemoved': (
          ('_ZN8Qt3DCore19QBackendNodePrivate16componentRemovedEPNS_5QNodeE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'Qt3DCore:Qt3DCore.QNode'),
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void Qt3DCore::QBackendNodePrivate::setEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qbackendnodeprivate.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Qt3DCore::QBackendNodePrivate::setEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore19QBackendNodePrivate10setEnabledEb', enabled,
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

  @overload(Qt3DCore.QBackendNode.Mode)
  def __init__(self, mode: Qt3DCore.QBackendNode.Mode) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::QBackendNodePrivate::QBackendNodePrivate(QBackendNode::Mode
    mode)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qbackendnodeprivate.html

    Parameters
    ----------

    mode : Qt3DCore.QBackendNode.Mode
      Passed on as its number.
    """
    #  Qt3DCore::QBackendNodePrivate::QBackendNodePrivate(QBackendNode::Mode
    #      mode)
    self._noteCreation(QBackendNodePrivate, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore19QBackendNodePrivateC1ENS_12QBackendNode4ModeE',
        mode.value,
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

  def q_func(self) -> Optional[Qt3DCore.QBackendNode]:
    """
    Calls Qt's 'QBackendNode *Qt3DCore::QBackendNodePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qbackendnodeprivate.html#q_func

    Returns
    -------

    Optional[Qt3DCore.QBackendNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBackendNode *Qt3DCore::QBackendNodePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore19QBackendNodePrivate6q_funcEv',
    )
    return Qt3DCore.QBackendNode._cuteAt(address)

  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def addedToEntity(self, frontend: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QBackendNodePrivate::addedToEntity(QNode
    *frontend)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qbackendnodeprivate.html#addedToEntity

    Parameters
    ----------

    frontend : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QBackendNodePrivate::addedToEntity(QNode *frontend)
    ritual = (
        'ritual_ZN8Qt3DCore19QBackendNodePrivate13addedToEntityEPNS_5QNodeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8Qt3DCore19QBackendNodePrivate13addedToEntityEPNS_5'
          'QNodeE')
    self.uglySide.call(ritual, self._addressOf(frontend))

  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def removedFromEntity(self, frontend: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QBackendNodePrivate::removedFromEntity(QNode
    *frontend)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qbackendnodeprivate.html

    Parameters
    ----------

    frontend : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QBackendNodePrivate::removedFromEntity(QNode *frontend)
    ritual = (
        'ritual_ZN8Qt3DCore19QBackendNodePrivate17removedFromEntityEPNS_5QN'
        'odeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8Qt3DCore19QBackendNodePrivate17removedFromEntityEP'
          'NS_5QNodeE')
    self.uglySide.call(ritual, self._addressOf(frontend))

  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def componentAdded(self, frontend: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QBackendNodePrivate::componentAdded(QNode
    *frontend)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qbackendnodeprivate.html#componentAdded

    Parameters
    ----------

    frontend : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QBackendNodePrivate::componentAdded(QNode *frontend)
    ritual = (
        'ritual_ZN8Qt3DCore19QBackendNodePrivate14componentAddedEPNS_5QNode'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8Qt3DCore19QBackendNodePrivate14componentAddedEPNS_'
          '5QNodeE')
    self.uglySide.call(ritual, self._addressOf(frontend))

  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def componentRemoved(self, frontend: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QBackendNodePrivate::componentRemoved(QNode
    *frontend)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qbackendnodeprivate.html#componentRemoved

    Parameters
    ----------

    frontend : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QBackendNodePrivate::componentRemoved(QNode *frontend)
    ritual = (
        'ritual_ZN8Qt3DCore19QBackendNodePrivate16componentRemovedEPNS_5QNo'
        'deE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN8Qt3DCore19QBackendNodePrivate16componentRemovedEPN'
          'S_5QNodeE')
    self.uglySide.call(ritual, self._addressOf(frontend))
