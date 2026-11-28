"""
QVirtualKeyboardDictionaryManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtVirtualKeyboard/qvirtualkeyboarddictionarymanager.h, Qt 6.12.0. Changes
#  made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QVirtualKeyboardDictionary

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QVirtualKeyboardDictionaryManager(QObject):
  """
  The cute side of Qt's QVirtualKeyboardDictionaryManager: a plain Python
  object standing in front of one C++ QVirtualKeyboardDictionaryManager.

  It is built on the cute 'QObject', as Qt's
  QVirtualKeyboardDictionaryManager is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QVirtualKeyboardDictionaryManager that has a ritual
  and that Python can call so far, 15 names in all: 'metaObject', 'tr',
  'instance', 'availableDictionaries', 'baseDictionaries',
  'setBaseDictionaries', 'extraDictionaries', 'setExtraDictionaries',
  'activeDictionaries', 'createDictionary', 'dictionary',
  'availableDictionariesChanged', 'baseDictionariesChanged',
  'extraDictionariesChanged', 'activeDictionariesChanged'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QVirtualKeyboardDictionaryManager::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QVirtualKeyboardDictionaryManager::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QVirtualKeyboardDictionaryManagerPrivate
    *QVirtualKeyboardDictionaryManager::d_func()': gives
    'QVirtualKeyboardDictionaryManagerPrivate', which has no cute class yet.
  - Qt's 'const QVirtualKeyboardDictionaryManagerPrivate
    *QVirtualKeyboardDictionaryManager::d_func() const': gives
    'QVirtualKeyboardDictionaryManagerPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 24 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QVirtualKeyboardDictionaryManager is created at the first use,
    not by 'QVirtualKeyboardDictionaryManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVirtualKeyboardDictionaryManager.
  - Qt tells when it has removed the C++ QVirtualKeyboardDictionaryManager.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QVirtualKeyboardDictionaryManager::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboarddictionarymanager.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QVirtualKeyboardDictionaryManager::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN33QVirtualKeyboardDictionaryManager2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def instance() -> Optional[QVirtualKeyboardDictionaryManager]:
    """
    Calls Qt's 'QVirtualKeyboardDictionaryManager
    *QVirtualKeyboardDictionaryManager::instance()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboarddictionarymanager.html#instance

    Returns
    -------

    Optional[QVirtualKeyboardDictionaryManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVirtualKeyboardDictionaryManager
    #      *QVirtualKeyboardDictionaryManager::instance()
    address = Rituals.call(
        'ritual_ZN33QVirtualKeyboardDictionaryManager8instanceEv',
    )
    return QVirtualKeyboardDictionaryManager._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVirtualKeyboardDictionaryManager'

  #  A C++ QVirtualKeyboardDictionaryManager Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVirtualKeyboardDictionaryManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QVirtualKeyboardDictionaryManager::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboarddictionarymanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QVirtualKeyboardDictionaryManager::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK33QVirtualKeyboardDictionaryManager10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def availableDictionaries(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    QVirtualKeyboardDictionaryManager::availableDictionaries() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboarddictionarymanager.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QVirtualKeyboardDictionaryManager::availableDictionaries()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK33QVirtualKeyboardDictionaryManager21availableDictionari'
        'esEv',
    )
    return QStringList._cuteOwning(address)

  def baseDictionaries(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    QVirtualKeyboardDictionaryManager::baseDictionaries() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboarddictionarymanager.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QVirtualKeyboardDictionaryManager::baseDictionaries()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK33QVirtualKeyboardDictionaryManager16baseDictionariesEv',
    )
    return QStringList._cuteOwning(address)

  def extraDictionaries(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    QVirtualKeyboardDictionaryManager::extraDictionaries() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboarddictionarymanager.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QVirtualKeyboardDictionaryManager::extraDictionaries()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK33QVirtualKeyboardDictionaryManager17extraDictionariesEv',
    )
    return QStringList._cuteOwning(address)

  def activeDictionaries(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    QVirtualKeyboardDictionaryManager::activeDictionaries() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboarddictionarymanager.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QVirtualKeyboardDictionaryManager::activeDictionaries()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK33QVirtualKeyboardDictionaryManager18activeDictionariesE'
        'v',
    )
    return QStringList._cuteOwning(address)

  @overload(str)
  def dictionary(self, name: str) -> Optional[QVirtualKeyboardDictionary]:
    """
    Calls Qt's 'QVirtualKeyboardDictionary
    *QVirtualKeyboardDictionaryManager::dictionary(const QString &name)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboarddictionarymanager.html#dictionary

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QVirtualKeyboardDictionary]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVirtualKeyboardDictionary
    #      *QVirtualKeyboardDictionaryManager::dictionary(const QString
    #      &name) const
    address = self.uglySide.call(
        'ritual_ZNK33QVirtualKeyboardDictionaryManager10dictionaryERK7QStri'
        'ng',
        name,
    )
    from . import QVirtualKeyboardDictionary
    return QVirtualKeyboardDictionary._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStringList)
  def setBaseDictionaries(self, baseDictionaries: QStringList) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardDictionaryManager::setBaseDictionaries(const QStringList
    &baseDictionaries)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboarddictionarymanager.html

    Parameters
    ----------

    baseDictionaries : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QVirtualKeyboardDictionaryManager::setBaseDictionaries(const
    #      QStringList &baseDictionaries)
    self.uglySide.call(
        'ritual_ZN33QVirtualKeyboardDictionaryManager19setBaseDictionariesE'
        'RK5QListI7QStringE',
        self._valueOf(baseDictionaries),
    )

  @overload(QStringList)
  def setExtraDictionaries(self, extraDictionaries: QStringList) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardDictionaryManager::setExtraDictionaries(const QStringList
    &extraDictionaries)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboarddictionarymanager.html

    Parameters
    ----------

    extraDictionaries : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QVirtualKeyboardDictionaryManager::setExtraDictionaries(const
    #      QStringList &extraDictionaries)
    self.uglySide.call(
        'ritual_ZN33QVirtualKeyboardDictionaryManager20setExtraDictionaries'
        'ERK5QListI7QStringE',
        self._valueOf(extraDictionaries),
    )

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QVirtualKeyboardDictionaryManager::QVirtualKeyboardDictionaryManager(
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboarddictionarymanager.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QVirtualKeyboardDictionaryManager::
    #      QVirtualKeyboardDictionaryManager(QObject *parent)
    self._noteCreation(
        QVirtualKeyboardDictionaryManager, lambda: Rituals.call(
            'ritual_ZN33QVirtualKeyboardDictionaryManagerC1EP7QObject',
            self._addressOf(parent, 'QObject'),
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

  @overload(str)
  def createDictionary(
      self,
      name: str,
  ) -> Optional[QVirtualKeyboardDictionary]:
    """
    Calls Qt's 'QVirtualKeyboardDictionary
    *QVirtualKeyboardDictionaryManager::createDictionary(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboarddictionarymanager.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QVirtualKeyboardDictionary]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVirtualKeyboardDictionary
    #      *QVirtualKeyboardDictionaryManager::createDictionary(const QString
    #      &name)
    address = self.uglySide.call(
        'ritual_ZN33QVirtualKeyboardDictionaryManager16createDictionaryERK7'
        'QString',
        name,
    )
    from . import QVirtualKeyboardDictionary
    return QVirtualKeyboardDictionary._cuteAt(address)

  def availableDictionariesChanged(self) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardDictionaryManager::availableDictionariesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboarddictionarymanager.html
    """
    #  void QVirtualKeyboardDictionaryManager::availableDictionariesChanged()
    self.uglySide.call(
        'ritual_ZN33QVirtualKeyboardDictionaryManager28availableDictionarie'
        'sChangedEv',
    )

  def baseDictionariesChanged(self) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardDictionaryManager::baseDictionariesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboarddictionarymanager.html
    """
    #  void QVirtualKeyboardDictionaryManager::baseDictionariesChanged()
    self.uglySide.call(
        'ritual_ZN33QVirtualKeyboardDictionaryManager23baseDictionariesChan'
        'gedEv',
    )

  def extraDictionariesChanged(self) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardDictionaryManager::extraDictionariesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboarddictionarymanager.html
    """
    #  void QVirtualKeyboardDictionaryManager::extraDictionariesChanged()
    self.uglySide.call(
        'ritual_ZN33QVirtualKeyboardDictionaryManager24extraDictionariesCha'
        'ngedEv',
    )

  def activeDictionariesChanged(self) -> None:
    """
    Calls Qt's 'void
    QVirtualKeyboardDictionaryManager::activeDictionariesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvirtualkeyboarddictionarymanager.html
    """
    #  void QVirtualKeyboardDictionaryManager::activeDictionariesChanged()
    self.uglySide.call(
        'ritual_ZN33QVirtualKeyboardDictionaryManager25activeDictionariesCh'
        'angedEv',
    )
