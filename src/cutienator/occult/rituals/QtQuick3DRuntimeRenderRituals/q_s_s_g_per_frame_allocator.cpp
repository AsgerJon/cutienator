//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgperframeallocator_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgperframeallocator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGPerFrameAllocator::QSSGPerFrameAllocator()
extern "C" Q_DECL_EXPORT
QSSGPerFrameAllocator *ritual_ZN21QSSGPerFrameAllocatorC1Ev() {
  return new QSSGPerFrameAllocator();
}

//  void QSSGPerFrameAllocator::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGPerFrameAllocator5resetEv(QSSGPerFrameAllocator *self) {
  self->reset();
}

//  QSSGPerFrameAllocator::~QSSGPerFrameAllocator()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGPerFrameAllocatorD1Ev(QSSGPerFrameAllocator *self) {
  delete self;
}
