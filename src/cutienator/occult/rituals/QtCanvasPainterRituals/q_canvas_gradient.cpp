//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/qcanvasgradient.h, Qt 6.12.0. Changes made here are lost.
#include <QtCanvasPainter/qcanvasgradient.h>
#include <QtGui/qcolor.h>
#include <QtCanvasPainter/qcanvasimage.h>
#include <QtCanvasPainter/qcanvasbrush.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>

//  QCanvasBrush::BrushType QCanvasGradient::type() const
extern "C" Q_DECL_EXPORT
QCanvasBrush::BrushType ritual_ZNK15QCanvasGradient4typeEv(
    const QCanvasGradient *self) {
  return self->type();
}

//  QColor QCanvasGradient::startColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK15QCanvasGradient10startColorEv(
    const QCanvasGradient *self) {
  return new QColor(self->startColor());
}

//  void QCanvasGradient::setStartColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCanvasGradient13setStartColorE6QColor(
    QCanvasGradient *self,
    const QColor *color) {
  self->setStartColor(*color);
}

//  QColor QCanvasGradient::endColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK15QCanvasGradient8endColorEv(const QCanvasGradient *self) {
  return new QColor(self->endColor());
}

//  void QCanvasGradient::setEndColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCanvasGradient11setEndColorE6QColor(
    QCanvasGradient *self,
    const QColor *color) {
  self->setEndColor(*color);
}

//  void QCanvasGradient::setColorAt(qreal position, QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCanvasGradient10setColorAtEd6QColor(
    QCanvasGradient *self,
    qreal position,
    const QColor *color) {
  self->setColorAt(position, *color);
}

//  void QCanvasGradient::setStops(const QCanvasGradientStops &stops)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCanvasGradient8setStopsERK5QListI19QCanvasGradientStopE(
    QCanvasGradient *self,
    const QList<QCanvasGradientStop> *stops) {
  self->setStops(*stops);
}

//  QCanvasGradientStops QCanvasGradient::stops() const
extern "C" Q_DECL_EXPORT
QList<QCanvasGradientStop> *ritual_ZNK15QCanvasGradient5stopsEv(
    const QCanvasGradient *self) {
  return new QList<QCanvasGradientStop>(self->stops());
}

//  void QCanvasGradient::setImage(const QCanvasImage &image, int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCanvasGradient8setImageERK12QCanvasImagei(
    QCanvasGradient *self,
    const QCanvasImage *image,
    int index) {
  self->setImage(*image, index);
}

//  void QCanvasGradient::addColorStop(qreal position, QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCanvasGradient12addColorStopEd6QColor(
    QCanvasGradient *self,
    qreal position,
    const QColor *color) {
  self->addColorStop(position, *color);
}

//  QCanvasBrush QCanvasGradient::operator QCanvasBrush() const
extern "C" Q_DECL_EXPORT
QCanvasBrush *ritual_ZNKR15QCanvasGradientcv12QCanvasBrushEv(
    const QCanvasGradient *self) {
  return new QCanvasBrush(self->operator QCanvasBrush());
}

//  QVariant QCanvasGradient::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QCanvasGradientcv8QVariantEv(
    const QCanvasGradient *self) {
  return new QVariant(self->operator QVariant());
}

//  QCanvasGradient::QCanvasGradient(QCanvasBrush::BrushType type)
extern "C" Q_DECL_EXPORT
QCanvasGradient *ritual_ZN15QCanvasGradientC1EN12QCanvasBrush9BrushTypeE(
    QCanvasBrush::BrushType type) {
  return new QCanvasGradient(type);
}

//  QCanvasGradient::QCanvasGradient(const QCanvasBrush &brush)
extern "C" Q_DECL_EXPORT
QCanvasGradient *ritual_ZN15QCanvasGradientC1ERK12QCanvasBrush(
    const QCanvasBrush *brush) {
  return new QCanvasGradient(*brush);
}

//  QCanvasGradient::~QCanvasGradient()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCanvasGradientD1Ev(QCanvasGradient *self) {
  delete self;
}
