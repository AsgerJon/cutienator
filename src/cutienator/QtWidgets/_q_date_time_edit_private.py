"""
QDateTimeEditPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qdatetimeedit_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QDateTimeEditPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QDateTimeParser
from . import QAbstractSpinBoxPrivate, QDateTimeEdit, QStyle

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDate, QDateTime, QLocale, QPoint, QTime, QTimeZone
  from ..QtCore import QVariant
  from ..QtGui import QKeyEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDate = WAIT['QDate']
  QDateTime = WAIT['QDateTime']
  QKeyEvent = WAIT['QKeyEvent']
  QPoint = WAIT['QPoint']
  QTime = WAIT['QTime']
  QTimeZone = WAIT['QTimeZone']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDateTimeEditPrivate(QAbstractSpinBoxPrivate, QDateTimeParser):
  """
  The cute side of Qt's QDateTimeEditPrivate: a plain Python object standing
  in front of one C++ QDateTimeEditPrivate.

  It is built on the cute 'QAbstractSpinBoxPrivate', as Qt's
  QDateTimeEditPrivate is built on Qt's QAbstractSpinBoxPrivate, and has
  everything that class has. It is built on the cute 'QDateTimeParser' as
  well, as Qt's QDateTimeEditPrivate is built on Qt's QDateTimeParser too,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDateTimeEditPrivate that has a ritual and that
  Python can call so far, 36 names in all: 'q_func', 'init',
  'readLocaleSettings', 'textFromValue', 'valueFromText',
  'editorCursorPositionChanged', 'clearCache', 'newHoverControl',
  'updateEditFieldGeometry', 'getZeroVariant', 'setRange', 'updateEdit',
  'displayText', 'getMinimum', 'getMaximum', 'locale', 'cursorPosition',
  'absoluteIndex', 'stepBy', 'sectionAt', 'closestSection',
  'nextPrevSection', 'setSelected', 'updateCache', 'convertTimeZone',
  'updateTimeZone', 'valueToText', 'dateTimeValue', '_q_resetButton',
  'updateArrow', 'calendarPopupEnabled', 'syncCalendarWidget',
  'isSeparatorKey', 'convertSections', 'convertToPublic',
  'positionCalendarPopup'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QDateTimeEdit *QDateTimeEditPrivate::q_func() const': takes
    in Python what 'QDateTimeEdit *QDateTimeEditPrivate::q_func()' takes.
  - Qt's 'QDateTime QDateTimeEditPrivate::validateAndInterpret(QString
    &input, int &a1, QValidator::State &state, bool fixup) const': takes a
    type Python has no way to hand over yet.
  - Qt's 'void QDateTimeEditPrivate::emitSignals(EmitPolicy ep, const
    QVariant &old)': names the enum 'EmitPolicy', whose class cannot be named
    here.
  - Qt's 'void QDateTimeEditPrivate::interpret(EmitPolicy ep)': names the
    enum 'EmitPolicy', whose class cannot be named here.

  What has no ritual
  ------------------

  3 of the 44 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QDateTimeEditPrivate; 1 leans on 'vtable for QCalendarPopup', which Qt's
  source does not mark for use from outside Qt and has no code for that could
  be taken.

  What to expect
  --------------

  - The C++ QDateTimeEditPrivate is created at the first use, not by
    'QDateTimeEditPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDateTimeEditPrivate.
  - Each name of Qt's QDateTimeEditPrivate that has no cute function yet,
    '__init__', 'clearSection', 'initCalendarPopup', 'validateAndInterpret',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QDateTimeParser.Sections)
  def convertSections(s: QDateTimeParser.Sections) -> QDateTimeEdit.Sections:
    """
    Calls Qt's 'QDateTimeEdit::Sections
    QDateTimeEditPrivate::convertSections(QDateTimeParser::Sections s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#convertSections

    Parameters
    ----------

    s : QDateTimeParser.Sections
      Passed on as its number.

    Returns
    -------

    QDateTimeEdit.Sections
      The value standing for the combination Qt gave back.
    """
    #  QDateTimeEdit::Sections
    #      QDateTimeEditPrivate::convertSections(QDateTimeParser::Sections s)
    return QDateTimeEdit.Sections(Rituals.call(
        'ritual_ZN20QDateTimeEditPrivate15convertSectionsE6QFlagsIN15QDateT'
        'imeParser7SectionEE',
        s.value,
    ))

  @staticmethod
  @overload(QDateTimeParser.Section)
  def convertToPublic(s: QDateTimeParser.Section) -> QDateTimeEdit.Section:
    """
    Calls Qt's 'QDateTimeEdit::Section
    QDateTimeEditPrivate::convertToPublic(QDateTimeParser::Section s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#convertToPublic

    Parameters
    ----------

    s : QDateTimeParser.Section
      Passed on as its number.

    Returns
    -------

    QDateTimeEdit.Section
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QDateTimeEdit.Section(number)' gives.
    """
    #  QDateTimeEdit::Section
    #      QDateTimeEditPrivate::convertToPublic(QDateTimeParser::Section s)
    return QDateTimeEdit.Section(Rituals.call(
        'ritual_ZN20QDateTimeEditPrivate15convertToPublicEN15QDateTimeParse'
        'r7SectionE',
        s.value,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDateTimeEditPrivate'

  #  Qt's QDateTimeEditPrivate is built on more than one class. The part of a
  #  C++ QDateTimeEditPrivate that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QDateTimeParser': 'ritual_cast_QDateTimeEditPrivate_QDateTimeParser',
  }

  #  A C++ QDateTimeEditPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDateTimeEditPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def textFromValue(self, f: QVariant) -> str:
    """
    Calls Qt's 'QString QDateTimeEditPrivate::textFromValue(const QVariant
    &f) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#textFromValue

    Parameters
    ----------

    f : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDateTimeEditPrivate::textFromValue(const QVariant &f) const
    ritual = 'ritual_ZNK20QDateTimeEditPrivate13textFromValueERK8QVariant'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QDateTimeEditPrivate13textFromValueERK8QVariant')
    return self.uglySide.call(ritual, self._valueOf(f))

  @overload(str)
  def valueFromText(self, f: str) -> QVariant:
    """
    Calls Qt's 'QVariant QDateTimeEditPrivate::valueFromText(const QString
    &f) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#valueFromText

    Parameters
    ----------

    f : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QDateTimeEditPrivate::valueFromText(const QString &f) const
    ritual = 'ritual_ZNK20QDateTimeEditPrivate13valueFromTextERK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QDateTimeEditPrivate13valueFromTextERK7QString')
    address = self.uglySide.call(ritual, f)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def getZeroVariant(self) -> QVariant:
    """
    Calls Qt's 'QVariant QDateTimeEditPrivate::getZeroVariant() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#getZeroVariant

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QDateTimeEditPrivate::getZeroVariant() const
    ritual = 'ritual_ZNK20QDateTimeEditPrivate14getZeroVariantEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QDateTimeEditPrivate14getZeroVariantEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def displayText(self) -> str:
    """
    Calls Qt's 'QString QDateTimeEditPrivate::displayText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#displayText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDateTimeEditPrivate::displayText() const
    ritual = 'ritual_ZNK20QDateTimeEditPrivate11displayTextEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QDateTimeEditPrivate11displayTextEv'
    return self.uglySide.call(ritual)

  @overload(QTimeZone)
  def getMinimum(self, zone: QTimeZone) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTimeEditPrivate::getMinimum(const QTimeZone
    &zone) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#getMinimum

    Parameters
    ----------

    zone : QTimeZone
      Passed on as a value: Qt reads the C++ QTimeZone, which stays Python's
      own.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTimeEditPrivate::getMinimum(const QTimeZone &zone)
    #      const
    ritual = 'ritual_ZNK20QDateTimeEditPrivate10getMinimumERK9QTimeZone'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QDateTimeEditPrivate10getMinimumERK9QTimeZone')
    address = self.uglySide.call(ritual, self._valueOf(zone))
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  @overload(QTimeZone)
  def getMaximum(self, zone: QTimeZone) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTimeEditPrivate::getMaximum(const QTimeZone
    &zone) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#getMaximum

    Parameters
    ----------

    zone : QTimeZone
      Passed on as a value: Qt reads the C++ QTimeZone, which stays Python's
      own.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTimeEditPrivate::getMaximum(const QTimeZone &zone)
    #      const
    ritual = 'ritual_ZNK20QDateTimeEditPrivate10getMaximumERK9QTimeZone'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QDateTimeEditPrivate10getMaximumERK9QTimeZone')
    address = self.uglySide.call(ritual, self._valueOf(zone))
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QDateTimeEditPrivate::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeeditprivate.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QDateTimeEditPrivate::locale() const
    ritual = 'ritual_ZNK20QDateTimeEditPrivate6localeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QDateTimeEditPrivate6localeEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QLocale
    return QLocale._cuteOwning(address)

  def cursorPosition(self) -> int:
    """
    Calls Qt's 'int QDateTimeEditPrivate::cursorPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#cursorPosition
    """
    #  int QDateTimeEditPrivate::cursorPosition() const
    ritual = 'ritual_ZNK20QDateTimeEditPrivate14cursorPositionEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QDateTimeEditPrivate14cursorPositionEv'
    return self.uglySide.call(ritual)

  @overload(QDateTimeEdit.Section, int)
  def absoluteIndex(self, s: QDateTimeEdit.Section, index: int) -> int:
    """
    Calls Qt's 'int
    QDateTimeEditPrivate::absoluteIndex(QDateTimeEdit::Section s, int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#absoluteIndex

    Parameters
    ----------

    s : QDateTimeEdit.Section
      Passed on as its number.

    index : int
      Passed on as it is.
    """
    #  int QDateTimeEditPrivate::absoluteIndex(QDateTimeEdit::Section s, int
    #      index) const
    return self.uglySide.call(
        'ritual_ZNK20QDateTimeEditPrivate13absoluteIndexEN13QDateTimeEdit7S'
        'ectionEi',
        s.value, index,
    )

  @overload(QDateTimeParser.SectionNode)
  def absoluteIndex(self, s: QDateTimeParser.SectionNode) -> int:
    """
    Calls Qt's 'int QDateTimeEditPrivate::absoluteIndex(SectionNode s)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#absoluteIndex

    Parameters
    ----------

    s : QDateTimeParser.SectionNode
      Passed on as a value: Qt reads the C++ QDateTimeParser::SectionNode,
      which stays Python's own.
    """
    #  int QDateTimeEditPrivate::absoluteIndex(SectionNode s) const
    return self.uglySide.call(
        'ritual_ZNK20QDateTimeEditPrivate13absoluteIndexEN15QDateTimeParser'
        '11SectionNodeE',
        self._valueOf(s),
    )

  @overload(int, int)
  @overload(int, int, bool)
  def stepBy(self, index: int, steps: int, test: bool = False) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTimeEditPrivate::stepBy(int index, int steps,
    bool test) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeeditprivate.html#stepBy

    Parameters
    ----------

    index : int
      Passed on as it is.

    steps : int
      Passed on as it is.

    test : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTimeEditPrivate::stepBy(int index, int steps, bool
    #      test) const
    address = self.uglySide.call(
        'ritual_ZNK20QDateTimeEditPrivate6stepByEiib', index, steps, test,
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  @overload(int)
  def sectionAt(self, pos: int) -> int:
    """
    Calls Qt's 'int QDateTimeEditPrivate::sectionAt(int pos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#sectionAt

    Parameters
    ----------

    pos : int
      Passed on as it is.
    """
    #  int QDateTimeEditPrivate::sectionAt(int pos) const
    return self.uglySide.call(
        'ritual_ZNK20QDateTimeEditPrivate9sectionAtEi', pos,
    )

  @overload(int, bool)
  def closestSection(self, index: int, forward: bool) -> int:
    """
    Calls Qt's 'int QDateTimeEditPrivate::closestSection(int index, bool
    forward) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#closestSection

    Parameters
    ----------

    index : int
      Passed on as it is.

    forward : bool
      Passed on as it is.
    """
    #  int QDateTimeEditPrivate::closestSection(int index, bool forward)
    #      const
    return self.uglySide.call(
        'ritual_ZNK20QDateTimeEditPrivate14closestSectionEib',
        index, forward,
    )

  @overload(int, bool)
  def nextPrevSection(self, index: int, forward: bool) -> int:
    """
    Calls Qt's 'int QDateTimeEditPrivate::nextPrevSection(int index, bool
    forward) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#nextPrevSection

    Parameters
    ----------

    index : int
      Passed on as it is.

    forward : bool
      Passed on as it is.
    """
    #  int QDateTimeEditPrivate::nextPrevSection(int index, bool forward)
    #      const
    return self.uglySide.call(
        'ritual_ZNK20QDateTimeEditPrivate15nextPrevSectionEib',
        index, forward,
    )

  @overload(QVariant)
  def valueToText(self, var: QVariant) -> str:
    """
    Calls Qt's 'QString QDateTimeEditPrivate::valueToText(const QVariant
    &var) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#valueToText

    Parameters
    ----------

    var : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDateTimeEditPrivate::valueToText(const QVariant &var) const
    return self.uglySide.call(
        'ritual_ZNK20QDateTimeEditPrivate11valueToTextERK8QVariant',
        self._valueOf(var),
    )

  @overload(QDate, QTime)
  def dateTimeValue(self, date: QDate, time: QTime) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTimeEditPrivate::dateTimeValue(QDate date,
    QTime time) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#dateTimeValue

    Parameters
    ----------

    date : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.

    time : QTime
      Passed on as a value: Qt reads the C++ QTime, which stays Python's own.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTimeEditPrivate::dateTimeValue(QDate date, QTime time)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK20QDateTimeEditPrivate13dateTimeValueE5QDate5QTime',
        self._valueOf(date), self._valueOf(time),
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def calendarPopupEnabled(self) -> bool:
    """
    Calls Qt's 'bool QDateTimeEditPrivate::calendarPopupEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#calendarPopupEnabled
    """
    #  bool QDateTimeEditPrivate::calendarPopupEnabled() const
    return self.uglySide.call(
        'ritual_ZNK20QDateTimeEditPrivate20calendarPopupEnabledEv',
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def isSeparatorKey(self, k: Optional[QKeyEvent]) -> bool:
    """
    Calls Qt's 'bool QDateTimeEditPrivate::isSeparatorKey(const QKeyEvent *k)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#isSeparatorKey

    Parameters
    ----------

    k : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDateTimeEditPrivate::isSeparatorKey(const QKeyEvent *k) const
    return self.uglySide.call(
        'ritual_ZNK20QDateTimeEditPrivate14isSeparatorKeyEPK9QKeyEvent',
        self._addressOf(k),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant, QVariant)
  def setRange(self, min: QVariant, max: QVariant) -> None:
    """
    Calls Qt's 'void QDateTimeEditPrivate::setRange(const QVariant &min,
    const QVariant &max)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeeditprivate.html#setRange

    Parameters
    ----------

    min : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    max : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDateTimeEditPrivate::setRange(const QVariant &min, const
    #      QVariant &max)
    ritual = 'ritual_ZN20QDateTimeEditPrivate8setRangeERK8QVariantS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QDateTimeEditPrivate8setRangeERK8QVariantS2_'
    self.uglySide.call(ritual, self._valueOf(min), self._valueOf(max))

  @overload(int)
  @overload(int, bool)
  def setSelected(self, index: int, forward: bool = False) -> None:
    """
    Calls Qt's 'void QDateTimeEditPrivate::setSelected(int index, bool
    forward)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#setSelected

    Parameters
    ----------

    index : int
      Passed on as it is.

    forward : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QDateTimeEditPrivate::setSelected(int index, bool forward)
    self.uglySide.call(
        'ritual_ZN20QDateTimeEditPrivate11setSelectedEib', index, forward,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QDateTimeEditPrivate::QDateTimeEditPrivate(const QTimeZone &zone)':
    leans on 'QDateTimeEditPrivate::updateEdit()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDateTimeEditPrivate.__init__' has no cute function yet. Qt's "
        "'QDateTimeEditPrivate::QDateTimeEditPrivate(const QTimeZone "
        "&zone)': leans on 'QDateTimeEditPrivate::updateEdit()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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

  def q_func(self) -> Optional[QDateTimeEdit]:
    """
    Calls Qt's 'QDateTimeEdit *QDateTimeEditPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeeditprivate.html#q_func

    Returns
    -------

    Optional[QDateTimeEdit]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDateTimeEdit *QDateTimeEditPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QDateTimeEditPrivate6q_funcEv')
    return QDateTimeEdit._cuteAt(address)

  @overload(QVariant)
  def init(self, var: QVariant) -> None:
    """
    Calls Qt's 'void QDateTimeEditPrivate::init(const QVariant &var)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeeditprivate.html#init

    Parameters
    ----------

    var : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDateTimeEditPrivate::init(const QVariant &var)
    self.uglySide.call(
        'ritual_ZN20QDateTimeEditPrivate4initERK8QVariant',
        self._valueOf(var),
    )

  def readLocaleSettings(self) -> None:
    """
    Calls Qt's 'void QDateTimeEditPrivate::readLocaleSettings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#readLocaleSettings
    """
    #  void QDateTimeEditPrivate::readLocaleSettings()
    self.uglySide.call(
        'ritual_ZN20QDateTimeEditPrivate18readLocaleSettingsEv',
    )

  @overload(int, int)
  def editorCursorPositionChanged(self, oldpos: int, newpos: int) -> None:
    """
    Calls Qt's 'void QDateTimeEditPrivate::editorCursorPositionChanged(int
    oldpos, int newpos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html

    Parameters
    ----------

    oldpos : int
      Passed on as it is.

    newpos : int
      Passed on as it is.
    """
    #  void QDateTimeEditPrivate::editorCursorPositionChanged(int oldpos, int
    #      newpos)
    self.uglySide.call(
        'ritual_ZN20QDateTimeEditPrivate27editorCursorPositionChangedEii',
        oldpos, newpos,
    )

  def clearCache(self) -> None:
    """
    Calls Qt's 'void QDateTimeEditPrivate::clearCache() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#clearCache
    """
    #  void QDateTimeEditPrivate::clearCache() const
    ritual = 'ritual_ZNK20QDateTimeEditPrivate10clearCacheEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QDateTimeEditPrivate10clearCacheEv'
    self.uglySide.call(ritual)

  @overload(QPoint)
  def newHoverControl(self, pos: QPoint) -> QStyle.SubControl:
    """
    Calls Qt's 'QStyle::SubControl
    QDateTimeEditPrivate::newHoverControl(const QPoint &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#newHoverControl

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    QStyle.SubControl
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QStyle.SubControl(number)' gives.
    """
    #  QStyle::SubControl QDateTimeEditPrivate::newHoverControl(const QPoint
    #      &pos)
    ritual = 'ritual_ZN20QDateTimeEditPrivate15newHoverControlERK6QPoint'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QDateTimeEditPrivate15newHoverControlERK6QPoint')
    return QStyle.SubControl(self.uglySide.call(ritual, self._valueOf(pos)))

  def updateEditFieldGeometry(self) -> None:
    """
    Calls Qt's 'void QDateTimeEditPrivate::updateEditFieldGeometry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#updateEditFieldGeometry
    """
    #  void QDateTimeEditPrivate::updateEditFieldGeometry()
    ritual = 'ritual_ZN20QDateTimeEditPrivate23updateEditFieldGeometryEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QDateTimeEditPrivate23updateEditFieldGeometryEv')
    self.uglySide.call(ritual)

  def updateEdit(self) -> None:
    """
    Calls Qt's 'void QDateTimeEditPrivate::updateEdit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#updateEdit
    """
    #  void QDateTimeEditPrivate::updateEdit()
    self.uglySide.call('ritual_ZN20QDateTimeEditPrivate10updateEditEv')

  @overload(QVariant, str)
  def updateCache(self, val: QVariant, str: str) -> None:
    """
    Calls Qt's 'void QDateTimeEditPrivate::updateCache(const QVariant &val,
    const QString &str) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#updateCache

    Parameters
    ----------

    val : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    str : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDateTimeEditPrivate::updateCache(const QVariant &val, const
    #      QString &str) const
    self.uglySide.call(
        'ritual_ZNK20QDateTimeEditPrivate11updateCacheERK8QVariantRK7QStrin'
        'g',
        self._valueOf(val), str,
    )

  @overload(QDateTime)
  def convertTimeZone(self, datetime: QDateTime) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTimeEditPrivate::convertTimeZone(const
    QDateTime &datetime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#convertTimeZone

    Parameters
    ----------

    datetime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTimeEditPrivate::convertTimeZone(const QDateTime
    #      &datetime)
    address = self.uglySide.call(
        'ritual_ZN20QDateTimeEditPrivate15convertTimeZoneERK9QDateTime',
        self._valueOf(datetime),
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def updateTimeZone(self) -> None:
    """
    Calls Qt's 'void QDateTimeEditPrivate::updateTimeZone()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#updateTimeZone
    """
    #  void QDateTimeEditPrivate::updateTimeZone()
    self.uglySide.call('ritual_ZN20QDateTimeEditPrivate14updateTimeZoneEv')

  def _q_resetButton(self) -> None:
    """
    Calls Qt's 'void QDateTimeEditPrivate::_q_resetButton()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#_q_resetButton
    """
    #  void QDateTimeEditPrivate::_q_resetButton()
    self.uglySide.call('ritual_ZN20QDateTimeEditPrivate14_q_resetButtonEv')

  @overload(QStyle.StateFlag)
  def updateArrow(self, state: QStyle.StateFlag) -> None:
    """
    Calls Qt's 'void QDateTimeEditPrivate::updateArrow(QStyle::StateFlag
    state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#updateArrow

    Parameters
    ----------

    state : QStyle.StateFlag
      Passed on as its number.
    """
    #  void QDateTimeEditPrivate::updateArrow(QStyle::StateFlag state)
    self.uglySide.call(
        'ritual_ZN20QDateTimeEditPrivate11updateArrowEN6QStyle9StateFlagE',
        state.value,
    )

  def syncCalendarWidget(self) -> None:
    """
    Calls Qt's 'void QDateTimeEditPrivate::syncCalendarWidget()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#syncCalendarWidget
    """
    #  void QDateTimeEditPrivate::syncCalendarWidget()
    self.uglySide.call(
        'ritual_ZN20QDateTimeEditPrivate18syncCalendarWidgetEv',
    )

  def positionCalendarPopup(self) -> None:
    """
    Calls Qt's 'void QDateTimeEditPrivate::positionCalendarPopup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeeditprivate.html#positionCalendarPopup
    """
    #  void QDateTimeEditPrivate::positionCalendarPopup()
    self.uglySide.call(
        'ritual_ZN20QDateTimeEditPrivate21positionCalendarPopupEv',
    )

  @staticmethod
  def clearSection(*__, **_) -> Never:
    """
    Qt's 'void QDateTimeEditPrivate::clearSection(int index)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'QDTEDEBUG'.
    """
    raise NotImplementedError(
        "'QDateTimeEditPrivate.clearSection' has no cute function yet. Qt's "
        "'void QDateTimeEditPrivate::clearSection(int index)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'QDTEDEBUG'.")

  @staticmethod
  def initCalendarPopup(*__, **_) -> Never:
    """
    Qt's 'void QDateTimeEditPrivate::initCalendarPopup(QCalendarWidget *cw)':
    leans on 'vtable for QCalendarPopup', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDateTimeEditPrivate.initCalendarPopup' has no cute function yet. "
        "Qt's 'void QDateTimeEditPrivate::initCalendarPopup(QCalendarWidget "
        "*cw)': leans on 'vtable for QCalendarPopup', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def validateAndInterpret(*__, **_) -> Never:
    """
    Qt's 'QDateTime QDateTimeEditPrivate::validateAndInterpret(QString
    &input, int &a1, QValidator::State &state, bool fixup) const': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDateTimeEditPrivate.validateAndInterpret' has no cute function "
        "yet. Qt's 'QDateTime "
        "QDateTimeEditPrivate::validateAndInterpret(QString &input, int "
        "&a1, QValidator::State &state, bool fixup) const': takes a type "
        "Python has no way to hand over yet.")
