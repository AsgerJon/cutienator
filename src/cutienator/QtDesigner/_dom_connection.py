"""
DomConnection binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomConnection to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import DomConnectionHints
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomConnectionHints = WAIT['DomConnectionHints']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DomConnection(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomConnection: a plain Python object standing in
  front of one C++ DomConnection.

  What exists
  -----------

  Every function of Qt's DomConnection that has a ritual and that Python can
  call so far, 21 names in all: 'elementSender', 'setElementSender',
  'hasElementSender', 'clearElementSender', 'elementSignal',
  'setElementSignal', 'hasElementSignal', 'clearElementSignal',
  'elementReceiver', 'setElementReceiver', 'hasElementReceiver',
  'clearElementReceiver', 'elementSlot', 'setElementSlot', 'hasElementSlot',
  'clearElementSlot', 'elementHints', 'takeElementHints', 'setElementHints',
  'hasElementHints', 'clearElementHints'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomConnection::~DomConnection()': the destructor: Python never
    removes a C++ DomConnection.
  - Qt's 'void DomConnection::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void DomConnection::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 29 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomConnection is created at the first use, not by
    'DomConnection(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomConnection.
  - Each name of Qt's DomConnection that has no cute function yet, 'read',
    'write', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DomConnection'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def elementSender(self) -> str:
    """
    Calls Qt's 'QString DomConnection::elementSender() const'.

    Qt's own words: https://doc.qt.io/qt-6/domconnection.html#elementSender

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomConnection::elementSender() const
    return self.uglySide.call('ritual_ZNK13DomConnection13elementSenderEv')

  def hasElementSender(self) -> bool:
    """
    Calls Qt's 'bool DomConnection::hasElementSender() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domconnection.html#hasElementSender
    """
    #  bool DomConnection::hasElementSender() const
    return self.uglySide.call(
        'ritual_ZNK13DomConnection16hasElementSenderEv',
    )

  def elementSignal(self) -> str:
    """
    Calls Qt's 'QString DomConnection::elementSignal() const'.

    Qt's own words: https://doc.qt.io/qt-6/domconnection.html#elementSignal

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomConnection::elementSignal() const
    return self.uglySide.call('ritual_ZNK13DomConnection13elementSignalEv')

  def hasElementSignal(self) -> bool:
    """
    Calls Qt's 'bool DomConnection::hasElementSignal() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domconnection.html#hasElementSignal
    """
    #  bool DomConnection::hasElementSignal() const
    return self.uglySide.call(
        'ritual_ZNK13DomConnection16hasElementSignalEv',
    )

  def elementReceiver(self) -> str:
    """
    Calls Qt's 'QString DomConnection::elementReceiver() const'.

    Qt's own words: https://doc.qt.io/qt-6/domconnection.html#elementReceiver

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomConnection::elementReceiver() const
    return self.uglySide.call('ritual_ZNK13DomConnection15elementReceiverEv')

  def hasElementReceiver(self) -> bool:
    """
    Calls Qt's 'bool DomConnection::hasElementReceiver() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domconnection.html#hasElementReceiver
    """
    #  bool DomConnection::hasElementReceiver() const
    return self.uglySide.call(
        'ritual_ZNK13DomConnection18hasElementReceiverEv',
    )

  def elementSlot(self) -> str:
    """
    Calls Qt's 'QString DomConnection::elementSlot() const'.

    Qt's own words: https://doc.qt.io/qt-6/domconnection.html#elementSlot

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomConnection::elementSlot() const
    return self.uglySide.call('ritual_ZNK13DomConnection11elementSlotEv')

  def hasElementSlot(self) -> bool:
    """
    Calls Qt's 'bool DomConnection::hasElementSlot() const'.

    Qt's own words: https://doc.qt.io/qt-6/domconnection.html#hasElementSlot
    """
    #  bool DomConnection::hasElementSlot() const
    return self.uglySide.call('ritual_ZNK13DomConnection14hasElementSlotEv')

  def elementHints(self) -> Optional[DomConnectionHints]:
    """
    Calls Qt's 'DomConnectionHints *DomConnection::elementHints() const'.

    Qt's own words: https://doc.qt.io/qt-6/domconnection.html#elementHints

    Returns
    -------

    Optional[DomConnectionHints]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomConnectionHints *DomConnection::elementHints() const
    address = self.uglySide.call('ritual_ZNK13DomConnection12elementHintsEv')
    from . import DomConnectionHints
    return DomConnectionHints._cuteAt(address)

  def hasElementHints(self) -> bool:
    """
    Calls Qt's 'bool DomConnection::hasElementHints() const'.

    Qt's own words: https://doc.qt.io/qt-6/domconnection.html#hasElementHints
    """
    #  bool DomConnection::hasElementHints() const
    return self.uglySide.call('ritual_ZNK13DomConnection15hasElementHintsEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setElementSender(self, a: str) -> None:
    """
    Calls Qt's 'void DomConnection::setElementSender(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domconnection.html#setElementSender

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomConnection::setElementSender(const QString &a)
    self.uglySide.call(
        'ritual_ZN13DomConnection16setElementSenderERK7QString', a,
    )

  @overload(str)
  def setElementSignal(self, a: str) -> None:
    """
    Calls Qt's 'void DomConnection::setElementSignal(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domconnection.html#setElementSignal

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomConnection::setElementSignal(const QString &a)
    self.uglySide.call(
        'ritual_ZN13DomConnection16setElementSignalERK7QString', a,
    )

  @overload(str)
  def setElementReceiver(self, a: str) -> None:
    """
    Calls Qt's 'void DomConnection::setElementReceiver(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domconnection.html#setElementReceiver

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomConnection::setElementReceiver(const QString &a)
    self.uglySide.call(
        'ritual_ZN13DomConnection18setElementReceiverERK7QString', a,
    )

  @overload(str)
  def setElementSlot(self, a: str) -> None:
    """
    Calls Qt's 'void DomConnection::setElementSlot(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domconnection.html#setElementSlot

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomConnection::setElementSlot(const QString &a)
    self.uglySide.call(
        'ritual_ZN13DomConnection14setElementSlotERK7QString', a,
    )

  @overload(DomConnectionHints)
  @overload(NoneType)
  def setElementHints(self, a: Optional[DomConnectionHints]) -> None:
    """
    Calls Qt's 'void DomConnection::setElementHints(DomConnectionHints *a)'.

    Qt's own words: https://doc.qt.io/qt-6/domconnection.html#setElementHints

    Parameters
    ----------

    a : Optional[DomConnectionHints]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DomConnection::setElementHints(DomConnectionHints *a)
    self.uglySide.call(
        'ritual_ZN13DomConnection15setElementHintsEP18DomConnectionHints',
        self._addressOf(a),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'DomConnection::DomConnection()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/domconnection.html#DomConnection
    """
    #  DomConnection::DomConnection()
    self._noteCreation(DomConnection, lambda: Rituals.call(
        'ritual_ZN13DomConnectionC1Ev',
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

  def clearElementSender(self) -> None:
    """
    Calls Qt's 'void DomConnection::clearElementSender()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domconnection.html#clearElementSender
    """
    #  void DomConnection::clearElementSender()
    self.uglySide.call('ritual_ZN13DomConnection18clearElementSenderEv')

  def clearElementSignal(self) -> None:
    """
    Calls Qt's 'void DomConnection::clearElementSignal()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domconnection.html#clearElementSignal
    """
    #  void DomConnection::clearElementSignal()
    self.uglySide.call('ritual_ZN13DomConnection18clearElementSignalEv')

  def clearElementReceiver(self) -> None:
    """
    Calls Qt's 'void DomConnection::clearElementReceiver()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domconnection.html#clearElementReceiver
    """
    #  void DomConnection::clearElementReceiver()
    self.uglySide.call('ritual_ZN13DomConnection20clearElementReceiverEv')

  def clearElementSlot(self) -> None:
    """
    Calls Qt's 'void DomConnection::clearElementSlot()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domconnection.html#clearElementSlot
    """
    #  void DomConnection::clearElementSlot()
    self.uglySide.call('ritual_ZN13DomConnection16clearElementSlotEv')

  def takeElementHints(self) -> Optional[DomConnectionHints]:
    """
    Calls Qt's 'DomConnectionHints *DomConnection::takeElementHints()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domconnection.html#takeElementHints

    Returns
    -------

    Optional[DomConnectionHints]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DomConnectionHints *DomConnection::takeElementHints()
    address = self.uglySide.call(
        'ritual_ZN13DomConnection16takeElementHintsEv',
    )
    from . import DomConnectionHints
    return DomConnectionHints._cuteAt(address)

  def clearElementHints(self) -> None:
    """
    Calls Qt's 'void DomConnection::clearElementHints()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domconnection.html#clearElementHints
    """
    #  void DomConnection::clearElementHints()
    self.uglySide.call('ritual_ZN13DomConnection17clearElementHintsEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomConnection::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomConnection.read' has no cute function yet. Qt's 'void "
        "DomConnection::read(QXmlStreamReader &reader)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomConnection::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomConnection.write' has no cute function yet. Qt's 'void "
        "DomConnection::write(QXmlStreamWriter &writer, const QString "
        "&tagName) const': takes a type Python has no way to hand over yet.")


#  Qt's 'QList<DomConnection *>': the list of DomConnection, which
#  'QList[DomConnection]' gives. It is made here, so that there is one as
#  soon as there can be a DomConnection.
QList.createKind(
    DomConnection, 'address',
    make='ritual_list_make_DomConnection_ptr',
    add='ritual_list_add_DomConnection_ptr',
    size='ritual_list_size_DomConnection_ptr',
    at='ritual_list_at_DomConnection_ptr',
    drop='ritual_list_drop_DomConnection_ptr',
)
