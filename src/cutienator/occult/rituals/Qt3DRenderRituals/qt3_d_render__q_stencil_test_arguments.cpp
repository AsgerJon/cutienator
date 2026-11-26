//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qstenciltestarguments.h, Qt 6.12.0. Changes made here are
//  lost.
#include <Qt3DRender/qstenciltestarguments.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QStencilTestArguments that Python can take functions over in. Every Qt3DRender::QStencilTestArguments
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QStencilTestArgumentsCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QStencilTestArgumentsCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QStencilTestArgumentsCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QStencilTestArgumentsCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QStencilTestArgumentsCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QStencilTestArgumentsCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QStencilTestArgumentsCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QStencilTestArguments : public Qt3DRender::QStencilTestArguments {
public:
  using Qt3DRender::QStencilTestArguments::QStencilTestArguments;
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
      CuteQt3DRender_QStencilTestArgumentsCall0 call = reinterpret_cast<CuteQt3DRender_QStencilTestArgumentsCall0>(taken[0]);
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
      CuteQt3DRender_QStencilTestArgumentsCall1 call = reinterpret_cast<CuteQt3DRender_QStencilTestArgumentsCall1>(taken[1]);
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
      CuteQt3DRender_QStencilTestArgumentsCall2 call = reinterpret_cast<CuteQt3DRender_QStencilTestArgumentsCall2>(taken[2]);
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
      CuteQt3DRender_QStencilTestArgumentsCall3 call = reinterpret_cast<CuteQt3DRender_QStencilTestArgumentsCall3>(taken[3]);
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
      CuteQt3DRender_QStencilTestArgumentsCall4 call = reinterpret_cast<CuteQt3DRender_QStencilTestArgumentsCall4>(taken[4]);
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
      CuteQt3DRender_QStencilTestArgumentsCall5 call = reinterpret_cast<CuteQt3DRender_QStencilTestArgumentsCall5>(taken[5]);
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
      CuteQt3DRender_QStencilTestArgumentsCall6 call = reinterpret_cast<CuteQt3DRender_QStencilTestArgumentsCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QStencilTestArguments::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender21QStencilTestArguments10metaObjectEv(
    const Qt3DRender::QStencilTestArguments *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QStencilTestArguments::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender21QStencilTestArguments11qt_metacastEPKc(
    Qt3DRender::QStencilTestArguments *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QStencilTestArguments::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender21QStencilTestArguments11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QStencilTestArguments *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QStencilTestArguments::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender21QStencilTestArguments2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QStencilTestArguments::tr(s, c, n));
}

//  Qt3DRender::QStencilTestArguments::~QStencilTestArguments()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QStencilTestArgumentsD1Ev(
    Qt3DRender::QStencilTestArguments *self) {
  delete self;
}

//  uint Qt3DRender::QStencilTestArguments::comparisonMask() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK10Qt3DRender21QStencilTestArguments14comparisonMaskEv(
    const Qt3DRender::QStencilTestArguments *self) {
  return self->comparisonMask();
}

//  int Qt3DRender::QStencilTestArguments::referenceValue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender21QStencilTestArguments14referenceValueEv(
    const Qt3DRender::QStencilTestArguments *self) {
  return self->referenceValue();
}

//  StencilFunction Qt3DRender::QStencilTestArguments::stencilFunction()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::QStencilTestArguments::StencilFunction ritual_ZNK10Qt3DRender21QStencilTestArguments15stencilFunctionEv(
    const Qt3DRender::QStencilTestArguments *self) {
  return self->stencilFunction();
}

//  StencilFaceMode Qt3DRender::QStencilTestArguments::faceMode() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QStencilTestArguments::StencilFaceMode ritual_ZNK10Qt3DRender21QStencilTestArguments8faceModeEv(
    const Qt3DRender::QStencilTestArguments *self) {
  return self->faceMode();
}

//  void Qt3DRender::QStencilTestArguments::setComparisonMask(uint
//      comparisonMask)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QStencilTestArguments17setComparisonMaskEj(
    Qt3DRender::QStencilTestArguments *self,
    uint comparisonMask) {
  self->setComparisonMask(comparisonMask);
}

//  void Qt3DRender::QStencilTestArguments::setReferenceValue(int
//      referenceValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QStencilTestArguments17setReferenceValueEi(
    Qt3DRender::QStencilTestArguments *self,
    int referenceValue) {
  self->setReferenceValue(referenceValue);
}

//  void
//      Qt3DRender::QStencilTestArguments::setStencilFunction(StencilFunction
//      stencilFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QStencilTestArguments18setStencilFunctionENS0_15StencilFunctionE(
    Qt3DRender::QStencilTestArguments *self,
    Qt3DRender::QStencilTestArguments::StencilFunction stencilFunction) {
  self->setStencilFunction(stencilFunction);
}

//  void Qt3DRender::QStencilTestArguments::comparisonMaskChanged(uint
//      comparisonMask)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QStencilTestArguments21comparisonMaskChangedEj(
    Qt3DRender::QStencilTestArguments *self,
    uint comparisonMask) {
  self->comparisonMaskChanged(comparisonMask);
}

//  void
//      Qt3DRender::QStencilTestArguments::stencilFunctionChanged(StencilFunc
//      tion stencilFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QStencilTestArguments22stencilFunctionChangedENS0_15StencilFunctionE(
    Qt3DRender::QStencilTestArguments *self,
    Qt3DRender::QStencilTestArguments::StencilFunction stencilFunction) {
  self->stencilFunctionChanged(stencilFunction);
}

//  void Qt3DRender::QStencilTestArguments::referenceValueChanged(int
//      referenceValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QStencilTestArguments21referenceValueChangedEi(
    Qt3DRender::QStencilTestArguments *self,
    int referenceValue) {
  self->referenceValueChanged(referenceValue);
}

//  void Qt3DRender::QStencilTestArguments::faceModeChanged(StencilFaceMode
//      faceMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QStencilTestArguments15faceModeChangedENS0_15StencilFaceModeE(
    Qt3DRender::QStencilTestArguments *self,
    Qt3DRender::QStencilTestArguments::StencilFaceMode faceMode) {
  self->faceModeChanged(faceMode);
}

//  Qt3DRender::QStencilTestArguments::QStencilTestArguments(StencilFaceMode
//      face, QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QStencilTestArguments *ritual_ZN10Qt3DRender21QStencilTestArgumentsC1ENS0_15StencilFaceModeEP7QObject(
    Qt3DRender::QStencilTestArguments::StencilFaceMode face,
    QObject *parent) {
  return new CuteQt3DRender_QStencilTestArguments(face, parent);
}

//  QStencilTestArgumentsPrivate *Qt3DRender::QStencilTestArguments::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QStencilTestArgumentsPrivate *ritual_ZN10Qt3DRender21QStencilTestArguments6d_funcEv(
    Qt3DRender::QStencilTestArguments *self) {
  return self->d_func();
}

//  const QStencilTestArgumentsPrivate
//      *Qt3DRender::QStencilTestArguments::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QStencilTestArgumentsPrivate *ritual_ZNK10Qt3DRender21QStencilTestArguments6d_funcEv(
    const Qt3DRender::QStencilTestArguments *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QStencilTestArguments, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QStencilTestArguments(
    Qt3DRender::QStencilTestArguments *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QStencilTestArguments *>(self)->take(key, call);
}
