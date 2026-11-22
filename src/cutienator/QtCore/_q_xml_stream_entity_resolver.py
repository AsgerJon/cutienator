"""
QXmlStreamEntityResolver binding of the Qt C++
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


class QXmlStreamEntityResolver(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QXmlStreamEntityResolver: a plain Python object
  standing in front of one C++ QXmlStreamEntityResolver.

  What exists
  -----------

  Every function of Qt's QXmlStreamEntityResolver that has a ritual and that
  Python can call so far, 2 names in all: 'resolveEntity',
  'resolveUndeclaredEntity'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QXmlStreamEntityResolver::~QXmlStreamEntityResolver()': the
    destructor: Python never removes a C++ QXmlStreamEntityResolver.

  What has no ritual
  ------------------

  4 of the 8 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QXmlStreamEntityResolver is created at the first use, not by
    'QXmlStreamEntityResolver(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QXmlStreamEntityResolver.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXmlStreamEntityResolver'

  #  A C++ QXmlStreamEntityResolver Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QXmlStreamEntityResolver'

  #  The functions Qt calls itself that QXmlStreamEntityResolver is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'resolveUndeclaredEntity': (
          ('_ZN24QXmlStreamEntityResolver23resolveUndeclaredEntityERK7QStri'
           'ng',
           ('address', 'text', ''),
           (
               ('address', 'text', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'QXmlStreamEntityResolver::QXmlStreamEntityResolver()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamentityresolver.html
    """
    #  QXmlStreamEntityResolver::QXmlStreamEntityResolver()
    self._noteCreation(QXmlStreamEntityResolver, lambda: Rituals.call(
        'ritual_ZN24QXmlStreamEntityResolverC1Ev',
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

  @overload(str, str)
  def resolveEntity(self, publicId: str, systemId: str) -> str:
    """
    Calls Qt's 'QString QXmlStreamEntityResolver::resolveEntity(const QString
    &publicId, const QString &systemId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamentityresolver.html#resolveEntity

    Parameters
    ----------

    publicId : str
      Passed on as it is: a QString is made of it for the call.

    systemId : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlStreamEntityResolver::resolveEntity(const QString
    #      &publicId, const QString &systemId)
    return self.uglySide.call(
        'ritual_ZN24QXmlStreamEntityResolver13resolveEntityERK7QStringS2_',
        publicId, systemId,
    )

  @overload(str)
  def resolveUndeclaredEntity(self, name: str) -> str:
    """
    Calls Qt's 'QString
    QXmlStreamEntityResolver::resolveUndeclaredEntity(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamentityresolver.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlStreamEntityResolver::resolveUndeclaredEntity(const
    #      QString &name)
    ritual = (
        'ritual_ZN24QXmlStreamEntityResolver23resolveUndeclaredEntityERK7QS'
        'tring')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QXmlStreamEntityResolver23resolveUndeclaredEntity'
          'ERK7QString')
    return self.uglySide.call(ritual, name)
