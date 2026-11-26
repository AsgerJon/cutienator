//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qtimerinfo_unix_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_UNIX)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qtimerinfo_unix_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QTimerInfo::QTimerInfo(Qt::TimerId timerId, Duration interval,
//      Qt::TimerType type, QObject *obj)
extern "C" Q_DECL_EXPORT
QTimerInfo *ritual_ZN10QTimerInfoC1EN2Qt7TimerIdENSt6chrono8durationIlSt5ratioILl1ELl1000000000EEEENS0_9TimerTypeEP7QObject(
    Qt::TimerId timerId,
    long long interval,
    Qt::TimerType type,
    QObject *obj) {
  return new QTimerInfo(timerId, QTimerInfo::Duration(interval), type, obj);
}

//  QTimerInfo::~QTimerInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTimerInfoD1Ev(QTimerInfo *self) {
  delete self;
}

#endif  // defined(Q_OS_UNIX)
