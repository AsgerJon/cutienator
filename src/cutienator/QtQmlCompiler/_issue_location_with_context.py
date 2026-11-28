"""
IssueLocationWithContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljslogger_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means IssueLocationWithContext to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtQml import QQmlJS


class IssueLocationWithContext(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's IssueLocationWithContext: a plain Python object
  standing in front of one C++ IssueLocationWithContext.

  C++ hands a IssueLocationWithContext around as a copy, so every C++
  IssueLocationWithContext behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's IssueLocationWithContext that has a ritual and that
  Python can call so far, 3 names in all: 'beforeText', 'issueText',
  'afterText'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'IssueLocationWithContext::~IssueLocationWithContext()': the
    destructor: Python removes its C++ IssueLocationWithContext by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ IssueLocationWithContext is created at the first use, not by
    'IssueLocationWithContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a IssueLocationWithContext back gives a copy the ritual
    made for Python, in a new cute IssueLocationWithContext.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'IssueLocationWithContext'

  #  Qt's '~IssueLocationWithContext()'. Naming it makes this a value class:
  #  Python owns every C++ IssueLocationWithContext behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN24IssueLocationWithContextD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def beforeText(self) -> str:
    """
    Calls Qt's 'QStringView IssueLocationWithContext::beforeText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/issuelocationwithcontext.html#beforeText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView IssueLocationWithContext::beforeText() const
    return self.uglySide.call(
        'ritual_ZNK24IssueLocationWithContext10beforeTextEv',
    )

  def issueText(self) -> str:
    """
    Calls Qt's 'QStringView IssueLocationWithContext::issueText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/issuelocationwithcontext.html#issueText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView IssueLocationWithContext::issueText() const
    return self.uglySide.call(
        'ritual_ZNK24IssueLocationWithContext9issueTextEv',
    )

  def afterText(self) -> str:
    """
    Calls Qt's 'QStringView IssueLocationWithContext::afterText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/issuelocationwithcontext.html#afterText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView IssueLocationWithContext::afterText() const
    return self.uglySide.call(
        'ritual_ZNK24IssueLocationWithContext9afterTextEv',
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

  @overload(str, WAIT['QQmlJS.SourceLocation'])
  def __init__(self, code: str, location: QQmlJS.SourceLocation) -> None:
    """
    Notes what was given, for Qt's
    'IssueLocationWithContext::IssueLocationWithContext(QStringView code,
    const QQmlJS::SourceLocation &location)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/issuelocationwithcontext.html

    Parameters
    ----------

    code : str
      Passed on as it is: a QString is made of it for the call.

    location : QQmlJS.SourceLocation
      Passed on as a value: Qt reads the C++ QQmlJS::SourceLocation, which
      stays Python's own.
    """
    #  IssueLocationWithContext::IssueLocationWithContext(QStringView code,
    #      const QQmlJS::SourceLocation &location)
    self._noteCreation(IssueLocationWithContext, lambda: Rituals.call(
        'ritual_ZN24IssueLocationWithContextC1E11QStringViewRKN6QQmlJS14Sou'
        'rceLocationE',
        code, self._valueOf(location),
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
