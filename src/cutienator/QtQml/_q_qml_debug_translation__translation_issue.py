"""
QQmlDebugTranslation::TranslationIssue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmldebugtranslationprotocol_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlDebugTranslation::TranslationIssue to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals


class TranslationIssue(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlDebugTranslation::TranslationIssue: a plain
  Python object standing in front of one C++
  QQmlDebugTranslation::TranslationIssue.

  C++ hands a QQmlDebugTranslation::TranslationIssue around as a copy, so
  every C++ QQmlDebugTranslation::TranslationIssue behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlDebugTranslation::TranslationIssue that has a
  ritual and that Python can call so far, 2 names in all: '__eq__',
  'toDebugString'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDataStream &operator>>(QDataStream &stream, TranslationIssue
    &issue)': an operator between other classes, written inside this one.
  - Qt's 'QDataStream &operator<<(QDataStream &stream, const TranslationIssue
    &issue)': takes a type Python has no way to hand over yet.
  - Qt's 'QQmlDebugTranslation::TranslationIssue::~TranslationIssue()': the
    destructor: Python removes its C++ QQmlDebugTranslation::TranslationIssue
    by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlDebugTranslation::TranslationIssue is created at the first
    use, not by 'QQmlDebugTranslation::TranslationIssue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlDebugTranslation::TranslationIssue back gives a
    copy the ritual made for Python, in a new cute
    QQmlDebugTranslation::TranslationIssue.
  """

  #  The enums Qt writes inside QQmlDebugTranslation::TranslationIssue, each
  #  a class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class Type(CuteNum, scoped=True):
    """
    The enum 'QQmlDebugTranslation::TranslationIssue::Type' of Qt, with the 2
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    Missing = Kee[int](0)
    Elided = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlDebugTranslation::TranslationIssue'

  #  Qt's '~QQmlDebugTranslation::TranslationIssue()'. Naming it makes this a
  #  value class: Python owns every C++
  #  QQmlDebugTranslation::TranslationIssue behind a cute one, and removes it
  #  by this ritual.
  __delete_ritual__ = 'ritual_ZN20QQmlDebugTranslation16TranslationIssueD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def toDebugString(self) -> str:
    """
    Calls Qt's 'QString
    QQmlDebugTranslation::TranslationIssue::toDebugString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugtranslation-translationissue.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlDebugTranslation::TranslationIssue::toDebugString() const
    return self.uglySide.call(
        'ritual_ZNK20QQmlDebugTranslation16TranslationIssue13toDebugStringE'
        'v',
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

  @overload(THIS)
  def __eq__(self, second: TranslationIssue) -> bool:
    """
    Calls Qt's 'bool operator==(const TranslationIssue &first, const
    TranslationIssue &second)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldebugtranslation-translationissue.html

    Parameters
    ----------

    second : TranslationIssue
      Passed on as a value: Qt reads the C++
      QQmlDebugTranslation::TranslationIssue, which stays Python's own.
    """
    #  bool operator==(const TranslationIssue &first, const TranslationIssue
    #      &second)
    return Rituals.call(
        'ritual_ZN20QQmlDebugTranslationeqERKNS_16TranslationIssueES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(second),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
