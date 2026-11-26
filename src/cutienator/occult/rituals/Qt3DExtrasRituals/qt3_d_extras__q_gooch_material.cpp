//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qgoochmaterial.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DExtras/qgoochmaterial.h>
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QGoochMaterial that Python can take functions over in. Every Qt3DExtras::QGoochMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QGoochMaterialCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QGoochMaterialCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QGoochMaterialCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QGoochMaterialCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QGoochMaterialCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QGoochMaterialCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QGoochMaterialCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QGoochMaterial : public Qt3DExtras::QGoochMaterial {
public:
  using Qt3DExtras::QGoochMaterial::QGoochMaterial;
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
      CuteQt3DExtras_QGoochMaterialCall0 call = reinterpret_cast<CuteQt3DExtras_QGoochMaterialCall0>(taken[0]);
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
      CuteQt3DExtras_QGoochMaterialCall1 call = reinterpret_cast<CuteQt3DExtras_QGoochMaterialCall1>(taken[1]);
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
      CuteQt3DExtras_QGoochMaterialCall2 call = reinterpret_cast<CuteQt3DExtras_QGoochMaterialCall2>(taken[2]);
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
      CuteQt3DExtras_QGoochMaterialCall3 call = reinterpret_cast<CuteQt3DExtras_QGoochMaterialCall3>(taken[3]);
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
      CuteQt3DExtras_QGoochMaterialCall4 call = reinterpret_cast<CuteQt3DExtras_QGoochMaterialCall4>(taken[4]);
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
      CuteQt3DExtras_QGoochMaterialCall5 call = reinterpret_cast<CuteQt3DExtras_QGoochMaterialCall5>(taken[5]);
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
      CuteQt3DExtras_QGoochMaterialCall6 call = reinterpret_cast<CuteQt3DExtras_QGoochMaterialCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QGoochMaterial::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras14QGoochMaterial10metaObjectEv(
    const Qt3DExtras::QGoochMaterial *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QGoochMaterial::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras14QGoochMaterial11qt_metacastEPKc(
    Qt3DExtras::QGoochMaterial *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QGoochMaterial::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras14QGoochMaterial11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QGoochMaterial *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QGoochMaterial::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras14QGoochMaterial2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QGoochMaterial::tr(s, c, n));
}

//  Qt3DExtras::QGoochMaterial::QGoochMaterial(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QGoochMaterial *ritual_ZN10Qt3DExtras14QGoochMaterialC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QGoochMaterial(parent);
}

//  Qt3DExtras::QGoochMaterial::~QGoochMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QGoochMaterialD1Ev(
    Qt3DExtras::QGoochMaterial *self) {
  delete self;
}

//  QColor Qt3DExtras::QGoochMaterial::diffuse() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10Qt3DExtras14QGoochMaterial7diffuseEv(
    const Qt3DExtras::QGoochMaterial *self) {
  return new QColor(self->diffuse());
}

//  QColor Qt3DExtras::QGoochMaterial::specular() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10Qt3DExtras14QGoochMaterial8specularEv(
    const Qt3DExtras::QGoochMaterial *self) {
  return new QColor(self->specular());
}

//  QColor Qt3DExtras::QGoochMaterial::cool() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10Qt3DExtras14QGoochMaterial4coolEv(
    const Qt3DExtras::QGoochMaterial *self) {
  return new QColor(self->cool());
}

//  QColor Qt3DExtras::QGoochMaterial::warm() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10Qt3DExtras14QGoochMaterial4warmEv(
    const Qt3DExtras::QGoochMaterial *self) {
  return new QColor(self->warm());
}

//  float Qt3DExtras::QGoochMaterial::alpha() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras14QGoochMaterial5alphaEv(
    const Qt3DExtras::QGoochMaterial *self) {
  return self->alpha();
}

//  float Qt3DExtras::QGoochMaterial::beta() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras14QGoochMaterial4betaEv(
    const Qt3DExtras::QGoochMaterial *self) {
  return self->beta();
}

//  float Qt3DExtras::QGoochMaterial::shininess() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras14QGoochMaterial9shininessEv(
    const Qt3DExtras::QGoochMaterial *self) {
  return self->shininess();
}

//  void Qt3DExtras::QGoochMaterial::setDiffuse(const QColor &diffuse)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QGoochMaterial10setDiffuseERK6QColor(
    Qt3DExtras::QGoochMaterial *self,
    const QColor *diffuse) {
  self->setDiffuse(*diffuse);
}

