"""
QXmlStreamAttribute binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qxmlstream.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QXmlStreamAttribute(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QXmlStreamAttribute: a plain Python object standing
  in front of one C++ QXmlStreamAttribute.

  C++ hands a QXmlStreamAttribute around as a copy, so every C++
  QXmlStreamAttribute behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QXmlStreamAttribute that has a ritual and that
  Python can call so far, 6 names in all: 'namespaceUri', 'name',
  'qualifiedName', 'prefix', 'value', 'isDefault'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QXmlStreamAttribute::~QXmlStreamAttribute()': the destructor:
    Python removes its C++ QXmlStreamAttribute by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QXmlStreamAttribute is created at the first use, not by
    'QXmlStreamAttribute(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QXmlStreamAttribute back gives a copy the ritual made
    for Python, in a new cute QXmlStreamAttribute.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXmlStreamAttribute'

  #  Qt's '~QXmlStreamAttribute()'. Naming it makes this a value class:
  #  Python owns every C++ QXmlStreamAttribute behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QXmlStreamAttributeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def namespaceUri(self) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamAttribute::namespaceUri() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamattribute.html#namespaceUri

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamAttribute::namespaceUri() const
    return self.uglySide.call(
        'ritual_ZNK19QXmlStreamAttribute12namespaceUriEv',
    )

  def name(self) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamAttribute::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamattribute.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamAttribute::name() const
    return self.uglySide.call('ritual_ZNK19QXmlStreamAttribute4nameEv')

  def qualifiedName(self) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamAttribute::qualifiedName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamattribute.html#qualifiedName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamAttribute::qualifiedName() const
    return self.uglySide.call(
        'ritual_ZNK19QXmlStreamAttribute13qualifiedNameEv',
    )

  def prefix(self) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamAttribute::prefix() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamattribute.html#prefix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamAttribute::prefix() const
    return self.uglySide.call('ritual_ZNK19QXmlStreamAttribute6prefixEv')

  def value(self) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamAttribute::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamattribute.html#value

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamAttribute::value() const
    return self.uglySide.call('ritual_ZNK19QXmlStreamAttribute5valueEv')

  def isDefault(self) -> bool:
    """
    Calls Qt's 'bool QXmlStreamAttribute::isDefault() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamattribute.html#isDefault
    """
    #  bool QXmlStreamAttribute::isDefault() const
    return self.uglySide.call('ritual_ZNK19QXmlStreamAttribute9isDefaultEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'QXmlStreamAttribute::QXmlStreamAttribute()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamattribute.html#QXmlStreamAttribute
    """
    #  QXmlStreamAttribute::QXmlStreamAttribute()
    self._noteCreation(QXmlStreamAttribute, lambda: Rituals.call(
        'ritual_ZN19QXmlStreamAttributeC1Ev',
    ))

  @overload(str, str)
  def __init__(self, qualifiedName: str, value: str) -> None:
    """
    Notes what was given, for Qt's
    'QXmlStreamAttribute::QXmlStreamAttribute(const QString &qualifiedName,
    const QString &value)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamattribute.html#QXmlStreamAttribute

    Parameters
    ----------

    qualifiedName : str
      Passed on as it is: a QString is made of it for the call.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QXmlStreamAttribute::QXmlStreamAttribute(const QString &qualifiedName,
    #      const QString &value)
    self._noteCreation(QXmlStreamAttribute, lambda: Rituals.call(
        'ritual_ZN19QXmlStreamAttributeC1ERK7QStringS2_',
        qualifiedName, value,
    ))

  @overload(str, str, str)
  def __init__(self, namespaceUri: str, name: str, value: str) -> None:
    """
    Notes what was given, for Qt's
    'QXmlStreamAttribute::QXmlStreamAttribute(const QString &namespaceUri,
    const QString &name, const QString &value)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamattribute.html#QXmlStreamAttribute

    Parameters
    ----------

    namespaceUri : str
      Passed on as it is: a QString is made of it for the call.

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QXmlStreamAttribute::QXmlStreamAttribute(const QString &namespaceUri,
    #      const QString &name, const QString &value)
    self._noteCreation(QXmlStreamAttribute, lambda: Rituals.call(
        'ritual_ZN19QXmlStreamAttributeC1ERK7QStringS2_S2_',
        namespaceUri, name, value,
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
