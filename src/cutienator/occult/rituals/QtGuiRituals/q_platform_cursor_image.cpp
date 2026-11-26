//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformcursor.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformcursor.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/qimage.h>

//  QPlatformCursorImage::QPlatformCursorImage(const uchar *data, const uchar
//      *mask, int width, int height, int hotX, int hotY)
extern "C" Q_DECL_EXPORT
QPlatformCursorImage *ritual_ZN20QPlatformCursorImageC1EPKhS1_iiii(
    const uchar *data,
    const uchar *mask,
    int width,
    int height,
    int hotX,
    int hotY) {
  return new QPlatformCursorImage(data, mask, width, height, hotX, hotY);
}

//  QImage *QPlatformCursorImage::image()
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN20QPlatformCursorImage5imageEv(QPlatformCursorImage *self) {
  return self->image();
}

//  QPoint QPlatformCursorImage::hotspot() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK20QPlatformCursorImage7hotspotEv(
    const QPlatformCursorImage *self) {
  return new QPoint(self->hotspot());
}

//  void QPlatformCursorImage::set(const uchar *data, const uchar *mask, int
//      width, int height, int hotX, int hotY)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformCursorImage3setEPKhS1_iiii(
    QPlatformCursorImage *self,
    const uchar *data,
    const uchar *mask,
    int width,
    int height,
    int hotX,
    int hotY) {
  self->set(data, mask, width, height, hotX, hotY);
}

//  void QPlatformCursorImage::set(const QImage &image, int hx, int hy)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformCursorImage3setERK6QImageii(
    QPlatformCursorImage *self,
    const QImage *image,
    int hx,
    int hy) {
  self->set(*image, hx, hy);
}

//  void QPlatformCursorImage::set(Qt::CursorShape a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformCursorImage3setEN2Qt11CursorShapeE(
    QPlatformCursorImage *self,
    Qt::CursorShape a0) {
  self->set(a0);
}

//  void QPlatformCursorImage::createSystemCursor(int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformCursorImage18createSystemCursorEi(int id) {
  QPlatformCursorImage::createSystemCursor(id);
}

//  QPlatformCursorImage::~QPlatformCursorImage()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformCursorImageD1Ev(QPlatformCursorImage *self) {
  delete self;
}
