//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSGBatchRenderer::DrawSet::DrawSet(int v, int z, int i)
extern "C" Q_DECL_EXPORT
QSGBatchRenderer::DrawSet *ritual_ZN16QSGBatchRenderer7DrawSetC1Eiii(
    int v,
    int z,
    int i) {
  return new QSGBatchRenderer::DrawSet(v, z, i);
}

//  QSGBatchRenderer::DrawSet::DrawSet()
extern "C" Q_DECL_EXPORT
QSGBatchRenderer::DrawSet *ritual_ZN16QSGBatchRenderer7DrawSetC1Ev() {
  return new QSGBatchRenderer::DrawSet();
}

//  QSGBatchRenderer::DrawSet::~DrawSet()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer7DrawSetD1Ev(
    QSGBatchRenderer::DrawSet *self) {
  delete self;
}
