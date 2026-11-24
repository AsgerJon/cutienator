//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicseffect.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(graphicseffect)
#include <QtWidgets/qgraphicseffect.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QGraphicsEffect may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGraphicsEffect : QGraphicsEffect {
  using QGraphicsEffect::sourceChanged;
};

//  A QGraphicsEffect that Python can take functions over in. Every QGraphicsEffect
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicseffect)
typedef const QRectF * (*CuteQGraphicsEffectCall0)(const void *, const QRectF *, int *);
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
typedef void (*CuteQGraphicsEffectCall1)(const void *, QPainter *, int *);
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
typedef void (*CuteQGraphicsEffectCall2)(const void *, int, int *);
#endif  // QT_CONFIG(graphicseffect)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGraphicsEffectCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGraphicsEffectCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsEffectCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsEffectCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsEffectCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsEffectCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsEffectCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGraphicsEffect : public QGraphicsEffect {
public:
  using QGraphicsEffect::QGraphicsEffect;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZNK15QGraphicsEffect15boundingRectForERK6QRectF")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZN15QGraphicsEffect4drawEP8QPainter")) {
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
  //  QRectF QGraphicsEffect::boundingRectFor(const QRectF &sourceRect)
  //      const
  QRectF boundingRectFor(const QRectF &sourceRect) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsEffectCall0 call = reinterpret_cast<CuteQGraphicsEffectCall0>(taken[0]);
      const QRectF * given = call(this, &sourceRect, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsEffect::boundingRectFor(sourceRect);
  }
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
  //  void QGraphicsEffect::draw(QPainter *painter)
  void draw(QPainter *painter) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsEffectCall1 call = reinterpret_cast<CuteQGraphicsEffectCall1>(taken[1]);
      call(this, painter, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
  //  void QGraphicsEffect::sourceChanged(ChangeFlags flags)
  void sourceChanged(QGraphicsEffect::ChangeFlags flags) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsEffectCall2 call = reinterpret_cast<CuteQGraphicsEffectCall2>(taken[2]);
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
      CuteQGraphicsEffectCall3 call = reinterpret_cast<CuteQGraphicsEffectCall3>(taken[3]);
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
      CuteQGraphicsEffectCall4 call = reinterpret_cast<CuteQGraphicsEffectCall4>(taken[4]);
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
      CuteQGraphicsEffectCall5 call = reinterpret_cast<CuteQGraphicsEffectCall5>(taken[5]);
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
      CuteQGraphicsEffectCall6 call = reinterpret_cast<CuteQGraphicsEffectCall6>(taken[6]);
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
      CuteQGraphicsEffectCall7 call = reinterpret_cast<CuteQGraphicsEffectCall7>(taken[7]);
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
      CuteQGraphicsEffectCall8 call = reinterpret_cast<CuteQGraphicsEffectCall8>(taken[8]);
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
      CuteQGraphicsEffectCall9 call = reinterpret_cast<CuteQGraphicsEffectCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGraphicsEffect::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QGraphicsEffect10metaObjectEv(
    const QGraphicsEffect *self) {
  return self->metaObject();
}

//  QString QGraphicsEffect::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QGraphicsEffect2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsEffect::tr(s, c, n));
}

//  QGraphicsEffect::~QGraphicsEffect()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsEffectD1Ev(QGraphicsEffect *self) {
  delete self;
}

//  QRectF QGraphicsEffect::boundingRectFor(const QRectF &sourceRect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK15QGraphicsEffect15boundingRectForERK6QRectF(
    const QGraphicsEffect *self,
    const QRectF *sourceRect) {
  return new QRectF(self->boundingRectFor(*sourceRect));
}

//  QRectF QGraphicsEffect::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK15QGraphicsEffect12boundingRectEv(
    const QGraphicsEffect *self) {
  return new QRectF(self->boundingRect());
}

//  bool QGraphicsEffect::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QGraphicsEffect9isEnabledEv(const QGraphicsEffect *self) {
  return self->isEnabled();
}