//  void Qt3DExtras::QGoochMaterial::setSpecular(const QColor &specular)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QGoochMaterial11setSpecularERK6QColor(
    Qt3DExtras::QGoochMaterial *self,
    const QColor *specular) {
  self->setSpecular(*specular);
}

//  void Qt3DExtras::QGoochMaterial::setCool(const QColor &cool)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QGoochMaterial7setCoolERK6QColor(
    Qt3DExtras::QGoochMaterial *self,
    const QColor *cool) {
  self->setCool(*cool);
}

//  void Qt3DExtras::QGoochMaterial::setWarm(const QColor &warm)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QGoochMaterial7setWarmERK6QColor(
    Qt3DExtras::QGoochMaterial *self,
    const QColor *warm) {
  self->setWarm(*warm);
}

//  void Qt3DExtras::QGoochMaterial::setAlpha(float alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QGoochMaterial8setAlphaEf(
    Qt3DExtras::QGoochMaterial *self,
    float alpha) {
  self->setAlpha(alpha);
}

//  void Qt3DExtras::QGoochMaterial::setBeta(float beta)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QGoochMaterial7setBetaEf(
    Qt3DExtras::QGoochMaterial *self,
    float beta) {
  self->setBeta(beta);
}

//  void Qt3DExtras::QGoochMaterial::setShininess(float shininess)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QGoochMaterial12setShininessEf(
    Qt3DExtras::QGoochMaterial *self,
    float shininess) {
  self->setShininess(shininess);
}

//  void Qt3DExtras::QGoochMaterial::diffuseChanged(const QColor &diffuse)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QGoochMaterial14diffuseChangedERK6QColor(
    Qt3DExtras::QGoochMaterial *self,
    const QColor *diffuse) {
  self->diffuseChanged(*diffuse);
}

//  void Qt3DExtras::QGoochMaterial::specularChanged(const QColor &specular)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QGoochMaterial15specularChangedERK6QColor(
    Qt3DExtras::QGoochMaterial *self,
    const QColor *specular) {
  self->specularChanged(*specular);
}

//  void Qt3DExtras::QGoochMaterial::coolChanged(const QColor &cool)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QGoochMaterial11coolChangedERK6QColor(
    Qt3DExtras::QGoochMaterial *self,
    const QColor *cool) {
  self->coolChanged(*cool);
}

//  void Qt3DExtras::QGoochMaterial::warmChanged(const QColor &warm)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QGoochMaterial11warmChangedERK6QColor(
    Qt3DExtras::QGoochMaterial *self,
    const QColor *warm) {
  self->warmChanged(*warm);
}

//  void Qt3DExtras::QGoochMaterial::alphaChanged(float alpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QGoochMaterial12alphaChangedEf(
    Qt3DExtras::QGoochMaterial *self,
    float alpha) {
  self->alphaChanged(alpha);
}

//  void Qt3DExtras::QGoochMaterial::betaChanged(float beta)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QGoochMaterial11betaChangedEf(
    Qt3DExtras::QGoochMaterial *self,
    float beta) {
  self->betaChanged(beta);
}

//  void Qt3DExtras::QGoochMaterial::shininessChanged(float shininess)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras14QGoochMaterial16shininessChangedEf(
    Qt3DExtras::QGoochMaterial *self,
    float shininess) {
  self->shininessChanged(shininess);
}

//  Qt3DExtras::QGoochMaterial::QGoochMaterial(QGoochMaterialPrivate &dd,
//      Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QGoochMaterial *ritual_ZN10Qt3DExtras14QGoochMaterialC1ERNS_21QGoochMaterialPrivateEPN8Qt3DCore5QNodeE(
    Qt3DExtras::QGoochMaterialPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QGoochMaterial(*dd, parent);
}

//  QGoochMaterialPrivate *Qt3DExtras::QGoochMaterial::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QGoochMaterialPrivate *ritual_ZN10Qt3DExtras14QGoochMaterial6d_funcEv(
    Qt3DExtras::QGoochMaterial *self) {
  return self->d_func();
}

//  const QGoochMaterialPrivate *Qt3DExtras::QGoochMaterial::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QGoochMaterialPrivate *ritual_ZNK10Qt3DExtras14QGoochMaterial6d_funcEv(
    const Qt3DExtras::QGoochMaterial *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DExtras_QGoochMaterial, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QGoochMaterial(
    Qt3DExtras::QGoochMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QGoochMaterial *>(self)->take(key, call);
}
