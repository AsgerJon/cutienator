"""
qdesigner_internal::DesignerMetaEnum binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::DesignerMetaEnum to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class DesignerMetaEnum(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's qdesigner_internal::DesignerMetaEnum: a plain Python
  object standing in front of one C++ qdesigner_internal::DesignerMetaEnum.

  C++ hands a qdesigner_internal::DesignerMetaEnum around as a copy, so every
  C++ qdesigner_internal::DesignerMetaEnum behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::DesignerMetaEnum that has a
  ritual and that Python can call so far, 2 names in all:
  'messageToStringFailed', 'messageParseFailed'. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'int qdesigner_internal::DesignerMetaEnum::parseEnum(const QString
    &s, bool *ok) const': takes a number to change where it is.
  - Qt's 'qdesigner_internal::DesignerMetaEnum::~DesignerMetaEnum()': the
    destructor: Python removes its C++ qdesigner_internal::DesignerMetaEnum
    by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 7 functions Qt declares: 1 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ qdesigner_internal::DesignerMetaEnum is created at the first use,
    not by 'qdesigner_internal::DesignerMetaEnum(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a qdesigner_internal::DesignerMetaEnum back gives a
    copy the ritual made for Python, in a new cute
    qdesigner_internal::DesignerMetaEnum.
  - Each name of Qt's qdesigner_internal::DesignerMetaEnum that has no cute
    function yet, 'parseEnum', 'toString', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::DesignerMetaEnum'

  #  Qt's '~qdesigner_internal::DesignerMetaEnum()'. Naming it makes this a
  #  value class: Python owns every C++ qdesigner_internal::DesignerMetaEnum
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN18qdesigner_internal16DesignerMetaEnumD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def messageToStringFailed(self, value: int) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::DesignerMetaEnum::messageToStringFailed(int value)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-designermetaenum.html

    Parameters
    ----------

    value : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString
    #      qdesigner_internal::DesignerMetaEnum::messageToStringFailed(int
    #      value) const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal16DesignerMetaEnum21messageToStringF'
        'ailedEi',
        value,
    )

  @overload(str)
  def messageParseFailed(self, s: str) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::DesignerMetaEnum::messageParseFailed(const QString
    &s) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-designermetaenum.html

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::DesignerMetaEnum::messageParseFailed(const
    #      QString &s) const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal16DesignerMetaEnum18messageParseFail'
        'edERK7QString',
        s,
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

  @overload(str, str, str)
  def __init__(self, name: str, scope: str, separator: str) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::DesignerMetaEnum::DesignerMetaEnum(const QString
    &name, const QString &scope, const QString &separator)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-designermetaenum.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    scope : str
      Passed on as it is: a QString is made of it for the call.

    separator : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  qdesigner_internal::DesignerMetaEnum::DesignerMetaEnum(const QString
    #      &name, const QString &scope, const QString &separator)
    self._noteCreation(DesignerMetaEnum, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal16DesignerMetaEnumC1ERK7QStringS3_S3_',
        name, scope, separator,
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::DesignerMetaEnum::DesignerMetaEnum()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-designermetaenum.html
    """
    #  qdesigner_internal::DesignerMetaEnum::DesignerMetaEnum()
    self._noteCreation(DesignerMetaEnum, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal16DesignerMetaEnumC1Ev',
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

  @staticmethod
  def parseEnum(*__, **_) -> Never:
    """
    Qt's 'int qdesigner_internal::DesignerMetaEnum::parseEnum(const QString
    &s, bool *ok) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'qdesigner_internal.DesignerMetaEnum.parseEnum' has no cute "
        "function yet. Qt's 'int "
        "qdesigner_internal::DesignerMetaEnum::parseEnum(const QString &s, "
        "bool *ok) const': takes a number to change where it is.")

  @staticmethod
  def toString(*__, **_) -> Never:
    """
    Qt's 'QString qdesigner_internal::DesignerMetaEnum::toString(int value,
    SerializationMode sm, bool *ok) const': the compiler refuses its ritual
    as it would be written here: unknown type name 'SerializationMode'.
    """
    raise NotImplementedError(
        "'qdesigner_internal.DesignerMetaEnum.toString' has no cute "
        "function yet. Qt's 'QString "
        "qdesigner_internal::DesignerMetaEnum::toString(int value, "
        "SerializationMode sm, bool *ok) const': the compiler refuses its "
        "ritual as it would be written here: unknown type name "
        "'SerializationMode'.")
