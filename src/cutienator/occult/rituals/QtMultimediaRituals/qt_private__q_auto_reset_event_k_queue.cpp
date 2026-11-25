//  Written by hand on 2026-11-25 from
//  QtMultimedia/6.12.0/QtMultimedia/private/qautoresetevent_kqueue_p.h, Qt
//  6.12.0, as the Qt of macOS installs it. Kept as it is when the generator
//  runs again.
//  It is final, so no Cute class is built on it. Not written: the templates
//  'callOnActivated' and the signal 'activated'.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_DARWIN)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qautoresetevent_kqueue_p.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qobject.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QtPrivate::QAutoResetEventKQueue::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QtPrivate21QAutoResetEventKQueue10metaObjectEv(
    const QtPrivate::QAutoResetEventKQueue *self) {
  return self->metaObject();
}

//  QString QtPrivate::QAutoResetEventKQueue::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QtPrivate21QAutoResetEventKQueue2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QtPrivate::QAutoResetEventKQueue::tr(s, c, n));
}

//  QtPrivate::QAutoResetEventKQueue::QAutoResetEventKQueue(QObject *parent)
extern "C" Q_DECL_EXPORT
QtPrivate::QAutoResetEventKQueue *ritual_ZN9QtPrivate21QAutoResetEventKQueueC1EP7QObject(
    QObject *parent) {
  return new QtPrivate::QAutoResetEventKQueue(parent);
}

//  QtPrivate::QAutoResetEventKQueue::~QAutoResetEventKQueue()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate21QAutoResetEventKQueueD1Ev(
    QtPrivate::QAutoResetEventKQueue *self) {
  delete self;
}

//  bool QtPrivate::QAutoResetEventKQueue::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QtPrivate21QAutoResetEventKQueue7isValidEv(
    const QtPrivate::QAutoResetEventKQueue *self) {
  return self->isValid();
}

//  void QtPrivate::QAutoResetEventKQueue::set()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate21QAutoResetEventKQueue3setEv(
    QtPrivate::QAutoResetEventKQueue *self) {
  self->set();
}

#endif  // defined(Q_OS_DARWIN)
