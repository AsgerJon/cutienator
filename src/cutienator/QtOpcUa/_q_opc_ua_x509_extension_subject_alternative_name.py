"""
QOpcUaX509ExtensionSubjectAlternativeName binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuax509extensionsubjectalternativename.h, Qt 6.12.0. Changes
#  made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from . import QOpcUaX509Extension

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QOpcUaX509ExtensionSubjectAlternativeName(QOpcUaX509Extension):
  """
  The cute side of Qt's QOpcUaX509ExtensionSubjectAlternativeName: a plain
  Python object standing in front of one C++
  QOpcUaX509ExtensionSubjectAlternativeName.

  It is built on the cute 'QOpcUaX509Extension', as Qt's
  QOpcUaX509ExtensionSubjectAlternativeName is built on Qt's
  QOpcUaX509Extension, and has everything that class has.

  C++ hands a QOpcUaX509ExtensionSubjectAlternativeName around as a copy, so
  every C++ QOpcUaX509ExtensionSubjectAlternativeName behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaX509ExtensionSubjectAlternativeName that has a
  ritual and that Python can call so far, 2 names in all: '__eq__',
  'addEntry'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaX509ExtensionSubjectAlternativeName
    &QOpcUaX509ExtensionSubjectAlternativeName::operator=(const
    QOpcUaX509ExtensionSubjectAlternativeName &a0)': assignment: Python binds
    a name and has no operator for it.
  - Qt's 'QOpcUaX509ExtensionSubjectAlternativeName::
    ~QOpcUaX509ExtensionSubjectAlternativeName()': the destructor: Python
    removes its C++ QOpcUaX509ExtensionSubjectAlternativeName by it, and has
    no other use for it.
  - Qt's 'const QList<std::pair<Type, QString>>
    &QOpcUaX509ExtensionSubjectAlternativeName::entries() const': gives a
    type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QOpcUaX509ExtensionSubjectAlternativeName is created at the first
    use, not by 'QOpcUaX509ExtensionSubjectAlternativeName(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaX509ExtensionSubjectAlternativeName back gives
    a copy the ritual made for Python, in a new cute
    QOpcUaX509ExtensionSubjectAlternativeName.
  - Each name of Qt's QOpcUaX509ExtensionSubjectAlternativeName that has no
    cute function yet, 'entries', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QOpcUaX509ExtensionSubjectAlternativeName,
  #  each a class in here as in C++, and the names Qt has for the
  #  combinations of its flags enums.

  class Type(CuteNum, scoped=True):
    """
    The enum 'QOpcUaX509ExtensionSubjectAlternativeName::Type' of Qt, with
    the 4 names Qt gives in it. C++ keeps these names inside the enum, so the
    class that holds the enum does not have them.
    """

    Email = Kee[int](0)
    URI = Kee[int](1)
    DNS = Kee[int](2)
    IP = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaX509ExtensionSubjectAlternativeName'

  #  Qt's '~QOpcUaX509ExtensionSubjectAlternativeName()'. Naming it makes
  #  this a value class: Python owns every C++
  #  QOpcUaX509ExtensionSubjectAlternativeName behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN41QOpcUaX509ExtensionSubjectAlternativeNameD1Ev')

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

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaX509ExtensionSubjectAlternativeName) -> bool:
    """
    Calls Qt's 'bool
    QOpcUaX509ExtensionSubjectAlternativeName::operator==(const
    QOpcUaX509ExtensionSubjectAlternativeName &rhs) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509extensionsubjectalternativename.html

    Parameters
    ----------

    rhs : QOpcUaX509ExtensionSubjectAlternativeName
      Passed on as a value: Qt reads the C++
      QOpcUaX509ExtensionSubjectAlternativeName, which stays Python's own.
    """
    #  bool QOpcUaX509ExtensionSubjectAlternativeName::operator==(const
    #      QOpcUaX509ExtensionSubjectAlternativeName &rhs) const
    return self.uglySide.call(
        'ritual_ZNK41QOpcUaX509ExtensionSubjectAlternativeNameeqERKS_',
        self._valueOf(rhs),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaX509ExtensionSubjectAlternativeName::
    QOpcUaX509ExtensionSubjectAlternativeName()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509extensionsubjectalternativename.html
    """
    #  QOpcUaX509ExtensionSubjectAlternativeName::
    #      QOpcUaX509ExtensionSubjectAlternativeName()
    self._noteCreation(
        QOpcUaX509ExtensionSubjectAlternativeName, lambda: Rituals.call(
            'ritual_ZN41QOpcUaX509ExtensionSubjectAlternativeNameC1Ev',
        ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaX509ExtensionSubjectAlternativeName) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaX509ExtensionSubjectAlternativeName::
    QOpcUaX509ExtensionSubjectAlternativeName(const
    QOpcUaX509ExtensionSubjectAlternativeName &a0)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509extensionsubjectalternativename.html

    Parameters
    ----------

    a0 : QOpcUaX509ExtensionSubjectAlternativeName
      Passed on as a value: Qt reads the C++
      QOpcUaX509ExtensionSubjectAlternativeName, which stays Python's own.
    """
    #  QOpcUaX509ExtensionSubjectAlternativeName::
    #      QOpcUaX509ExtensionSubjectAlternativeName(const
    #      QOpcUaX509ExtensionSubjectAlternativeName &a0)
    self._noteCreation(
        QOpcUaX509ExtensionSubjectAlternativeName, lambda: Rituals.call(
            'ritual_ZN41QOpcUaX509ExtensionSubjectAlternativeNameC1ERKS_',
            self._valueOf(a0),
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

  @overload(Type, str)
  def addEntry(self, type: Type, value: str) -> None:
    """
    Calls Qt's 'void QOpcUaX509ExtensionSubjectAlternativeName::addEntry(Type
    type, const QString &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuax509extensionsubjectalternativename.html

    Parameters
    ----------

    type : Type
      Passed on as its number.

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaX509ExtensionSubjectAlternativeName::addEntry(Type type,
    #      const QString &value)
    self.uglySide.call(
        'ritual_ZN41QOpcUaX509ExtensionSubjectAlternativeName8addEntryENS_4'
        'TypeERK7QString',
        type.value, value,
    )

  @staticmethod
  def entries(*__, **_) -> Never:
    """
    Qt's 'const QList<std::pair<Type, QString>>
    &QOpcUaX509ExtensionSubjectAlternativeName::entries() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaX509ExtensionSubjectAlternativeName.entries' has no cute "
        "function yet. Qt's 'const QList<std::pair<Type, QString>> "
        "&QOpcUaX509ExtensionSubjectAlternativeName::entries() const': "
        "gives a type Python has no way to take yet.")
