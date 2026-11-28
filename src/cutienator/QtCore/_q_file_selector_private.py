"""
QFileSelectorPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qfileselector_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QFileSelectorPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QObjectPrivate, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QChar, QFileSelector
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChar = WAIT['QChar']


class QFileSelectorPrivate(QObjectPrivate):
  """
  The cute side of Qt's QFileSelectorPrivate: a plain Python object standing
  in front of one C++ QFileSelectorPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QFileSelectorPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFileSelectorPrivate that has a ritual and that
  Python can call so far, 7 names in all: 'q_func', 'updateSelectors',
  'platformSelectors', 'addStatics', 'removeStatics', 'selectionHelper',
  'select'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QFileSelector *QFileSelectorPrivate::q_func() const': takes
    in Python what 'QFileSelector *QFileSelectorPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QFileSelectorPrivate is created at the first use, not by
    'QFileSelectorPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFileSelectorPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def updateSelectors() -> None:
    """
    Calls Qt's 'void QFileSelectorPrivate::updateSelectors()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfileselectorprivate.html#updateSelectors
    """
    #  void QFileSelectorPrivate::updateSelectors()
    Rituals.call('ritual_ZN20QFileSelectorPrivate15updateSelectorsEv')

  @staticmethod
  def platformSelectors() -> QStringList:
    """
    Calls Qt's 'QStringList QFileSelectorPrivate::platformSelectors()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfileselectorprivate.html#platformSelectors

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QFileSelectorPrivate::platformSelectors()
    address = Rituals.call(
        'ritual_ZN20QFileSelectorPrivate17platformSelectorsEv',
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(QStringList)
  def addStatics(a0: QStringList) -> None:
    """
    Calls Qt's 'void QFileSelectorPrivate::addStatics(const QStringList
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfileselectorprivate.html#addStatics

    Parameters
    ----------

    a0 : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QFileSelectorPrivate::addStatics(const QStringList &a0)
    Rituals.call(
        'ritual_ZN20QFileSelectorPrivate10addStaticsERK5QListI7QStringE',
        CuteMixin._valueOf(a0),
    )

  @staticmethod
  @overload(QStringList)
  def removeStatics(a0: QStringList) -> int:
    """
    Calls Qt's 'qsizetype QFileSelectorPrivate::removeStatics(const
    QStringList &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfileselectorprivate.html#removeStatics

    Parameters
    ----------

    a0 : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  qsizetype QFileSelectorPrivate::removeStatics(const QStringList &a0)
    return Rituals.call(
        'ritual_ZN20QFileSelectorPrivate13removeStaticsERK5QListI7QStringE',
        CuteMixin._valueOf(a0),
    )

  @staticmethod
  @overload(str, str, QStringList, QChar)
  def selectionHelper(
      path: str,
      fileName: str,
      selectors: QStringList,
      indicator: QChar,
  ) -> str:
    """
    Calls Qt's 'QString QFileSelectorPrivate::selectionHelper(const QString
    &path, const QString &fileName, const QStringList &selectors, QChar
    indicator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfileselectorprivate.html#selectionHelper

    Parameters
    ----------

    path : str
      Passed on as it is: a QString is made of it for the call.

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    selectors : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    indicator : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileSelectorPrivate::selectionHelper(const QString &path,
    #      const QString &fileName, const QStringList &selectors, QChar
    #      indicator)
    return Rituals.call(
        'ritual_ZN20QFileSelectorPrivate15selectionHelperERK7QStringS2_RK5Q'
        'ListIS0_E5QChar',
        path, fileName, CuteMixin._valueOf(selectors),
        CuteMixin._valueOf(indicator),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFileSelectorPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def select(self, filePath: str) -> str:
    """
    Calls Qt's 'QString QFileSelectorPrivate::select(const QString &filePath)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileselectorprivate.html#select

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileSelectorPrivate::select(const QString &filePath) const
    return self.uglySide.call(
        'ritual_ZNK20QFileSelectorPrivate6selectERK7QString', filePath,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QFileSelectorPrivate::QFileSelectorPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfileselectorprivate.html#QFileSelectorPrivate
    """
    #  QFileSelectorPrivate::QFileSelectorPrivate()
    self._noteCreation(QFileSelectorPrivate, lambda: Rituals.call(
        'ritual_ZN20QFileSelectorPrivateC1Ev',
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

  def q_func(self) -> Optional[QFileSelector]:
    """
    Calls Qt's 'QFileSelector *QFileSelectorPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qfileselectorprivate.html#q_func

    Returns
    -------

    Optional[QFileSelector]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFileSelector *QFileSelectorPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QFileSelectorPrivate6q_funcEv')
    from . import QFileSelector
    return QFileSelector._cuteAt(address)
