//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qbrush.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qbrush.h>

//  QBrushData::QBrushData()
extern "C" Q_DECL_EXPORT
QBrushData *ritual_ZN10QBrushDataC1Ev() {
  return new QBrushData();
}

//  QBrushData::~QBrushData()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QBrushDataD1Ev(QBrushData *self) {
  delete self;
}
