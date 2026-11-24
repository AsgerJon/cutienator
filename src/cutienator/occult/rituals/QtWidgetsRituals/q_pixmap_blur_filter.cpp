//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qpixmapfilter_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qpixmapfilter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPixmapBlurFilter that Python can take functions over in. Every QPixmapBlurFilter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicseffect)
typedef const QRectF * (*CuteQPixmapBlurFilterCall0)(const void *, const QRectF *, int *);
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
typedef void (*CuteQPixmapBlurFilterCall1)(const void *, QPainter *, const QPointF *, const QPixmap *, const QRectF *, int *);
#endif  // QT_CONFIG(graphicseffect)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPixmapBlurFilterCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPixmapBlurFilterCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPixmapBlurFilterCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPixmapBlurFilterCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPixmapBlurFilterCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPixmapBlurFilterCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPixmapBlurFilterCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPixmapBlurFilter : public QPixmapBlurFilter {
public:
  using QPixmapBlurFilter::QPixmapBlurFilter;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZNK13QPixmapFilter15boundingRectForERK6QRectF")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZNK13QPixmapFilter4drawEP8QPainterRK7QPointFRK7QPixmapRK6QRectF")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(graphicseffect)
  //  QRectF QPixmapBlurFilter::boundingRectFor(const QRectF &rect) const
  QRectF boundingRectFor(const QRectF &rect) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPixmapBlurFilterCall0 call = reinterpret_cast<CuteQPixmapBlurFilterCall0>(taken[0]);
      const QRectF * given = call(this, &rect, &handled);
      if (handled && given) return *given;
    }
    return QPixmapBlurFilter::boundingRectFor(rect);
  }
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
  //  void QPixmapBlurFilter::draw(QPainter *painter, const QPointF &dest,
  //      const QPixmap &src, const QRectF &srcRect) const
  void draw(
      QPainter *painter,
      const QPointF &dest,
      const QPixmap &src,
      const QRectF &srcRect) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPixmapBlurFilterCall1 call = reinterpret_cast<CuteQPixmapBlurFilterCall1>(taken[1]);
      call(this, painter, &dest, &src, &srcRect, &handled);
      if (handled) return;
    }
    QPixmapBlurFilter::draw(painter, dest, src, srcRect);
  }
#endif  // QT_CONFIG(graphicseffect)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPixmapBlurFilterCall2 call = reinterpret_cast<CuteQPixmapBlurFilterCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPixmapBlurFilterCall3 call = reinterpret_cast<CuteQPixmapBlurFilterCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPixmapBlurFilterCall4 call = reinterpret_cast<CuteQPixmapBlurFilterCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPixmapBlurFilterCall5 call = reinterpret_cast<CuteQPixmapBlurFilterCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPixmapBlurFilterCall6 call = reinterpret_cast<CuteQPixmapBlurFilterCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPixmapBlurFilterCall7 call = reinterpret_cast<CuteQPixmapBlurFilterCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQPixmapBlurFilterCall8 call = reinterpret_cast<CuteQPixmapBlurFilterCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPixmapBlurFilter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QPixmapBlurFilter10metaObjectEv(
    const QPixmapBlurFilter *self) {
  return self->metaObject();
}

//  QString QPixmapBlurFilter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QPixmapBlurFilter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPixmapBlurFilter::tr(s, c, n));
}

//  QPixmapBlurFilter::QPixmapBlurFilter(QObject *parent)
extern "C" Q_DECL_EXPORT
QPixmapBlurFilter *ritual_ZN17QPixmapBlurFilterC1EP7QObject(
    QObject *parent) {
  return new CuteQPixmapBlurFilter(parent);
}

//  QPixmapBlurFilter::~QPixmapBlurFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPixmapBlurFilterD1Ev(QPixmapBlurFilter *self) {
  delete self;
}

//  void QPixmapBlurFilter::setRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPixmapBlurFilter9setRadiusEd(
    QPixmapBlurFilter *self,
    qreal radius) {
  self->setRadius(radius);
}

//  void QPixmapBlurFilter::setBlurHints(QGraphicsBlurEffect::BlurHints
//      hints)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPixmapBlurFilter12setBlurHintsE6QFlagsIN19QGraphicsBlurEffect8BlurHintEE(
    QPixmapBlurFilter *self,
    int hints) {
  self->setBlurHints(QFlags<QGraphicsBlurEffect::BlurHint>::fromInt(hints));
}

//  qreal QPixmapBlurFilter::radius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QPixmapBlurFilter6radiusEv(const QPixmapBlurFilter *self) {
  return self->radius();
}

//  QGraphicsBlurEffect::BlurHints QPixmapBlurFilter::blurHints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QPixmapBlurFilter9blurHintsEv(
    const QPixmapBlurFilter *self) {
  return static_cast<int>(self->blurHints().toInt());
}

//  QRectF QPixmapBlurFilter::boundingRectFor(const QRectF &rect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QPixmapBlurFilter15boundingRectForERK6QRectF(
    const QPixmapBlurFilter *self,
    const QRectF *rect) {
  return new QRectF(self->boundingRectFor(*rect));
}

//  void QPixmapBlurFilter::draw(QPainter *painter, const QPointF &dest,
//      const QPixmap &src, const QRectF &srcRect) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QPixmapBlurFilter4drawEP8QPainterRK7QPointFRK7QPixmapRK6QRectF(
    const QPixmapBlurFilter *self,
    QPainter *painter,
    const QPointF *dest,
    const QPixmap *src,
    const QRectF *srcRect) {
  self->draw(painter, *dest, *src, *srcRect);
}

//  a Python function taken by a CuteQPixmapBlurFilter, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPixmapBlurFilter(
    QPixmapBlurFilter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPixmapBlurFilter *>(self)->take(key, call);
}

//  QRectF QPixmapBlurFilter::boundingRectFor(const QRectF &rect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK17QPixmapBlurFilter15boundingRectForERK6QRectF(
    const QPixmapBlurFilter *self,
    const QRectF *rect) {
  return new QRectF(self->QPixmapBlurFilter::boundingRectFor(*rect));
}

//  void QPixmapBlurFilter::draw(QPainter *painter, const QPointF &dest,
//      const QPixmap &src, const QRectF &srcRect) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK17QPixmapBlurFilter4drawEP8QPainterRK7QPointFRK7QPixmapRK6QRectF(
    const QPixmapBlurFilter *self,
    QPainter *painter,
    const QPointF *dest,
    const QPixmap *src,
    const QRectF *srcRect) {
  self->QPixmapBlurFilter::draw(painter, *dest, *src, *srcRect);
}

#endif  // QT_CONFIG(graphicseffect)
#endif  // QT_CONFIG(graphicseffect)
