//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmonthmodel_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_calendar)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmonthmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qquickmonthmodel_p.h>
#include <QtCore/private/qabstractitemmodel_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qtimezone.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickmonthmodel.cpp, line 200, as _ZNK16QQuickMonthModel9roleNamesEv
inline QHash<int, QByteArray> QQuickMonthModel::roleNames() const
{
    QHash<int, QByteArray> roles;
    roles[DateRole] = QByteArrayLiteral("date");
    roles[DayRole] = QByteArrayLiteral("day");
    roles[TodayRole] = QByteArrayLiteral("today");
    roles[WeekNumberRole] = QByteArrayLiteral("weekNumber");
    roles[MonthRole] = QByteArrayLiteral("month");
    roles[YearRole] = QByteArrayLiteral("year");
    return roles;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickMonthModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuickMonthModel10metaObjectEv(
    const QQuickMonthModel *self) {
  return self->metaObject();
}

//  QHash<int, QByteArray> QQuickMonthModel::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK16QQuickMonthModel9roleNamesEv(
    const QQuickMonthModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

#endif  // QT_CONFIG(quicktemplates2_calendar)
