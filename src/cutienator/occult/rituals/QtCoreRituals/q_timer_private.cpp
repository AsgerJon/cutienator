//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qtimer_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qtimer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qtimer.h>
#include <QtCore/private/qtimer_p.h>
#include <QtCore/private/qsingleshottimer_p.h>
#include <QtCore/qabstracteventdispatcher.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/private/qcoreapplication_p.h>
#include <QtCore/qdeadlinetimer.h>
#include <QtCore/private/qmetaobject_p.h>
#include <QtCore/private/qobject_p.h>
#include <QtCore/private/qproperty_p.h>
#include <QtCore/qthread.h>
#include <QtCore/q26numeric.h> // for q26::staturate_cast
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/kernel/qtimer.cpp, line 25, as _ZN13QTimerPrivateD1Ev
inline QTimerPrivate::~QTimerPrivate()
    = default;
//  -----------------------------------------------------------------------

//  QTimerPrivate::QTimerPrivate(QTimer *qq)
extern "C" Q_DECL_EXPORT
QTimerPrivate *ritual_ZN13QTimerPrivateC1EP6QTimer(QTimer *qq) {
  return new QTimerPrivate(qq);
}

//  QTimerPrivate::~QTimerPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTimerPrivateD1Ev(QTimerPrivate *self) {
  delete self;
}

//  void QTimerPrivate::setIntervalDuration(std::chrono::nanoseconds nsec)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTimerPrivate19setIntervalDurationENSt6chrono8durationIlSt5ratioILl1ELl1000000000EEEE(
    QTimerPrivate *self,
    long long nsec) {
  self->setIntervalDuration(std::chrono::nanoseconds(nsec));
}

//  void QTimerPrivate::setInterval(int msec)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTimerPrivate11setIntervalEi(QTimerPrivate *self, int msec) {
  self->setInterval(msec);
}

//  bool QTimerPrivate::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QTimerPrivate8isActiveEv(const QTimerPrivate *self) {
  return self->isActive();
}

//  size_t QTimerPrivate::_qt_property_inter_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN13QTimerPrivate25_qt_property_inter_offsetEv() {
  return QTimerPrivate::_qt_property_inter_offset();
}

//  size_t QTimerPrivate::_qt_property_intervalDuration_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN13QTimerPrivate36_qt_property_intervalDuration_offsetEv() {
  return QTimerPrivate::_qt_property_intervalDuration_offset();
}

//  size_t QTimerPrivate::_qt_property_single_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN13QTimerPrivate26_qt_property_single_offsetEv() {
  return QTimerPrivate::_qt_property_single_offset();
}

//  size_t QTimerPrivate::_qt_property_type_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN13QTimerPrivate24_qt_property_type_offsetEv() {
  return QTimerPrivate::_qt_property_type_offset();
}

//  size_t QTimerPrivate::_qt_property_isActiveData_offset()
extern "C" Q_DECL_EXPORT
size_t ritual_ZN13QTimerPrivate32_qt_property_isActiveData_offsetEv() {
  return QTimerPrivate::_qt_property_isActiveData_offset();
}
