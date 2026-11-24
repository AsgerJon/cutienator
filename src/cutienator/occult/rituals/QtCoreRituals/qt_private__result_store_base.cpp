//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qresultstore.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(future)
#include <QtCore/qresultstore.h>

//  QtPrivate::ResultStoreBase::~ResultStoreBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate15ResultStoreBaseD1Ev(
    QtPrivate::ResultStoreBase *self) {
  delete self;
}

//  int QtPrivate::ResultStoreBase::addCanceledResult(int index)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtPrivate15ResultStoreBase17addCanceledResultEi(
    QtPrivate::ResultStoreBase *self,
    int index) {
  return self->addCanceledResult(index);
}

#endif  // QT_CONFIG(future)
