//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qblendequationarguments.h, Qt 6.12.0. Changes made here are
//  lost.
#include <Qt3DRender/qblendequationarguments.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QBlendEquationArguments that Python can take functions over in. Every Qt3DRender::QBlendEquationArguments
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QBlendEquationArgumentsCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QBlendEquationArgumentsCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QBlendEquationArgumentsCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QBlendEquationArgumentsCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QBlendEquationArgumentsCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QBlendEquationArgumentsCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QBlendEquationArgumentsCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QBlendEquationArguments : public Qt3DRender::QBlendEquationArguments {
public:
  using Qt3DRender::QBlendEquationArguments::QBlendEquationArguments;
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
      CuteQt3DRender_QBlendEquationArgumentsCall0 call = reinterpret_cast<CuteQt3DRender_QBlendEquationArgumentsCall0>(taken[0]);
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
      CuteQt3DRender_QBlendEquationArgumentsCall1 call = reinterpret_cast<CuteQt3DRender_QBlendEquationArgumentsCall1>(taken[1]);
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
      CuteQt3DRender_QBlendEquationArgumentsCall2 call = reinterpret_cast<CuteQt3DRender_QBlendEquationArgumentsCall2>(taken[2]);
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
      CuteQt3DRender_QBlendEquationArgumentsCall3 call = reinterpret_cast<CuteQt3DRender_QBlendEquationArgumentsCall3>(taken[3]);
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
      CuteQt3DRender_QBlendEquationArgumentsCall4 call = reinterpret_cast<CuteQt3DRender_QBlendEquationArgumentsCall4>(taken[4]);
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
      CuteQt3DRender_QBlendEquationArgumentsCall5 call = reinterpret_cast<CuteQt3DRender_QBlendEquationArgumentsCall5>(taken[5]);
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
      CuteQt3DRender_QBlendEquationArgumentsCall6 call = reinterpret_cast<CuteQt3DRender_QBlendEquationArgumentsCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QBlendEquationArguments::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender23QBlendEquationArguments10metaObjectEv(
    const Qt3DRender::QBlendEquationArguments *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QBlendEquationArguments::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender23QBlendEquationArguments11qt_metacastEPKc(
    Qt3DRender::QBlendEquationArguments *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QBlendEquationArguments::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender23QBlendEquationArguments11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QBlendEquationArguments *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QBlendEquationArguments::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender23QBlendEquationArguments2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QBlendEquationArguments::tr(s, c, n));
}

//  Qt3DRender::QBlendEquationArguments::QBlendEquationArguments(Qt3DCore::QN
//      ode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QBlendEquationArguments *ritual_ZN10Qt3DRender23QBlendEquationArgumentsC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QBlendEquationArguments(parent);
}

//  Qt3DRender::QBlendEquationArguments::~QBlendEquationArguments()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender23QBlendEquationArgumentsD1Ev(
    Qt3DRender::QBlendEquationArguments *self) {
  delete self;
}

//  Blending Qt3DRender::QBlendEquationArguments::sourceRgb() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QBlendEquationArguments::Blending ritual_ZNK10Qt3DRender23QBlendEquationArguments9sourceRgbEv(
    const Qt3DRender::QBlendEquationArguments *self) {
  return self->sourceRgb();
}

//  Blending Qt3DRender::QBlendEquationArguments::destinationRgb() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QBlendEquationArguments::Blending ritual_ZNK10Qt3DRender23QBlendEquationArguments14destinationRgbEv(
    const Qt3DRender::QBlendEquationArguments *self) {
  return self->destinationRgb();
}

//  Blending Qt3DRender::QBlendEquationArguments::sourceAlpha() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QBlendEquationArguments::Blending ritual_ZNK10Qt3DRender23QBlendEquationArguments11sourceAlphaEv(
    const Qt3DRender::QBlendEquationArguments *self) {
  return self->sourceAlpha();
}

//  Blending Qt3DRender::QBlendEquationArguments::destinationAlpha() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QBlendEquationArguments::Blending ritual_ZNK10Qt3DRender23QBlendEquationArguments16destinationAlphaEv(
    const Qt3DRender::QBlendEquationArguments *self) {
  return self->destinationAlpha();
}

//  int Qt3DRender::QBlendEquationArguments::bufferIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender23QBlendEquationArguments11bufferIndexEv(
    const Qt3DRender::QBlendEquationArguments *self) {
  return self->bufferIndex();
}

//  void Qt3DRender::QBlendEquationArguments::setSourceRgb(Blending
//      sourceRgb)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender23QBlendEquationArguments12setSourceRgbENS0_8BlendingE(
    Qt3DRender::QBlendEquationArguments *self,
    Qt3DRender::QBlendEquationArguments::Blending sourceRgb) {
  self->setSourceRgb(sourceRgb);
}

//  void Qt3DRender::QBlendEquationArguments::setDestinationRgb(Blending
//      destinationRgb)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender23QBlendEquationArguments17setDestinationRgbENS0_8BlendingE(
    Qt3DRender::QBlendEquationArguments *self,
    Qt3DRender::QBlendEquationArguments::Blending destinationRgb) {
  self->setDestinationRgb(destinationRgb);
}

//  void Qt3DRender::QBlendEquationArguments::setSourceAlpha(Blending
//      sourceAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender23QBlendEquationArguments14setSourceAlphaENS0_8BlendingE(
    Qt3DRender::QBlendEquationArguments *self,
    Qt3DRender::QBlendEquationArguments::Blending sourceAlpha) {
  self->setSourceAlpha(sourceAlpha);
}

