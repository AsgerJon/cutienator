"""
QQmlLoggingCategory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlMeta/6.12.0/QtQmlMeta/private/qqmlloggingcategory_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlLoggingCategory to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlLoggingCategoryBase, QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlLoggingCategory(QQmlLoggingCategoryBase, QQmlParserStatus):
  """
  The cute side of Qt's QQmlLoggingCategory: a plain Python object standing
  in front of one C++ QQmlLoggingCategory.

  It is built on the cute 'QQmlLoggingCategoryBase', as Qt's
  QQmlLoggingCategory is built on Qt's QQmlLoggingCategoryBase, and has
  everything that class has. It is built on the cute 'QQmlParserStatus' as
  well, as Qt's QQmlLoggingCategory is built on Qt's QQmlParserStatus too,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlLoggingCategory that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr',
  'defaultLogLevel', 'setDefaultLogLevel', 'name', 'setName', 'classBegin',
  'componentComplete', 'forceCompletion'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlLoggingCategory::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQmlLoggingCategory::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlLoggingCategory::~QQmlLoggingCategory()': the destructor:
    Python never removes a C++ QQmlLoggingCategory.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlLoggingCategory is created at the first use, not by
    'QQmlLoggingCategory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlLoggingCategory.
  - Qt tells when it has removed the C++ QQmlLoggingCategory. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQmlLoggingCategory, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class DefaultLogLevel(CuteNum):
    """
    The enum 'QQmlLoggingCategory::DefaultLogLevel' of Qt, with the 5 names
    Qt gives in it.
    """

    Debug = Kee[int](0)
    Info = Kee[int](4)
    Warning = Kee[int](1)
    Critical = Kee[int](2)
    Fatal = Kee[int](3)

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
    Calls Qt's 'QString QQmlLoggingCategory::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlloggingcategory.html#tr

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
    #  QString QQmlLoggingCategory::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQmlLoggingCategory2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlLoggingCategory'

  #  Qt's QQmlLoggingCategory is built on more than one class. The part of a
  #  C++ QQmlLoggingCategory that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QQmlLoggingCategory_QQmlParserStatus',
  }

  #  A C++ QQmlLoggingCategory Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlLoggingCategory'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlLoggingCategory::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlloggingcategory.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlLoggingCategory::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQmlLoggingCategory10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def defaultLogLevel(self) -> DefaultLogLevel:
    """
    Calls Qt's 'DefaultLogLevel QQmlLoggingCategory::defaultLogLevel()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlloggingcategory.html#defaultLogLevel

    Returns
    -------

    DefaultLogLevel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'DefaultLogLevel(number)'
      gives.
    """
    #  DefaultLogLevel QQmlLoggingCategory::defaultLogLevel() const
    return QQmlLoggingCategory.DefaultLogLevel(self.uglySide.call(
        'ritual_ZNK19QQmlLoggingCategory15defaultLogLevelEv',
    ))

  def name(self) -> str:
    """
    Calls Qt's 'QString QQmlLoggingCategory::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlloggingcategory.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlLoggingCategory::name() const
    return self.uglySide.call('ritual_ZNK19QQmlLoggingCategory4nameEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(DefaultLogLevel)
  def setDefaultLogLevel(self, defaultLogLevel: DefaultLogLevel) -> None:
    """
    Calls Qt's 'void QQmlLoggingCategory::setDefaultLogLevel(DefaultLogLevel
    defaultLogLevel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlloggingcategory.html#setDefaultLogLevel

    Parameters
    ----------

    defaultLogLevel : DefaultLogLevel
      Passed on as its number.
    """
    #  void QQmlLoggingCategory::setDefaultLogLevel(DefaultLogLevel
    #      defaultLogLevel)
    self.uglySide.call(
        'ritual_ZN19QQmlLoggingCategory18setDefaultLogLevelENS_15DefaultLog'
        'LevelE',
        defaultLogLevel.value,
    )

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QQmlLoggingCategory::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlloggingcategory.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlLoggingCategory::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN19QQmlLoggingCategory7setNameERK7QString', name,
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
    'QQmlLoggingCategory::QQmlLoggingCategory(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlloggingcategory.html#QQmlLoggingCategory

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlLoggingCategory::QQmlLoggingCategory(QObject *parent)
    self._noteCreation(QQmlLoggingCategory, lambda: Rituals.call(
        'ritual_ZN19QQmlLoggingCategoryC1EP7QObject',
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

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQmlLoggingCategory::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlloggingcategory.html#classBegin
    """
    #  void QQmlLoggingCategory::classBegin()
    ritual = 'ritual_ZN19QQmlLoggingCategory10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlLoggingCategory10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQmlLoggingCategory::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlloggingcategory.html#componentComplete
    """
    #  void QQmlLoggingCategory::componentComplete()
    ritual = 'ritual_ZN19QQmlLoggingCategory17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQmlLoggingCategory17componentCompleteEv'
    self.uglySide.call(ritual)

  def forceCompletion(self) -> None:
    """
    Calls Qt's 'void QQmlLoggingCategory::forceCompletion()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlloggingcategory.html#forceCompletion
    """
    #  void QQmlLoggingCategory::forceCompletion()
    self.uglySide.call('ritual_ZN19QQmlLoggingCategory15forceCompletionEv')
