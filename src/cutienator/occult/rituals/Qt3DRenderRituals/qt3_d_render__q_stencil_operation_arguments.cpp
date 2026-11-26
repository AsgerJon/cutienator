//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qstenciloperationarguments.h, Qt 6.12.0. Changes made here are
//  lost.
#include <Qt3DRender/qstenciloperationarguments.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QStencilOperationArguments that Python can take functions over in. Every Qt3DRender::QStencilOperationArguments
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QStencilOperationArgumentsCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QStencilOperationArgumentsCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QStencilOperationArgumentsCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QStencilOperationArgumentsCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QStencilOperationArgumentsCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QStencilOperationArgumentsCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QStencilOperationArgumentsCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QStencilOperationArguments : public Qt3DRender::QStencilOperationArguments {
public:
  using Qt3DRender::QStencilOperationArguments::QStencilOperationArguments;
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
      CuteQt3DRender_QStencilOperationArgumentsCall0 call = reinterpret_cast<CuteQt3DRender_QStencilOperationArgumentsCall0>(taken[0]);
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
      CuteQt3DRender_QStencilOperationArgumentsCall1 call = reinterpret_cast<CuteQt3DRender_QStencilOperationArgumentsCall1>(taken[1]);
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
      CuteQt3DRender_QStencilOperationArgumentsCall2 call = reinterpret_cast<CuteQt3DRender_QStencilOperationArgumentsCall2>(taken[2]);
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
      CuteQt3DRender_QStencilOperationArgumentsCall3 call = reinterpret_cast<CuteQt3DRender_QStencilOperationArgumentsCall3>(taken[3]);
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
      CuteQt3DRender_QStencilOperationArgumentsCall4 call = reinterpret_cast<CuteQt3DRender_QStencilOperationArgumentsCall4>(taken[4]);
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
      CuteQt3DRender_QStencilOperationArgumentsCall5 call = reinterpret_cast<CuteQt3DRender_QStencilOperationArgumentsCall5>(taken[5]);
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
      CuteQt3DRender_QStencilOperationArgumentsCall6 call = reinterpret_cast<CuteQt3DRender_QStencilOperationArgumentsCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QStencilOperationArguments::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender26QStencilOperationArguments10metaObjectEv(
    const Qt3DRender::QStencilOperationArguments *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QStencilOperationArguments::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender26QStencilOperationArguments11qt_metacastEPKc(
    Qt3DRender::QStencilOperationArguments *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QStencilOperationArguments::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender26QStencilOperationArguments11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QStencilOperationArguments *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QStencilOperationArguments::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender26QStencilOperationArguments2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QStencilOperationArguments::tr(s, c, n));
}

//  Qt3DRender::QStencilOperationArguments::~QStencilOperationArguments()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender26QStencilOperationArgumentsD1Ev(
    Qt3DRender::QStencilOperationArguments *self) {
  delete self;
}

//  FaceMode Qt3DRender::QStencilOperationArguments::faceMode() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QStencilOperationArguments::FaceMode ritual_ZNK10Qt3DRender26QStencilOperationArguments8faceModeEv(
    const Qt3DRender::QStencilOperationArguments *self) {
  return self->faceMode();
}

//  Operation
//      Qt3DRender::QStencilOperationArguments::stencilTestFailureOperation()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::QStencilOperationArguments::Operation ritual_ZNK10Qt3DRender26QStencilOperationArguments27stencilTestFailureOperationEv(
    const Qt3DRender::QStencilOperationArguments *self) {
  return self->stencilTestFailureOperation();
}

//  Operation
//      Qt3DRender::QStencilOperationArguments::depthTestFailureOperation()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::QStencilOperationArguments::Operation ritual_ZNK10Qt3DRender26QStencilOperationArguments25depthTestFailureOperationEv(
    const Qt3DRender::QStencilOperationArguments *self) {
  return self->depthTestFailureOperation();
}

//  Operation Qt3DRender::QStencilOperationArguments::allTestsPassOperation()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::QStencilOperationArguments::Operation ritual_ZNK10Qt3DRender26QStencilOperationArguments21allTestsPassOperationEv(
    const Qt3DRender::QStencilOperationArguments *self) {
  return self->allTestsPassOperation();
}

