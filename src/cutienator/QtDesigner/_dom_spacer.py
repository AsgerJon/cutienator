"""
DomSpacer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomSpacer to be private: it declares the class in a header it
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


class DomSpacer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomSpacer: a plain Python object standing in front of
  one C++ DomSpacer.

  What exists
  -----------

  Every function of Qt's DomSpacer that has a ritual and that Python can call
  so far, 6 names in all: 'hasAttributeName', 'attributeName',
  'setAttributeName', 'clearAttributeName', 'elementProperty',
  'setElementProperty'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomSpacer::~DomSpacer()': the destructor: Python never removes a
    C++ DomSpacer.
  - Qt's 'void DomSpacer::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void DomSpacer::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 14 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomSpacer is created at the first use, not by 'DomSpacer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomSpacer.
  - Each name of Qt's DomSpacer that has no cute function yet, 'read',
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
  __qt_class__ = 'DomSpacer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasAttributeName(self) -> bool:
    """
    Calls Qt's 'bool DomSpacer::hasAttributeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/domspacer.html#hasAttributeName
    """
    #  bool DomSpacer::hasAttributeName() const
    return self.uglySide.call('ritual_ZNK9DomSpacer16hasAttributeNameEv')

  def attributeName(self) -> str:
    """
    Calls Qt's 'QString DomSpacer::attributeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/domspacer.html#attributeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomSpacer::attributeName() const
    return self.uglySide.call('ritual_ZNK9DomSpacer13attributeNameEv')

  def elementProperty(self) -> QList[DomProperty]:
    """
    Calls Qt's 'QList<DomProperty *> DomSpacer::elementProperty() const'.

    Qt's own words: https://doc.qt.io/qt-6/domspacer.html#elementProperty

    Returns
    -------

    QList[DomProperty]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomProperty *> DomSpacer::elementProperty() const
    address = self.uglySide.call('ritual_ZNK9DomSpacer15elementPropertyEv')
    from . import DomProperty
    return QList[DomProperty]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setAttributeName(self, a: str) -> None:
    """
    Calls Qt's 'void DomSpacer::setAttributeName(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domspacer.html#setAttributeName

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomSpacer::setAttributeName(const QString &a)
    self.uglySide.call('ritual_ZN9DomSpacer16setAttributeNameERK7QString', a)

  @overload(QList[DomProperty])
  def setElementProperty(self, a: QList[DomProperty]) -> None:
    """
    Calls Qt's 'void DomSpacer::setElementProperty(const QList<DomProperty *>
    &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domspacer.html#setElementProperty

    Parameters
    ----------

    a : QList[DomProperty]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomSpacer::setElementProperty(const QList<DomProperty *> &a)
    self.uglySide.call(
        'ritual_ZN9DomSpacer18setElementPropertyERK5QListIP11DomPropertyE',
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
    Notes what was given, for Qt's 'DomSpacer::DomSpacer()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/domspacer.html#DomSpacer
    """
    #  DomSpacer::DomSpacer()
    self._noteCreation(DomSpacer, lambda: Rituals.call(
        'ritual_ZN9DomSpacerC1Ev',
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
    Calls Qt's 'void DomSpacer::clearAttributeName()'.

    Qt's own words: https://doc.qt.io/qt-6/domspacer.html#clearAttributeName
    """
    #  void DomSpacer::clearAttributeName()
    self.uglySide.call('ritual_ZN9DomSpacer18clearAttributeNameEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomSpacer::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomSpacer.read' has no cute function yet. Qt's 'void "
        "DomSpacer::read(QXmlStreamReader &reader)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomSpacer::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomSpacer.write' has no cute function yet. Qt's 'void "
        "DomSpacer::write(QXmlStreamWriter &writer, const QString &tagName) "
        "const': takes a type Python has no way to hand over yet.")
