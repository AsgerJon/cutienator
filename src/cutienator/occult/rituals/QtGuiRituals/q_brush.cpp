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

//  QBrush &QBrush::operator=(const QBrush &brush)
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZN6QBrushaSERKS_(QBrush *self, const QBrush *brush) {
  return &(self->operator=(*brush));
}

//  QBrush &QBrush::operator=(QBrush &&other)
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZN6QBrushaSEOS_(QBrush *self, QBrush *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QBrush::swap(QBrush &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QBrush4swapERS_(QBrush *self, QBrush *other) {
  self->swap(*other);
}

//  QBrush &QBrush::operator=(Qt::BrushStyle style)
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZN6QBrushaSEN2Qt10BrushStyleE(
    QBrush *self,
    Qt::BrushStyle style) {
  return &(self->operator=(style));
}

//  QBrush &QBrush::operator=(QColor color)
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZN6QBrushaSE6QColor(QBrush *self, const QColor *color) {
  return &(self->operator=(*color));
}

//  QBrush &QBrush::operator=(Qt::GlobalColor color)
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZN6QBrushaSEN2Qt11GlobalColorE(
    QBrush *self,
    Qt::GlobalColor color) {
  return &(self->operator=(color));
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

//  bool QBrush::doCompareEqualColor(QColor rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QBrush19doCompareEqualColorE6QColor(
    const QBrush *self,
    const QColor *rhs) {
  return self->doCompareEqualColor(*rhs);
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

//  bool operator==(const QBrush &lhs, const Qt::GlobalColor &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK6QBrushRKN2Qt11GlobalColorE(
    const QBrush *lhs,
    const Qt::GlobalColor *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QBrush &lhs, const Qt::GlobalColor &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK6QBrushRKN2Qt11GlobalColorE(
    const QBrush *lhs,
    const Qt::GlobalColor *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(const Qt::GlobalColor &lhs, const QBrush &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN2Qt11GlobalColorERK6QBrush(
    const Qt::GlobalColor *lhs,
    const QBrush *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const Qt::GlobalColor &lhs, const QBrush &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN2Qt11GlobalColorERK6QBrush(
    const Qt::GlobalColor *lhs,
    const QBrush *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool QBrush::doCompareEqualStyle(Qt::BrushStyle rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QBrush19doCompareEqualStyleEN2Qt10BrushStyleE(
    const QBrush *self,
    Qt::BrushStyle rhs) {
  return self->doCompareEqualStyle(rhs);
}

//  bool operator==(const QBrush &lhs, const Qt::BrushStyle &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK6QBrushRKN2Qt10BrushStyleE(
    const QBrush *lhs,
    const Qt::BrushStyle *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QBrush &lhs, const Qt::BrushStyle &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK6QBrushRKN2Qt10BrushStyleE(
    const QBrush *lhs,
    const Qt::BrushStyle *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(const Qt::BrushStyle &lhs, const QBrush &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN2Qt10BrushStyleERK6QBrush(
    const Qt::BrushStyle *lhs,
    const QBrush *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const Qt::BrushStyle &lhs, const QBrush &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN2Qt10BrushStyleERK6QBrush(
    const Qt::BrushStyle *lhs,
    const QBrush *rhs) {
  return operator!=(*lhs, *rhs);
}

//  void QBrush::detach(Qt::BrushStyle newStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QBrush6detachEN2Qt10BrushStyleE(
    QBrush *self,
    Qt::BrushStyle newStyle) {
  self->detach(newStyle);
}

//  void QBrush::init(const QColor &color, Qt::BrushStyle bs)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QBrush4initERK6QColorN2Qt10BrushStyleE(
    QBrush *self,
    const QColor *color,
    Qt::BrushStyle bs) {
  self->init(*color, bs);
}

//  bool QBrush::isDetached() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QBrush10isDetachedEv(const QBrush *self) {
  return self->isDetached();
}

//  DataPtr &QBrush::data_ptr()
extern "C" Q_DECL_EXPORT
QBrush::DataPtr *ritual_ZN6QBrush8data_ptrEv(QBrush *self) {
  return &(self->data_ptr());
}
