//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickfontloader_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickfontloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtGui/qfont.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickFontLoader that Python can take functions over in. Every QQuickFontLoader
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickFontLoaderCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickFontLoaderCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFontLoaderCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFontLoaderCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFontLoaderCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFontLoaderCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickFontLoaderCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickFontLoader : public QQuickFontLoader {
public:
  using QQuickFontLoader::QQuickFontLoader;
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
      CuteQQuickFontLoaderCall0 call = reinterpret_cast<CuteQQuickFontLoaderCall0>(taken[0]);
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
      CuteQQuickFontLoaderCall1 call = reinterpret_cast<CuteQQuickFontLoaderCall1>(taken[1]);
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
      CuteQQuickFontLoaderCall2 call = reinterpret_cast<CuteQQuickFontLoaderCall2>(taken[2]);
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
      CuteQQuickFontLoaderCall3 call = reinterpret_cast<CuteQQuickFontLoaderCall3>(taken[3]);
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
      CuteQQuickFontLoaderCall4 call = reinterpret_cast<CuteQQuickFontLoaderCall4>(taken[4]);
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
      CuteQQuickFontLoaderCall5 call = reinterpret_cast<CuteQQuickFontLoaderCall5>(taken[5]);
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
      CuteQQuickFontLoaderCall6 call = reinterpret_cast<CuteQQuickFontLoaderCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickFontLoader::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuickFontLoader10metaObjectEv(
    const QQuickFontLoader *self) {
  return self->metaObject();
}

//  void *QQuickFontLoader::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QQuickFontLoader11qt_metacastEPKc(
    QQuickFontLoader *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickFontLoader::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQuickFontLoader11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickFontLoader *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickFontLoader::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuickFontLoader2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFontLoader::tr(s, c, n));
}

//  QQuickFontLoaderPrivate *QQuickFontLoader::d_func()
extern "C" Q_DECL_EXPORT
QQuickFontLoaderPrivate *ritual_ZN16QQuickFontLoader6d_funcEv(
    QQuickFontLoader *self) {
  return self->d_func();
}

//  const QQuickFontLoaderPrivate *QQuickFontLoader::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickFontLoaderPrivate *ritual_ZNK16QQuickFontLoader6d_funcEv(
    const QQuickFontLoader *self) {
  return self->d_func();
}

//  QQuickFontLoader::QQuickFontLoader(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickFontLoader *ritual_ZN16QQuickFontLoaderC1EP7QObject(QObject *parent) {
  return new CuteQQuickFontLoader(parent);
}

//  QUrl QQuickFontLoader::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK16QQuickFontLoader6sourceEv(const QQuickFontLoader *self) {
  return new QUrl(self->source());
}

//  void QQuickFontLoader::setSource(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFontLoader9setSourceERK4QUrl(
    QQuickFontLoader *self,
    const QUrl *url) {
  self->setSource(*url);
}

//  QString QQuickFontLoader::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QQuickFontLoader4nameEv(const QQuickFontLoader *self) {
  return new QString(self->name());
}

//  QFont QQuickFontLoader::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK16QQuickFontLoader4fontEv(const QQuickFontLoader *self) {
  return new QFont(self->font());
}

//  Status QQuickFontLoader::status() const
extern "C" Q_DECL_EXPORT
QQuickFontLoader::Status ritual_ZNK16QQuickFontLoader6statusEv(
    const QQuickFontLoader *self) {
  return self->status();
}

//  void QQuickFontLoader::updateFontInfo(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFontLoader14updateFontInfoEi(
    QQuickFontLoader *self,
    int a0) {
  self->updateFontInfo(a0);
}

//  void QQuickFontLoader::sourceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFontLoader13sourceChangedEv(QQuickFontLoader *self) {
  self->sourceChanged();
}

//  void QQuickFontLoader::nameChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFontLoader11nameChangedEv(QQuickFontLoader *self) {
  self->nameChanged();
}

//  void QQuickFontLoader::fontChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFontLoader11fontChangedEv(QQuickFontLoader *self) {
  self->fontChanged();
}

//  void QQuickFontLoader::statusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFontLoader13statusChangedEv(QQuickFontLoader *self) {
  self->statusChanged();
}

//  a Python function taken by a CuteQQuickFontLoader, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickFontLoader(
    QQuickFontLoader *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickFontLoader *>(self)->take(key, call);
}
