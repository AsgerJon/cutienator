//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qpixmapfilter_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicseffect)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qpixmapfilter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qpoint.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPixmapColorizeFilter that Python can take functions over in. Every QPixmapColorizeFilter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicseffect)
typedef void (*CuteQPixmapColorizeFilterCall0)(const void *, QPainter *, const QPointF *, const QPixmap *, const QRectF *, int *);
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
typedef const QRectF * (*CuteQPixmapColorizeFilterCall1)(const void *, const QRectF *, int *);
#endif  // QT_CONFIG(graphicseffect)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPixmapColorizeFilterCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPixmapColorizeFilterCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPixmapColorizeFilterCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPixmapColorizeFilterCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPixmapColorizeFilterCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPixmapColorizeFilterCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPixmapColorizeFilterCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPixmapColorizeFilter : public QPixmapColorizeFilter {
public:
  using QPixmapColorizeFilter::QPixmapColorizeFilter;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZNK13QPixmapFilter4drawEP8QPainterRK7QPointFRK7QPixmapRK6QRectF")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
    if (!std::strcmp(key, "_ZNK13QPixmapFilter15boundingRectForERK6QRectF")) {
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
  //  void QPixmapColorizeFilter::draw(QPainter *painter, const QPointF
  //      &dest, const QPixmap &src, const QRectF &srcRect) const
  void draw(
      QPainter *painter,
      const QPointF &dest,
      const QPixmap &src,
      const QRectF &srcRect) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPixmapColorizeFilterCall0 call = reinterpret_cast<CuteQPixmapColorizeFilterCall0>(taken[0]);
      call(this, painter, &dest, &src, &srcRect, &handled);
      if (handled) return;
    }
    QPixmapColorizeFilter::draw(painter, dest, src, srcRect);
  }
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
  //  QRectF QPixmapFilter::boundingRectFor(const QRectF &rect) const
  QRectF boundingRectFor(const QRectF &rect) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPixmapColorizeFilterCall1 call = reinterpret_cast<CuteQPixmapColorizeFilterCall1>(taken[1]);
      const QRectF * given = call(this, &rect, &handled);
      if (handled && given) return *given;
    }
    return QPixmapFilter::boundingRectFor(rect);
  }
#endif  // QT_CONFIG(graphicseffect)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPixmapColorizeFilterCall2 call = reinterpret_cast<CuteQPixmapColorizeFilterCall2>(taken[2]);
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
      CuteQPixmapColorizeFilterCall3 call = reinterpret_cast<CuteQPixmapColorizeFilterCall3>(taken[3]);
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
      CuteQPixmapColorizeFilterCall4 call = reinterpret_cast<CuteQPixmapColorizeFilterCall4>(taken[4]);
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
      CuteQPixmapColorizeFilterCall5 call = reinterpret_cast<CuteQPixmapColorizeFilterCall5>(taken[5]);
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
      CuteQPixmapColorizeFilterCall6 call = reinterpret_cast<CuteQPixmapColorizeFilterCall6>(taken[6]);
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
      CuteQPixmapColorizeFilterCall7 call = reinterpret_cast<CuteQPixmapColorizeFilterCall7>(taken[7]);
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
      CuteQPixmapColorizeFilterCall8 call = reinterpret_cast<CuteQPixmapColorizeFilterCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPixmapColorizeFilter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QPixmapColorizeFilter10metaObjectEv(
    const QPixmapColorizeFilter *self) {
  return self->metaObject();
}

//  QString QPixmapColorizeFilter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QPixmapColorizeFilter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPixmapColorizeFilter::tr(s, c, n));
}

//  QPixmapColorizeFilter::QPixmapColorizeFilter(QObject *parent)
extern "C" Q_DECL_EXPORT
QPixmapColorizeFilter *ritual_ZN21QPixmapColorizeFilterC1EP7QObject(
    QObject *parent) {
  return new CuteQPixmapColorizeFilter(parent);
}

//  QPixmapColorizeFilter::~QPixmapColorizeFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPixmapColorizeFilterD1Ev(QPixmapColorizeFilter *self) {
  delete self;
}

//  void QPixmapColorizeFilter::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPixmapColorizeFilter8setColorERK6QColor(
    QPixmapColorizeFilter *self,
    const QColor *color) {
  self->setColor(*color);
}

//  QColor QPixmapColorizeFilter::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK21QPixmapColorizeFilter5colorEv(
    const QPixmapColorizeFilter *self) {
  return new QColor(self->color());
}

//  void QPixmapColorizeFilter::setStrength(qreal strength)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPixmapColorizeFilter11setStrengthEd(
    QPixmapColorizeFilter *self,
    qreal strength) {
  self->setStrength(strength);
}

//  qreal QPixmapColorizeFilter::strength() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QPixmapColorizeFilter8strengthEv(
    const QPixmapColorizeFilter *self) {
  return self->strength();
}

//  void QPixmapColorizeFilter::draw(QPainter *painter, const QPointF &dest,
//      const QPixmap &src, const QRectF &srcRect) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QPixmapColorizeFilter4drawEP8QPainterRK7QPointFRK7QPixmapRK6QRectF(
    const QPixmapColorizeFilter *self,
    QPainter *painter,
    const QPointF *dest,
    const QPixmap *src,
    const QRectF *srcRect) {
  self->draw(painter, *dest, *src, *srcRect);
}

//  a Python function taken by a CuteQPixmapColorizeFilter, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPixmapColorizeFilter(
    QPixmapColorizeFilter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPixmapColorizeFilter *>(self)->take(key, call);
}

//  void QPixmapColorizeFilter::draw(QPainter *painter, const QPointF &dest,
//      const QPixmap &src, const QRectF &srcRect) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK21QPixmapColorizeFilter4drawEP8QPainterRK7QPointFRK7QPixmapRK6QRectF(
    const QPixmapColorizeFilter *self,
    QPainter *painter,
    const QPointF *dest,
    const QPixmap *src,
    const QRectF *srcRect) {
  self->QPixmapColorizeFilter::draw(painter, *dest, *src, *srcRect);
}

#endif  // QT_CONFIG(graphicseffect)
