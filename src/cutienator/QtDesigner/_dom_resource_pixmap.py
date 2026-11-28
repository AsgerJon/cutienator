"""
DomResourcePixmap binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomResourcePixmap to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class DomResourcePixmap(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomResourcePixmap: a plain Python object standing in
  front of one C++ DomResourcePixmap.

  What exists
  -----------

  Every function of Qt's DomResourcePixmap that has a ritual and that Python
  can call so far, 10 names in all: 'text', 'setText',
  'hasAttributeResource', 'attributeResource', 'setAttributeResource',
  'clearAttributeResource', 'hasAttributeAlias', 'attributeAlias',
  'setAttributeAlias', 'clearAttributeAlias'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomResourcePixmap::~DomResourcePixmap()': the destructor: Python
    never removes a C++ DomResourcePixmap.
  - Qt's 'void DomResourcePixmap::read(QXmlStreamReader &reader)': takes a
    type Python has no way to hand over yet.
  - Qt's 'void DomResourcePixmap::write(QXmlStreamWriter &writer, const
    QString &tagName) const': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  4 of the 18 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomResourcePixmap is created at the first use, not by
    'DomResourcePixmap(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomResourcePixmap.
  - Each name of Qt's DomResourcePixmap that has no cute function yet,
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
  __qt_class__ = 'DomResourcePixmap'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def text(self) -> str:
    """
    Calls Qt's 'QString DomResourcePixmap::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/domresourcepixmap.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomResourcePixmap::text() const
    return self.uglySide.call('ritual_ZNK17DomResourcePixmap4textEv')

  def hasAttributeResource(self) -> bool:
    """
    Calls Qt's 'bool DomResourcePixmap::hasAttributeResource() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourcepixmap.html#hasAttributeResource
    """
    #  bool DomResourcePixmap::hasAttributeResource() const
    return self.uglySide.call(
        'ritual_ZNK17DomResourcePixmap20hasAttributeResourceEv',
    )

  def attributeResource(self) -> str:
    """
    Calls Qt's 'QString DomResourcePixmap::attributeResource() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourcepixmap.html#attributeResource

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomResourcePixmap::attributeResource() const
    return self.uglySide.call(
        'ritual_ZNK17DomResourcePixmap17attributeResourceEv',
    )

  def hasAttributeAlias(self) -> bool:
    """
    Calls Qt's 'bool DomResourcePixmap::hasAttributeAlias() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourcepixmap.html#hasAttributeAlias
    """
    #  bool DomResourcePixmap::hasAttributeAlias() const
    return self.uglySide.call(
        'ritual_ZNK17DomResourcePixmap17hasAttributeAliasEv',
    )

  def attributeAlias(self) -> str:
    """
    Calls Qt's 'QString DomResourcePixmap::attributeAlias() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourcepixmap.html#attributeAlias

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomResourcePixmap::attributeAlias() const
    return self.uglySide.call(
        'ritual_ZNK17DomResourcePixmap14attributeAliasEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setText(self, s: str) -> None:
    """
    Calls Qt's 'void DomResourcePixmap::setText(const QString &s)'.

    Qt's own words: https://doc.qt.io/qt-6/domresourcepixmap.html#setText

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomResourcePixmap::setText(const QString &s)
    self.uglySide.call('ritual_ZN17DomResourcePixmap7setTextERK7QString', s)

  @overload(str)
  def setAttributeResource(self, a: str) -> None:
    """
    Calls Qt's 'void DomResourcePixmap::setAttributeResource(const QString
    &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourcepixmap.html#setAttributeResource

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomResourcePixmap::setAttributeResource(const QString &a)
    self.uglySide.call(
        'ritual_ZN17DomResourcePixmap20setAttributeResourceERK7QString', a,
    )

  @overload(str)
  def setAttributeAlias(self, a: str) -> None:
    """
    Calls Qt's 'void DomResourcePixmap::setAttributeAlias(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourcepixmap.html#setAttributeAlias

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomResourcePixmap::setAttributeAlias(const QString &a)
    self.uglySide.call(
        'ritual_ZN17DomResourcePixmap17setAttributeAliasERK7QString', a,
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
    Notes what was given, for Qt's 'DomResourcePixmap::DomResourcePixmap()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourcepixmap.html#DomResourcePixmap
    """
    #  DomResourcePixmap::DomResourcePixmap()
    self._noteCreation(DomResourcePixmap, lambda: Rituals.call(
        'ritual_ZN17DomResourcePixmapC1Ev',
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

  def clearAttributeResource(self) -> None:
    """
    Calls Qt's 'void DomResourcePixmap::clearAttributeResource()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourcepixmap.html#clearAttributeResource
    """
    #  void DomResourcePixmap::clearAttributeResource()
    self.uglySide.call(
        'ritual_ZN17DomResourcePixmap22clearAttributeResourceEv',
    )

  def clearAttributeAlias(self) -> None:
    """
    Calls Qt's 'void DomResourcePixmap::clearAttributeAlias()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domresourcepixmap.html#clearAttributeAlias
    """
    #  void DomResourcePixmap::clearAttributeAlias()
    self.uglySide.call('ritual_ZN17DomResourcePixmap19clearAttributeAliasEv')

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomResourcePixmap::read(QXmlStreamReader &reader)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomResourcePixmap.read' has no cute function yet. Qt's 'void "
        "DomResourcePixmap::read(QXmlStreamReader &reader)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomResourcePixmap::write(QXmlStreamWriter &writer, const
    QString &tagName) const': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'DomResourcePixmap.write' has no cute function yet. Qt's 'void "
        "DomResourcePixmap::write(QXmlStreamWriter &writer, const QString "
        "&tagName) const': takes a type Python has no way to hand over yet.")
