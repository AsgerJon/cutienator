"""
QScxmlError binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/qscxmlerror.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QList


class QScxmlError(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QScxmlError: a plain Python object standing in front
  of one C++ QScxmlError.

  C++ hands a QScxmlError around as a copy, so every C++ QScxmlError behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QScxmlError that has a ritual and that Python can
  call so far, 6 names in all: 'isValid', 'fileName', 'line', 'column',
  'description', 'toString'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QScxmlError &QScxmlError::operator=(const QScxmlError &a0)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QScxmlError::~QScxmlError()': the destructor: Python removes its
    C++ QScxmlError by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 14 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QScxmlError is created at the first use, not by
    'QScxmlError(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QScxmlError back gives a copy the ritual made for
    Python, in a new cute QScxmlError.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlError'

  #  Qt's '~QScxmlError()'. Naming it makes this a value class: Python owns
  #  every C++ QScxmlError behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QScxmlErrorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QScxmlError::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlerror.html#isValid
    """
    #  bool QScxmlError::isValid() const
    return self.uglySide.call('ritual_ZNK11QScxmlError7isValidEv')

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QScxmlError::fileName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlerror.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScxmlError::fileName() const
    return self.uglySide.call('ritual_ZNK11QScxmlError8fileNameEv')

  def line(self) -> int:
    """
    Calls Qt's 'int QScxmlError::line() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlerror.html#line
    """
    #  int QScxmlError::line() const
    return self.uglySide.call('ritual_ZNK11QScxmlError4lineEv')

  def column(self) -> int:
    """
    Calls Qt's 'int QScxmlError::column() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlerror.html#column
    """
    #  int QScxmlError::column() const
    return self.uglySide.call('ritual_ZNK11QScxmlError6columnEv')

  def description(self) -> str:
    """
    Calls Qt's 'QString QScxmlError::description() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlerror.html#description

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScxmlError::description() const
    return self.uglySide.call('ritual_ZNK11QScxmlError11descriptionEv')

  def toString(self) -> str:
    """
    Calls Qt's 'QString QScxmlError::toString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlerror.html#toString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScxmlError::toString() const
    return self.uglySide.call('ritual_ZNK11QScxmlError8toStringEv')

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
    Notes what was given, for Qt's 'QScxmlError::QScxmlError()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlerror.html#QScxmlError
    """
    #  QScxmlError::QScxmlError()
    self._noteCreation(QScxmlError, lambda: Rituals.call(
        'ritual_ZN11QScxmlErrorC1Ev',
    ))

  @overload(str, int, int, str)
  def __init__(
      self,
      fileName: str,
      line: int,
      column: int,
      description: str,
  ) -> None:
    """
    Notes what was given, for Qt's 'QScxmlError::QScxmlError(const QString
    &fileName, int line, int column, const QString &description)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlerror.html#QScxmlError

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    line : int
      Passed on as it is.

    column : int
      Passed on as it is.

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QScxmlError::QScxmlError(const QString &fileName, int line, int
    #      column, const QString &description)
    self._noteCreation(QScxmlError, lambda: Rituals.call(
        'ritual_ZN11QScxmlErrorC1ERK7QStringiiS2_',
        fileName, line, column, description,
    ))

  @overload(THIS)
  def __init__(self, a0: QScxmlError) -> None:
    """
    Notes what was given, for Qt's 'QScxmlError::QScxmlError(const
    QScxmlError &a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlerror.html#QScxmlError

    Parameters
    ----------

    a0 : QScxmlError
      Passed on as a value: Qt reads the C++ QScxmlError, which stays
      Python's own.
    """
    #  QScxmlError::QScxmlError(const QScxmlError &a0)
    self._noteCreation(QScxmlError, lambda: Rituals.call(
        'ritual_ZN11QScxmlErrorC1ERKS_', self._valueOf(a0),
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


#  Qt's 'QList<QScxmlError>': the list of QScxmlError, which
#  'QList[QScxmlError]' gives. It is made here, so that there is one as soon
#  as there can be a QScxmlError.
QList.createKind(
    QScxmlError, 'value',
    make='ritual_list_make_QScxmlError',
    add='ritual_list_add_QScxmlError',
    size='ritual_list_size_QScxmlError',
    at='ritual_list_at_QScxmlError',
    drop='ritual_list_drop_QScxmlError',
)
