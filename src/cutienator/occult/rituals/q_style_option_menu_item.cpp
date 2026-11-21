//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstyleoption.h>

//  QStyleOptionMenuItem::QStyleOptionMenuItem()
extern "C" Q_DECL_EXPORT
QStyleOptionMenuItem *ritual_ZN20QStyleOptionMenuItemC1Ev() {
  return new QStyleOptionMenuItem();
}

//  QStyleOptionMenuItem::QStyleOptionMenuItem(const QStyleOptionMenuItem
//      &other)
extern "C" Q_DECL_EXPORT
QStyleOptionMenuItem *ritual_ZN20QStyleOptionMenuItemC1ERKS_(
    const QStyleOptionMenuItem *other) {
  return new QStyleOptionMenuItem(*other);
}

//  QStyleOptionMenuItem::~QStyleOptionMenuItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStyleOptionMenuItemD1Ev(QStyleOptionMenuItem *self) {
  delete self;
}
