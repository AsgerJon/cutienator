//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstyleoption.h>

//  QStyleOptionComboBox::QStyleOptionComboBox()
extern "C" Q_DECL_EXPORT
QStyleOptionComboBox *ritual_ZN20QStyleOptionComboBoxC1Ev() {
  return new QStyleOptionComboBox();
}

//  QStyleOptionComboBox::QStyleOptionComboBox(const QStyleOptionComboBox
//      &other)
extern "C" Q_DECL_EXPORT
QStyleOptionComboBox *ritual_ZN20QStyleOptionComboBoxC1ERKS_(
    const QStyleOptionComboBox *other) {
  return new QStyleOptionComboBox(*other);
}

//  QStyleOptionComboBox::~QStyleOptionComboBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QStyleOptionComboBoxD1Ev(QStyleOptionComboBox *self) {
  delete self;
}
