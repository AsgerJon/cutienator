"""
QPixmapCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qpixmapcache.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QPixmap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPixmap = WAIT['QPixmap']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPixmapCache(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPixmapCache: a plain Python object standing in front
  of one C++ QPixmapCache.

  C++ hands a QPixmapCache around as a copy, so every C++ QPixmapCache behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPixmapCache that has a ritual and that Python can
  call so far, 6 names in all: 'cacheLimit', 'setCacheLimit', 'find',
  'insert', 'remove', 'clear'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QPixmapCache::find(const Key &key, QPixmap *pixmap)': names
    'QPixmapCache::Key', which has no cute class yet.
  - Qt's 'Key QPixmapCache::insert(const QPixmap &pixmap)': gives
    'QPixmapCache::Key', which has no cute class yet.
  - Qt's 'bool QPixmapCache::replace(const Key &key, const QPixmap &pixmap)':
    names 'QPixmapCache::Key', which has no cute class yet.
  - Qt's 'void QPixmapCache::remove(const Key &key)': names
    'QPixmapCache::Key', which has no cute class yet.
  - Qt's 'QPixmapCache::~QPixmapCache()': the destructor: Python removes its
    C++ QPixmapCache by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QPixmapCache is created at the first use, not by
    'QPixmapCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPixmapCache back gives a copy the ritual made for
    Python, in a new cute QPixmapCache.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def cacheLimit() -> int:
    """
    Calls Qt's 'int QPixmapCache::cacheLimit()'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapcache.html#cacheLimit
    """
    #  int QPixmapCache::cacheLimit()
    return Rituals.call('ritual_ZN12QPixmapCache10cacheLimitEv')

  @staticmethod
  @overload(int)
  def setCacheLimit(a0: int) -> None:
    """
    Calls Qt's 'void QPixmapCache::setCacheLimit(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapcache.html#setCacheLimit

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QPixmapCache::setCacheLimit(int a0)
    Rituals.call('ritual_ZN12QPixmapCache13setCacheLimitEi', a0)

  @staticmethod
  @overload(str, QPixmap)
  @overload(str, NoneType)
  def find(key: str, pixmap: Optional[QPixmap]) -> bool:
    """
    Calls Qt's 'bool QPixmapCache::find(const QString &key, QPixmap
    *pixmap)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapcache.html#find

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    pixmap : Optional[QPixmap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPixmapCache::find(const QString &key, QPixmap *pixmap)
    return Rituals.call(
        'ritual_ZN12QPixmapCache4findERK7QStringP7QPixmap',
        key, CuteMixin._addressOf(pixmap),
    )

  @staticmethod
  @overload(str, QPixmap)
  def insert(key: str, pixmap: QPixmap) -> bool:
    """
    Calls Qt's 'bool QPixmapCache::insert(const QString &key, const QPixmap
    &pixmap)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapcache.html#insert

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  bool QPixmapCache::insert(const QString &key, const QPixmap &pixmap)
    return Rituals.call(
        'ritual_ZN12QPixmapCache6insertERK7QStringRK7QPixmap',
        key, CuteMixin._valueOf(pixmap),
    )

  @staticmethod
  @overload(str)
  def remove(key: str) -> None:
    """
    Calls Qt's 'void QPixmapCache::remove(const QString &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapcache.html#remove

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPixmapCache::remove(const QString &key)
    Rituals.call('ritual_ZN12QPixmapCache6removeERK7QString', key)

  @staticmethod
  def clear() -> None:
    """
    Calls Qt's 'void QPixmapCache::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapcache.html#clear
    """
    #  void QPixmapCache::clear()
    Rituals.call('ritual_ZN12QPixmapCache5clearEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPixmapCache'

  #  Qt's '~QPixmapCache()'. Naming it makes this a value class: Python owns
  #  every C++ QPixmapCache behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QPixmapCacheD1Ev'

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
