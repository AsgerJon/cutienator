//  Written by hand on 2026-11-25 from
//  QtMultimedia/6.12.0/QtMultimedia/private/qavfhelpers_p.h, Qt 6.12.0, as
//  the Qt of macOS installs it. Kept as it is when the generator runs again.
//  A 'CVPixelBufferRef' is passed as an address. Not written: 'ref' and
//  'unref', which call CoreVideo, a library outside Qt.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_DARWIN)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qavfhelpers_p.h>

//  Type QAVFHelpers::QSharedCVPixelBufferHandleTraits::invalidValue()
extern "C" Q_DECL_EXPORT
CVPixelBufferRef ritual_ZN11QAVFHelpers32QSharedCVPixelBufferHandleTraits12invalidValueEv() {
  return QAVFHelpers::QSharedCVPixelBufferHandleTraits::invalidValue();
}

//  QAVFHelpers::QSharedCVPixelBufferHandleTraits::~QSharedCVPixelBufferHandl
//      eTraits()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAVFHelpers32QSharedCVPixelBufferHandleTraitsD1Ev(
    QAVFHelpers::QSharedCVPixelBufferHandleTraits *self) {
  delete self;
}

#endif  // defined(Q_OS_DARWIN)
