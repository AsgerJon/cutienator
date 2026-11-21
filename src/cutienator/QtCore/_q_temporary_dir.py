"""
QTemporaryDir binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qtemporarydir.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QTemporaryDir(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTemporaryDir: a plain Python object standing in
  front of one C++ QTemporaryDir.

  What exists
  -----------

  Every function of Qt's QTemporaryDir that has a ritual and that Python can
  call so far, 7 names in all: 'isValid', 'errorString', 'autoRemove',
  'setAutoRemove', 'remove', 'path', 'filePath'. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTemporaryDir::~QTemporaryDir()': the destructor: Python never
    removes a C++ QTemporaryDir.

  What has no ritual
  ------------------

  5 of the 15 functions Qt declares: 3 takes or gives a type that cannot be
  passed yet; 2 forbidden.

  What to expect
  --------------

  - The C++ QTemporaryDir is created at the first use, not by
    'QTemporaryDir(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTemporaryDir.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTemporaryDir'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QTemporaryDir::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtemporarydir.html#isValid
    """
    #  bool QTemporaryDir::isValid() const
    return self.uglySide.call('ritual_ZNK13QTemporaryDir7isValidEv')

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QTemporaryDir::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtemporarydir.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTemporaryDir::errorString() const
    return self.uglySide.call('ritual_ZNK13QTemporaryDir11errorStringEv')

  def autoRemove(self) -> bool:
    """
    Calls Qt's 'bool QTemporaryDir::autoRemove() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtemporarydir.html#autoRemove
    """
    #  bool QTemporaryDir::autoRemove() const
    return self.uglySide.call('ritual_ZNK13QTemporaryDir10autoRemoveEv')

  def path(self) -> str:
    """
    Calls Qt's 'QString QTemporaryDir::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtemporarydir.html#path

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTemporaryDir::path() const
    return self.uglySide.call('ritual_ZNK13QTemporaryDir4pathEv')

  @overload(str)
  def filePath(self, fileName: str) -> str:
    """
    Calls Qt's 'QString QTemporaryDir::filePath(const QString &fileName)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtemporarydir.html#filePath

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTemporaryDir::filePath(const QString &fileName) const
    return self.uglySide.call(
        'ritual_ZNK13QTemporaryDir8filePathERK7QString', fileName,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAutoRemove(self, b: bool) -> None:
    """
    Calls Qt's 'void QTemporaryDir::setAutoRemove(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/qtemporarydir.html#setAutoRemove

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void QTemporaryDir::setAutoRemove(bool b)
    self.uglySide.call('ritual_ZN13QTemporaryDir13setAutoRemoveEb', b)

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
    Notes what was given, for Qt's 'QTemporaryDir::QTemporaryDir()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtemporarydir.html#QTemporaryDir
    """
    #  QTemporaryDir::QTemporaryDir()
    self._noteCreation(QTemporaryDir, lambda: Rituals.call(
        'ritual_ZN13QTemporaryDirC1Ev',
    ))

  @overload(str)
  def __init__(self, templateName: str) -> None:
    """
    Notes what was given, for Qt's 'QTemporaryDir::QTemporaryDir(const
    QString &templateName)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtemporarydir.html#QTemporaryDir

    Parameters
    ----------

    templateName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QTemporaryDir::QTemporaryDir(const QString &templateName)
    self._noteCreation(QTemporaryDir, lambda: Rituals.call(
        'ritual_ZN13QTemporaryDirC1ERK7QString', templateName,
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

  def remove(self) -> bool:
    """
    Calls Qt's 'bool QTemporaryDir::remove()'.

    Qt's own words: https://doc.qt.io/qt-6/qtemporarydir.html#remove
    """
    #  bool QTemporaryDir::remove()
    return self.uglySide.call('ritual_ZN13QTemporaryDir6removeEv')
