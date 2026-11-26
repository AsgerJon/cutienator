//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qparameter.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qparameter.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QParameter that Python can take functions over in. Every Qt3DRender::QParameter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QParameterCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QParameterCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QParameterCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QParameterCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QParameterCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QParameterCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QParameterCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QParameter : public Qt3DRender::QParameter {
public:
  using Qt3DRender::QParameter::QParameter;
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
      CuteQt3DRender_QParameterCall0 call = reinterpret_cast<CuteQt3DRender_QParameterCall0>(taken[0]);
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
      CuteQt3DRender_QParameterCall1 call = reinterpret_cast<CuteQt3DRender_QParameterCall1>(taken[1]);
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
      CuteQt3DRender_QParameterCall2 call = reinterpret_cast<CuteQt3DRender_QParameterCall2>(taken[2]);
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
      CuteQt3DRender_QParameterCall3 call = reinterpret_cast<CuteQt3DRender_QParameterCall3>(taken[3]);
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
      CuteQt3DRender_QParameterCall4 call = reinterpret_cast<CuteQt3DRender_QParameterCall4>(taken[4]);
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
      CuteQt3DRender_QParameterCall5 call = reinterpret_cast<CuteQt3DRender_QParameterCall5>(taken[5]);
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
      CuteQt3DRender_QParameterCall6 call = reinterpret_cast<CuteQt3DRender_QParameterCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QParameter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender10QParameter10metaObjectEv(
    const Qt3DRender::QParameter *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QParameter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender10QParameter11qt_metacastEPKc(
    Qt3DRender::QParameter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QParameter::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender10QParameter11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QParameter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QParameter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender10QParameter2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QParameter::tr(s, c, n));
}

//  Qt3DRender::QParameter::QParameter(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QParameter *ritual_ZN10Qt3DRender10QParameterC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QParameter(parent);
}

//  Qt3DRender::QParameter::QParameter(const QString &name, const QVariant
//      &value, Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QParameter *ritual_ZN10Qt3DRender10QParameterC1ERK7QStringRK8QVariantPN8Qt3DCore5QNodeE(
    const QString *name,
    const QVariant *value,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QParameter(*name, *value, parent);
}

//  Qt3DRender::QParameter::QParameter(const QString &name, QAbstractTexture
//      *texture, Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QParameter *ritual_ZN10Qt3DRender10QParameterC1ERK7QStringPNS_16QAbstractTextureEPN8Qt3DCore5QNodeE(
    const QString *name,
    Qt3DRender::QAbstractTexture *texture,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QParameter(*name, texture, parent);
}

//  Qt3DRender::QParameter::~QParameter()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QParameterD1Ev(Qt3DRender::QParameter *self) {
  delete self;
}

//  QString Qt3DRender::QParameter::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10Qt3DRender10QParameter4nameEv(
    const Qt3DRender::QParameter *self) {
  return new QString(self->name());
}

//  QVariant Qt3DRender::QParameter::value() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10Qt3DRender10QParameter5valueEv(
    const Qt3DRender::QParameter *self) {
  return new QVariant(self->value());
}

//  void Qt3DRender::QParameter::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QParameter7setNameERK7QString(
    Qt3DRender::QParameter *self,
    const QString *name) {
  self->setName(*name);
}

//  void Qt3DRender::QParameter::setValue(const QVariant &dv)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QParameter8setValueERK8QVariant(
    Qt3DRender::QParameter *self,
    const QVariant *dv) {
  self->setValue(*dv);
}

//  void Qt3DRender::QParameter::valueChanged(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QParameter12valueChangedERK8QVariant(
    Qt3DRender::QParameter *self,
    const QVariant *value) {
  self->valueChanged(*value);
}

//  void Qt3DRender::QParameter::nameChanged(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QParameter11nameChangedERK7QString(
    Qt3DRender::QParameter *self,
    const QString *name) {
  self->nameChanged(*name);
}

//  Qt3DRender::QParameter::QParameter(QParameterPrivate &dd, Qt3DCore::QNode
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QParameter *ritual_ZN10Qt3DRender10QParameterC1ERNS_17QParameterPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QParameterPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QParameter(*dd, parent);
}

//  QParameterPrivate *Qt3DRender::QParameter::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QParameterPrivate *ritual_ZN10Qt3DRender10QParameter6d_funcEv(
    Qt3DRender::QParameter *self) {
  return self->d_func();
}

//  const QParameterPrivate *Qt3DRender::QParameter::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QParameterPrivate *ritual_ZNK10Qt3DRender10QParameter6d_funcEv(
    const Qt3DRender::QParameter *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QParameter, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QParameter(
    Qt3DRender::QParameter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QParameter *>(self)->take(key, call);
}
