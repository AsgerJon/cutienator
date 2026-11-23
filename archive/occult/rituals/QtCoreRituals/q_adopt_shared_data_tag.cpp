//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qshareddata.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qshareddata.h>

//  QAdoptSharedDataTag::QAdoptSharedDataTag()
extern "C" Q_DECL_EXPORT
QAdoptSharedDataTag *ritual_ZN19QAdoptSharedDataTagC1Ev() {
  return new QAdoptSharedDataTag();
}

//  QAdoptSharedDataTag::~QAdoptSharedDataTag()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAdoptSharedDataTagD1Ev(QAdoptSharedDataTag *self) {
  delete self;
}
