//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qdatetimeedit_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(datetimeedit)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qdatetimeedit_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdatetime.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qapplication_p.h>
#include <QtWidgets/private/qdatetimeedit_p.h>
#include <QtWidgets/qabstractspinbox.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qdatetimeedit.h>
#include <QtCore/qdebug.h>
#include <QtGui/qevent.h>
#include <QtWidgets/qlineedit.h>
#include <QtWidgets/private/qlineedit_p.h>
#include <QtCore/qlocale.h>
#include <QtGui/qpainter.h>
#include <QtWidgets/qlayout.h>
#include <QtCore/qset.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstylepainter.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2677, as _ZN14QCalendarPopup9hideEventEP10QHideEvent
inline void QCalendarPopup::hideEvent(QHideEvent *)
{
    emit resetButton();
    if (!dateChanged)
        emit hidingCalendar(oldDate);
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2633, as _ZN14QCalendarPopup15mousePressEventEP11QMouseEvent
inline void QCalendarPopup::mousePressEvent(QMouseEvent *event)
{
    QDateTimeEdit *dateTime = qobject_cast<QDateTimeEdit *>(parentWidget());
    if (dateTime) {
        QStyleOptionComboBox opt;
        opt.initFrom(dateTime);
        QRect arrowRect = dateTime->style()->subControlRect(QStyle::CC_ComboBox, &opt,
                                                            QStyle::SC_ComboBoxArrow, dateTime);
        arrowRect.moveTo(dateTime->mapToGlobal(arrowRect .topLeft()));
        if (arrowRect.contains(event->globalPosition().toPoint()) || rect().contains(event->position().toPoint()))
            setAttribute(Qt::WA_NoMouseReplay);
    }
    QWidget::mousePressEvent(event);
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2648, as _ZN14QCalendarPopup17mouseReleaseEventEP11QMouseEvent
inline void QCalendarPopup::mouseReleaseEvent(QMouseEvent*)
{
    emit resetButton();
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2653, as _ZN14QCalendarPopup5eventEP6QEvent
inline bool QCalendarPopup::event(QEvent *event)
{
#if QT_CONFIG(shortcut)
    if (event->type() == QEvent::KeyPress) {
        QKeyEvent *keyEvent = static_cast<QKeyEvent*>(event);
        if (keyEvent->matches(QKeySequence::Cancel))
            dateChanged = false;
    }
#endif
    return QWidget::event(event);
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2620, as _ZN14QCalendarPopup7setDateE5QDate
inline void QCalendarPopup::setDate(QDate date)
{
    oldDate = date;
    verifyCalendarInstance()->setSelectedDate(date);
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2626, as _ZN14QCalendarPopup12setDateRangeE5QDateS0_
inline void QCalendarPopup::setDateRange(QDate min, QDate max)
{
    QCalendarWidget *cw = verifyCalendarInstance();
    cw->setMinimumDate(min);
    cw->setMaximumDate(max);
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2599, as _ZN14QCalendarPopup17setCalendarWidgetEP15QCalendarWidget
inline void QCalendarPopup::setCalendarWidget(QCalendarWidget *cw)
{
    Q_ASSERT(cw);
    QVBoxLayout *widgetLayout = qobject_cast<QVBoxLayout*>(layout());
    if (!widgetLayout) {
        widgetLayout = new QVBoxLayout(this);
        widgetLayout->setContentsMargins(QMargins());
        widgetLayout->setSpacing(0);
    }
    delete calendar.data();
    calendar = QPointer<QCalendarWidget>(cw);
    widgetLayout->addWidget(cw);

    connect(cw, SIGNAL(activated(QDate)), this, SLOT(dateSelected(QDate)));
    connect(cw, SIGNAL(clicked(QDate)), this, SLOT(dateSelected(QDate)));
    connect(cw, SIGNAL(selectionChanged()), this, SLOT(dateSelectionChanged()));

    cw->setFocus();
}

//  from src/widgets/widgets/qdatetimeedit.cpp, line 2586, as _ZN14QCalendarPopup22verifyCalendarInstanceEv
inline QCalendarWidget *QCalendarPopup::verifyCalendarInstance()
{
    if (calendar.isNull()) {
        QCalendarWidget *cw = new QCalendarWidget(this);
        cw->setCalendar(calendarSystem);
        cw->setVerticalHeaderFormat(QCalendarWidget::NoVerticalHeader);
        setCalendarWidget(cw);
        return cw;
    } else {
        return calendar.data();
    }
}
//  -----------------------------------------------------------------------

//  Only a class built on QCalendarPopup may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQCalendarPopup : QCalendarPopup {
  using QCalendarPopup::mousePressEvent;
  using QCalendarPopup::event;
};

//  const QMetaObject *QCalendarPopup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QCalendarPopup10metaObjectEv(
    const QCalendarPopup *self) {
  return self->metaObject();
}

//  void *QCalendarPopup::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QCalendarPopup11qt_metacastEPKc(
    QCalendarPopup *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QCalendarPopup::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QCalendarPopup11qt_metacallEN11QMetaObject4CallEiPPv(
    QCalendarPopup *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QDate QCalendarPopup::selectedDate()
extern "C" Q_DECL_EXPORT
QDate *ritual_ZN14QCalendarPopup12selectedDateEv(QCalendarPopup *self) {
  return new QDate(self->selectedDate());
}

//  void QCalendarPopup::setDate(QDate date)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCalendarPopup7setDateE5QDate(
    QCalendarPopup *self,
    const QDate *date) {
  self->setDate(*date);
}

//  void QCalendarPopup::setDateRange(QDate min, QDate max)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCalendarPopup12setDateRangeE5QDateS0_(
    QCalendarPopup *self,
    const QDate *min,
    const QDate *max) {
  self->setDateRange(*min, *max);
}

//  void QCalendarPopup::setFirstDayOfWeek(Qt::DayOfWeek dow)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCalendarPopup17setFirstDayOfWeekEN2Qt9DayOfWeekE(
    QCalendarPopup *self,
    Qt::DayOfWeek dow) {
  self->setFirstDayOfWeek(dow);
}

//  QCalendarWidget *QCalendarPopup::calendarWidget() const
extern "C" Q_DECL_EXPORT
QCalendarWidget *ritual_ZNK14QCalendarPopup14calendarWidgetEv(
    const QCalendarPopup *self) {
  return self->calendarWidget();
}

//  void QCalendarPopup::setCalendarWidget(QCalendarWidget *cw)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCalendarPopup17setCalendarWidgetEP15QCalendarWidget(
    QCalendarPopup *self,
    QCalendarWidget *cw) {
  self->setCalendarWidget(cw);
}

//  void QCalendarPopup::activated(QDate date)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCalendarPopup9activatedE5QDate(
    QCalendarPopup *self,
    const QDate *date) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QCalendarPopup")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "activated(QDate)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "activated(QDate)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(date)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QCalendarPopup::newDateSelected(QDate newDate)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCalendarPopup15newDateSelectedE5QDate(
    QCalendarPopup *self,
    const QDate *newDate) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QCalendarPopup")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "newDateSelected(QDate)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "newDateSelected(QDate)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(newDate)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QCalendarPopup::hidingCalendar(QDate oldDate)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCalendarPopup14hidingCalendarE5QDate(
    QCalendarPopup *self,
    const QDate *oldDate) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QCalendarPopup")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "hidingCalendar(QDate)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "hidingCalendar(QDate)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(oldDate)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QCalendarPopup::resetButton()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCalendarPopup11resetButtonEv(QCalendarPopup *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QCalendarPopup")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "resetButton()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "resetButton()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QCalendarPopup::dateSelected(QDate date)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCalendarPopup12dateSelectedE5QDate(
    QCalendarPopup *self,
    const QDate *date) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QCalendarPopup")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "dateSelected(QDate)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "dateSelected(QDate)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(date)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QCalendarPopup::dateSelectionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCalendarPopup20dateSelectionChangedEv(
    QCalendarPopup *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QCalendarPopup")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "dateSelectionChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "dateSelectionChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QCalendarPopup::hideEvent(QHideEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCalendarPopup9hideEventEP10QHideEvent(
    QCalendarPopup *self,
    QHideEvent *a0) {
  self->hideEvent(a0);
}

