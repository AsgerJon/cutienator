//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstyleoption.h>

//  QStyleHintReturn::QStyleHintReturn(int version, int type)
extern "C" Q_DECL_EXPORT
QStyleHintReturn *ritual_ZN16QStyleHintReturnC1Eii(int version, int type) {
  return new QStyleHintReturn(version, type);
}

//  QStyleHintReturn::~QStyleHintReturn()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QStyleHintReturnD1Ev(QStyleHintReturn *self) {
  delete self;
}
