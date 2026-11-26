//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3drenderstats_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3drenderstats_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QQuick3DRenderStats::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuick3DRenderStats10metaObjectEv(
    const QQuick3DRenderStats *self) {
  return self->metaObject();
}

//  void *QQuick3DRenderStats::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QQuick3DRenderStats11qt_metacastEPKc(
    QQuick3DRenderStats *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DRenderStats::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuick3DRenderStats11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DRenderStats *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DRenderStats::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQuick3DRenderStats2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DRenderStats::tr(s, c, n));
}

//  void QQuick3DRenderStats::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats24qt_qmlMarker_uncreatableEv(
    QQuick3DRenderStats *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuick3DRenderStats::QQuick3DRenderStats(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DRenderStats *ritual_ZN19QQuick3DRenderStatsC1EP7QObject(
    QObject *parent) {
  return new QQuick3DRenderStats(parent);
}

//  int QQuick3DRenderStats::fps() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuick3DRenderStats3fpsEv(const QQuick3DRenderStats *self) {
  return self->fps();
}

//  float QQuick3DRenderStats::frameTime() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QQuick3DRenderStats9frameTimeEv(
    const QQuick3DRenderStats *self) {
  return self->frameTime();
}

//  float QQuick3DRenderStats::renderTime() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QQuick3DRenderStats10renderTimeEv(
    const QQuick3DRenderStats *self) {
  return self->renderTime();
}

//  float QQuick3DRenderStats::renderPrepareTime() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QQuick3DRenderStats17renderPrepareTimeEv(
    const QQuick3DRenderStats *self) {
  return self->renderPrepareTime();
}

//  float QQuick3DRenderStats::syncTime() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QQuick3DRenderStats8syncTimeEv(
    const QQuick3DRenderStats *self) {
  return self->syncTime();
}

//  float QQuick3DRenderStats::maxFrameTime() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QQuick3DRenderStats12maxFrameTimeEv(
    const QQuick3DRenderStats *self) {
  return self->maxFrameTime();
}

//  void QQuick3DRenderStats::startSync()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats9startSyncEv(QQuick3DRenderStats *self) {
  self->startSync();
}

//  void QQuick3DRenderStats::endSync(bool dump)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats7endSyncEb(
    QQuick3DRenderStats *self,
    bool dump) {
  self->endSync(dump);
}

//  void QQuick3DRenderStats::startRender()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats11startRenderEv(
    QQuick3DRenderStats *self) {
  self->startRender();
}

//  void QQuick3DRenderStats::startRenderPrepare()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats18startRenderPrepareEv(
    QQuick3DRenderStats *self) {
  self->startRenderPrepare();
}

//  void QQuick3DRenderStats::endRenderPrepare()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats16endRenderPrepareEv(
    QQuick3DRenderStats *self) {
  self->endRenderPrepare();
}

//  void QQuick3DRenderStats::endRender(bool dump)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats9endRenderEb(
    QQuick3DRenderStats *self,
    bool dump) {
  self->endRender(dump);
}

//  void QQuick3DRenderStats::setRhiContext(QSSGRhiContext *ctx,
//      QSSGRenderLayer *layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats13setRhiContextEP14QSSGRhiContextP15QSSGRenderLayer(
    QQuick3DRenderStats *self,
    QSSGRhiContext *ctx,
    QSSGRenderLayer *layer) {
  self->setRhiContext(ctx, layer);
}

//  bool QQuick3DRenderStats::extendedDataCollectionEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuick3DRenderStats29extendedDataCollectionEnabledEv(
    const QQuick3DRenderStats *self) {
  return self->extendedDataCollectionEnabled();
}

//  void QQuick3DRenderStats::setExtendedDataCollectionEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats32setExtendedDataCollectionEnabledEb(
    QQuick3DRenderStats *self,
    bool enable) {
  self->setExtendedDataCollectionEnabled(enable);
}

//  quint64 QQuick3DRenderStats::drawCallCount() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK19QQuick3DRenderStats13drawCallCountEv(
    const QQuick3DRenderStats *self) {
  return self->drawCallCount();
}

