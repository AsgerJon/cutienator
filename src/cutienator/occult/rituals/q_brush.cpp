//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qbrush.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qbrush.h>
#include <QtGui/qcolor.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qimage.h>
#include <QtCore/qvariant.h>
#include <QtGui/qtransform.h>

//  QBrush::QBrush()
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZN6QBrushC1Ev() {
  return new QBrush();
}

//  QBrush::QBrush(Qt::BrushStyle bs)
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZN6QBrushC1EN2Qt10BrushStyleE(Qt::BrushStyle bs) {
  return new QBrush(bs);
}

//  QBrush::QBrush(const QColor &color, Qt::BrushStyle bs)
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZN6QBrushC1ERK6QColorN2Qt10BrushStyleE(
    const QColor *color,
    Qt::BrushStyle bs) {
  return new QBrush(*color, bs);
}

//  QBrush::QBrush(Qt::GlobalColor color, Qt::BrushStyle bs)
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZN6QBrushC1EN2Qt11GlobalColorENS0_10BrushStyleE(
    Qt::GlobalColor color,
    Qt::BrushStyle bs) {
  return new QBrush(color, bs);
}

//  QBrush::QBrush(const QColor &color, const QPixmap &pixmap)
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZN6QBrushC1ERK6QColorRK7QPixmap(
    const QColor *color,
    const QPixmap *pixmap) {
  return new QBrush(*color, *pixmap);
}

//  QBrush::QBrush(Qt::GlobalColor color, const QPixmap &pixmap)
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZN6QBrushC1EN2Qt11GlobalColorERK7QPixmap(
    Qt::GlobalColor color,
    const QPixmap *pixmap) {
  return new QBrush(color, *pixmap);
}

//  QBrush::QBrush(const QPixmap &pixmap)
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZN6QBrushC1ERK7QPixmap(const QPixmap *pixmap) {
  return new QBrush(*pixmap);
}

//  QBrush::QBrush(const QImage &image)
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZN6QBrushC1ERK6QImage(const QImage *image) {
  return new QBrush(*image);
}

//  QBrush::QBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZN6QBrushC1ERKS_(const QBrush *brush) {
  return new QBrush(*brush);
}

//  QBrush::QBrush(const QGradient &gradient)
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZN6QBrushC1ERK9QGradient(const QGradient *gradient) {
  return new QBrush(*gradient);
}

//  QBrush::~QBrush()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QBrushD1Ev(QBrush *self) {
  delete self;
}

//  QVariant QBrush::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK6QBrushcv8QVariantEv(const QBrush *self) {
  return new QVariant(self->operator QVariant());
}

//  Qt::BrushStyle QBrush::style() const
extern "C" Q_DECL_EXPORT
Qt::BrushStyle ritual_ZNK6QBrush5styleEv(const QBrush *self) {
  return self->style();
}

//  void QBrush::setStyle(Qt::BrushStyle a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QBrush8setStyleEN2Qt10BrushStyleE(
    QBrush *self,
    Qt::BrushStyle a0) {
  self->setStyle(a0);
}

//  QTransform QBrush::transform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK6QBrush9transformEv(const QBrush *self) {
  return new QTransform(self->transform());
}

//  void QBrush::setTransform(const QTransform &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QBrush12setTransformERK10QTransform(
    QBrush *self,
    const QTransform *a0) {
  self->setTransform(*a0);
}

//  QPixmap QBrush::texture() const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK6QBrush7textureEv(const QBrush *self) {
  return new QPixmap(self->texture());
}

//  void QBrush::setTexture(const QPixmap &pixmap)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QBrush10setTextureERK7QPixmap(
    QBrush *self,
    const QPixmap *pixmap) {
  self->setTexture(*pixmap);
}

//  QImage QBrush::textureImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK6QBrush12textureImageEv(const QBrush *self) {
  return new QImage(self->textureImage());
}

//  void QBrush::setTextureImage(const QImage &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QBrush15setTextureImageERK6QImage(
    QBrush *self,
    const QImage *image) {
  self->setTextureImage(*image);
}

//  const QColor &QBrush::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK6QBrush5colorEv(const QBrush *self) {
  return new QColor(self->color());
}

//  void QBrush::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QBrush8setColorERK6QColor(QBrush *self, const QColor *color) {
  self->setColor(*color);
}

//  void QBrush::setColor(Qt::GlobalColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QBrush8setColorEN2Qt11GlobalColorE(
    QBrush *self,
    Qt::GlobalColor color) {
  self->setColor(color);
}

//  const QGradient *QBrush::gradient() const
extern "C" Q_DECL_EXPORT
const QGradient *ritual_ZNK6QBrush8gradientEv(const QBrush *self) {
  return self->gradient();
}

//  bool QBrush::isOpaque() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QBrush8isOpaqueEv(const QBrush *self) {
  return self->isOpaque();
}

//  bool QBrush::operator==(const QBrush &b) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QBrusheqERKS_(const QBrush *self, const QBrush *b) {
  return self->operator==(*b);
}

//  bool QBrush::operator!=(const QBrush &b) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QBrushneERKS_(const QBrush *self, const QBrush *b) {
  return self->operator!=(*b);
}

//  bool operator==(const QBrush &lhs, const QColor &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK6QBrushRK6QColor(const QBrush *lhs, const QColor *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QBrush &lhs, const QColor &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK6QBrushRK6QColor(const QBrush *lhs, const QColor *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(const QColor &lhs, const QBrush &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK6QColorRK6QBrush(const QColor *lhs, const QBrush *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QColor &lhs, const QBrush &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK6QColorRK6QBrush(const QColor *lhs, const QBrush *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool QBrush::isDetached() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QBrush10isDetachedEv(const QBrush *self) {
  return self->isDetached();
}
