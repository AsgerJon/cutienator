//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgmaterialshader.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsgmaterialshader.h>
#include <QtGui/qmatrix4x4.h>
#include <QtCore/qrect.h>

//  DirtyStates QSGMaterialShader::RenderState::dirtyStates() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QSGMaterialShader11RenderState11dirtyStatesEv(
    const QSGMaterialShader::RenderState *self) {
  return static_cast<int>(self->dirtyStates().toInt());
}

//  bool QSGMaterialShader::RenderState::isMatrixDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSGMaterialShader11RenderState13isMatrixDirtyEv(
    const QSGMaterialShader::RenderState *self) {
  return self->isMatrixDirty();
}

//  bool QSGMaterialShader::RenderState::isOpacityDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSGMaterialShader11RenderState14isOpacityDirtyEv(
    const QSGMaterialShader::RenderState *self) {
  return self->isOpacityDirty();
}

//  float QSGMaterialShader::RenderState::opacity() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK17QSGMaterialShader11RenderState7opacityEv(
    const QSGMaterialShader::RenderState *self) {
  return self->opacity();
}

//  QMatrix4x4 QSGMaterialShader::RenderState::combinedMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK17QSGMaterialShader11RenderState14combinedMatrixEv(
    const QSGMaterialShader::RenderState *self) {
  return new QMatrix4x4(self->combinedMatrix());
}

//  QMatrix4x4 QSGMaterialShader::RenderState::combinedMatrix(qsizetype
//      index) const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK17QSGMaterialShader11RenderState14combinedMatrixEx(
    const QSGMaterialShader::RenderState *self,
    qsizetype index) {
  return new QMatrix4x4(self->combinedMatrix(index));
}

//  QMatrix4x4 QSGMaterialShader::RenderState::modelViewMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK17QSGMaterialShader11RenderState15modelViewMatrixEv(
    const QSGMaterialShader::RenderState *self) {
  return new QMatrix4x4(self->modelViewMatrix());
}

//  QMatrix4x4 QSGMaterialShader::RenderState::projectionMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK17QSGMaterialShader11RenderState16projectionMatrixEv(
    const QSGMaterialShader::RenderState *self) {
  return new QMatrix4x4(self->projectionMatrix());
}

//  QMatrix4x4 QSGMaterialShader::RenderState::projectionMatrix(qsizetype
//      index) const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK17QSGMaterialShader11RenderState16projectionMatrixEx(
    const QSGMaterialShader::RenderState *self,
    qsizetype index) {
  return new QMatrix4x4(self->projectionMatrix(index));
}

//  qsizetype QSGMaterialShader::RenderState::projectionMatrixCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK17QSGMaterialShader11RenderState21projectionMatrixCountEv(
    const QSGMaterialShader::RenderState *self) {
  return self->projectionMatrixCount();
}

//  QRect QSGMaterialShader::RenderState::viewportRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK17QSGMaterialShader11RenderState12viewportRectEv(
    const QSGMaterialShader::RenderState *self) {
  return new QRect(self->viewportRect());
}

//  QRect QSGMaterialShader::RenderState::deviceRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK17QSGMaterialShader11RenderState10deviceRectEv(
    const QSGMaterialShader::RenderState *self) {
  return new QRect(self->deviceRect());
}

//  float QSGMaterialShader::RenderState::determinant() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK17QSGMaterialShader11RenderState11determinantEv(
    const QSGMaterialShader::RenderState *self) {
  return self->determinant();
}

//  float QSGMaterialShader::RenderState::devicePixelRatio() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK17QSGMaterialShader11RenderState16devicePixelRatioEv(
    const QSGMaterialShader::RenderState *self) {
  return self->devicePixelRatio();
}

//  QByteArray *QSGMaterialShader::RenderState::uniformData()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN17QSGMaterialShader11RenderState11uniformDataEv(
    QSGMaterialShader::RenderState *self) {
  return self->uniformData();
}

//  QRhiResourceUpdateBatch
//      *QSGMaterialShader::RenderState::resourceUpdateBatch()
extern "C" Q_DECL_EXPORT
QRhiResourceUpdateBatch *ritual_ZN17QSGMaterialShader11RenderState19resourceUpdateBatchEv(
    QSGMaterialShader::RenderState *self) {
  return self->resourceUpdateBatch();
}

//  QRhi *QSGMaterialShader::RenderState::rhi()
extern "C" Q_DECL_EXPORT
QRhi *ritual_ZN17QSGMaterialShader11RenderState3rhiEv(
    QSGMaterialShader::RenderState *self) {
  return self->rhi();
}

//  QSGMaterialShader::RenderState::~RenderState()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSGMaterialShader11RenderStateD1Ev(
    QSGMaterialShader::RenderState *self) {
  delete self;
}