//  void QCalendarPopup::mousePressEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCalendarPopup15mousePressEventEP11QMouseEvent(
    QCalendarPopup *self,
    QMouseEvent *e) {
  self->mousePressEvent(e);
}

//  void QCalendarPopup::mouseReleaseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QCalendarPopup17mouseReleaseEventEP11QMouseEvent(
    QCalendarPopup *self,
    QMouseEvent *a0) {
  self->mouseReleaseEvent(a0);
}

//  bool QCalendarPopup::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QCalendarPopup5eventEP6QEvent(
    QCalendarPopup *self,
    QEvent *e) {
  return self->event(e);
}

//  QCalendarWidget *QCalendarPopup::verifyCalendarInstance()
extern "C" Q_DECL_EXPORT
QCalendarWidget *ritual_ZN14QCalendarPopup22verifyCalendarInstanceEv(
    QCalendarPopup *self) {
  return self->verifyCalendarInstance();
}

//  void QCalendarPopup::mousePressEvent(QMouseEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QCalendarPopup15mousePressEventEP11QMouseEvent(
    QCalendarPopup *self,
    QMouseEvent *e) {
  static_cast<OwnQCalendarPopup *>(self)->OwnQCalendarPopup::mousePressEvent(
      e);
}

//  bool QCalendarPopup::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QCalendarPopup5eventEP6QEvent(
    QCalendarPopup *self,
    QEvent *e) {
  return static_cast<OwnQCalendarPopup *>(self)->OwnQCalendarPopup::event(e);
}

#endif  // QT_CONFIG(datetimeedit)
