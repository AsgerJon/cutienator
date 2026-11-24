//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QSGBatchRenderer::Rect::operator|=(const Pt &pt)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer4RectoRERKNS_2PtE(
    QSGBatchRenderer::Rect *self,
    const QSGBatchRenderer::Pt *pt) {
  self->operator|=(*pt);
}

//  void QSGBatchRenderer::Rect::operator|=(const Rect &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer4RectoRERKS0_(
    QSGBatchRenderer::Rect *self,
    const QSGBatchRenderer::Rect *r) {
  self->operator|=(*r);
}

//  void QSGBatchRenderer::Rect::set(float left, float top, float right,
//      float bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer4Rect3setEffff(
    QSGBatchRenderer::Rect *self,
    float left,
    float top,
    float right,
    float bottom) {
  self->set(left, top, right, bottom);
}

//  bool QSGBatchRenderer::Rect::intersects(const Rect &r)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSGBatchRenderer4Rect10intersectsERKS0_(
    QSGBatchRenderer::Rect *self,
    const QSGBatchRenderer::Rect *r) {
  return self->intersects(*r);
}

//  bool QSGBatchRenderer::Rect::isOutsideFloatRange() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QSGBatchRenderer4Rect19isOutsideFloatRangeEv(
    const QSGBatchRenderer::Rect *self) {
  return self->isOutsideFloatRange();
}

//  QSGBatchRenderer::Rect::~Rect()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer4RectD1Ev(QSGBatchRenderer::Rect *self) {
  delete self;
}
