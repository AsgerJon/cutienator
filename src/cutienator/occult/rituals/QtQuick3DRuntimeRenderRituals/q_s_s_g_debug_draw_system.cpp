//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgdebugdrawsystem_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgdebugdrawsystem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtGui/qcolor.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgbounds3_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendermesh_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGDebugDrawSystem::QSSGDebugDrawSystem()
extern "C" Q_DECL_EXPORT
QSSGDebugDrawSystem *ritual_ZN19QSSGDebugDrawSystemC1Ev() {
  return new QSSGDebugDrawSystem();
}

//  QSSGDebugDrawSystem::~QSSGDebugDrawSystem()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGDebugDrawSystemD1Ev(QSSGDebugDrawSystem *self) {
  delete self;
}

//  bool QSSGDebugDrawSystem::hasContent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QSSGDebugDrawSystem10hasContentEv(
    const QSSGDebugDrawSystem *self) {
  return self->hasContent();
}

//  void QSSGDebugDrawSystem::drawLine(const QVector3D &startPoint, const
//      QVector3D &endPoint, const QColor &color, bool isPersistent)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGDebugDrawSystem8drawLineERK9QVector3DS2_RK6QColorb(
    QSSGDebugDrawSystem *self,
    const QVector3D *startPoint,
    const QVector3D *endPoint,
    const QColor *color,
    bool isPersistent) {
  self->drawLine(*startPoint, *endPoint, *color, isPersistent);
}

//  void QSSGDebugDrawSystem::drawBounds(const QSSGBounds3 &bounds, const
//      QColor &color, bool isPersistent)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGDebugDrawSystem10drawBoundsERK11QSSGBounds3RK6QColorb(
    QSSGDebugDrawSystem *self,
    const QSSGBounds3 *bounds,
    const QColor *color,
    bool isPersistent) {
  self->drawBounds(*bounds, *color, isPersistent);
}

//  void QSSGDebugDrawSystem::drawPoint(const QVector3D &vertex, const QColor
//      &color, bool isPersistent)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGDebugDrawSystem9drawPointERK9QVector3DRK6QColorb(
    QSSGDebugDrawSystem *self,
    const QVector3D *vertex,
    const QColor *color,
    bool isPersistent) {
  self->drawPoint(*vertex, *color, isPersistent);
}

//  void QSSGDebugDrawSystem::prepareGeometry(QSSGRhiContext *rhiCtx,
//      QRhiResourceUpdateBatch *rub)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGDebugDrawSystem15prepareGeometryEP14QSSGRhiContextP23QRhiResourceUpdateBatch(
    QSSGDebugDrawSystem *self,
    QSSGRhiContext *rhiCtx,
    QRhiResourceUpdateBatch *rub) {
  self->prepareGeometry(rhiCtx, rub);
}

//  void QSSGDebugDrawSystem::recordRenderDebugObjects(QSSGRhiContext
//      *rhiCtx, QSSGRhiGraphicsPipelineState *ps, QRhiShaderResourceBindings
//      *srb, QRhiRenderPassDescriptor *rpDesc)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGDebugDrawSystem24recordRenderDebugObjectsEP14QSSGRhiContextP28QSSGRhiGraphicsPipelineStateP26QRhiShaderResourceBindingsP24QRhiRenderPassDescriptor(
    QSSGDebugDrawSystem *self,
    QSSGRhiContext *rhiCtx,
    QSSGRhiGraphicsPipelineState *ps,
    QRhiShaderResourceBindings *srb,
    QRhiRenderPassDescriptor *rpDesc) {
  self->recordRenderDebugObjects(rhiCtx, ps, srb, rpDesc);
}

//  void QSSGDebugDrawSystem::setEnabled(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGDebugDrawSystem10setEnabledEb(
    QSSGDebugDrawSystem *self,
    bool v) {
  self->setEnabled(v);
}

//  bool QSSGDebugDrawSystem::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QSSGDebugDrawSystem9isEnabledEv(
    const QSSGDebugDrawSystem *self) {
  return self->isEnabled();
}

//  void QSSGDebugDrawSystem::generateLine(const LineData &line,
//      QVector<VertexData> &vertexArray, QVector<quint32> &indexArray)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGDebugDrawSystem12generateLineERKNS_8LineDataER5QListINS_10VertexDataEERS3_IjE(
    QSSGDebugDrawSystem *self,
    const QSSGDebugDrawSystem::LineData *line,
    QVector<QSSGDebugDrawSystem::VertexData> *vertexArray,
    QVector<quint32> *indexArray) {
  self->generateLine(*line, *vertexArray, *indexArray);
}

//  void QSSGDebugDrawSystem::generateBox(const BoundsData &bounds,
//      QVector<VertexData> &vertexArray, QVector<quint32> &indexArray)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGDebugDrawSystem11generateBoxERKNS_10BoundsDataER5QListINS_10VertexDataEERS3_IjE(
    QSSGDebugDrawSystem *self,
    const QSSGDebugDrawSystem::BoundsData *bounds,
    QVector<QSSGDebugDrawSystem::VertexData> *vertexArray,
    QVector<quint32> *indexArray) {
  self->generateBox(*bounds, *vertexArray, *indexArray);
}

//  bool QSSGDebugDrawSystem::isEnabled(Mode mode) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QSSGDebugDrawSystem9isEnabledENS_4ModeE(
    const QSSGDebugDrawSystem *self,
    QSSGDebugDrawSystem::Mode mode) {
  return self->isEnabled(mode);
}

//  QColor QSSGDebugDrawSystem::levelOfDetailColor(quint32 lod)
extern "C" Q_DECL_EXPORT
QColor *ritual_ZN19QSSGDebugDrawSystem18levelOfDetailColorEj(quint32 lod) {
  return new QColor(QSSGDebugDrawSystem::levelOfDetailColor(lod));
}

//  void QSSGDebugDrawSystem::debugNormals(QSSGBufferManager &bufferManager,
//      const QSSGModelContext &theModelContext, const QSSGRenderSubset
//      &theSubset, quint32 subsetLevelOfDetail, float lineLength)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGDebugDrawSystem12debugNormalsER17QSSGBufferManagerRK16QSSGModelContextRK16QSSGRenderSubsetjf(
    QSSGDebugDrawSystem *self,
    QSSGBufferManager *bufferManager,
    const QSSGModelContext *theModelContext,
    const QSSGRenderSubset *theSubset,
    quint32 subsetLevelOfDetail,
    float lineLength) {
  self->debugNormals(
      *bufferManager,
      *theModelContext,
      *theSubset,
      subsetLevelOfDetail,
      lineLength);
}
