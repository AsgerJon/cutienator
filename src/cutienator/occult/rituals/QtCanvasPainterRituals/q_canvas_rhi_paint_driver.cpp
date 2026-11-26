//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/qcanvasrhipaintdriver.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCanvasPainter/qcanvasrhipaintdriver.h>
#include <QtGui/qcolor.h>
#include <QtCore/qsize.h>
#include <QtGui/qmatrix4x4.h>
#include <QtCanvasPainter/qcanvasoffscreencanvas.h>

//  QCanvasRhiPaintDriver::QCanvasRhiPaintDriver()
extern "C" Q_DECL_EXPORT
QCanvasRhiPaintDriver *ritual_ZN21QCanvasRhiPaintDriverC1Ev() {
  return new QCanvasRhiPaintDriver();
}

//  QCanvasRhiPaintDriver::~QCanvasRhiPaintDriver()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasRhiPaintDriverD1Ev(QCanvasRhiPaintDriver *self) {
  delete self;
}

//  void QCanvasRhiPaintDriver::resetForNewFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasRhiPaintDriver16resetForNewFrameEv(
    QCanvasRhiPaintDriver *self) {
  self->resetForNewFrame();
}

//  void QCanvasRhiPaintDriver::beginPaint(QRhiCommandBuffer *cb,
//      QRhiRenderTarget *rt, QColor fillColor, QSize logicalSize, qreal dpr,
//      BeginPaintFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasRhiPaintDriver10beginPaintEP17QRhiCommandBufferP16QRhiRenderTarget6QColor5QSized6QFlagsINS_14BeginPaintFlagEE(
    QCanvasRhiPaintDriver *self,
    QRhiCommandBuffer *cb,
    QRhiRenderTarget *rt,
    const QColor *fillColor,
    const QSize *logicalSize,
    qreal dpr,
    int flags) {
  self->beginPaint(
      cb,
      rt,
      *fillColor,
      *logicalSize,
      dpr,
      QFlags<QCanvasRhiPaintDriver::BeginPaintFlag>::fromInt(flags));
}

//  void QCanvasRhiPaintDriver::beginPaint(QRhiCommandBuffer *cb,
//      QRhiRenderTarget *rt, const QMatrix4x4 &matrix, BeginPaintFlags
//      flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasRhiPaintDriver10beginPaintEP17QRhiCommandBufferP16QRhiRenderTargetRK10QMatrix4x46QFlagsINS_14BeginPaintFlagEE(
    QCanvasRhiPaintDriver *self,
    QRhiCommandBuffer *cb,
    QRhiRenderTarget *rt,
    const QMatrix4x4 *matrix,
    int flags) {
  self->beginPaint(
      cb,
      rt,
      *matrix,
      QFlags<QCanvasRhiPaintDriver::BeginPaintFlag>::fromInt(flags));
}

//  void QCanvasRhiPaintDriver::beginPaint(QCanvasOffscreenCanvas &canvas,
//      QRhiCommandBuffer *cb, BeginPaintFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasRhiPaintDriver10beginPaintER22QCanvasOffscreenCanvasP17QRhiCommandBuffer6QFlagsINS_14BeginPaintFlagEE(
    QCanvasRhiPaintDriver *self,
    QCanvasOffscreenCanvas *canvas,
    QRhiCommandBuffer *cb,
    int flags) {
  self->beginPaint(
      *canvas,
      cb,
      QFlags<QCanvasRhiPaintDriver::BeginPaintFlag>::fromInt(flags));
}

//  void QCanvasRhiPaintDriver::endPaint(EndPaintFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasRhiPaintDriver8endPaintE6QFlagsINS_12EndPaintFlagEE(
    QCanvasRhiPaintDriver *self,
    int flags) {
  self->endPaint(
      QFlags<QCanvasRhiPaintDriver::EndPaintFlag>::fromInt(flags));
}

//  void QCanvasRhiPaintDriver::renderPaint()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasRhiPaintDriver11renderPaintEv(
    QCanvasRhiPaintDriver *self) {
  self->renderPaint();
}

//  void QCanvasRhiPaintDriver::grabCanvasImpl(const QCanvasOffscreenCanvas
//      &canvas, const QObject *context, QtPrivate::QSlotObjectBase *slotObj)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasRhiPaintDriver14grabCanvasImplERK22QCanvasOffscreenCanvasPK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QCanvasRhiPaintDriver *self,
    const QCanvasOffscreenCanvas *canvas,
    const QObject *context,
    QtPrivate::QSlotObjectBase *slotObj) {
  self->grabCanvasImpl(*canvas, context, slotObj);
}
