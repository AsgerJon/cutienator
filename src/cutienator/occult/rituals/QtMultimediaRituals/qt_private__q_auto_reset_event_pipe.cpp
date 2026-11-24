//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qautoresetevent_pipe_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_UNIX)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qautoresetevent_pipe_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QtPrivate::QAutoResetEventPipe::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QtPrivate19QAutoResetEventPipe10metaObjectEv(
    const QtPrivate::QAutoResetEventPipe *self) {
  return self->metaObject();
}

//  QString QtPrivate::QAutoResetEventPipe::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QtPrivate19QAutoResetEventPipe2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtPrivate::QAutoResetEventPipe::tr(s, c, n));
}

//  bool QtPrivate::QAutoResetEventPipe::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate19QAutoResetEventPipe7isValidEv(
    const QtPrivate::QAutoResetEventPipe *self) {
  return self->isValid();
}

#endif  // defined(Q_OS_UNIX)