//  void Qt3DRender::QBlendEquationArguments::setDestinationAlpha(Blending
//      destinationAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender23QBlendEquationArguments19setDestinationAlphaENS0_8BlendingE(
    Qt3DRender::QBlendEquationArguments *self,
    Qt3DRender::QBlendEquationArguments::Blending destinationAlpha) {
  self->setDestinationAlpha(destinationAlpha);
}

//  void Qt3DRender::QBlendEquationArguments::setSourceRgba(Blending
//      sourceRgba)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender23QBlendEquationArguments13setSourceRgbaENS0_8BlendingE(
    Qt3DRender::QBlendEquationArguments *self,
    Qt3DRender::QBlendEquationArguments::Blending sourceRgba) {
  self->setSourceRgba(sourceRgba);
}

//  void Qt3DRender::QBlendEquationArguments::setDestinationRgba(Blending
//      destinationRgba)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender23QBlendEquationArguments18setDestinationRgbaENS0_8BlendingE(
    Qt3DRender::QBlendEquationArguments *self,
    Qt3DRender::QBlendEquationArguments::Blending destinationRgba) {
  self->setDestinationRgba(destinationRgba);
}

//  void Qt3DRender::QBlendEquationArguments::setBufferIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender23QBlendEquationArguments14setBufferIndexEi(
    Qt3DRender::QBlendEquationArguments *self,
    int index) {
  self->setBufferIndex(index);
}

//  void Qt3DRender::QBlendEquationArguments::sourceRgbChanged(Blending
//      sourceRgb)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender23QBlendEquationArguments16sourceRgbChangedENS0_8BlendingE(
    Qt3DRender::QBlendEquationArguments *self,
    Qt3DRender::QBlendEquationArguments::Blending sourceRgb) {
  self->sourceRgbChanged(sourceRgb);
}

//  void Qt3DRender::QBlendEquationArguments::sourceAlphaChanged(Blending
//      sourceAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender23QBlendEquationArguments18sourceAlphaChangedENS0_8BlendingE(
    Qt3DRender::QBlendEquationArguments *self,
    Qt3DRender::QBlendEquationArguments::Blending sourceAlpha) {
  self->sourceAlphaChanged(sourceAlpha);
}

//  void Qt3DRender::QBlendEquationArguments::destinationRgbChanged(Blending
//      destinationRgb)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender23QBlendEquationArguments21destinationRgbChangedENS0_8BlendingE(
    Qt3DRender::QBlendEquationArguments *self,
    Qt3DRender::QBlendEquationArguments::Blending destinationRgb) {
  self->destinationRgbChanged(destinationRgb);
}

//  void
//      Qt3DRender::QBlendEquationArguments::destinationAlphaChanged(Blending
//      destinationAlpha)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender23QBlendEquationArguments23destinationAlphaChangedENS0_8BlendingE(
    Qt3DRender::QBlendEquationArguments *self,
    Qt3DRender::QBlendEquationArguments::Blending destinationAlpha) {
  self->destinationAlphaChanged(destinationAlpha);
}

//  void Qt3DRender::QBlendEquationArguments::sourceRgbaChanged(Blending
//      sourceRgba)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender23QBlendEquationArguments17sourceRgbaChangedENS0_8BlendingE(
    Qt3DRender::QBlendEquationArguments *self,
    Qt3DRender::QBlendEquationArguments::Blending sourceRgba) {
  self->sourceRgbaChanged(sourceRgba);
}

//  void Qt3DRender::QBlendEquationArguments::destinationRgbaChanged(Blending
//      destinationRgba)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender23QBlendEquationArguments22destinationRgbaChangedENS0_8BlendingE(
    Qt3DRender::QBlendEquationArguments *self,
    Qt3DRender::QBlendEquationArguments::Blending destinationRgba) {
  self->destinationRgbaChanged(destinationRgba);
}

//  void Qt3DRender::QBlendEquationArguments::bufferIndexChanged(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender23QBlendEquationArguments18bufferIndexChangedEi(
    Qt3DRender::QBlendEquationArguments *self,
    int index) {
  self->bufferIndexChanged(index);
}

//  Qt3DRender::QBlendEquationArguments::QBlendEquationArguments(QBlendEquati
//      onArgumentsPrivate &dd, Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QBlendEquationArguments *ritual_ZN10Qt3DRender23QBlendEquationArgumentsC1ERNS_30QBlendEquationArgumentsPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QBlendEquationArgumentsPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QBlendEquationArguments(*dd, parent);
}

//  QBlendEquationArgumentsPrivate
//      *Qt3DRender::QBlendEquationArguments::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QBlendEquationArgumentsPrivate *ritual_ZN10Qt3DRender23QBlendEquationArguments6d_funcEv(
    Qt3DRender::QBlendEquationArguments *self) {
  return self->d_func();
}

//  const QBlendEquationArgumentsPrivate
//      *Qt3DRender::QBlendEquationArguments::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QBlendEquationArgumentsPrivate *ritual_ZNK10Qt3DRender23QBlendEquationArguments6d_funcEv(
    const Qt3DRender::QBlendEquationArguments *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QBlendEquationArguments, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QBlendEquationArguments(
    Qt3DRender::QBlendEquationArguments *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QBlendEquationArguments *>(self)->take(key, call);
}
