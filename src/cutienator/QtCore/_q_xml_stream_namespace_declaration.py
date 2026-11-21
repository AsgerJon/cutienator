"""
QXmlStreamNamespaceDeclaration binding of the Qt C++
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


class QXmlStreamNamespaceDeclaration(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QXmlStreamNamespaceDeclaration: a plain Python object
  standing in front of one C++ QXmlStreamNamespaceDeclaration.

  C++ hands a QXmlStreamNamespaceDeclaration around as a copy, so every C++
  QXmlStreamNamespaceDeclaration behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QXmlStreamNamespaceDeclaration that has a ritual and
  that Python can call so far, 2 names in all: 'prefix', 'namespaceUri'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QXmlStreamNamespaceDeclaration::~QXmlStreamNamespaceDeclaration()':
    the destructor: Python removes its C++ QXmlStreamNamespaceDeclaration by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QXmlStreamNamespaceDeclaration is created at the first use, not
    by 'QXmlStreamNamespaceDeclaration(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QXmlStreamNamespaceDeclaration back gives a copy the
    ritual made for Python, in a new cute QXmlStreamNamespaceDeclaration.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXmlStreamNamespaceDeclaration'

  #  Qt's '~QXmlStreamNamespaceDeclaration()'. Naming it makes this a value
  #  class: Python owns every C++ QXmlStreamNamespaceDeclaration behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN30QXmlStreamNamespaceDeclarationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def prefix(self) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamNamespaceDeclaration::prefix() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamnamespacedeclaration.html#prefix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamNamespaceDeclaration::prefix() const
    return self.uglySide.call(
        'ritual_ZNK30QXmlStreamNamespaceDeclaration6prefixEv',
    )

  def namespaceUri(self) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamNamespaceDeclaration::namespaceUri()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamnamespacedeclaration.html#namespaceUri

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamNamespaceDeclaration::namespaceUri() const
    return self.uglySide.call(
        'ritual_ZNK30QXmlStreamNamespaceDeclaration12namespaceUriEv',
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
    'QXmlStreamNamespaceDeclaration::QXmlStreamNamespaceDeclaration()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamnamespacedeclaration.html
    """
    #  QXmlStreamNamespaceDeclaration::QXmlStreamNamespaceDeclaration()
    self._noteCreation(QXmlStreamNamespaceDeclaration, lambda: Rituals.call(
        'ritual_ZN30QXmlStreamNamespaceDeclarationC1Ev',
    ))

  @overload(str, str)
  def __init__(self, prefix: str, namespaceUri: str) -> None:
    """
    Notes what was given, for Qt's
    'QXmlStreamNamespaceDeclaration::QXmlStreamNamespaceDeclaration(const
    QString &prefix, const QString &namespaceUri)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamnamespacedeclaration.html

    Parameters
    ----------

    prefix : str
      Passed on as it is: a QString is made of it for the call.

    namespaceUri : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QXmlStreamNamespaceDeclaration::QXmlStreamNamespaceDeclaration(const
    #      QString &prefix, const QString &namespaceUri)
    self._noteCreation(QXmlStreamNamespaceDeclaration, lambda: Rituals.call(
        'ritual_ZN30QXmlStreamNamespaceDeclarationC1ERK7QStringS2_',
        prefix, namespaceUri,
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
