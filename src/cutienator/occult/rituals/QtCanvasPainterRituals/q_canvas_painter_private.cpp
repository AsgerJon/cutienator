//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvaspainter_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/QtCanvasPainter>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvaspainter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCanvasPainter/qcanvasimage.h>
#include <QtCanvasPainter/qcanvasoffscreencanvas.h>
#include <QtCore/qrect.h>
#include <QtGui/qtransform.h>
#include <QtGui/qfont.h>
#include <QtCore/qstring.h>
#include <QtCanvasPainter/qcanvasboxshadow.h>
#include <QtCore/qlist.h>

//  QCanvasPainterPrivate::QCanvasPainterPrivate()
extern "C" Q_DECL_EXPORT
QCanvasPainterPrivate *ritual_ZN21QCanvasPainterPrivateC1Ev() {
  return new QCanvasPainterPrivate();
}

//  QCanvasPainterPrivate::~QCanvasPainterPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasPainterPrivateD1Ev(QCanvasPainterPrivate *self) {
  delete self;
}

//  QCPainterEngine *QCanvasPainterPrivate::engine() const
extern "C" Q_DECL_EXPORT
QCPainterEngine *ritual_ZNK21QCanvasPainterPrivate6engineEv(
    const QCanvasPainterPrivate *self) {
  return self->engine();
}

//  QCanvasPainterPrivate *QCanvasPainterPrivate::get(QCanvasPainter
//      *painter)
extern "C" Q_DECL_EXPORT
QCanvasPainterPrivate *ritual_ZN21QCanvasPainterPrivate3getEP14QCanvasPainter(
    QCanvasPainter *painter) {
  return QCanvasPainterPrivate::get(painter);
}

//  const QCanvasPainterPrivate *QCanvasPainterPrivate::get(const
//      QCanvasPainter *painter)
extern "C" Q_DECL_EXPORT
const QCanvasPainterPrivate *ritual_ZN21QCanvasPainterPrivate3getEPK14QCanvasPainter(
    const QCanvasPainter *painter) {
  return QCanvasPainterPrivate::get(painter);
}

//  qint64 QCanvasPainterPrivate::generateImageKey(const QImage &image,
//      QCanvasPainter::ImageFlags flags) const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK21QCanvasPainterPrivate16generateImageKeyERK6QImage6QFlagsIN14QCanvasPainter9ImageFlagEE(
    const QCanvasPainterPrivate *self,
    const QImage *image,
    int flags) {
  return self->generateImageKey(
      *image,
      QFlags<QCanvasPainter::ImageFlag>::fromInt(flags));
}

//  QCanvasImage QCanvasPainterPrivate::getQCanvasImage(const QImage &image,
//      QCanvasPainter::ImageFlags flags, qint64 imageKey)
extern "C" Q_DECL_EXPORT
QCanvasImage *ritual_ZN21QCanvasPainterPrivate15getQCanvasImageERK6QImage6QFlagsIN14QCanvasPainter9ImageFlagEEx(
    QCanvasPainterPrivate *self,
    const QImage *image,
    int flags,
    qint64 imageKey) {
  return new QCanvasImage(
      self->getQCanvasImage(
          *image,
          QFlags<QCanvasPainter::ImageFlag>::fromInt(flags),
          imageKey));
}

//  QCanvasImage QCanvasPainterPrivate::getQCanvasImage(QRhiTexture *texture,
//      QCanvasPainter::ImageFlags flags)
extern "C" Q_DECL_EXPORT
QCanvasImage *ritual_ZN21QCanvasPainterPrivate15getQCanvasImageEP11QRhiTexture6QFlagsIN14QCanvasPainter9ImageFlagEE(
    QCanvasPainterPrivate *self,
    QRhiTexture *texture,
    int flags) {
  return new QCanvasImage(
      self->getQCanvasImage(
          texture,
          QFlags<QCanvasPainter::ImageFlag>::fromInt(flags)));
}

//  QCanvasImage QCanvasPainterPrivate::getQCanvasImage(const
//      QCanvasOffscreenCanvas &canvas, QCanvasPainter::ImageFlags flags)
extern "C" Q_DECL_EXPORT
QCanvasImage *ritual_ZN21QCanvasPainterPrivate15getQCanvasImageERK22QCanvasOffscreenCanvas6QFlagsIN14QCanvasPainter9ImageFlagEE(
    QCanvasPainterPrivate *self,
    const QCanvasOffscreenCanvas *canvas,
    int flags) {
  return new QCanvasImage(
      self->getQCanvasImage(
          *canvas,
          QFlags<QCanvasPainter::ImageFlag>::fromInt(flags)));
}

