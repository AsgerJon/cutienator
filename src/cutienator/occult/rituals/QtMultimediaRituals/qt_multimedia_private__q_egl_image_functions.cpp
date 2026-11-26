//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qdmabuftextureimporter_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if QT_CONFIG(linux_dmabuf)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qdmabuftextureimporter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QtMultimediaPrivate::QEglImageFunctions::QEglImageFunctions()
extern "C" Q_DECL_EXPORT
QtMultimediaPrivate::QEglImageFunctions *ritual_ZN19QtMultimediaPrivate18QEglImageFunctionsC1Ev() {
  return new QtMultimediaPrivate::QEglImageFunctions();
}

//  const QEglImageFunctions
//      &QtMultimediaPrivate::QEglImageFunctions::instance()
extern "C" Q_DECL_EXPORT
QtMultimediaPrivate::QEglImageFunctions *ritual_ZN19QtMultimediaPrivate18QEglImageFunctions8instanceEv() {
  return new QtMultimediaPrivate::QEglImageFunctions(
      QtMultimediaPrivate::QEglImageFunctions::instance());
}

//  bool QtMultimediaPrivate::QEglImageFunctions::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QtMultimediaPrivate18QEglImageFunctions7isValidEv(
    const QtMultimediaPrivate::QEglImageFunctions *self) {
  return self->isValid();
}

//  void QtMultimediaPrivate::QEglImageFunctions::glEGLImageTargetTexture2DOE
//      S(GLenum a0, GLeglImageOES a1) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QtMultimediaPrivate18QEglImageFunctions28glEGLImageTargetTexture2DOESEjPv(
    const QtMultimediaPrivate::QEglImageFunctions *self,
    GLenum a0,
    GLeglImageOES a1) {
  self->glEGLImageTargetTexture2DOES(a0, a1);
}

//  QtMultimediaPrivate::QEglImageFunctions::~QEglImageFunctions()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate18QEglImageFunctionsD1Ev(
    QtMultimediaPrivate::QEglImageFunctions *self) {
  delete self;
}

#endif  // QT_CONFIG(linux_dmabuf)
