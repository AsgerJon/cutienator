//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qcullface.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qcullface.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QCullFace that Python can take functions over in. Every Qt3DRender::QCullFace
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QCullFaceCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QCullFaceCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QCullFaceCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QCullFaceCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QCullFaceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QCullFaceCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QCullFaceCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QCullFace : public Qt3DRender::QCullFace {
public:
  using Qt3DRender::QCullFace::QCullFace;
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
      CuteQt3DRender_QCullFaceCall0 call = reinterpret_cast<CuteQt3DRender_QCullFaceCall0>(taken[0]);
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
      CuteQt3DRender_QCullFaceCall1 call = reinterpret_cast<CuteQt3DRender_QCullFaceCall1>(taken[1]);
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
      CuteQt3DRender_QCullFaceCall2 call = reinterpret_cast<CuteQt3DRender_QCullFaceCall2>(taken[2]);
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
      CuteQt3DRender_QCullFaceCall3 call = reinterpret_cast<CuteQt3DRender_QCullFaceCall3>(taken[3]);
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
      CuteQt3DRender_QCullFaceCall4 call = reinterpret_cast<CuteQt3DRender_QCullFaceCall4>(taken[4]);
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
      CuteQt3DRender_QCullFaceCall5 call = reinterpret_cast<CuteQt3DRender_QCullFaceCall5>(taken[5]);
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
      CuteQt3DRender_QCullFaceCall6 call = reinterpret_cast<CuteQt3DRender_QCullFaceCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QCullFace::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender9QCullFace10metaObjectEv(
    const Qt3DRender::QCullFace *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QCullFace::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender9QCullFace11qt_metacastEPKc(
    Qt3DRender::QCullFace *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QCullFace::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender9QCullFace11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QCullFace *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QCullFace::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender9QCullFace2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QCullFace::tr(s, c, n));
}

//  Qt3DRender::QCullFace::QCullFace(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QCullFace *ritual_ZN10Qt3DRender9QCullFaceC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QCullFace(parent);
}

//  Qt3DRender::QCullFace::~QCullFace()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender9QCullFaceD1Ev(Qt3DRender::QCullFace *self) {
  delete self;
}

//  CullingMode Qt3DRender::QCullFace::mode() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QCullFace::CullingMode ritual_ZNK10Qt3DRender9QCullFace4modeEv(
    const Qt3DRender::QCullFace *self) {
  return self->mode();
}

//  void Qt3DRender::QCullFace::setMode(CullingMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender9QCullFace7setModeENS0_11CullingModeE(
    Qt3DRender::QCullFace *self,
    Qt3DRender::QCullFace::CullingMode mode) {
  self->setMode(mode);
}

//  void Qt3DRender::QCullFace::modeChanged(CullingMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender9QCullFace11modeChangedENS0_11CullingModeE(
    Qt3DRender::QCullFace *self,
    Qt3DRender::QCullFace::CullingMode mode) {
  self->modeChanged(mode);
}

//  QCullFacePrivate *Qt3DRender::QCullFace::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QCullFacePrivate *ritual_ZN10Qt3DRender9QCullFace6d_funcEv(
    Qt3DRender::QCullFace *self) {
  return self->d_func();
}

//  const QCullFacePrivate *Qt3DRender::QCullFace::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QCullFacePrivate *ritual_ZNK10Qt3DRender9QCullFace6d_funcEv(
    const Qt3DRender::QCullFace *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QCullFace, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QCullFace(
    Qt3DRender::QCullFace *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QCullFace *>(self)->take(key, call);
}
