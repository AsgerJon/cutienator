//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qcolortransform.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qcolortransform.h>
#include <QtGui/qrgba64.h>
#include <QtGui/qcolor.h>

//  QColorTransform::QColorTransform()
extern "C" Q_DECL_EXPORT
QColorTransform *ritual_ZN15QColorTransformC1Ev() {
  return new QColorTransform();
}

//  QColorTransform::~QColorTransform()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QColorTransformD1Ev(QColorTransform *self) {
  delete self;
}

//  QColorTransform::QColorTransform(const QColorTransform &colorTransform)
extern "C" Q_DECL_EXPORT
QColorTransform *ritual_ZN15QColorTransformC1ERKS_(
    const QColorTransform *colorTransform) {
  return new QColorTransform(*colorTransform);
}

//  bool QColorTransform::isIdentity() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QColorTransform10isIdentityEv(const QColorTransform *self) {
  return self->isIdentity();
}

//  QRgb QColorTransform::map(QRgb argb) const
extern "C" Q_DECL_EXPORT
QRgb ritual_ZNK15QColorTransform3mapEj(
    const QColorTransform *self,
    QRgb argb) {
  return self->map(argb);
}

//  QRgba64 QColorTransform::map(QRgba64 rgba64) const
extern "C" Q_DECL_EXPORT
QRgba64 *ritual_ZNK15QColorTransform3mapE7QRgba64(
    const QColorTransform *self,
    const QRgba64 *rgba64) {
  return new QRgba64(self->map(*rgba64));
}

//  QColor QColorTransform::map(const QColor &color) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK15QColorTransform3mapERK6QColor(
    const QColorTransform *self,
    const QColor *color) {
  return new QColor(self->map(*color));
}
