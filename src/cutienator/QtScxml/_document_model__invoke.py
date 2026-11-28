"""
DocumentModel::Invoke binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/6.12.0/QtScxml/private/qscxmlcompiler_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means DocumentModel::Invoke to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import DocumentModel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Invoke(DocumentModel.Instruction):
  """
  The cute side of Qt's DocumentModel::Invoke: a plain Python object standing
  in front of one C++ DocumentModel::Invoke.

  It is built on the cute 'DocumentModel::Instruction', as Qt's
  DocumentModel::Invoke is built on Qt's DocumentModel::Instruction, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's DocumentModel::Invoke that has a ritual and that
  Python can call so far, 2 names in all: 'asInvoke', 'accept'. It can be
  made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ DocumentModel::Invoke is created at the first use, not by
    'DocumentModel::Invoke(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DocumentModel::Invoke.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DocumentModel::Invoke'

  #  A C++ DocumentModel::Invoke Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_DocumentModel_Invoke'

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
    Notes what was given, for Qt's 'DocumentModel::Invoke::Invoke(const
    XmlLocation &xmlLocation)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/documentmodel-invoke.html#Invoke

    Parameters
    ----------

    xmlLocation : DocumentModel.XmlLocation
      Passed on as a value: Qt reads the C++ DocumentModel::XmlLocation,
      which stays Python's own.
    """
    #  DocumentModel::Invoke::Invoke(const XmlLocation &xmlLocation)
    self._noteCreation(Invoke, lambda: Rituals.call(
        'ritual_ZN13DocumentModel6InvokeC1ERKNS_11XmlLocationE',
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

  def asInvoke(self) -> Optional[Invoke]:
    """
    Calls Qt's 'Invoke *DocumentModel::Invoke::asInvoke()'.

    Qt's own words: https://doc.qt.io/qt-6/documentmodel-invoke.html#asInvoke

    Returns
    -------

    Optional[Invoke]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Invoke *DocumentModel::Invoke::asInvoke()
    ritual = 'ritual_ZN13DocumentModel6Invoke8asInvokeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13DocumentModel6Invoke8asInvokeEv'
    address = self.uglySide.call(ritual)
    return Invoke._cuteAt(address)

  @overload(WAIT['DocumentModel.NodeVisitor'])
  @overload(NoneType)
  def accept(self, visitor: Optional[DocumentModel.NodeVisitor]) -> None:
    """
    Calls Qt's 'void DocumentModel::Invoke::accept(NodeVisitor *visitor)'.

    Qt's own words: https://doc.qt.io/qt-6/documentmodel-invoke.html#accept

    Parameters
    ----------

    visitor : Optional[DocumentModel.NodeVisitor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DocumentModel::Invoke::accept(NodeVisitor *visitor)
    ritual = 'ritual_ZN13DocumentModel6Invoke6acceptEPNS_11NodeVisitorE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13DocumentModel6Invoke6acceptEPNS_11NodeVisitorE')
    self.uglySide.call(ritual, self._addressOf(visitor))
