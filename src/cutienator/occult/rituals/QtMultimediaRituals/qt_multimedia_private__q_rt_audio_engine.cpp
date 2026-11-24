//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qrtaudioengine_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qrtaudioengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QtMultimediaPrivate::QRtAudioEngine::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QtMultimediaPrivate14QRtAudioEngine10metaObjectEv(
    const QtMultimediaPrivate::QRtAudioEngine *self) {
  return self->metaObject();
}

//  QString QtMultimediaPrivate::QRtAudioEngine::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QtMultimediaPrivate14QRtAudioEngine2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtMultimediaPrivate::QRtAudioEngine::tr(s, c, n));
}
