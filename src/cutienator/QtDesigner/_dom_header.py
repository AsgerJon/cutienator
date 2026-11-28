"""
DomHeader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomHeader to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class DomHeader(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomHeader: a plain Python object standing in front of
  one C++ DomHeader.

  What exists
  -----------

  Every function of Qt's DomHeader that has a ritual and that Python can call
  so far, 6 names in all: 'text', 'setText', 'hasAttributeLocation',
  'attributeLocation', 'setAttributeLocation', 'clearAttributeLocation'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomHeader::~DomHeader()': the destructor: Python never removes a
    C++ DomHeader.
  - Qt's 'void DomHeader::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void DomHeader::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 14 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomHeader is created at the first use, not by 'DomHeader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomHeader.
  - Each name of Qt's DomHeader that has no cute function yet, 'read',
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
  __qt_class__ = 'DomHeader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def text(self) -> str:
    """
    Calls Qt's 'QString DomHeader::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/domheader.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomHeader::text() const
    return self.uglySide.call('ritual_ZNK9DomHeader4textEv')

  def hasAttributeLocation(self) -> bool:
    """
    Calls Qt's 'bool DomHeader::hasAttributeLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domheader.html#hasAttributeLocation
    """
    #  bool DomHeader::hasAttributeLocation() const
    return self.uglySide.call('ritual_ZNK9DomHeader20hasAttributeLocationEv')

  def attributeLocation(self) -> str:
    """
    Calls Qt's 'QString DomHeader::attributeLocation() const'.

    Qt's own words: https://doc.qt.io/qt-6/domheader.html#attributeLocation

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomHeader::attributeLocation() const
    return self.uglySide.call('ritual_ZNK9DomHeader17attributeLocationEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setText(self, s: str) -> None:
    """
    Calls Qt's 'void DomHeader::setText(const QString &s)'.

    Qt's own words: https://doc.qt.io/qt-6/domheader.html#setText

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomHeader::setText(const QString &s)
    self.uglySide.call('ritual_ZN9DomHeader7setTextERK7QString', s)

  @overload(str)
  def setAttributeLocation(self, a: str) -> None:
    """
    Calls Qt's 'void DomHeader::setAttributeLocation(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domheader.html#setAttributeLocation

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomHeader::setAttributeLocation(const QString &a)
    self.uglySide.call(
        'ritual_ZN9DomHeader20setAttributeLocationERK7QString', a,
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
    Notes what was given, for Qt's 'DomHeader::DomHeader()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/domheader.html#DomHeader
    """
    #  DomHeader::DomHeader()
    self._noteCreation(DomHeader, lambda: Rituals.call(
        'ritual_ZN9DomHeaderC1Ev',
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

  def clearAttributeLocation(self) -> None:
    """
    Calls Qt's 'void DomHeader::clearAttributeLocation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domheader.html#clearAttributeLocation
    """
    #  void DomHeader::clearAttributeLocation()
    self.uglySide.call('ritual_ZN9DomHeader22clearAttributeLocationEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomHeader::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomHeader.read' has no cute function yet. Qt's 'void "
        "DomHeader::read(QXmlStreamReader &reader)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomHeader::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomHeader.write' has no cute function yet. Qt's 'void "
        "DomHeader::write(QXmlStreamWriter &writer, const QString &tagName) "
        "const': takes a type Python has no way to hand over yet.")
