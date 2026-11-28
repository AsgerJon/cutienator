"""
QV4::PersistentValueStorage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4persistent_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::PersistentValueStorage to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PersistentValueStorage(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::PersistentValueStorage: a plain Python object
  standing in front of one C++ QV4::PersistentValueStorage.

  C++ hands a QV4::PersistentValueStorage around as a copy, so every C++
  QV4::PersistentValueStorage behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QV4::PersistentValueStorage that has a ritual and
  that Python can call so far, 6 names in all: 'allocate', 'free', 'mark',
  'clearFreePageHint', 'getEngine', 'freeUnchecked'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::PersistentValueStorage::~PersistentValueStorage()': the
    destructor: Python removes its C++ QV4::PersistentValueStorage by it, and
    has no other use for it.
  - Qt's 'void QV4::PersistentValueStorage::freePage(void *page)': names
    'void', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 leans on 'QV4.

  What to expect
  --------------

  - The C++ QV4::PersistentValueStorage is created at the first use, not by
    'QV4::PersistentValueStorage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::PersistentValueStorage back gives a copy the
    ritual made for Python, in a new cute QV4::PersistentValueStorage.
  - Each name of Qt's QV4::PersistentValueStorage that has no cute function
    yet, 'begin', 'end', 'freePage', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QV4::PersistentValueStorage, each a class
  #  in here as in C++.

  class Iterator(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::PersistentValueStorage::Iterator: a plain
    Python object standing in front of one C++
    QV4::PersistentValueStorage::Iterator.

    What exists
    -----------

    Every function of Qt's QV4::PersistentValueStorage::Iterator that has a
    ritual and that Python can call so far, 1 name in all: '__ne__'. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has no ritual
    ------------------

    6 of the 7 functions Qt declares: 6 Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file.

    What to expect
    --------------

    - The C++ QV4::PersistentValueStorage::Iterator is created at the first
      use, not by 'QV4::PersistentValueStorage::Iterator(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QV4::PersistentValueStorage::Iterator.
    - Each name of Qt's QV4::PersistentValueStorage::Iterator that has no
      cute function yet, '__init__', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::PersistentValueStorage::Iterator'

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
    def __ne__(self, other: PersistentValueStorage.Iterator) -> bool:
      """
      Calls Qt's 'bool
      QV4::PersistentValueStorage::Iterator::operator!=(const Iterator
      &other)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-persistentvaluestorage-iterator.html

      Parameters
      ----------

      other : PersistentValueStorage.Iterator
        Passed on as a value: Qt reads the C++
        QV4::PersistentValueStorage::Iterator, which stays Python's own.
      """
      #  bool QV4::PersistentValueStorage::Iterator::operator!=(const
      #      Iterator &other)
      return self.uglySide.call(
          'ritual_ZN3QV422PersistentValueStorage8IteratorneERKS1_',
          self._valueOf(other),
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

    @staticmethod
    def __init__(*__, **_) -> Never:
      """
      - Qt's 'QV4::PersistentValueStorage::Iterator::Iterator(const Iterator
        &o)': Qt's library has no name for it, and its code in Qt's source
        does not compile apart from its file: unknown type name 'Page'.
      - Qt's 'QV4::PersistentValueStorage::Iterator::Iterator(void *p, int
        idx)': Qt's library has no name for it, and its code in Qt's source
        does not compile apart from its file: member access into incomplete
        type 'Page'.
      """
      raise NotImplementedError(
          "'QV4.PersistentValueStorage.Iterator.__init__' has no cute "
          "function yet. Qt's "
          "'QV4::PersistentValueStorage::Iterator::Iterator(const Iterator "
          "&o)': Qt's library has no name for it, and its code in Qt's "
          "source does not compile apart from its file: unknown type name "
          "'Page'. Qt's "
          "'QV4::PersistentValueStorage::Iterator::Iterator(void *p, int "
          "idx)': Qt's library has no name for it, and its code in Qt's "
          "source does not compile apart from its file: member access into "
          "incomplete type 'Page'.")

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
  @overload(WAIT['QV4.Value'])
  @overload(NoneType)
  def free(v: Optional[QV4.Value]) -> None:
    """
    Calls Qt's 'void QV4::PersistentValueStorage::free(Value *v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-persistentvaluestorage.html#free

    Parameters
    ----------

    v : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::PersistentValueStorage::free(Value *v)
    Rituals.call(
        'ritual_ZN3QV422PersistentValueStorage4freeEPNS_5ValueE',
        CuteMixin._addressOf(v),
    )

  @staticmethod
  @overload(WAIT['QV4.Value'])
  @overload(NoneType)
  def getEngine(v: Optional[QV4.Value]) -> Optional[QV4.ExecutionEngine]:
    """
    Calls Qt's 'ExecutionEngine *QV4::PersistentValueStorage::getEngine(const
    Value *v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-persistentvaluestorage.html#getEngine

    Parameters
    ----------

    v : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.ExecutionEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ExecutionEngine *QV4::PersistentValueStorage::getEngine(const Value
    #      *v)
    address = Rituals.call(
        'ritual_ZN3QV422PersistentValueStorage9getEngineEPKNS_5ValueE',
        CuteMixin._addressOf(v),
    )
    return QV4.ExecutionEngine._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.Value'])
  @overload(NoneType)
  def freeUnchecked(v: Optional[QV4.Value]) -> None:
    """
    Calls Qt's 'void QV4::PersistentValueStorage::freeUnchecked(Value *v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-persistentvaluestorage.html#freeUnchecked

    Parameters
    ----------

    v : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::PersistentValueStorage::freeUnchecked(Value *v)
    Rituals.call(
        'ritual_ZN3QV422PersistentValueStorage13freeUncheckedEPNS_5ValueE',
        CuteMixin._addressOf(v),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::PersistentValueStorage'

  #  Qt's '~QV4::PersistentValueStorage()'. Naming it makes this a value
  #  class: Python owns every C++ QV4::PersistentValueStorage behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV422PersistentValueStorageD1Ev'

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

  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def __init__(self, engine: Optional[QV4.ExecutionEngine]) -> None:
    """
    Notes what was given, for Qt's
    'QV4::PersistentValueStorage::PersistentValueStorage(ExecutionEngine
    *engine)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-persistentvaluestorage.html

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QV4::PersistentValueStorage::PersistentValueStorage(ExecutionEngine
    #      *engine)
    self._noteCreation(PersistentValueStorage, lambda: Rituals.call(
        'ritual_ZN3QV422PersistentValueStorageC1EPNS_15ExecutionEngineE',
        self._addressOf(engine),
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

  def allocate(self) -> Optional[QV4.Value]:
    """
    Calls Qt's 'Value *QV4::PersistentValueStorage::allocate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-persistentvaluestorage.html#allocate

    Returns
    -------

    Optional[QV4.Value]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Value *QV4::PersistentValueStorage::allocate()
    address = self.uglySide.call(
        'ritual_ZN3QV422PersistentValueStorage8allocateEv',
    )
    return QV4.Value._cuteAt(address)

  @overload(WAIT['QV4.MarkStack'])
  @overload(NoneType)
  def mark(self, markStack: Optional[QV4.MarkStack]) -> None:
    """
    Calls Qt's 'void QV4::PersistentValueStorage::mark(MarkStack
    *markStack)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-persistentvaluestorage.html#mark

    Parameters
    ----------

    markStack : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::PersistentValueStorage::mark(MarkStack *markStack)
    self.uglySide.call(
        'ritual_ZN3QV422PersistentValueStorage4markEPNS_9MarkStackE',
        self._addressOf(markStack),
    )

  def clearFreePageHint(self) -> None:
    """
    Calls Qt's 'void QV4::PersistentValueStorage::clearFreePageHint()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-persistentvaluestorage.html#clearFreePageHint
    """
    #  void QV4::PersistentValueStorage::clearFreePageHint()
    self.uglySide.call(
        'ritual_ZN3QV422PersistentValueStorage17clearFreePageHintEv',
    )

  @staticmethod
  def begin(*__, **_) -> Never:
    """
    Qt's 'Iterator QV4::PersistentValueStorage::begin()': leans on
    'QV4::PersistentValueStorage::Iterator::Iterator(void*, int)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QV4.PersistentValueStorage.begin' has no cute function yet. Qt's "
        "'Iterator QV4::PersistentValueStorage::begin()': leans on "
        "'QV4::PersistentValueStorage::Iterator::Iterator(void*, int)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def end(*__, **_) -> Never:
    """
    Qt's 'Iterator QV4::PersistentValueStorage::end()': leans on
    'QV4::PersistentValueStorage::Iterator::Iterator(void*, int)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QV4.PersistentValueStorage.end' has no cute function yet. Qt's "
        "'Iterator QV4::PersistentValueStorage::end()': leans on "
        "'QV4::PersistentValueStorage::Iterator::Iterator(void*, int)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def freePage(*__, **_) -> Never:
    """
    Qt's 'void QV4::PersistentValueStorage::freePage(void *page)': names
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.PersistentValueStorage.freePage' has no cute function yet. "
        "Qt's 'void QV4::PersistentValueStorage::freePage(void *page)': "
        "names 'void', which has no cute class yet.")
