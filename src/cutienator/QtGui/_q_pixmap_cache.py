"""
QPixmapCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qpixmapcache.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
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
  call so far, 7 names in all: 'cacheLimit', 'setCacheLimit', 'find',
  'insert', 'replace', 'remove', 'clear'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

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

  #  The classes Qt writes inside QPixmapCache, each a class in here as in
  #  C++.

  class Key(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QPixmapCache::Key: a plain Python object standing
    in front of one C++ QPixmapCache::Key.

    C++ hands a QPixmapCache::Key around as a copy, so every C++
    QPixmapCache::Key behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QPixmapCache::Key that has a ritual and that
    Python can call so far, 3 names in all: '__eq__', '__ne__', 'isValid'. It
    can be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QPixmapCache::Key::~Key()': the destructor: Python removes its
      C++ QPixmapCache::Key by it, and has no other use for it.

    What has no ritual
    ------------------

    5 of the 11 functions Qt declares: 4 takes or gives a type that cannot be
    passed yet; 1 private.

    What to expect
    --------------

    - The C++ QPixmapCache::Key is created at the first use, not by
      'QPixmapCache::Key(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QPixmapCache::Key back gives a copy the ritual made
      for Python, in a new cute QPixmapCache::Key.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QPixmapCache::Key'

    #  Qt's '~QPixmapCache::Key()'. Naming it makes this a value class:
    #  Python owns every C++ QPixmapCache::Key behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = 'ritual_ZN12QPixmapCache3KeyD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isValid(self) -> bool:
      """
      Calls Qt's 'bool QPixmapCache::Key::isValid() const'.

      Qt's own words: https://doc.qt.io/qt-6/qpixmapcache-key.html#isValid
      """
      #  bool QPixmapCache::Key::isValid() const
      return self.uglySide.call('ritual_ZNK12QPixmapCache3Key7isValidEv')

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(THIS)
    def __eq__(self, key: QPixmapCache.Key) -> bool:
      """
      Calls Qt's 'bool QPixmapCache::Key::operator==(const Key &key) const'.

      Qt's own words: https://doc.qt.io/qt-6/qpixmapcache-key.html#operator==

      Parameters
      ----------

      key : QPixmapCache.Key
        Passed on as a value: Qt reads the C++ QPixmapCache::Key, which stays
        Python's own.
      """
      #  bool QPixmapCache::Key::operator==(const Key &key) const
      return self.uglySide.call(
          'ritual_ZNK12QPixmapCache3KeyeqERKS0_', self._valueOf(key),
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
    def __ne__(self, key: QPixmapCache.Key) -> bool:
      """
      Calls Qt's 'bool QPixmapCache::Key::operator!=(const Key &key) const'.

      Qt's own words: https://doc.qt.io/qt-6/qpixmapcache-key.html#operator!=

      Parameters
      ----------

      key : QPixmapCache.Key
        Passed on as a value: Qt reads the C++ QPixmapCache::Key, which stays
        Python's own.
      """
      #  bool QPixmapCache::Key::operator!=(const Key &key) const
      return self.uglySide.call(
          'ritual_ZNK12QPixmapCache3KeyneERKS0_', self._valueOf(key),
      )

    @overload.fallback
    def __ne__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QPixmapCache::Key::Key()', which is
      called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qpixmapcache-key.html#Key
      """
      #  QPixmapCache::Key::Key()
      self._noteCreation(QPixmapCache.Key, lambda: Rituals.call(
          'ritual_ZN12QPixmapCache3KeyC1Ev',
      ))

    @overload(THIS)
    def __init__(self, other: QPixmapCache.Key) -> None:
      """
      Notes what was given, for Qt's 'QPixmapCache::Key::Key(const Key
      &other)', which is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qpixmapcache-key.html#Key

      Parameters
      ----------

      other : QPixmapCache.Key
        Passed on as a value: Qt reads the C++ QPixmapCache::Key, which stays
        Python's own.
      """
      #  QPixmapCache::Key::Key(const Key &other)
      self._noteCreation(QPixmapCache.Key, lambda: Rituals.call(
          'ritual_ZN12QPixmapCache3KeyC1ERKS0_', self._valueOf(other),
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
  @overload(Key, QPixmap)
  @overload(Key, NoneType)
  def find(key: Key, pixmap: Optional[QPixmap]) -> bool:
    """
    Calls Qt's 'bool QPixmapCache::find(const Key &key, QPixmap *pixmap)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapcache.html#find

    Parameters
    ----------

    key : Key
      Passed on as a value: Qt reads the C++ QPixmapCache::Key, which stays
      Python's own.

    pixmap : Optional[QPixmap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPixmapCache::find(const Key &key, QPixmap *pixmap)
    return Rituals.call(
        'ritual_ZN12QPixmapCache4findERKNS_3KeyEP7QPixmap',
        CuteMixin._valueOf(key), CuteMixin._addressOf(pixmap),
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
  @overload(QPixmap)
  def insert(pixmap: QPixmap) -> Key:
    """
    Calls Qt's 'Key QPixmapCache::insert(const QPixmap &pixmap)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapcache.html#insert

    Parameters
    ----------

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    Returns
    -------

    Key
      A new cute QPixmapCache::Key around the copy Qt gave back. Python owns
      it.
    """
    #  Key QPixmapCache::insert(const QPixmap &pixmap)
    address = Rituals.call(
        'ritual_ZN12QPixmapCache6insertERK7QPixmap',
        CuteMixin._valueOf(pixmap),
    )
    return QPixmapCache.Key._cuteOwning(address)

  @staticmethod
  @overload(Key, QPixmap)
  def replace(key: Key, pixmap: QPixmap) -> bool:
    """
    Calls Qt's 'bool QPixmapCache::replace(const Key &key, const QPixmap
    &pixmap)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapcache.html#replace

    Parameters
    ----------

    key : Key
      Passed on as a value: Qt reads the C++ QPixmapCache::Key, which stays
      Python's own.

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  bool QPixmapCache::replace(const Key &key, const QPixmap &pixmap)
    return Rituals.call(
        'ritual_ZN12QPixmapCache7replaceERKNS_3KeyERK7QPixmap',
        CuteMixin._valueOf(key), CuteMixin._valueOf(pixmap),
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
  @overload(Key)
  def remove(key: Key) -> None:
    """
    Calls Qt's 'void QPixmapCache::remove(const Key &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qpixmapcache.html#remove

    Parameters
    ----------

    key : Key
      Passed on as a value: Qt reads the C++ QPixmapCache::Key, which stays
      Python's own.
    """
    #  void QPixmapCache::remove(const Key &key)
    Rituals.call(
        'ritual_ZN12QPixmapCache6removeERKNS_3KeyE', CuteMixin._valueOf(key),
    )

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
