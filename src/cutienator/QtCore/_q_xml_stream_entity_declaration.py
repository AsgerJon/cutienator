"""
QXmlStreamEntityDeclaration binding of the Qt C++
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


class QXmlStreamEntityDeclaration(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QXmlStreamEntityDeclaration: a plain Python object
  standing in front of one C++ QXmlStreamEntityDeclaration.

  C++ hands a QXmlStreamEntityDeclaration around as a copy, so every C++
  QXmlStreamEntityDeclaration behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QXmlStreamEntityDeclaration that has a ritual and
  that Python can call so far, 5 names in all: 'name', 'notationName',
  'systemId', 'publicId', 'value'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QXmlStreamEntityDeclaration::~QXmlStreamEntityDeclaration()': the
    destructor: Python removes its C++ QXmlStreamEntityDeclaration by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QXmlStreamEntityDeclaration is created at the first use, not by
    'QXmlStreamEntityDeclaration(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QXmlStreamEntityDeclaration back gives a copy the
    ritual made for Python, in a new cute QXmlStreamEntityDeclaration.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXmlStreamEntityDeclaration'

  #  Qt's '~QXmlStreamEntityDeclaration()'. Naming it makes this a value
  #  class: Python owns every C++ QXmlStreamEntityDeclaration behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN27QXmlStreamEntityDeclarationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamEntityDeclaration::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamentitydeclaration.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamEntityDeclaration::name() const
    return self.uglySide.call(
        'ritual_ZNK27QXmlStreamEntityDeclaration4nameEv',
    )

  def notationName(self) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamEntityDeclaration::notationName()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamentitydeclaration.html#notationName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamEntityDeclaration::notationName() const
    return self.uglySide.call(
        'ritual_ZNK27QXmlStreamEntityDeclaration12notationNameEv',
    )

  def systemId(self) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamEntityDeclaration::systemId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamentitydeclaration.html#systemId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamEntityDeclaration::systemId() const
    return self.uglySide.call(
        'ritual_ZNK27QXmlStreamEntityDeclaration8systemIdEv',
    )

  def publicId(self) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamEntityDeclaration::publicId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamentitydeclaration.html#publicId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamEntityDeclaration::publicId() const
    return self.uglySide.call(
        'ritual_ZNK27QXmlStreamEntityDeclaration8publicIdEv',
    )

  def value(self) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamEntityDeclaration::value() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamentitydeclaration.html#value

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamEntityDeclaration::value() const
    return self.uglySide.call(
        'ritual_ZNK27QXmlStreamEntityDeclaration5valueEv',
    )

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
    'QXmlStreamEntityDeclaration::QXmlStreamEntityDeclaration()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamentitydeclaration.html
    """
    #  QXmlStreamEntityDeclaration::QXmlStreamEntityDeclaration()
    self._noteCreation(QXmlStreamEntityDeclaration, lambda: Rituals.call(
        'ritual_ZN27QXmlStreamEntityDeclarationC1Ev',
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
