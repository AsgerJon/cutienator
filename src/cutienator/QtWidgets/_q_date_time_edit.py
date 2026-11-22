"""
QDateTimeEdit binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qdatetimeedit.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QAbstractSpinBox, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QCalendar, QDate, QDateTime, QEvent, QMetaObject
  from ..QtCore import QSize, QTime, QTimeZone
  from ..QtGui import QFocusEvent, QKeyEvent, QMouseEvent, QPaintEvent
  from ..QtGui import QWheelEvent
  from . import QCalendarWidget, QStyleOptionSpinBox
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCalendar = WAIT['QCalendar']
  QCalendarWidget = WAIT['QCalendarWidget']
  QDate = WAIT['QDate']
  QDateTime = WAIT['QDateTime']
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QStyleOptionSpinBox = WAIT['QStyleOptionSpinBox']
  QTime = WAIT['QTime']
  QTimeZone = WAIT['QTimeZone']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDateTimeEdit(QAbstractSpinBox):
  """
  The cute side of Qt's QDateTimeEdit: a plain Python object standing in
  front of one C++ QDateTimeEdit.

  It is built on the cute 'QAbstractSpinBox', as Qt's QDateTimeEdit is built
  on Qt's QAbstractSpinBox, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDateTimeEdit that has a ritual and that Python can
  call so far, 61 names in all: 'metaObject', 'tr', 'dateTime', 'date',
  'time', 'calendar', 'setCalendar', 'minimumDateTime',
  'clearMinimumDateTime', 'setMinimumDateTime', 'maximumDateTime',
  'clearMaximumDateTime', 'setMaximumDateTime', 'setDateTimeRange',
  'minimumDate', 'setMinimumDate', 'clearMinimumDate', 'maximumDate',
  'setMaximumDate', 'clearMaximumDate', 'setDateRange', 'minimumTime',
  'setMinimumTime', 'clearMinimumTime', 'maximumTime', 'setMaximumTime',
  'clearMaximumTime', 'setTimeRange', 'displayedSections', 'currentSection',
  'sectionAt', 'setCurrentSection', 'currentSectionIndex',
  'setCurrentSectionIndex', 'calendarWidget', 'setCalendarWidget',
  'sectionCount', 'setSelectedSection', 'sectionText', 'displayFormat',
  'setDisplayFormat', 'calendarPopup', 'setCalendarPopup', 'timeSpec',
  'setTimeSpec', 'timeZone', 'setTimeZone', 'sizeHint', 'clear', 'stepBy',
  'event', 'setDateTime', 'setDate', 'setTime', 'keyPressEvent',
  'wheelEvent', 'focusInEvent', 'focusNextPrevChild', 'mousePressEvent',
  'paintEvent', 'initStyleOption'. It can be made from Python, in 4 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDateTimeEdit::~QDateTimeEdit()': the destructor: Python never
    removes a C++ QDateTimeEdit.

  What has no ritual
  ------------------

  17 of the 83 functions Qt declares: 6 protected; 3 private; 3 a signal; 2
  takes or gives a type that cannot be passed yet; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QDateTimeEdit is created at the first use, not by
    'QDateTimeEdit(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDateTimeEdit.
  - Qt tells when it has removed the C++ QDateTimeEdit. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QDateTimeEdit, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Section(CuteFlags):
    """
    The flags enum 'QDateTimeEdit::Section' of Qt, with the 11 names Qt gives
    in it. Qt names the type of its combinations 'QDateTimeEdit::Sections'.
    """

    NoSection = 0x0
    AmPmSection = 0x1
    MSecSection = 0x2
    SecondSection = 0x4
    MinuteSection = 0x8
    HourSection = 0x10
    DaySection = 0x100
    MonthSection = 0x200
    YearSection = 0x400
    TimeSections_Mask = 0x1f
    DateSections_Mask = 0x700

  Sections = Section

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
    Calls Qt's 'QString QDateTimeEdit::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#tr

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
    #  QString QDateTimeEdit::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QDateTimeEdit2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDateTimeEdit'

  #  A C++ QDateTimeEdit Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDateTimeEdit'

  #  The functions Qt calls itself that QDateTimeEdit is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'dateTimeFromText': (
          'QDateTime QDateTimeEdit::dateTimeFromText(const QString &) const',
      ),
      'textFromDateTime': (
          'QString QDateTimeEdit::textFromDateTime(const QDateTime &) const',
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDateTimeEdit::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDateTimeEdit::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QDateTimeEdit10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def dateTime(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTimeEdit::dateTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#dateTime

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTimeEdit::dateTime() const
    address = self.uglySide.call('ritual_ZNK13QDateTimeEdit8dateTimeEv')
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def date(self) -> QDate:
    """
    Calls Qt's 'QDate QDateTimeEdit::date() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#date

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QDateTimeEdit::date() const
    address = self.uglySide.call('ritual_ZNK13QDateTimeEdit4dateEv')
    from ..QtCore import QDate
    return QDate._cuteOwning(address)

  def time(self) -> QTime:
    """
    Calls Qt's 'QTime QDateTimeEdit::time() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#time

    Returns
    -------

    QTime
      A new cute QTime around the copy Qt gave back. Python owns it.
    """
    #  QTime QDateTimeEdit::time() const
    address = self.uglySide.call('ritual_ZNK13QDateTimeEdit4timeEv')
    from ..QtCore import QTime
    return QTime._cuteOwning(address)

  def calendar(self) -> QCalendar:
    """
    Calls Qt's 'QCalendar QDateTimeEdit::calendar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#calendar

    Returns
    -------

    QCalendar
      A new cute QCalendar around the copy Qt gave back. Python owns it.
    """
    #  QCalendar QDateTimeEdit::calendar() const
    address = self.uglySide.call('ritual_ZNK13QDateTimeEdit8calendarEv')
    from ..QtCore import QCalendar
    return QCalendar._cuteOwning(address)

  def minimumDateTime(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTimeEdit::minimumDateTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#minimumDateTime

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTimeEdit::minimumDateTime() const
    address = self.uglySide.call(
        'ritual_ZNK13QDateTimeEdit15minimumDateTimeEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def maximumDateTime(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTimeEdit::maximumDateTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#maximumDateTime

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTimeEdit::maximumDateTime() const
    address = self.uglySide.call(
        'ritual_ZNK13QDateTimeEdit15maximumDateTimeEv',
    )
    from ..QtCore import QDateTime
    return QDateTime._cuteOwning(address)

  def minimumDate(self) -> QDate:
    """
    Calls Qt's 'QDate QDateTimeEdit::minimumDate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#minimumDate

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QDateTimeEdit::minimumDate() const
    address = self.uglySide.call('ritual_ZNK13QDateTimeEdit11minimumDateEv')
    from ..QtCore import QDate
    return QDate._cuteOwning(address)

  def maximumDate(self) -> QDate:
    """
    Calls Qt's 'QDate QDateTimeEdit::maximumDate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#maximumDate

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QDateTimeEdit::maximumDate() const
    address = self.uglySide.call('ritual_ZNK13QDateTimeEdit11maximumDateEv')
    from ..QtCore import QDate
    return QDate._cuteOwning(address)

  def minimumTime(self) -> QTime:
    """
    Calls Qt's 'QTime QDateTimeEdit::minimumTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#minimumTime

    Returns
    -------

    QTime
      A new cute QTime around the copy Qt gave back. Python owns it.
    """
    #  QTime QDateTimeEdit::minimumTime() const
    address = self.uglySide.call('ritual_ZNK13QDateTimeEdit11minimumTimeEv')
    from ..QtCore import QTime
    return QTime._cuteOwning(address)

  def maximumTime(self) -> QTime:
    """
    Calls Qt's 'QTime QDateTimeEdit::maximumTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#maximumTime

    Returns
    -------

    QTime
      A new cute QTime around the copy Qt gave back. Python owns it.
    """
    #  QTime QDateTimeEdit::maximumTime() const
    address = self.uglySide.call('ritual_ZNK13QDateTimeEdit11maximumTimeEv')
    from ..QtCore import QTime
    return QTime._cuteOwning(address)

  def displayedSections(self) -> Sections:
    """
    Calls Qt's 'Sections QDateTimeEdit::displayedSections() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeedit.html#displayedSections

    Returns
    -------

    Sections
      The value standing for the combination Qt gave back.
    """
    #  Sections QDateTimeEdit::displayedSections() const
    return QDateTimeEdit.Sections(self.uglySide.call(
        'ritual_ZNK13QDateTimeEdit17displayedSectionsEv',
    ))

  def currentSection(self) -> Section:
    """
    Calls Qt's 'Section QDateTimeEdit::currentSection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#currentSection

    Returns
    -------

    Section
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Section(number)' gives.
    """
    #  Section QDateTimeEdit::currentSection() const
    return QDateTimeEdit.Section(self.uglySide.call(
        'ritual_ZNK13QDateTimeEdit14currentSectionEv',
    ))

  @overload(int)
  def sectionAt(self, index: int) -> Section:
    """
    Calls Qt's 'Section QDateTimeEdit::sectionAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#sectionAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Section
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Section(number)' gives.
    """
    #  Section QDateTimeEdit::sectionAt(int index) const
    return QDateTimeEdit.Section(self.uglySide.call(
        'ritual_ZNK13QDateTimeEdit9sectionAtEi', index,
    ))

  def currentSectionIndex(self) -> int:
    """
    Calls Qt's 'int QDateTimeEdit::currentSectionIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeedit.html#currentSectionIndex
    """
    #  int QDateTimeEdit::currentSectionIndex() const
    return self.uglySide.call(
        'ritual_ZNK13QDateTimeEdit19currentSectionIndexEv',
    )

  def calendarWidget(self) -> Optional[QCalendarWidget]:
    """
    Calls Qt's 'QCalendarWidget *QDateTimeEdit::calendarWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#calendarWidget

    Returns
    -------

    Optional[QCalendarWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCalendarWidget *QDateTimeEdit::calendarWidget() const
    address = self.uglySide.call(
        'ritual_ZNK13QDateTimeEdit14calendarWidgetEv',
    )
    from . import QCalendarWidget
    return QCalendarWidget._cuteAt(address)

  def sectionCount(self) -> int:
    """
    Calls Qt's 'int QDateTimeEdit::sectionCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#sectionCount
    """
    #  int QDateTimeEdit::sectionCount() const
    return self.uglySide.call('ritual_ZNK13QDateTimeEdit12sectionCountEv')

  @overload(Section)
  def sectionText(self, section: Section) -> str:
    """
    Calls Qt's 'QString QDateTimeEdit::sectionText(Section section) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#sectionText

    Parameters
    ----------

    section : Section
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDateTimeEdit::sectionText(Section section) const
    return self.uglySide.call(
        'ritual_ZNK13QDateTimeEdit11sectionTextENS_7SectionE', section.value,
    )

  def displayFormat(self) -> str:
    """
    Calls Qt's 'QString QDateTimeEdit::displayFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#displayFormat

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDateTimeEdit::displayFormat() const
    return self.uglySide.call('ritual_ZNK13QDateTimeEdit13displayFormatEv')

  def calendarPopup(self) -> bool:
    """
    Calls Qt's 'bool QDateTimeEdit::calendarPopup() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#calendarPopup
    """
    #  bool QDateTimeEdit::calendarPopup() const
    return self.uglySide.call('ritual_ZNK13QDateTimeEdit13calendarPopupEv')

  def timeSpec(self) -> Qt.TimeSpec:
    """
    Calls Qt's 'Qt::TimeSpec QDateTimeEdit::timeSpec() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#timeSpec

    Returns
    -------

    Qt.TimeSpec
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.TimeSpec(number)'
      gives.
    """
    #  Qt::TimeSpec QDateTimeEdit::timeSpec() const
    return Qt.TimeSpec(self.uglySide.call(
        'ritual_ZNK13QDateTimeEdit8timeSpecEv',
    ))

  def timeZone(self) -> QTimeZone:
    """
    Calls Qt's 'QTimeZone QDateTimeEdit::timeZone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#timeZone

    Returns
    -------

    QTimeZone
      A new cute QTimeZone around the copy Qt gave back. Python owns it.
    """
    #  QTimeZone QDateTimeEdit::timeZone() const
    address = self.uglySide.call('ritual_ZNK13QDateTimeEdit8timeZoneEv')
    from ..QtCore import QTimeZone
    return QTimeZone._cuteOwning(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QDateTimeEdit::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QDateTimeEdit::sizeHint() const
    ritual = 'ritual_ZNK13QDateTimeEdit8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QDateTimeEdit8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QCalendar)
  def setCalendar(self, calendar: QCalendar) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::setCalendar(QCalendar calendar)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#setCalendar

    Parameters
    ----------

    calendar : QCalendar
      Passed on as a value: Qt reads the C++ QCalendar, which stays Python's
      own.
    """
    #  void QDateTimeEdit::setCalendar(QCalendar calendar)
    self.uglySide.call(
        'ritual_ZN13QDateTimeEdit11setCalendarE9QCalendar',
        self._valueOf(calendar),
    )

  @overload(QDateTime)
  def setMinimumDateTime(self, dt: QDateTime) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::setMinimumDateTime(const QDateTime &dt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeedit.html#setMinimumDateTime

    Parameters
    ----------

    dt : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QDateTimeEdit::setMinimumDateTime(const QDateTime &dt)
    self.uglySide.call(
        'ritual_ZN13QDateTimeEdit18setMinimumDateTimeERK9QDateTime',
        self._valueOf(dt),
    )

  @overload(QDateTime)
  def setMaximumDateTime(self, dt: QDateTime) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::setMaximumDateTime(const QDateTime &dt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeedit.html#setMaximumDateTime

    Parameters
    ----------

    dt : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QDateTimeEdit::setMaximumDateTime(const QDateTime &dt)
    self.uglySide.call(
        'ritual_ZN13QDateTimeEdit18setMaximumDateTimeERK9QDateTime',
        self._valueOf(dt),
    )

  @overload(QDateTime, QDateTime)
  def setDateTimeRange(self, min: QDateTime, max: QDateTime) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::setDateTimeRange(const QDateTime &min,
    const QDateTime &max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeedit.html#setDateTimeRange

    Parameters
    ----------

    min : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    max : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QDateTimeEdit::setDateTimeRange(const QDateTime &min, const
    #      QDateTime &max)
    self.uglySide.call(
        'ritual_ZN13QDateTimeEdit16setDateTimeRangeERK9QDateTimeS2_',
        self._valueOf(min), self._valueOf(max),
    )

  @overload(QDate)
  def setMinimumDate(self, min: QDate) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::setMinimumDate(QDate min)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#setMinimumDate

    Parameters
    ----------

    min : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.
    """
    #  void QDateTimeEdit::setMinimumDate(QDate min)
    self.uglySide.call(
        'ritual_ZN13QDateTimeEdit14setMinimumDateE5QDate',
        self._valueOf(min),
    )

  @overload(QDate)
  def setMaximumDate(self, max: QDate) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::setMaximumDate(QDate max)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#setMaximumDate

    Parameters
    ----------

    max : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.
    """
    #  void QDateTimeEdit::setMaximumDate(QDate max)
    self.uglySide.call(
        'ritual_ZN13QDateTimeEdit14setMaximumDateE5QDate',
        self._valueOf(max),
    )

  @overload(QDate, QDate)
  def setDateRange(self, min: QDate, max: QDate) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::setDateRange(QDate min, QDate max)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#setDateRange

    Parameters
    ----------

    min : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.

    max : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.
    """
    #  void QDateTimeEdit::setDateRange(QDate min, QDate max)
    self.uglySide.call(
        'ritual_ZN13QDateTimeEdit12setDateRangeE5QDateS0_',
        self._valueOf(min), self._valueOf(max),
    )

  @overload(QTime)
  def setMinimumTime(self, min: QTime) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::setMinimumTime(QTime min)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#setMinimumTime

    Parameters
    ----------

    min : QTime
      Passed on as a value: Qt reads the C++ QTime, which stays Python's own.
    """
    #  void QDateTimeEdit::setMinimumTime(QTime min)
    self.uglySide.call(
        'ritual_ZN13QDateTimeEdit14setMinimumTimeE5QTime',
        self._valueOf(min),
    )

  @overload(QTime)
  def setMaximumTime(self, max: QTime) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::setMaximumTime(QTime max)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#setMaximumTime

    Parameters
    ----------

    max : QTime
      Passed on as a value: Qt reads the C++ QTime, which stays Python's own.
    """
    #  void QDateTimeEdit::setMaximumTime(QTime max)
    self.uglySide.call(
        'ritual_ZN13QDateTimeEdit14setMaximumTimeE5QTime',
        self._valueOf(max),
    )

  @overload(QTime, QTime)
  def setTimeRange(self, min: QTime, max: QTime) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::setTimeRange(QTime min, QTime max)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#setTimeRange

    Parameters
    ----------

    min : QTime
      Passed on as a value: Qt reads the C++ QTime, which stays Python's own.

    max : QTime
      Passed on as a value: Qt reads the C++ QTime, which stays Python's own.
    """
    #  void QDateTimeEdit::setTimeRange(QTime min, QTime max)
    self.uglySide.call(
        'ritual_ZN13QDateTimeEdit12setTimeRangeE5QTimeS0_',
        self._valueOf(min), self._valueOf(max),
    )

  @overload(Section)
  def setCurrentSection(self, section: Section) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::setCurrentSection(Section section)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeedit.html#setCurrentSection

    Parameters
    ----------

    section : Section
      Passed on as its number.
    """
    #  void QDateTimeEdit::setCurrentSection(Section section)
    self.uglySide.call(
        'ritual_ZN13QDateTimeEdit17setCurrentSectionENS_7SectionE',
        section.value,
    )

  @overload(int)
  def setCurrentSectionIndex(self, index: int) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::setCurrentSectionIndex(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeedit.html#setCurrentSectionIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QDateTimeEdit::setCurrentSectionIndex(int index)
    self.uglySide.call(
        'ritual_ZN13QDateTimeEdit22setCurrentSectionIndexEi', index,
    )

  @overload(QCalendarWidget)
  @overload(NoneType)
  def setCalendarWidget(
      self,
      calendarWidget: Optional[QCalendarWidget],
  ) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::setCalendarWidget(QCalendarWidget
    *calendarWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeedit.html#setCalendarWidget

    Parameters
    ----------

    calendarWidget : Optional[QCalendarWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDateTimeEdit::setCalendarWidget(QCalendarWidget *calendarWidget)
    self.uglySide.call(
        'ritual_ZN13QDateTimeEdit17setCalendarWidgetEP15QCalendarWidget',
        self._addressOf(calendarWidget),
    )

  @overload(Section)
  def setSelectedSection(self, section: Section) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::setSelectedSection(Section section)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeedit.html#setSelectedSection

    Parameters
    ----------

    section : Section
      Passed on as its number.
    """
    #  void QDateTimeEdit::setSelectedSection(Section section)
    self.uglySide.call(
        'ritual_ZN13QDateTimeEdit18setSelectedSectionENS_7SectionE',
        section.value,
    )

  @overload(str)
  def setDisplayFormat(self, format: str) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::setDisplayFormat(const QString &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeedit.html#setDisplayFormat

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDateTimeEdit::setDisplayFormat(const QString &format)
    self.uglySide.call(
        'ritual_ZN13QDateTimeEdit16setDisplayFormatERK7QString', format,
    )

  @overload(bool)
  def setCalendarPopup(self, enable: bool) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::setCalendarPopup(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeedit.html#setCalendarPopup

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QDateTimeEdit::setCalendarPopup(bool enable)
    self.uglySide.call(
        'ritual_ZN13QDateTimeEdit16setCalendarPopupEb', enable,
    )

  @overload(Qt.TimeSpec)
  def setTimeSpec(self, spec: Qt.TimeSpec) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::setTimeSpec(Qt::TimeSpec spec)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#setTimeSpec

    Parameters
    ----------

    spec : Qt.TimeSpec
      Passed on as its number.
    """
    #  void QDateTimeEdit::setTimeSpec(Qt::TimeSpec spec)
    self.uglySide.call(
        'ritual_ZN13QDateTimeEdit11setTimeSpecEN2Qt8TimeSpecE', spec.value,
    )

  @overload(QTimeZone)
  def setTimeZone(self, zone: QTimeZone) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::setTimeZone(const QTimeZone &zone)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#setTimeZone

    Parameters
    ----------

    zone : QTimeZone
      Passed on as a value: Qt reads the C++ QTimeZone, which stays Python's
      own.
    """
    #  void QDateTimeEdit::setTimeZone(const QTimeZone &zone)
    self.uglySide.call(
        'ritual_ZN13QDateTimeEdit11setTimeZoneERK9QTimeZone',
        self._valueOf(zone),
    )

  @overload(QDateTime)
  def setDateTime(self, dateTime: QDateTime) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::setDateTime(const QDateTime &dateTime)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#setDateTime

    Parameters
    ----------

    dateTime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QDateTimeEdit::setDateTime(const QDateTime &dateTime)
    self.uglySide.call(
        'ritual_ZN13QDateTimeEdit11setDateTimeERK9QDateTime',
        self._valueOf(dateTime),
    )

  @overload(QDate)
  def setDate(self, date: QDate) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::setDate(QDate date)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#setDate

    Parameters
    ----------

    date : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.
    """
    #  void QDateTimeEdit::setDate(QDate date)
    self.uglySide.call(
        'ritual_ZN13QDateTimeEdit7setDateE5QDate', self._valueOf(date),
    )

  @overload(QTime)
  def setTime(self, time: QTime) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::setTime(QTime time)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#setTime

    Parameters
    ----------

    time : QTime
      Passed on as a value: Qt reads the C++ QTime, which stays Python's own.
    """
    #  void QDateTimeEdit::setTime(QTime time)
    self.uglySide.call(
        'ritual_ZN13QDateTimeEdit7setTimeE5QTime', self._valueOf(time),
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
    Notes what was given, for Qt's 'QDateTimeEdit::QDateTimeEdit(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#QDateTimeEdit

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDateTimeEdit::QDateTimeEdit(QWidget *parent)
    self._noteCreation(QDateTimeEdit, lambda: Rituals.call(
        'ritual_ZN13QDateTimeEditC1EP7QWidget', self._addressOf(parent),
    ))

  @overload(QDateTime)
  @overload(QDateTime, QWidget)
  @overload(QDateTime, NoneType)
  def __init__(
      self,
      dt: QDateTime,
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QDateTimeEdit::QDateTimeEdit(const
    QDateTime &dt, QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#QDateTimeEdit

    Parameters
    ----------

    dt : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDateTimeEdit::QDateTimeEdit(const QDateTime &dt, QWidget *parent)
    self._noteCreation(QDateTimeEdit, lambda: Rituals.call(
        'ritual_ZN13QDateTimeEditC1ERK9QDateTimeP7QWidget',
        self._valueOf(dt), self._addressOf(parent),
    ))

  @overload(QDate)
  @overload(QDate, QWidget)
  @overload(QDate, NoneType)
  def __init__(self, d: QDate, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QDateTimeEdit::QDateTimeEdit(QDate d,
    QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#QDateTimeEdit

    Parameters
    ----------

    d : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDateTimeEdit::QDateTimeEdit(QDate d, QWidget *parent)
    self._noteCreation(QDateTimeEdit, lambda: Rituals.call(
        'ritual_ZN13QDateTimeEditC1E5QDateP7QWidget',
        self._valueOf(d), self._addressOf(parent),
    ))

  @overload(QTime)
  @overload(QTime, QWidget)
  @overload(QTime, NoneType)
  def __init__(self, t: QTime, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QDateTimeEdit::QDateTimeEdit(QTime t,
    QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#QDateTimeEdit

    Parameters
    ----------

    t : QTime
      Passed on as a value: Qt reads the C++ QTime, which stays Python's own.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDateTimeEdit::QDateTimeEdit(QTime t, QWidget *parent)
    self._noteCreation(QDateTimeEdit, lambda: Rituals.call(
        'ritual_ZN13QDateTimeEditC1E5QTimeP7QWidget',
        self._valueOf(t), self._addressOf(parent),
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

  def clearMinimumDateTime(self) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::clearMinimumDateTime()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeedit.html#clearMinimumDateTime
    """
    #  void QDateTimeEdit::clearMinimumDateTime()
    self.uglySide.call('ritual_ZN13QDateTimeEdit20clearMinimumDateTimeEv')

  def clearMaximumDateTime(self) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::clearMaximumDateTime()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeedit.html#clearMaximumDateTime
    """
    #  void QDateTimeEdit::clearMaximumDateTime()
    self.uglySide.call('ritual_ZN13QDateTimeEdit20clearMaximumDateTimeEv')

  def clearMinimumDate(self) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::clearMinimumDate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeedit.html#clearMinimumDate
    """
    #  void QDateTimeEdit::clearMinimumDate()
    self.uglySide.call('ritual_ZN13QDateTimeEdit16clearMinimumDateEv')

  def clearMaximumDate(self) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::clearMaximumDate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeedit.html#clearMaximumDate
    """
    #  void QDateTimeEdit::clearMaximumDate()
    self.uglySide.call('ritual_ZN13QDateTimeEdit16clearMaximumDateEv')

  def clearMinimumTime(self) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::clearMinimumTime()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeedit.html#clearMinimumTime
    """
    #  void QDateTimeEdit::clearMinimumTime()
    self.uglySide.call('ritual_ZN13QDateTimeEdit16clearMinimumTimeEv')

  def clearMaximumTime(self) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::clearMaximumTime()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeedit.html#clearMaximumTime
    """
    #  void QDateTimeEdit::clearMaximumTime()
    self.uglySide.call('ritual_ZN13QDateTimeEdit16clearMaximumTimeEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#clear
    """
    #  void QDateTimeEdit::clear()
    ritual = 'ritual_ZN13QDateTimeEdit5clearEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QDateTimeEdit5clearEv'
    self.uglySide.call(ritual)

  @overload(int)
  def stepBy(self, steps: int) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::stepBy(int steps)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#stepBy

    Parameters
    ----------

    steps : int
      Passed on as it is.
    """
    #  void QDateTimeEdit::stepBy(int steps)
    ritual = 'ritual_ZN13QDateTimeEdit6stepByEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QDateTimeEdit6stepByEi'
    self.uglySide.call(ritual, steps)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QDateTimeEdit::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDateTimeEdit::event(QEvent *event)
    ritual = 'ritual_ZN13QDateTimeEdit5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QDateTimeEdit5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::keyPressEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDateTimeEdit::keyPressEvent(QKeyEvent *event)
    self.uglySide.call(
        'ritual_own_ZN13QDateTimeEdit13keyPressEventEP9QKeyEvent',
        self._addressOf(event),
    )

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, event: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::wheelEvent(QWheelEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#wheelEvent

    Parameters
    ----------

    event : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDateTimeEdit::wheelEvent(QWheelEvent *event)
    self.uglySide.call(
        'ritual_own_ZN13QDateTimeEdit10wheelEventEP11QWheelEvent',
        self._addressOf(event),
    )

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::focusInEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#focusInEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDateTimeEdit::focusInEvent(QFocusEvent *event)
    self.uglySide.call(
        'ritual_own_ZN13QDateTimeEdit12focusInEventEP11QFocusEvent',
        self._addressOf(event),
    )

  @overload(bool)
  def focusNextPrevChild(self, next: bool) -> bool:
    """
    Calls Qt's 'bool QDateTimeEdit::focusNextPrevChild(bool next)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetimeedit.html#focusNextPrevChild

    Parameters
    ----------

    next : bool
      Passed on as it is.
    """
    #  bool QDateTimeEdit::focusNextPrevChild(bool next)
    return self.uglySide.call(
        'ritual_own_ZN13QDateTimeEdit18focusNextPrevChildEb', next,
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::mousePressEvent(QMouseEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDateTimeEdit::mousePressEvent(QMouseEvent *event)
    self.uglySide.call(
        'ritual_own_ZN13QDateTimeEdit15mousePressEventEP11QMouseEvent',
        self._addressOf(event),
    )

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, event: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::paintEvent(QPaintEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#paintEvent

    Parameters
    ----------

    event : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDateTimeEdit::paintEvent(QPaintEvent *event)
    self.uglySide.call(
        'ritual_own_ZN13QDateTimeEdit10paintEventEP11QPaintEvent',
        self._addressOf(event),
    )

  @overload(QStyleOptionSpinBox)
  @overload(NoneType)
  def initStyleOption(self, option: Optional[QStyleOptionSpinBox]) -> None:
    """
    Calls Qt's 'void QDateTimeEdit::initStyleOption(QStyleOptionSpinBox
    *option) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetimeedit.html#initStyleOption

    Parameters
    ----------

    option : Optional[QStyleOptionSpinBox]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDateTimeEdit::initStyleOption(QStyleOptionSpinBox *option) const
    self.uglySide.call(
        'ritual_own_ZNK13QDateTimeEdit15initStyleOptionEP19QStyleOptionSpin'
        'Box',
        self._addressOf(option),
    )