//  void QCanvasPainterPrivate::handleCleanupTextures()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasPainterPrivate21handleCleanupTexturesEv(
    QCanvasPainterPrivate *self) {
  self->handleCleanupTextures();
}

//  void QCanvasPainterPrivate::clearTextureCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasPainterPrivate17clearTextureCacheEv(
    QCanvasPainterPrivate *self) {
  self->clearTextureCache();
}

//  void QCanvasPainterPrivate::markTextureIdUsed(int imageId)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasPainterPrivate17markTextureIdUsedEi(
    QCanvasPainterPrivate *self,
    int imageId) {
  self->markTextureIdUsed(imageId);
}

//  void QCanvasPainterPrivate::setStencilClip(const QList<QRectF> &rects)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasPainterPrivate14setStencilClipERK5QListI6QRectFE(
    QCanvasPainterPrivate *self,
    const QList<QRectF> *rects) {
  self->setStencilClip(*rects);
}

//  void QCanvasPainterPrivate::setStencilClip(const QVectorPath &clipPath)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasPainterPrivate14setStencilClipERK11QVectorPath(
    QCanvasPainterPrivate *self,
    const QVectorPath *clipPath) {
  self->setStencilClip(*clipPath);
}

//  void QCanvasPainterPrivate::setBrushTransform(const QTransform
//      &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasPainterPrivate17setBrushTransformERK10QTransform(
    QCanvasPainterPrivate *self,
    const QTransform *transform) {
  self->setBrushTransform(*transform);
}

//  void QCanvasPainterPrivate::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasPainterPrivate7setFontERK5QFont(
    QCanvasPainterPrivate *self,
    const QFont *font) {
  self->setFont(*font);
}

//  void QCanvasPainterPrivate::fillText(const QString &text, qreal x, qreal
//      y, qreal maxWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasPainterPrivate8fillTextERK7QStringddd(
    QCanvasPainterPrivate *self,
    const QString *text,
    qreal x,
    qreal y,
    qreal maxWidth) {
  self->fillText(*text, x, y, maxWidth);
}

//  void QCanvasPainterPrivate::fillText(const QString &text, const QRectF
//      &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasPainterPrivate8fillTextERK7QStringRK6QRectF(
    QCanvasPainterPrivate *self,
    const QString *text,
    const QRectF *rect) {
  self->fillText(*text, *rect);
}

//  void QCanvasPainterPrivate::fillShapedText(QFontEngine *fontEngine, const
//      quint32 *glyphIndexes, const QFixedPoint *glyphPositions, int
//      glyphCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasPainterPrivate14fillShapedTextEP11QFontEnginePKjPK11QFixedPointi(
    QCanvasPainterPrivate *self,
    QFontEngine *fontEngine,
    const quint32 *glyphIndexes,
    const QFixedPoint *glyphPositions,
    int glyphCount) {
  self->fillShapedText(fontEngine, glyphIndexes, glyphPositions, glyphCount);
}

//  QRectF QCanvasPainterPrivate::textBoundingBox(const QString &text, qreal
//      x, qreal y, qreal maxWidth) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK21QCanvasPainterPrivate15textBoundingBoxERK7QStringddd(
    const QCanvasPainterPrivate *self,
    const QString *text,
    qreal x,
    qreal y,
    qreal maxWidth) {
  return new QRectF(self->textBoundingBox(*text, x, y, maxWidth));
}

//  QRectF QCanvasPainterPrivate::textBoundingBox(const QString &text, const
//      QRectF &rect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK21QCanvasPainterPrivate15textBoundingBoxERK7QStringRK6QRectF(
    const QCanvasPainterPrivate *self,
    const QString *text,
    const QRectF *rect) {
  return new QRectF(self->textBoundingBox(*text, *rect));
}

//  void QCanvasPainterPrivate::drawBoxShadow(QCanvasPainter *painter, const
//      QCanvasBoxShadow &shadow)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasPainterPrivate13drawBoxShadowEP14QCanvasPainterRK16QCanvasBoxShadow(
    QCanvasPainterPrivate *self,
    QCanvasPainter *painter,
    const QCanvasBoxShadow *shadow) {
  self->drawBoxShadow(painter, *shadow);
}

//  void QCanvasPainterPrivate::setAntialiasingEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QCanvasPainterPrivate22setAntialiasingEnabledEb(
    QCanvasPainterPrivate *self,
    bool enabled) {
  self->setAntialiasingEnabled(enabled);
}
