"""
QQmlTypeNameCache binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmltypenamecache_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlTypeNameCache to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QUrl
  from . import QHashedString, QHashedStringRef, QQmlImportRef, QQmlType
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QHashedString = WAIT['QHashedString']
  QHashedStringRef = WAIT['QHashedStringRef']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlTypeNameCache(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlTypeNameCache: a plain Python object standing in
  front of one C++ QQmlTypeNameCache.

  What exists
  -----------

  Every function of Qt's QQmlTypeNameCache that has a ritual and that Python
  can call so far, 4 names in all: 'isEmpty', 'add', 'toHashedStringRef',
  'toQString'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlTypeNameCache::QQmlTypeNameCache(const
    QQmlRefPointer<QQmlImports> &imports)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QQmlTypeNameCache::~QQmlTypeNameCache()': the destructor: Python
    never removes a C++ QQmlTypeNameCache.

  What has no ritual
  ------------------

  9 of the 18 functions Qt declares: 9 a template.

  What to expect
  --------------

  - The C++ QQmlTypeNameCache is created at the first use, not by
    'QQmlTypeNameCache(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlTypeNameCache.
  - Each name of Qt's QQmlTypeNameCache that has no cute function yet,
    '__init__', 'doQuery', 'query', 'typeSearch', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlTypeNameCache, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class QueryNamespaced(CuteNum, scoped=True):
    """
    The enum 'QQmlTypeNameCache::QueryNamespaced' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    No = Kee[int](0)
    Yes = Kee[int](1)

  #  The classes Qt writes inside QQmlTypeNameCache, each a class in here as
  #  in C++.

  class Result(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlTypeNameCache::Result: a plain Python object
    standing in front of one C++ QQmlTypeNameCache::Result.

    C++ hands a QQmlTypeNameCache::Result around as a copy, so every C++
    QQmlTypeNameCache::Result behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QQmlTypeNameCache::Result that has a ritual and
    that Python can call so far, 1 name in all: 'isValid'. It can be made
    from Python, in 4 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlTypeNameCache::Result::~Result()': the destructor: Python
      removes its C++ QQmlTypeNameCache::Result by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QQmlTypeNameCache::Result is created at the first use, not by
      'QQmlTypeNameCache::Result(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlTypeNameCache::Result back gives a copy the
      ritual made for Python, in a new cute QQmlTypeNameCache::Result.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QQmlImportRef = WAIT['QQmlImportRef']
      QQmlType = WAIT['QQmlType']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlTypeNameCache::Result'

    #  Qt's '~QQmlTypeNameCache::Result()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlTypeNameCache::Result behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN17QQmlTypeNameCache6ResultD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isValid(self) -> bool:
      """
      Calls Qt's 'bool QQmlTypeNameCache::Result::isValid() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmltypenamecache-result.html#isValid
      """
      #  bool QQmlTypeNameCache::Result::isValid() const
      return self.uglySide.call(
          'ritual_ZNK17QQmlTypeNameCache6Result7isValidEv',
      )

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
      Notes what was given, for Qt's 'QQmlTypeNameCache::Result::Result()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmltypenamecache-result.html#Result
      """
      #  QQmlTypeNameCache::Result::Result()
      self._noteCreation(QQmlTypeNameCache.Result, lambda: Rituals.call(
          'ritual_ZN17QQmlTypeNameCache6ResultC1Ev',
      ))

    @overload(QQmlImportRef)
    @overload(NoneType)
    def __init__(self, importNamespace: Optional[QQmlImportRef]) -> None:
      """
      Notes what was given, for Qt's 'QQmlTypeNameCache::Result::Result(const
      QQmlImportRef *importNamespace)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmltypenamecache-result.html#Result

      Parameters
      ----------

      importNamespace : Optional[QQmlImportRef]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QQmlTypeNameCache::Result::Result(const QQmlImportRef
      #      *importNamespace)
      self._noteCreation(QQmlTypeNameCache.Result, lambda: Rituals.call(
          'ritual_ZN17QQmlTypeNameCache6ResultC1EPK13QQmlImportRef',
          self._addressOf(importNamespace),
      ))

    @overload(QQmlType)
    def __init__(self, type: QQmlType) -> None:
      """
      Notes what was given, for Qt's 'QQmlTypeNameCache::Result::Result(const
      QQmlType &type)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmltypenamecache-result.html#Result

      Parameters
      ----------

      type : QQmlType
        Passed on as a value: Qt reads the C++ QQmlType, which stays Python's
        own.
      """
      #  QQmlTypeNameCache::Result::Result(const QQmlType &type)
      self._noteCreation(QQmlTypeNameCache.Result, lambda: Rituals.call(
          'ritual_ZN17QQmlTypeNameCache6ResultC1ERK8QQmlType',
          self._valueOf(type),
      ))

    @overload(int)
    def __init__(self, scriptIndex: int) -> None:
      """
      Notes what was given, for Qt's 'QQmlTypeNameCache::Result::Result(int
      scriptIndex)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmltypenamecache-result.html#Result

      Parameters
      ----------

      scriptIndex : int
        Passed on as it is.
      """
      #  QQmlTypeNameCache::Result::Result(int scriptIndex)
      self._noteCreation(QQmlTypeNameCache.Result, lambda: Rituals.call(
          'ritual_ZN17QQmlTypeNameCache6ResultC1Ei', scriptIndex,
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
  @overload(QHashedStringRef)
  def toHashedStringRef(key: QHashedStringRef) -> QHashedStringRef:
    """
    Calls Qt's 'QHashedStringRef QQmlTypeNameCache::toHashedStringRef(const
    QHashedStringRef &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypenamecache.html#toHashedStringRef

    Parameters
    ----------

    key : QHashedStringRef
      Passed on as a value: Qt reads the C++ QHashedStringRef, which stays
      Python's own.

    Returns
    -------

    QHashedStringRef
      A new cute QHashedStringRef around the copy Qt gave back. Python owns
      it.
    """
    #  QHashedStringRef QQmlTypeNameCache::toHashedStringRef(const
    #      QHashedStringRef &key)
    address = Rituals.call(
        'ritual_ZN17QQmlTypeNameCache17toHashedStringRefERK16QHashedStringR'
        'ef',
        CuteMixin._valueOf(key),
    )
    from . import QHashedStringRef
    return QHashedStringRef._cuteOwning(address)

  @staticmethod
  @overload(WAIT['QV4.String'])
  @overload(NoneType)
  def toHashedStringRef(key: Optional[QV4.String]) -> QHashedStringRef:
    """
    Calls Qt's 'QHashedStringRef QQmlTypeNameCache::toHashedStringRef(const
    QV4::String *key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmltypenamecache.html#toHashedStringRef

    Parameters
    ----------

    key : Optional[QV4.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QHashedStringRef
      A new cute QHashedStringRef around the copy Qt gave back. Python owns
      it.
    """
    #  QHashedStringRef QQmlTypeNameCache::toHashedStringRef(const
    #      QV4::String *key)
    address = Rituals.call(
        'ritual_ZN17QQmlTypeNameCache17toHashedStringRefEPKN3QV46StringE',
        CuteMixin._addressOf(key),
    )
    from . import QHashedStringRef
    return QHashedStringRef._cuteOwning(address)

  @staticmethod
  @overload(QHashedStringRef)
  def toQString(key: QHashedStringRef) -> str:
    """
    Calls Qt's 'QString QQmlTypeNameCache::toQString(const QHashedStringRef
    &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypenamecache.html#toQString

    Parameters
    ----------

    key : QHashedStringRef
      Passed on as a value: Qt reads the C++ QHashedStringRef, which stays
      Python's own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlTypeNameCache::toQString(const QHashedStringRef &key)
    return Rituals.call(
        'ritual_ZN17QQmlTypeNameCache9toQStringERK16QHashedStringRef',
        CuteMixin._valueOf(key),
    )

  @staticmethod
  @overload(WAIT['QV4.String'])
  @overload(NoneType)
  def toQString(key: Optional[QV4.String]) -> str:
    """
    Calls Qt's 'QString QQmlTypeNameCache::toQString(const QV4::String
    *key)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypenamecache.html#toQString

    Parameters
    ----------

    key : Optional[QV4.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlTypeNameCache::toQString(const QV4::String *key)
    return Rituals.call(
        'ritual_ZN17QQmlTypeNameCache9toQStringEPKN3QV46StringE',
        CuteMixin._addressOf(key),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlTypeNameCache'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QQmlTypeNameCache::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypenamecache.html#isEmpty
    """
    #  bool QQmlTypeNameCache::isEmpty() const
    return self.uglySide.call('ritual_ZNK17QQmlTypeNameCache7isEmptyEv')

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQmlTypeNameCache::QQmlTypeNameCache(const
    QQmlRefPointer<QQmlImports> &imports)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTypeNameCache.__init__' has no cute function yet. Qt's "
        "'QQmlTypeNameCache::QQmlTypeNameCache(const "
        "QQmlRefPointer<QQmlImports> &imports)': takes a type Python has no "
        "way to hand over yet.")

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

  @overload(QHashedString)
  @overload(QHashedString, int)
  @overload(QHashedString, int, QHashedString)
  def add(
      self,
      name: QHashedString,
      sciptIndex: int = -1,
      nameSpace: Optional[QHashedString] = None,
  ) -> None:
    """
    Calls Qt's 'void QQmlTypeNameCache::add(const QHashedString &name, int
    sciptIndex, const QHashedString &nameSpace)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypenamecache.html#add

    Parameters
    ----------

    name : QHashedString
      Passed on as a value: Qt reads the C++ QHashedString, which stays
      Python's own.

    sciptIndex : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    nameSpace : Optional[QHashedString]
      Passed on as a value: Qt reads the C++ QHashedString, which stays
      Python's own. May be left out, as in Qt: a new 'QHashedString()' is
      then passed on.
    """
    #  void QQmlTypeNameCache::add(const QHashedString &name, int sciptIndex,
    #      const QHashedString &nameSpace)
    if nameSpace is None:
      from . import QHashedString
      nameSpace = QHashedString()
    self.uglySide.call(
        'ritual_ZN17QQmlTypeNameCache3addERK13QHashedStringiS2_',
        self._valueOf(name), sciptIndex, self._valueOf(nameSpace),
    )

  @overload(QHashedString, QUrl)
  @overload(QHashedString, QUrl, QHashedString)
  def add(
      self,
      name: QHashedString,
      url: QUrl,
      nameSpace: Optional[QHashedString] = None,
  ) -> None:
    """
    Calls Qt's 'void QQmlTypeNameCache::add(const QHashedString &name, const
    QUrl &url, const QHashedString &nameSpace)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltypenamecache.html#add

    Parameters
    ----------

    name : QHashedString
      Passed on as a value: Qt reads the C++ QHashedString, which stays
      Python's own.

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    nameSpace : Optional[QHashedString]
      Passed on as a value: Qt reads the C++ QHashedString, which stays
      Python's own. May be left out, as in Qt: a new 'QHashedString()' is
      then passed on.
    """
    #  void QQmlTypeNameCache::add(const QHashedString &name, const QUrl
    #      &url, const QHashedString &nameSpace)
    if nameSpace is None:
      from . import QHashedString
      nameSpace = QHashedString()
    self.uglySide.call(
        'ritual_ZN17QQmlTypeNameCache3addERK13QHashedStringRK4QUrlS2_',
        self._valueOf(name), self._valueOf(url), self._valueOf(nameSpace),
    )

  @staticmethod
  def doQuery(*__, **_) -> Never:
    """
    Qt's 'QQmlTypeNameCache::doQuery': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQmlTypeNameCache.doQuery' has no cute function yet. Qt's "
        "'QQmlTypeNameCache::doQuery': a template: a pattern and no single "
        "function.")

  @staticmethod
  def query(*__, **_) -> Never:
    """
    Qt's 'QQmlTypeNameCache::query': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQmlTypeNameCache.query' has no cute function yet. Qt's "
        "'QQmlTypeNameCache::query': a template: a pattern and no single "
        "function.")

  @staticmethod
  def typeSearch(*__, **_) -> Never:
    """
    Qt's 'QQmlTypeNameCache::typeSearch': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQmlTypeNameCache.typeSearch' has no cute function yet. Qt's "
        "'QQmlTypeNameCache::typeSearch': a template: a pattern and no "
        "single function.")
