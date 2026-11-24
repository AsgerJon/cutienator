//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qwidgetitemdata_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(itemviews)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qwidgetitemdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>

//  QWidgetItemData::QWidgetItemData()
extern "C" Q_DECL_EXPORT
QWidgetItemData *ritual_ZN15QWidgetItemDataC1Ev() {
  return new QWidgetItemData();
}

//  QWidgetItemData::QWidgetItemData(int r, const QVariant &v)
extern "C" Q_DECL_EXPORT
QWidgetItemData *ritual_ZN15QWidgetItemDataC1EiRK8QVariant(
    int r,
    const QVariant *v) {
  return new QWidgetItemData(r, *v);
}

//  bool QWidgetItemData::operator==(const QWidgetItemData &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QWidgetItemDataeqERKS_(
    const QWidgetItemData *self,
    const QWidgetItemData *other) {
  return self->operator==(*other);
}

//  QWidgetItemData::~QWidgetItemData()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWidgetItemDataD1Ev(QWidgetItemData *self) {
  delete self;
}

#endif  // QT_CONFIG(itemviews)
