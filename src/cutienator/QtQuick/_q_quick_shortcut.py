"""
QQuickShortcut binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickshortcut_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickShortcut to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickShortcut(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QQuickShortcut: a plain Python object standing in
  front of one C++ QQuickShortcut.

  It is built on the cute 'QObject', as Qt's QQuickShortcut is built on Qt's
  QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QQuickShortcut is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickShortcut that has a ritual and that Python can
  call so far, 26 names in all: 'metaObject', 'tr', 'sequence',
  'setSequence', 'sequences', 'setSequences', 'nativeText', 'portableText',
  'isEnabled', 'setEnabled', 'autoRepeat', 'setAutoRepeat', 'context',
  'setContext', 'sequenceChanged', 'sequencesChanged', 'nativeTextChanged',
  'portableTextChanged', 'enabledChanged', 'autoRepeatChanged',
  'contextChanged', 'activated', 'activatedAmbiguously', 'classBegin',
  'componentComplete', 'event'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickShortcut::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickShortcut::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickShortcut::~QQuickShortcut()': the destructor: Python never
    removes a C++ QQuickShortcut.
  - Qt's 'void QQuickShortcut::setEnabled(Shortcut &shortcut, bool enabled)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QQuickShortcut::setAutoRepeat(Shortcut &shortcut, bool
    repeat)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQuickShortcut::grabShortcut(Shortcut &shortcut,
    Qt::ShortcutContext context)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QQuickShortcut::ungrabShortcut(Shortcut &shortcut)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 36 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickShortcut is created at the first use, not by
    'QQuickShortcut(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickShortcut.
  - Qt tells when it has removed the C++ QQuickShortcut. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickShortcut that has no cute function yet,
    'grabShortcut', 'ungrabShortcut', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QQuickShortcut::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshortcut.html#tr

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
    #  QString QQuickShortcut::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickShortcut2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickShortcut'

  #  Qt's QQuickShortcut is built on more than one class. The part of a C++
  #  QQuickShortcut that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QQuickShortcut_QQmlParserStatus',
  }

  #  A C++ QQuickShortcut Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickShortcut'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickShortcut::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshortcut.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickShortcut::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickShortcut10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sequence(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickShortcut::sequence() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshortcut.html#sequence

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickShortcut::sequence() const
    address = self.uglySide.call('ritual_ZNK14QQuickShortcut8sequenceEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def sequences(self) -> QList[QVariant]:
    """
    Calls Qt's 'QVariantList QQuickShortcut::sequences() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshortcut.html#sequences

    Returns
    -------

    QList[QVariant]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QVariantList QQuickShortcut::sequences() const
    address = self.uglySide.call('ritual_ZNK14QQuickShortcut9sequencesEv')
    from ..QtCore import QVariant
    return QList[QVariant]._cuteOwning(address)

  def nativeText(self) -> str:
    """
    Calls Qt's 'QString QQuickShortcut::nativeText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshortcut.html#nativeText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickShortcut::nativeText() const
    return self.uglySide.call('ritual_ZNK14QQuickShortcut10nativeTextEv')

  def portableText(self) -> str:
    """
    Calls Qt's 'QString QQuickShortcut::portableText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshortcut.html#portableText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickShortcut::portableText() const
    return self.uglySide.call('ritual_ZNK14QQuickShortcut12portableTextEv')

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickShortcut::isEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshortcut.html#isEnabled
    """
    #  bool QQuickShortcut::isEnabled() const
    return self.uglySide.call('ritual_ZNK14QQuickShortcut9isEnabledEv')

  def autoRepeat(self) -> bool:
    """
    Calls Qt's 'bool QQuickShortcut::autoRepeat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshortcut.html#autoRepeat
    """
    #  bool QQuickShortcut::autoRepeat() const
    return self.uglySide.call('ritual_ZNK14QQuickShortcut10autoRepeatEv')

  def context(self) -> Qt.ShortcutContext:
    """
    Calls Qt's 'Qt::ShortcutContext QQuickShortcut::context() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshortcut.html#context

    Returns
    -------

    Qt.ShortcutContext
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ShortcutContext(number)' gives.
    """
    #  Qt::ShortcutContext QQuickShortcut::context() const
    return Qt.ShortcutContext(self.uglySide.call(
        'ritual_ZNK14QQuickShortcut7contextEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setSequence(self, sequence: QVariant) -> None:
    """
    Calls Qt's 'void QQuickShortcut::setSequence(const QVariant &sequence)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshortcut.html#setSequence

    Parameters
    ----------

    sequence : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickShortcut::setSequence(const QVariant &sequence)
    self.uglySide.call(
        'ritual_ZN14QQuickShortcut11setSequenceERK8QVariant',
        self._valueOf(sequence),
    )

  @overload(QList[QVariant])
  def setSequences(self, sequences: QList[QVariant]) -> None:
    """
    Calls Qt's 'void QQuickShortcut::setSequences(const QVariantList
    &sequences)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshortcut.html#setSequences

    Parameters
    ----------

    sequences : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickShortcut::setSequences(const QVariantList &sequences)
    self.uglySide.call(
        'ritual_ZN14QQuickShortcut12setSequencesERK5QListI8QVariantE',
        self._valueOf(sequences),
    )

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickShortcut::setEnabled(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshortcut.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickShortcut::setEnabled(bool enabled)
    self.uglySide.call('ritual_ZN14QQuickShortcut10setEnabledEb', enabled)

  @overload(bool)
  def setAutoRepeat(self, repeat: bool) -> None:
    """
    Calls Qt's 'void QQuickShortcut::setAutoRepeat(bool repeat)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshortcut.html#setAutoRepeat

    Parameters
    ----------

    repeat : bool
      Passed on as it is.
    """
    #  void QQuickShortcut::setAutoRepeat(bool repeat)
    self.uglySide.call('ritual_ZN14QQuickShortcut13setAutoRepeatEb', repeat)

  @overload(Qt.ShortcutContext)
  def setContext(self, context: Qt.ShortcutContext) -> None:
    """
    Calls Qt's 'void QQuickShortcut::setContext(Qt::ShortcutContext
    context)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshortcut.html#setContext

    Parameters
    ----------

    context : Qt.ShortcutContext
      Passed on as its number.
    """
    #  void QQuickShortcut::setContext(Qt::ShortcutContext context)
    self.uglySide.call(
        'ritual_ZN14QQuickShortcut10setContextEN2Qt15ShortcutContextE',
        context.value,
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
    Notes what was given, for Qt's 'QQuickShortcut::QQuickShortcut(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickshortcut.html#QQuickShortcut

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickShortcut::QQuickShortcut(QObject *parent)
    self._noteCreation(QQuickShortcut, lambda: Rituals.call(
        'ritual_ZN14QQuickShortcutC1EP7QObject',
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

  def sequenceChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShortcut::sequenceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshortcut.html#sequenceChanged
    """
    #  void QQuickShortcut::sequenceChanged()
    self.uglySide.call('ritual_ZN14QQuickShortcut15sequenceChangedEv')

  def sequencesChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShortcut::sequencesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshortcut.html#sequencesChanged
    """
    #  void QQuickShortcut::sequencesChanged()
    self.uglySide.call('ritual_ZN14QQuickShortcut16sequencesChangedEv')

  def nativeTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShortcut::nativeTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshortcut.html#nativeTextChanged
    """
    #  void QQuickShortcut::nativeTextChanged()
    self.uglySide.call('ritual_ZN14QQuickShortcut17nativeTextChangedEv')

  def portableTextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShortcut::portableTextChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshortcut.html#portableTextChanged
    """
    #  void QQuickShortcut::portableTextChanged()
    self.uglySide.call('ritual_ZN14QQuickShortcut19portableTextChangedEv')

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShortcut::enabledChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshortcut.html#enabledChanged
    """
    #  void QQuickShortcut::enabledChanged()
    self.uglySide.call('ritual_ZN14QQuickShortcut14enabledChangedEv')

  def autoRepeatChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShortcut::autoRepeatChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshortcut.html#autoRepeatChanged
    """
    #  void QQuickShortcut::autoRepeatChanged()
    self.uglySide.call('ritual_ZN14QQuickShortcut17autoRepeatChangedEv')

  def contextChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShortcut::contextChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshortcut.html#contextChanged
    """
    #  void QQuickShortcut::contextChanged()
    self.uglySide.call('ritual_ZN14QQuickShortcut14contextChangedEv')

  def activated(self) -> None:
    """
    Calls Qt's 'void QQuickShortcut::activated()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshortcut.html#activated
    """
    #  void QQuickShortcut::activated()
    self.uglySide.call('ritual_ZN14QQuickShortcut9activatedEv')

  def activatedAmbiguously(self) -> None:
    """
    Calls Qt's 'void QQuickShortcut::activatedAmbiguously()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshortcut.html#activatedAmbiguously
    """
    #  void QQuickShortcut::activatedAmbiguously()
    self.uglySide.call('ritual_ZN14QQuickShortcut20activatedAmbiguouslyEv')

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickShortcut::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshortcut.html#classBegin
    """
    #  void QQuickShortcut::classBegin()
    ritual = 'ritual_ZN14QQuickShortcut10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickShortcut10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickShortcut::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshortcut.html#componentComplete
    """
    #  void QQuickShortcut::componentComplete()
    ritual = 'ritual_ZN14QQuickShortcut17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickShortcut17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickShortcut::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshortcut.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickShortcut::event(QEvent *event)
    ritual = 'ritual_ZN14QQuickShortcut5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickShortcut5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @staticmethod
  def grabShortcut(*__, **_) -> Never:
    """
    Qt's 'void QQuickShortcut::grabShortcut(Shortcut &shortcut,
    Qt::ShortcutContext context)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQuickShortcut.grabShortcut' has no cute function yet. Qt's 'void "
        "QQuickShortcut::grabShortcut(Shortcut &shortcut, "
        "Qt::ShortcutContext context)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def ungrabShortcut(*__, **_) -> Never:
    """
    Qt's 'void QQuickShortcut::ungrabShortcut(Shortcut &shortcut)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickShortcut.ungrabShortcut' has no cute function yet. Qt's "
        "'void QQuickShortcut::ungrabShortcut(Shortcut &shortcut)': takes a "
        "type Python has no way to hand over yet.")
