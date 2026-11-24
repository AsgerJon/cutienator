//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickdayofweekmodel_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_calendar)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdayofweekmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickdayofweekmodel_p.h"
#include <QtCore/private/qabstractitemmodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickdayofweekmodel.cpp, line 79, as _ZNK20QQuickDayOfWeekModel9roleNamesEv
inline QHash<int, QByteArray> QQuickDayOfWeekModel::roleNames() const
{
    QHash<int, QByteArray> roles;
    roles[DayRole] = QByteArrayLiteral("day");
    roles[LongNameRole] = QByteArrayLiteral("longName");
    roles[ShortNameRole] = QByteArrayLiteral("shortName");
    roles[NarrowNameRole] = QByteArrayLiteral("narrowName");
    return roles;
}

//  from ../qtdeclarative/src/quicktemplates/qquickdayofweekmodel.cpp, line 72, as _ZNK20QQuickDayOfWeekModel8rowCountERK11QModelIndex
inline int QQuickDayOfWeekModel::rowCount(const QModelIndex &parent) const
{
    if (parent.isValid())
        return 0;
    return 7;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickDayOfWeekModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickDayOfWeekModel10metaObjectEv(
    const QQuickDayOfWeekModel *self) {
  return self->metaObject();
}

//  QHash<int, QByteArray> QQuickDayOfWeekModel::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK20QQuickDayOfWeekModel9roleNamesEv(
    const QQuickDayOfWeekModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  int QQuickDayOfWeekModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickDayOfWeekModel8rowCountERK11QModelIndex(
    const QQuickDayOfWeekModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  int QQuickDayOfWeekModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QQuickDayOfWeekModel8rowCountERK11QModelIndex(
    const QQuickDayOfWeekModel *self,
    const QModelIndex *parent) {
  return self->QQuickDayOfWeekModel::rowCount(*parent);
}

#endif  // QT_CONFIG(quicktemplates2_calendar)
