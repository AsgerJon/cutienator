"""
QFontCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qfont_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QFontCache to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QTimerEvent
  from . import QFontDef, QFontEngine, QFontEngineData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFontDef = WAIT['QFontDef']
  QFontEngine = WAIT['QFontEngine']
  QFontEngineData = WAIT['QFontEngineData']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFontCache(QObject):
  """
  The cute side of Qt's QFontCache: a plain Python object standing in front
  of one C++ QFontCache.

  It is built on the cute 'QObject', as Qt's QFontCache is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFontCache that has a ritual and that Python can
  call so far, 12 names in all: 'instance', 'cleanup', 'id', 'clear',
  'findEngineData', 'insertEngineData', 'findEngine', 'insertEngine',
  'increaseCost', 'decreaseCost', 'timerEvent', 'decreaseCache'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFontCache::~QFontCache()': the destructor: Python never removes a
    C++ QFontCache.
  - Qt's 'void QFontCache::updateHitCountAndTimeStamp(Engine &value)': takes
    a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QFontCache is created at the first use, not by 'QFontCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFontCache.
  - Qt tells when it has removed the C++ QFontCache. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QFontCache that has no cute function yet,
    'updateHitCountAndTimeStamp', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QFontCache, each a class in here as in C++.

  class Engine(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QFontCache::Engine: a plain Python object standing
    in front of one C++ QFontCache::Engine.

    C++ hands a QFontCache::Engine around as a copy, so every C++
    QFontCache::Engine behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QFontCache::Engine yet. It can be made from Python,
    in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QFontCache::Engine::~Engine()': the destructor: Python removes
      its C++ QFontCache::Engine by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QFontCache::Engine is created at the first use, not by
      'QFontCache::Engine(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QFontCache::Engine back gives a copy the ritual
      made for Python, in a new cute QFontCache::Engine.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QFontEngine = WAIT['QFontEngine']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QFontCache::Engine'

    #  Qt's '~QFontCache::Engine()'. Naming it makes this a value class:
    #  Python owns every C++ QFontCache::Engine behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN10QFontCache6EngineD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QFontCache::Engine::Engine()', which is
      called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qfontcache-engine.html#Engine
      """
      #  QFontCache::Engine::Engine()
      self._noteCreation(QFontCache.Engine, lambda: Rituals.call(
          'ritual_ZN10QFontCache6EngineC1Ev',
      ))

    @overload(QFontEngine)
    @overload(NoneType)
    def __init__(self, d: Optional[QFontEngine]) -> None:
      """
      Notes what was given, for Qt's 'QFontCache::Engine::Engine(QFontEngine
      *d)', which is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qfontcache-engine.html#Engine

      Parameters
      ----------

      d : Optional[QFontEngine]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QFontCache::Engine::Engine(QFontEngine *d)
      self._noteCreation(QFontCache.Engine, lambda: Rituals.call(
          'ritual_ZN10QFontCache6EngineC1EP11QFontEngine',
          self._addressOf(d),
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

  class Key(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QFontCache::Key: a plain Python object standing in
    front of one C++ QFontCache::Key.

    C++ hands a QFontCache::Key around as a copy, so every C++
    QFontCache::Key behind a cute one is Python's own: it is removed, by the
    ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QFontCache::Key that has a ritual and that Python
    can call so far, 2 names in all: '__lt__', '__eq__'. It can be made from
    Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QFontCache::Key::~Key()': the destructor: Python removes its C++
      QFontCache::Key by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QFontCache::Key is created at the first use, not by
      'QFontCache::Key(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QFontCache::Key back gives a copy the ritual made
      for Python, in a new cute QFontCache::Key.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QFontDef = WAIT['QFontDef']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QFontCache::Key'

    #  Qt's '~QFontCache::Key()'. Naming it makes this a value class: Python
    #  owns every C++ QFontCache::Key behind a cute one, and removes it by
    #  this ritual.
    __delete_ritual__ = 'ritual_ZN10QFontCache3KeyD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    def __lt__(self, other: QFontCache.Key) -> bool:
      """
      Calls Qt's 'bool QFontCache::Key::operator<(const Key &other) const'.

      Qt's own words: https://doc.qt.io/qt-6/qfontcache-key.html#operator<

      Parameters
      ----------

      other : QFontCache.Key
        Passed on as a value: Qt reads the C++ QFontCache::Key, which stays
        Python's own.
      """
      #  bool QFontCache::Key::operator<(const Key &other) const
      return self.uglySide.call(
          'ritual_ZNK10QFontCache3KeyltERKS0_', self._valueOf(other),
      )

    @overload.fallback
    def __lt__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    @overload(THIS)
    def __eq__(self, other: QFontCache.Key) -> bool:
      """
      Calls Qt's 'bool QFontCache::Key::operator==(const Key &other) const'.

      Qt's own words: https://doc.qt.io/qt-6/qfontcache-key.html#operator==

      Parameters
      ----------

      other : QFontCache.Key
        Passed on as a value: Qt reads the C++ QFontCache::Key, which stays
        Python's own.
      """
      #  bool QFontCache::Key::operator==(const Key &other) const
      return self.uglySide.call(
          'ritual_ZNK10QFontCache3KeyeqERKS0_', self._valueOf(other),
      )

    @overload.fallback
    def __eq__(self, *args: object) -> object:
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
      Notes what was given, for Qt's 'QFontCache::Key::Key()', which is
      called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qfontcache-key.html#Key
      """
      #  QFontCache::Key::Key()
      self._noteCreation(QFontCache.Key, lambda: Rituals.call(
          'ritual_ZN10QFontCache3KeyC1Ev',
      ))

    @overload(QFontDef, int)
    @overload(QFontDef, int, bool)
    def __init__(self, d: QFontDef, c: int, m: bool = False) -> None:
      """
      Notes what was given, for Qt's 'QFontCache::Key::Key(const QFontDef &d,
      uchar c, bool m)', which is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qfontcache-key.html#Key

      Parameters
      ----------

      d : QFontDef
        Passed on as a value: Qt reads the C++ QFontDef, which stays Python's
        own.

      c : int
        Passed on as it is.

      m : bool
        Passed on as it is. May be left out, as in Qt: it is then False.
      """
      #  QFontCache::Key::Key(const QFontDef &d, uchar c, bool m)
      self._noteCreation(QFontCache.Key, lambda: Rituals.call(
          'ritual_ZN10QFontCache3KeyC1ERK8QFontDefhb',
          self._valueOf(d), c, m,
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
  def instance() -> Optional[QFontCache]:
    """
    Calls Qt's 'QFontCache *QFontCache::instance()'.

    Qt's own words: https://doc.qt.io/qt-6/qfontcache.html#instance

    Returns
    -------

    Optional[QFontCache]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFontCache *QFontCache::instance()
    address = Rituals.call('ritual_ZN10QFontCache8instanceEv')
    return QFontCache._cuteAt(address)

  @staticmethod
  def cleanup() -> None:
    """
    Calls Qt's 'void QFontCache::cleanup()'.

    Qt's own words: https://doc.qt.io/qt-6/qfontcache.html#cleanup
    """
    #  void QFontCache::cleanup()
    Rituals.call('ritual_ZN10QFontCache7cleanupEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFontCache'

  #  A C++ QFontCache Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFontCache'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def id(self) -> int:
    """
    Calls Qt's 'int QFontCache::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontcache.html#id
    """
    #  int QFontCache::id() const
    return self.uglySide.call('ritual_ZNK10QFontCache2idEv')

  @overload(QFontDef)
  def findEngineData(self, def_: QFontDef) -> Optional[QFontEngineData]:
    """
    Calls Qt's 'QFontEngineData *QFontCache::findEngineData(const QFontDef
    &def) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontcache.html#findEngineData

    Parameters
    ----------

    def_ : QFontDef
      Passed on as a value: Qt reads the C++ QFontDef, which stays Python's
      own.

    Returns
    -------

    Optional[QFontEngineData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFontEngineData *QFontCache::findEngineData(const QFontDef &def) const
    address = self.uglySide.call(
        'ritual_ZNK10QFontCache14findEngineDataERK8QFontDef',
        self._valueOf(def_),
    )
    from . import QFontEngineData
    return QFontEngineData._cuteAt(address)

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
    Notes what was given, for Qt's 'QFontCache::QFontCache()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfontcache.html#QFontCache
    """
    #  QFontCache::QFontCache()
    self._noteCreation(QFontCache, lambda: Rituals.call(
        'ritual_ZN10QFontCacheC1Ev',
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QFontCache::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qfontcache.html#clear
    """
    #  void QFontCache::clear()
    self.uglySide.call('ritual_ZN10QFontCache5clearEv')

  @overload(QFontDef, QFontEngineData)
  @overload(QFontDef, NoneType)
  def insertEngineData(
      self,
      def_: QFontDef,
      engineData: Optional[QFontEngineData],
  ) -> None:
    """
    Calls Qt's 'void QFontCache::insertEngineData(const QFontDef &def,
    QFontEngineData *engineData)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontcache.html#insertEngineData

    Parameters
    ----------

    def_ : QFontDef
      Passed on as a value: Qt reads the C++ QFontDef, which stays Python's
      own.

    engineData : Optional[QFontEngineData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFontCache::insertEngineData(const QFontDef &def, QFontEngineData
    #      *engineData)
    self.uglySide.call(
        'ritual_ZN10QFontCache16insertEngineDataERK8QFontDefP15QFontEngineD'
        'ata',
        self._valueOf(def_), self._addressOf(engineData),
    )

  @overload(Key)
  def findEngine(self, key: Key) -> Optional[QFontEngine]:
    """
    Calls Qt's 'QFontEngine *QFontCache::findEngine(const Key &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontcache.html#findEngine

    Parameters
    ----------

    key : Key
      Passed on as a value: Qt reads the C++ QFontCache::Key, which stays
      Python's own.

    Returns
    -------

    Optional[QFontEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFontEngine *QFontCache::findEngine(const Key &key)
    address = self.uglySide.call(
        'ritual_ZN10QFontCache10findEngineERKNS_3KeyE', self._valueOf(key),
    )
    from . import QFontEngine
    return QFontEngine._cuteAt(address)

  @overload(Key, QFontEngine)
  @overload(Key, NoneType)
  @overload(Key, QFontEngine, bool)
  @overload(Key, NoneType, bool)
  def insertEngine(
      self,
      key: Key,
      engine: Optional[QFontEngine],
      insertMulti: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QFontCache::insertEngine(const Key &key, QFontEngine
    *engine, bool insertMulti)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontcache.html#insertEngine

    Parameters
    ----------

    key : Key
      Passed on as a value: Qt reads the C++ QFontCache::Key, which stays
      Python's own.

    engine : Optional[QFontEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    insertMulti : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QFontCache::insertEngine(const Key &key, QFontEngine *engine,
    #      bool insertMulti)
    self.uglySide.call(
        'ritual_ZN10QFontCache12insertEngineERKNS_3KeyEP11QFontEngineb',
        self._valueOf(key), self._addressOf(engine), insertMulti,
    )

  @overload(int)
  def increaseCost(self, cost: int) -> None:
    """
    Calls Qt's 'void QFontCache::increaseCost(uint cost)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontcache.html#increaseCost

    Parameters
    ----------

    cost : int
      Passed on as it is.
    """
    #  void QFontCache::increaseCost(uint cost)
    self.uglySide.call('ritual_ZN10QFontCache12increaseCostEj', cost)

  @overload(int)
  def decreaseCost(self, cost: int) -> None:
    """
    Calls Qt's 'void QFontCache::decreaseCost(uint cost)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontcache.html#decreaseCost

    Parameters
    ----------

    cost : int
      Passed on as it is.
    """
    #  void QFontCache::decreaseCost(uint cost)
    self.uglySide.call('ritual_ZN10QFontCache12decreaseCostEj', cost)

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QFontCache::timerEvent(QTimerEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontcache.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFontCache::timerEvent(QTimerEvent *event)
    ritual = 'ritual_ZN10QFontCache10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QFontCache10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def decreaseCache(self) -> None:
    """
    Calls Qt's 'void QFontCache::decreaseCache()'.

    Qt's own words: https://doc.qt.io/qt-6/qfontcache.html#decreaseCache
    """
    #  void QFontCache::decreaseCache()
    self.uglySide.call('ritual_ZN10QFontCache13decreaseCacheEv')

  @staticmethod
  def updateHitCountAndTimeStamp(*__, **_) -> Never:
    """
    Qt's 'void QFontCache::updateHitCountAndTimeStamp(Engine &value)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QFontCache.updateHitCountAndTimeStamp' has no cute function yet. "
        "Qt's 'void QFontCache::updateHitCountAndTimeStamp(Engine &value)': "
        "takes a type Python has no way to hand over yet.")
