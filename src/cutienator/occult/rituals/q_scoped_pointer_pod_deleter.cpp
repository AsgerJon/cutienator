//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qscopedpointer.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qscopedpointer.h>

//  QScopedPointerPodDeleter::~QScopedPointerPodDeleter()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScopedPointerPodDeleterD1Ev(
    QScopedPointerPodDeleter *self) {
  delete self;
}
