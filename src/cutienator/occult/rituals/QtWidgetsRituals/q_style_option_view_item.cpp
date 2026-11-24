//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(itemviews)
#include <QtWidgets/qstyleoption.h>

//  QStyleOptionViewItem::QStyleOptionViewItem()
extern "C" Q_DECL_EXPORT
QStyleOptionViewItem *ritual_ZN20QStyleOptionViewItemC1Ev() {
  return new QStyleOptionViewItem();
}

//  QStyleOptionViewItem::QStyleOptionViewItem(const QStyleOptionViewItem
//      &other)
extern "C" Q_DECL_EXPORT
QStyleOptionViewItem *ritual_ZN20QStyleOptionViewItemC1ERKS_(
    const QStyleOptionViewItem *other) {
  return new QStyleOptionViewItem(*other);
}

//  QStyleOptionViewItem::QStyleOptionViewItem(int version)
extern "C" Q_DECL_EXPORT
QStyleOptionViewItem *ritual_ZN20QStyleOptionViewItemC1Ei(int version) {
  return new QStyleOptionViewItem(version);
}

//  QStyleOptionViewItem::~QStyleOptionViewItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStyleOptionViewItemD1Ev(QStyleOptionViewItem *self) {
  delete self;
}

#endif  // QT_CONFIG(itemviews)
