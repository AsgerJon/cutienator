//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qscatterseries.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#if QT_CONFIG(charts_scatter_chart)
#include <QtCharts/qscatterseries.h>
#include <QtCore/qstring.h>
#include <QtGui/qpen.h>
#include <QtGui/qbrush.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QScatterSeries that Python can take functions over in. Every QScatterSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQScatterSeriesCall0)(const void *, int *);
typedef void (*CuteQScatterSeriesCall1)(const void *, const QPen *, int *);
typedef void (*CuteQScatterSeriesCall2)(const void *, const QBrush *, int *);
typedef void (*CuteQScatterSeriesCall3)(const void *, const QColor *, int *);
typedef const QColor * (*CuteQScatterSeriesCall4)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScatterSeriesCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQScatterSeriesCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatterSeriesCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatterSeriesCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatterSeriesCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatterSeriesCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQScatterSeriesCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQScatterSeries : public QScatterSeries {
public:
  using QScatterSeries::QScatterSeries;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK15QAbstractSeries4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QXYSeries6setPenERK4QPen")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QXYSeries8setBrushERK6QBrush")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QXYSeries8setColorERK6QColor")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QXYSeries5colorEv")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QAbstractSeries::SeriesType QScatterSeries::type() const
  QAbstractSeries::SeriesType type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQScatterSeriesCall0 call = reinterpret_cast<CuteQScatterSeriesCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries::SeriesType>(given);
    }
    return QScatterSeries::type();
  }

  //  void QScatterSeries::setPen(const QPen &pen)
  void setPen(const QPen &pen) override {
    if (taken[1]) {
      int handled = 0;
      CuteQScatterSeriesCall1 call = reinterpret_cast<CuteQScatterSeriesCall1>(taken[1]);
      call(this, &pen, &handled);
      if (handled) return;
    }
    QScatterSeries::setPen(pen);
  }

  //  void QScatterSeries::setBrush(const QBrush &brush)
  void setBrush(const QBrush &brush) override {
    if (taken[2]) {
      int handled = 0;
      CuteQScatterSeriesCall2 call = reinterpret_cast<CuteQScatterSeriesCall2>(taken[2]);
      call(this, &brush, &handled);
      if (handled) return;
    }
    QScatterSeries::setBrush(brush);
  }

  //  void QScatterSeries::setColor(const QColor &color)
  void setColor(const QColor &color) override {
    if (taken[3]) {
      int handled = 0;
      CuteQScatterSeriesCall3 call = reinterpret_cast<CuteQScatterSeriesCall3>(taken[3]);
      call(this, &color, &handled);
      if (handled) return;
    }
    QScatterSeries::setColor(color);
  }

  //  QColor QScatterSeries::color() const
  QColor color() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQScatterSeriesCall4 call = reinterpret_cast<CuteQScatterSeriesCall4>(taken[4]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QScatterSeries::color();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQScatterSeriesCall5 call = reinterpret_cast<CuteQScatterSeriesCall5>(taken[5]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQScatterSeriesCall6 call = reinterpret_cast<CuteQScatterSeriesCall6>(taken[6]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQScatterSeriesCall7 call = reinterpret_cast<CuteQScatterSeriesCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQScatterSeriesCall8 call = reinterpret_cast<CuteQScatterSeriesCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQScatterSeriesCall9 call = reinterpret_cast<CuteQScatterSeriesCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQScatterSeriesCall10 call = reinterpret_cast<CuteQScatterSeriesCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQScatterSeriesCall11 call = reinterpret_cast<CuteQScatterSeriesCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QScatterSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QScatterSeries10metaObjectEv(
    const QScatterSeries *self) {
  return self->metaObject();
}

//  void *QScatterSeries::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QScatterSeries11qt_metacastEPKc(
    QScatterSeries *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QScatterSeries::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QScatterSeries11qt_metacallEN11QMetaObject4CallEiPPv(
    QScatterSeries *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QScatterSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QScatterSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QScatterSeries::tr(s, c, n));
}

//  QScatterSeries::QScatterSeries(QObject *parent)
extern "C" Q_DECL_EXPORT
QScatterSeries *ritual_ZN14QScatterSeriesC1EP7QObject(QObject *parent) {
  return new CuteQScatterSeries(parent);
}

//  QScatterSeries::~QScatterSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScatterSeriesD1Ev(QScatterSeries *self) {
  delete self;
}

//  QAbstractSeries::SeriesType QScatterSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_ZNK14QScatterSeries4typeEv(
    const QScatterSeries *self) {
  return self->type();
}

