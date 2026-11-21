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
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QKeySequence
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QKeySequence = WAIT['QKeySequence']

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
  can call so far, 9 names in all: 'metaObject', 'tr', 'keySequence',
  'maximumSequenceLength', 'setClearButtonEnabled', 'isClearButtonEnabled',
  'setKeySequence', 'clear', 'setMaximumSequenceLength'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QKeySequenceEdit::~QKeySequenceEdit()': the destructor: Python
    never removes a C++ QKeySequenceEdit.

  What has no ritual
  ------------------

  18 of the 30 functions Qt declares: 6 protected; 4 takes or gives a type
  that cannot be passed yet; 3 private; 2 a signal; 2 forbidden; 1 a
  template.

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
