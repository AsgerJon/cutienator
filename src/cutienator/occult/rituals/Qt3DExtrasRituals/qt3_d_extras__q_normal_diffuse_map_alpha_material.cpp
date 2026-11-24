//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qnormaldiffusemapalphamaterial.h, Qt 6.12.0. Changes made here
//  are lost.
#include <Qt3DExtras/qnormaldiffusemapalphamaterial.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QNormalDiffuseMapAlphaMaterial that Python can take functions over in. Every Qt3DExtras::QNormalDiffuseMapAlphaMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QNormalDiffuseMapAlphaMaterialCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QNormalDiffuseMapAlphaMaterialCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QNormalDiffuseMapAlphaMaterialCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QNormalDiffuseMapAlphaMaterialCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QNormalDiffuseMapAlphaMaterialCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QNormalDiffuseMapAlphaMaterialCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QNormalDiffuseMapAlphaMaterialCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QNormalDiffuseMapAlphaMaterial : public Qt3DExtras::QNormalDiffuseMapAlphaMaterial {
public:
  using Qt3DExtras::QNormalDiffuseMapAlphaMaterial::QNormalDiffuseMapAlphaMaterial;
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
      CuteQt3DExtras_QNormalDiffuseMapAlphaMaterialCall0 call = reinterpret_cast<CuteQt3DExtras_QNormalDiffuseMapAlphaMaterialCall0>(taken[0]);
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
      CuteQt3DExtras_QNormalDiffuseMapAlphaMaterialCall1 call = reinterpret_cast<CuteQt3DExtras_QNormalDiffuseMapAlphaMaterialCall1>(taken[1]);
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
      CuteQt3DExtras_QNormalDiffuseMapAlphaMaterialCall2 call = reinterpret_cast<CuteQt3DExtras_QNormalDiffuseMapAlphaMaterialCall2>(taken[2]);
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
      CuteQt3DExtras_QNormalDiffuseMapAlphaMaterialCall3 call = reinterpret_cast<CuteQt3DExtras_QNormalDiffuseMapAlphaMaterialCall3>(taken[3]);
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
      CuteQt3DExtras_QNormalDiffuseMapAlphaMaterialCall4 call = reinterpret_cast<CuteQt3DExtras_QNormalDiffuseMapAlphaMaterialCall4>(taken[4]);
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
      CuteQt3DExtras_QNormalDiffuseMapAlphaMaterialCall5 call = reinterpret_cast<CuteQt3DExtras_QNormalDiffuseMapAlphaMaterialCall5>(taken[5]);
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
      CuteQt3DExtras_QNormalDiffuseMapAlphaMaterialCall6 call = reinterpret_cast<CuteQt3DExtras_QNormalDiffuseMapAlphaMaterialCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *Qt3DExtras::QNormalDiffuseMapAlphaMaterial::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras30QNormalDiffuseMapAlphaMaterial10metaObjectEv(
    const Qt3DExtras::QNormalDiffuseMapAlphaMaterial *self) {
  return self->metaObject();
}

//  QString Qt3DExtras::QNormalDiffuseMapAlphaMaterial::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras30QNormalDiffuseMapAlphaMaterial2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      Qt3DExtras::QNormalDiffuseMapAlphaMaterial::tr(
          s,
          c,
          n));
}

//  QNormalDiffuseMapAlphaMaterialPrivate
//      *Qt3DExtras::QNormalDiffuseMapAlphaMaterial::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QNormalDiffuseMapAlphaMaterialPrivate *ritual_ZN10Qt3DExtras30QNormalDiffuseMapAlphaMaterial6d_funcEv(
    Qt3DExtras::QNormalDiffuseMapAlphaMaterial *self) {
  return self->d_func();
}

//  const QNormalDiffuseMapAlphaMaterialPrivate
//      *Qt3DExtras::QNormalDiffuseMapAlphaMaterial::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QNormalDiffuseMapAlphaMaterialPrivate *ritual_ZNK10Qt3DExtras30QNormalDiffuseMapAlphaMaterial6d_funcEv(
    const Qt3DExtras::QNormalDiffuseMapAlphaMaterial *self) {
  return self->d_func();
}

//  a Python function taken by a
//      CuteQt3DExtras_QNormalDiffuseMapAlphaMaterial, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QNormalDiffuseMapAlphaMaterial(
    Qt3DExtras::QNormalDiffuseMapAlphaMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QNormalDiffuseMapAlphaMaterial *>(self)->take(key, call);
}
