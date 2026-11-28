"""
DomPropertySpecifications binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomPropertySpecifications to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import DomPropertyToolTip, DomStringPropertySpecification
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomPropertyToolTip = WAIT['DomPropertyToolTip']
  DomStringPropertySpecification = WAIT['DomStringPropertySpecification']


class DomPropertySpecifications(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomPropertySpecifications: a plain Python object
  standing in front of one C++ DomPropertySpecifications.

  What exists
  -----------

  Every function of Qt's DomPropertySpecifications that has a ritual and that
  Python can call so far, 4 names in all: 'elementTooltip',
  'setElementTooltip', 'elementStringpropertyspecification',
  'setElementStringpropertyspecification'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomPropertySpecifications::~DomPropertySpecifications()': the
    destructor: Python never removes a C++ DomPropertySpecifications.
  - Qt's 'void DomPropertySpecifications::read(QXmlStreamReader &reader)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void DomPropertySpecifications::write(QXmlStreamWriter &writer,
    const QString &tagName) const': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomPropertySpecifications is created at the first use, not by
    'DomPropertySpecifications(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomPropertySpecifications.
  - Each name of Qt's DomPropertySpecifications that has no cute function
    yet, 'read', 'write', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DomPropertySpecifications'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def elementTooltip(self) -> QList[DomPropertyToolTip]:
    """
    Calls Qt's 'QList<DomPropertyToolTip *>
    DomPropertySpecifications::elementTooltip() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/dompropertyspecifications.html#elementTooltip

    Returns
    -------

    QList[DomPropertyToolTip]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomPropertyToolTip *>
    #      DomPropertySpecifications::elementTooltip() const
    address = self.uglySide.call(
        'ritual_ZNK25DomPropertySpecifications14elementTooltipEv',
    )
    from . import DomPropertyToolTip
    return QList[DomPropertyToolTip]._cuteOwning(address)

  def elementStringpropertyspecification(
      self,
  ) -> QList[DomStringPropertySpecification]:
    """
    Calls Qt's 'QList<DomStringPropertySpecification *>
    DomPropertySpecifications::elementStringpropertyspecification() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/dompropertyspecifications.html

    Returns
    -------

    QList[DomStringPropertySpecification]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomStringPropertySpecification *>
    #      DomPropertySpecifications::elementStringpropertyspecification()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK25DomPropertySpecifications34elementStringpropertyspecif'
        'icationEv',
    )
    from . import DomStringPropertySpecification
    return QList[DomStringPropertySpecification]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[DomPropertyToolTip])
  def setElementTooltip(self, a: QList[DomPropertyToolTip]) -> None:
    """
    Calls Qt's 'void DomPropertySpecifications::setElementTooltip(const
    QList<DomPropertyToolTip *> &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/dompropertyspecifications.html#setElementTooltip

    Parameters
    ----------

    a : QList[DomPropertyToolTip]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomPropertySpecifications::setElementTooltip(const
    #      QList<DomPropertyToolTip *> &a)
    self.uglySide.call(
        'ritual_ZN25DomPropertySpecifications17setElementTooltipERK5QListIP'
        '18DomPropertyToolTipE',
        self._valueOf(a),
    )

  @overload(QList[DomStringPropertySpecification])
  def setElementStringpropertyspecification(
      self,
      a: QList[DomStringPropertySpecification],
  ) -> None:
    """
    Calls Qt's 'void
    DomPropertySpecifications::setElementStringpropertyspecification(const
    QList<DomStringPropertySpecification *> &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/dompropertyspecifications.html

    Parameters
    ----------

    a : QList[DomStringPropertySpecification]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomPropertySpecifications::setElementStringpropertyspecification(
    #      const QList<DomStringPropertySpecification *> &a)
    self.uglySide.call(
        'ritual_ZN25DomPropertySpecifications37setElementStringpropertyspec'
        'ificationERK5QListIP30DomStringPropertySpecificationE',
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
    Notes what was given, for Qt's
    'DomPropertySpecifications::DomPropertySpecifications()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/dompropertyspecifications.html
    """
    #  DomPropertySpecifications::DomPropertySpecifications()
    self._noteCreation(DomPropertySpecifications, lambda: Rituals.call(
        'ritual_ZN25DomPropertySpecificationsC1Ev',
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

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomPropertySpecifications::read(QXmlStreamReader &reader)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomPropertySpecifications.read' has no cute function yet. Qt's "
        "'void DomPropertySpecifications::read(QXmlStreamReader &reader)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomPropertySpecifications::write(QXmlStreamWriter &writer,
    const QString &tagName) const': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'DomPropertySpecifications.write' has no cute function yet. Qt's "
        "'void DomPropertySpecifications::write(QXmlStreamWriter &writer, "
        "const QString &tagName) const': takes a type Python has no way to "
        "hand over yet.")
