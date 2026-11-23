"""
QCalendarPopup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qdatetimeedit_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QCalendarPopup to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import Qt
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QDate, QEvent, QMetaObject
  from ..QtGui import QHideEvent, QMouseEvent
  from . import QCalendarWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCalendarWidget = WAIT['QCalendarWidget']
  QDate = WAIT['QDate']
  QEvent = WAIT['QEvent']
  QHideEvent = WAIT['QHideEvent']
  QMouseEvent = WAIT['QMouseEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCalendarPopup(QWidget):
  """
  The cute side of Qt's QCalendarPopup: a plain Python object standing in
  front of one C++ QCalendarPopup.

  It is built on the cute 'QWidget', as Qt's QCalendarPopup is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCalendarPopup that has a ritual and that Python can
  call so far, 12 names in all: 'metaObject', 'selectedDate', 'setDate',
  'setDateRange', 'setFirstDayOfWeek', 'calendarWidget', 'setCalendarWidget',
  'hideEvent', 'mousePressEvent', 'mouseReleaseEvent', 'event',
  'verifyCalendarInstance'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has no ritual
  ------------------

  14 of the 26 functions Qt declares: 5 leans on 'QCalendarPopup; 4 a signal;
  2 takes or gives a type that cannot be passed yet; 1 a template; 1 declared
  and nowhere to be found; 1 leans on 'vtable for QCalendarPopup', which Qt's
  library does not offer and Qt's source has no code for that could be taken.

  What to expect
  --------------

  - The C++ QCalendarPopup is created at the first use, not by
    'QCalendarPopup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCalendarPopup.
  - Qt tells when it has removed the C++ QCalendarPopup. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCalendarPopup'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCalendarPopup::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarpopup.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCalendarPopup::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QCalendarPopup10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def calendarWidget(self) -> Optional[QCalendarWidget]:
    """
    Calls Qt's 'QCalendarWidget *QCalendarPopup::calendarWidget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarpopup.html#calendarWidget

    Returns
    -------

    Optional[QCalendarWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCalendarWidget *QCalendarPopup::calendarWidget() const
    address = self.uglySide.call(
        'ritual_ZNK14QCalendarPopup14calendarWidgetEv',
    )
    from . import QCalendarWidget
    return QCalendarWidget._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDate)
  def setDate(self, date: QDate) -> None:
    """
    Calls Qt's 'void QCalendarPopup::setDate(QDate date)'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarpopup.html#setDate

    Parameters
    ----------

    date : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.
    """
    #  void QCalendarPopup::setDate(QDate date)
    self.uglySide.call(
        'ritual_ZN14QCalendarPopup7setDateE5QDate', self._valueOf(date),
    )

  @overload(QDate, QDate)
  def setDateRange(self, min: QDate, max: QDate) -> None:
    """
    Calls Qt's 'void QCalendarPopup::setDateRange(QDate min, QDate max)'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarpopup.html#setDateRange

    Parameters
    ----------

    min : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.

    max : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.
    """
    #  void QCalendarPopup::setDateRange(QDate min, QDate max)
    self.uglySide.call(
        'ritual_ZN14QCalendarPopup12setDateRangeE5QDateS0_',
        self._valueOf(min), self._valueOf(max),
    )

  @overload(Qt.DayOfWeek)
  def setFirstDayOfWeek(self, dow: Qt.DayOfWeek) -> None:
    """
    Calls Qt's 'void QCalendarPopup::setFirstDayOfWeek(Qt::DayOfWeek dow)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarpopup.html#setFirstDayOfWeek

    Parameters
    ----------

    dow : Qt.DayOfWeek
      Passed on as its number.
    """
    #  void QCalendarPopup::setFirstDayOfWeek(Qt::DayOfWeek dow)
    self.uglySide.call(
        'ritual_ZN14QCalendarPopup17setFirstDayOfWeekEN2Qt9DayOfWeekE',
        dow.value,
    )

  @overload(QCalendarWidget)
  @overload(NoneType)
  def setCalendarWidget(self, cw: Optional[QCalendarWidget]) -> None:
    """
    Calls Qt's 'void QCalendarPopup::setCalendarWidget(QCalendarWidget *cw)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarpopup.html#setCalendarWidget

    Parameters
    ----------

    cw : Optional[QCalendarWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCalendarPopup::setCalendarWidget(QCalendarWidget *cw)
    self.uglySide.call(
        'ritual_ZN14QCalendarPopup17setCalendarWidgetEP15QCalendarWidget',
        self._addressOf(cw),
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

  def selectedDate(self) -> QDate:
    """
    Calls Qt's 'QDate QCalendarPopup::selectedDate()'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarpopup.html#selectedDate

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QCalendarPopup::selectedDate()
    address = self.uglySide.call('ritual_ZN14QCalendarPopup12selectedDateEv')
    from ..QtCore import QDate
    return QDate._cuteOwning(address)

  @overload(QHideEvent)
  @overload(NoneType)
  def hideEvent(self, a0: Optional[QHideEvent]) -> None:
    """
    Calls Qt's 'void QCalendarPopup::hideEvent(QHideEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarpopup.html#hideEvent

    Parameters
    ----------

    a0 : Optional[QHideEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCalendarPopup::hideEvent(QHideEvent *a0)
    self.uglySide.call(
        'ritual_ZN14QCalendarPopup9hideEventEP10QHideEvent',
        self._addressOf(a0),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, e: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QCalendarPopup::mousePressEvent(QMouseEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarpopup.html#mousePressEvent

    Parameters
    ----------

    e : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCalendarPopup::mousePressEvent(QMouseEvent *e)
    ritual = 'ritual_ZN14QCalendarPopup15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QCalendarPopup15mousePressEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QCalendarPopup::mouseReleaseEvent(QMouseEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarpopup.html#mouseReleaseEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QCalendarPopup::mouseReleaseEvent(QMouseEvent *a0)
    self.uglySide.call(
        'ritual_ZN14QCalendarPopup17mouseReleaseEventEP11QMouseEvent',
        self._addressOf(a0),
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QCalendarPopup::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarpopup.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QCalendarPopup::event(QEvent *e)
    ritual = 'ritual_ZN14QCalendarPopup5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QCalendarPopup5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  def verifyCalendarInstance(self) -> Optional[QCalendarWidget]:
    """
    Calls Qt's 'QCalendarWidget *QCalendarPopup::verifyCalendarInstance()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarpopup.html#verifyCalendarInstance

    Returns
    -------

    Optional[QCalendarWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCalendarWidget *QCalendarPopup::verifyCalendarInstance()
    address = self.uglySide.call(
        'ritual_ZN14QCalendarPopup22verifyCalendarInstanceEv',
    )
    from . import QCalendarWidget
    return QCalendarWidget._cuteAt(address)
