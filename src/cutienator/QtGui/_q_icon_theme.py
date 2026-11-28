"""
QIconTheme binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qiconloader_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QIconTheme to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QList, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QIconDirInfo


class QIconTheme(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QIconTheme: a plain Python object standing in front
  of one C++ QIconTheme.

  C++ hands a QIconTheme around as a copy, so every C++ QIconTheme behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QIconTheme that has a ritual and that Python can
  call so far, 4 names in all: 'parents', 'keyList', 'contentDirs',
  'isValid'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QIconTheme::~QIconTheme()': the destructor: Python removes its C++
    QIconTheme by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 7 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QIconTheme is created at the first use, not by 'QIconTheme(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QIconTheme back gives a copy the ritual made for
    Python, in a new cute QIconTheme.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QIconTheme'

  #  Qt's '~QIconTheme()'. Naming it makes this a value class: Python owns
  #  every C++ QIconTheme behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QIconThemeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def parents(self) -> QStringList:
    """
    Calls Qt's 'QStringList QIconTheme::parents() const'.

    Qt's own words: https://doc.qt.io/qt-6/qicontheme.html#parents

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QIconTheme::parents() const
    address = self.uglySide.call('ritual_ZNK10QIconTheme7parentsEv')
    return QStringList._cuteOwning(address)

  def keyList(self) -> QList[QIconDirInfo]:
    """
    Calls Qt's 'QList<QIconDirInfo> QIconTheme::keyList() const'.

    Qt's own words: https://doc.qt.io/qt-6/qicontheme.html#keyList

    Returns
    -------

    QList[QIconDirInfo]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QIconDirInfo> QIconTheme::keyList() const
    address = self.uglySide.call('ritual_ZNK10QIconTheme7keyListEv')
    from . import QIconDirInfo
    return QList[QIconDirInfo]._cuteOwning(address)

  def contentDirs(self) -> QStringList:
    """
    Calls Qt's 'QStringList QIconTheme::contentDirs() const'.

    Qt's own words: https://doc.qt.io/qt-6/qicontheme.html#contentDirs

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QIconTheme::contentDirs() const
    address = self.uglySide.call('ritual_ZNK10QIconTheme11contentDirsEv')
    return QStringList._cuteOwning(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QIconTheme::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qicontheme.html#isValid
    """
    #  bool QIconTheme::isValid() const
    return self.uglySide.call('ritual_ZNK10QIconTheme7isValidEv')

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
    Notes what was given, for Qt's 'QIconTheme::QIconTheme()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qicontheme.html#QIconTheme
    """
    #  QIconTheme::QIconTheme()
    self._noteCreation(QIconTheme, lambda: Rituals.call(
        'ritual_ZN10QIconThemeC1Ev',
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
