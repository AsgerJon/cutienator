//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qlistwidget_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(listwidget)
#if QT_CONFIG(listwidget)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qlistwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QListModelGreaterThan::operator()(QListWidgetItem *i1,
//      QListWidgetItem *i2) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QListModelGreaterThanclEP15QListWidgetItemS1_(
    const QListModelGreaterThan *self,
    QListWidgetItem *i1,
    QListWidgetItem *i2) {
  return self->operator()(i1, i2);
}

//  QListModelGreaterThan::~QListModelGreaterThan()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QListModelGreaterThanD1Ev(QListModelGreaterThan *self) {
  delete self;
}

#endif  // QT_CONFIG(listwidget)
#endif  // QT_CONFIG(listwidget)
