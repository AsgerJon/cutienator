//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicseffect.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicseffect.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QGraphicsDropShadowEffect may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGraphicsDropShadowEffect : QGraphicsDropShadowEffect {
  using QGraphicsDropShadowEffect::draw;
};

//  A QGraphicsDropShadowEffect that Python can take functions over in. Every QGraphicsDropShadowEffect
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QRectF * (*CuteQGraphicsDropShadowEffectCall0)(const void *, const QRectF *, int *);
typedef void (*CuteQGraphicsDropShadowEffectCall1)(const void *, QPainter *, int *);
typedef bool (*CuteQGraphicsDropShadowEffectCall2)(const void *, QEvent *, int *);
typedef bool (*CuteQGraphicsDropShadowEffectCall3)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQGraphicsDropShadowEffectCall4)(const void *, QTimerEvent *, int *);
typedef void (*CuteQGraphicsDropShadowEffectCall5)(const void *, QChildEvent *, int *);
typedef void (*CuteQGraphicsDropShadowEffectCall6)(const void *, QEvent *, int *);
typedef void (*CuteQGraphicsDropShadowEffectCall7)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQGraphicsDropShadowEffectCall8)(const void *, const QMetaMethod *, int *);
class CuteQGraphicsDropShadowEffect : public QGraphicsDropShadowEffect {
public:
  using QGraphicsDropShadowEffect::QGraphicsDropShadowEffect;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK15QGraphicsEffect15boundingRectForERK6QRectF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QGraphicsEffect4drawEP8QPainter")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
    return false;
  }

  //  QRectF QGraphicsDropShadowEffect::boundingRectFor(const QRectF &rect)
  //      const
  QRectF boundingRectFor(const QRectF &rect) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsDropShadowEffectCall0 call = reinterpret_cast<CuteQGraphicsDropShadowEffectCall0>(taken[0]);
      const QRectF * given = call(this, &rect, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsDropShadowEffect::boundingRectFor(rect);
  }

  //  void QGraphicsDropShadowEffect::draw(QPainter *painter)
  void draw(QPainter *painter) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsDropShadowEffectCall1 call = reinterpret_cast<CuteQGraphicsDropShadowEffectCall1>(taken[1]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QGraphicsDropShadowEffect::draw(painter);
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsDropShadowEffectCall2 call = reinterpret_cast<CuteQGraphicsDropShadowEffectCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsDropShadowEffectCall3 call = reinterpret_cast<CuteQGraphicsDropShadowEffectCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsDropShadowEffectCall4 call = reinterpret_cast<CuteQGraphicsDropShadowEffectCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsDropShadowEffectCall5 call = reinterpret_cast<CuteQGraphicsDropShadowEffectCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsDropShadowEffectCall6 call = reinterpret_cast<CuteQGraphicsDropShadowEffectCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsDropShadowEffectCall7 call = reinterpret_cast<CuteQGraphicsDropShadowEffectCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphicsDropShadowEffectCall8 call = reinterpret_cast<CuteQGraphicsDropShadowEffectCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QGraphicsDropShadowEffect::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QGraphicsDropShadowEffect10metaObjectEv(
    const QGraphicsDropShadowEffect *self) {
  return self->metaObject();
}

//  QString QGraphicsDropShadowEffect::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QGraphicsDropShadowEffect2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsDropShadowEffect::tr(s, c, n));
}

//  QGraphicsDropShadowEffect::QGraphicsDropShadowEffect(QObject *parent)
extern "C" Q_DECL_EXPORT
QGraphicsDropShadowEffect *ritual_ZN25QGraphicsDropShadowEffectC1EP7QObject(
    QObject *parent) {
  return new CuteQGraphicsDropShadowEffect(parent);
}

//  QGraphicsDropShadowEffect::~QGraphicsDropShadowEffect()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsDropShadowEffectD1Ev(
    QGraphicsDropShadowEffect *self) {
  delete self;
}

