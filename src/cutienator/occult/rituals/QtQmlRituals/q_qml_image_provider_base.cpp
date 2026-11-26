//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlengine.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlengine.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlImageProviderBase that Python can take functions over in. Every QQmlImageProviderBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQQmlImageProviderBaseCall0)(const void *, int *);
typedef int (*CuteQQmlImageProviderBaseCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlImageProviderBaseCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlImageProviderBaseCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlImageProviderBaseCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlImageProviderBaseCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlImageProviderBaseCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlImageProviderBaseCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlImageProviderBaseCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlImageProviderBase : public QQmlImageProviderBase {
public:
  using QQmlImageProviderBase::QQmlImageProviderBase;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK21QQmlImageProviderBase9imageTypeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QQmlImageProviderBase5flagsEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  ImageType QQmlImageProviderBase::imageType() const
  QQmlImageProviderBase::ImageType imageType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlImageProviderBaseCall0 call = reinterpret_cast<CuteQQmlImageProviderBaseCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQmlImageProviderBase::ImageType>(given);
    }
    return {};
  }

  //  Flags QQmlImageProviderBase::flags() const
  QQmlImageProviderBase::Flags flags() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlImageProviderBaseCall1 call = reinterpret_cast<CuteQQmlImageProviderBaseCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return QFlags<QQmlImageProviderBase::Flag>::fromInt(given);
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlImageProviderBaseCall2 call = reinterpret_cast<CuteQQmlImageProviderBaseCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlImageProviderBaseCall3 call = reinterpret_cast<CuteQQmlImageProviderBaseCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlImageProviderBaseCall4 call = reinterpret_cast<CuteQQmlImageProviderBaseCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlImageProviderBaseCall5 call = reinterpret_cast<CuteQQmlImageProviderBaseCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlImageProviderBaseCall6 call = reinterpret_cast<CuteQQmlImageProviderBaseCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlImageProviderBaseCall7 call = reinterpret_cast<CuteQQmlImageProviderBaseCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlImageProviderBaseCall8 call = reinterpret_cast<CuteQQmlImageProviderBaseCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlImageProviderBase::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQmlImageProviderBase10metaObjectEv(
    const QQmlImageProviderBase *self) {
  return self->metaObject();
}

//  void *QQmlImageProviderBase::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQmlImageProviderBase11qt_metacastEPKc(
    QQmlImageProviderBase *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlImageProviderBase::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQmlImageProviderBase11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlImageProviderBase *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlImageProviderBase::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQmlImageProviderBase2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlImageProviderBase::tr(s, c, n));
}

//  QQmlImageProviderBase::~QQmlImageProviderBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlImageProviderBaseD1Ev(QQmlImageProviderBase *self) {
  delete self;
}

//  ImageType QQmlImageProviderBase::imageType() const
extern "C" Q_DECL_EXPORT
QQmlImageProviderBase::ImageType ritual_ZNK21QQmlImageProviderBase9imageTypeEv(
    const QQmlImageProviderBase *self) {
  return self->imageType();
}

//  Flags QQmlImageProviderBase::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQmlImageProviderBase5flagsEv(
    const QQmlImageProviderBase *self) {
  return static_cast<int>(self->flags().toInt());
}

//  QQmlImageProviderBase::QQmlImageProviderBase()
extern "C" Q_DECL_EXPORT
QQmlImageProviderBase *ritual_ZN21QQmlImageProviderBaseC1Ev() {
  return new CuteQQmlImageProviderBase();
}

//  a Python function taken by a CuteQQmlImageProviderBase, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlImageProviderBase(
    QQmlImageProviderBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlImageProviderBase *>(self)->take(key, call);
}
