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

//  QStyleOptionMenuItem &QStyleOptionMenuItem::operator=(const
//      QStyleOptionMenuItem &a0)
extern "C" Q_DECL_EXPORT
QStyleOptionMenuItem *ritual_ZN20QStyleOptionMenuItemaSERKS_(
    QStyleOptionMenuItem *self,
    const QStyleOptionMenuItem *a0) {
  return &(self->operator=(*a0));
}

//  QStyleOptionMenuItem::QStyleOptionMenuItem(int version)
extern "C" Q_DECL_EXPORT
QStyleOptionMenuItem *ritual_ZN20QStyleOptionMenuItemC1Ei(int version) {
  return new QStyleOptionMenuItem(version);
}

//  QStyleOptionMenuItem::~QStyleOptionMenuItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStyleOptionMenuItemD1Ev(QStyleOptionMenuItem *self) {
  delete self;
}
