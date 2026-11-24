//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/platformsurfacefilter_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/platformsurfacefilter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::Render::PlatformSurfaceFilter that Python can take functions over in. Every Qt3DRender::Render::PlatformSurfaceFilter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_Render_PlatformSurfaceFilterCall0)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_Render_PlatformSurfaceFilterCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_PlatformSurfaceFilterCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_PlatformSurfaceFilterCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_PlatformSurfaceFilterCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_PlatformSurfaceFilterCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_PlatformSurfaceFilterCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_Render_PlatformSurfaceFilter : public Qt3DRender::Render::PlatformSurfaceFilter {
public:
  using Qt3DRender::Render::PlatformSurfaceFilter::PlatformSurfaceFilter;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool Qt3DRender::Render::PlatformSurfaceFilter::eventFilter(QObject
  //      *obj, QEvent *e)
  bool eventFilter(QObject *obj, QEvent *e) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_PlatformSurfaceFilterCall0 call = reinterpret_cast<CuteQt3DRender_Render_PlatformSurfaceFilterCall0>(taken[0]);
      bool given = call(this, obj, e, &handled);
      if (handled) return given;
    }
    return Qt3DRender::Render::PlatformSurfaceFilter::eventFilter(obj, e);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_Render_PlatformSurfaceFilterCall1 call = reinterpret_cast<CuteQt3DRender_Render_PlatformSurfaceFilterCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DRender_Render_PlatformSurfaceFilterCall2 call = reinterpret_cast<CuteQt3DRender_Render_PlatformSurfaceFilterCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DRender_Render_PlatformSurfaceFilterCall3 call = reinterpret_cast<CuteQt3DRender_Render_PlatformSurfaceFilterCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DRender_Render_PlatformSurfaceFilterCall4 call = reinterpret_cast<CuteQt3DRender_Render_PlatformSurfaceFilterCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DRender_Render_PlatformSurfaceFilterCall5 call = reinterpret_cast<CuteQt3DRender_Render_PlatformSurfaceFilterCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DRender_Render_PlatformSurfaceFilterCall6 call = reinterpret_cast<CuteQt3DRender_Render_PlatformSurfaceFilterCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *Qt3DRender::Render::PlatformSurfaceFilter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender6Render21PlatformSurfaceFilter10metaObjectEv(
    const Qt3DRender::Render::PlatformSurfaceFilter *self) {
  return self->metaObject();
}

//  QString Qt3DRender::Render::PlatformSurfaceFilter::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender6Render21PlatformSurfaceFilter2trEPKcS3_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::Render::PlatformSurfaceFilter::tr(s, c, n));
}

//  a Python function taken by a CuteQt3DRender_Render_PlatformSurfaceFilter,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_PlatformSurfaceFilter(
    Qt3DRender::Render::PlatformSurfaceFilter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_PlatformSurfaceFilter *>(self)->take(key, call);
}

//  bool Qt3DRender::Render::PlatformSurfaceFilter::eventFilter(QObject *obj,
//      QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10Qt3DRender6Render21PlatformSurfaceFilter11eventFilterEP7QObjectP6QEvent(
    Qt3DRender::Render::PlatformSurfaceFilter *self,
    QObject *obj,
    QEvent *e) {
  return self->Qt3DRender::Render::PlatformSurfaceFilter::eventFilter(
      obj,
      e);
}
