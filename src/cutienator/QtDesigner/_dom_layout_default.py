"""
DomLayoutDefault binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomLayoutDefault to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class DomLayoutDefault(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomLayoutDefault: a plain Python object standing in
  front of one C++ DomLayoutDefault.

  What exists
  -----------

  Every function of Qt's DomLayoutDefault that has a ritual and that Python
  can call so far, 8 names in all: 'hasAttributeSpacing', 'attributeSpacing',
  'setAttributeSpacing', 'clearAttributeSpacing', 'hasAttributeMargin',
  'attributeMargin', 'setAttributeMargin', 'clearAttributeMargin'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomLayoutDefault::~DomLayoutDefault()': the destructor: Python
    never removes a C++ DomLayoutDefault.
  - Qt's 'void DomLayoutDefault::read(QXmlStreamReader &reader)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void DomLayoutDefault::write(QXmlStreamWriter &writer, const
    QString &tagName) const': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomLayoutDefault is created at the first use, not by
    'DomLayoutDefault(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomLayoutDefault.
  - Each name of Qt's DomLayoutDefault that has no cute function yet, 'read',
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
  __qt_class__ = 'DomLayoutDefault'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasAttributeSpacing(self) -> bool:
    """
    Calls Qt's 'bool DomLayoutDefault::hasAttributeSpacing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutdefault.html#hasAttributeSpacing
    """
    #  bool DomLayoutDefault::hasAttributeSpacing() const
    return self.uglySide.call(
        'ritual_ZNK16DomLayoutDefault19hasAttributeSpacingEv',
    )

  def attributeSpacing(self) -> int:
    """
    Calls Qt's 'int DomLayoutDefault::attributeSpacing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutdefault.html#attributeSpacing
    """
    #  int DomLayoutDefault::attributeSpacing() const
    return self.uglySide.call(
        'ritual_ZNK16DomLayoutDefault16attributeSpacingEv',
    )

  def hasAttributeMargin(self) -> bool:
    """
    Calls Qt's 'bool DomLayoutDefault::hasAttributeMargin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutdefault.html#hasAttributeMargin
    """
    #  bool DomLayoutDefault::hasAttributeMargin() const
    return self.uglySide.call(
        'ritual_ZNK16DomLayoutDefault18hasAttributeMarginEv',
    )

  def attributeMargin(self) -> int:
    """
    Calls Qt's 'int DomLayoutDefault::attributeMargin() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutdefault.html#attributeMargin
    """
    #  int DomLayoutDefault::attributeMargin() const
    return self.uglySide.call(
        'ritual_ZNK16DomLayoutDefault15attributeMarginEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setAttributeSpacing(self, a: int) -> None:
    """
    Calls Qt's 'void DomLayoutDefault::setAttributeSpacing(int a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutdefault.html#setAttributeSpacing

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomLayoutDefault::setAttributeSpacing(int a)
    self.uglySide.call(
        'ritual_ZN16DomLayoutDefault19setAttributeSpacingEi', a,
    )

  @overload(int)
  def setAttributeMargin(self, a: int) -> None:
    """
    Calls Qt's 'void DomLayoutDefault::setAttributeMargin(int a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutdefault.html#setAttributeMargin

    Parameters
    ----------

    a : int
      Passed on as it is.
    """
    #  void DomLayoutDefault::setAttributeMargin(int a)
    self.uglySide.call(
        'ritual_ZN16DomLayoutDefault18setAttributeMarginEi', a,
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
    Notes what was given, for Qt's 'DomLayoutDefault::DomLayoutDefault()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutdefault.html#DomLayoutDefault
    """
    #  DomLayoutDefault::DomLayoutDefault()
    self._noteCreation(DomLayoutDefault, lambda: Rituals.call(
        'ritual_ZN16DomLayoutDefaultC1Ev',
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
    Calls Qt's 'void DomLayoutDefault::clearAttributeSpacing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutdefault.html#clearAttributeSpacing
    """
    #  void DomLayoutDefault::clearAttributeSpacing()
    self.uglySide.call(
        'ritual_ZN16DomLayoutDefault21clearAttributeSpacingEv',
    )

  def clearAttributeMargin(self) -> None:
    """
    Calls Qt's 'void DomLayoutDefault::clearAttributeMargin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domlayoutdefault.html#clearAttributeMargin
    """
    #  void DomLayoutDefault::clearAttributeMargin()
    self.uglySide.call('ritual_ZN16DomLayoutDefault20clearAttributeMarginEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomLayoutDefault::read(QXmlStreamReader &reader)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomLayoutDefault.read' has no cute function yet. Qt's 'void "
        "DomLayoutDefault::read(QXmlStreamReader &reader)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomLayoutDefault::write(QXmlStreamWriter &writer, const
    QString &tagName) const': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'DomLayoutDefault.write' has no cute function yet. Qt's 'void "
        "DomLayoutDefault::write(QXmlStreamWriter &writer, const QString "
        "&tagName) const': takes a type Python has no way to hand over yet.")
