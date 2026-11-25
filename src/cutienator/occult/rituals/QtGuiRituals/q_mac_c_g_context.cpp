//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qcoregraphics_p.h, Qt 6.12.0, as the Qt of
//  macOS installs it. Kept as it is when the generator runs again.
//  A 'CGContextRef' of Apple's Core Graphics is passed as an address.
//  Not written: the destructor, which its header writes out and which
//  releases the context by 'CFRelease', a function of Apple's
//  CoreFoundation, a library outside Qt.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_DARWIN)
#include <QtGui/6.12.0/QtGui/private/qcoregraphics_p.h>
#include <QtGui/qimage.h>
#include <QtGui/qpaintdevice.h>
#include <QtGui/qpainter.h>

//  QMacCGContext::QMacCGContext()
extern "C" Q_DECL_EXPORT
QMacCGContext *ritual_ZN13QMacCGContextC1Ev() {
  return new QMacCGContext();
}

//  QMacCGContext::QMacCGContext(QPaintDevice *pdev)
extern "C" Q_DECL_EXPORT
QMacCGContext *ritual_ZN13QMacCGContextC1EP12QPaintDevice(
    QPaintDevice *pdev) {
  return new QMacCGContext(pdev);
}

//  QMacCGContext::QMacCGContext(QPainter *p)
extern "C" Q_DECL_EXPORT
QMacCGContext *ritual_ZN13QMacCGContextC1EP8QPainter(QPainter *p) {
  return new QMacCGContext(p);
}

//  QMacCGContext::operator CGContextRef()
extern "C" Q_DECL_EXPORT
CGContextRef ritual_ZN13QMacCGContextcvP9CGContextEv(QMacCGContext *self) {
  return self->operator CGContextRef();
}

//  void QMacCGContext::initialize(QPaintDevice *paintDevice)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMacCGContext10initializeEP12QPaintDevice(
    QMacCGContext *self,
    QPaintDevice *paintDevice) {
  self->initialize(paintDevice);
}

//  void QMacCGContext::initialize(const QImage *a0, QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMacCGContext10initializeEPK6QImageP8QPainter(
    QMacCGContext *self,
    const QImage *a0,
    QPainter *painter) {
  self->initialize(a0, painter);
}

#endif  // defined(Q_OS_DARWIN)
