//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickimage_p_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickimage_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickImageTextureProvider that Python can take functions over in. Every QQuickImageTextureProvider
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuickImageTextureProviderCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickImageTextureProviderCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickImageTextureProviderCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageTextureProviderCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageTextureProviderCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageTextureProviderCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageTextureProviderCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickImageTextureProviderCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickImageTextureProvider : public QQuickImageTextureProvider {
public:
  using QQuickImageTextureProvider::QQuickImageTextureProvider;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK18QSGTextureProvider7textureEv")) {
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

  //  QSGTexture *QQuickImageTextureProvider::texture() const
  QSGTexture *texture() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickImageTextureProviderCall0 call = reinterpret_cast<CuteQQuickImageTextureProviderCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTexture *>(given);
    }
    return QQuickImageTextureProvider::texture();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickImageTextureProviderCall1 call = reinterpret_cast<CuteQQuickImageTextureProviderCall1>(taken[1]);
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
      CuteQQuickImageTextureProviderCall2 call = reinterpret_cast<CuteQQuickImageTextureProviderCall2>(taken[2]);
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
      CuteQQuickImageTextureProviderCall3 call = reinterpret_cast<CuteQQuickImageTextureProviderCall3>(taken[3]);
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
      CuteQQuickImageTextureProviderCall4 call = reinterpret_cast<CuteQQuickImageTextureProviderCall4>(taken[4]);
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
      CuteQQuickImageTextureProviderCall5 call = reinterpret_cast<CuteQQuickImageTextureProviderCall5>(taken[5]);
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
      CuteQQuickImageTextureProviderCall6 call = reinterpret_cast<CuteQQuickImageTextureProviderCall6>(taken[6]);
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
      CuteQQuickImageTextureProviderCall7 call = reinterpret_cast<CuteQQuickImageTextureProviderCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickImageTextureProvider::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QQuickImageTextureProvider10metaObjectEv(
    const QQuickImageTextureProvider *self) {
  return self->metaObject();
}

//  void *QQuickImageTextureProvider::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QQuickImageTextureProvider11qt_metacastEPKc(
    QQuickImageTextureProvider *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickImageTextureProvider::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QQuickImageTextureProvider11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickImageTextureProvider *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickImageTextureProvider::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QQuickImageTextureProvider2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickImageTextureProvider::tr(s, c, n));
}

//  QQuickImageTextureProvider::QQuickImageTextureProvider()
extern "C" Q_DECL_EXPORT
QQuickImageTextureProvider *ritual_ZN26QQuickImageTextureProviderC1Ev() {
  return new CuteQQuickImageTextureProvider();
}

//  void QQuickImageTextureProvider::updateTexture(QSGTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickImageTextureProvider13updateTextureEP10QSGTexture(
    QQuickImageTextureProvider *self,
    QSGTexture *texture) {
  self->updateTexture(texture);
}

//  QSGTexture *QQuickImageTextureProvider::texture() const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK26QQuickImageTextureProvider7textureEv(
    const QQuickImageTextureProvider *self) {
  return self->texture();
}

//  a Python function taken by a CuteQQuickImageTextureProvider, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickImageTextureProvider(
    QQuickImageTextureProvider *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickImageTextureProvider *>(self)->take(key, call);
}

//  QSGTexture *QQuickImageTextureProvider::texture() const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_own_ZNK26QQuickImageTextureProvider7textureEv(
    const QQuickImageTextureProvider *self) {
  return self->QQuickImageTextureProvider::texture();
}
