"""
DocumentModel::Node binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/6.12.0/QtScxml/private/qscxmlcompiler_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means DocumentModel::Node to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
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


class Node(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DocumentModel::Node: a plain Python object standing
  in front of one C++ DocumentModel::Node.

  What exists
  -----------

  Every function of Qt's DocumentModel::Node that has a ritual and that
  Python can call so far, 10 names in all: 'accept', 'asIf', 'asSend',
  'asInvoke', 'asScript', 'asState', 'asTransition', 'asHistoryState',
  'asScxml', 'asAbstractState'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DocumentModel::Node::~Node()': the destructor: Python never removes
    a C++ DocumentModel::Node.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ DocumentModel::Node is created at the first use, not by
    'DocumentModel::Node(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DocumentModel::Node.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DocumentModel::Node'

  #  A C++ DocumentModel::Node Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_DocumentModel_Node'

  #  The functions Qt calls itself that DocumentModel::Node is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'accept': (
          ('_ZN13DocumentModel4Node6acceptEPNS_11NodeVisitorE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtScxml:DocumentModel.NodeVisitor'),
           )),
      ),
      'asIf': (
          ('_ZN13DocumentModel4Node4asIfEv',
           ('address', 'address', 'QtScxml:DocumentModel.If'),
           ()),
      ),
      'asSend': (
          ('_ZN13DocumentModel4Node6asSendEv',
           ('address', 'address', 'QtScxml:DocumentModel.Send'),
           ()),
      ),
      'asInvoke': (
          ('_ZN13DocumentModel4Node8asInvokeEv',
           ('address', 'address', 'QtScxml:DocumentModel.Invoke'),
           ()),
      ),
      'asScript': (
          ('_ZN13DocumentModel4Node8asScriptEv',
           ('address', 'address', 'QtScxml:DocumentModel.Script'),
           ()),
      ),
      'asState': (
          ('_ZN13DocumentModel4Node7asStateEv',
           ('address', 'address', 'QtScxml:DocumentModel.State'),
           ()),
      ),
      'asTransition': (
          ('_ZN13DocumentModel4Node12asTransitionEv',
           ('address', 'address', 'QtScxml:DocumentModel.Transition'),
           ()),
      ),
      'asHistoryState': (
          ('_ZN13DocumentModel4Node14asHistoryStateEv',
           ('address', 'address', 'QtScxml:DocumentModel.HistoryState'),
           ()),
      ),
      'asScxml': (
          ('_ZN13DocumentModel4Node7asScxmlEv',
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

  @overload(WAIT['DocumentModel.XmlLocation'])
  def __init__(self, theLocation: DocumentModel.XmlLocation) -> None:
    """
    Notes what was given, for Qt's 'DocumentModel::Node::Node(const
    XmlLocation &theLocation)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/documentmodel-node.html#Node

    Parameters
    ----------

    theLocation : DocumentModel.XmlLocation
      Passed on as a value: Qt reads the C++ DocumentModel::XmlLocation,
      which stays Python's own.
    """
    #  DocumentModel::Node::Node(const XmlLocation &theLocation)
    self._noteCreation(Node, lambda: Rituals.call(
        'ritual_ZN13DocumentModel4NodeC1ERKNS_11XmlLocationE',
        self._valueOf(theLocation),
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

  @overload(WAIT['DocumentModel.NodeVisitor'])
  @overload(NoneType)
  def accept(self, visitor: Optional[DocumentModel.NodeVisitor]) -> None:
    """
    Calls Qt's 'void DocumentModel::Node::accept(NodeVisitor *visitor)'.

    Qt's own words: https://doc.qt.io/qt-6/documentmodel-node.html#accept

    Parameters
    ----------

    visitor : Optional[DocumentModel.NodeVisitor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DocumentModel::Node::accept(NodeVisitor *visitor)
    self._callAs(
        'DocumentModel::Node',
        'ritual_ZN13DocumentModel4Node6acceptEPNS_11NodeVisitorE',
        self._addressOf(visitor),
    )

  def asIf(self) -> Optional[DocumentModel.If]:
    """
    Calls Qt's 'If *DocumentModel::Node::asIf()'.

    Qt's own words: https://doc.qt.io/qt-6/documentmodel-node.html#asIf

    Returns
    -------

    Optional[DocumentModel.If]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  If *DocumentModel::Node::asIf()
    ritual = 'ritual_ZN13DocumentModel4Node4asIfEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13DocumentModel4Node4asIfEv'
    address = self._callAs('DocumentModel::Node', ritual)
    return DocumentModel.If._cuteAt(address)

  def asSend(self) -> Optional[DocumentModel.Send]:
    """
    Calls Qt's 'Send *DocumentModel::Node::asSend()'.

    Qt's own words: https://doc.qt.io/qt-6/documentmodel-node.html#asSend

    Returns
    -------

    Optional[DocumentModel.Send]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Send *DocumentModel::Node::asSend()
    ritual = 'ritual_ZN13DocumentModel4Node6asSendEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13DocumentModel4Node6asSendEv'
    address = self._callAs('DocumentModel::Node', ritual)
    return DocumentModel.Send._cuteAt(address)

  def asInvoke(self) -> Optional[DocumentModel.Invoke]:
    """
    Calls Qt's 'Invoke *DocumentModel::Node::asInvoke()'.

    Qt's own words: https://doc.qt.io/qt-6/documentmodel-node.html#asInvoke

    Returns
    -------

    Optional[DocumentModel.Invoke]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Invoke *DocumentModel::Node::asInvoke()
    ritual = 'ritual_ZN13DocumentModel4Node8asInvokeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13DocumentModel4Node8asInvokeEv'
    address = self._callAs('DocumentModel::Node', ritual)
    return DocumentModel.Invoke._cuteAt(address)

  def asScript(self) -> Optional[DocumentModel.Script]:
    """
    Calls Qt's 'Script *DocumentModel::Node::asScript()'.

    Qt's own words: https://doc.qt.io/qt-6/documentmodel-node.html#asScript

    Returns
    -------

    Optional[DocumentModel.Script]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Script *DocumentModel::Node::asScript()
    ritual = 'ritual_ZN13DocumentModel4Node8asScriptEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13DocumentModel4Node8asScriptEv'
    address = self._callAs('DocumentModel::Node', ritual)
    return DocumentModel.Script._cuteAt(address)

  def asState(self) -> Optional[DocumentModel.State]:
    """
    Calls Qt's 'State *DocumentModel::Node::asState()'.

    Qt's own words: https://doc.qt.io/qt-6/documentmodel-node.html#asState

    Returns
    -------

    Optional[DocumentModel.State]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  State *DocumentModel::Node::asState()
    ritual = 'ritual_ZN13DocumentModel4Node7asStateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13DocumentModel4Node7asStateEv'
    address = self._callAs('DocumentModel::Node', ritual)
    return DocumentModel.State._cuteAt(address)

  def asTransition(self) -> Optional[DocumentModel.Transition]:
    """
    Calls Qt's 'Transition *DocumentModel::Node::asTransition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-node.html#asTransition

    Returns
    -------

    Optional[DocumentModel.Transition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Transition *DocumentModel::Node::asTransition()
    ritual = 'ritual_ZN13DocumentModel4Node12asTransitionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13DocumentModel4Node12asTransitionEv'
    address = self._callAs('DocumentModel::Node', ritual)
    return DocumentModel.Transition._cuteAt(address)

  def asHistoryState(self) -> Optional[DocumentModel.HistoryState]:
    """
    Calls Qt's 'HistoryState *DocumentModel::Node::asHistoryState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-node.html#asHistoryState

    Returns
    -------

    Optional[DocumentModel.HistoryState]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  HistoryState *DocumentModel::Node::asHistoryState()
    ritual = 'ritual_ZN13DocumentModel4Node14asHistoryStateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13DocumentModel4Node14asHistoryStateEv'
    address = self._callAs('DocumentModel::Node', ritual)
    return DocumentModel.HistoryState._cuteAt(address)

  def asScxml(self) -> Optional[DocumentModel.Scxml]:
    """
    Calls Qt's 'Scxml *DocumentModel::Node::asScxml()'.

    Qt's own words: https://doc.qt.io/qt-6/documentmodel-node.html#asScxml

    Returns
    -------

    Optional[DocumentModel.Scxml]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Scxml *DocumentModel::Node::asScxml()
    ritual = 'ritual_ZN13DocumentModel4Node7asScxmlEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13DocumentModel4Node7asScxmlEv'
    address = self._callAs('DocumentModel::Node', ritual)
    return DocumentModel.Scxml._cuteAt(address)

  def asAbstractState(self) -> Optional[DocumentModel.AbstractState]:
    """
    Calls Qt's 'AbstractState *DocumentModel::Node::asAbstractState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-node.html#asAbstractState

    Returns
    -------

    Optional[DocumentModel.AbstractState]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  AbstractState *DocumentModel::Node::asAbstractState()
    address = self._callAs(
        'DocumentModel::Node',
        'ritual_ZN13DocumentModel4Node15asAbstractStateEv',
    )
    return DocumentModel.AbstractState._cuteAt(address)
