"""
QKeySequenceEdit binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qkeysequenceedit.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QKeyCombination, QMetaObject, QTimerEvent
  from ..QtGui import QFocusEvent, QKeyEvent, QKeySequence
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QKeyCombination = WAIT['QKeyCombination']
  QKeyEvent = WAIT['QKeyEvent']
  QKeySequence = WAIT['QKeySequence']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QKeySequenceEdit(QWidget):
  """
  The cute side of Qt's QKeySequenceEdit: a plain Python object standing in
  front of one C++ QKeySequenceEdit.

  It is built on the cute 'QWidget', as Qt's QKeySequenceEdit is built on
  Qt's QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QKeySequenceEdit that has a ritual and that Python
  can call so far, 16 names in all: 'metaObject', 'tr', 'keySequence',
  'maximumSequenceLength', 'setClearButtonEnabled', 'isClearButtonEnabled',
  'setFinishingKeyCombinations', 'finishingKeyCombinations',
  'setKeySequence', 'clear', 'setMaximumSequenceLength', 'event',
  'keyPressEvent', 'keyReleaseEvent', 'timerEvent', 'focusOutEvent'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QKeySequenceEdit::~QKeySequenceEdit()': the destructor: Python
    never removes a C++ QKeySequenceEdit.

  What has no ritual
  ------------------

  11 of the 30 functions Qt declares: 3 private; 2 takes or gives a type that
  cannot be passed yet; 2 a signal; 2 forbidden; 1 a template; 1 protected.

  What to expect
  --------------

  - The C++ QKeySequenceEdit is created at the first use, not by
    'QKeySequenceEdit(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QKeySequenceEdit.
  - Qt tells when it has removed the C++ QKeySequenceEdit. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QKeySequenceEdit::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequenceedit.html#tr

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
    #  QString QKeySequenceEdit::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QKeySequenceEdit2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QKeySequenceEdit'

  #  A C++ QKeySequenceEdit Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QKeySequenceEdit'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QKeySequenceEdit::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequenceedit.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QKeySequenceEdit::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QKeySequenceEdit10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def keySequence(self) -> QKeySequence:
    """
    Calls Qt's 'QKeySequence QKeySequenceEdit::keySequence() const'.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequenceedit.html#keySequence

    Returns
    -------

    QKeySequence
      A new cute QKeySequence around the copy Qt gave back. Python owns it.
    """
    #  QKeySequence QKeySequenceEdit::keySequence() const
    address = self.uglySide.call(
        'ritual_ZNK16QKeySequenceEdit11keySequenceEv',
    )
    from ..QtGui import QKeySequence
    return QKeySequence._cuteOwning(address)

  def maximumSequenceLength(self) -> int:
    """
    Calls Qt's 'qsizetype QKeySequenceEdit::maximumSequenceLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeysequenceedit.html#maximumSequenceLength
    """
    #  qsizetype QKeySequenceEdit::maximumSequenceLength() const
    return self.uglySide.call(
        'ritual_ZNK16QKeySequenceEdit21maximumSequenceLengthEv',
    )

  def isClearButtonEnabled(self) -> bool:
    """
    Calls Qt's 'bool QKeySequenceEdit::isClearButtonEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeysequenceedit.html#isClearButtonEnabled
    """
    #  bool QKeySequenceEdit::isClearButtonEnabled() const
    return self.uglySide.call(
        'ritual_ZNK16QKeySequenceEdit20isClearButtonEnabledEv',
    )

  def finishingKeyCombinations(self) -> QList[QKeyCombination]:
    """
    Calls Qt's 'QList<QKeyCombination>
    QKeySequenceEdit::finishingKeyCombinations() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeysequenceedit.html#finishingKeyCombinations

    Returns
    -------

    QList[QKeyCombination]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QKeyCombination> QKeySequenceEdit::finishingKeyCombinations()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK16QKeySequenceEdit24finishingKeyCombinationsEv',
    )
    from ..QtCore import QKeyCombination
    return QList[QKeyCombination]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setClearButtonEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QKeySequenceEdit::setClearButtonEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeysequenceedit.html#setClearButtonEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QKeySequenceEdit::setClearButtonEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN16QKeySequenceEdit21setClearButtonEnabledEb', enable,
    )

  @overload(QList[QKeyCombination])
  def setFinishingKeyCombinations(
      self,
      finishingKeyCombinations: QList[QKeyCombination],
  ) -> None:
    """
    Calls Qt's 'void QKeySequenceEdit::setFinishingKeyCombinations(const
    QList<QKeyCombination> &finishingKeyCombinations)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeysequenceedit.html#setFinishingKeyCombinations

    Parameters
    ----------

    finishingKeyCombinations : QList[QKeyCombination]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QKeySequenceEdit::setFinishingKeyCombinations(const
    #      QList<QKeyCombination> &finishingKeyCombinations)
    self.uglySide.call(
        'ritual_ZN16QKeySequenceEdit27setFinishingKeyCombinationsERK5QListI'
        '15QKeyCombinationE',
        self._valueOf(finishingKeyCombinations),
    )

  @overload(QKeySequence)
  def setKeySequence(self, keySequence: QKeySequence) -> None:
    """
    Calls Qt's 'void QKeySequenceEdit::setKeySequence(const QKeySequence
    &keySequence)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeysequenceedit.html#setKeySequence

    Parameters
    ----------

    keySequence : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.
    """
    #  void QKeySequenceEdit::setKeySequence(const QKeySequence &keySequence)
    self.uglySide.call(
        'ritual_ZN16QKeySequenceEdit14setKeySequenceERK12QKeySequence',
        self._valueOf(keySequence),
    )

  @overload(int)
  def setMaximumSequenceLength(self, count: int) -> None:
    """
    Calls Qt's 'void QKeySequenceEdit::setMaximumSequenceLength(qsizetype
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeysequenceedit.html#setMaximumSequenceLength

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QKeySequenceEdit::setMaximumSequenceLength(qsizetype count)
    self.uglySide.call(
        'ritual_ZN16QKeySequenceEdit24setMaximumSequenceLengthEx', count,
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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's
    'QKeySequenceEdit::QKeySequenceEdit(QWidget *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeysequenceedit.html#QKeySequenceEdit

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QKeySequenceEdit::QKeySequenceEdit(QWidget *parent)
    self._noteCreation(QKeySequenceEdit, lambda: Rituals.call(
        'ritual_ZN16QKeySequenceEditC1EP7QWidget', self._addressOf(parent),
    ))

  @overload(QKeySequence)
  @overload(QKeySequence, QWidget)
  @overload(QKeySequence, NoneType)
  def __init__(
      self,
      keySequence: QKeySequence,
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QKeySequenceEdit::QKeySequenceEdit(const
    QKeySequence &keySequence, QWidget *parent)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeysequenceedit.html#QKeySequenceEdit

    Parameters
    ----------

    keySequence : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QKeySequenceEdit::QKeySequenceEdit(const QKeySequence &keySequence,
    #      QWidget *parent)
    self._noteCreation(QKeySequenceEdit, lambda: Rituals.call(
        'ritual_ZN16QKeySequenceEditC1ERK12QKeySequenceP7QWidget',
        self._valueOf(keySequence), self._addressOf(parent),
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
    Calls Qt's 'void QKeySequenceEdit::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequenceedit.html#clear
    """
    #  void QKeySequenceEdit::clear()
    self.uglySide.call('ritual_ZN16QKeySequenceEdit5clearEv')

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QKeySequenceEdit::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequenceedit.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QKeySequenceEdit::event(QEvent *a0)
    return self.uglySide.call(
        'ritual_own_ZN16QKeySequenceEdit5eventEP6QEvent',
        self._addressOf(a0),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, a0: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QKeySequenceEdit::keyPressEvent(QKeyEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeysequenceedit.html#keyPressEvent

    Parameters
    ----------

    a0 : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QKeySequenceEdit::keyPressEvent(QKeyEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN16QKeySequenceEdit13keyPressEventEP9QKeyEvent',
        self._addressOf(a0),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, a0: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QKeySequenceEdit::keyReleaseEvent(QKeyEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeysequenceedit.html#keyReleaseEvent

    Parameters
    ----------

    a0 : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QKeySequenceEdit::keyReleaseEvent(QKeyEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN16QKeySequenceEdit15keyReleaseEventEP9QKeyEvent',
        self._addressOf(a0),
    )

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, a0: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QKeySequenceEdit::timerEvent(QTimerEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qkeysequenceedit.html#timerEvent

    Parameters
    ----------

    a0 : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QKeySequenceEdit::timerEvent(QTimerEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN16QKeySequenceEdit10timerEventEP11QTimerEvent',
        self._addressOf(a0),
    )

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, a0: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QKeySequenceEdit::focusOutEvent(QFocusEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qkeysequenceedit.html#focusOutEvent

    Parameters
    ----------

    a0 : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QKeySequenceEdit::focusOutEvent(QFocusEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN16QKeySequenceEdit13focusOutEventEP11QFocusEvent',
        self._addressOf(a0),
    )
