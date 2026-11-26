//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/quick3dlayerfilter_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/qt3dquickrender_global_p.h>
#include <Qt3DQuickRender/Qt3DQuickRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/quick3dlayerfilter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <Qt3DRender/Qt3DRender>

//  A Qt3DRender::Render::Quick::Quick3DLayerFilter that Python can take functions over in. Every Qt3DRender::Render::Quick::Quick3DLayerFilter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_Render_Quick_Quick3DLayerFilterCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_Render_Quick_Quick3DLayerFilterCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_Quick_Quick3DLayerFilterCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_Quick_Quick3DLayerFilterCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_Quick_Quick3DLayerFilterCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_Quick_Quick3DLayerFilterCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Render_Quick_Quick3DLayerFilterCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_Render_Quick_Quick3DLayerFilter : public Qt3DRender::Render::Quick::Quick3DLayerFilter {
public:
  using Qt3DRender::Render::Quick::Quick3DLayerFilter::Quick3DLayerFilter;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
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
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_Quick_Quick3DLayerFilterCall0 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Quick3DLayerFilterCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_Render_Quick_Quick3DLayerFilterCall1 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Quick3DLayerFilterCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DRender_Render_Quick_Quick3DLayerFilterCall2 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Quick3DLayerFilterCall2>(taken[2]);
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
      CuteQt3DRender_Render_Quick_Quick3DLayerFilterCall3 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Quick3DLayerFilterCall3>(taken[3]);
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
      CuteQt3DRender_Render_Quick_Quick3DLayerFilterCall4 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Quick3DLayerFilterCall4>(taken[4]);
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
      CuteQt3DRender_Render_Quick_Quick3DLayerFilterCall5 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Quick3DLayerFilterCall5>(taken[5]);
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
      CuteQt3DRender_Render_Quick_Quick3DLayerFilterCall6 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Quick3DLayerFilterCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *Qt3DRender::Render::Quick::Quick3DLayerFilter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender6Render5Quick18Quick3DLayerFilter10metaObjectEv(
    const Qt3DRender::Render::Quick::Quick3DLayerFilter *self) {
  return self->metaObject();
}

//  void *Qt3DRender::Render::Quick::Quick3DLayerFilter::qt_metacast(const
//      char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender6Render5Quick18Quick3DLayerFilter11qt_metacastEPKc(
    Qt3DRender::Render::Quick::Quick3DLayerFilter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::Render::Quick::Quick3DLayerFilter::qt_metacall(QMetaObjec
//      t::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender6Render5Quick18Quick3DLayerFilter11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::Render::Quick::Quick3DLayerFilter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::Render::Quick::Quick3DLayerFilter::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender6Render5Quick18Quick3DLayerFilter2trEPKcS4_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      Qt3DRender::Render::Quick::Quick3DLayerFilter::tr(
          s,
          c,
          n));
}

//  Qt3DRender::Render::Quick::Quick3DLayerFilter::Quick3DLayerFilter(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Quick::Quick3DLayerFilter *ritual_ZN10Qt3DRender6Render5Quick18Quick3DLayerFilterC1EP7QObject(
    QObject *parent) {
  return new CuteQt3DRender_Render_Quick_Quick3DLayerFilter(parent);
}

//  QLayerFilter
//      *Qt3DRender::Render::Quick::Quick3DLayerFilter::parentFilter() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QLayerFilter *ritual_ZNK10Qt3DRender6Render5Quick18Quick3DLayerFilter12parentFilterEv(
    const Qt3DRender::Render::Quick::Quick3DLayerFilter *self) {
  return self->parentFilter();
}

//  QQmlListProperty<QLayer>
//      Qt3DRender::Render::Quick::Quick3DLayerFilter::qmlLayers()
extern "C" Q_DECL_EXPORT
QQmlListProperty<Qt3DRender::QLayer> *ritual_ZN10Qt3DRender6Render5Quick18Quick3DLayerFilter9qmlLayersEv(
    Qt3DRender::Render::Quick::Quick3DLayerFilter *self) {
  return new QQmlListProperty<Qt3DRender::QLayer>(self->qmlLayers());
}

//  a Python function taken by a
//      CuteQt3DRender_Render_Quick_Quick3DLayerFilter, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_Quick_Quick3DLayerFilter(
    Qt3DRender::Render::Quick::Quick3DLayerFilter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_Quick_Quick3DLayerFilter *>(self)->take(key, call);
}

//  a QQmlListProperty<Qt3DRender::QLayer> a ritual of
//      Qt3DRender::Render::Quick::Quick3DLayerFilter gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_Quick_Quick3DLayerFilter__QQmlListProperty_Qt3DRender_QLayer(
    QQmlListProperty<Qt3DRender::QLayer> *self) {
  delete self;
}
