"""
DomAction binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomAction to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import DomProperty
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomProperty = WAIT['DomProperty']


class DomAction(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomAction: a plain Python object standing in front of
  one C++ DomAction.

  What exists
  -----------

  Every function of Qt's DomAction that has a ritual and that Python can call
  so far, 12 names in all: 'hasAttributeName', 'attributeName',
  'setAttributeName', 'clearAttributeName', 'hasAttributeMenu',
  'attributeMenu', 'setAttributeMenu', 'clearAttributeMenu',
  'elementProperty', 'setElementProperty', 'elementAttribute',
  'setElementAttribute'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomAction::~DomAction()': the destructor: Python never removes a
    C++ DomAction.
  - Qt's 'void DomAction::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void DomAction::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 20 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomAction is created at the first use, not by 'DomAction(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomAction.
  - Each name of Qt's DomAction that has no cute function yet, 'read',
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
  __qt_class__ = 'DomAction'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasAttributeName(self) -> bool:
    """
    Calls Qt's 'bool DomAction::hasAttributeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/domaction.html#hasAttributeName
    """
    #  bool DomAction::hasAttributeName() const
    return self.uglySide.call('ritual_ZNK9DomAction16hasAttributeNameEv')

  def attributeName(self) -> str:
    """
    Calls Qt's 'QString DomAction::attributeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/domaction.html#attributeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomAction::attributeName() const
    return self.uglySide.call('ritual_ZNK9DomAction13attributeNameEv')

  def hasAttributeMenu(self) -> bool:
    """
    Calls Qt's 'bool DomAction::hasAttributeMenu() const'.

    Qt's own words: https://doc.qt.io/qt-6/domaction.html#hasAttributeMenu
    """
    #  bool DomAction::hasAttributeMenu() const
    return self.uglySide.call('ritual_ZNK9DomAction16hasAttributeMenuEv')

  def attributeMenu(self) -> str:
    """
    Calls Qt's 'QString DomAction::attributeMenu() const'.

    Qt's own words: https://doc.qt.io/qt-6/domaction.html#attributeMenu

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomAction::attributeMenu() const
    return self.uglySide.call('ritual_ZNK9DomAction13attributeMenuEv')

  def elementProperty(self) -> QList[DomProperty]:
    """
    Calls Qt's 'QList<DomProperty *> DomAction::elementProperty() const'.

    Qt's own words: https://doc.qt.io/qt-6/domaction.html#elementProperty

    Returns
    -------

    QList[DomProperty]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomProperty *> DomAction::elementProperty() const
    address = self.uglySide.call('ritual_ZNK9DomAction15elementPropertyEv')
    from . import DomProperty
    return QList[DomProperty]._cuteOwning(address)

  def elementAttribute(self) -> QList[DomProperty]:
    """
    Calls Qt's 'QList<DomProperty *> DomAction::elementAttribute() const'.

    Qt's own words: https://doc.qt.io/qt-6/domaction.html#elementAttribute

    Returns
    -------

    QList[DomProperty]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomProperty *> DomAction::elementAttribute() const
    address = self.uglySide.call('ritual_ZNK9DomAction16elementAttributeEv')
    from . import DomProperty
    return QList[DomProperty]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setAttributeName(self, a: str) -> None:
    """
    Calls Qt's 'void DomAction::setAttributeName(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domaction.html#setAttributeName

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomAction::setAttributeName(const QString &a)
    self.uglySide.call('ritual_ZN9DomAction16setAttributeNameERK7QString', a)

  @overload(str)
  def setAttributeMenu(self, a: str) -> None:
    """
    Calls Qt's 'void DomAction::setAttributeMenu(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domaction.html#setAttributeMenu

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomAction::setAttributeMenu(const QString &a)
    self.uglySide.call('ritual_ZN9DomAction16setAttributeMenuERK7QString', a)

  @overload(QList[DomProperty])
  def setElementProperty(self, a: QList[DomProperty]) -> None:
    """
    Calls Qt's 'void DomAction::setElementProperty(const QList<DomProperty *>
    &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domaction.html#setElementProperty

    Parameters
    ----------

    a : QList[DomProperty]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomAction::setElementProperty(const QList<DomProperty *> &a)
    self.uglySide.call(
        'ritual_ZN9DomAction18setElementPropertyERK5QListIP11DomPropertyE',
        self._valueOf(a),
    )

  @overload(QList[DomProperty])
  def setElementAttribute(self, a: QList[DomProperty]) -> None:
    """
    Calls Qt's 'void DomAction::setElementAttribute(const QList<DomProperty
    *> &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domaction.html#setElementAttribute

    Parameters
    ----------

    a : QList[DomProperty]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomAction::setElementAttribute(const QList<DomProperty *> &a)
    self.uglySide.call(
        'ritual_ZN9DomAction19setElementAttributeERK5QListIP11DomPropertyE',
        self._valueOf(a),
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
    Notes what was given, for Qt's 'DomAction::DomAction()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/domaction.html#DomAction
    """
    #  DomAction::DomAction()
    self._noteCreation(DomAction, lambda: Rituals.call(
        'ritual_ZN9DomActionC1Ev',
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

  def clearAttributeName(self) -> None:
    """
    Calls Qt's 'void DomAction::clearAttributeName()'.

    Qt's own words: https://doc.qt.io/qt-6/domaction.html#clearAttributeName
    """
    #  void DomAction::clearAttributeName()
    self.uglySide.call('ritual_ZN9DomAction18clearAttributeNameEv')

  def clearAttributeMenu(self) -> None:
    """
    Calls Qt's 'void DomAction::clearAttributeMenu()'.

    Qt's own words: https://doc.qt.io/qt-6/domaction.html#clearAttributeMenu
    """
    #  void DomAction::clearAttributeMenu()
    self.uglySide.call('ritual_ZN9DomAction18clearAttributeMenuEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomAction::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomAction.read' has no cute function yet. Qt's 'void "
        "DomAction::read(QXmlStreamReader &reader)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomAction::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomAction.write' has no cute function yet. Qt's 'void "
        "DomAction::write(QXmlStreamWriter &writer, const QString &tagName) "
        "const': takes a type Python has no way to hand over yet.")


#  Qt's 'QList<DomAction *>': the list of DomAction, which 'QList[DomAction]'
#  gives. It is made here, so that there is one as soon as there can be a
#  DomAction.
QList.createKind(
    DomAction, 'address',
    make='ritual_list_make_DomAction_ptr',
    add='ritual_list_add_DomAction_ptr',
    size='ritual_list_size_DomAction_ptr',
    at='ritual_list_at_DomAction_ptr',
    drop='ritual_list_drop_DomAction_ptr',
)
