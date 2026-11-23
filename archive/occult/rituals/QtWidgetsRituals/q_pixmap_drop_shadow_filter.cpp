//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qpixmapfilter_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/QtWidgets>
#include <QtWidgets/6.12.0/QtWidgets/private/qpixmapfilter_p.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPixmapDropShadowFilter that Python can take functions over in. Every QPixmapDropShadowFilter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QRectF * (*CuteQPixmapDropShadowFilterCall0)(const void *, const QRectF *, int *);
typedef void (*CuteQPixmapDropShadowFilterCall1)(const void *, QPainter *, const QPointF *, const QPixmap *, const QRectF *, int *);
typedef bool (*CuteQPixmapDropShadowFilterCall2)(const void *, QEvent *, int *);
typedef bool (*CuteQPixmapDropShadowFilterCall3)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQPixmapDropShadowFilterCall4)(const void *, QTimerEvent *, int *);
typedef void (*CuteQPixmapDropShadowFilterCall5)(const void *, QChildEvent *, int *);
typedef void (*CuteQPixmapDropShadowFilterCall6)(const void *, QEvent *, int *);
typedef void (*CuteQPixmapDropShadowFilterCall7)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQPixmapDropShadowFilterCall8)(const void *, const QMetaMethod *, int *);
class CuteQPixmapDropShadowFilter : public QPixmapDropShadowFilter {
public:
  using QPixmapDropShadowFilter::QPixmapDropShadowFilter;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK13QPixmapFilter15boundingRectForERK6QRectF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPixmapFilter4drawEP8QPainterRK7QPointFRK7QPixmapRK6QRectF")) {
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

  //  QRectF QPixmapDropShadowFilter::boundingRectFor(const QRectF &rect)
  //      const
  QRectF boundingRectFor(const QRectF &rect) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPixmapDropShadowFilterCall0 call = reinterpret_cast<CuteQPixmapDropShadowFilterCall0>(taken[0]);
      const QRectF * given = call(this, &rect, &handled);
      if (handled && given) return *given;
    }
    return QPixmapDropShadowFilter::boundingRectFor(rect);
  }

  //  void QPixmapDropShadowFilter::draw(QPainter *p, const QPointF &pos,
  //      const QPixmap &px, const QRectF &src) const
  void draw(
      QPainter *p,
      const QPointF &pos,
      const QPixmap &px,
      const QRectF &src) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPixmapDropShadowFilterCall1 call = reinterpret_cast<CuteQPixmapDropShadowFilterCall1>(taken[1]);
      call(this, p, &pos, &px, &src, &handled);
      if (handled) return;
    }
    QPixmapDropShadowFilter::draw(p, pos, px, src);
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPixmapDropShadowFilterCall2 call = reinterpret_cast<CuteQPixmapDropShadowFilterCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPixmapDropShadowFilterCall3 call = reinterpret_cast<CuteQPixmapDropShadowFilterCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPixmapDropShadowFilterCall4 call = reinterpret_cast<CuteQPixmapDropShadowFilterCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPixmapDropShadowFilterCall5 call = reinterpret_cast<CuteQPixmapDropShadowFilterCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPixmapDropShadowFilterCall6 call = reinterpret_cast<CuteQPixmapDropShadowFilterCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPixmapDropShadowFilterCall7 call = reinterpret_cast<CuteQPixmapDropShadowFilterCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQPixmapDropShadowFilterCall8 call = reinterpret_cast<CuteQPixmapDropShadowFilterCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QPixmapDropShadowFilter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QPixmapDropShadowFilter10metaObjectEv(
    const QPixmapDropShadowFilter *self) {
  return self->metaObject();
}

//  QString QPixmapDropShadowFilter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QPixmapDropShadowFilter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPixmapDropShadowFilter::tr(s, c, n));
}

//  QPixmapDropShadowFilter::QPixmapDropShadowFilter(QObject *parent)
extern "C" Q_DECL_EXPORT
QPixmapDropShadowFilter *ritual_ZN23QPixmapDropShadowFilterC1EP7QObject(
    QObject *parent) {
  return new CuteQPixmapDropShadowFilter(parent);
}

//  QPixmapDropShadowFilter::~QPixmapDropShadowFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPixmapDropShadowFilterD1Ev(QPixmapDropShadowFilter *self) {
  delete self;
}

//  QRectF QPixmapDropShadowFilter::boundingRectFor(const QRectF &rect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK23QPixmapDropShadowFilter15boundingRectForERK6QRectF(
    const QPixmapDropShadowFilter *self,
    const QRectF *rect) {
  return new QRectF(self->boundingRectFor(*rect));
}

//  void QPixmapDropShadowFilter::draw(QPainter *p, const QPointF &pos, const
//      QPixmap &px, const QRectF &src) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK23QPixmapDropShadowFilter4drawEP8QPainterRK7QPointFRK7QPixmapRK6QRectF(
    const QPixmapDropShadowFilter *self,
    QPainter *p,
    const QPointF *pos,
    const QPixmap *px,
    const QRectF *src) {
  self->draw(p, *pos, *px, *src);
}

//  qreal QPixmapDropShadowFilter::blurRadius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QPixmapDropShadowFilter10blurRadiusEv(
    const QPixmapDropShadowFilter *self) {
  return self->blurRadius();
}

//  void QPixmapDropShadowFilter::setBlurRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPixmapDropShadowFilter13setBlurRadiusEd(
    QPixmapDropShadowFilter *self,
    qreal radius) {
  self->setBlurRadius(radius);
}

//  QColor QPixmapDropShadowFilter::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK23QPixmapDropShadowFilter5colorEv(
    const QPixmapDropShadowFilter *self) {
  return new QColor(self->color());
}

//  void QPixmapDropShadowFilter::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPixmapDropShadowFilter8setColorERK6QColor(
    QPixmapDropShadowFilter *self,
    const QColor *color) {
  self->setColor(*color);
}

//  QPointF QPixmapDropShadowFilter::offset() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK23QPixmapDropShadowFilter6offsetEv(
    const QPixmapDropShadowFilter *self) {
  return new QPointF(self->offset());
}

//  void QPixmapDropShadowFilter::setOffset(const QPointF &offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPixmapDropShadowFilter9setOffsetERK7QPointF(
    QPixmapDropShadowFilter *self,
    const QPointF *offset) {
  self->setOffset(*offset);
}

//  void QPixmapDropShadowFilter::setOffset(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPixmapDropShadowFilter9setOffsetEdd(
    QPixmapDropShadowFilter *self,
    qreal dx,
    qreal dy) {
  self->setOffset(dx, dy);
}

//  a Python function taken by a CuteQPixmapDropShadowFilter, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPixmapDropShadowFilter(
    QPixmapDropShadowFilter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPixmapDropShadowFilter *>(self)->take(key, call);
}

//  QRectF QPixmapDropShadowFilter::boundingRectFor(const QRectF &rect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK23QPixmapDropShadowFilter15boundingRectForERK6QRectF(
    const QPixmapDropShadowFilter *self,
    const QRectF *rect) {
  return new QRectF(self->QPixmapDropShadowFilter::boundingRectFor(*rect));
}

//  void QPixmapDropShadowFilter::draw(QPainter *p, const QPointF &pos, const
//      QPixmap &px, const QRectF &src) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK23QPixmapDropShadowFilter4drawEP8QPainterRK7QPointFRK7QPixmapRK6QRectF(
    const QPixmapDropShadowFilter *self,
    QPainter *p,
    const QPointF *pos,
    const QPixmap *px,
    const QRectF *src) {
  self->QPixmapDropShadowFilter::draw(p, *pos, *px, *src);
}
