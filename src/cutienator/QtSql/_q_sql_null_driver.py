"""
QSqlNullDriver binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSql/6.12.0/QtSql/private/qsqlnulldriver_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSqlNullDriver to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSqlDriver

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSqlError, QSqlResult
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSqlError = WAIT['QSqlError']


class QSqlNullDriver(QSqlDriver):
  """
  The cute side of Qt's QSqlNullDriver: a plain Python object standing in
  front of one C++ QSqlNullDriver.

  It is built on the cute 'QSqlDriver', as Qt's QSqlNullDriver is built on
  Qt's QSqlDriver, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSqlNullDriver that has a ritual and that Python can
  call so far, 7 names in all: 'hasFeature', 'open', 'close', 'createResult',
  'setOpen', 'setOpenError', 'setLastError'. It can be made from Python, in 1
  way; see '__init__'.

  What to expect
  --------------

  - The C++ QSqlNullDriver is created at the first use, not by
    'QSqlNullDriver(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSqlNullDriver.
  - Qt tells when it has removed the C++ QSqlNullDriver. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSqlNullDriver'

  #  A C++ QSqlNullDriver Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSqlNullDriver'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSqlDriver.DriverFeature)
  def hasFeature(self, a0: QSqlDriver.DriverFeature) -> bool:
    """
    Calls Qt's 'bool QSqlNullDriver::hasFeature(DriverFeature a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlnulldriver.html#hasFeature

    Parameters
    ----------

    a0 : QSqlDriver.DriverFeature
      Passed on as its number.
    """
    #  bool QSqlNullDriver::hasFeature(DriverFeature a0) const
    ritual = (
        'ritual_ZNK14QSqlNullDriver10hasFeatureEN10QSqlDriver13DriverFeatur'
        'eE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QSqlNullDriver10hasFeatureEN10QSqlDriver13Driver'
          'FeatureE')
    return self.uglySide.call(ritual, a0.value)

  def createResult(self) -> Optional[QSqlResult]:
    """
    Calls Qt's 'QSqlResult *QSqlNullDriver::createResult() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlnulldriver.html#createResult

    Returns
    -------

    Optional[QSqlResult]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSqlResult *QSqlNullDriver::createResult() const
    ritual = 'ritual_ZNK14QSqlNullDriver12createResultEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QSqlNullDriver12createResultEv'
    address = self.uglySide.call(ritual)
    from . import QSqlResult
    return QSqlResult._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setOpen(self, a0: bool) -> None:
    """
    Calls Qt's 'void QSqlNullDriver::setOpen(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlnulldriver.html#setOpen

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QSqlNullDriver::setOpen(bool a0)
    ritual = 'ritual_ZN14QSqlNullDriver7setOpenEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlNullDriver7setOpenEb'
    self.uglySide.call(ritual, a0)

  @overload(bool)
  def setOpenError(self, a0: bool) -> None:
    """
    Calls Qt's 'void QSqlNullDriver::setOpenError(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlnulldriver.html#setOpenError

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QSqlNullDriver::setOpenError(bool a0)
    ritual = 'ritual_ZN14QSqlNullDriver12setOpenErrorEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlNullDriver12setOpenErrorEb'
    self.uglySide.call(ritual, a0)

  @overload(QSqlError)
  def setLastError(self, a0: QSqlError) -> None:
    """
    Calls Qt's 'void QSqlNullDriver::setLastError(const QSqlError &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlnulldriver.html#setLastError

    Parameters
    ----------

    a0 : QSqlError
      Passed on as a value: Qt reads the C++ QSqlError, which stays Python's
      own.
    """
    #  void QSqlNullDriver::setLastError(const QSqlError &a0)
    ritual = 'ritual_ZN14QSqlNullDriver12setLastErrorERK9QSqlError'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlNullDriver12setLastErrorERK9QSqlError'
    self.uglySide.call(ritual, self._valueOf(a0))

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
    Notes what was given, for Qt's 'QSqlNullDriver::QSqlNullDriver()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsqlnulldriver.html#QSqlNullDriver
    """
    #  QSqlNullDriver::QSqlNullDriver()
    self._noteCreation(QSqlNullDriver, lambda: Rituals.call(
        'ritual_ZN14QSqlNullDriverC1Ev',
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

  @overload(str, str, str, str, int, str)
  def open(
      self,
      a0: str,
      a1: str,
      a2: str,
      a3: str,
      a4: int,
      a5: str,
  ) -> bool:
    """
    Calls Qt's 'bool QSqlNullDriver::open(const QString &a0, const QString
    &a1, const QString &a2, const QString &a3, int a4, const QString &a5)'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlnulldriver.html#open

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    a1 : str
      Passed on as it is: a QString is made of it for the call.

    a2 : str
      Passed on as it is: a QString is made of it for the call.

    a3 : str
      Passed on as it is: a QString is made of it for the call.

    a4 : int
      Passed on as it is.

    a5 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QSqlNullDriver::open(const QString &a0, const QString &a1, const
    #      QString &a2, const QString &a3, int a4, const QString &a5)
    ritual = 'ritual_ZN14QSqlNullDriver4openERK7QStringS2_S2_S2_iS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlNullDriver4openERK7QStringS2_S2_S2_iS2_'
    return self.uglySide.call(ritual, a0, a1, a2, a3, a4, a5)

  def close(self) -> None:
    """
    Calls Qt's 'void QSqlNullDriver::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlnulldriver.html#close
    """
    #  void QSqlNullDriver::close()
    ritual = 'ritual_ZN14QSqlNullDriver5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QSqlNullDriver5closeEv'
    self.uglySide.call(ritual)
