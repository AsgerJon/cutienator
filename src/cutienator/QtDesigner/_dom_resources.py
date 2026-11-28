"""
DomResources binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomResources to be private: it declares the class in a header it
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

  from . import DomResource
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomResource = WAIT['DomResource']


class DomResources(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomResources: a plain Python object standing in front
  of one C++ DomResources.

  What exists
  -----------

  Every function of Qt's DomResources that has a ritual and that Python can
  call so far, 6 names in all: 'hasAttributeName', 'attributeName',
  'setAttributeName', 'clearAttributeName', 'elementInclude',
  'setElementInclude'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomResources::~DomResources()': the destructor: Python never
    removes a C++ DomResources.
  - Qt's 'void DomResources::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void DomResources::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 14 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomResources is created at the first use, not by
    'DomResources(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomResources.
  - Each name of Qt's DomResources that has no cute function yet, 'read',
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
  __qt_class__ = 'DomResources'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasAttributeName(self) -> bool:
    """
    Calls Qt's 'bool DomResources::hasAttributeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/domresources.html#hasAttributeName
    """
    #  bool DomResources::hasAttributeName() const
    return self.uglySide.call('ritual_ZNK12DomResources16hasAttributeNameEv')

  def attributeName(self) -> str:
    """
    Calls Qt's 'QString DomResources::attributeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/domresources.html#attributeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomResources::attributeName() const
    return self.uglySide.call('ritual_ZNK12DomResources13attributeNameEv')

  def elementInclude(self) -> QList[DomResource]:
    """
    Calls Qt's 'QList<DomResource *> DomResources::elementInclude() const'.

    Qt's own words: https://doc.qt.io/qt-6/domresources.html#elementInclude

    Returns
    -------

    QList[DomResource]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomResource *> DomResources::elementInclude() const
    address = self.uglySide.call(
        'ritual_ZNK12DomResources14elementIncludeEv',
    )
    from . import DomResource
    return QList[DomResource]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setAttributeName(self, a: str) -> None:
    """
    Calls Qt's 'void DomResources::setAttributeName(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domresources.html#setAttributeName

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomResources::setAttributeName(const QString &a)
    self.uglySide.call(
        'ritual_ZN12DomResources16setAttributeNameERK7QString', a,
    )

  @overload(QList[DomResource])
  def setElementInclude(self, a: QList[DomResource]) -> None:
    """
    Calls Qt's 'void DomResources::setElementInclude(const QList<DomResource
    *> &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresources.html#setElementInclude

    Parameters
    ----------

    a : QList[DomResource]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomResources::setElementInclude(const QList<DomResource *> &a)
    self.uglySide.call(
        'ritual_ZN12DomResources17setElementIncludeERK5QListIP11DomResource'
        'E',
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
    Notes what was given, for Qt's 'DomResources::DomResources()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/domresources.html#DomResources
    """
    #  DomResources::DomResources()
    self._noteCreation(DomResources, lambda: Rituals.call(
        'ritual_ZN12DomResourcesC1Ev',
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
    Calls Qt's 'void DomResources::clearAttributeName()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresources.html#clearAttributeName
    """
    #  void DomResources::clearAttributeName()
    self.uglySide.call('ritual_ZN12DomResources18clearAttributeNameEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomResources::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomResources.read' has no cute function yet. Qt's 'void "
        "DomResources::read(QXmlStreamReader &reader)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomResources::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomResources.write' has no cute function yet. Qt's 'void "
        "DomResources::write(QXmlStreamWriter &writer, const QString "
        "&tagName) const': takes a type Python has no way to hand over yet.")
