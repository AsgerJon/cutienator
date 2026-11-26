//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qlinewidth.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qlinewidth.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QLineWidth that Python can take functions over in. Every Qt3DRender::QLineWidth
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QLineWidthCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QLineWidthCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QLineWidthCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QLineWidthCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QLineWidthCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QLineWidthCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QLineWidthCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QLineWidth : public Qt3DRender::QLineWidth {
public:
  using Qt3DRender::QLineWidth::QLineWidth;
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
      CuteQt3DRender_QLineWidthCall0 call = reinterpret_cast<CuteQt3DRender_QLineWidthCall0>(taken[0]);
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
      CuteQt3DRender_QLineWidthCall1 call = reinterpret_cast<CuteQt3DRender_QLineWidthCall1>(taken[1]);
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
      CuteQt3DRender_QLineWidthCall2 call = reinterpret_cast<CuteQt3DRender_QLineWidthCall2>(taken[2]);
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
      CuteQt3DRender_QLineWidthCall3 call = reinterpret_cast<CuteQt3DRender_QLineWidthCall3>(taken[3]);
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
      CuteQt3DRender_QLineWidthCall4 call = reinterpret_cast<CuteQt3DRender_QLineWidthCall4>(taken[4]);
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
      CuteQt3DRender_QLineWidthCall5 call = reinterpret_cast<CuteQt3DRender_QLineWidthCall5>(taken[5]);
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
      CuteQt3DRender_QLineWidthCall6 call = reinterpret_cast<CuteQt3DRender_QLineWidthCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QLineWidth::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender10QLineWidth10metaObjectEv(
    const Qt3DRender::QLineWidth *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QLineWidth::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender10QLineWidth11qt_metacastEPKc(
    Qt3DRender::QLineWidth *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QLineWidth::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender10QLineWidth11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QLineWidth *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QLineWidth::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender10QLineWidth2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QLineWidth::tr(s, c, n));
}

//  Qt3DRender::QLineWidth::QLineWidth(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QLineWidth *ritual_ZN10Qt3DRender10QLineWidthC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QLineWidth(parent);
}

//  Qt3DRender::QLineWidth::~QLineWidth()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QLineWidthD1Ev(Qt3DRender::QLineWidth *self) {
  delete self;
}

//  float Qt3DRender::QLineWidth::value() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender10QLineWidth5valueEv(
    const Qt3DRender::QLineWidth *self) {
  return self->value();
}

//  bool Qt3DRender::QLineWidth::smooth() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender10QLineWidth6smoothEv(
    const Qt3DRender::QLineWidth *self) {
  return self->smooth();
}

//  void Qt3DRender::QLineWidth::setValue(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QLineWidth8setValueEf(
    Qt3DRender::QLineWidth *self,
    float value) {
  self->setValue(value);
}

//  void Qt3DRender::QLineWidth::setSmooth(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QLineWidth9setSmoothEb(
    Qt3DRender::QLineWidth *self,
    bool enabled) {
  self->setSmooth(enabled);
}

//  void Qt3DRender::QLineWidth::valueChanged(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QLineWidth12valueChangedEf(
    Qt3DRender::QLineWidth *self,
    float value) {
  self->valueChanged(value);
}

//  void Qt3DRender::QLineWidth::smoothChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QLineWidth13smoothChangedEb(
    Qt3DRender::QLineWidth *self,
    bool enabled) {
  self->smoothChanged(enabled);
}

//  QLineWidthPrivate *Qt3DRender::QLineWidth::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QLineWidthPrivate *ritual_ZN10Qt3DRender10QLineWidth6d_funcEv(
    Qt3DRender::QLineWidth *self) {
  return self->d_func();
}

//  const QLineWidthPrivate *Qt3DRender::QLineWidth::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QLineWidthPrivate *ritual_ZNK10Qt3DRender10QLineWidth6d_funcEv(
    const Qt3DRender::QLineWidth *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QLineWidth, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QLineWidth(
    Qt3DRender::QLineWidth *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QLineWidth *>(self)->take(key, call);
}
