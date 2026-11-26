//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qthreadstorage.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(thread)
#include <QtCore/qthreadstorage.h>

//  QThreadStorageData::QThreadStorageData(void (*)(void *) func)
extern "C" Q_DECL_EXPORT
QThreadStorageData *ritual_ZN18QThreadStorageDataC1EPFvPvE(void *func) {
  return new QThreadStorageData(reinterpret_cast<void (*)(void *)>(func));
}

//  QThreadStorageData::~QThreadStorageData()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QThreadStorageDataD1Ev(QThreadStorageData *self) {
  delete self;
}

//  void **QThreadStorageData::get() const
extern "C" Q_DECL_EXPORT
void **ritual_ZNK18QThreadStorageData3getEv(const QThreadStorageData *self) {
  return self->get();
}

//  void **QThreadStorageData::set(void *p)
extern "C" Q_DECL_EXPORT
void **ritual_ZN18QThreadStorageData3setEPv(
    QThreadStorageData *self,
    void *p) {
  return self->set(p);
}

#endif  // QT_CONFIG(thread)
