//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicseffect.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicseffect.h>
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QGraphicsColorizeEffect may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGraphicsColorizeEffect : QGraphicsColorizeEffect {
  using QGraphicsColorizeEffect::draw;
};

//  A QGraphicsColorizeEffect that Python can take functions over in. Every QGraphicsColorizeEffect
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGraphicsColorizeEffectCall0)(const void *, QPainter *, int *);
typedef const QRectF * (*CuteQGraphicsColorizeEffectCall1)(const void *, const QRectF *, int *);
typedef void (*CuteQGraphicsColorizeEffectCall2)(const void *, int, int *);
typedef bool (*CuteQGraphicsColorizeEffectCall3)(const void *, QEvent *, int *);
typedef bool (*CuteQGraphicsColorizeEffectCall4)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQGraphicsColorizeEffectCall5)(const void *, QTimerEvent *, int *);
typedef void (*CuteQGraphicsColorizeEffectCall6)(const void *, QChildEvent *, int *);
typedef void (*CuteQGraphicsColorizeEffectCall7)(const void *, QEvent *, int *);
typedef void (*CuteQGraphicsColorizeEffectCall8)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQGraphicsColorizeEffectCall9)(const void *, const QMetaMethod *, int *);
class CuteQGraphicsColorizeEffect : public QGraphicsColorizeEffect {
public:
  using QGraphicsColorizeEffect::QGraphicsColorizeEffect;
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

  //  void QGraphicsColorizeEffect::draw(QPainter *painter)
  void draw(QPainter *painter) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsColorizeEffectCall0 call = reinterpret_cast<CuteQGraphicsColorizeEffectCall0>(taken[0]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QGraphicsColorizeEffect::draw(painter);
  }

  //  QRectF QGraphicsEffect::boundingRectFor(const QRectF &sourceRect)
  //      const
  QRectF boundingRectFor(const QRectF &sourceRect) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsColorizeEffectCall1 call = reinterpret_cast<CuteQGraphicsColorizeEffectCall1>(taken[1]);
      const QRectF * given = call(this, &sourceRect, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsEffect::boundingRectFor(sourceRect);
  }

  //  void QGraphicsEffect::sourceChanged(ChangeFlags flags)
  void sourceChanged(QGraphicsEffect::ChangeFlags flags) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsColorizeEffectCall2 call = reinterpret_cast<CuteQGraphicsColorizeEffectCall2>(taken[2]);
      call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return;
    }
    QGraphicsEffect::sourceChanged(flags);
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsColorizeEffectCall3 call = reinterpret_cast<CuteQGraphicsColorizeEffectCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsColorizeEffectCall4 call = reinterpret_cast<CuteQGraphicsColorizeEffectCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsColorizeEffectCall5 call = reinterpret_cast<CuteQGraphicsColorizeEffectCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsColorizeEffectCall6 call = reinterpret_cast<CuteQGraphicsColorizeEffectCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsColorizeEffectCall7 call = reinterpret_cast<CuteQGraphicsColorizeEffectCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphicsColorizeEffectCall8 call = reinterpret_cast<CuteQGraphicsColorizeEffectCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQGraphicsColorizeEffectCall9 call = reinterpret_cast<CuteQGraphicsColorizeEffectCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QGraphicsColorizeEffect::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QGraphicsColorizeEffect10metaObjectEv(
    const QGraphicsColorizeEffect *self) {
  return self->metaObject();
}

//  QString QGraphicsColorizeEffect::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QGraphicsColorizeEffect2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsColorizeEffect::tr(s, c, n));
}

//  QGraphicsColorizeEffect::QGraphicsColorizeEffect(QObject *parent)
extern "C" Q_DECL_EXPORT
QGraphicsColorizeEffect *ritual_ZN23QGraphicsColorizeEffectC1EP7QObject(
    QObject *parent) {
  return new CuteQGraphicsColorizeEffect(parent);
}

//  QGraphicsColorizeEffect::~QGraphicsColorizeEffect()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsColorizeEffectD1Ev(QGraphicsColorizeEffect *self) {
  delete self;
}

//  QColor QGraphicsColorizeEffect::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK23QGraphicsColorizeEffect5colorEv(
    const QGraphicsColorizeEffect *self) {
  return new QColor(self->color());
}

//  qreal QGraphicsColorizeEffect::strength() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QGraphicsColorizeEffect8strengthEv(
    const QGraphicsColorizeEffect *self) {
  return self->strength();
}

//  void QGraphicsColorizeEffect::setColor(const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsColorizeEffect8setColorERK6QColor(
    QGraphicsColorizeEffect *self,
    const QColor *c) {
  self->setColor(*c);
}

//  void QGraphicsColorizeEffect::setStrength(qreal strength)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsColorizeEffect11setStrengthEd(
    QGraphicsColorizeEffect *self,
    qreal strength) {
  self->setStrength(strength);
}

//  void QGraphicsColorizeEffect::draw(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsColorizeEffect4drawEP8QPainter(
    QGraphicsColorizeEffect *self,
    QPainter *painter) {
  self->draw(painter);
}

//  a Python function taken by a CuteQGraphicsColorizeEffect, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsColorizeEffect(
    QGraphicsColorizeEffect *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsColorizeEffect *>(self)->take(key, call);
}

//  void QGraphicsColorizeEffect::draw(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QGraphicsColorizeEffect4drawEP8QPainter(
    QGraphicsColorizeEffect *self,
    QPainter *painter) {
  static_cast<OwnQGraphicsColorizeEffect *>(self)->OwnQGraphicsColorizeEffect::draw(
      painter);
}
