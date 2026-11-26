//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qshaderdata.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qshaderdata.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <Qt3DRender/Qt3DRender>

//  A Qt3DRender::QShaderData that Python can take functions over in. Every Qt3DRender::QShaderData
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QShaderDataCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QShaderDataCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QShaderDataCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QShaderDataCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QShaderDataCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QShaderDataCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QShaderDataCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QShaderData : public Qt3DRender::QShaderData {
public:
  using Qt3DRender::QShaderData::QShaderData;
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
  //  bool Qt3DRender::QShaderData::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_QShaderDataCall0 call = reinterpret_cast<CuteQt3DRender_QShaderDataCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return Qt3DRender::QShaderData::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QShaderDataCall1 call = reinterpret_cast<CuteQt3DRender_QShaderDataCall1>(taken[1]);
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
      CuteQt3DRender_QShaderDataCall2 call = reinterpret_cast<CuteQt3DRender_QShaderDataCall2>(taken[2]);
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
      CuteQt3DRender_QShaderDataCall3 call = reinterpret_cast<CuteQt3DRender_QShaderDataCall3>(taken[3]);
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
      CuteQt3DRender_QShaderDataCall4 call = reinterpret_cast<CuteQt3DRender_QShaderDataCall4>(taken[4]);
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
      CuteQt3DRender_QShaderDataCall5 call = reinterpret_cast<CuteQt3DRender_QShaderDataCall5>(taken[5]);
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
      CuteQt3DRender_QShaderDataCall6 call = reinterpret_cast<CuteQt3DRender_QShaderDataCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QShaderData::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender11QShaderData10metaObjectEv(
    const Qt3DRender::QShaderData *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QShaderData::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender11QShaderData11qt_metacastEPKc(
    Qt3DRender::QShaderData *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QShaderData::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender11QShaderData11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QShaderData *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QShaderData::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender11QShaderData2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QShaderData::tr(s, c, n));
}

//  Qt3DRender::QShaderData::QShaderData(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderData *ritual_ZN10Qt3DRender11QShaderDataC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QShaderData(parent);
}

//  Qt3DRender::QShaderData::~QShaderData()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QShaderDataD1Ev(Qt3DRender::QShaderData *self) {
  delete self;
}

//  PropertyReaderInterfacePtr Qt3DRender::QShaderData::propertyReader()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::PropertyReaderInterfacePtr *ritual_ZNK10Qt3DRender11QShaderData14propertyReaderEv(
    const Qt3DRender::QShaderData *self) {
  return new Qt3DRender::PropertyReaderInterfacePtr(self->propertyReader());
}

//  bool Qt3DRender::QShaderData::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10Qt3DRender11QShaderData5eventEP6QEvent(
    Qt3DRender::QShaderData *self,
    QEvent *event) {
  return self->event(event);
}

//  Qt3DRender::QShaderData::QShaderData(QShaderDataPrivate &dd,
//      Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderData *ritual_ZN10Qt3DRender11QShaderDataC1ERNS_18QShaderDataPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QShaderDataPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QShaderData(*dd, parent);
}

//  QShaderDataPrivate *Qt3DRender::QShaderData::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderDataPrivate *ritual_ZN10Qt3DRender11QShaderData6d_funcEv(
    Qt3DRender::QShaderData *self) {
  return self->d_func();
}

//  const QShaderDataPrivate *Qt3DRender::QShaderData::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QShaderDataPrivate *ritual_ZNK10Qt3DRender11QShaderData6d_funcEv(
    const Qt3DRender::QShaderData *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QShaderData, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QShaderData(
    Qt3DRender::QShaderData *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QShaderData *>(self)->take(key, call);
}

//  bool Qt3DRender::QShaderData::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10Qt3DRender11QShaderData5eventEP6QEvent(
    Qt3DRender::QShaderData *self,
    QEvent *event) {
  return self->Qt3DRender::QShaderData::event(event);
}

//  a Qt3DRender::PropertyReaderInterfacePtr a ritual of
//      Qt3DRender::QShaderData gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QShaderData__Qt3DRender_PropertyReaderInterfacePtr(
    Qt3DRender::PropertyReaderInterfacePtr *self) {
  delete self;
}
