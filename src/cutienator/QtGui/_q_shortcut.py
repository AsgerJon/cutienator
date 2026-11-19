"""
QShortcut binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qshortcut.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import Qt
from ._q_key_sequence import QKeySequence
from ..QtCore import QMetaObject
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QShortcut(QObject):
  """
  The cute side of Qt's QShortcut: a plain Python object standing in front of
  one C++ QShortcut.

  It is built on the cute 'QObject', as Qt's QShortcut is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QShortcut that has a ritual and that Python can call
  so far, 14 names in all: 'metaObject', 'tr', 'setKey', 'key', 'setKeys',
  'setEnabled', 'isEnabled', 'setContext', 'context', 'setAutoRepeat',
  'autoRepeat', 'id', 'setWhatsThis', 'whatsThis'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QShortcut::~QShortcut()': the destructor: Python never removes a
    C++ QShortcut.

  What has no ritual
  ------------------

  20 of the 38 functions Qt declares: 10 a template; 4 takes or gives a type
  that cannot be passed yet; 3 private; 2 a signal; 1 protected.

  What to expect
  --------------

  - The C++ QShortcut is created at the first use, not by 'QShortcut(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QShortcut.
  - Qt tells when it has removed the C++ QShortcut. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QShortcut::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qshortcut.html#tr

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
    #  QString QShortcut::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QShortcut2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QShortcut'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QShortcut::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qshortcut.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QShortcut::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QShortcut10metaObjectEv')
    return QMetaObject._cuteAt(address)

  def key(self) -> QKeySequence:
    """
    Calls Qt's 'QKeySequence QShortcut::key() const'.

    Qt's own words: https://doc.qt.io/qt-6/qshortcut.html#key

    Returns
    -------

    QKeySequence
      A new cute QKeySequence around the copy Qt gave back. Python owns it.
    """
    #  QKeySequence QShortcut::key() const
    address = self.uglySide.call('ritual_ZNK9QShortcut3keyEv')
    return QKeySequence._cuteOwning(address)

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QShortcut::isEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qshortcut.html#isEnabled
    """
    #  bool QShortcut::isEnabled() const
    return self.uglySide.call('ritual_ZNK9QShortcut9isEnabledEv')

  def context(self) -> Qt.ShortcutContext:
    """
    Calls Qt's 'Qt::ShortcutContext QShortcut::context() const'.

    Qt's own words: https://doc.qt.io/qt-6/qshortcut.html#context

    Returns
    -------

    Qt.ShortcutContext
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ShortcutContext(number)' gives.
    """
    #  Qt::ShortcutContext QShortcut::context() const
    return Qt.ShortcutContext(self.uglySide.call(
        'ritual_ZNK9QShortcut7contextEv',
    ))

  def autoRepeat(self) -> bool:
    """
    Calls Qt's 'bool QShortcut::autoRepeat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qshortcut.html#autoRepeat
    """
    #  bool QShortcut::autoRepeat() const
    return self.uglySide.call('ritual_ZNK9QShortcut10autoRepeatEv')

  def id(self) -> int:
    """
    Calls Qt's 'int QShortcut::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qshortcut.html#id
    """
    #  int QShortcut::id() const
    return self.uglySide.call('ritual_ZNK9QShortcut2idEv')

  def whatsThis(self) -> str:
    """
    Calls Qt's 'QString QShortcut::whatsThis() const'.

    Qt's own words: https://doc.qt.io/qt-6/qshortcut.html#whatsThis

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QShortcut::whatsThis() const
    return self.uglySide.call('ritual_ZNK9QShortcut9whatsThisEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QKeySequence)
  def setKey(self, key: QKeySequence) -> None:
    """
    Calls Qt's 'void QShortcut::setKey(const QKeySequence &key)'.

    Qt's own words: https://doc.qt.io/qt-6/qshortcut.html#setKey

    Parameters
    ----------

    key : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.
    """
    #  void QShortcut::setKey(const QKeySequence &key)
    self.uglySide.call(
        'ritual_ZN9QShortcut6setKeyERK12QKeySequence', self._valueOf(key),
    )

  @overload(QKeySequence.StandardKey)
  def setKeys(self, key: QKeySequence.StandardKey) -> None:
    """
    Calls Qt's 'void QShortcut::setKeys(QKeySequence::StandardKey key)'.

    Qt's own words: https://doc.qt.io/qt-6/qshortcut.html#setKeys

    Parameters
    ----------

    key : QKeySequence.StandardKey
      Passed on as its number.
    """
    #  void QShortcut::setKeys(QKeySequence::StandardKey key)
    self.uglySide.call(
        'ritual_ZN9QShortcut7setKeysEN12QKeySequence11StandardKeyE',
        key.value,
    )

  @overload(bool)
  def setEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QShortcut::setEnabled(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qshortcut.html#setEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QShortcut::setEnabled(bool enable)
    self.uglySide.call('ritual_ZN9QShortcut10setEnabledEb', enable)

  @overload(Qt.ShortcutContext)
  def setContext(self, context: Qt.ShortcutContext) -> None:
    """
    Calls Qt's 'void QShortcut::setContext(Qt::ShortcutContext context)'.

    Qt's own words: https://doc.qt.io/qt-6/qshortcut.html#setContext

    Parameters
    ----------

    context : Qt.ShortcutContext
      Passed on as its number.
    """
    #  void QShortcut::setContext(Qt::ShortcutContext context)
    self.uglySide.call(
        'ritual_ZN9QShortcut10setContextEN2Qt15ShortcutContextE',
        context.value,
    )

  @overload(bool)
  def setAutoRepeat(self, on: bool) -> None:
    """
    Calls Qt's 'void QShortcut::setAutoRepeat(bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qshortcut.html#setAutoRepeat

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QShortcut::setAutoRepeat(bool on)
    self.uglySide.call('ritual_ZN9QShortcut13setAutoRepeatEb', on)

  @overload(str)
  def setWhatsThis(self, text: str) -> None:
    """
    Calls Qt's 'void QShortcut::setWhatsThis(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qshortcut.html#setWhatsThis

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QShortcut::setWhatsThis(const QString &text)
    self.uglySide.call('ritual_ZN9QShortcut12setWhatsThisERK7QString', text)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's 'QShortcut::QShortcut(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qshortcut.html#QShortcut

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QShortcut::QShortcut(QObject *parent)
    self._noteCreation(QShortcut, lambda: Rituals.call(
        'ritual_ZN9QShortcutC1EP7QObject', self._addressOf(parent),
    ))

  @overload(QKeySequence, QObject)
  @overload(QKeySequence, NoneType)
  @overload(QKeySequence, QObject, str)
  @overload(QKeySequence, QObject, NoneType)
  @overload(QKeySequence, NoneType, str)
  @overload(QKeySequence, NoneType, NoneType)
  @overload(QKeySequence, QObject, str, str)
  @overload(QKeySequence, QObject, str, NoneType)
  @overload(QKeySequence, QObject, NoneType, str)
  @overload(QKeySequence, QObject, NoneType, NoneType)
  @overload(QKeySequence, NoneType, str, str)
  @overload(QKeySequence, NoneType, str, NoneType)
  @overload(QKeySequence, NoneType, NoneType, str)
  @overload(QKeySequence, NoneType, NoneType, NoneType)
  @overload(QKeySequence, QObject, str, str, Qt.ShortcutContext)
  @overload(QKeySequence, QObject, str, NoneType, Qt.ShortcutContext)
  @overload(QKeySequence, QObject, NoneType, str, Qt.ShortcutContext)
  @overload(QKeySequence, QObject, NoneType, NoneType, Qt.ShortcutContext)
  @overload(QKeySequence, NoneType, str, str, Qt.ShortcutContext)
  @overload(QKeySequence, NoneType, str, NoneType, Qt.ShortcutContext)
  @overload(QKeySequence, NoneType, NoneType, str, Qt.ShortcutContext)
  @overload(QKeySequence, NoneType, NoneType, NoneType, Qt.ShortcutContext)
  def __init__(
      self,
      key: QKeySequence,
      parent: Optional[QObject],
      member: Optional[str] = None,
      ambiguousMember: Optional[str] = None,
      context: Qt.ShortcutContext = Qt.ShortcutContext.WindowShortcut,
  ) -> None:
    """
    Notes what was given, for Qt's 'QShortcut::QShortcut(const QKeySequence
    &key, QObject *parent, const char *member, const char *ambiguousMember,
    Qt::ShortcutContext context)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qshortcut.html#QShortcut

    Parameters
    ----------

    key : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    ambiguousMember : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    context : Qt.ShortcutContext
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ShortcutContext.WindowShortcut.
    """
    #  QShortcut::QShortcut(const QKeySequence &key, QObject *parent, const
    #      char *member, const char *ambiguousMember, Qt::ShortcutContext
    #      context)
    self._noteCreation(QShortcut, lambda: Rituals.call(
        'ritual_ZN9QShortcutC1ERK12QKeySequenceP7QObjectPKcS6_N2Qt15Shortcu'
        'tContextE',
        self._valueOf(key), self._addressOf(parent), self._bytesOf(member),
        self._bytesOf(ambiguousMember), context.value,
    ))

  @overload(QKeySequence.StandardKey, QObject)
  @overload(QKeySequence.StandardKey, NoneType)
  @overload(QKeySequence.StandardKey, QObject, str)
  @overload(QKeySequence.StandardKey, QObject, NoneType)
  @overload(QKeySequence.StandardKey, NoneType, str)
  @overload(QKeySequence.StandardKey, NoneType, NoneType)
  @overload(QKeySequence.StandardKey, QObject, str, str)
  @overload(QKeySequence.StandardKey, QObject, str, NoneType)
  @overload(QKeySequence.StandardKey, QObject, NoneType, str)
  @overload(QKeySequence.StandardKey, QObject, NoneType, NoneType)
  @overload(QKeySequence.StandardKey, NoneType, str, str)
  @overload(QKeySequence.StandardKey, NoneType, str, NoneType)
  @overload(QKeySequence.StandardKey, NoneType, NoneType, str)
  @overload(QKeySequence.StandardKey, NoneType, NoneType, NoneType)
  @overload(QKeySequence.StandardKey, QObject, str, str, Qt.ShortcutContext)
  @overload(
      QKeySequence.StandardKey, QObject, str, NoneType, Qt.ShortcutContext,
  )
  @overload(
      QKeySequence.StandardKey, QObject, NoneType, str, Qt.ShortcutContext,
  )
  @overload(
      QKeySequence.StandardKey, QObject, NoneType, NoneType,
      Qt.ShortcutContext,
  )
  @overload(QKeySequence.StandardKey, NoneType, str, str, Qt.ShortcutContext)
  @overload(
      QKeySequence.StandardKey, NoneType, str, NoneType, Qt.ShortcutContext,
  )
  @overload(
      QKeySequence.StandardKey, NoneType, NoneType, str, Qt.ShortcutContext,
  )
  @overload(
      QKeySequence.StandardKey, NoneType, NoneType, NoneType,
      Qt.ShortcutContext,
  )
  def __init__(
      self,
      key: QKeySequence.StandardKey,
      parent: Optional[QObject],
      member: Optional[str] = None,
      ambiguousMember: Optional[str] = None,
      context: Qt.ShortcutContext = Qt.ShortcutContext.WindowShortcut,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QShortcut::QShortcut(QKeySequence::StandardKey key, QObject *parent,
    const char *member, const char *ambiguousMember, Qt::ShortcutContext
    context)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qshortcut.html#QShortcut

    Parameters
    ----------

    key : QKeySequence.StandardKey
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    ambiguousMember : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    context : Qt.ShortcutContext
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.ShortcutContext.WindowShortcut.
    """
    #  QShortcut::QShortcut(QKeySequence::StandardKey key, QObject *parent,
    #      const char *member, const char *ambiguousMember,
    #      Qt::ShortcutContext context)
    self._noteCreation(QShortcut, lambda: Rituals.call(
        'ritual_ZN9QShortcutC1EN12QKeySequence11StandardKeyEP7QObjectPKcS5_'
        'N2Qt15ShortcutContextE',
        key.value, self._addressOf(parent), self._bytesOf(member),
        self._bytesOf(ambiguousMember), context.value,
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
