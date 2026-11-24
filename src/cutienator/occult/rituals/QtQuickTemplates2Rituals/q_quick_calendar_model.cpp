//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickcalendarmodel_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_calendar)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickcalendarmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickcalendarmodel_p.h"
#include <QtCore/private/qabstractitemmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickcalendarmodel.cpp, line 208, as _ZNK19QQuickCalendarModel9roleNamesEv
inline QHash<int, QByteArray> QQuickCalendarModel::roleNames() const
{
    QHash<int, QByteArray> roles;
    roles[MonthRole] = QByteArrayLiteral("month");
    roles[YearRole] = QByteArrayLiteral("year");
    return roles;
}

//  from ../qtdeclarative/src/quicktemplates/qquickcalendarmodel.cpp, line 216, as _ZN19QQuickCalendarModel10classBeginEv
inline void QQuickCalendarModel::classBegin()
{
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickCalendarModel may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickCalendarModel : QQuickCalendarModel {
  using QQuickCalendarModel::classBegin;
};

//  const QMetaObject *QQuickCalendarModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickCalendarModel10metaObjectEv(
    const QQuickCalendarModel *self) {
  return self->metaObject();
}

//  QHash<int, QByteArray> QQuickCalendarModel::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK19QQuickCalendarModel9roleNamesEv(
    const QQuickCalendarModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  void QQuickCalendarModel::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickCalendarModel10classBeginEv(
    QQuickCalendarModel *self) {
  self->classBegin();
}

//  QQuickCalendarModel as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickCalendarModel_QQmlParserStatus(
    QQuickCalendarModel *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  void QQuickCalendarModel::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickCalendarModel10classBeginEv(
    QQuickCalendarModel *self) {
  static_cast<OwnQQuickCalendarModel *>(self)->OwnQQuickCalendarModel::classBegin();
}

#endif  // QT_CONFIG(quicktemplates2_calendar)
