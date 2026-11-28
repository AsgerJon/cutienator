"""
DomButtonGroup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomButtonGroup to be private: it declares the class in a header
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

  from . import DomProperty
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomProperty = WAIT['DomProperty']


class DomButtonGroup(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomButtonGroup: a plain Python object standing in
  front of one C++ DomButtonGroup.

  What exists
  -----------

  Every function of Qt's DomButtonGroup that has a ritual and that Python can
  call so far, 8 names in all: 'hasAttributeName', 'attributeName',
  'setAttributeName', 'clearAttributeName', 'elementProperty',
  'setElementProperty', 'elementAttribute', 'setElementAttribute'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomButtonGroup::~DomButtonGroup()': the destructor: Python never
    removes a C++ DomButtonGroup.
  - Qt's 'void DomButtonGroup::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void DomButtonGroup::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomButtonGroup is created at the first use, not by
    'DomButtonGroup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomButtonGroup.
  - Each name of Qt's DomButtonGroup that has no cute function yet, 'read',
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
  __qt_class__ = 'DomButtonGroup'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasAttributeName(self) -> bool:
    """
    Calls Qt's 'bool DomButtonGroup::hasAttributeName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/dombuttongroup.html#hasAttributeName
    """
    #  bool DomButtonGroup::hasAttributeName() const
    return self.uglySide.call(
        'ritual_ZNK14DomButtonGroup16hasAttributeNameEv',
    )

  def attributeName(self) -> str:
    """
    Calls Qt's 'QString DomButtonGroup::attributeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/dombuttongroup.html#attributeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomButtonGroup::attributeName() const
    return self.uglySide.call('ritual_ZNK14DomButtonGroup13attributeNameEv')

  def elementProperty(self) -> QList[DomProperty]:
    """
    Calls Qt's 'QList<DomProperty *> DomButtonGroup::elementProperty()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/dombuttongroup.html#elementProperty

    Returns
    -------

    QList[DomProperty]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomProperty *> DomButtonGroup::elementProperty() const
    address = self.uglySide.call(
        'ritual_ZNK14DomButtonGroup15elementPropertyEv',
    )
    from . import DomProperty
    return QList[DomProperty]._cuteOwning(address)

  def elementAttribute(self) -> QList[DomProperty]:
    """
    Calls Qt's 'QList<DomProperty *> DomButtonGroup::elementAttribute()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/dombuttongroup.html#elementAttribute

    Returns
    -------

    QList[DomProperty]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomProperty *> DomButtonGroup::elementAttribute() const
    address = self.uglySide.call(
        'ritual_ZNK14DomButtonGroup16elementAttributeEv',
    )
    from . import DomProperty
    return QList[DomProperty]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setAttributeName(self, a: str) -> None:
    """
    Calls Qt's 'void DomButtonGroup::setAttributeName(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/dombuttongroup.html#setAttributeName

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomButtonGroup::setAttributeName(const QString &a)
    self.uglySide.call(
        'ritual_ZN14DomButtonGroup16setAttributeNameERK7QString', a,
    )

  @overload(QList[DomProperty])
  def setElementProperty(self, a: QList[DomProperty]) -> None:
    """
    Calls Qt's 'void DomButtonGroup::setElementProperty(const
    QList<DomProperty *> &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/dombuttongroup.html#setElementProperty

    Parameters
    ----------

    a : QList[DomProperty]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomButtonGroup::setElementProperty(const QList<DomProperty *> &a)
    self.uglySide.call(
        'ritual_ZN14DomButtonGroup18setElementPropertyERK5QListIP11DomPrope'
        'rtyE',
        self._valueOf(a),
    )

  @overload(QList[DomProperty])
  def setElementAttribute(self, a: QList[DomProperty]) -> None:
    """
    Calls Qt's 'void DomButtonGroup::setElementAttribute(const
    QList<DomProperty *> &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/dombuttongroup.html#setElementAttribute

    Parameters
    ----------

    a : QList[DomProperty]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomButtonGroup::setElementAttribute(const QList<DomProperty *>
    #      &a)
    self.uglySide.call(
        'ritual_ZN14DomButtonGroup19setElementAttributeERK5QListIP11DomProp'
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
    Notes what was given, for Qt's 'DomButtonGroup::DomButtonGroup()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/dombuttongroup.html#DomButtonGroup
    """
    #  DomButtonGroup::DomButtonGroup()
    self._noteCreation(DomButtonGroup, lambda: Rituals.call(
        'ritual_ZN14DomButtonGroupC1Ev',
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
    Calls Qt's 'void DomButtonGroup::clearAttributeName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/dombuttongroup.html#clearAttributeName
    """
    #  void DomButtonGroup::clearAttributeName()
    self.uglySide.call('ritual_ZN14DomButtonGroup18clearAttributeNameEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomButtonGroup::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomButtonGroup.read' has no cute function yet. Qt's 'void "
        "DomButtonGroup::read(QXmlStreamReader &reader)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomButtonGroup::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomButtonGroup.write' has no cute function yet. Qt's 'void "
        "DomButtonGroup::write(QXmlStreamWriter &writer, const QString "
        "&tagName) const': takes a type Python has no way to hand over yet.")


#  Qt's 'QList<DomButtonGroup *>': the list of DomButtonGroup, which
#  'QList[DomButtonGroup]' gives. It is made here, so that there is one as
#  soon as there can be a DomButtonGroup.
QList.createKind(
    DomButtonGroup, 'address',
    make='ritual_list_make_DomButtonGroup_ptr',
    add='ritual_list_add_DomButtonGroup_ptr',
    size='ritual_list_size_DomButtonGroup_ptr',
    at='ritual_list_at_DomButtonGroup_ptr',
    drop='ritual_list_drop_DomButtonGroup_ptr',
)
