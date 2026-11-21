//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qhash.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qhash.h>

//  QHashDummyValue::QHashDummyValue()
extern "C" Q_DECL_EXPORT
QHashDummyValue *ritual_ZN15QHashDummyValueC1Ev() {
  return new QHashDummyValue();
}

//  QHashDummyValue::~QHashDummyValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHashDummyValueD1Ev(QHashDummyValue *self) {
  delete self;
}
