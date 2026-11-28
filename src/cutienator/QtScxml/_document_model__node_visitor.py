"""
DocumentModel::NodeVisitor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/6.12.0/QtScxml/private/qscxmlcompiler_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means DocumentModel::NodeVisitor to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import DocumentModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class NodeVisitor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DocumentModel::NodeVisitor: a plain Python object
  standing in front of one C++ DocumentModel::NodeVisitor.

  C++ hands a DocumentModel::NodeVisitor around as a copy, so every C++
  DocumentModel::NodeVisitor behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's DocumentModel::NodeVisitor that has a ritual and
  that Python can call so far, 2 names in all: 'visit', 'endVisit'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DocumentModel::NodeVisitor::~NodeVisitor()': the destructor: Python
    removes its C++ DocumentModel::NodeVisitor by it, and has no other use
    for it.
  - Qt's 'void DocumentModel::NodeVisitor::visit(InstructionSequence
    *sequence)': names 'DocumentModel::InstructionSequence', which has no
    cute class yet.
  - Qt's 'void DocumentModel::NodeVisitor::visit(const QList<DataElement *>
    &dataElements)': takes a type Python has no way to hand over yet.
  - Qt's 'void DocumentModel::NodeVisitor::visit(const
    QList<StateOrTransition *> &children)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void DocumentModel::NodeVisitor::visit(const InstructionSequences
    &sequences)': takes a type Python has no way to hand over yet.
  - Qt's 'void DocumentModel::NodeVisitor::visit(const QList<Param *>
    &params)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ DocumentModel::NodeVisitor is created at the first use, not by
    'DocumentModel::NodeVisitor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a DocumentModel::NodeVisitor back gives a copy the
    ritual made for Python, in a new cute DocumentModel::NodeVisitor.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DocumentModel::NodeVisitor'

  #  A C++ DocumentModel::NodeVisitor Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_DocumentModel_NodeVisitor'

  #  The functions Qt calls itself that DocumentModel::NodeVisitor is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'visit': (
          ('_ZN13DocumentModel11NodeVisitor5visitEPNS_11DataElementE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtScxml:DocumentModel.DataElement'),
           )),
          ('_ZN13DocumentModel11NodeVisitor5visitEPNS_5ParamE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtScxml:DocumentModel.Param'),
           )),
          ('_ZN13DocumentModel11NodeVisitor5visitEPNS_8DoneDataE',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtScxml:DocumentModel.DoneData'),
           )),
          ('_ZN13DocumentModel11NodeVisitor5visitEPNS_4SendE',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtScxml:DocumentModel.Send'),
           )),
          ('_ZN13DocumentModel11NodeVisitor5visitEPNS_6InvokeE',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtScxml:DocumentModel.Invoke'),
           )),
          ('_ZN13DocumentModel11NodeVisitor5visitEPNS_5RaiseE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtScxml:DocumentModel.Raise'),
           )),
          ('_ZN13DocumentModel11NodeVisitor5visitEPNS_3LogE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtScxml:DocumentModel.Log'),
           )),
          ('_ZN13DocumentModel11NodeVisitor5visitEPNS_6ScriptE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtScxml:DocumentModel.Script'),
           )),
          ('_ZN13DocumentModel11NodeVisitor5visitEPNS_6AssignE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtScxml:DocumentModel.Assign'),
           )),
          ('_ZN13DocumentModel11NodeVisitor5visitEPNS_2IfE',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtScxml:DocumentModel.If'),
           )),
          ('_ZN13DocumentModel11NodeVisitor5visitEPNS_7ForeachE',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtScxml:DocumentModel.Foreach'),
           )),
          ('_ZN13DocumentModel11NodeVisitor5visitEPNS_6CancelE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtScxml:DocumentModel.Cancel'),
           )),
          ('_ZN13DocumentModel11NodeVisitor5visitEPNS_5StateE',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtScxml:DocumentModel.State'),
           )),
          ('_ZN13DocumentModel11NodeVisitor5visitEPNS_10TransitionE',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtScxml:DocumentModel.Transition'),
           )),
          ('_ZN13DocumentModel11NodeVisitor5visitEPNS_12HistoryStateE',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtScxml:DocumentModel.HistoryState'),
           )),
          ('_ZN13DocumentModel11NodeVisitor5visitEPNS_5ScxmlE',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtScxml:DocumentModel.Scxml'),
           )),
      ),
      'endVisit': (
          ('_ZN13DocumentModel11NodeVisitor8endVisitEPNS_8DoneDataE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtScxml:DocumentModel.DoneData'),
           )),
          ('_ZN13DocumentModel11NodeVisitor8endVisitEPNS_4SendE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtScxml:DocumentModel.Send'),
           )),
          ('_ZN13DocumentModel11NodeVisitor8endVisitEPNS_6InvokeE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtScxml:DocumentModel.Invoke'),
           )),
          ('_ZN13DocumentModel11NodeVisitor8endVisitEPNS_2IfE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtScxml:DocumentModel.If'),
           )),
          ('_ZN13DocumentModel11NodeVisitor8endVisitEPNS_7ForeachE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtScxml:DocumentModel.Foreach'),
           )),
          ('_ZN13DocumentModel11NodeVisitor8endVisitEPNS_5StateE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtScxml:DocumentModel.State'),
           )),
          ('_ZN13DocumentModel11NodeVisitor8endVisitEPNS_10TransitionE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtScxml:DocumentModel.Transition'),
           )),
          ('_ZN13DocumentModel11NodeVisitor8endVisitEPNS_12HistoryStateE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtScxml:DocumentModel.HistoryState'),
           )),
          ('_ZN13DocumentModel11NodeVisitor8endVisitEPNS_5ScxmlE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtScxml:DocumentModel.Scxml'),
           )),
      ),
  }

  #  Qt's '~DocumentModel::NodeVisitor()'. Naming it makes this a value
  #  class: Python owns every C++ DocumentModel::NodeVisitor behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN13DocumentModel11NodeVisitorD1Ev'

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

  @overload(WAIT['DocumentModel.DataElement'])
  @overload(NoneType)
  def visit(self, a0: Optional[DocumentModel.DataElement]) -> None:
    """
    Calls Qt's 'void DocumentModel::NodeVisitor::visit(DataElement *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-nodevisitor.html#visit

    Parameters
    ----------

    a0 : Optional[DocumentModel.DataElement]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DocumentModel::NodeVisitor::visit(DataElement *a0)
    ritual = 'ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_11DataElementE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_11DataElemen'
          'tE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['DocumentModel.Param'])
  def visit(self, a0: Optional[DocumentModel.Param]) -> None:
    """
    Calls Qt's 'void DocumentModel::NodeVisitor::visit(Param *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-nodevisitor.html#visit

    Parameters
    ----------

    a0 : Optional[DocumentModel.Param]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DocumentModel::NodeVisitor::visit(Param *a0)
    ritual = 'ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_5ParamE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_5ParamE'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['DocumentModel.DoneData'])
  def visit(self, a0: Optional[DocumentModel.DoneData]) -> bool:
    """
    Calls Qt's 'bool DocumentModel::NodeVisitor::visit(DoneData *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-nodevisitor.html#visit

    Parameters
    ----------

    a0 : Optional[DocumentModel.DoneData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool DocumentModel::NodeVisitor::visit(DoneData *a0)
    ritual = 'ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_8DoneDataE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_8DoneDataE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['DocumentModel.Send'])
  def visit(self, a0: Optional[DocumentModel.Send]) -> bool:
    """
    Calls Qt's 'bool DocumentModel::NodeVisitor::visit(Send *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-nodevisitor.html#visit

    Parameters
    ----------

    a0 : Optional[DocumentModel.Send]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool DocumentModel::NodeVisitor::visit(Send *a0)
    ritual = 'ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_4SendE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_4SendE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['DocumentModel.Invoke'])
  def visit(self, a0: Optional[DocumentModel.Invoke]) -> bool:
    """
    Calls Qt's 'bool DocumentModel::NodeVisitor::visit(Invoke *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-nodevisitor.html#visit

    Parameters
    ----------

    a0 : Optional[DocumentModel.Invoke]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool DocumentModel::NodeVisitor::visit(Invoke *a0)
    ritual = 'ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_6InvokeE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_6InvokeE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['DocumentModel.Raise'])
  def visit(self, a0: Optional[DocumentModel.Raise]) -> None:
    """
    Calls Qt's 'void DocumentModel::NodeVisitor::visit(Raise *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-nodevisitor.html#visit

    Parameters
    ----------

    a0 : Optional[DocumentModel.Raise]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DocumentModel::NodeVisitor::visit(Raise *a0)
    ritual = 'ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_5RaiseE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_5RaiseE'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['DocumentModel.Log'])
  def visit(self, a0: Optional[DocumentModel.Log]) -> None:
    """
    Calls Qt's 'void DocumentModel::NodeVisitor::visit(Log *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-nodevisitor.html#visit

    Parameters
    ----------

    a0 : Optional[DocumentModel.Log]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DocumentModel::NodeVisitor::visit(Log *a0)
    ritual = 'ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_3LogE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_3LogE'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['DocumentModel.Script'])
  def visit(self, a0: Optional[DocumentModel.Script]) -> None:
    """
    Calls Qt's 'void DocumentModel::NodeVisitor::visit(Script *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-nodevisitor.html#visit

    Parameters
    ----------

    a0 : Optional[DocumentModel.Script]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DocumentModel::NodeVisitor::visit(Script *a0)
    ritual = 'ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_6ScriptE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_6ScriptE'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['DocumentModel.Assign'])
  def visit(self, a0: Optional[DocumentModel.Assign]) -> None:
    """
    Calls Qt's 'void DocumentModel::NodeVisitor::visit(Assign *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-nodevisitor.html#visit

    Parameters
    ----------

    a0 : Optional[DocumentModel.Assign]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DocumentModel::NodeVisitor::visit(Assign *a0)
    ritual = 'ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_6AssignE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_6AssignE'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['DocumentModel.If'])
  def visit(self, a0: Optional[DocumentModel.If]) -> bool:
    """
    Calls Qt's 'bool DocumentModel::NodeVisitor::visit(If *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-nodevisitor.html#visit

    Parameters
    ----------

    a0 : Optional[DocumentModel.If]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool DocumentModel::NodeVisitor::visit(If *a0)
    ritual = 'ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_2IfE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_2IfE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['DocumentModel.Foreach'])
  def visit(self, a0: Optional[DocumentModel.Foreach]) -> bool:
    """
    Calls Qt's 'bool DocumentModel::NodeVisitor::visit(Foreach *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-nodevisitor.html#visit

    Parameters
    ----------

    a0 : Optional[DocumentModel.Foreach]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool DocumentModel::NodeVisitor::visit(Foreach *a0)
    ritual = 'ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_7ForeachE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_7ForeachE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['DocumentModel.Cancel'])
  def visit(self, a0: Optional[DocumentModel.Cancel]) -> None:
    """
    Calls Qt's 'void DocumentModel::NodeVisitor::visit(Cancel *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-nodevisitor.html#visit

    Parameters
    ----------

    a0 : Optional[DocumentModel.Cancel]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DocumentModel::NodeVisitor::visit(Cancel *a0)
    ritual = 'ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_6CancelE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_6CancelE'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['DocumentModel.State'])
  def visit(self, a0: Optional[DocumentModel.State]) -> bool:
    """
    Calls Qt's 'bool DocumentModel::NodeVisitor::visit(State *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-nodevisitor.html#visit

    Parameters
    ----------

    a0 : Optional[DocumentModel.State]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool DocumentModel::NodeVisitor::visit(State *a0)
    ritual = 'ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_5StateE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_5StateE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['DocumentModel.Transition'])
  def visit(self, a0: Optional[DocumentModel.Transition]) -> bool:
    """
    Calls Qt's 'bool DocumentModel::NodeVisitor::visit(Transition *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-nodevisitor.html#visit

    Parameters
    ----------

    a0 : Optional[DocumentModel.Transition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool DocumentModel::NodeVisitor::visit(Transition *a0)
    ritual = 'ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_10TransitionE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_10Transition'
          'E')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['DocumentModel.HistoryState'])
  def visit(self, a0: Optional[DocumentModel.HistoryState]) -> bool:
    """
    Calls Qt's 'bool DocumentModel::NodeVisitor::visit(HistoryState *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-nodevisitor.html#visit

    Parameters
    ----------

    a0 : Optional[DocumentModel.HistoryState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool DocumentModel::NodeVisitor::visit(HistoryState *a0)
    ritual = (
        'ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_12HistoryStateE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_12HistorySta'
          'teE')
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['DocumentModel.Scxml'])
  def visit(self, a0: Optional[DocumentModel.Scxml]) -> bool:
    """
    Calls Qt's 'bool DocumentModel::NodeVisitor::visit(Scxml *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-nodevisitor.html#visit

    Parameters
    ----------

    a0 : Optional[DocumentModel.Scxml]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool DocumentModel::NodeVisitor::visit(Scxml *a0)
    ritual = 'ritual_ZN13DocumentModel11NodeVisitor5visitEPNS_5ScxmlE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13DocumentModel11NodeVisitor5visitEPNS_5ScxmlE'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['DocumentModel.DoneData'])
  @overload(NoneType)
  def endVisit(self, a0: Optional[DocumentModel.DoneData]) -> None:
    """
    Calls Qt's 'void DocumentModel::NodeVisitor::endVisit(DoneData *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-nodevisitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[DocumentModel.DoneData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DocumentModel::NodeVisitor::endVisit(DoneData *a0)
    ritual = 'ritual_ZN13DocumentModel11NodeVisitor8endVisitEPNS_8DoneDataE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13DocumentModel11NodeVisitor8endVisitEPNS_8DoneData'
          'E')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['DocumentModel.Send'])
  def endVisit(self, a0: Optional[DocumentModel.Send]) -> None:
    """
    Calls Qt's 'void DocumentModel::NodeVisitor::endVisit(Send *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-nodevisitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[DocumentModel.Send]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DocumentModel::NodeVisitor::endVisit(Send *a0)
    ritual = 'ritual_ZN13DocumentModel11NodeVisitor8endVisitEPNS_4SendE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13DocumentModel11NodeVisitor8endVisitEPNS_4SendE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['DocumentModel.Invoke'])
  def endVisit(self, a0: Optional[DocumentModel.Invoke]) -> None:
    """
    Calls Qt's 'void DocumentModel::NodeVisitor::endVisit(Invoke *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-nodevisitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[DocumentModel.Invoke]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DocumentModel::NodeVisitor::endVisit(Invoke *a0)
    ritual = 'ritual_ZN13DocumentModel11NodeVisitor8endVisitEPNS_6InvokeE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13DocumentModel11NodeVisitor8endVisitEPNS_6InvokeE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['DocumentModel.If'])
  def endVisit(self, a0: Optional[DocumentModel.If]) -> None:
    """
    Calls Qt's 'void DocumentModel::NodeVisitor::endVisit(If *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-nodevisitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[DocumentModel.If]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DocumentModel::NodeVisitor::endVisit(If *a0)
    ritual = 'ritual_ZN13DocumentModel11NodeVisitor8endVisitEPNS_2IfE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13DocumentModel11NodeVisitor8endVisitEPNS_2IfE'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['DocumentModel.Foreach'])
  def endVisit(self, a0: Optional[DocumentModel.Foreach]) -> None:
    """
    Calls Qt's 'void DocumentModel::NodeVisitor::endVisit(Foreach *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-nodevisitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[DocumentModel.Foreach]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DocumentModel::NodeVisitor::endVisit(Foreach *a0)
    ritual = 'ritual_ZN13DocumentModel11NodeVisitor8endVisitEPNS_7ForeachE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13DocumentModel11NodeVisitor8endVisitEPNS_7ForeachE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['DocumentModel.State'])
  def endVisit(self, a0: Optional[DocumentModel.State]) -> None:
    """
    Calls Qt's 'void DocumentModel::NodeVisitor::endVisit(State *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-nodevisitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[DocumentModel.State]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DocumentModel::NodeVisitor::endVisit(State *a0)
    ritual = 'ritual_ZN13DocumentModel11NodeVisitor8endVisitEPNS_5StateE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13DocumentModel11NodeVisitor8endVisitEPNS_5StateE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['DocumentModel.Transition'])
  def endVisit(self, a0: Optional[DocumentModel.Transition]) -> None:
    """
    Calls Qt's 'void DocumentModel::NodeVisitor::endVisit(Transition *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-nodevisitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[DocumentModel.Transition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DocumentModel::NodeVisitor::endVisit(Transition *a0)
    ritual = (
        'ritual_ZN13DocumentModel11NodeVisitor8endVisitEPNS_10TransitionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13DocumentModel11NodeVisitor8endVisitEPNS_10Transit'
          'ionE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['DocumentModel.HistoryState'])
  def endVisit(self, a0: Optional[DocumentModel.HistoryState]) -> None:
    """
    Calls Qt's 'void DocumentModel::NodeVisitor::endVisit(HistoryState *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-nodevisitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[DocumentModel.HistoryState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DocumentModel::NodeVisitor::endVisit(HistoryState *a0)
    ritual = (
        'ritual_ZN13DocumentModel11NodeVisitor8endVisitEPNS_12HistoryStateE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13DocumentModel11NodeVisitor8endVisitEPNS_12History'
          'StateE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(WAIT['DocumentModel.Scxml'])
  def endVisit(self, a0: Optional[DocumentModel.Scxml]) -> None:
    """
    Calls Qt's 'void DocumentModel::NodeVisitor::endVisit(Scxml *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-nodevisitor.html#endVisit

    Parameters
    ----------

    a0 : Optional[DocumentModel.Scxml]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DocumentModel::NodeVisitor::endVisit(Scxml *a0)
    ritual = 'ritual_ZN13DocumentModel11NodeVisitor8endVisitEPNS_5ScxmlE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13DocumentModel11NodeVisitor8endVisitEPNS_5ScxmlE')
    self.uglySide.call(ritual, self._addressOf(a0))
