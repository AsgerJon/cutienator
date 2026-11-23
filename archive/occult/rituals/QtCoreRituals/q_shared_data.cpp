//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qshareddata.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qshareddata.h>

//  QSharedData::QSharedData()
extern "C" Q_DECL_EXPORT
QSharedData *ritual_ZN11QSharedDataC1Ev() {
  return new QSharedData();
}

//  QSharedData::QSharedData(const QSharedData &a0)
extern "C" Q_DECL_EXPORT
QSharedData *ritual_ZN11QSharedDataC1ERKS_(const QSharedData *a0) {
  return new QSharedData(*a0);
}

//  QSharedData::~QSharedData()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSharedDataD1Ev(QSharedData *self) {
  delete self;
}