//  quint64 QQuick3DRenderStats::drawVertexCount() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK19QQuick3DRenderStats15drawVertexCountEv(
    const QQuick3DRenderStats *self) {
  return self->drawVertexCount();
}

//  quint64 QQuick3DRenderStats::imageDataSize() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK19QQuick3DRenderStats13imageDataSizeEv(
    const QQuick3DRenderStats *self) {
  return self->imageDataSize();
}

//  quint64 QQuick3DRenderStats::meshDataSize() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK19QQuick3DRenderStats12meshDataSizeEv(
    const QQuick3DRenderStats *self) {
  return self->meshDataSize();
}

//  int QQuick3DRenderStats::renderPassCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuick3DRenderStats15renderPassCountEv(
    const QQuick3DRenderStats *self) {
  return self->renderPassCount();
}

//  QString QQuick3DRenderStats::renderPassDetails() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQuick3DRenderStats17renderPassDetailsEv(
    const QQuick3DRenderStats *self) {
  return new QString(self->renderPassDetails());
}

//  QString QQuick3DRenderStats::textureDetails() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQuick3DRenderStats14textureDetailsEv(
    const QQuick3DRenderStats *self) {
  return new QString(self->textureDetails());
}

//  QString QQuick3DRenderStats::meshDetails() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQuick3DRenderStats11meshDetailsEv(
    const QQuick3DRenderStats *self) {
  return new QString(self->meshDetails());
}

//  int QQuick3DRenderStats::pipelineCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QQuick3DRenderStats13pipelineCountEv(
    const QQuick3DRenderStats *self) {
  return self->pipelineCount();
}

//  qint64 QQuick3DRenderStats::materialGenerationTime() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK19QQuick3DRenderStats22materialGenerationTimeEv(
    const QQuick3DRenderStats *self) {
  return self->materialGenerationTime();
}

//  qint64 QQuick3DRenderStats::effectGenerationTime() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK19QQuick3DRenderStats20effectGenerationTimeEv(
    const QQuick3DRenderStats *self) {
  return self->effectGenerationTime();
}

//  qint64 QQuick3DRenderStats::pipelineCreationTime() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK19QQuick3DRenderStats20pipelineCreationTimeEv(
    const QQuick3DRenderStats *self) {
  return self->pipelineCreationTime();
}

//  quint32 QQuick3DRenderStats::vmemAllocCount() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK19QQuick3DRenderStats14vmemAllocCountEv(
    const QQuick3DRenderStats *self) {
  return self->vmemAllocCount();
}

//  quint64 QQuick3DRenderStats::vmemUsedBytes() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK19QQuick3DRenderStats13vmemUsedBytesEv(
    const QQuick3DRenderStats *self) {
  return self->vmemUsedBytes();
}

//  QString QQuick3DRenderStats::graphicsApiName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQuick3DRenderStats15graphicsApiNameEv(
    const QQuick3DRenderStats *self) {
  return new QString(self->graphicsApiName());
}

//  float QQuick3DRenderStats::lastCompletedGpuTime() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QQuick3DRenderStats20lastCompletedGpuTimeEv(
    const QQuick3DRenderStats *self) {
  return self->lastCompletedGpuTime();
}

//  void QQuick3DRenderStats::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats22releaseCachedResourcesEv(
    QQuick3DRenderStats *self) {
  self->releaseCachedResources();
}

//  void QQuick3DRenderStats::setWindow(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats9setWindowEP12QQuickWindow(
    QQuick3DRenderStats *self,
    QQuickWindow *window) {
  self->setWindow(window);
}

//  void QQuick3DRenderStats::fpsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats10fpsChangedEv(
    QQuick3DRenderStats *self) {
  self->fpsChanged();
}

//  void QQuick3DRenderStats::frameTimeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats16frameTimeChangedEv(
    QQuick3DRenderStats *self) {
  self->frameTimeChanged();
}

//  void QQuick3DRenderStats::renderTimeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats17renderTimeChangedEv(
    QQuick3DRenderStats *self) {
  self->renderTimeChanged();
}

//  void QQuick3DRenderStats::syncTimeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats15syncTimeChangedEv(
    QQuick3DRenderStats *self) {
  self->syncTimeChanged();
}

