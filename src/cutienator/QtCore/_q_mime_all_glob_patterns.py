"""
QMimeAllGlobPatterns binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qmimeglobpattern_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QMimeAllGlobPatterns to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QMimeGlobPattern
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMimeGlobPattern = WAIT['QMimeGlobPattern']


class QMimeAllGlobPatterns(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMimeAllGlobPatterns: a plain Python object standing
  in front of one C++ QMimeAllGlobPatterns.

  C++ hands a QMimeAllGlobPatterns around as a copy, so every C++
  QMimeAllGlobPatterns behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QMimeAllGlobPatterns that has a ritual and that
  Python can call so far, 3 names in all: 'addGlob', 'removeMimeType',
  'clear'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QMimeAllGlobPatterns::matchingGlobs(const QString &fileName,
    QMimeGlobMatchResult &result, const AddMatchFilterFunc &filterFunc)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'QMimeAllGlobPatterns::~QMimeAllGlobPatterns()': the destructor:
    Python removes its C++ QMimeAllGlobPatterns by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QMimeAllGlobPatterns is created at the first use, not by
    'QMimeAllGlobPatterns(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QMimeAllGlobPatterns back gives a copy the ritual
    made for Python, in a new cute QMimeAllGlobPatterns.
  - Each name of Qt's QMimeAllGlobPatterns that has no cute function yet,
    'matchingGlobs', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMimeAllGlobPatterns'

  #  Qt's '~QMimeAllGlobPatterns()'. Naming it makes this a value class:
  #  Python owns every C++ QMimeAllGlobPatterns behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QMimeAllGlobPatternsD1Ev'

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

  @overload(QMimeGlobPattern)
  def addGlob(self, glob: QMimeGlobPattern) -> None:
    """
    Calls Qt's 'void QMimeAllGlobPatterns::addGlob(const QMimeGlobPattern
    &glob)'.

    Qt's own words: https://doc.qt.io/qt-6/qmimeallglobpatterns.html#addGlob

    Parameters
    ----------

    glob : QMimeGlobPattern
      Passed on as a value: Qt reads the C++ QMimeGlobPattern, which stays
      Python's own.
    """
    #  void QMimeAllGlobPatterns::addGlob(const QMimeGlobPattern &glob)
    self.uglySide.call(
        'ritual_ZN20QMimeAllGlobPatterns7addGlobERK16QMimeGlobPattern',
        self._valueOf(glob),
    )

  @overload(str)
  def removeMimeType(self, mimeType: str) -> None:
    """
    Calls Qt's 'void QMimeAllGlobPatterns::removeMimeType(const QString
    &mimeType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmimeallglobpatterns.html#removeMimeType

    Parameters
    ----------

    mimeType : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMimeAllGlobPatterns::removeMimeType(const QString &mimeType)
    self.uglySide.call(
        'ritual_ZN20QMimeAllGlobPatterns14removeMimeTypeERK7QString',
        mimeType,
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QMimeAllGlobPatterns::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qmimeallglobpatterns.html#clear
    """
    #  void QMimeAllGlobPatterns::clear()
    self.uglySide.call('ritual_ZN20QMimeAllGlobPatterns5clearEv')

  @staticmethod
  def matchingGlobs(*__, **_) -> Never:
    """
    Qt's 'void QMimeAllGlobPatterns::matchingGlobs(const QString &fileName,
    QMimeGlobMatchResult &result, const AddMatchFilterFunc &filterFunc)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QMimeAllGlobPatterns.matchingGlobs' has no cute function yet. "
        "Qt's 'void QMimeAllGlobPatterns::matchingGlobs(const QString "
        "&fileName, QMimeGlobMatchResult &result, const AddMatchFilterFunc "
        "&filterFunc) const': takes a type Python has no way to hand over "
        "yet.")
