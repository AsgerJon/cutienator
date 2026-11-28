"""
DocumentModel::StateContainer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/6.12.0/QtScxml/private/qscxmlcompiler_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means DocumentModel::StateContainer to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import DocumentModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class StateContainer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DocumentModel::StateContainer: a plain Python object
  standing in front of one C++ DocumentModel::StateContainer.

  What exists
  -----------

  Every function of Qt's DocumentModel::StateContainer that has a ritual and
  that Python can call so far, 4 names in all: 'add', 'asAbstractState',
  'asState', 'asScxml'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DocumentModel::StateContainer::~StateContainer()': the destructor:
    Python never removes a C++ DocumentModel::StateContainer.

  What to expect
  --------------

  - The C++ DocumentModel::StateContainer is created at the first use, not by
    'DocumentModel::StateContainer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DocumentModel::StateContainer.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DocumentModel::StateContainer'

  #  A C++ DocumentModel::StateContainer Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_DocumentModel_StateContainer'

  #  The functions Qt calls itself that DocumentModel::StateContainer is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'add': (
          ('_ZN13DocumentModel14StateContainer3addEPNS_17StateOrTransitionE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtScxml:DocumentModel.StateOrTransition'),
           )),
      ),
      'asAbstractState': (
          ('_ZN13DocumentModel14StateContainer15asAbstractStateEv',
           ('address', 'address', 'QtScxml:DocumentModel.AbstractState'),
           ()),
      ),
      'asState': (
          ('_ZN13DocumentModel14StateContainer7asStateEv',
           ('address', 'address', 'QtScxml:DocumentModel.State'),
           ()),
      ),
      'asScxml': (
          ('_ZN13DocumentModel14StateContainer7asScxmlEv',
           ('address', 'address', 'QtScxml:DocumentModel.Scxml'),
           ()),
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
    'DocumentModel::StateContainer::StateContainer()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-statecontainer.html#StateContainer
    """
    #  DocumentModel::StateContainer::StateContainer()
    self._noteCreation(StateContainer, lambda: Rituals.call(
        'ritual_ZN13DocumentModel14StateContainerC1Ev',
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

  @overload(WAIT['DocumentModel.StateOrTransition'])
  @overload(NoneType)
  def add(self, s: Optional[DocumentModel.StateOrTransition]) -> None:
    """
    Calls Qt's 'void DocumentModel::StateContainer::add(StateOrTransition
    *s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-statecontainer.html#add

    Parameters
    ----------

    s : Optional[DocumentModel.StateOrTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DocumentModel::StateContainer::add(StateOrTransition *s)
    self.uglySide.call(
        'ritual_ZN13DocumentModel14StateContainer3addEPNS_17StateOrTransiti'
        'onE',
        self._addressOf(s, 'DocumentModel::StateOrTransition'),
    )

  def asAbstractState(self) -> Optional[DocumentModel.AbstractState]:
    """
    Calls Qt's 'AbstractState
    *DocumentModel::StateContainer::asAbstractState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-statecontainer.html#asAbstractState

    Returns
    -------

    Optional[DocumentModel.AbstractState]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  AbstractState *DocumentModel::StateContainer::asAbstractState()
    ritual = 'ritual_ZN13DocumentModel14StateContainer15asAbstractStateEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13DocumentModel14StateContainer15asAbstractStateEv')
    address = self.uglySide.call(ritual)
    return DocumentModel.AbstractState._cuteAt(address)

  def asState(self) -> Optional[DocumentModel.State]:
    """
    Calls Qt's 'State *DocumentModel::StateContainer::asState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-statecontainer.html#asState

    Returns
    -------

    Optional[DocumentModel.State]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  State *DocumentModel::StateContainer::asState()
    ritual = 'ritual_ZN13DocumentModel14StateContainer7asStateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13DocumentModel14StateContainer7asStateEv'
    address = self.uglySide.call(ritual)
    return DocumentModel.State._cuteAt(address)

  def asScxml(self) -> Optional[DocumentModel.Scxml]:
    """
    Calls Qt's 'Scxml *DocumentModel::StateContainer::asScxml()'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-statecontainer.html#asScxml

    Returns
    -------

    Optional[DocumentModel.Scxml]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Scxml *DocumentModel::StateContainer::asScxml()
    ritual = 'ritual_ZN13DocumentModel14StateContainer7asScxmlEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13DocumentModel14StateContainer7asScxmlEv'
    address = self.uglySide.call(ritual)
    return DocumentModel.Scxml._cuteAt(address)
