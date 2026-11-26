//  Written by hand on 2026-11-25 from
//  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderreflectionmap_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  The header names Q_QUICK3D_PROFILE_ID without including its
//  definition, so the profiler header is included first.
//  The class is exported, has no virtual function and no Q_OBJECT, so it
//  has no Cute class.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qquick3dprofiler_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderreflectionmap_p.h>

//  QSSGRenderReflectionMap::QSSGRenderReflectionMap(const
//      QSSGRenderContextInterface &inContext)
extern "C" Q_DECL_EXPORT
QSSGRenderReflectionMap *ritual_ZN23QSSGRenderReflectionMapC1ERK26QSSGRenderContextInterface(
    const QSSGRenderContextInterface *inContext) {
  return new QSSGRenderReflectionMap(*inContext);
}

//  QSSGRenderReflectionMap::~QSSGRenderReflectionMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSSGRenderReflectionMapD1Ev(
    QSSGRenderReflectionMap *self) {
  delete self;
}

//  void QSSGRenderReflectionMap::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSSGRenderReflectionMap22releaseCachedResourcesEv(
    QSSGRenderReflectionMap *self) {
  self->releaseCachedResources();
}

//  void QSSGRenderReflectionMap::addReflectionMapEntry(qint32 probeIdx,
//      const QSSGRenderReflectionProbe &probe)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSSGRenderReflectionMap21addReflectionMapEntryEiRK25QSSGRenderReflectionProbe(
    QSSGRenderReflectionMap *self,
    qint32 probeIdx,
    const QSSGRenderReflectionProbe *probe) {
  self->addReflectionMapEntry(probeIdx, *probe);
}

//  void QSSGRenderReflectionMap::addTexturedReflectionMapEntry(qint32
//      probeIdx, const QSSGRenderReflectionProbe &probe)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSSGRenderReflectionMap29addTexturedReflectionMapEntryEiRK25QSSGRenderReflectionProbe(
    QSSGRenderReflectionMap *self,
    qint32 probeIdx,
    const QSSGRenderReflectionProbe *probe) {
  self->addTexturedReflectionMapEntry(probeIdx, *probe);
}

//  QSSGReflectionMapEntry *QSSGRenderReflectionMap::reflectionMapEntry(int
//      probeIdx)
extern "C" Q_DECL_EXPORT
QSSGReflectionMapEntry *ritual_ZN23QSSGRenderReflectionMap18reflectionMapEntryEi(
    QSSGRenderReflectionMap *self,
    int probeIdx) {
  return self->reflectionMapEntry(probeIdx);
}

//  qint32 QSSGRenderReflectionMap::reflectionMapEntryCount()
extern "C" Q_DECL_EXPORT
qint32 ritual_ZN23QSSGRenderReflectionMap23reflectionMapEntryCountEv(
    QSSGRenderReflectionMap *self) {
  return self->reflectionMapEntryCount();
}
