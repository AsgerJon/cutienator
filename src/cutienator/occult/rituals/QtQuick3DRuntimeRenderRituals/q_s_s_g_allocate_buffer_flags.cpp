//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercommands_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGAllocateBufferFlags::QSSGAllocateBufferFlags(quint32 inValues)
extern "C" Q_DECL_EXPORT
QSSGAllocateBufferFlags *ritual_ZN23QSSGAllocateBufferFlagsC1Ej(
    quint32 inValues) {
  return new QSSGAllocateBufferFlags(inValues);
}

//  QSSGAllocateBufferFlags::QSSGAllocateBufferFlags()
extern "C" Q_DECL_EXPORT
QSSGAllocateBufferFlags *ritual_ZN23QSSGAllocateBufferFlagsC1Ev() {
  return new QSSGAllocateBufferFlags();
}

//  void QSSGAllocateBufferFlags::setSceneLifetime(bool inValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSSGAllocateBufferFlags16setSceneLifetimeEb(
    QSSGAllocateBufferFlags *self,
    bool inValue) {
  self->setSceneLifetime(inValue);
}

//  bool QSSGAllocateBufferFlags::isSceneLifetime() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QSSGAllocateBufferFlags15isSceneLifetimeEv(
    const QSSGAllocateBufferFlags *self) {
  return self->isSceneLifetime();
}

//  QSSGAllocateBufferFlags::~QSSGAllocateBufferFlags()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSSGAllocateBufferFlagsD1Ev(QSSGAllocateBufferFlags *self) {
  delete self;
}
