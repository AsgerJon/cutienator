//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicseffect_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicseffect)
#if QT_CONFIG(graphicseffect)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicseffect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QGraphicsEffectSource that Python can take functions over in. Every QGraphicsEffectSource
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGraphicsEffectSourceCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGraphicsEffectSourceCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsEffectSourceCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsEffectSourceCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsEffectSourceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsEffectSourceCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGraphicsEffectSourceCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGraphicsEffectSource : public QGraphicsEffectSource {
public:
  using QGraphicsEffectSource::QGraphicsEffectSource;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsEffectSourceCall0 call = reinterpret_cast<CuteQGraphicsEffectSourceCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsEffectSourceCall1 call = reinterpret_cast<CuteQGraphicsEffectSourceCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsEffectSourceCall2 call = reinterpret_cast<CuteQGraphicsEffectSourceCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsEffectSourceCall3 call = reinterpret_cast<CuteQGraphicsEffectSourceCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsEffectSourceCall4 call = reinterpret_cast<CuteQGraphicsEffectSourceCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsEffectSourceCall5 call = reinterpret_cast<CuteQGraphicsEffectSourceCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsEffectSourceCall6 call = reinterpret_cast<CuteQGraphicsEffectSourceCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGraphicsEffectSource::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QGraphicsEffectSource10metaObjectEv(
    const QGraphicsEffectSource *self) {
  return self->metaObject();
}

//  QString QGraphicsEffectSource::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QGraphicsEffectSource2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsEffectSource::tr(s, c, n));
}

//  QGraphicsEffectSource::~QGraphicsEffectSource()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsEffectSourceD1Ev(QGraphicsEffectSource *self) {
  delete self;
}

//  const QGraphicsItem *QGraphicsEffectSource::graphicsItem() const
extern "C" Q_DECL_EXPORT
const QGraphicsItem *ritual_ZNK21QGraphicsEffectSource12graphicsItemEv(
    const QGraphicsEffectSource *self) {
  return self->graphicsItem();
}

//  const QWidget *QGraphicsEffectSource::widget() const
extern "C" Q_DECL_EXPORT
const QWidget *ritual_ZNK21QGraphicsEffectSource6widgetEv(
    const QGraphicsEffectSource *self) {
  return self->widget();
}

//  const QStyleOption *QGraphicsEffectSource::styleOption() const
extern "C" Q_DECL_EXPORT
const QStyleOption *ritual_ZNK21QGraphicsEffectSource11styleOptionEv(
    const QGraphicsEffectSource *self) {
  return self->styleOption();
}

//  bool QGraphicsEffectSource::isPixmap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QGraphicsEffectSource8isPixmapEv(
    const QGraphicsEffectSource *self) {
  return self->isPixmap();
}

//  void QGraphicsEffectSource::draw(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsEffectSource4drawEP8QPainter(
    QGraphicsEffectSource *self,
    QPainter *painter) {
  self->draw(painter);
}

//  void QGraphicsEffectSource::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QGraphicsEffectSource6updateEv(QGraphicsEffectSource *self) {
  self->update();
}

//  QRectF QGraphicsEffectSource::boundingRect(Qt::CoordinateSystem
//      coordinateSystem) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK21QGraphicsEffectSource12boundingRectEN2Qt16CoordinateSystemE(
    const QGraphicsEffectSource *self,
    Qt::CoordinateSystem coordinateSystem) {
  return new QRectF(self->boundingRect(coordinateSystem));
}

//  QPixmap QGraphicsEffectSource::pixmap(Qt::CoordinateSystem system, QPoint
//      *offset, QGraphicsEffect::PixmapPadMode mode) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK21QGraphicsEffectSource6pixmapEN2Qt16CoordinateSystemEP6QPointN15QGraphicsEffect13PixmapPadModeE(
    const QGraphicsEffectSource *self,
    Qt::CoordinateSystem system,
    QPoint *offset,
    QGraphicsEffect::PixmapPadMode mode) {
  return new QPixmap(self->pixmap(system, offset, mode));
}

//  QGraphicsEffectSourcePrivate *QGraphicsEffectSource::d_func()
extern "C" Q_DECL_EXPORT
QGraphicsEffectSourcePrivate *ritual_ZN21QGraphicsEffectSource6d_funcEv(
    QGraphicsEffectSource *self) {
  return self->d_func();
}

//  const QGraphicsEffectSourcePrivate *QGraphicsEffectSource::d_func() const
extern "C" Q_DECL_EXPORT
const QGraphicsEffectSourcePrivate *ritual_ZNK21QGraphicsEffectSource6d_funcEv(
    const QGraphicsEffectSource *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQGraphicsEffectSource, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsEffectSource(
    QGraphicsEffectSource *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsEffectSource *>(self)->take(key, call);
}

#endif  // QT_CONFIG(graphicseffect)
#endif  // QT_CONFIG(graphicseffect)
