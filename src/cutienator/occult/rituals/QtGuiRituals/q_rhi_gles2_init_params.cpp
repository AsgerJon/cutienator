//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi_platform.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(opengl) || defined(Q_QDOC)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi_platform.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qsurfaceformat.h>

//  QRhiGles2InitParams::QRhiGles2InitParams()
extern "C" Q_DECL_EXPORT
QRhiGles2InitParams *ritual_ZN19QRhiGles2InitParamsC1Ev() {
  return new QRhiGles2InitParams();
}

//  QOffscreenSurface *QRhiGles2InitParams::newFallbackSurface(const
//      QSurfaceFormat &format)
extern "C" Q_DECL_EXPORT
QOffscreenSurface *ritual_ZN19QRhiGles2InitParams18newFallbackSurfaceERK14QSurfaceFormat(
    const QSurfaceFormat *format) {
  return QRhiGles2InitParams::newFallbackSurface(*format);
}

//  QRhiGles2InitParams::~QRhiGles2InitParams()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRhiGles2InitParamsD1Ev(QRhiGles2InitParams *self) {
  delete self;
}

#endif  // QT_CONFIG(opengl) || defined(Q_QDOC)
