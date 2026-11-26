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

//  QBrushData::QBrushData(const QBrushData &a0)
extern "C" Q_DECL_EXPORT
QBrushData *ritual_ZN10QBrushDataC1ERKS_(const QBrushData *a0) {
  return new QBrushData(*a0);
}

//  QBrushData::QBrushData(QBrushData &&a0)
extern "C" Q_DECL_EXPORT
QBrushData *ritual_ZN10QBrushDataC1EOS_(QBrushData *a0) {
  return new QBrushData(std::move(*a0));
}

//  QBrushData &QBrushData::operator=(const QBrushData &a0)
extern "C" Q_DECL_EXPORT
QBrushData *ritual_ZN10QBrushDataaSERKS_(
    QBrushData *self,
    const QBrushData *a0) {
  return &(self->operator=(*a0));
}

//  QBrushData &QBrushData::operator=(QBrushData &&a0)
extern "C" Q_DECL_EXPORT
QBrushData *ritual_ZN10QBrushDataaSEOS_(QBrushData *self, QBrushData *a0) {
  return &(self->operator=(std::move(*a0)));
}
