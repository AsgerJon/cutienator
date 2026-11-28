"""
QtPrivate::QXmlString binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qxmlstream.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QXmlString(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtPrivate::QXmlString: a plain Python object standing
  in front of one C++ QtPrivate::QXmlString.

  C++ hands a QtPrivate::QXmlString around as a copy, so every C++
  QtPrivate::QXmlString behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtPrivate::QXmlString that has a ritual and that
  Python can call so far, 4 names in all: 'size', 'isNull', '__eq__',
  '__ne__'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtPrivate::QXmlString::QXmlString(QStringPrivate &&d)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QXmlString &QtPrivate::QXmlString::operator=(const QString &s)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QXmlString &QtPrivate::QXmlString::operator=(QString &&s)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QtPrivate::QXmlString::swap(QXmlString &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QStringView QtPrivate::QXmlString::operator QStringView() const':
    an operator Python has no name for.
  - Qt's 'QtPrivate::QXmlString::~QXmlString()': the destructor: Python
    removes its C++ QtPrivate::QXmlString by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QtPrivate::QXmlString is created at the first use, not by
    'QtPrivate::QXmlString(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtPrivate::QXmlString back gives a copy the ritual
    made for Python, in a new cute QtPrivate::QXmlString.
  - Each name of Qt's QtPrivate::QXmlString that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtPrivate::QXmlString'

  #  Qt's '~QtPrivate::QXmlString()'. Naming it makes this a value class:
  #  Python owns every C++ QtPrivate::QXmlString behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QtPrivate10QXmlStringD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def size(self) -> int:
    """
    Calls Qt's 'qsizetype QtPrivate::QXmlString::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtprivate-qxmlstring.html#size
    """
    #  qsizetype QtPrivate::QXmlString::size() const
    return self.uglySide.call('ritual_ZNK9QtPrivate10QXmlString4sizeEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QtPrivate::QXmlString::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtprivate-qxmlstring.html#isNull
    """
    #  bool QtPrivate::QXmlString::isNull() const
    return self.uglySide.call('ritual_ZNK9QtPrivate10QXmlString6isNullEv')

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
  def __eq__(self, rhs: QXmlString) -> bool:
    """
    Calls Qt's 'bool operator==(const QXmlString &lhs, const QXmlString
    &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qxmlstring.html#operator==

    Parameters
    ----------

    rhs : QXmlString
      Passed on as a value: Qt reads the C++ QtPrivate::QXmlString, which
      stays Python's own.
    """
    #  bool operator==(const QXmlString &lhs, const QXmlString &rhs)
    return Rituals.call(
        'ritual_ZN9QtPrivateeqERKNS_10QXmlStringES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QXmlString) -> bool:
    """
    Calls Qt's 'bool operator!=(const QXmlString &lhs, const QXmlString
    &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qxmlstring.html#operator!=

    Parameters
    ----------

    rhs : QXmlString
      Passed on as a value: Qt reads the C++ QtPrivate::QXmlString, which
      stays Python's own.
    """
    #  bool operator!=(const QXmlString &lhs, const QXmlString &rhs)
    return Rituals.call(
        'ritual_ZN9QtPrivateneERKNS_10QXmlStringES2_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def __init__(self, s: str) -> None:
    """
    Notes what was given, for Qt's 'QtPrivate::QXmlString::QXmlString(const
    QString &s)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qxmlstring.html#QXmlString

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QtPrivate::QXmlString::QXmlString(const QString &s)
    self._noteCreation(QXmlString, lambda: Rituals.call(
        'ritual_ZN9QtPrivate10QXmlStringC1ERK7QString', s,
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QtPrivate::QXmlString::QXmlString()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-qxmlstring.html#QXmlString
    """
    #  QtPrivate::QXmlString::QXmlString()
    self._noteCreation(QXmlString, lambda: Rituals.call(
        'ritual_ZN9QtPrivate10QXmlStringC1Ev',
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
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QtPrivate::QXmlString::swap(QXmlString &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QtPrivate.QXmlString.swap' has no cute function yet. Qt's 'void "
        "QtPrivate::QXmlString::swap(QXmlString &other)': takes a type "
        "Python has no way to hand over yet.")
