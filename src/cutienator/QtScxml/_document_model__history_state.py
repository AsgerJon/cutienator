"""
DocumentModel::HistoryState binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/6.12.0/QtScxml/private/qscxmlcompiler_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means DocumentModel::HistoryState to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from . import DocumentModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class HistoryState(DocumentModel.AbstractState, DocumentModel.StateOrTransition):
  """
  The cute side of Qt's DocumentModel::HistoryState: a plain Python object
  standing in front of one C++ DocumentModel::HistoryState.

  It is built on the cute 'DocumentModel::AbstractState', as Qt's
  DocumentModel::HistoryState is built on Qt's DocumentModel::AbstractState,
  and has everything that class has. It is built on the cute
  'DocumentModel::StateOrTransition' as well, as Qt's
  DocumentModel::HistoryState is built on Qt's
  DocumentModel::StateOrTransition too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's DocumentModel::HistoryState that has a ritual and
  that Python can call so far, 4 names in all: 'add', 'defaultConfiguration',
  'asHistoryState', 'accept'. It can be made from Python, in 1 way; see
  '__init__'.

  What to expect
  --------------

  - The C++ DocumentModel::HistoryState is created at the first use, not by
    'DocumentModel::HistoryState(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DocumentModel::HistoryState.
  """

  #  The enums Qt writes inside DocumentModel::HistoryState, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Type(CuteNum):
    """
    The enum 'DocumentModel::HistoryState::Type' of Qt, with the 2 names Qt
    gives in it.
    """

    Deep = Kee[int](0)
    Shallow = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DocumentModel::HistoryState'

  #  Qt's DocumentModel::HistoryState is built on more than one class. The
  #  part of a C++ DocumentModel::HistoryState that belongs to a class after
  #  the first begins somewhere inside the object, and the ritual named for
  #  that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'DocumentModel::StateOrTransition':
          'ritual_cast_DocumentModel_HistoryState_DocumentModel_StateOrTransition',
  }

  #  A C++ DocumentModel::HistoryState Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_DocumentModel_HistoryState'

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

  @overload(WAIT['DocumentModel.XmlLocation'])
  def __init__(self, xmlLocation: DocumentModel.XmlLocation) -> None:
    """
    Notes what was given, for Qt's
    'DocumentModel::HistoryState::HistoryState(const XmlLocation
    &xmlLocation)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-historystate.html#HistoryState

    Parameters
    ----------

    xmlLocation : DocumentModel.XmlLocation
      Passed on as a value: Qt reads the C++ DocumentModel::XmlLocation,
      which stays Python's own.
    """
    #  DocumentModel::HistoryState::HistoryState(const XmlLocation
    #      &xmlLocation)
    self._noteCreation(HistoryState, lambda: Rituals.call(
        'ritual_ZN13DocumentModel12HistoryStateC1ERKNS_11XmlLocationE',
        self._valueOf(xmlLocation),
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

  @overload(DocumentModel.StateOrTransition)
  @overload(NoneType)
  def add(self, s: Optional[DocumentModel.StateOrTransition]) -> None:
    """
    Calls Qt's 'void DocumentModel::HistoryState::add(StateOrTransition *s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-historystate.html#add

    Parameters
    ----------

    s : Optional[DocumentModel.StateOrTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DocumentModel::HistoryState::add(StateOrTransition *s)
    ritual = (
        'ritual_ZN13DocumentModel12HistoryState3addEPNS_17StateOrTransition'
        'E')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13DocumentModel12HistoryState3addEPNS_17StateOrTran'
          'sitionE')
    self.uglySide.call(
        ritual, self._addressOf(s, 'DocumentModel::StateOrTransition'),
    )

  def defaultConfiguration(self) -> Optional[DocumentModel.Transition]:
    """
    Calls Qt's 'Transition
    *DocumentModel::HistoryState::defaultConfiguration()'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-historystate.html

    Returns
    -------

    Optional[DocumentModel.Transition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Transition *DocumentModel::HistoryState::defaultConfiguration()
    address = self.uglySide.call(
        'ritual_ZN13DocumentModel12HistoryState20defaultConfigurationEv',
    )
    return DocumentModel.Transition._cuteAt(address)

  def asHistoryState(self) -> Optional[HistoryState]:
    """
    Calls Qt's 'HistoryState *DocumentModel::HistoryState::asHistoryState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-historystate.html#asHistoryState

    Returns
    -------

    Optional[HistoryState]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  HistoryState *DocumentModel::HistoryState::asHistoryState()
    ritual = 'ritual_ZN13DocumentModel12HistoryState14asHistoryStateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13DocumentModel12HistoryState14asHistoryStateEv'
    address = self.uglySide.call(ritual)
    return HistoryState._cuteAt(address)

  @overload(WAIT['DocumentModel.NodeVisitor'])
  @overload(NoneType)
  def accept(self, visitor: Optional[DocumentModel.NodeVisitor]) -> None:
    """
    Calls Qt's 'void DocumentModel::HistoryState::accept(NodeVisitor
    *visitor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-historystate.html#accept

    Parameters
    ----------

    visitor : Optional[DocumentModel.NodeVisitor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DocumentModel::HistoryState::accept(NodeVisitor *visitor)
    ritual = (
        'ritual_ZN13DocumentModel12HistoryState6acceptEPNS_11NodeVisitorE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13DocumentModel12HistoryState6acceptEPNS_11NodeVisi'
          'torE')
    self.uglySide.call(ritual, self._addressOf(visitor))