//  void QGraphicsEffect::setEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsEffect10setEnabledEb(
    QGraphicsEffect *self,
    bool enable) {
  self->setEnabled(enable);
}

//  void QGraphicsEffect::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsEffect6updateEv(QGraphicsEffect *self) {
  self->update();
}

//  void QGraphicsEffect::draw(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsEffect4drawEP8QPainter(
    QGraphicsEffect *self,
    QPainter *painter) {
  self->draw(painter);
}

//  void QGraphicsEffect::sourceChanged(ChangeFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsEffect13sourceChangedE6QFlagsINS_10ChangeFlagEE(
    QGraphicsEffect *self,
    int flags) {
  self->sourceChanged(QFlags<QGraphicsEffect::ChangeFlag>::fromInt(flags));
}

//  void QGraphicsEffect::updateBoundingRect()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsEffect18updateBoundingRectEv(
    QGraphicsEffect *self) {
  self->updateBoundingRect();
}

//  bool QGraphicsEffect::sourceIsPixmap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QGraphicsEffect14sourceIsPixmapEv(
    const QGraphicsEffect *self) {
  return self->sourceIsPixmap();
}

//  QRectF QGraphicsEffect::sourceBoundingRect(Qt::CoordinateSystem system)
//      const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK15QGraphicsEffect18sourceBoundingRectEN2Qt16CoordinateSystemE(
    const QGraphicsEffect *self,
    Qt::CoordinateSystem system) {
  return new QRectF(self->sourceBoundingRect(system));
}

//  void QGraphicsEffect::drawSource(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QGraphicsEffect10drawSourceEP8QPainter(
    QGraphicsEffect *self,
    QPainter *painter) {
  self->drawSource(painter);
}

//  QPixmap QGraphicsEffect::sourcePixmap(Qt::CoordinateSystem system, QPoint
//      *offset, PixmapPadMode mode) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK15QGraphicsEffect12sourcePixmapEN2Qt16CoordinateSystemEP6QPointNS_13PixmapPadModeE(
    const QGraphicsEffect *self,
    Qt::CoordinateSystem system,
    QPoint *offset,
    QGraphicsEffect::PixmapPadMode mode) {
  return new QPixmap(self->sourcePixmap(system, offset, mode));
}

//  QGraphicsEffectPrivate *QGraphicsEffect::d_func()
extern "C" Q_DECL_EXPORT
QGraphicsEffectPrivate *ritual_ZN15QGraphicsEffect6d_funcEv(
    QGraphicsEffect *self) {
  return self->d_func();
}

//  const QGraphicsEffectPrivate *QGraphicsEffect::d_func() const
extern "C" Q_DECL_EXPORT
const QGraphicsEffectPrivate *ritual_ZNK15QGraphicsEffect6d_funcEv(
    const QGraphicsEffect *self) {
  return self->d_func();
}

//  QGraphicsEffectSource *QGraphicsEffect::source() const
extern "C" Q_DECL_EXPORT
QGraphicsEffectSource *ritual_ZNK15QGraphicsEffect6sourceEv(
    const QGraphicsEffect *self) {
  return self->source();
}

//  a Python function taken by a CuteQGraphicsEffect, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsEffect(
    QGraphicsEffect *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsEffect *>(self)->take(key, call);
}

//  QRectF QGraphicsEffect::boundingRectFor(const QRectF &sourceRect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK15QGraphicsEffect15boundingRectForERK6QRectF(
    const QGraphicsEffect *self,
    const QRectF *sourceRect) {
  return new QRectF(self->QGraphicsEffect::boundingRectFor(*sourceRect));
}

//  void QGraphicsEffect::sourceChanged(ChangeFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QGraphicsEffect13sourceChangedE6QFlagsINS_10ChangeFlagEE(
    QGraphicsEffect *self,
    int flags) {
  static_cast<OwnQGraphicsEffect *>(self)->OwnQGraphicsEffect::sourceChanged(
      QFlags<QGraphicsEffect::ChangeFlag>::fromInt(flags));
}

#endif  // QT_CONFIG(graphicseffect)
