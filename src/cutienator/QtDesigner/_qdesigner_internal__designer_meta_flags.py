"""
qdesigner_internal::DesignerMetaFlags binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::DesignerMetaFlags to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class DesignerMetaFlags(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's qdesigner_internal::DesignerMetaFlags: a plain Python
  object standing in front of one C++ qdesigner_internal::DesignerMetaFlags.

  C++ hands a qdesigner_internal::DesignerMetaFlags around as a copy, so
  every C++ qdesigner_internal::DesignerMetaFlags behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::DesignerMetaFlags that has a
  ritual and that Python can call so far, 2 names in all: 'flags',
  'messageParseFailed'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'int qdesigner_internal::DesignerMetaFlags::parseFlags(const QString
    &s, bool *ok) const': takes a number to change where it is.
  - Qt's 'qdesigner_internal::DesignerMetaFlags::~DesignerMetaFlags()': the
    destructor: Python removes its C++ qdesigner_internal::DesignerMetaFlags
    by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 7 functions Qt declares: 1 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ qdesigner_internal::DesignerMetaFlags is created at the first
    use, not by 'qdesigner_internal::DesignerMetaFlags(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a qdesigner_internal::DesignerMetaFlags back gives a
    copy the ritual made for Python, in a new cute
    qdesigner_internal::DesignerMetaFlags.
  - Each name of Qt's qdesigner_internal::DesignerMetaFlags that has no cute
    function yet, 'parseFlags', 'toString', holds a function that raises
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
  __qt_class__ = 'qdesigner_internal::DesignerMetaFlags'

  #  Qt's '~qdesigner_internal::DesignerMetaFlags()'. Naming it makes this a
  #  value class: Python owns every C++ qdesigner_internal::DesignerMetaFlags
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN18qdesigner_internal17DesignerMetaFlagsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def flags(self, value: int) -> QStringList:
    """
    Calls Qt's 'QStringList qdesigner_internal::DesignerMetaFlags::flags(int
    value) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-designermetaflags.html#flags

    Parameters
    ----------

    value : int
      Passed on as it is.

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList qdesigner_internal::DesignerMetaFlags::flags(int value)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal17DesignerMetaFlags5flagsEi', value,
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def messageParseFailed(self, s: str) -> str:
    """
    Calls Qt's 'QString
    qdesigner_internal::DesignerMetaFlags::messageParseFailed(const QString
    &s) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-designermetaflags.html

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString
    #      qdesigner_internal::DesignerMetaFlags::messageParseFailed(const
    #      QString &s) const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal17DesignerMetaFlags18messageParseFai'
        'ledERK7QString',
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
  def __init__(self, enumName: str, scope: str, separator: str) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::DesignerMetaFlags::DesignerMetaFlags(const QString
    &enumName, const QString &scope, const QString &separator)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-designermetaflags.html

    Parameters
    ----------

    enumName : str
      Passed on as it is: a QString is made of it for the call.

    scope : str
      Passed on as it is: a QString is made of it for the call.

    separator : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  qdesigner_internal::DesignerMetaFlags::DesignerMetaFlags(const QString
    #      &enumName, const QString &scope, const QString &separator)
    self._noteCreation(DesignerMetaFlags, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal17DesignerMetaFlagsC1ERK7QStringS3_S3'
        '_',
        enumName, scope, separator,
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::DesignerMetaFlags::DesignerMetaFlags()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-designermetaflags.html
    """
    #  qdesigner_internal::DesignerMetaFlags::DesignerMetaFlags()
    self._noteCreation(DesignerMetaFlags, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal17DesignerMetaFlagsC1Ev',
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
  def parseFlags(*__, **_) -> Never:
    """
    Qt's 'int qdesigner_internal::DesignerMetaFlags::parseFlags(const QString
    &s, bool *ok) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'qdesigner_internal.DesignerMetaFlags.parseFlags' has no cute "
        "function yet. Qt's 'int "
        "qdesigner_internal::DesignerMetaFlags::parseFlags(const QString "
        "&s, bool *ok) const': takes a number to change where it is.")

  @staticmethod
  def toString(*__, **_) -> Never:
    """
    Qt's 'QString qdesigner_internal::DesignerMetaFlags::toString(int value,
    SerializationMode sm) const': the compiler refuses its ritual as it would
    be written here: unknown type name 'SerializationMode'.
    """
    raise NotImplementedError(
        "'qdesigner_internal.DesignerMetaFlags.toString' has no cute "
        "function yet. Qt's 'QString "
        "qdesigner_internal::DesignerMetaFlags::toString(int value, "
        "SerializationMode sm) const': the compiler refuses its ritual as "
        "it would be written here: unknown type name 'SerializationMode'.")
