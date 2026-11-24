//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSGBatchRenderer::RenderNodeElement::RenderNodeElement(QSGRenderNode *rn)
extern "C" Q_DECL_EXPORT
QSGBatchRenderer::RenderNodeElement *ritual_ZN16QSGBatchRenderer17RenderNodeElementC1EP13QSGRenderNode(
    QSGRenderNode *rn) {
  return new QSGBatchRenderer::RenderNodeElement(rn);
}

//  QSGBatchRenderer::RenderNodeElement::~RenderNodeElement()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer17RenderNodeElementD1Ev(
    QSGBatchRenderer::RenderNodeElement *self) {
  delete self;
}
