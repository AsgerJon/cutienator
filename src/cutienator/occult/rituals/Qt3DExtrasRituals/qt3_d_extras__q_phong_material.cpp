//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qphongmaterial.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DExtras/qphongmaterial.h>
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QPhongMaterial that Python can take functions over in. Every Qt3DExtras::QPhongMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QPhongMaterialCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QPhongMaterialCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QPhongMaterialCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QPhongMaterialCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QPhongMaterialCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QPhongMaterialCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QPhongMaterialCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QPhongMaterial : public Qt3DExtras::QPhongMaterial {
public:
  using Qt3DExtras::QPhongMaterial::QPhongMaterial;
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
      CuteQt3DExtras_QPhongMaterialCall0 call = reinterpret_cast<CuteQt3DExtras_QPhongMaterialCall0>(taken[0]);
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
      CuteQt3DExtras_QPhongMaterialCall1 call = reinterpret_cast<CuteQt3DExtras_QPhongMaterialCall1>(taken[1]);
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
      CuteQt3DExtras_QPhongMaterialCall2 call = reinterpret_cast<CuteQt3DExtras_QPhongMaterialCall2>(taken[2]);
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
      CuteQt3DExtras_QPhongMaterialCall3 call = reinterpret_cast<CuteQt3DExtras_QPhongMaterialCall3>(taken[3]);
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
      CuteQt3DExtras_QPhongMaterialCall4 call = reinterpret_cast<CuteQt3DExtras_QPhongMaterialCall4>(taken[4]);
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
      CuteQt3DExtras_QPhongMaterialCall5 call = reinterpret_cast<CuteQt3DExtras_QPhongMaterialCall5>(taken[5]);
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
      CuteQt3DExtras_QPhongMaterialCall6 call = reinterpret_cast<CuteQt3DExtras_QPhongMaterialCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QPhongMaterial::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras14QPhongMaterial10metaObjectEv(
    const Qt3DExtras::QPhongMaterial *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QPhongMaterial::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras14QPhongMaterial11qt_metacastEPKc(
    Qt3DExtras::QPhongMaterial *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QPhongMaterial::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras14QPhongMaterial11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QPhongMaterial *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QPhongMaterial::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras14QPhongMaterial2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QPhongMaterial::tr(s, c, n));
}

//  Qt3DExtras::QPhongMaterial::QPhongMaterial(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QPhongMaterial *ritual_ZN10Qt3DExtras14QPhongMaterialC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QPhongMaterial(parent);
}

//  Qt3DExtras::QPhongMaterial::~QPhongMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QPhongMaterialD1Ev(
    Qt3DExtras::QPhongMaterial *self) {
  delete self;
}

//  QColor Qt3DExtras::QPhongMaterial::ambient() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10Qt3DExtras14QPhongMaterial7ambientEv(
    const Qt3DExtras::QPhongMaterial *self) {
  return new QColor(self->ambient());
}

//  QColor Qt3DExtras::QPhongMaterial::diffuse() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10Qt3DExtras14QPhongMaterial7diffuseEv(
    const Qt3DExtras::QPhongMaterial *self) {
  return new QColor(self->diffuse());
}

//  QColor Qt3DExtras::QPhongMaterial::specular() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10Qt3DExtras14QPhongMaterial8specularEv(
    const Qt3DExtras::QPhongMaterial *self) {
  return new QColor(self->specular());
}

//  float Qt3DExtras::QPhongMaterial::shininess() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras14QPhongMaterial9shininessEv(
    const Qt3DExtras::QPhongMaterial *self) {
  return self->shininess();
}

//  void Qt3DExtras::QPhongMaterial::setAmbient(const QColor &ambient)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QPhongMaterial10setAmbientERK6QColor(
    Qt3DExtras::QPhongMaterial *self,
    const QColor *ambient) {
  self->setAmbient(*ambient);
}

//  void Qt3DExtras::QPhongMaterial::setDiffuse(const QColor &diffuse)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QPhongMaterial10setDiffuseERK6QColor(
    Qt3DExtras::QPhongMaterial *self,
    const QColor *diffuse) {
  self->setDiffuse(*diffuse);
}

//  void Qt3DExtras::QPhongMaterial::setSpecular(const QColor &specular)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QPhongMaterial11setSpecularERK6QColor(
    Qt3DExtras::QPhongMaterial *self,
    const QColor *specular) {
  self->setSpecular(*specular);
}

//  void Qt3DExtras::QPhongMaterial::setShininess(float shininess)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QPhongMaterial12setShininessEf(
    Qt3DExtras::QPhongMaterial *self,
    float shininess) {
  self->setShininess(shininess);
}

//  void Qt3DExtras::QPhongMaterial::ambientChanged(const QColor &ambient)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QPhongMaterial14ambientChangedERK6QColor(
    Qt3DExtras::QPhongMaterial *self,
    const QColor *ambient) {
  self->ambientChanged(*ambient);
}

//  void Qt3DExtras::QPhongMaterial::diffuseChanged(const QColor &diffuse)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QPhongMaterial14diffuseChangedERK6QColor(
    Qt3DExtras::QPhongMaterial *self,
    const QColor *diffuse) {
  self->diffuseChanged(*diffuse);
}

//  void Qt3DExtras::QPhongMaterial::specularChanged(const QColor &specular)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QPhongMaterial15specularChangedERK6QColor(
    Qt3DExtras::QPhongMaterial *self,
    const QColor *specular) {
  self->specularChanged(*specular);
}

//  void Qt3DExtras::QPhongMaterial::shininessChanged(float shininess)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QPhongMaterial16shininessChangedEf(
    Qt3DExtras::QPhongMaterial *self,
    float shininess) {
  self->shininessChanged(shininess);
}

//  QPhongMaterialPrivate *Qt3DExtras::QPhongMaterial::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QPhongMaterialPrivate *ritual_ZN10Qt3DExtras14QPhongMaterial6d_funcEv(
    Qt3DExtras::QPhongMaterial *self) {
  return self->d_func();
}

//  const QPhongMaterialPrivate *Qt3DExtras::QPhongMaterial::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QPhongMaterialPrivate *ritual_ZNK10Qt3DExtras14QPhongMaterial6d_funcEv(
    const Qt3DExtras::QPhongMaterial *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DExtras_QPhongMaterial, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QPhongMaterial(
    Qt3DExtras::QPhongMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QPhongMaterial *>(self)->take(key, call);
}
