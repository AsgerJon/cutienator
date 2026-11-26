//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qalphatest.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qalphatest.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QAlphaTest that Python can take functions over in. Every Qt3DRender::QAlphaTest
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QAlphaTestCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QAlphaTestCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QAlphaTestCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QAlphaTestCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QAlphaTestCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QAlphaTestCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QAlphaTestCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QAlphaTest : public Qt3DRender::QAlphaTest {
public:
  using Qt3DRender::QAlphaTest::QAlphaTest;
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
      CuteQt3DRender_QAlphaTestCall0 call = reinterpret_cast<CuteQt3DRender_QAlphaTestCall0>(taken[0]);
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
      CuteQt3DRender_QAlphaTestCall1 call = reinterpret_cast<CuteQt3DRender_QAlphaTestCall1>(taken[1]);
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
      CuteQt3DRender_QAlphaTestCall2 call = reinterpret_cast<CuteQt3DRender_QAlphaTestCall2>(taken[2]);
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
      CuteQt3DRender_QAlphaTestCall3 call = reinterpret_cast<CuteQt3DRender_QAlphaTestCall3>(taken[3]);
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
      CuteQt3DRender_QAlphaTestCall4 call = reinterpret_cast<CuteQt3DRender_QAlphaTestCall4>(taken[4]);
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
      CuteQt3DRender_QAlphaTestCall5 call = reinterpret_cast<CuteQt3DRender_QAlphaTestCall5>(taken[5]);
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
      CuteQt3DRender_QAlphaTestCall6 call = reinterpret_cast<CuteQt3DRender_QAlphaTestCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QAlphaTest::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender10QAlphaTest10metaObjectEv(
    const Qt3DRender::QAlphaTest *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QAlphaTest::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender10QAlphaTest11qt_metacastEPKc(
    Qt3DRender::QAlphaTest *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QAlphaTest::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender10QAlphaTest11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QAlphaTest *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QAlphaTest::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender10QAlphaTest2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QAlphaTest::tr(s, c, n));
}

//  Qt3DRender::QAlphaTest::QAlphaTest(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QAlphaTest *ritual_ZN10Qt3DRender10QAlphaTestC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QAlphaTest(parent);
}

//  Qt3DRender::QAlphaTest::~QAlphaTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QAlphaTestD1Ev(Qt3DRender::QAlphaTest *self) {
  delete self;
}

//  AlphaFunction Qt3DRender::QAlphaTest::alphaFunction() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAlphaTest::AlphaFunction ritual_ZNK10Qt3DRender10QAlphaTest13alphaFunctionEv(
    const Qt3DRender::QAlphaTest *self) {
  return self->alphaFunction();
}

//  float Qt3DRender::QAlphaTest::referenceValue() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender10QAlphaTest14referenceValueEv(
    const Qt3DRender::QAlphaTest *self) {
  return self->referenceValue();
}

//  void Qt3DRender::QAlphaTest::setAlphaFunction(AlphaFunction
//      alphaFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QAlphaTest16setAlphaFunctionENS0_13AlphaFunctionE(
    Qt3DRender::QAlphaTest *self,
    Qt3DRender::QAlphaTest::AlphaFunction alphaFunction) {
  self->setAlphaFunction(alphaFunction);
}

//  void Qt3DRender::QAlphaTest::setReferenceValue(float referenceValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QAlphaTest17setReferenceValueEf(
    Qt3DRender::QAlphaTest *self,
    float referenceValue) {
  self->setReferenceValue(referenceValue);
}

//  void Qt3DRender::QAlphaTest::alphaFunctionChanged(AlphaFunction
//      alphaFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QAlphaTest20alphaFunctionChangedENS0_13AlphaFunctionE(
    Qt3DRender::QAlphaTest *self,
    Qt3DRender::QAlphaTest::AlphaFunction alphaFunction) {
  self->alphaFunctionChanged(alphaFunction);
}

//  void Qt3DRender::QAlphaTest::referenceValueChanged(float referenceValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QAlphaTest21referenceValueChangedEf(
    Qt3DRender::QAlphaTest *self,
    float referenceValue) {
  self->referenceValueChanged(referenceValue);
}

//  QAlphaTestPrivate *Qt3DRender::QAlphaTest::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QAlphaTestPrivate *ritual_ZN10Qt3DRender10QAlphaTest6d_funcEv(
    Qt3DRender::QAlphaTest *self) {
  return self->d_func();
}

//  const QAlphaTestPrivate *Qt3DRender::QAlphaTest::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QAlphaTestPrivate *ritual_ZNK10Qt3DRender10QAlphaTest6d_funcEv(
    const Qt3DRender::QAlphaTest *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QAlphaTest, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QAlphaTest(
    Qt3DRender::QAlphaTest *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QAlphaTest *>(self)->take(key, call);
}
