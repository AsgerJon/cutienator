//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qwindowsnativeimage_p.h, Qt 6.12.0, as the
//  Qt of Windows installs it. Kept as it is when the generator runs
//  again.
//  A handle of Windows, as 'HDC', is passed as an address.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtGui/6.12.0/QtGui/private/qwindowsnativeimage_p.h>
#include <QtGui/qimage.h>

//  QWindowsNativeImage::QWindowsNativeImage(int width, int height,
//      QImage::Format format)
extern "C" Q_DECL_EXPORT
QWindowsNativeImage *ritual_ZN19QWindowsNativeImageC1EiiN6QImage6FormatE(
    int width,
    int height,
    QImage::Format format) {
  return new QWindowsNativeImage(width, height, format);
}

//  QWindowsNativeImage::~QWindowsNativeImage()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWindowsNativeImageD1Ev(QWindowsNativeImage *self) {
  delete self;
}

//  int QWindowsNativeImage::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QWindowsNativeImage5widthEv(
    const QWindowsNativeImage *self) {
  return self->width();
}

//  int QWindowsNativeImage::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QWindowsNativeImage6heightEv(
    const QWindowsNativeImage *self) {
  return self->height();
}

//  QImage &QWindowsNativeImage::image()
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN19QWindowsNativeImage5imageEv(QWindowsNativeImage *self) {
  return &self->image();
}

//  const QImage &QWindowsNativeImage::image() const
extern "C" Q_DECL_EXPORT
const QImage *ritual_ZNK19QWindowsNativeImage5imageEv(
    const QWindowsNativeImage *self) {
  return &self->image();
}

//  HDC QWindowsNativeImage::hdc() const
extern "C" Q_DECL_EXPORT
HDC ritual_ZNK19QWindowsNativeImage3hdcEv(const QWindowsNativeImage *self) {
  return self->hdc();
}

//  QImage::Format QWindowsNativeImage::systemFormat()
extern "C" Q_DECL_EXPORT
QImage::Format ritual_ZN19QWindowsNativeImage12systemFormatEv() {
  return QWindowsNativeImage::systemFormat();
}

#endif  // defined(Q_OS_WIN)
