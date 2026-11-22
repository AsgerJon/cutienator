//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicseffect.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicseffect.h>
#include <QtCore/qstring.h>
#include <QtGui/qbrush.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QGraphicsOpacityEffect may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGraphicsOpacityEffect : QGraphicsOpacityEffect {
  using QGraphicsOpacityEffect::draw;
};

//  A QGraphicsOpacityEffect that Python can take functions over in. Every QGraphicsOpacityEffect
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGraphicsOpacityEffectCall0)(const void *, QPainter *, int *);
typedef const QRectF * (*CuteQGraphicsOpacityEffectCall1)(const void *, const QRectF *, int *);
typedef void (*CuteQGraphicsOpacityEffectCall2)(const void *, int, int *);
typedef bool (*CuteQGraphicsOpacityEffectCall3)(const void *, QEvent *, int *);
typedef bool (*CuteQGraphicsOpacityEffectCall4)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQGraphicsOpacityEffectCall5)(const void *, QTimerEvent *, int *);
typedef void (*CuteQGraphicsOpacityEffectCall6)(const void *, QChildEvent *, int *);
typedef void (*CuteQGraphicsOpacityEffectCall7)(const void *, QEvent *, int *);
typedef void (*CuteQGraphicsOpacityEffectCall8)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQGraphicsOpacityEffectCall9)(const void *, const QMetaMethod *, int *);
class CuteQGraphicsOpacityEffect : public QGraphicsOpacityEffect {
public:
  using QGraphicsOpacityEffect::QGraphicsOpacityEffect;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN15QGraphicsEffect4drawEP8QPainter")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QGraphicsEffect15boundingRectForERK6QRectF")) {
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

  //  void QGraphicsOpacityEffect::draw(QPainter *painter)
  void draw(QPainter *painter) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsOpacityEffectCall0 call = reinterpret_cast<CuteQGraphicsOpacityEffectCall0>(taken[0]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QGraphicsOpacityEffect::draw(painter);
  }

  //  QRectF QGraphicsEffect::boundingRectFor(const QRectF &sourceRect)
  //      const
  QRectF boundingRectFor(const QRectF &sourceRect) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsOpacityEffectCall1 call = reinterpret_cast<CuteQGraphicsOpacityEffectCall1>(taken[1]);
      const QRectF * given = call(this, &sourceRect, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsEffect::boundingRectFor(sourceRect);
  }

  //  void QGraphicsEffect::sourceChanged(ChangeFlags flags)
  void sourceChanged(QGraphicsEffect::ChangeFlags flags) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsOpacityEffectCall2 call = reinterpret_cast<CuteQGraphicsOpacityEffectCall2>(taken[2]);
      call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QGraphicsEffect::sourceChanged(flags);
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsOpacityEffectCall3 call = reinterpret_cast<CuteQGraphicsOpacityEffectCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsOpacityEffectCall4 call = reinterpret_cast<CuteQGraphicsOpacityEffectCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsOpacityEffectCall5 call = reinterpret_cast<CuteQGraphicsOpacityEffectCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsOpacityEffectCall6 call = reinterpret_cast<CuteQGraphicsOpacityEffectCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsOpacityEffectCall7 call = reinterpret_cast<CuteQGraphicsOpacityEffectCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphicsOpacityEffectCall8 call = reinterpret_cast<CuteQGraphicsOpacityEffectCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQGraphicsOpacityEffectCall9 call = reinterpret_cast<CuteQGraphicsOpacityEffectCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QGraphicsOpacityEffect::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QGraphicsOpacityEffect10metaObjectEv(
    const QGraphicsOpacityEffect *self) {
  return self->metaObject();
}

//  QString QGraphicsOpacityEffect::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QGraphicsOpacityEffect2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsOpacityEffect::tr(s, c, n));
}

//  QGraphicsOpacityEffect::QGraphicsOpacityEffect(QObject *parent)
extern "C" Q_DECL_EXPORT
QGraphicsOpacityEffect *ritual_ZN22QGraphicsOpacityEffectC1EP7QObject(
    QObject *parent) {
  return new CuteQGraphicsOpacityEffect(parent);
}

//  QGraphicsOpacityEffect::~QGraphicsOpacityEffect()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsOpacityEffectD1Ev(QGraphicsOpacityEffect *self) {
  delete self;
}

//  qreal QGraphicsOpacityEffect::opacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QGraphicsOpacityEffect7opacityEv(
    const QGraphicsOpacityEffect *self) {
  return self->opacity();
}

//  QBrush QGraphicsOpacityEffect::opacityMask() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK22QGraphicsOpacityEffect11opacityMaskEv(
    const QGraphicsOpacityEffect *self) {
  return new QBrush(self->opacityMask());
}

//  void QGraphicsOpacityEffect::setOpacity(qreal opacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsOpacityEffect10setOpacityEd(
    QGraphicsOpacityEffect *self,
    qreal opacity) {
  self->setOpacity(opacity);
}

//  void QGraphicsOpacityEffect::setOpacityMask(const QBrush &mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsOpacityEffect14setOpacityMaskERK6QBrush(
    QGraphicsOpacityEffect *self,
    const QBrush *mask) {
  self->setOpacityMask(*mask);
}

//  a Python function taken by a CuteQGraphicsOpacityEffect, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsOpacityEffect(
    QGraphicsOpacityEffect *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsOpacityEffect *>(self)->take(key, call);
}

//  void QGraphicsOpacityEffect::draw(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QGraphicsOpacityEffect4drawEP8QPainter(
    QGraphicsOpacityEffect *self,
    QPainter *painter) {
  static_cast<OwnQGraphicsOpacityEffect *>(self)->OwnQGraphicsOpacityEffect::draw(
      painter);
}
