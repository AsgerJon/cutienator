"""
DomActionGroup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomActionGroup to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import DomAction, DomProperty
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomAction = WAIT['DomAction']
  DomProperty = WAIT['DomProperty']


class DomActionGroup(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomActionGroup: a plain Python object standing in
  front of one C++ DomActionGroup.

  What exists
  -----------

  Every function of Qt's DomActionGroup that has a ritual and that Python can
  call so far, 12 names in all: 'hasAttributeName', 'attributeName',
  'setAttributeName', 'clearAttributeName', 'elementAction',
  'setElementAction', 'elementActionGroup', 'setElementActionGroup',
  'elementProperty', 'setElementProperty', 'elementAttribute',
  'setElementAttribute'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomActionGroup::~DomActionGroup()': the destructor: Python never
    removes a C++ DomActionGroup.
  - Qt's 'void DomActionGroup::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void DomActionGroup::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 20 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomActionGroup is created at the first use, not by
    'DomActionGroup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomActionGroup.
  - Each name of Qt's DomActionGroup that has no cute function yet, 'read',
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
  __qt_class__ = 'DomActionGroup'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasAttributeName(self) -> bool:
    """
    Calls Qt's 'bool DomActionGroup::hasAttributeName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domactiongroup.html#hasAttributeName
    """
    #  bool DomActionGroup::hasAttributeName() const
    return self.uglySide.call(
        'ritual_ZNK14DomActionGroup16hasAttributeNameEv',
    )

  def attributeName(self) -> str:
    """
    Calls Qt's 'QString DomActionGroup::attributeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/domactiongroup.html#attributeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomActionGroup::attributeName() const
    return self.uglySide.call('ritual_ZNK14DomActionGroup13attributeNameEv')

  def elementAction(self) -> QList[DomAction]:
    """
    Calls Qt's 'QList<DomAction *> DomActionGroup::elementAction() const'.

    Qt's own words: https://doc.qt.io/qt-6/domactiongroup.html#elementAction

    Returns
    -------

    QList[DomAction]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomAction *> DomActionGroup::elementAction() const
    address = self.uglySide.call(
        'ritual_ZNK14DomActionGroup13elementActionEv',
    )
    from . import DomAction
    return QList[DomAction]._cuteOwning(address)

  def elementActionGroup(self) -> QList[DomActionGroup]:
    """
    Calls Qt's 'QList<DomActionGroup *> DomActionGroup::elementActionGroup()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domactiongroup.html#elementActionGroup

    Returns
    -------

    QList[DomActionGroup]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomActionGroup *> DomActionGroup::elementActionGroup() const
    address = self.uglySide.call(
        'ritual_ZNK14DomActionGroup18elementActionGroupEv',
    )
    return QList[DomActionGroup]._cuteOwning(address)

  def elementProperty(self) -> QList[DomProperty]:
    """
    Calls Qt's 'QList<DomProperty *> DomActionGroup::elementProperty()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domactiongroup.html#elementProperty

    Returns
    -------

    QList[DomProperty]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomProperty *> DomActionGroup::elementProperty() const
    address = self.uglySide.call(
        'ritual_ZNK14DomActionGroup15elementPropertyEv',
    )
    from . import DomProperty
    return QList[DomProperty]._cuteOwning(address)

  def elementAttribute(self) -> QList[DomProperty]:
    """
    Calls Qt's 'QList<DomProperty *> DomActionGroup::elementAttribute()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domactiongroup.html#elementAttribute

    Returns
    -------

    QList[DomProperty]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomProperty *> DomActionGroup::elementAttribute() const
    address = self.uglySide.call(
        'ritual_ZNK14DomActionGroup16elementAttributeEv',
    )
    from . import DomProperty
    return QList[DomProperty]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setAttributeName(self, a: str) -> None:
    """
    Calls Qt's 'void DomActionGroup::setAttributeName(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domactiongroup.html#setAttributeName

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomActionGroup::setAttributeName(const QString &a)
    self.uglySide.call(
        'ritual_ZN14DomActionGroup16setAttributeNameERK7QString', a,
    )

  @overload(QList[DomAction])
  def setElementAction(self, a: QList[DomAction]) -> None:
    """
    Calls Qt's 'void DomActionGroup::setElementAction(const QList<DomAction
    *> &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domactiongroup.html#setElementAction

    Parameters
    ----------

    a : QList[DomAction]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomActionGroup::setElementAction(const QList<DomAction *> &a)
    self.uglySide.call(
        'ritual_ZN14DomActionGroup16setElementActionERK5QListIP9DomActionE',
        self._valueOf(a),
    )

  @overload(QList[WAIT['DomActionGroup']])
  def setElementActionGroup(self, a: QList[DomActionGroup]) -> None:
    """
    Calls Qt's 'void DomActionGroup::setElementActionGroup(const
    QList<DomActionGroup *> &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domactiongroup.html#setElementActionGroup

    Parameters
    ----------

    a : QList[DomActionGroup]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomActionGroup::setElementActionGroup(const QList<DomActionGroup
    #      *> &a)
    self.uglySide.call(
        'ritual_ZN14DomActionGroup21setElementActionGroupERK5QListIPS_E',
        self._valueOf(a),
    )

  @overload(QList[DomProperty])
  def setElementProperty(self, a: QList[DomProperty]) -> None:
    """
    Calls Qt's 'void DomActionGroup::setElementProperty(const
    QList<DomProperty *> &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domactiongroup.html#setElementProperty

    Parameters
    ----------

    a : QList[DomProperty]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomActionGroup::setElementProperty(const QList<DomProperty *> &a)
    self.uglySide.call(
        'ritual_ZN14DomActionGroup18setElementPropertyERK5QListIP11DomPrope'
        'rtyE',
        self._valueOf(a),
    )

  @overload(QList[DomProperty])
  def setElementAttribute(self, a: QList[DomProperty]) -> None:
    """
    Calls Qt's 'void DomActionGroup::setElementAttribute(const
    QList<DomProperty *> &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domactiongroup.html#setElementAttribute

    Parameters
    ----------

    a : QList[DomProperty]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomActionGroup::setElementAttribute(const QList<DomProperty *>
    #      &a)
    self.uglySide.call(
        'ritual_ZN14DomActionGroup19setElementAttributeERK5QListIP11DomProp'
        'ertyE',
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
    Notes what was given, for Qt's 'DomActionGroup::DomActionGroup()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/domactiongroup.html#DomActionGroup
    """
    #  DomActionGroup::DomActionGroup()
    self._noteCreation(DomActionGroup, lambda: Rituals.call(
        'ritual_ZN14DomActionGroupC1Ev',
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
    Calls Qt's 'void DomActionGroup::clearAttributeName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domactiongroup.html#clearAttributeName
    """
    #  void DomActionGroup::clearAttributeName()
    self.uglySide.call('ritual_ZN14DomActionGroup18clearAttributeNameEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomActionGroup::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomActionGroup.read' has no cute function yet. Qt's 'void "
        "DomActionGroup::read(QXmlStreamReader &reader)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomActionGroup::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomActionGroup.write' has no cute function yet. Qt's 'void "
        "DomActionGroup::write(QXmlStreamWriter &writer, const QString "
        "&tagName) const': takes a type Python has no way to hand over yet.")


#  Qt's 'QList<DomActionGroup *>': the list of DomActionGroup, which
#  'QList[DomActionGroup]' gives. It is made here, so that there is one as
#  soon as there can be a DomActionGroup.
QList.createKind(
    DomActionGroup, 'address',
    make='ritual_list_make_DomActionGroup_ptr',
    add='ritual_list_add_DomActionGroup_ptr',
    size='ritual_list_size_DomActionGroup_ptr',
    at='ritual_list_at_DomActionGroup_ptr',
    drop='ritual_list_drop_DomActionGroup_ptr',
)
