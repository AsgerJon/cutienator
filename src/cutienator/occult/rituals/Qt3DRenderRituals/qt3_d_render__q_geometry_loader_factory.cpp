//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qgeometryloaderfactory_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qgeometryloaderfactory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QGeometryLoaderFactory that Python can take functions over in. Every Qt3DRender::QGeometryLoaderFactory
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQt3DRender_QGeometryLoaderFactoryCall0)(const void *, const QString *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QGeometryLoaderFactoryCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QGeometryLoaderFactoryCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QGeometryLoaderFactoryCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QGeometryLoaderFactoryCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QGeometryLoaderFactoryCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QGeometryLoaderFactoryCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QGeometryLoaderFactoryCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QGeometryLoaderFactory : public Qt3DRender::QGeometryLoaderFactory {
public:
  using Qt3DRender::QGeometryLoaderFactory::QGeometryLoaderFactory;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10Qt3DRender22QGeometryLoaderFactory6createERK7QString")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QGeometryLoaderInterface
  //      *Qt3DRender::QGeometryLoaderFactory::create(const QString &ext)
  Qt3DRender::QGeometryLoaderInterface *create(const QString &ext) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_QGeometryLoaderFactoryCall0 call = reinterpret_cast<CuteQt3DRender_QGeometryLoaderFactoryCall0>(taken[0]);
      void * given = call(this, &ext, &handled);
      if (handled) return static_cast<Qt3DRender::QGeometryLoaderInterface *>(given);
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QGeometryLoaderFactoryCall1 call = reinterpret_cast<CuteQt3DRender_QGeometryLoaderFactoryCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DRender_QGeometryLoaderFactoryCall2 call = reinterpret_cast<CuteQt3DRender_QGeometryLoaderFactoryCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DRender_QGeometryLoaderFactoryCall3 call = reinterpret_cast<CuteQt3DRender_QGeometryLoaderFactoryCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DRender_QGeometryLoaderFactoryCall4 call = reinterpret_cast<CuteQt3DRender_QGeometryLoaderFactoryCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DRender_QGeometryLoaderFactoryCall5 call = reinterpret_cast<CuteQt3DRender_QGeometryLoaderFactoryCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DRender_QGeometryLoaderFactoryCall6 call = reinterpret_cast<CuteQt3DRender_QGeometryLoaderFactoryCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQt3DRender_QGeometryLoaderFactoryCall7 call = reinterpret_cast<CuteQt3DRender_QGeometryLoaderFactoryCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QGeometryLoaderFactory::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender22QGeometryLoaderFactory10metaObjectEv(
    const Qt3DRender::QGeometryLoaderFactory *self) {
  return self->metaObject();
}

//  QString Qt3DRender::QGeometryLoaderFactory::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender22QGeometryLoaderFactory2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QGeometryLoaderFactory::tr(s, c, n));
}

//  Qt3DRender::QGeometryLoaderFactory::~QGeometryLoaderFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender22QGeometryLoaderFactoryD1Ev(
    Qt3DRender::QGeometryLoaderFactory *self) {
  delete self;
}

//  QGeometryLoaderInterface
//      *Qt3DRender::QGeometryLoaderFactory::create(const QString &ext)
extern "C" Q_DECL_EXPORT
Qt3DRender::QGeometryLoaderInterface *ritual_ZN10Qt3DRender22QGeometryLoaderFactory6createERK7QString(
    Qt3DRender::QGeometryLoaderFactory *self,
    const QString *ext) {
  return self->create(*ext);
}

//  Qt3DRender::QGeometryLoaderFactory as the QFactoryInterface it is built
//      on
extern "C" Q_DECL_EXPORT
QFactoryInterface *ritual_cast_Qt3DRender_QGeometryLoaderFactory_QFactoryInterface(
    Qt3DRender::QGeometryLoaderFactory *self) {
  return static_cast<QFactoryInterface *>(self);
}

//  a Python function taken by a CuteQt3DRender_QGeometryLoaderFactory, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QGeometryLoaderFactory(
    Qt3DRender::QGeometryLoaderFactory *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QGeometryLoaderFactory *>(self)->take(key, call);
}
