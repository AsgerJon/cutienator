"""
DocumentModel::Transition binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/6.12.0/QtScxml/private/qscxmlcompiler_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means DocumentModel::Transition to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
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


class Transition(DocumentModel.StateOrTransition):
  """
  The cute side of Qt's DocumentModel::Transition: a plain Python object
  standing in front of one C++ DocumentModel::Transition.

  It is built on the cute 'DocumentModel::StateOrTransition', as Qt's
  DocumentModel::Transition is built on Qt's
  DocumentModel::StateOrTransition, and has everything that class has.

  What exists
  -----------

  Every function of Qt's DocumentModel::Transition that has a ritual and that
  Python can call so far, 2 names in all: 'asTransition', 'accept'. It can be
  made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ DocumentModel::Transition is created at the first use, not by
    'DocumentModel::Transition(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DocumentModel::Transition.
  """

  #  The enums Qt writes inside DocumentModel::Transition, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class Type(CuteNum):
    """
    The enum 'DocumentModel::Transition::Type' of Qt, with the 3 names Qt
    gives in it.
    """

    Internal = Kee[int](0)
    External = Kee[int](1)
    Synthetic = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DocumentModel::Transition'

  #  A C++ DocumentModel::Transition Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_DocumentModel_Transition'

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
    'DocumentModel::Transition::Transition(const XmlLocation &xmlLocation)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-transition.html#Transition

    Parameters
    ----------

    xmlLocation : DocumentModel.XmlLocation
      Passed on as a value: Qt reads the C++ DocumentModel::XmlLocation,
      which stays Python's own.
    """
    #  DocumentModel::Transition::Transition(const XmlLocation &xmlLocation)
    self._noteCreation(Transition, lambda: Rituals.call(
        'ritual_ZN13DocumentModel10TransitionC1ERKNS_11XmlLocationE',
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

  def asTransition(self) -> Optional[Transition]:
    """
    Calls Qt's 'Transition *DocumentModel::Transition::asTransition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-transition.html#asTransition

    Returns
    -------

    Optional[Transition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Transition *DocumentModel::Transition::asTransition()
    ritual = 'ritual_ZN13DocumentModel10Transition12asTransitionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13DocumentModel10Transition12asTransitionEv'
    address = self.uglySide.call(ritual)
    return Transition._cuteAt(address)

  @overload(WAIT['DocumentModel.NodeVisitor'])
  @overload(NoneType)
  def accept(self, visitor: Optional[DocumentModel.NodeVisitor]) -> None:
    """
    Calls Qt's 'void DocumentModel::Transition::accept(NodeVisitor
    *visitor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-transition.html#accept

    Parameters
    ----------

    visitor : Optional[DocumentModel.NodeVisitor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DocumentModel::Transition::accept(NodeVisitor *visitor)
    ritual = 'ritual_ZN13DocumentModel10Transition6acceptEPNS_11NodeVisitorE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13DocumentModel10Transition6acceptEPNS_11NodeVisito'
          'rE')
    self.uglySide.call(ritual, self._addressOf(visitor))
