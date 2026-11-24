//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/qcanvaspainterfactory.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCanvasPainter/qcanvaspainterfactory.h>

//  QCanvasPainterFactory::QCanvasPainterFactory()
extern "C" Q_DECL_EXPORT
QCanvasPainterFactory *ritual_ZN21QCanvasPainterFactoryC1Ev() {
  return new QCanvasPainterFactory();
}

//  QCanvasPainterFactory::~QCanvasPainterFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasPainterFactoryD1Ev(QCanvasPainterFactory *self) {
  delete self;
}

//  QCanvasPainterFactory *QCanvasPainterFactory::sharedInstance(QRhi *rhi)
extern "C" Q_DECL_EXPORT
QCanvasPainterFactory *ritual_ZN21QCanvasPainterFactory14sharedInstanceEP4QRhi(
    QRhi *rhi) {
  return QCanvasPainterFactory::sharedInstance(rhi);
}

//  bool QCanvasPainterFactory::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QCanvasPainterFactory7isValidEv(
    const QCanvasPainterFactory *self) {
  return self->isValid();
}

//  QCanvasPainter *QCanvasPainterFactory::create(QRhi *rhi)
extern "C" Q_DECL_EXPORT
QCanvasPainter *ritual_ZN21QCanvasPainterFactory6createEP4QRhi(
    QCanvasPainterFactory *self,
    QRhi *rhi) {
  return self->create(rhi);
}

//  void QCanvasPainterFactory::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasPainterFactory7destroyEv(
    QCanvasPainterFactory *self) {
  self->destroy();
}

//  QCanvasPainter *QCanvasPainterFactory::painter()
extern "C" Q_DECL_EXPORT
QCanvasPainter *ritual_ZN21QCanvasPainterFactory7painterEv(
    QCanvasPainterFactory *self) {
  return self->painter();
}

//  QCanvasRhiPaintDriver *QCanvasPainterFactory::paintDriver()
extern "C" Q_DECL_EXPORT
QCanvasRhiPaintDriver *ritual_ZN21QCanvasPainterFactory11paintDriverEv(
    QCanvasPainterFactory *self) {
  return self->paintDriver();
}