//  void QScatterSeries::setPen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScatterSeries6setPenERK4QPen(
    QScatterSeries *self,
    const QPen *pen) {
  self->setPen(*pen);
}

//  void QScatterSeries::setBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScatterSeries8setBrushERK6QBrush(
    QScatterSeries *self,
    const QBrush *brush) {
  self->setBrush(*brush);
}

//  QBrush QScatterSeries::brush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK14QScatterSeries5brushEv(const QScatterSeries *self) {
  return new QBrush(self->brush());
}

//  void QScatterSeries::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScatterSeries8setColorERK6QColor(
    QScatterSeries *self,
    const QColor *color) {
  self->setColor(*color);
}

//  QColor QScatterSeries::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK14QScatterSeries5colorEv(const QScatterSeries *self) {
  return new QColor(self->color());
}

//  void QScatterSeries::setBorderColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScatterSeries14setBorderColorERK6QColor(
    QScatterSeries *self,
    const QColor *color) {
  self->setBorderColor(*color);
}

//  QColor QScatterSeries::borderColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK14QScatterSeries11borderColorEv(
    const QScatterSeries *self) {
  return new QColor(self->borderColor());
}

//  MarkerShape QScatterSeries::markerShape() const
extern "C" Q_DECL_EXPORT
QScatterSeries::MarkerShape ritual_ZNK14QScatterSeries11markerShapeEv(
    const QScatterSeries *self) {
  return self->markerShape();
}

//  void QScatterSeries::setMarkerShape(MarkerShape shape)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScatterSeries14setMarkerShapeENS_11MarkerShapeE(
    QScatterSeries *self,
    QScatterSeries::MarkerShape shape) {
  self->setMarkerShape(shape);
}

//  qreal QScatterSeries::markerSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QScatterSeries10markerSizeEv(const QScatterSeries *self) {
  return self->markerSize();
}

//  void QScatterSeries::setMarkerSize(qreal size)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScatterSeries13setMarkerSizeEd(
    QScatterSeries *self,
    qreal size) {
  self->setMarkerSize(size);
}

//  void QScatterSeries::colorChanged(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScatterSeries12colorChangedE6QColor(
    QScatterSeries *self,
    const QColor *color) {
  self->colorChanged(*color);
}

//  void QScatterSeries::borderColorChanged(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScatterSeries18borderColorChangedE6QColor(
    QScatterSeries *self,
    const QColor *color) {
  self->borderColorChanged(*color);
}

//  void QScatterSeries::markerShapeChanged(MarkerShape shape)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScatterSeries18markerShapeChangedENS_11MarkerShapeE(
    QScatterSeries *self,
    QScatterSeries::MarkerShape shape) {
  self->markerShapeChanged(shape);
}

//  void QScatterSeries::markerSizeChanged(qreal size)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScatterSeries17markerSizeChangedEd(
    QScatterSeries *self,
    qreal size) {
  self->markerSizeChanged(size);
}

//  QScatterSeriesPrivate *QScatterSeries::d_func()
extern "C" Q_DECL_EXPORT
QScatterSeriesPrivate *ritual_ZN14QScatterSeries6d_funcEv(
    QScatterSeries *self) {
  return self->d_func();
}

//  const QScatterSeriesPrivate *QScatterSeries::d_func() const
extern "C" Q_DECL_EXPORT
const QScatterSeriesPrivate *ritual_ZNK14QScatterSeries6d_funcEv(
    const QScatterSeries *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQScatterSeries, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScatterSeries(
    QScatterSeries *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScatterSeries *>(self)->take(key, call);
}

//  QAbstractSeries::SeriesType QScatterSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_own_ZNK14QScatterSeries4typeEv(
    const QScatterSeries *self) {
  return self->QScatterSeries::type();
}

//  void QScatterSeries::setPen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QScatterSeries6setPenERK4QPen(
    QScatterSeries *self,
    const QPen *pen) {
  self->QScatterSeries::setPen(*pen);
}

//  void QScatterSeries::setBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QScatterSeries8setBrushERK6QBrush(
    QScatterSeries *self,
    const QBrush *brush) {
  self->QScatterSeries::setBrush(*brush);
}

//  void QScatterSeries::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QScatterSeries8setColorERK6QColor(
    QScatterSeries *self,
    const QColor *color) {
  self->QScatterSeries::setColor(*color);
}

//  QColor QScatterSeries::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_own_ZNK14QScatterSeries5colorEv(const QScatterSeries *self) {
  return new QColor(self->QScatterSeries::color());
}

#endif  // QT_CONFIG(charts_scatter_chart)
