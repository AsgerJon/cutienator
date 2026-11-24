//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dlightmapbaker_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dlightmapbaker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuick3DLightmapBaker that Python can take functions over in. Every QQuick3DLightmapBaker
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DLightmapBakerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DLightmapBakerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DLightmapBakerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DLightmapBakerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DLightmapBakerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DLightmapBakerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DLightmapBakerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DLightmapBaker : public QQuick3DLightmapBaker {
public:
  using QQuick3DLightmapBaker::QQuick3DLightmapBaker;
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
      CuteQQuick3DLightmapBakerCall0 call = reinterpret_cast<CuteQQuick3DLightmapBakerCall0>(taken[0]);
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
      CuteQQuick3DLightmapBakerCall1 call = reinterpret_cast<CuteQQuick3DLightmapBakerCall1>(taken[1]);
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
      CuteQQuick3DLightmapBakerCall2 call = reinterpret_cast<CuteQQuick3DLightmapBakerCall2>(taken[2]);
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
      CuteQQuick3DLightmapBakerCall3 call = reinterpret_cast<CuteQQuick3DLightmapBakerCall3>(taken[3]);
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
      CuteQQuick3DLightmapBakerCall4 call = reinterpret_cast<CuteQQuick3DLightmapBakerCall4>(taken[4]);
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
      CuteQQuick3DLightmapBakerCall5 call = reinterpret_cast<CuteQQuick3DLightmapBakerCall5>(taken[5]);
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
      CuteQQuick3DLightmapBakerCall6 call = reinterpret_cast<CuteQQuick3DLightmapBakerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DLightmapBaker::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuick3DLightmapBaker10metaObjectEv(
    const QQuick3DLightmapBaker *self) {
  return self->metaObject();
}

//  QString QQuick3DLightmapBaker::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuick3DLightmapBaker2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DLightmapBaker::tr(s, c, n));
}

//  QQuick3DLightmapBaker::QQuick3DLightmapBaker(QQuick3DViewport *view)
extern "C" Q_DECL_EXPORT
QQuick3DLightmapBaker *ritual_ZN21QQuick3DLightmapBakerC1EP16QQuick3DViewport(
    QQuick3DViewport *view) {
  return new CuteQQuick3DLightmapBaker(view);
}

//  QQuick3DLightmapBaker::~QQuick3DLightmapBaker()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DLightmapBakerD1Ev(QQuick3DLightmapBaker *self) {
  delete self;
}

//  void QQuick3DLightmapBaker::bake()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DLightmapBaker4bakeEv(QQuick3DLightmapBaker *self) {
  self->bake();
}

//  void QQuick3DLightmapBaker::denoise()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DLightmapBaker7denoiseEv(
    QQuick3DLightmapBaker *self) {
  self->denoise();
}

//  void QQuick3DLightmapBaker::onLmCancelButtonClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DLightmapBaker23onLmCancelButtonClickedEv(
    QQuick3DLightmapBaker *self) {
  self->onLmCancelButtonClicked();
}

//  void QQuick3DLightmapBaker::onLmWindowClosing(QQuickCloseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DLightmapBaker17onLmWindowClosingEP16QQuickCloseEvent(
    QQuick3DLightmapBaker *self,
    QQuickCloseEvent *event) {
  self->onLmWindowClosing(event);
}

//  void QQuick3DLightmapBaker::updateView()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuick3DLightmapBaker10updateViewEv(
    QQuick3DLightmapBaker *self) {
  self->updateView();
}

//  a Python function taken by a CuteQQuick3DLightmapBaker, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DLightmapBaker(
    QQuick3DLightmapBaker *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DLightmapBaker *>(self)->take(key, call);
}
