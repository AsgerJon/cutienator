//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtablewidget_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(tablewidget)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qtablewidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QTableModelGreaterThan::operator()(QTableWidgetItem *i1,
//      QTableWidgetItem *i2) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QTableModelGreaterThanclEP16QTableWidgetItemS1_(
    const QTableModelGreaterThan *self,
    QTableWidgetItem *i1,
    QTableWidgetItem *i2) {
  return self->operator()(i1, i2);
}

//  QTableModelGreaterThan::~QTableModelGreaterThan()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QTableModelGreaterThanD1Ev(QTableModelGreaterThan *self) {
  delete self;
}

#endif  // QT_CONFIG(tablewidget)
