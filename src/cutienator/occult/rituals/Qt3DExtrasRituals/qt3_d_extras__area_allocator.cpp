//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/areaallocator_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/areaallocator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>

//  bool Qt3DExtras::AreaAllocator::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DExtras13AreaAllocator7isEmptyEv(
    const Qt3DExtras::AreaAllocator *self) {
  return self->isEmpty();
}

//  QSize Qt3DExtras::AreaAllocator::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10Qt3DExtras13AreaAllocator4sizeEv(
    const Qt3DExtras::AreaAllocator *self) {
  return new QSize(self->size());
}
