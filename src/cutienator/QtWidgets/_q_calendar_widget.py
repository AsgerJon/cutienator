"""
QCalendarWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qcalendarwidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QCalendar, QDate, QEvent, QMetaObject, QRect, QSize
  from ..QtGui import QKeyEvent, QMouseEvent, QPainter, QResizeEvent
  from ..QtGui import QTextCharFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCalendar = WAIT['QCalendar']
  QDate = WAIT['QDate']
  QEvent = WAIT['QEvent']
  QKeyEvent = WAIT['QKeyEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPainter = WAIT['QPainter']
  QRect = WAIT['QRect']
  QResizeEvent = WAIT['QResizeEvent']
  QTextCharFormat = WAIT['QTextCharFormat']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCalendarWidget(QWidget):
  """
  The cute side of Qt's QCalendarWidget: a plain Python object standing in
  front of one C++ QCalendarWidget.

  It is built on the cute 'QWidget', as Qt's QCalendarWidget is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCalendarWidget that has a ritual and that Python
  can call so far, 54 names in all: 'metaObject', 'tr', 'sizeHint',
  'minimumSizeHint', 'selectedDate', 'yearShown', 'monthShown',
  'minimumDate', 'setMinimumDate', 'clearMinimumDate', 'maximumDate',
  'setMaximumDate', 'clearMaximumDate', 'firstDayOfWeek',
  'setFirstDayOfWeek', 'isNavigationBarVisible', 'isGridVisible', 'calendar',
  'setCalendar', 'selectionMode', 'setSelectionMode',
  'horizontalHeaderFormat', 'setHorizontalHeaderFormat',
  'verticalHeaderFormat', 'setVerticalHeaderFormat', 'headerTextFormat',
  'setHeaderTextFormat', 'weekdayTextFormat', 'setWeekdayTextFormat',
  'dateTextFormat', 'setDateTextFormat', 'isDateEditEnabled',
  'setDateEditEnabled', 'dateEditAcceptDelay', 'setDateEditAcceptDelay',
  'event', 'eventFilter', 'mousePressEvent', 'resizeEvent', 'keyPressEvent',
  'paintCell', 'updateCell', 'updateCells', 'setSelectedDate',
  'setDateRange', 'setCurrentPage', 'setGridVisible',
  'setNavigationBarVisible', 'showNextMonth', 'showPreviousMonth',
  'showNextYear', 'showPreviousYear', 'showSelectedDate', 'showToday'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCalendarWidget::~QCalendarWidget()': the destructor: Python never
    removes a C++ QCalendarWidget.

  What has no ritual
  ------------------

  13 of the 69 functions Qt declares: 5 takes or gives a type that cannot be
  passed yet; 4 a signal; 2 forbidden; 1 a template; 1 declared and nowhere
  to be found.

  What to expect
  --------------

  - The C++ QCalendarWidget is created at the first use, not by
    'QCalendarWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCalendarWidget.
  - Qt tells when it has removed the C++ QCalendarWidget. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QCalendarWidget, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class HorizontalHeaderFormat(CuteNum):
    """
    The enum 'QCalendarWidget::HorizontalHeaderFormat' of Qt, with the 4
    names Qt gives in it.
    """

    NoHorizontalHeader = Kee[int](0)
    SingleLetterDayNames = Kee[int](1)
    ShortDayNames = Kee[int](2)
    LongDayNames = Kee[int](3)

  class SelectionMode(CuteNum):
    """
    The enum 'QCalendarWidget::SelectionMode' of Qt, with the 2 names Qt
    gives in it.
    """

    NoSelection = Kee[int](0)
    SingleSelection = Kee[int](1)

  class VerticalHeaderFormat(CuteNum):
    """
    The enum 'QCalendarWidget::VerticalHeaderFormat' of Qt, with the 2 names
    Qt gives in it.
    """

    NoVerticalHeader = Kee[int](0)
    ISOWeekNumbers = Kee[int](1)

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
    Calls Qt's 'QString QCalendarWidget::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarwidget.html#tr

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
    #  QString QCalendarWidget::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QCalendarWidget2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCalendarWidget'

  #  A C++ QCalendarWidget Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCalendarWidget'

  #  The functions Qt calls itself that QCalendarWidget is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'paintCell': (
          ('_ZNK15QCalendarWidget9paintCellEP8QPainterRK5QRect5QDate',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QPainter'),
               ('address', 'value', 'QtCore:QRect'),
               ('address', 'value', 'QtCore:QDate'),
           )),
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
    Calls Qt's 'const QMetaObject *QCalendarWidget::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarwidget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCalendarWidget::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QCalendarWidget10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QCalendarWidget::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarwidget.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QCalendarWidget::sizeHint() const
    ritual = 'ritual_ZNK15QCalendarWidget8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QCalendarWidget8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QCalendarWidget::minimumSizeHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#minimumSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QCalendarWidget::minimumSizeHint() const
    ritual = 'ritual_ZNK15QCalendarWidget15minimumSizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QCalendarWidget15minimumSizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def selectedDate(self) -> QDate:
    """
    Calls Qt's 'QDate QCalendarWidget::selectedDate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarwidget.html#selectedDate

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QCalendarWidget::selectedDate() const
    address = self.uglySide.call(
        'ritual_ZNK15QCalendarWidget12selectedDateEv',
    )
    from ..QtCore import QDate
    return QDate._cuteOwning(address)

  def yearShown(self) -> int:
    """
    Calls Qt's 'int QCalendarWidget::yearShown() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarwidget.html#yearShown
    """
    #  int QCalendarWidget::yearShown() const
    return self.uglySide.call('ritual_ZNK15QCalendarWidget9yearShownEv')

  def monthShown(self) -> int:
    """
    Calls Qt's 'int QCalendarWidget::monthShown() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarwidget.html#monthShown
    """
    #  int QCalendarWidget::monthShown() const
    return self.uglySide.call('ritual_ZNK15QCalendarWidget10monthShownEv')

  def minimumDate(self) -> QDate:
    """
    Calls Qt's 'QDate QCalendarWidget::minimumDate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarwidget.html#minimumDate

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QCalendarWidget::minimumDate() const
    address = self.uglySide.call(
        'ritual_ZNK15QCalendarWidget11minimumDateEv',
    )
    from ..QtCore import QDate
    return QDate._cuteOwning(address)

  def maximumDate(self) -> QDate:
    """
    Calls Qt's 'QDate QCalendarWidget::maximumDate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarwidget.html#maximumDate

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QCalendarWidget::maximumDate() const
    address = self.uglySide.call(
        'ritual_ZNK15QCalendarWidget11maximumDateEv',
    )
    from ..QtCore import QDate
    return QDate._cuteOwning(address)

  def firstDayOfWeek(self) -> Qt.DayOfWeek:
    """
    Calls Qt's 'Qt::DayOfWeek QCalendarWidget::firstDayOfWeek() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#firstDayOfWeek

    Returns
    -------

    Qt.DayOfWeek
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.DayOfWeek(number)'
      gives.
    """
    #  Qt::DayOfWeek QCalendarWidget::firstDayOfWeek() const
    return Qt.DayOfWeek(self.uglySide.call(
        'ritual_ZNK15QCalendarWidget14firstDayOfWeekEv',
    ))

  def isNavigationBarVisible(self) -> bool:
    """
    Calls Qt's 'bool QCalendarWidget::isNavigationBarVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#isNavigationBarVisible
    """
    #  bool QCalendarWidget::isNavigationBarVisible() const
    return self.uglySide.call(
        'ritual_ZNK15QCalendarWidget22isNavigationBarVisibleEv',
    )

  def isGridVisible(self) -> bool:
    """
    Calls Qt's 'bool QCalendarWidget::isGridVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarwidget.html#isGridVisible
    """
    #  bool QCalendarWidget::isGridVisible() const
    return self.uglySide.call('ritual_ZNK15QCalendarWidget13isGridVisibleEv')

  def calendar(self) -> QCalendar:
    """
    Calls Qt's 'QCalendar QCalendarWidget::calendar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarwidget.html#calendar

    Returns
    -------

    QCalendar
      A new cute QCalendar around the copy Qt gave back. Python owns it.
    """
    #  QCalendar QCalendarWidget::calendar() const
    address = self.uglySide.call('ritual_ZNK15QCalendarWidget8calendarEv')
    from ..QtCore import QCalendar
    return QCalendar._cuteOwning(address)

  def selectionMode(self) -> SelectionMode:
    """
    Calls Qt's 'SelectionMode QCalendarWidget::selectionMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarwidget.html#selectionMode

    Returns
    -------

    SelectionMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SelectionMode(number)'
      gives.
    """
    #  SelectionMode QCalendarWidget::selectionMode() const
    return QCalendarWidget.SelectionMode(self.uglySide.call(
        'ritual_ZNK15QCalendarWidget13selectionModeEv',
    ))

  def horizontalHeaderFormat(self) -> HorizontalHeaderFormat:
    """
    Calls Qt's 'HorizontalHeaderFormat
    QCalendarWidget::horizontalHeaderFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#horizontalHeaderFormat

    Returns
    -------

    HorizontalHeaderFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'HorizontalHeaderFormat(number)' gives.
    """
    #  HorizontalHeaderFormat QCalendarWidget::horizontalHeaderFormat() const
    return QCalendarWidget.HorizontalHeaderFormat(self.uglySide.call(
        'ritual_ZNK15QCalendarWidget22horizontalHeaderFormatEv',
    ))

  def verticalHeaderFormat(self) -> VerticalHeaderFormat:
    """
    Calls Qt's 'VerticalHeaderFormat QCalendarWidget::verticalHeaderFormat()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#verticalHeaderFormat

    Returns
    -------

    VerticalHeaderFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'VerticalHeaderFormat(number)' gives.
    """
    #  VerticalHeaderFormat QCalendarWidget::verticalHeaderFormat() const
    return QCalendarWidget.VerticalHeaderFormat(self.uglySide.call(
        'ritual_ZNK15QCalendarWidget20verticalHeaderFormatEv',
    ))

  def headerTextFormat(self) -> QTextCharFormat:
    """
    Calls Qt's 'QTextCharFormat QCalendarWidget::headerTextFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#headerTextFormat

    Returns
    -------

    QTextCharFormat
      A new cute QTextCharFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextCharFormat QCalendarWidget::headerTextFormat() const
    address = self.uglySide.call(
        'ritual_ZNK15QCalendarWidget16headerTextFormatEv',
    )
    from ..QtGui import QTextCharFormat
    return QTextCharFormat._cuteOwning(address)

  @overload(Qt.DayOfWeek)
  def weekdayTextFormat(self, dayOfWeek: Qt.DayOfWeek) -> QTextCharFormat:
    """
    Calls Qt's 'QTextCharFormat
    QCalendarWidget::weekdayTextFormat(Qt::DayOfWeek dayOfWeek) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#weekdayTextFormat

    Parameters
    ----------

    dayOfWeek : Qt.DayOfWeek
      Passed on as its number.

    Returns
    -------

    QTextCharFormat
      A new cute QTextCharFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextCharFormat QCalendarWidget::weekdayTextFormat(Qt::DayOfWeek
    #      dayOfWeek) const
    address = self.uglySide.call(
        'ritual_ZNK15QCalendarWidget17weekdayTextFormatEN2Qt9DayOfWeekE',
        dayOfWeek.value,
    )
    from ..QtGui import QTextCharFormat
    return QTextCharFormat._cuteOwning(address)

  @overload(QDate)
  def dateTextFormat(self, date: QDate) -> QTextCharFormat:
    """
    Calls Qt's 'QTextCharFormat QCalendarWidget::dateTextFormat(QDate date)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#dateTextFormat

    Parameters
    ----------

    date : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.

    Returns
    -------

    QTextCharFormat
      A new cute QTextCharFormat around the copy Qt gave back. Python owns
      it.
    """
    #  QTextCharFormat QCalendarWidget::dateTextFormat(QDate date) const
    address = self.uglySide.call(
        'ritual_ZNK15QCalendarWidget14dateTextFormatE5QDate',
        self._valueOf(date),
    )
    from ..QtGui import QTextCharFormat
    return QTextCharFormat._cuteOwning(address)

  def isDateEditEnabled(self) -> bool:
    """
    Calls Qt's 'bool QCalendarWidget::isDateEditEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#isDateEditEnabled
    """
    #  bool QCalendarWidget::isDateEditEnabled() const
    return self.uglySide.call(
        'ritual_ZNK15QCalendarWidget17isDateEditEnabledEv',
    )

  def dateEditAcceptDelay(self) -> int:
    """
    Calls Qt's 'int QCalendarWidget::dateEditAcceptDelay() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#dateEditAcceptDelay
    """
    #  int QCalendarWidget::dateEditAcceptDelay() const
    return self.uglySide.call(
        'ritual_ZNK15QCalendarWidget19dateEditAcceptDelayEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDate)
  def setMinimumDate(self, date: QDate) -> None:
    """
    Calls Qt's 'void QCalendarWidget::setMinimumDate(QDate date)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#setMinimumDate

    Parameters
    ----------

    date : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.
    """
    #  void QCalendarWidget::setMinimumDate(QDate date)
    self.uglySide.call(
        'ritual_ZN15QCalendarWidget14setMinimumDateE5QDate',
        self._valueOf(date),
    )

  @overload(QDate)
  def setMaximumDate(self, date: QDate) -> None:
    """
    Calls Qt's 'void QCalendarWidget::setMaximumDate(QDate date)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#setMaximumDate

    Parameters
    ----------

    date : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.
    """
    #  void QCalendarWidget::setMaximumDate(QDate date)
    self.uglySide.call(
        'ritual_ZN15QCalendarWidget14setMaximumDateE5QDate',
        self._valueOf(date),
    )

  @overload(Qt.DayOfWeek)
  def setFirstDayOfWeek(self, dayOfWeek: Qt.DayOfWeek) -> None:
    """
    Calls Qt's 'void QCalendarWidget::setFirstDayOfWeek(Qt::DayOfWeek
    dayOfWeek)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#setFirstDayOfWeek

    Parameters
    ----------

    dayOfWeek : Qt.DayOfWeek
      Passed on as its number.
    """
    #  void QCalendarWidget::setFirstDayOfWeek(Qt::DayOfWeek dayOfWeek)
    self.uglySide.call(
        'ritual_ZN15QCalendarWidget17setFirstDayOfWeekEN2Qt9DayOfWeekE',
        dayOfWeek.value,
    )

  @overload(QCalendar)
  def setCalendar(self, calendar: QCalendar) -> None:
    """
    Calls Qt's 'void QCalendarWidget::setCalendar(QCalendar calendar)'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarwidget.html#setCalendar

    Parameters
    ----------

    calendar : QCalendar
      Passed on as a value: Qt reads the C++ QCalendar, which stays Python's
      own.
    """
    #  void QCalendarWidget::setCalendar(QCalendar calendar)
    self.uglySide.call(
        'ritual_ZN15QCalendarWidget11setCalendarE9QCalendar',
        self._valueOf(calendar),
    )

  @overload(SelectionMode)
  def setSelectionMode(self, mode: SelectionMode) -> None:
    """
    Calls Qt's 'void QCalendarWidget::setSelectionMode(SelectionMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#setSelectionMode

    Parameters
    ----------

    mode : SelectionMode
      Passed on as its number.
    """
    #  void QCalendarWidget::setSelectionMode(SelectionMode mode)
    self.uglySide.call(
        'ritual_ZN15QCalendarWidget16setSelectionModeENS_13SelectionModeE',
        mode.value,
    )

  @overload(HorizontalHeaderFormat)
  def setHorizontalHeaderFormat(
      self,
      format: HorizontalHeaderFormat,
  ) -> None:
    """
    Calls Qt's 'void
    QCalendarWidget::setHorizontalHeaderFormat(HorizontalHeaderFormat
    format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#setHorizontalHeaderFormat

    Parameters
    ----------

    format : HorizontalHeaderFormat
      Passed on as its number.
    """
    #  void QCalendarWidget::setHorizontalHeaderFormat(HorizontalHeaderFormat
    #      format)
    self.uglySide.call(
        'ritual_ZN15QCalendarWidget25setHorizontalHeaderFormatENS_22Horizon'
        'talHeaderFormatE',
        format.value,
    )

  @overload(VerticalHeaderFormat)
  def setVerticalHeaderFormat(self, format: VerticalHeaderFormat) -> None:
    """
    Calls Qt's 'void
    QCalendarWidget::setVerticalHeaderFormat(VerticalHeaderFormat format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#setVerticalHeaderFormat

    Parameters
    ----------

    format : VerticalHeaderFormat
      Passed on as its number.
    """
    #  void QCalendarWidget::setVerticalHeaderFormat(VerticalHeaderFormat
    #      format)
    self.uglySide.call(
        'ritual_ZN15QCalendarWidget23setVerticalHeaderFormatENS_20VerticalH'
        'eaderFormatE',
        format.value,
    )

  @overload(QTextCharFormat)
  def setHeaderTextFormat(self, format: QTextCharFormat) -> None:
    """
    Calls Qt's 'void QCalendarWidget::setHeaderTextFormat(const
    QTextCharFormat &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#setHeaderTextFormat

    Parameters
    ----------

    format : QTextCharFormat
      Passed on as a value: Qt reads the C++ QTextCharFormat, which stays
      Python's own.
    """
    #  void QCalendarWidget::setHeaderTextFormat(const QTextCharFormat
    #      &format)
    self.uglySide.call(
        'ritual_ZN15QCalendarWidget19setHeaderTextFormatERK15QTextCharForma'
        't',
        self._valueOf(format),
    )

  @overload(Qt.DayOfWeek, QTextCharFormat)
  def setWeekdayTextFormat(
      self,
      dayOfWeek: Qt.DayOfWeek,
      format: QTextCharFormat,
  ) -> None:
    """
    Calls Qt's 'void QCalendarWidget::setWeekdayTextFormat(Qt::DayOfWeek
    dayOfWeek, const QTextCharFormat &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#setWeekdayTextFormat

    Parameters
    ----------

    dayOfWeek : Qt.DayOfWeek
      Passed on as its number.

    format : QTextCharFormat
      Passed on as a value: Qt reads the C++ QTextCharFormat, which stays
      Python's own.
    """
    #  void QCalendarWidget::setWeekdayTextFormat(Qt::DayOfWeek dayOfWeek,
    #      const QTextCharFormat &format)
    self.uglySide.call(
        'ritual_ZN15QCalendarWidget20setWeekdayTextFormatEN2Qt9DayOfWeekERK'
        '15QTextCharFormat',
        dayOfWeek.value, self._valueOf(format),
    )

  @overload(QDate, QTextCharFormat)
  def setDateTextFormat(self, date: QDate, format: QTextCharFormat) -> None:
    """
    Calls Qt's 'void QCalendarWidget::setDateTextFormat(QDate date, const
    QTextCharFormat &format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#setDateTextFormat

    Parameters
    ----------

    date : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.

    format : QTextCharFormat
      Passed on as a value: Qt reads the C++ QTextCharFormat, which stays
      Python's own.
    """
    #  void QCalendarWidget::setDateTextFormat(QDate date, const
    #      QTextCharFormat &format)
    self.uglySide.call(
        'ritual_ZN15QCalendarWidget17setDateTextFormatE5QDateRK15QTextCharF'
        'ormat',
        self._valueOf(date), self._valueOf(format),
    )

  @overload(bool)
  def setDateEditEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QCalendarWidget::setDateEditEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#setDateEditEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QCalendarWidget::setDateEditEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN15QCalendarWidget18setDateEditEnabledEb', enable,
    )

  @overload(int)
  def setDateEditAcceptDelay(self, delay: int) -> None:
    """
    Calls Qt's 'void QCalendarWidget::setDateEditAcceptDelay(int delay)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#setDateEditAcceptDelay

    Parameters
    ----------

    delay : int
      Passed on as it is.
    """
    #  void QCalendarWidget::setDateEditAcceptDelay(int delay)
    self.uglySide.call(
        'ritual_ZN15QCalendarWidget22setDateEditAcceptDelayEi', delay,
    )

  @overload(QDate)
  def setSelectedDate(self, date: QDate) -> None:
    """
    Calls Qt's 'void QCalendarWidget::setSelectedDate(QDate date)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#setSelectedDate

    Parameters
    ----------

    date : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.
    """
    #  void QCalendarWidget::setSelectedDate(QDate date)
    self.uglySide.call(
        'ritual_ZN15QCalendarWidget15setSelectedDateE5QDate',
        self._valueOf(date),
    )

  @overload(QDate, QDate)
  def setDateRange(self, min: QDate, max: QDate) -> None:
    """
    Calls Qt's 'void QCalendarWidget::setDateRange(QDate min, QDate max)'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarwidget.html#setDateRange

    Parameters
    ----------

    min : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.

    max : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.
    """
    #  void QCalendarWidget::setDateRange(QDate min, QDate max)
    self.uglySide.call(
        'ritual_ZN15QCalendarWidget12setDateRangeE5QDateS0_',
        self._valueOf(min), self._valueOf(max),
    )

  @overload(int, int)
  def setCurrentPage(self, year: int, month: int) -> None:
    """
    Calls Qt's 'void QCalendarWidget::setCurrentPage(int year, int month)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#setCurrentPage

    Parameters
    ----------

    year : int
      Passed on as it is.

    month : int
      Passed on as it is.
    """
    #  void QCalendarWidget::setCurrentPage(int year, int month)
    self.uglySide.call(
        'ritual_ZN15QCalendarWidget14setCurrentPageEii', year, month,
    )

  @overload(bool)
  def setGridVisible(self, show: bool) -> None:
    """
    Calls Qt's 'void QCalendarWidget::setGridVisible(bool show)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#setGridVisible

    Parameters
    ----------

    show : bool
      Passed on as it is.
    """
    #  void QCalendarWidget::setGridVisible(bool show)
    self.uglySide.call('ritual_ZN15QCalendarWidget14setGridVisibleEb', show)

  @overload(bool)
  def setNavigationBarVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QCalendarWidget::setNavigationBarVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#setNavigationBarVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QCalendarWidget::setNavigationBarVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN15QCalendarWidget23setNavigationBarVisibleEb', visible,
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
    Notes what was given, for Qt's 'QCalendarWidget::QCalendarWidget(QWidget
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#QCalendarWidget

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCalendarWidget::QCalendarWidget(QWidget *parent)
    self._noteCreation(QCalendarWidget, lambda: Rituals.call(
        'ritual_ZN15QCalendarWidgetC1EP7QWidget', self._addressOf(parent),
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

  def clearMinimumDate(self) -> None:
    """
    Calls Qt's 'void QCalendarWidget::clearMinimumDate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#clearMinimumDate
    """
    #  void QCalendarWidget::clearMinimumDate()
    self.uglySide.call('ritual_ZN15QCalendarWidget16clearMinimumDateEv')

  def clearMaximumDate(self) -> None:
    """
    Calls Qt's 'void QCalendarWidget::clearMaximumDate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#clearMaximumDate
    """
    #  void QCalendarWidget::clearMaximumDate()
    self.uglySide.call('ritual_ZN15QCalendarWidget16clearMaximumDateEv')

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QCalendarWidget::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarwidget.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCalendarWidget::event(QEvent *event)
    ritual = 'ritual_ZN15QCalendarWidget5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QCalendarWidget5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      watched: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QCalendarWidget::eventFilter(QObject *watched, QEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarwidget.html#eventFilter

    Parameters
    ----------

    watched : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCalendarWidget::eventFilter(QObject *watched, QEvent *event)
    ritual = 'ritual_ZN15QCalendarWidget11eventFilterEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QCalendarWidget11eventFilterEP7QObjectP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(watched), self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QCalendarWidget::mousePressEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCalendarWidget::mousePressEvent(QMouseEvent *event)
    ritual = 'ritual_ZN15QCalendarWidget15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QCalendarWidget15mousePressEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, event: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QCalendarWidget::resizeEvent(QResizeEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarwidget.html#resizeEvent

    Parameters
    ----------

    event : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCalendarWidget::resizeEvent(QResizeEvent *event)
    ritual = 'ritual_ZN15QCalendarWidget11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QCalendarWidget11resizeEventEP12QResizeEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QCalendarWidget::keyPressEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarwidget.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCalendarWidget::keyPressEvent(QKeyEvent *event)
    ritual = 'ritual_ZN15QCalendarWidget13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QCalendarWidget13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QPainter, QRect, QDate)
  @overload(NoneType, QRect, QDate)
  def paintCell(
      self,
      painter: Optional[QPainter],
      rect: QRect,
      date: QDate,
  ) -> None:
    """
    Calls Qt's 'void QCalendarWidget::paintCell(QPainter *painter, const
    QRect &rect, QDate date) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarwidget.html#paintCell

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    date : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.
    """
    #  void QCalendarWidget::paintCell(QPainter *painter, const QRect &rect,
    #      QDate date) const
    ritual = 'ritual_ZNK15QCalendarWidget9paintCellEP8QPainterRK5QRect5QDate'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK15QCalendarWidget9paintCellEP8QPainterRK5QRect5QDa'
          'te')
    self.uglySide.call(
        ritual,
        self._addressOf(painter), self._valueOf(rect), self._valueOf(date),
    )

  @overload(QDate)
  def updateCell(self, date: QDate) -> None:
    """
    Calls Qt's 'void QCalendarWidget::updateCell(QDate date)'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarwidget.html#updateCell

    Parameters
    ----------

    date : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.
    """
    #  void QCalendarWidget::updateCell(QDate date)
    self.uglySide.call(
        'ritual_ZN15QCalendarWidget10updateCellE5QDate', self._valueOf(date),
    )

  def updateCells(self) -> None:
    """
    Calls Qt's 'void QCalendarWidget::updateCells()'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarwidget.html#updateCells
    """
    #  void QCalendarWidget::updateCells()
    self.uglySide.call('ritual_ZN15QCalendarWidget11updateCellsEv')

  def showNextMonth(self) -> None:
    """
    Calls Qt's 'void QCalendarWidget::showNextMonth()'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarwidget.html#showNextMonth
    """
    #  void QCalendarWidget::showNextMonth()
    self.uglySide.call('ritual_ZN15QCalendarWidget13showNextMonthEv')

  def showPreviousMonth(self) -> None:
    """
    Calls Qt's 'void QCalendarWidget::showPreviousMonth()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#showPreviousMonth
    """
    #  void QCalendarWidget::showPreviousMonth()
    self.uglySide.call('ritual_ZN15QCalendarWidget17showPreviousMonthEv')

  def showNextYear(self) -> None:
    """
    Calls Qt's 'void QCalendarWidget::showNextYear()'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarwidget.html#showNextYear
    """
    #  void QCalendarWidget::showNextYear()
    self.uglySide.call('ritual_ZN15QCalendarWidget12showNextYearEv')

  def showPreviousYear(self) -> None:
    """
    Calls Qt's 'void QCalendarWidget::showPreviousYear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#showPreviousYear
    """
    #  void QCalendarWidget::showPreviousYear()
    self.uglySide.call('ritual_ZN15QCalendarWidget16showPreviousYearEv')

  def showSelectedDate(self) -> None:
    """
    Calls Qt's 'void QCalendarWidget::showSelectedDate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarwidget.html#showSelectedDate
    """
    #  void QCalendarWidget::showSelectedDate()
    self.uglySide.call('ritual_ZN15QCalendarWidget16showSelectedDateEv')

  def showToday(self) -> None:
    """
    Calls Qt's 'void QCalendarWidget::showToday()'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarwidget.html#showToday
    """
    #  void QCalendarWidget::showToday()
    self.uglySide.call('ritual_ZN15QCalendarWidget9showTodayEv')
