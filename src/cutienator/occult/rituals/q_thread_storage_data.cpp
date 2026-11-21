//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qthreadstorage.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qthreadstorage.h>

//  QThreadStorageData::~QThreadStorageData()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QThreadStorageDataD1Ev(QThreadStorageData *self) {
  delete self;
}
