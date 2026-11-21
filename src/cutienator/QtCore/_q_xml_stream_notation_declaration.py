"""
QXmlStreamNotationDeclaration binding of the Qt C++
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


class QXmlStreamNotationDeclaration(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QXmlStreamNotationDeclaration: a plain Python object
  standing in front of one C++ QXmlStreamNotationDeclaration.

  C++ hands a QXmlStreamNotationDeclaration around as a copy, so every C++
  QXmlStreamNotationDeclaration behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QXmlStreamNotationDeclaration that has a ritual and
  that Python can call so far, 3 names in all: 'name', 'systemId',
  'publicId'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QXmlStreamNotationDeclaration::~QXmlStreamNotationDeclaration()':
    the destructor: Python removes its C++ QXmlStreamNotationDeclaration by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QXmlStreamNotationDeclaration is created at the first use, not by
    'QXmlStreamNotationDeclaration(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QXmlStreamNotationDeclaration back gives a copy the
    ritual made for Python, in a new cute QXmlStreamNotationDeclaration.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXmlStreamNotationDeclaration'

  #  Qt's '~QXmlStreamNotationDeclaration()'. Naming it makes this a value
  #  class: Python owns every C++ QXmlStreamNotationDeclaration behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN29QXmlStreamNotationDeclarationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamNotationDeclaration::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamnotationdeclaration.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamNotationDeclaration::name() const
    return self.uglySide.call(
        'ritual_ZNK29QXmlStreamNotationDeclaration4nameEv',
    )

  def systemId(self) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamNotationDeclaration::systemId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamnotationdeclaration.html#systemId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamNotationDeclaration::systemId() const
    return self.uglySide.call(
        'ritual_ZNK29QXmlStreamNotationDeclaration8systemIdEv',
    )

  def publicId(self) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamNotationDeclaration::publicId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamnotationdeclaration.html#publicId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamNotationDeclaration::publicId() const
    return self.uglySide.call(
        'ritual_ZNK29QXmlStreamNotationDeclaration8publicIdEv',
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
    'QXmlStreamNotationDeclaration::QXmlStreamNotationDeclaration()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamnotationdeclaration.html
    """
    #  QXmlStreamNotationDeclaration::QXmlStreamNotationDeclaration()
    self._noteCreation(QXmlStreamNotationDeclaration, lambda: Rituals.call(
        'ritual_ZN29QXmlStreamNotationDeclarationC1Ev',
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
