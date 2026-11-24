//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qdiffusespecularmapmaterial.h, Qt 6.12.0. Changes made here
//  are lost.
#include <Qt3DExtras/qdiffusespecularmapmaterial.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QDiffuseSpecularMapMaterial that Python can take functions over in. Every Qt3DExtras::QDiffuseSpecularMapMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QDiffuseSpecularMapMaterialCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QDiffuseSpecularMapMaterialCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QDiffuseSpecularMapMaterialCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QDiffuseSpecularMapMaterialCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QDiffuseSpecularMapMaterialCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QDiffuseSpecularMapMaterialCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QDiffuseSpecularMapMaterialCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QDiffuseSpecularMapMaterial : public Qt3DExtras::QDiffuseSpecularMapMaterial {
public:
  using Qt3DExtras::QDiffuseSpecularMapMaterial::QDiffuseSpecularMapMaterial;
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
      CuteQt3DExtras_QDiffuseSpecularMapMaterialCall0 call = reinterpret_cast<CuteQt3DExtras_QDiffuseSpecularMapMaterialCall0>(taken[0]);
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
      CuteQt3DExtras_QDiffuseSpecularMapMaterialCall1 call = reinterpret_cast<CuteQt3DExtras_QDiffuseSpecularMapMaterialCall1>(taken[1]);
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
      CuteQt3DExtras_QDiffuseSpecularMapMaterialCall2 call = reinterpret_cast<CuteQt3DExtras_QDiffuseSpecularMapMaterialCall2>(taken[2]);
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
      CuteQt3DExtras_QDiffuseSpecularMapMaterialCall3 call = reinterpret_cast<CuteQt3DExtras_QDiffuseSpecularMapMaterialCall3>(taken[3]);
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
      CuteQt3DExtras_QDiffuseSpecularMapMaterialCall4 call = reinterpret_cast<CuteQt3DExtras_QDiffuseSpecularMapMaterialCall4>(taken[4]);
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
      CuteQt3DExtras_QDiffuseSpecularMapMaterialCall5 call = reinterpret_cast<CuteQt3DExtras_QDiffuseSpecularMapMaterialCall5>(taken[5]);
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
      CuteQt3DExtras_QDiffuseSpecularMapMaterialCall6 call = reinterpret_cast<CuteQt3DExtras_QDiffuseSpecularMapMaterialCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QDiffuseSpecularMapMaterial::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras27QDiffuseSpecularMapMaterial10metaObjectEv(
    const Qt3DExtras::QDiffuseSpecularMapMaterial *self) {
  return self->metaObject();
}

//  QString Qt3DExtras::QDiffuseSpecularMapMaterial::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras27QDiffuseSpecularMapMaterial2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QDiffuseSpecularMapMaterial::tr(s, c, n));
}

//  QDiffuseSpecularMapMaterialPrivate
//      *Qt3DExtras::QDiffuseSpecularMapMaterial::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QDiffuseSpecularMapMaterialPrivate *ritual_ZN10Qt3DExtras27QDiffuseSpecularMapMaterial6d_funcEv(
    Qt3DExtras::QDiffuseSpecularMapMaterial *self) {
  return self->d_func();
}

//  const QDiffuseSpecularMapMaterialPrivate
//      *Qt3DExtras::QDiffuseSpecularMapMaterial::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QDiffuseSpecularMapMaterialPrivate *ritual_ZNK10Qt3DExtras27QDiffuseSpecularMapMaterial6d_funcEv(
    const Qt3DExtras::QDiffuseSpecularMapMaterial *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DExtras_QDiffuseSpecularMapMaterial,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QDiffuseSpecularMapMaterial(
    Qt3DExtras::QDiffuseSpecularMapMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QDiffuseSpecularMapMaterial *>(self)->take(key, call);
}
