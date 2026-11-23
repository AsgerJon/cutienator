//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicseffect.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicseffect.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QGraphicsBlurEffect may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGraphicsBlurEffect : QGraphicsBlurEffect {
  using QGraphicsBlurEffect::draw;
};

//  A QGraphicsBlurEffect that Python can take functions over in. Every QGraphicsBlurEffect
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QRectF * (*CuteQGraphicsBlurEffectCall0)(const void *, const QRectF *, int *);
typedef void (*CuteQGraphicsBlurEffectCall1)(const void *, QPainter *, int *);
typedef void (*CuteQGraphicsBlurEffectCall2)(const void *, int, int *);
typedef bool (*CuteQGraphicsBlurEffectCall3)(const void *, QEvent *, int *);
typedef bool (*CuteQGraphicsBlurEffectCall4)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQGraphicsBlurEffectCall5)(const void *, QTimerEvent *, int *);
typedef void (*CuteQGraphicsBlurEffectCall6)(const void *, QChildEvent *, int *);
typedef void (*CuteQGraphicsBlurEffectCall7)(const void *, QEvent *, int *);
typedef void (*CuteQGraphicsBlurEffectCall8)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQGraphicsBlurEffectCall9)(const void *, const QMetaMethod *, int *);
class CuteQGraphicsBlurEffect : public QGraphicsBlurEffect {
public:
  using QGraphicsBlurEffect::QGraphicsBlurEffect;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK15QGraphicsEffect15boundingRectForERK6QRectF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphicsEffect4drawEP8QPainter")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphicsEffect13sourceChangedE6QFlagsINS_10ChangeFlagEE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
    return false;
  }

  //  QRectF QGraphicsBlurEffect::boundingRectFor(const QRectF &rect) const
  QRectF boundingRectFor(const QRectF &rect) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsBlurEffectCall0 call = reinterpret_cast<CuteQGraphicsBlurEffectCall0>(taken[0]);
      const QRectF * given = call(this, &rect, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsBlurEffect::boundingRectFor(rect);
  }

  //  void QGraphicsBlurEffect::draw(QPainter *painter)
  void draw(QPainter *painter) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsBlurEffectCall1 call = reinterpret_cast<CuteQGraphicsBlurEffectCall1>(taken[1]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QGraphicsBlurEffect::draw(painter);
  }

  //  void QGraphicsEffect::sourceChanged(ChangeFlags flags)
  void sourceChanged(QGraphicsEffect::ChangeFlags flags) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsBlurEffectCall2 call = reinterpret_cast<CuteQGraphicsBlurEffectCall2>(taken[2]);
      call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QGraphicsEffect::sourceChanged(flags);
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsBlurEffectCall3 call = reinterpret_cast<CuteQGraphicsBlurEffectCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsBlurEffectCall4 call = reinterpret_cast<CuteQGraphicsBlurEffectCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsBlurEffectCall5 call = reinterpret_cast<CuteQGraphicsBlurEffectCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsBlurEffectCall6 call = reinterpret_cast<CuteQGraphicsBlurEffectCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsBlurEffectCall7 call = reinterpret_cast<CuteQGraphicsBlurEffectCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphicsBlurEffectCall8 call = reinterpret_cast<CuteQGraphicsBlurEffectCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQGraphicsBlurEffectCall9 call = reinterpret_cast<CuteQGraphicsBlurEffectCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QGraphicsBlurEffect::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QGraphicsBlurEffect10metaObjectEv(
    const QGraphicsBlurEffect *self) {
  return self->metaObject();
}

//  QString QGraphicsBlurEffect::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QGraphicsBlurEffect2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsBlurEffect::tr(s, c, n));
}

//  QGraphicsBlurEffect::QGraphicsBlurEffect(QObject *parent)
extern "C" Q_DECL_EXPORT
QGraphicsBlurEffect *ritual_ZN19QGraphicsBlurEffectC1EP7QObject(
    QObject *parent) {
  return new CuteQGraphicsBlurEffect(parent);
}

//  QGraphicsBlurEffect::~QGraphicsBlurEffect()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsBlurEffectD1Ev(QGraphicsBlurEffect *self) {
  delete self;
}

//  QRectF QGraphicsBlurEffect::boundingRectFor(const QRectF &rect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19QGraphicsBlurEffect15boundingRectForERK6QRectF(
    const QGraphicsBlurEffect *self,
    const QRectF *rect) {
  return new QRectF(self->boundingRectFor(*rect));
}

//  qreal QGraphicsBlurEffect::blurRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGraphicsBlurEffect10blurRadiusEv(
    const QGraphicsBlurEffect *self) {
  return self->blurRadius();
}

//  BlurHints QGraphicsBlurEffect::blurHints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QGraphicsBlurEffect9blurHintsEv(
    const QGraphicsBlurEffect *self) {
  return static_cast<int>(self->blurHints().toInt());
}

//  void QGraphicsBlurEffect::setBlurRadius(qreal blurRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsBlurEffect13setBlurRadiusEd(
    QGraphicsBlurEffect *self,
    qreal blurRadius) {
  self->setBlurRadius(blurRadius);
}

//  void QGraphicsBlurEffect::setBlurHints(BlurHints hints)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsBlurEffect12setBlurHintsE6QFlagsINS_8BlurHintEE(
    QGraphicsBlurEffect *self,
    int hints) {
  self->setBlurHints(QFlags<QGraphicsBlurEffect::BlurHint>::fromInt(hints));
}

//  void QGraphicsBlurEffect::draw(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGraphicsBlurEffect4drawEP8QPainter(
    QGraphicsBlurEffect *self,
    QPainter *painter) {
  self->draw(painter);
}

//  QGraphicsBlurEffectPrivate *QGraphicsBlurEffect::d_func()
extern "C" Q_DECL_EXPORT
QGraphicsBlurEffectPrivate *ritual_ZN19QGraphicsBlurEffect6d_funcEv(
    QGraphicsBlurEffect *self) {
  return self->d_func();
}

//  const QGraphicsBlurEffectPrivate *QGraphicsBlurEffect::d_func() const
extern "C" Q_DECL_EXPORT
const QGraphicsBlurEffectPrivate *ritual_ZNK19QGraphicsBlurEffect6d_funcEv(
    const QGraphicsBlurEffect *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQGraphicsBlurEffect, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsBlurEffect(
    QGraphicsBlurEffect *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsBlurEffect *>(self)->take(key, call);
}

//  QRectF QGraphicsBlurEffect::boundingRectFor(const QRectF &rect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK19QGraphicsBlurEffect15boundingRectForERK6QRectF(
    const QGraphicsBlurEffect *self,
    const QRectF *rect) {
  return new QRectF(self->QGraphicsBlurEffect::boundingRectFor(*rect));
}

//  void QGraphicsBlurEffect::draw(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QGraphicsBlurEffect4drawEP8QPainter(
    QGraphicsBlurEffect *self,
    QPainter *painter) {
  static_cast<OwnQGraphicsBlurEffect *>(self)->OwnQGraphicsBlurEffect::draw(
      painter);
}
