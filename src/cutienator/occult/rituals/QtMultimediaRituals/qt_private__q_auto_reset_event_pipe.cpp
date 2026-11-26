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

//  void *QtPrivate::QAutoResetEventPipe::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9QtPrivate19QAutoResetEventPipe11qt_metacastEPKc(
    QtPrivate::QAutoResetEventPipe *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtPrivate::QAutoResetEventPipe::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtPrivate19QAutoResetEventPipe11qt_metacallEN11QMetaObject4CallEiPPv(
    QtPrivate::QAutoResetEventPipe *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  QtPrivate::QAutoResetEventPipe::QAutoResetEventPipe(QObject *parent)
extern "C" Q_DECL_EXPORT
QtPrivate::QAutoResetEventPipe *ritual_ZN9QtPrivate19QAutoResetEventPipeC1EP7QObject(
    QObject *parent) {
  return new QtPrivate::QAutoResetEventPipe(parent);
}

//  QtPrivate::QAutoResetEventPipe::~QAutoResetEventPipe()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate19QAutoResetEventPipeD1Ev(
    QtPrivate::QAutoResetEventPipe *self) {
  delete self;
}

//  bool QtPrivate::QAutoResetEventPipe::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate19QAutoResetEventPipe7isValidEv(
    const QtPrivate::QAutoResetEventPipe *self) {
  return self->isValid();
}

//  void QtPrivate::QAutoResetEventPipe::set()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate19QAutoResetEventPipe3setEv(
    QtPrivate::QAutoResetEventPipe *self) {
  self->set();
}

//  void QtPrivate::QAutoResetEventPipe::activated()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate19QAutoResetEventPipe9activatedEv(
    QtPrivate::QAutoResetEventPipe *self) {
  self->activated();
}

#endif  // defined(Q_OS_UNIX)
