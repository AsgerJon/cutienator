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
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPixmapConvolutionFilter that Python can take functions over in. Every QPixmapConvolutionFilter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicseffect)
typedef const QRectF * (*CuteQPixmapConvolutionFilterCall0)(const void *, const QRectF *, int *);
#endif  // QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
typedef void (*CuteQPixmapConvolutionFilterCall1)(const void *, QPainter *, const QPointF *, const QPixmap *, const QRectF *, int *);
#endif  // QT_CONFIG(graphicseffect)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPixmapConvolutionFilterCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPixmapConvolutionFilterCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPixmapConvolutionFilterCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPixmapConvolutionFilterCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPixmapConvolutionFilterCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPixmapConvolutionFilterCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPixmapConvolutionFilterCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPixmapConvolutionFilter : public QPixmapConvolutionFilter {
public:
  using QPixmapConvolutionFilter::QPixmapConvolutionFilter;
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
  //  QRectF QPixmapConvolutionFilter::boundingRectFor(const QRectF &rect)
  //      const
  QRectF boundingRectFor(const QRectF &rect) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPixmapConvolutionFilterCall0 call = reinterpret_cast<CuteQPixmapConvolutionFilterCall0>(taken[0]);
      const QRectF * given = call(this, &rect, &handled);
      if (handled && given) return *given;
    }
    return QPixmapConvolutionFilter::boundingRectFor(rect);
  }
#endif  // QT_CONFIG(graphicseffect)

#if QT_CONFIG(graphicseffect)
  //  void QPixmapConvolutionFilter::draw(QPainter *painter, const QPointF
  //      &dest, const QPixmap &src, const QRectF &srcRect) const
  void draw(
      QPainter *painter,
      const QPointF &dest,
      const QPixmap &src,
      const QRectF &srcRect) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPixmapConvolutionFilterCall1 call = reinterpret_cast<CuteQPixmapConvolutionFilterCall1>(taken[1]);
      call(this, painter, &dest, &src, &srcRect, &handled);
      if (handled) return;
    }
    QPixmapConvolutionFilter::draw(painter, dest, src, srcRect);
  }
#endif  // QT_CONFIG(graphicseffect)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPixmapConvolutionFilterCall2 call = reinterpret_cast<CuteQPixmapConvolutionFilterCall2>(taken[2]);
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
      CuteQPixmapConvolutionFilterCall3 call = reinterpret_cast<CuteQPixmapConvolutionFilterCall3>(taken[3]);
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
      CuteQPixmapConvolutionFilterCall4 call = reinterpret_cast<CuteQPixmapConvolutionFilterCall4>(taken[4]);
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
      CuteQPixmapConvolutionFilterCall5 call = reinterpret_cast<CuteQPixmapConvolutionFilterCall5>(taken[5]);
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
      CuteQPixmapConvolutionFilterCall6 call = reinterpret_cast<CuteQPixmapConvolutionFilterCall6>(taken[6]);
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
      CuteQPixmapConvolutionFilterCall7 call = reinterpret_cast<CuteQPixmapConvolutionFilterCall7>(taken[7]);
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
      CuteQPixmapConvolutionFilterCall8 call = reinterpret_cast<CuteQPixmapConvolutionFilterCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPixmapConvolutionFilter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QPixmapConvolutionFilter10metaObjectEv(
    const QPixmapConvolutionFilter *self) {
  return self->metaObject();
}

//  QString QPixmapConvolutionFilter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QPixmapConvolutionFilter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPixmapConvolutionFilter::tr(s, c, n));
}

//  QPixmapConvolutionFilter::QPixmapConvolutionFilter(QObject *parent)
extern "C" Q_DECL_EXPORT
QPixmapConvolutionFilter *ritual_ZN24QPixmapConvolutionFilterC1EP7QObject(
    QObject *parent) {
  return new CuteQPixmapConvolutionFilter(parent);
}

//  QPixmapConvolutionFilter::~QPixmapConvolutionFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPixmapConvolutionFilterD1Ev(
    QPixmapConvolutionFilter *self) {
  delete self;
}

//  QRectF QPixmapConvolutionFilter::boundingRectFor(const QRectF &rect)
//      const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK24QPixmapConvolutionFilter15boundingRectForERK6QRectF(
    const QPixmapConvolutionFilter *self,
    const QRectF *rect) {
  return new QRectF(self->boundingRectFor(*rect));
}

//  void QPixmapConvolutionFilter::draw(QPainter *painter, const QPointF
//      &dest, const QPixmap &src, const QRectF &srcRect) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK24QPixmapConvolutionFilter4drawEP8QPainterRK7QPointFRK7QPixmapRK6QRectF(
    const QPixmapConvolutionFilter *self,
    QPainter *painter,
    const QPointF *dest,
    const QPixmap *src,
    const QRectF *srcRect) {
  self->draw(painter, *dest, *src, *srcRect);
}

//  int QPixmapConvolutionFilter::rows() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QPixmapConvolutionFilter4rowsEv(
    const QPixmapConvolutionFilter *self) {
  return self->rows();
}

//  int QPixmapConvolutionFilter::columns() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QPixmapConvolutionFilter7columnsEv(
    const QPixmapConvolutionFilter *self) {
  return self->columns();
}

//  a Python function taken by a CuteQPixmapConvolutionFilter, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPixmapConvolutionFilter(
    QPixmapConvolutionFilter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPixmapConvolutionFilter *>(self)->take(key, call);
}

//  QRectF QPixmapConvolutionFilter::boundingRectFor(const QRectF &rect)
//      const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK24QPixmapConvolutionFilter15boundingRectForERK6QRectF(
    const QPixmapConvolutionFilter *self,
    const QRectF *rect) {
  return new QRectF(self->QPixmapConvolutionFilter::boundingRectFor(*rect));
}

//  void QPixmapConvolutionFilter::draw(QPainter *painter, const QPointF
//      &dest, const QPixmap &src, const QRectF &srcRect) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK24QPixmapConvolutionFilter4drawEP8QPainterRK7QPointFRK7QPixmapRK6QRectF(
    const QPixmapConvolutionFilter *self,
    QPainter *painter,
    const QPointF *dest,
    const QPixmap *src,
    const QRectF *srcRect) {
  self->QPixmapConvolutionFilter::draw(painter, *dest, *src, *srcRect);
}

#endif  // QT_CONFIG(graphicseffect)
