//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qscissortest.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qscissortest.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QScissorTest that Python can take functions over in. Every Qt3DRender::QScissorTest
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QScissorTestCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QScissorTestCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QScissorTestCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QScissorTestCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QScissorTestCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QScissorTestCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QScissorTestCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QScissorTest : public Qt3DRender::QScissorTest {
public:
  using Qt3DRender::QScissorTest::QScissorTest;
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
      CuteQt3DRender_QScissorTestCall0 call = reinterpret_cast<CuteQt3DRender_QScissorTestCall0>(taken[0]);
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
      CuteQt3DRender_QScissorTestCall1 call = reinterpret_cast<CuteQt3DRender_QScissorTestCall1>(taken[1]);
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
      CuteQt3DRender_QScissorTestCall2 call = reinterpret_cast<CuteQt3DRender_QScissorTestCall2>(taken[2]);
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
      CuteQt3DRender_QScissorTestCall3 call = reinterpret_cast<CuteQt3DRender_QScissorTestCall3>(taken[3]);
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
      CuteQt3DRender_QScissorTestCall4 call = reinterpret_cast<CuteQt3DRender_QScissorTestCall4>(taken[4]);
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
      CuteQt3DRender_QScissorTestCall5 call = reinterpret_cast<CuteQt3DRender_QScissorTestCall5>(taken[5]);
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
      CuteQt3DRender_QScissorTestCall6 call = reinterpret_cast<CuteQt3DRender_QScissorTestCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QScissorTest::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender12QScissorTest10metaObjectEv(
    const Qt3DRender::QScissorTest *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QScissorTest::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender12QScissorTest11qt_metacastEPKc(
    Qt3DRender::QScissorTest *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QScissorTest::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender12QScissorTest11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QScissorTest *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QScissorTest::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender12QScissorTest2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QScissorTest::tr(s, c, n));
}

//  Qt3DRender::QScissorTest::QScissorTest(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QScissorTest *ritual_ZN10Qt3DRender12QScissorTestC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QScissorTest(parent);
}

//  Qt3DRender::QScissorTest::~QScissorTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QScissorTestD1Ev(
    Qt3DRender::QScissorTest *self) {
  delete self;
}

//  int Qt3DRender::QScissorTest::left() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender12QScissorTest4leftEv(
    const Qt3DRender::QScissorTest *self) {
  return self->left();
}

//  int Qt3DRender::QScissorTest::bottom() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender12QScissorTest6bottomEv(
    const Qt3DRender::QScissorTest *self) {
  return self->bottom();
}

//  int Qt3DRender::QScissorTest::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender12QScissorTest5widthEv(
    const Qt3DRender::QScissorTest *self) {
  return self->width();
}

//  int Qt3DRender::QScissorTest::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender12QScissorTest6heightEv(
    const Qt3DRender::QScissorTest *self) {
  return self->height();
}

//  void Qt3DRender::QScissorTest::setLeft(int left)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QScissorTest7setLeftEi(
    Qt3DRender::QScissorTest *self,
    int left) {
  self->setLeft(left);
}

//  void Qt3DRender::QScissorTest::setBottom(int bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QScissorTest9setBottomEi(
    Qt3DRender::QScissorTest *self,
    int bottom) {
  self->setBottom(bottom);
}

//  void Qt3DRender::QScissorTest::setWidth(int width)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QScissorTest8setWidthEi(
    Qt3DRender::QScissorTest *self,
    int width) {
  self->setWidth(width);
}

//  void Qt3DRender::QScissorTest::setHeight(int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QScissorTest9setHeightEi(
    Qt3DRender::QScissorTest *self,
    int height) {
  self->setHeight(height);
}

//  void Qt3DRender::QScissorTest::leftChanged(int left)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QScissorTest11leftChangedEi(
    Qt3DRender::QScissorTest *self,
    int left) {
  self->leftChanged(left);
}

//  void Qt3DRender::QScissorTest::bottomChanged(int bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QScissorTest13bottomChangedEi(
    Qt3DRender::QScissorTest *self,
    int bottom) {
  self->bottomChanged(bottom);
}

//  void Qt3DRender::QScissorTest::widthChanged(int width)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QScissorTest12widthChangedEi(
    Qt3DRender::QScissorTest *self,
    int width) {
  self->widthChanged(width);
}

//  void Qt3DRender::QScissorTest::heightChanged(int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QScissorTest13heightChangedEi(
    Qt3DRender::QScissorTest *self,
    int height) {
  self->heightChanged(height);
}

//  QScissorTestPrivate *Qt3DRender::QScissorTest::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QScissorTestPrivate *ritual_ZN10Qt3DRender12QScissorTest6d_funcEv(
    Qt3DRender::QScissorTest *self) {
  return self->d_func();
}

//  const QScissorTestPrivate *Qt3DRender::QScissorTest::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QScissorTestPrivate *ritual_ZNK10Qt3DRender12QScissorTest6d_funcEv(
    const Qt3DRender::QScissorTest *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QScissorTest, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QScissorTest(
    Qt3DRender::QScissorTest *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QScissorTest *>(self)->take(key, call);
}
