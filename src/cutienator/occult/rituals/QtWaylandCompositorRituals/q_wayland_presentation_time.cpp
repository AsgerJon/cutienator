//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwaylandpresentationtime_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if QT_CONFIG(wayland_compositor_quick)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandpresentationtime_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QWaylandPresentationTime that Python can take functions over in. Every QWaylandPresentationTime
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWaylandPresentationTimeCall0)(const void *, int *);
class CuteQWaylandPresentationTime : public QWaylandPresentationTime {
public:
  using QWaylandPresentationTime::QWaylandPresentationTime;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QWaylandPresentationTime10initializeEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QWaylandPresentationTime::initialize()
  void initialize() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandPresentationTimeCall0 call = reinterpret_cast<CuteQWaylandPresentationTimeCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandPresentationTime::initialize();
  }
};

//  const QMetaObject *QWaylandPresentationTime::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QWaylandPresentationTime10metaObjectEv(
    const QWaylandPresentationTime *self) {
  return self->metaObject();
}

//  QString QWaylandPresentationTime::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QWaylandPresentationTime2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandPresentationTime::tr(s, c, n));
}

//  QWaylandPresentationTime::QWaylandPresentationTime()
extern "C" Q_DECL_EXPORT
QWaylandPresentationTime *ritual_ZN24QWaylandPresentationTimeC1Ev() {
  return new CuteQWaylandPresentationTime();
}

//  QWaylandPresentationTime::QWaylandPresentationTime(QWaylandCompositor
//      *compositor)
extern "C" Q_DECL_EXPORT
QWaylandPresentationTime *ritual_ZN24QWaylandPresentationTimeC1EP18QWaylandCompositor(
    QWaylandCompositor *compositor) {
  return new CuteQWaylandPresentationTime(compositor);
}

//  QWaylandCompositor *QWaylandPresentationTime::compositor() const
extern "C" Q_DECL_EXPORT
QWaylandCompositor *ritual_ZNK24QWaylandPresentationTime10compositorEv(
    const QWaylandPresentationTime *self) {
  return self->compositor();
}

//  void QWaylandPresentationTime::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWaylandPresentationTime10initializeEv(
    QWaylandPresentationTime *self) {
  self->initialize();
}

//  void QWaylandPresentationTime::sendFeedback(QQuickWindow *window, quint64
//      sequence, quint64 tv_sec, quint32 tv_nsec)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWaylandPresentationTime12sendFeedbackEP12QQuickWindowyyj(
    QWaylandPresentationTime *self,
    QQuickWindow *window,
    quint64 sequence,
    quint64 tv_sec,
    quint32 tv_nsec) {
  self->sendFeedback(window, sequence, tv_sec, tv_nsec);
}

//  QByteArray QWaylandPresentationTime::interfaceName()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN24QWaylandPresentationTime13interfaceNameEv() {
  return new QByteArray(QWaylandPresentationTime::interfaceName());
}

//  a Python function taken by a CuteQWaylandPresentationTime, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandPresentationTime(
    QWaylandPresentationTime *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandPresentationTime *>(self)->take(key, call);
}

//  void QWaylandPresentationTime::initialize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QWaylandPresentationTime10initializeEv(
    QWaylandPresentationTime *self) {
  self->QWaylandPresentationTime::initialize();
}

#endif  // QT_CONFIG(wayland_compositor_quick)
