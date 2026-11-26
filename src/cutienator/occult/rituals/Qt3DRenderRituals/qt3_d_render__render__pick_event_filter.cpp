//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/pickeventfilter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/pickeventfilter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::Render::PickEventFilter that Python can take functions over in. Every Qt3DRender::Render::PickEventFilter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_Render_PickEventFilterCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_PickEventFilterCall1)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_PickEventFilterCall2)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_PickEventFilterCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_PickEventFilterCall4)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_PickEventFilterCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_Render_PickEventFilter : public Qt3DRender::Render::PickEventFilter {
public:
  using Qt3DRender::Render::PickEventFilter::PickEventFilter;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_PickEventFilterCall0 call = reinterpret_cast<CuteQt3DRender_Render_PickEventFilterCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_Render_PickEventFilterCall1 call = reinterpret_cast<CuteQt3DRender_Render_PickEventFilterCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DRender_Render_PickEventFilterCall2 call = reinterpret_cast<CuteQt3DRender_Render_PickEventFilterCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DRender_Render_PickEventFilterCall3 call = reinterpret_cast<CuteQt3DRender_Render_PickEventFilterCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DRender_Render_PickEventFilterCall4 call = reinterpret_cast<CuteQt3DRender_Render_PickEventFilterCall4>(taken[4]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DRender_Render_PickEventFilterCall5 call = reinterpret_cast<CuteQt3DRender_Render_PickEventFilterCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::Render::PickEventFilter::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender6Render15PickEventFilter10metaObjectEv(
    const Qt3DRender::Render::PickEventFilter *self) {
  return self->metaObject();
}

//  void *Qt3DRender::Render::PickEventFilter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender6Render15PickEventFilter11qt_metacastEPKc(
    Qt3DRender::Render::PickEventFilter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::Render::PickEventFilter::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender6Render15PickEventFilter11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::Render::PickEventFilter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::Render::PickEventFilter::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender6Render15PickEventFilter2trEPKcS3_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::Render::PickEventFilter::tr(s, c, n));
}

//  Qt3DRender::Render::PickEventFilter::PickEventFilter(QRenderAspectPrivate
//      *aspect, QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::PickEventFilter *ritual_ZN10Qt3DRender6Render15PickEventFilterC1EPNS_20QRenderAspectPrivateEP7QObject(
    Qt3DRender::QRenderAspectPrivate *aspect,
    QObject *parent) {
  return new CuteQt3DRender_Render_PickEventFilter(aspect, parent);
}

//  Qt3DRender::Render::PickEventFilter::~PickEventFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render15PickEventFilterD1Ev(
    Qt3DRender::Render::PickEventFilter *self) {
  delete self;
}

//  bool Qt3DRender::Render::PickEventFilter::eventFilter(QObject *obj,
//      QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10Qt3DRender6Render15PickEventFilter11eventFilterEP7QObjectP6QEvent(
    Qt3DRender::Render::PickEventFilter *self,
    QObject *obj,
    QEvent *e) {
  return self->eventFilter(obj, e);
}

//  a Python function taken by a CuteQt3DRender_Render_PickEventFilter, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_PickEventFilter(
    Qt3DRender::Render::PickEventFilter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_PickEventFilter *>(self)->take(key, call);
}
