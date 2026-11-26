//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstyleoption.h>

//  QStyleOptionMenuItemV2::QStyleOptionMenuItemV2()
extern "C" Q_DECL_EXPORT
QStyleOptionMenuItemV2 *ritual_ZN22QStyleOptionMenuItemV2C1Ev() {
  return new QStyleOptionMenuItemV2();
}

//  QStyleOptionMenuItemV2::QStyleOptionMenuItemV2(const
//      QStyleOptionMenuItemV2 &other)
extern "C" Q_DECL_EXPORT
QStyleOptionMenuItemV2 *ritual_ZN22QStyleOptionMenuItemV2C1ERKS_(
    const QStyleOptionMenuItemV2 *other) {
  return new QStyleOptionMenuItemV2(*other);
}

//  QStyleOptionMenuItemV2 &QStyleOptionMenuItemV2::operator=(const
//      QStyleOptionMenuItemV2 &a0)
extern "C" Q_DECL_EXPORT
QStyleOptionMenuItemV2 *ritual_ZN22QStyleOptionMenuItemV2aSERKS_(
    QStyleOptionMenuItemV2 *self,
    const QStyleOptionMenuItemV2 *a0) {
  return &(self->operator=(*a0));
}

//  QStyleOptionMenuItemV2::QStyleOptionMenuItemV2(int version)
extern "C" Q_DECL_EXPORT
QStyleOptionMenuItemV2 *ritual_ZN22QStyleOptionMenuItemV2C1Ei(int version) {
  return new QStyleOptionMenuItemV2(version);
}

//  QStyleOptionMenuItemV2::~QStyleOptionMenuItemV2()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QStyleOptionMenuItemV2D1Ev(QStyleOptionMenuItemV2 *self) {
  delete self;
}
