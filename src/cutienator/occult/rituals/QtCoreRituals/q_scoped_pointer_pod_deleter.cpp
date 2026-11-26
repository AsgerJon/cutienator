//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qscopedpointer.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qscopedpointer.h>

//  void QScopedPointerPodDeleter::cleanup(void *pointer)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScopedPointerPodDeleter7cleanupEPv(void *pointer) {
  QScopedPointerPodDeleter::cleanup(pointer);
}

//  void QScopedPointerPodDeleter::operator()(void *pointer) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK24QScopedPointerPodDeleterclEPv(
    const QScopedPointerPodDeleter *self,
    void *pointer) {
  self->operator()(pointer);
}

//  QScopedPointerPodDeleter::~QScopedPointerPodDeleter()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScopedPointerPodDeleterD1Ev(
    QScopedPointerPodDeleter *self) {
  delete self;
}
