"""
QHostInfoCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qhostinfo_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QHostInfoCache to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QHostInfo
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHostInfo = WAIT['QHostInfo']


class QHostInfoCache(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHostInfoCache: a plain Python object standing in
  front of one C++ QHostInfoCache.

  What exists
  -----------

  Every function of Qt's QHostInfoCache that has a ritual and that Python can
  call so far, 4 names in all: 'put', 'clear', 'isEnabled', 'setEnabled'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHostInfo QHostInfoCache::get(const QString &name, bool *valid)':
    takes a number to change where it is.

  What to expect
  --------------

  - The C++ QHostInfoCache is created at the first use, not by
    'QHostInfoCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHostInfoCache.
  - Each name of Qt's QHostInfoCache that has no cute function yet, 'get',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHostInfoCache'

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

  @overload(bool)
  def setEnabled(self, e: bool) -> None:
    """
    Calls Qt's 'void QHostInfoCache::setEnabled(bool e)'.

    Qt's own words: https://doc.qt.io/qt-6/qhostinfocache.html#setEnabled

    Parameters
    ----------

    e : bool
      Passed on as it is.
    """
    #  void QHostInfoCache::setEnabled(bool e)
    self.uglySide.call('ritual_ZN14QHostInfoCache10setEnabledEb', e)

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
    Notes what was given, for Qt's 'QHostInfoCache::QHostInfoCache()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qhostinfocache.html#QHostInfoCache
    """
    #  QHostInfoCache::QHostInfoCache()
    self._noteCreation(QHostInfoCache, lambda: Rituals.call(
        'ritual_ZN14QHostInfoCacheC1Ev',
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

  @overload(str, QHostInfo)
  def put(self, name: str, info: QHostInfo) -> None:
    """
    Calls Qt's 'void QHostInfoCache::put(const QString &name, const QHostInfo
    &info)'.

    Qt's own words: https://doc.qt.io/qt-6/qhostinfocache.html#put

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    info : QHostInfo
      Passed on as a value: Qt reads the C++ QHostInfo, which stays Python's
      own.
    """
    #  void QHostInfoCache::put(const QString &name, const QHostInfo &info)
    self.uglySide.call(
        'ritual_ZN14QHostInfoCache3putERK7QStringRK9QHostInfo',
        name, self._valueOf(info),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QHostInfoCache::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qhostinfocache.html#clear
    """
    #  void QHostInfoCache::clear()
    self.uglySide.call('ritual_ZN14QHostInfoCache5clearEv')

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QHostInfoCache::isEnabled()'.

    Qt's own words: https://doc.qt.io/qt-6/qhostinfocache.html#isEnabled
    """
    #  bool QHostInfoCache::isEnabled()
    return self.uglySide.call('ritual_ZN14QHostInfoCache9isEnabledEv')

  @staticmethod
  def get(*__, **_) -> Never:
    """
    Qt's 'QHostInfo QHostInfoCache::get(const QString &name, bool *valid)':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QHostInfoCache.get' has no cute function yet. Qt's 'QHostInfo "
        "QHostInfoCache::get(const QString &name, bool *valid)': takes a "
        "number to change where it is.")
