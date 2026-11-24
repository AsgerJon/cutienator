//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtablewidget_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(tablewidget)
#if QT_CONFIG(tablewidget)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qtablewidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QTableWidgetItemPrivate::QTableWidgetItemPrivate(QTableWidgetItem *item)
extern "C" Q_DECL_EXPORT
QTableWidgetItemPrivate *ritual_ZN23QTableWidgetItemPrivateC1EP16QTableWidgetItem(
    QTableWidgetItem *item) {
  return new QTableWidgetItemPrivate(item);
}

//  QTableWidgetItemPrivate::~QTableWidgetItemPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QTableWidgetItemPrivateD1Ev(QTableWidgetItemPrivate *self) {
  delete self;
}

#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(tablewidget)
