//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qhash.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qhash.h>

//  QHashDummyValue::QHashDummyValue()
extern "C" Q_DECL_EXPORT
QHashDummyValue *ritual_ZN15QHashDummyValueC1Ev() {
  return new QHashDummyValue();
}

//  bool operator==(QHashDummyValue a0, QHashDummyValue a1)
extern "C" Q_DECL_EXPORT
bool ritual_Zeq15QHashDummyValueS_(
    const QHashDummyValue *a0,
    const QHashDummyValue *a1) {
  return operator==(*a0, *a1);
}

//  bool operator!=(QHashDummyValue a0, QHashDummyValue a1)
extern "C" Q_DECL_EXPORT
bool ritual_Zne15QHashDummyValueS_(
    const QHashDummyValue *a0,
    const QHashDummyValue *a1) {
  return operator!=(*a0, *a1);
}

//  QHashDummyValue::~QHashDummyValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHashDummyValueD1Ev(QHashDummyValue *self) {
  delete self;
}
