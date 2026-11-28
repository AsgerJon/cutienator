"""
DocumentModel::ScxmlDocument binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/6.12.0/QtScxml/private/qscxmlcompiler_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means DocumentModel::ScxmlDocument to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import DocumentModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ScxmlDocument(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DocumentModel::ScxmlDocument: a plain Python object
  standing in front of one C++ DocumentModel::ScxmlDocument.

  C++ hands a DocumentModel::ScxmlDocument around as a copy, so every C++
  DocumentModel::ScxmlDocument behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's DocumentModel::ScxmlDocument that has a ritual and
  that Python can call so far, 3 names in all: 'newState', 'newHistoryState',
  'newTransition'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DocumentModel::ScxmlDocument::~ScxmlDocument()': the destructor:
    Python removes its C++ DocumentModel::ScxmlDocument by it, and has no
    other use for it.
  - Qt's 'InstructionSequence
    *DocumentModel::ScxmlDocument::newSequence(InstructionSequences
    *container)': names 'DocumentModel::InstructionSequences', which has no
    cute class yet.

  What has no ritual
  ------------------

  1 of the 7 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ DocumentModel::ScxmlDocument is created at the first use, not by
    'DocumentModel::ScxmlDocument(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a DocumentModel::ScxmlDocument back gives a copy the
    ritual made for Python, in a new cute DocumentModel::ScxmlDocument.
  - Each name of Qt's DocumentModel::ScxmlDocument that has no cute function
    yet, 'newNode', 'newSequence', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DocumentModel::ScxmlDocument'

  #  Qt's '~DocumentModel::ScxmlDocument()'. Naming it makes this a value
  #  class: Python owns every C++ DocumentModel::ScxmlDocument behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN13DocumentModel13ScxmlDocumentD1Ev'

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

  @overload(str)
  def __init__(self, fileName: str) -> None:
    """
    Notes what was given, for Qt's
    'DocumentModel::ScxmlDocument::ScxmlDocument(const QString &fileName)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-scxmldocument.html#ScxmlDocument

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  DocumentModel::ScxmlDocument::ScxmlDocument(const QString &fileName)
    self._noteCreation(ScxmlDocument, lambda: Rituals.call(
        'ritual_ZN13DocumentModel13ScxmlDocumentC1ERK7QString', fileName,
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

  @overload(
      WAIT['DocumentModel.StateContainer'], DocumentModel.State.Type,
      WAIT['DocumentModel.XmlLocation'],
  )
  @overload(
      NoneType, DocumentModel.State.Type, WAIT['DocumentModel.XmlLocation'],
  )
  def newState(
      self,
      parent: Optional[DocumentModel.StateContainer],
      type: DocumentModel.State.Type,
      xmlLocation: DocumentModel.XmlLocation,
  ) -> Optional[DocumentModel.State]:
    """
    Calls Qt's 'State *DocumentModel::ScxmlDocument::newState(StateContainer
    *parent, State::Type type, const XmlLocation &xmlLocation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-scxmldocument.html#newState

    Parameters
    ----------

    parent : Optional[DocumentModel.StateContainer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    type : DocumentModel.State.Type
      Passed on as its number.

    xmlLocation : DocumentModel.XmlLocation
      Passed on as a value: Qt reads the C++ DocumentModel::XmlLocation,
      which stays Python's own.

    Returns
    -------

    Optional[DocumentModel.State]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  State *DocumentModel::ScxmlDocument::newState(StateContainer *parent,
    #      State::Type type, const XmlLocation &xmlLocation)
    address = self.uglySide.call(
        'ritual_ZN13DocumentModel13ScxmlDocument8newStateEPNS_14StateContai'
        'nerENS_5State4TypeERKNS_11XmlLocationE',
        self._addressOf(parent), type.value, self._valueOf(xmlLocation),
    )
    return DocumentModel.State._cuteAt(address)

  @overload(
      WAIT['DocumentModel.StateContainer'],
      WAIT['DocumentModel.XmlLocation'],
  )
  @overload(NoneType, WAIT['DocumentModel.XmlLocation'])
  def newHistoryState(
      self,
      parent: Optional[DocumentModel.StateContainer],
      xmlLocation: DocumentModel.XmlLocation,
  ) -> Optional[DocumentModel.HistoryState]:
    """
    Calls Qt's 'HistoryState
    *DocumentModel::ScxmlDocument::newHistoryState(StateContainer *parent,
    const XmlLocation &xmlLocation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-scxmldocument.html#newHistoryState

    Parameters
    ----------

    parent : Optional[DocumentModel.StateContainer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    xmlLocation : DocumentModel.XmlLocation
      Passed on as a value: Qt reads the C++ DocumentModel::XmlLocation,
      which stays Python's own.

    Returns
    -------

    Optional[DocumentModel.HistoryState]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  HistoryState
    #      *DocumentModel::ScxmlDocument::newHistoryState(StateContainer
    #      *parent, const XmlLocation &xmlLocation)
    address = self.uglySide.call(
        'ritual_ZN13DocumentModel13ScxmlDocument15newHistoryStateEPNS_14Sta'
        'teContainerERKNS_11XmlLocationE',
        self._addressOf(parent), self._valueOf(xmlLocation),
    )
    return DocumentModel.HistoryState._cuteAt(address)

  @overload(
      WAIT['DocumentModel.StateContainer'],
      WAIT['DocumentModel.XmlLocation'],
  )
  @overload(NoneType, WAIT['DocumentModel.XmlLocation'])
  def newTransition(
      self,
      parent: Optional[DocumentModel.StateContainer],
      xmlLocation: DocumentModel.XmlLocation,
  ) -> Optional[DocumentModel.Transition]:
    """
    Calls Qt's 'Transition
    *DocumentModel::ScxmlDocument::newTransition(StateContainer *parent,
    const XmlLocation &xmlLocation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/documentmodel-scxmldocument.html#newTransition

    Parameters
    ----------

    parent : Optional[DocumentModel.StateContainer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    xmlLocation : DocumentModel.XmlLocation
      Passed on as a value: Qt reads the C++ DocumentModel::XmlLocation,
      which stays Python's own.

    Returns
    -------

    Optional[DocumentModel.Transition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Transition *DocumentModel::ScxmlDocument::newTransition(StateContainer
    #      *parent, const XmlLocation &xmlLocation)
    address = self.uglySide.call(
        'ritual_ZN13DocumentModel13ScxmlDocument13newTransitionEPNS_14State'
        'ContainerERKNS_11XmlLocationE',
        self._addressOf(parent), self._valueOf(xmlLocation),
    )
    return DocumentModel.Transition._cuteAt(address)

  @staticmethod
  def newNode(*__, **_) -> Never:
    """
    Qt's 'DocumentModel::ScxmlDocument::newNode': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'DocumentModel.ScxmlDocument.newNode' has no cute function yet. "
        "Qt's 'DocumentModel::ScxmlDocument::newNode': a template: a "
        "pattern and no single function.")

  @staticmethod
  def newSequence(*__, **_) -> Never:
    """
    Qt's 'InstructionSequence
    *DocumentModel::ScxmlDocument::newSequence(InstructionSequences
    *container)': names 'DocumentModel::InstructionSequences', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'DocumentModel.ScxmlDocument.newSequence' has no cute function "
        "yet. Qt's 'InstructionSequence "
        "*DocumentModel::ScxmlDocument::newSequence(InstructionSequences "
        "*container)': names 'DocumentModel::InstructionSequences', which "
        "has no cute class yet.")
