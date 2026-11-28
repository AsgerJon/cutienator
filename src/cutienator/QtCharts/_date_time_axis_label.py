"""
DateTimeAxisLabel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/datetimeaxislabel_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means DateTimeAxisLabel to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtWidgets import QGraphicsItem
from . import EditableAxisLabel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QDateTime, QMetaObject
  from ..QtGui import QKeyEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDateTime = WAIT['QDateTime']
  QKeyEvent = WAIT['QKeyEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class DateTimeAxisLabel(EditableAxisLabel):
  """
  The cute side of Qt's DateTimeAxisLabel: a plain Python object standing in
  front of one C++ DateTimeAxisLabel.

  It is built on the cute 'EditableAxisLabel', as Qt's DateTimeAxisLabel is
  built on Qt's EditableAxisLabel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's DateTimeAxisLabel that has a ritual and that Python
  can call so far, 10 names in all: 'metaObject', 'tr', 'keyPressEvent',
  'value', 'setValue', 'setFormat', 'setInitialEditValue', 'finishEditing',
  'resetBeforeEditValue', 'dateTimeChanged'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *DateTimeAxisLabel::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int DateTimeAxisLabel::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ DateTimeAxisLabel is created at the first use, not by
    'DateTimeAxisLabel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DateTimeAxisLabel.
  - Qt tells when it has removed the C++ DateTimeAxisLabel. Every call on the
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
    Calls Qt's 'QString DateTimeAxisLabel::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/datetimeaxislabel.html#tr

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
    #  QString DateTimeAxisLabel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17DateTimeAxisLabel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DateTimeAxisLabel'

  #  A C++ DateTimeAxisLabel Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_DateTimeAxisLabel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *DateTimeAxisLabel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/datetimeaxislabel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *DateTimeAxisLabel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17DateTimeAxisLabel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def value(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime DateTimeAxisLabel::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/datetimeaxislabel.html#value

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime DateTimeAxisLabel::value() const
    address = self.uglySide.call('ritual_ZNK17DateTimeAxisLabel5valueEv')
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDateTime)
  def setValue(self, value: QDateTime) -> None:
    """
    Calls Qt's 'void DateTimeAxisLabel::setValue(const QDateTime &value)'.

    Qt's own words: https://doc.qt.io/qt-6/datetimeaxislabel.html#setValue

    Parameters
    ----------

    value : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void DateTimeAxisLabel::setValue(const QDateTime &value)
    self.uglySide.call(
        'ritual_ZN17DateTimeAxisLabel8setValueERK9QDateTime',
        self._valueOf(value),
    )

  @overload(str)
  def setFormat(self, format: str) -> None:
    """
    Calls Qt's 'void DateTimeAxisLabel::setFormat(const QString &format)'.

    Qt's own words: https://doc.qt.io/qt-6/datetimeaxislabel.html#setFormat

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DateTimeAxisLabel::setFormat(const QString &format)
    self.uglySide.call(
        'ritual_ZN17DateTimeAxisLabel9setFormatERK7QString', format,
    )

  def setInitialEditValue(self) -> None:
    """
    Calls Qt's 'void DateTimeAxisLabel::setInitialEditValue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/datetimeaxislabel.html#setInitialEditValue
    """
    #  void DateTimeAxisLabel::setInitialEditValue()
    ritual = 'ritual_ZN17DateTimeAxisLabel19setInitialEditValueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17DateTimeAxisLabel19setInitialEditValueEv'
    self.uglySide.call(ritual)

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
  @overload(QGraphicsItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QGraphicsItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'DateTimeAxisLabel::DateTimeAxisLabel(QGraphicsItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/datetimeaxislabel.html#DateTimeAxisLabel

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  DateTimeAxisLabel::DateTimeAxisLabel(QGraphicsItem *parent)
    self._noteCreation(DateTimeAxisLabel, lambda: Rituals.call(
        'ritual_ZN17DateTimeAxisLabelC1EP13QGraphicsItem',
        self._addressOf(parent, 'QGraphicsItem'),
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

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void DateTimeAxisLabel::keyPressEvent(QKeyEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/datetimeaxislabel.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void DateTimeAxisLabel::keyPressEvent(QKeyEvent *event)
    ritual = 'ritual_ZN17DateTimeAxisLabel13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17DateTimeAxisLabel13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def finishEditing(self) -> None:
    """
    Calls Qt's 'void DateTimeAxisLabel::finishEditing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/datetimeaxislabel.html#finishEditing
    """
    #  void DateTimeAxisLabel::finishEditing()
    ritual = 'ritual_ZN17DateTimeAxisLabel13finishEditingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17DateTimeAxisLabel13finishEditingEv'
    self.uglySide.call(ritual)

  def resetBeforeEditValue(self) -> None:
    """
    Calls Qt's 'void DateTimeAxisLabel::resetBeforeEditValue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/datetimeaxislabel.html#resetBeforeEditValue
    """
    #  void DateTimeAxisLabel::resetBeforeEditValue()
    ritual = 'ritual_ZN17DateTimeAxisLabel20resetBeforeEditValueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17DateTimeAxisLabel20resetBeforeEditValueEv'
    self.uglySide.call(ritual)

  @overload(QDateTime, QDateTime)
  def dateTimeChanged(
      self,
      oldDateTime: QDateTime,
      newDateTime: QDateTime,
  ) -> None:
    """
    Calls Qt's 'void DateTimeAxisLabel::dateTimeChanged(const QDateTime
    &oldDateTime, const QDateTime &newDateTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/datetimeaxislabel.html#dateTimeChanged

    Parameters
    ----------

    oldDateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    newDateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void DateTimeAxisLabel::dateTimeChanged(const QDateTime &oldDateTime,
    #      const QDateTime &newDateTime)
    self.uglySide.call(
        'ritual_ZN17DateTimeAxisLabel15dateTimeChangedERK9QDateTimeS2_',
        self._valueOf(oldDateTime), self._valueOf(newDateTime),
    )
