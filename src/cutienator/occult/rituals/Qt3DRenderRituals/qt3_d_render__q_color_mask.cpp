//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qcolormask.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qcolormask.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QColorMask that Python can take functions over in. Every Qt3DRender::QColorMask
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QColorMaskCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QColorMaskCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QColorMaskCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QColorMaskCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QColorMaskCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QColorMaskCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QColorMaskCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QColorMask : public Qt3DRender::QColorMask {
public:
  using Qt3DRender::QColorMask::QColorMask;
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
      CuteQt3DRender_QColorMaskCall0 call = reinterpret_cast<CuteQt3DRender_QColorMaskCall0>(taken[0]);
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
      CuteQt3DRender_QColorMaskCall1 call = reinterpret_cast<CuteQt3DRender_QColorMaskCall1>(taken[1]);
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
      CuteQt3DRender_QColorMaskCall2 call = reinterpret_cast<CuteQt3DRender_QColorMaskCall2>(taken[2]);
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
      CuteQt3DRender_QColorMaskCall3 call = reinterpret_cast<CuteQt3DRender_QColorMaskCall3>(taken[3]);
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
      CuteQt3DRender_QColorMaskCall4 call = reinterpret_cast<CuteQt3DRender_QColorMaskCall4>(taken[4]);
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
      CuteQt3DRender_QColorMaskCall5 call = reinterpret_cast<CuteQt3DRender_QColorMaskCall5>(taken[5]);
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
      CuteQt3DRender_QColorMaskCall6 call = reinterpret_cast<CuteQt3DRender_QColorMaskCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QColorMask::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender10QColorMask10metaObjectEv(
    const Qt3DRender::QColorMask *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QColorMask::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender10QColorMask11qt_metacastEPKc(
    Qt3DRender::QColorMask *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QColorMask::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender10QColorMask11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QColorMask *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QColorMask::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender10QColorMask2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QColorMask::tr(s, c, n));
}

//  Qt3DRender::QColorMask::QColorMask(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QColorMask *ritual_ZN10Qt3DRender10QColorMaskC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QColorMask(parent);
}

//  Qt3DRender::QColorMask::~QColorMask()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QColorMaskD1Ev(Qt3DRender::QColorMask *self) {
  delete self;
}

//  bool Qt3DRender::QColorMask::isRedMasked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender10QColorMask11isRedMaskedEv(
    const Qt3DRender::QColorMask *self) {
  return self->isRedMasked();
}

//  bool Qt3DRender::QColorMask::isGreenMasked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender10QColorMask13isGreenMaskedEv(
    const Qt3DRender::QColorMask *self) {
  return self->isGreenMasked();
}

//  bool Qt3DRender::QColorMask::isBlueMasked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender10QColorMask12isBlueMaskedEv(
    const Qt3DRender::QColorMask *self) {
  return self->isBlueMasked();
}

//  bool Qt3DRender::QColorMask::isAlphaMasked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender10QColorMask13isAlphaMaskedEv(
    const Qt3DRender::QColorMask *self) {
  return self->isAlphaMasked();
}

//  void Qt3DRender::QColorMask::setRedMasked(bool redMasked)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QColorMask12setRedMaskedEb(
    Qt3DRender::QColorMask *self,
    bool redMasked) {
  self->setRedMasked(redMasked);
}

//  void Qt3DRender::QColorMask::setGreenMasked(bool greenMasked)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QColorMask14setGreenMaskedEb(
    Qt3DRender::QColorMask *self,
    bool greenMasked) {
  self->setGreenMasked(greenMasked);
}

//  void Qt3DRender::QColorMask::setBlueMasked(bool blueMasked)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QColorMask13setBlueMaskedEb(
    Qt3DRender::QColorMask *self,
    bool blueMasked) {
  self->setBlueMasked(blueMasked);
}

//  void Qt3DRender::QColorMask::setAlphaMasked(bool alphaMasked)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QColorMask14setAlphaMaskedEb(
    Qt3DRender::QColorMask *self,
    bool alphaMasked) {
  self->setAlphaMasked(alphaMasked);
}

//  void Qt3DRender::QColorMask::redMaskedChanged(bool redMasked)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QColorMask16redMaskedChangedEb(
    Qt3DRender::QColorMask *self,
    bool redMasked) {
  self->redMaskedChanged(redMasked);
}

//  void Qt3DRender::QColorMask::greenMaskedChanged(bool greenMasked)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QColorMask18greenMaskedChangedEb(
    Qt3DRender::QColorMask *self,
    bool greenMasked) {
  self->greenMaskedChanged(greenMasked);
}

//  void Qt3DRender::QColorMask::blueMaskedChanged(bool blueMasked)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QColorMask17blueMaskedChangedEb(
    Qt3DRender::QColorMask *self,
    bool blueMasked) {
  self->blueMaskedChanged(blueMasked);
}

//  void Qt3DRender::QColorMask::alphaMaskedChanged(bool alphaMasked)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QColorMask18alphaMaskedChangedEb(
    Qt3DRender::QColorMask *self,
    bool alphaMasked) {
  self->alphaMaskedChanged(alphaMasked);
}

//  QColorMaskPrivate *Qt3DRender::QColorMask::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QColorMaskPrivate *ritual_ZN10Qt3DRender10QColorMask6d_funcEv(
    Qt3DRender::QColorMask *self) {
  return self->d_func();
}

//  const QColorMaskPrivate *Qt3DRender::QColorMask::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QColorMaskPrivate *ritual_ZNK10Qt3DRender10QColorMask6d_funcEv(
    const Qt3DRender::QColorMask *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QColorMask, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QColorMask(
    Qt3DRender::QColorMask *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QColorMask *>(self)->take(key, call);
}
