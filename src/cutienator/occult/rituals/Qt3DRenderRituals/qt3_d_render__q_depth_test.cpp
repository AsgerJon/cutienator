//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qdepthtest.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qdepthtest.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QDepthTest that Python can take functions over in. Every Qt3DRender::QDepthTest
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QDepthTestCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QDepthTestCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QDepthTestCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QDepthTestCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QDepthTestCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QDepthTestCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QDepthTestCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QDepthTest : public Qt3DRender::QDepthTest {
public:
  using Qt3DRender::QDepthTest::QDepthTest;
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
      CuteQt3DRender_QDepthTestCall0 call = reinterpret_cast<CuteQt3DRender_QDepthTestCall0>(taken[0]);
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
      CuteQt3DRender_QDepthTestCall1 call = reinterpret_cast<CuteQt3DRender_QDepthTestCall1>(taken[1]);
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
      CuteQt3DRender_QDepthTestCall2 call = reinterpret_cast<CuteQt3DRender_QDepthTestCall2>(taken[2]);
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
      CuteQt3DRender_QDepthTestCall3 call = reinterpret_cast<CuteQt3DRender_QDepthTestCall3>(taken[3]);
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
      CuteQt3DRender_QDepthTestCall4 call = reinterpret_cast<CuteQt3DRender_QDepthTestCall4>(taken[4]);
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
      CuteQt3DRender_QDepthTestCall5 call = reinterpret_cast<CuteQt3DRender_QDepthTestCall5>(taken[5]);
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
      CuteQt3DRender_QDepthTestCall6 call = reinterpret_cast<CuteQt3DRender_QDepthTestCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QDepthTest::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender10QDepthTest10metaObjectEv(
    const Qt3DRender::QDepthTest *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QDepthTest::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender10QDepthTest11qt_metacastEPKc(
    Qt3DRender::QDepthTest *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QDepthTest::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender10QDepthTest11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QDepthTest *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QDepthTest::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender10QDepthTest2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QDepthTest::tr(s, c, n));
}

//  Qt3DRender::QDepthTest::QDepthTest(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QDepthTest *ritual_ZN10Qt3DRender10QDepthTestC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QDepthTest(parent);
}

//  Qt3DRender::QDepthTest::~QDepthTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QDepthTestD1Ev(Qt3DRender::QDepthTest *self) {
  delete self;
}

//  DepthFunction Qt3DRender::QDepthTest::depthFunction() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QDepthTest::DepthFunction ritual_ZNK10Qt3DRender10QDepthTest13depthFunctionEv(
    const Qt3DRender::QDepthTest *self) {
  return self->depthFunction();
}

//  void Qt3DRender::QDepthTest::setDepthFunction(DepthFunction
//      depthFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QDepthTest16setDepthFunctionENS0_13DepthFunctionE(
    Qt3DRender::QDepthTest *self,
    Qt3DRender::QDepthTest::DepthFunction depthFunction) {
  self->setDepthFunction(depthFunction);
}

//  void Qt3DRender::QDepthTest::depthFunctionChanged(DepthFunction
//      depthFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QDepthTest20depthFunctionChangedENS0_13DepthFunctionE(
    Qt3DRender::QDepthTest *self,
    Qt3DRender::QDepthTest::DepthFunction depthFunction) {
  self->depthFunctionChanged(depthFunction);
}

//  QDepthTestPrivate *Qt3DRender::QDepthTest::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QDepthTestPrivate *ritual_ZN10Qt3DRender10QDepthTest6d_funcEv(
    Qt3DRender::QDepthTest *self) {
  return self->d_func();
}

//  const QDepthTestPrivate *Qt3DRender::QDepthTest::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QDepthTestPrivate *ritual_ZNK10Qt3DRender10QDepthTest6d_funcEv(
    const Qt3DRender::QDepthTest *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QDepthTest, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QDepthTest(
    Qt3DRender::QDepthTest *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QDepthTest *>(self)->take(key, call);
}