//  QRectF QGraphicsDropShadowEffect::boundingRectFor(const QRectF &rect)
//      const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK25QGraphicsDropShadowEffect15boundingRectForERK6QRectF(
    const QGraphicsDropShadowEffect *self,
    const QRectF *rect) {
  return new QRectF(self->boundingRectFor(*rect));
}

//  QPointF QGraphicsDropShadowEffect::offset() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK25QGraphicsDropShadowEffect6offsetEv(
    const QGraphicsDropShadowEffect *self) {
  return new QPointF(self->offset());
}

//  qreal QGraphicsDropShadowEffect::xOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QGraphicsDropShadowEffect7xOffsetEv(
    const QGraphicsDropShadowEffect *self) {
  return self->xOffset();
}

//  qreal QGraphicsDropShadowEffect::yOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QGraphicsDropShadowEffect7yOffsetEv(
    const QGraphicsDropShadowEffect *self) {
  return self->yOffset();
}

//  qreal QGraphicsDropShadowEffect::blurRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QGraphicsDropShadowEffect10blurRadiusEv(
    const QGraphicsDropShadowEffect *self) {
  return self->blurRadius();
}

//  QColor QGraphicsDropShadowEffect::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK25QGraphicsDropShadowEffect5colorEv(
    const QGraphicsDropShadowEffect *self) {
  return new QColor(self->color());
}

//  void QGraphicsDropShadowEffect::setOffset(const QPointF &ofs)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsDropShadowEffect9setOffsetERK7QPointF(
    QGraphicsDropShadowEffect *self,
    const QPointF *ofs) {
  self->setOffset(*ofs);
}

//  void QGraphicsDropShadowEffect::setOffset(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsDropShadowEffect9setOffsetEdd(
    QGraphicsDropShadowEffect *self,
    qreal dx,
    qreal dy) {
  self->setOffset(dx, dy);
}

//  void QGraphicsDropShadowEffect::setOffset(qreal d)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsDropShadowEffect9setOffsetEd(
    QGraphicsDropShadowEffect *self,
    qreal d) {
  self->setOffset(d);
}

//  void QGraphicsDropShadowEffect::setXOffset(qreal dx)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsDropShadowEffect10setXOffsetEd(
    QGraphicsDropShadowEffect *self,
    qreal dx) {
  self->setXOffset(dx);
}

//  void QGraphicsDropShadowEffect::setYOffset(qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsDropShadowEffect10setYOffsetEd(
    QGraphicsDropShadowEffect *self,
    qreal dy) {
  self->setYOffset(dy);
}

//  void QGraphicsDropShadowEffect::setBlurRadius(qreal blurRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsDropShadowEffect13setBlurRadiusEd(
    QGraphicsDropShadowEffect *self,
    qreal blurRadius) {
  self->setBlurRadius(blurRadius);
}

//  void QGraphicsDropShadowEffect::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsDropShadowEffect8setColorERK6QColor(
    QGraphicsDropShadowEffect *self,
    const QColor *color) {
  self->setColor(*color);
}

//  a Python function taken by a CuteQGraphicsDropShadowEffect, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsDropShadowEffect(
    QGraphicsDropShadowEffect *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsDropShadowEffect *>(self)->take(key, call);
}

//  QRectF QGraphicsDropShadowEffect::boundingRectFor(const QRectF &rect)
//      const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK25QGraphicsDropShadowEffect15boundingRectForERK6QRectF(
    const QGraphicsDropShadowEffect *self,
    const QRectF *rect) {
  return new QRectF(self->QGraphicsDropShadowEffect::boundingRectFor(*rect));
}

//  void QGraphicsDropShadowEffect::draw(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QGraphicsDropShadowEffect4drawEP8QPainter(
    QGraphicsDropShadowEffect *self,
    QPainter *painter) {
  static_cast<OwnQGraphicsDropShadowEffect *>(self)->OwnQGraphicsDropShadowEffect::draw(
      painter);
}
