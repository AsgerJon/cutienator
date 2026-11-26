//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qmaterial.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qmaterial.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>
#include <Qt3DRender/Qt3DRender>

//  A Qt3DRender::QMaterial that Python can take functions over in. Every Qt3DRender::QMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QMaterialCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QMaterialCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QMaterialCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QMaterialCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QMaterialCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QMaterialCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QMaterialCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QMaterial : public Qt3DRender::QMaterial {
public:
  using Qt3DRender::QMaterial::QMaterial;
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
      CuteQt3DRender_QMaterialCall0 call = reinterpret_cast<CuteQt3DRender_QMaterialCall0>(taken[0]);
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
      CuteQt3DRender_QMaterialCall1 call = reinterpret_cast<CuteQt3DRender_QMaterialCall1>(taken[1]);
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
      CuteQt3DRender_QMaterialCall2 call = reinterpret_cast<CuteQt3DRender_QMaterialCall2>(taken[2]);
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
      CuteQt3DRender_QMaterialCall3 call = reinterpret_cast<CuteQt3DRender_QMaterialCall3>(taken[3]);
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
      CuteQt3DRender_QMaterialCall4 call = reinterpret_cast<CuteQt3DRender_QMaterialCall4>(taken[4]);
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
      CuteQt3DRender_QMaterialCall5 call = reinterpret_cast<CuteQt3DRender_QMaterialCall5>(taken[5]);
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
      CuteQt3DRender_QMaterialCall6 call = reinterpret_cast<CuteQt3DRender_QMaterialCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QMaterial::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender9QMaterial10metaObjectEv(
    const Qt3DRender::QMaterial *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QMaterial::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender9QMaterial11qt_metacastEPKc(
    Qt3DRender::QMaterial *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QMaterial::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender9QMaterial11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QMaterial *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QMaterial::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender9QMaterial2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QMaterial::tr(s, c, n));
}

//  Qt3DRender::QMaterial::QMaterial(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QMaterial *ritual_ZN10Qt3DRender9QMaterialC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QMaterial(parent);
}

//  Qt3DRender::QMaterial::~QMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender9QMaterialD1Ev(Qt3DRender::QMaterial *self) {
  delete self;
}

//  QEffect *Qt3DRender::QMaterial::effect() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QEffect *ritual_ZNK10Qt3DRender9QMaterial6effectEv(
    const Qt3DRender::QMaterial *self) {
  return self->effect();
}

//  void Qt3DRender::QMaterial::addParameter(QParameter *parameter)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender9QMaterial12addParameterEPNS_10QParameterE(
    Qt3DRender::QMaterial *self,
    Qt3DRender::QParameter *parameter) {
  self->addParameter(parameter);
}

//  void Qt3DRender::QMaterial::removeParameter(QParameter *parameter)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender9QMaterial15removeParameterEPNS_10QParameterE(
    Qt3DRender::QMaterial *self,
    Qt3DRender::QParameter *parameter) {
  self->removeParameter(parameter);
}

//  QList<QParameter *> Qt3DRender::QMaterial::parameters() const
extern "C" Q_DECL_EXPORT
QList<Qt3DRender::QParameter *> *ritual_ZNK10Qt3DRender9QMaterial10parametersEv(
    const Qt3DRender::QMaterial *self) {
  return new QList<Qt3DRender::QParameter *>(self->parameters());
}

//  void Qt3DRender::QMaterial::setEffect(QEffect *effect)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender9QMaterial9setEffectEPNS_7QEffectE(
    Qt3DRender::QMaterial *self,
    Qt3DRender::QEffect *effect) {
  self->setEffect(effect);
}

//  void Qt3DRender::QMaterial::effectChanged(QEffect *effect)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender9QMaterial13effectChangedEPNS_7QEffectE(
    Qt3DRender::QMaterial *self,
    Qt3DRender::QEffect *effect) {
  self->effectChanged(effect);
}

//  Qt3DRender::QMaterial::QMaterial(QMaterialPrivate &dd, Qt3DCore::QNode
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QMaterial *ritual_ZN10Qt3DRender9QMaterialC1ERNS_16QMaterialPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QMaterialPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QMaterial(*dd, parent);
}

//  QMaterialPrivate *Qt3DRender::QMaterial::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QMaterialPrivate *ritual_ZN10Qt3DRender9QMaterial6d_funcEv(
    Qt3DRender::QMaterial *self) {
  return self->d_func();
}

//  const QMaterialPrivate *Qt3DRender::QMaterial::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QMaterialPrivate *ritual_ZNK10Qt3DRender9QMaterial6d_funcEv(
    const Qt3DRender::QMaterial *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QMaterial, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QMaterial(
    Qt3DRender::QMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QMaterial *>(self)->take(key, call);
}

//  a QList<Qt3DRender::QParameter *> a ritual of Qt3DRender::QMaterial gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QMaterial__QList_Qt3DRender_QParameter(
    QList<Qt3DRender::QParameter *> *self) {
  delete self;
}
