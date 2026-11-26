//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicseffect.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
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
#if QT_CONFIG(graphicseffect)
typedef void (*CuteQGraphicsColorizeEffectCall0)(const void *, QPainter *, int *);
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
typedef const QRectF * (*CuteQGraphicsColorizeEffectCall1)(const void *, const QRectF *, int *);
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
typedef void (*CuteQGraphicsColorizeEffectCall2)(const void *, int, int *);
#endif  // QT_CONFIG(graphicseffect)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGraphicsColorizeEffectCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGraphicsColorizeEffectCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsColorizeEffectCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsColorizeEffectCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsColorizeEffectCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsColorizeEffectCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsColorizeEffectCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGraphicsColorizeEffect : public QGraphicsColorizeEffect {
public:
  using QGraphicsColorizeEffect::QGraphicsColorizeEffect;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZN15QGraphicsEffect4drawEP8QPainter")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZNK15QGraphicsEffect15boundingRectForERK6QRectF")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZN15QGraphicsEffect13sourceChangedE6QFlagsINS_10ChangeFlagEE")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(graphicseffect)
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
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
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
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
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
#endif  // QT_CONFIG(graphicseffect)

#if !defined(QT_NO_QOBJECT)
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
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
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
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
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
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
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
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
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
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
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
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
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
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGraphicsColorizeEffect::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QGraphicsColorizeEffect10metaObjectEv(
    const QGraphicsColorizeEffect *self) {
  return self->metaObject();
}

//  void *QGraphicsColorizeEffect::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QGraphicsColorizeEffect11qt_metacastEPKc(
    QGraphicsColorizeEffect *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QGraphicsColorizeEffect::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QGraphicsColorizeEffect11qt_metacallEN11QMetaObject4CallEiPPv(
    QGraphicsColorizeEffect *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  void QGraphicsColorizeEffect::colorChanged(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsColorizeEffect12colorChangedERK6QColor(
    QGraphicsColorizeEffect *self,
    const QColor *color) {
  self->colorChanged(*color);
}

//  void QGraphicsColorizeEffect::strengthChanged(qreal strength)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsColorizeEffect15strengthChangedEd(
    QGraphicsColorizeEffect *self,
    qreal strength) {
  self->strengthChanged(strength);
}

//  void QGraphicsColorizeEffect::draw(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsColorizeEffect4drawEP8QPainter(
    QGraphicsColorizeEffect *self,
    QPainter *painter) {
  self->draw(painter);
}

//  QGraphicsColorizeEffectPrivate *QGraphicsColorizeEffect::d_func()
extern "C" Q_DECL_EXPORT
QGraphicsColorizeEffectPrivate *ritual_ZN23QGraphicsColorizeEffect6d_funcEv(
    QGraphicsColorizeEffect *self) {
  return self->d_func();
}

//  const QGraphicsColorizeEffectPrivate *QGraphicsColorizeEffect::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QGraphicsColorizeEffectPrivate *ritual_ZNK23QGraphicsColorizeEffect6d_funcEv(
    const QGraphicsColorizeEffect *self) {
  return self->d_func();
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

#endif  // QT_CONFIG(graphicseffect)
#endif  // QT_CONFIG(graphicseffect)
