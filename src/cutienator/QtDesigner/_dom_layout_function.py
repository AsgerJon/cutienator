"""
DomLayoutFunction binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomLayoutFunction to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class DomLayoutFunction(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomLayoutFunction: a plain Python object standing in
  front of one C++ DomLayoutFunction.

  What exists
  -----------

  Every function of Qt's DomLayoutFunction that has a ritual and that Python
  can call so far, 8 names in all: 'hasAttributeSpacing', 'attributeSpacing',
  'setAttributeSpacing', 'clearAttributeSpacing', 'hasAttributeMargin',
  'attributeMargin', 'setAttributeMargin', 'clearAttributeMargin'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomLayoutFunction::~DomLayoutFunction()': the destructor: Python
    never removes a C++ DomLayoutFunction.
  - Qt's 'void DomLayoutFunction::read(QXmlStreamReader &reader)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void DomLayoutFunction::write(QXmlStreamWriter &writer, const
    QString &tagName) const': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomLayoutFunction is created at the first use, not by
    'DomLayoutFunction(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomLayoutFunction.
  - Each name of Qt's DomLayoutFunction that has no cute function yet,
    'read', 'write', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DomLayoutFunction'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasAttributeSpacing(self) -> bool:
    """
    Calls Qt's 'bool DomLayoutFunction::hasAttributeSpacing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutfunction.html#hasAttributeSpacing
    """
    #  bool DomLayoutFunction::hasAttributeSpacing() const
    return self.uglySide.call(
        'ritual_ZNK17DomLayoutFunction19hasAttributeSpacingEv',
    )

  def attributeSpacing(self) -> str:
    """
    Calls Qt's 'QString DomLayoutFunction::attributeSpacing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutfunction.html#attributeSpacing

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomLayoutFunction::attributeSpacing() const
    return self.uglySide.call(
        'ritual_ZNK17DomLayoutFunction16attributeSpacingEv',
    )

  def hasAttributeMargin(self) -> bool:
    """
    Calls Qt's 'bool DomLayoutFunction::hasAttributeMargin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutfunction.html#hasAttributeMargin
    """
    #  bool DomLayoutFunction::hasAttributeMargin() const
    return self.uglySide.call(
        'ritual_ZNK17DomLayoutFunction18hasAttributeMarginEv',
    )

  def attributeMargin(self) -> str:
    """
    Calls Qt's 'QString DomLayoutFunction::attributeMargin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutfunction.html#attributeMargin

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomLayoutFunction::attributeMargin() const
    return self.uglySide.call(
        'ritual_ZNK17DomLayoutFunction15attributeMarginEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setAttributeSpacing(self, a: str) -> None:
    """
    Calls Qt's 'void DomLayoutFunction::setAttributeSpacing(const QString
    &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutfunction.html#setAttributeSpacing

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomLayoutFunction::setAttributeSpacing(const QString &a)
    self.uglySide.call(
        'ritual_ZN17DomLayoutFunction19setAttributeSpacingERK7QString', a,
    )

  @overload(str)
  def setAttributeMargin(self, a: str) -> None:
    """
    Calls Qt's 'void DomLayoutFunction::setAttributeMargin(const QString
    &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutfunction.html#setAttributeMargin

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomLayoutFunction::setAttributeMargin(const QString &a)
    self.uglySide.call(
        'ritual_ZN17DomLayoutFunction18setAttributeMarginERK7QString', a,
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
    Notes what was given, for Qt's 'DomLayoutFunction::DomLayoutFunction()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutfunction.html#DomLayoutFunction
    """
    #  DomLayoutFunction::DomLayoutFunction()
    self._noteCreation(DomLayoutFunction, lambda: Rituals.call(
        'ritual_ZN17DomLayoutFunctionC1Ev',
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

  def clearAttributeSpacing(self) -> None:
    """
    Calls Qt's 'void DomLayoutFunction::clearAttributeSpacing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutfunction.html#clearAttributeSpacing
    """
    #  void DomLayoutFunction::clearAttributeSpacing()
    self.uglySide.call(
        'ritual_ZN17DomLayoutFunction21clearAttributeSpacingEv',
    )

  def clearAttributeMargin(self) -> None:
    """
    Calls Qt's 'void DomLayoutFunction::clearAttributeMargin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutfunction.html#clearAttributeMargin
    """
    #  void DomLayoutFunction::clearAttributeMargin()
    self.uglySide.call(
        'ritual_ZN17DomLayoutFunction20clearAttributeMarginEv',
    )

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomLayoutFunction::read(QXmlStreamReader &reader)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomLayoutFunction.read' has no cute function yet. Qt's 'void "
        "DomLayoutFunction::read(QXmlStreamReader &reader)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomLayoutFunction::write(QXmlStreamWriter &writer, const
    QString &tagName) const': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'DomLayoutFunction.write' has no cute function yet. Qt's 'void "
        "DomLayoutFunction::write(QXmlStreamWriter &writer, const QString "
        "&tagName) const': takes a type Python has no way to hand over yet.")
