//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qbitmap.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qbitmap.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qsize.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtGui/qimage.h>
#include <QtGui/qtransform.h>

//  QBitmap::QBitmap()
extern "C" Q_DECL_EXPORT
QBitmap *ritual_ZN7QBitmapC1Ev() {
  return new QBitmap();
}

//  QBitmap::QBitmap(const QPixmap &a0)
extern "C" Q_DECL_EXPORT
QBitmap *ritual_ZN7QBitmapC1ERK7QPixmap(const QPixmap *a0) {
  return new QBitmap(*a0);
}

//  QBitmap::QBitmap(int w, int h)
extern "C" Q_DECL_EXPORT
QBitmap *ritual_ZN7QBitmapC1Eii(int w, int h) {
  return new QBitmap(w, h);
}

//  QBitmap::QBitmap(const QSize &a0)
extern "C" Q_DECL_EXPORT
QBitmap *ritual_ZN7QBitmapC1ERK5QSize(const QSize *a0) {
  return new QBitmap(*a0);
}

//  QBitmap::QBitmap(const QString &fileName, const char *format)
extern "C" Q_DECL_EXPORT
QBitmap *ritual_ZN7QBitmapC1ERK7QStringPKc(
    const QString *fileName,
    const char *format) {
  return new QBitmap(*fileName, format);
}

//  QBitmap::~QBitmap()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBitmapD1Ev(QBitmap *self) {
  delete self;
}

//  QVariant QBitmap::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK7QBitmapcv8QVariantEv(const QBitmap *self) {
  return new QVariant(self->operator QVariant());
}

//  void QBitmap::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBitmap5clearEv(QBitmap *self) {
  self->clear();
}

//  QBitmap QBitmap::fromImage(const QImage &image, Qt::ImageConversionFlags
//      flags)
extern "C" Q_DECL_EXPORT
QBitmap *ritual_ZN7QBitmap9fromImageERK6QImage6QFlagsIN2Qt19ImageConversionFlagEE(
    const QImage *image,
    int flags) {
  return new QBitmap(
      QBitmap::fromImage(
          *image,
          QFlags<Qt::ImageConversionFlag>::fromInt(flags)));
}

//  QBitmap QBitmap::fromPixmap(const QPixmap &pixmap)
extern "C" Q_DECL_EXPORT
QBitmap *ritual_ZN7QBitmap10fromPixmapERK7QPixmap(const QPixmap *pixmap) {
  return new QBitmap(QBitmap::fromPixmap(*pixmap));
}

//  QBitmap QBitmap::transformed(const QTransform &matrix) const
extern "C" Q_DECL_EXPORT
QBitmap *ritual_ZNK7QBitmap11transformedERK10QTransform(
    const QBitmap *self,
    const QTransform *matrix) {
  return new QBitmap(self->transformed(*matrix));
}
