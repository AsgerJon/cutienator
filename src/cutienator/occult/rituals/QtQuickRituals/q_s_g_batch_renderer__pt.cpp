//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qmatrix4x4.h>

//  void QSGBatchRenderer::Pt::map(const QMatrix4x4 &mat)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer2Pt3mapERK10QMatrix4x4(
    QSGBatchRenderer::Pt *self,
    const QMatrix4x4 *mat) {
  self->map(*mat);
}

//  void QSGBatchRenderer::Pt::set(float nx, float ny)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer2Pt3setEff(
    QSGBatchRenderer::Pt *self,
    float nx,
    float ny) {
  self->set(nx, ny);
}

//  QSGBatchRenderer::Pt::~Pt()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer2PtD1Ev(QSGBatchRenderer::Pt *self) {
  delete self;
}
