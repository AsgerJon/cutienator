//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstyleoption.h>

//  QStyleOptionGroupBox::QStyleOptionGroupBox()
extern "C" Q_DECL_EXPORT
QStyleOptionGroupBox *ritual_ZN20QStyleOptionGroupBoxC1Ev() {
  return new QStyleOptionGroupBox();
}

//  QStyleOptionGroupBox::QStyleOptionGroupBox(const QStyleOptionGroupBox
//      &other)
extern "C" Q_DECL_EXPORT
QStyleOptionGroupBox *ritual_ZN20QStyleOptionGroupBoxC1ERKS_(
    const QStyleOptionGroupBox *other) {
  return new QStyleOptionGroupBox(*other);
}

//  QStyleOptionGroupBox::QStyleOptionGroupBox(int version)
extern "C" Q_DECL_EXPORT
QStyleOptionGroupBox *ritual_ZN20QStyleOptionGroupBoxC1Ei(int version) {
  return new QStyleOptionGroupBox(version);
}

//  QStyleOptionGroupBox::~QStyleOptionGroupBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStyleOptionGroupBoxD1Ev(QStyleOptionGroupBox *self) {
  delete self;
}
