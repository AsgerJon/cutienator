//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qlistwidget_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(listwidget)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qlistwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QListModelLessThan::operator()(QListWidgetItem *i1, QListWidgetItem
//      *i2) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QListModelLessThanclEP15QListWidgetItemS1_(
    const QListModelLessThan *self,
    QListWidgetItem *i1,
    QListWidgetItem *i2) {
  return self->operator()(i1, i2);
}

//  QListModelLessThan::~QListModelLessThan()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QListModelLessThanD1Ev(QListModelLessThan *self) {
  delete self;
}

#endif  // QT_CONFIG(listwidget)