//  void Qt3DRender::QStencilOperationArguments::setStencilTestFailureOperati
//      on(Operation operation)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender26QStencilOperationArguments30setStencilTestFailureOperationENS0_9OperationE(
    Qt3DRender::QStencilOperationArguments *self,
    Qt3DRender::QStencilOperationArguments::Operation operation) {
  self->setStencilTestFailureOperation(operation);
}

//  void Qt3DRender::QStencilOperationArguments::setDepthTestFailureOperation
//      (Operation operation)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender26QStencilOperationArguments28setDepthTestFailureOperationENS0_9OperationE(
    Qt3DRender::QStencilOperationArguments *self,
    Qt3DRender::QStencilOperationArguments::Operation operation) {
  self->setDepthTestFailureOperation(operation);
}

//  void Qt3DRender::QStencilOperationArguments::setAllTestsPassOperation(Ope
//      ration operation)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender26QStencilOperationArguments24setAllTestsPassOperationENS0_9OperationE(
    Qt3DRender::QStencilOperationArguments *self,
    Qt3DRender::QStencilOperationArguments::Operation operation) {
  self->setAllTestsPassOperation(operation);
}

//  void Qt3DRender::QStencilOperationArguments::stencilTestFailureOperationC
//      hanged(Operation stencilFail)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender26QStencilOperationArguments34stencilTestFailureOperationChangedENS0_9OperationE(
    Qt3DRender::QStencilOperationArguments *self,
    Qt3DRender::QStencilOperationArguments::Operation stencilFail) {
  self->stencilTestFailureOperationChanged(stencilFail);
}

//  void Qt3DRender::QStencilOperationArguments::depthTestFailureOperationCha
//      nged(Operation depthFail)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender26QStencilOperationArguments32depthTestFailureOperationChangedENS0_9OperationE(
    Qt3DRender::QStencilOperationArguments *self,
    Qt3DRender::QStencilOperationArguments::Operation depthFail) {
  self->depthTestFailureOperationChanged(depthFail);
}

//  void Qt3DRender::QStencilOperationArguments::allTestsPassOperationChanged
//      (Operation stencilDepthPass)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender26QStencilOperationArguments28allTestsPassOperationChangedENS0_9OperationE(
    Qt3DRender::QStencilOperationArguments *self,
    Qt3DRender::QStencilOperationArguments::Operation stencilDepthPass) {
  self->allTestsPassOperationChanged(stencilDepthPass);
}

//  void Qt3DRender::QStencilOperationArguments::faceModeChanged(FaceMode
//      faceMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender26QStencilOperationArguments15faceModeChangedENS0_8FaceModeE(
    Qt3DRender::QStencilOperationArguments *self,
    Qt3DRender::QStencilOperationArguments::FaceMode faceMode) {
  self->faceModeChanged(faceMode);
}

//  Qt3DRender::QStencilOperationArguments::QStencilOperationArguments(FaceMo
//      de mode, QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QStencilOperationArguments *ritual_ZN10Qt3DRender26QStencilOperationArgumentsC1ENS0_8FaceModeEP7QObject(
    Qt3DRender::QStencilOperationArguments::FaceMode mode,
    QObject *parent) {
  return new CuteQt3DRender_QStencilOperationArguments(mode, parent);
}

//  QStencilOperationArgumentsPrivate
//      *Qt3DRender::QStencilOperationArguments::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QStencilOperationArgumentsPrivate *ritual_ZN10Qt3DRender26QStencilOperationArguments6d_funcEv(
    Qt3DRender::QStencilOperationArguments *self) {
  return self->d_func();
}

//  const QStencilOperationArgumentsPrivate
//      *Qt3DRender::QStencilOperationArguments::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QStencilOperationArgumentsPrivate *ritual_ZNK10Qt3DRender26QStencilOperationArguments6d_funcEv(
    const Qt3DRender::QStencilOperationArguments *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QStencilOperationArguments,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QStencilOperationArguments(
    Qt3DRender::QStencilOperationArguments *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QStencilOperationArguments *>(self)->take(key, call);
}