//  void QQuick3DRenderStats::maxFrameTimeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats19maxFrameTimeChangedEv(
    QQuick3DRenderStats *self) {
  self->maxFrameTimeChanged();
}

//  void QQuick3DRenderStats::extendedDataCollectionEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats36extendedDataCollectionEnabledChangedEv(
    QQuick3DRenderStats *self) {
  self->extendedDataCollectionEnabledChanged();
}

//  void QQuick3DRenderStats::drawCallCountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats20drawCallCountChangedEv(
    QQuick3DRenderStats *self) {
  self->drawCallCountChanged();
}

//  void QQuick3DRenderStats::drawVertexCountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats22drawVertexCountChangedEv(
    QQuick3DRenderStats *self) {
  self->drawVertexCountChanged();
}

//  void QQuick3DRenderStats::imageDataSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats20imageDataSizeChangedEv(
    QQuick3DRenderStats *self) {
  self->imageDataSizeChanged();
}

//  void QQuick3DRenderStats::meshDataSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats19meshDataSizeChangedEv(
    QQuick3DRenderStats *self) {
  self->meshDataSizeChanged();
}

//  void QQuick3DRenderStats::renderPassCountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats22renderPassCountChangedEv(
    QQuick3DRenderStats *self) {
  self->renderPassCountChanged();
}

//  void QQuick3DRenderStats::renderPassDetailsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats24renderPassDetailsChangedEv(
    QQuick3DRenderStats *self) {
  self->renderPassDetailsChanged();
}

//  void QQuick3DRenderStats::textureDetailsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats21textureDetailsChangedEv(
    QQuick3DRenderStats *self) {
  self->textureDetailsChanged();
}

//  void QQuick3DRenderStats::meshDetailsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats18meshDetailsChangedEv(
    QQuick3DRenderStats *self) {
  self->meshDetailsChanged();
}

//  void QQuick3DRenderStats::pipelineCountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats20pipelineCountChangedEv(
    QQuick3DRenderStats *self) {
  self->pipelineCountChanged();
}

//  void QQuick3DRenderStats::materialGenerationTimeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats29materialGenerationTimeChangedEv(
    QQuick3DRenderStats *self) {
  self->materialGenerationTimeChanged();
}

//  void QQuick3DRenderStats::effectGenerationTimeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats27effectGenerationTimeChangedEv(
    QQuick3DRenderStats *self) {
  self->effectGenerationTimeChanged();
}

//  void QQuick3DRenderStats::pipelineCreationTimeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats27pipelineCreationTimeChangedEv(
    QQuick3DRenderStats *self) {
  self->pipelineCreationTimeChanged();
}

//  void QQuick3DRenderStats::vmemAllocCountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats21vmemAllocCountChangedEv(
    QQuick3DRenderStats *self) {
  self->vmemAllocCountChanged();
}

//  void QQuick3DRenderStats::vmemUsedBytesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats20vmemUsedBytesChangedEv(
    QQuick3DRenderStats *self) {
  self->vmemUsedBytesChanged();
}

//  void QQuick3DRenderStats::graphicsApiNameChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats22graphicsApiNameChangedEv(
    QQuick3DRenderStats *self) {
  self->graphicsApiNameChanged();
}

//  void QQuick3DRenderStats::lastCompletedGpuTimeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats27lastCompletedGpuTimeChangedEv(
    QQuick3DRenderStats *self) {
  self->lastCompletedGpuTimeChanged();
}

//  void QQuick3DRenderStats::onFrameSwapped()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats14onFrameSwappedEv(
    QQuick3DRenderStats *self) {
  self->onFrameSwapped();
}

//  float QQuick3DRenderStats::timestamp() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QQuick3DRenderStats9timestampEv(
    const QQuick3DRenderStats *self) {
  return self->timestamp();
}

//  void QQuick3DRenderStats::processRhiContextStats()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats22processRhiContextStatsEv(
    QQuick3DRenderStats *self) {
  self->processRhiContextStats();
}

//  void QQuick3DRenderStats::notifyRhiContextStats()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuick3DRenderStats21notifyRhiContextStatsEv(
    QQuick3DRenderStats *self) {
  self->notifyRhiContextStats();
}
