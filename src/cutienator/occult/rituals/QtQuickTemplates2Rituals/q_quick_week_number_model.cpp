//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickweeknumbermodel_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_calendar)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickweeknumbermodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickweeknumbermodel_p.h"
#include <QtCore/private/qabstractitemmodel_p.h>
#include <QtCore/qdatetime.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickweeknumbermodel.cpp, line 141, as _ZNK21QQuickWeekNumberModel9roleNamesEv
inline QHash<int, QByteArray> QQuickWeekNumberModel::roleNames() const
{
    QHash<int, QByteArray> roles;
    roles[WeekNumberRole] = QByteArrayLiteral("weekNumber");
    return roles;
}

//  from ../qtdeclarative/src/quicktemplates/qquickweeknumbermodel.cpp, line 124, as _ZNK21QQuickWeekNumberModel4dataERK11QModelIndexi
inline QVariant QQuickWeekNumberModel::data(const QModelIndex &index, int role) const
{
    if (role == WeekNumberRole) {
        int weekNumber = weekNumberAt(index.row());
        if (weekNumber != -1)
            return weekNumber;
    }
    return QVariant();
}

//  from ../qtdeclarative/src/quicktemplates/qquickweeknumbermodel.cpp, line 134, as _ZNK21QQuickWeekNumberModel8rowCountERK11QModelIndex
inline int QQuickWeekNumberModel::rowCount(const QModelIndex &parent) const
{
    if (parent.isValid())
        return 0;
    return 6;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickWeekNumberModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickWeekNumberModel10metaObjectEv(
    const QQuickWeekNumberModel *self) {
  return self->metaObject();
}

//  QHash<int, QByteArray> QQuickWeekNumberModel::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK21QQuickWeekNumberModel9roleNamesEv(
    const QQuickWeekNumberModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  QVariant QQuickWeekNumberModel::data(const QModelIndex &index, int role)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK21QQuickWeekNumberModel4dataERK11QModelIndexi(
    const QQuickWeekNumberModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  int QQuickWeekNumberModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickWeekNumberModel8rowCountERK11QModelIndex(
    const QQuickWeekNumberModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  int QQuickWeekNumberModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QQuickWeekNumberModel8rowCountERK11QModelIndex(
    const QQuickWeekNumberModel *self,
    const QModelIndex *parent) {
  return self->QQuickWeekNumberModel::rowCount(*parent);
}

#endif  // QT_CONFIG(quicktemplates2_calendar)
