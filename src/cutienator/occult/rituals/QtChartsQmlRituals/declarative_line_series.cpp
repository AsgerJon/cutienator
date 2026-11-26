//  Written by dev_tooling.RitualGenerator from the records of
//  QtChartsQml/6.12.0/QtChartsQml/private/declarativelineseries_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtChartsQml/qtchartsqmlexports.h>
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#if QT_CONFIG(charts_line_chart)
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#include <QtChartsQml/QtChartsQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativelineseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtGui/qpen.h>
#include <QtGui/qbrush.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>

//  A DeclarativeLineSeries that Python can take functions over in. Every DeclarativeLineSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteDeclarativeLineSeriesCall0)(const void *, int *);
typedef void (*CuteDeclarativeLineSeriesCall1)(const void *, int *);
typedef void (*CuteDeclarativeLineSeriesCall2)(const void *, int *);
#if QT_CONFIG(charts_line_chart)
typedef int (*CuteDeclarativeLineSeriesCall3)(const void *, int *);
#endif  // QT_CONFIG(charts_line_chart)
typedef void (*CuteDeclarativeLineSeriesCall4)(const void *, const QPen *, int *);
typedef void (*CuteDeclarativeLineSeriesCall5)(const void *, const QBrush *, int *);
typedef void (*CuteDeclarativeLineSeriesCall6)(const void *, const QColor *, int *);
typedef const QColor * (*CuteDeclarativeLineSeriesCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteDeclarativeLineSeriesCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteDeclarativeLineSeriesCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeLineSeriesCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeLineSeriesCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeLineSeriesCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeLineSeriesCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeLineSeriesCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteDeclarativeLineSeries : public DeclarativeLineSeries {
public:
  using DeclarativeLineSeries::DeclarativeLineSeries;
  void *taken[15] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19DeclarativeXySeries8xySeriesEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19DeclarativeXySeries10classBeginEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19DeclarativeXySeries17componentCompleteEv")) {
      taken[2] = call;
      return true;
    }
#if QT_CONFIG(charts_line_chart)
    if (!std::strcmp(key, "_ZNK15QAbstractSeries4typeEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(charts_line_chart)
    if (!std::strcmp(key, "_ZN9QXYSeries6setPenERK4QPen")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QXYSeries8setBrushERK6QBrush")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QXYSeries8setColorERK6QColor")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QXYSeries5colorEv")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QXYSeries *DeclarativeLineSeries::xySeries()
  QXYSeries *xySeries() override {
    if (taken[0]) {
      int handled = 0;
      CuteDeclarativeLineSeriesCall0 call = reinterpret_cast<CuteDeclarativeLineSeriesCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QXYSeries *>(given);
    }
    return DeclarativeLineSeries::xySeries();
  }

  //  void DeclarativeLineSeries::classBegin()
  void classBegin() override {
    if (taken[1]) {
      int handled = 0;
      CuteDeclarativeLineSeriesCall1 call = reinterpret_cast<CuteDeclarativeLineSeriesCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    DeclarativeLineSeries::classBegin();
  }

  //  void DeclarativeLineSeries::componentComplete()
  void componentComplete() override {
    if (taken[2]) {
      int handled = 0;
      CuteDeclarativeLineSeriesCall2 call = reinterpret_cast<CuteDeclarativeLineSeriesCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    DeclarativeLineSeries::componentComplete();
  }

#if QT_CONFIG(charts_line_chart)
  //  QAbstractSeries::SeriesType QLineSeries::type() const
  QAbstractSeries::SeriesType type() const override {
    if (taken[3]) {
      int handled = 0;
      CuteDeclarativeLineSeriesCall3 call = reinterpret_cast<CuteDeclarativeLineSeriesCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries::SeriesType>(given);
    }
    return QLineSeries::type();
  }
#endif  // QT_CONFIG(charts_line_chart)

  //  void QXYSeries::setPen(const QPen &pen)
  void setPen(const QPen &pen) override {
    if (taken[4]) {
      int handled = 0;
      CuteDeclarativeLineSeriesCall4 call = reinterpret_cast<CuteDeclarativeLineSeriesCall4>(taken[4]);
      call(this, &pen, &handled);
      if (handled) return;
    }
    QXYSeries::setPen(pen);
  }

  //  void QXYSeries::setBrush(const QBrush &brush)
  void setBrush(const QBrush &brush) override {
    if (taken[5]) {
      int handled = 0;
      CuteDeclarativeLineSeriesCall5 call = reinterpret_cast<CuteDeclarativeLineSeriesCall5>(taken[5]);
      call(this, &brush, &handled);
      if (handled) return;
    }
    QXYSeries::setBrush(brush);
  }

  //  void QXYSeries::setColor(const QColor &color)
  void setColor(const QColor &color) override {
    if (taken[6]) {
      int handled = 0;
      CuteDeclarativeLineSeriesCall6 call = reinterpret_cast<CuteDeclarativeLineSeriesCall6>(taken[6]);
      call(this, &color, &handled);
      if (handled) return;
    }
    QXYSeries::setColor(color);
  }

  //  QColor QXYSeries::color() const
  QColor color() const override {
    if (taken[7]) {
      int handled = 0;
      CuteDeclarativeLineSeriesCall7 call = reinterpret_cast<CuteDeclarativeLineSeriesCall7>(taken[7]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QXYSeries::color();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteDeclarativeLineSeriesCall8 call = reinterpret_cast<CuteDeclarativeLineSeriesCall8>(taken[8]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteDeclarativeLineSeriesCall9 call = reinterpret_cast<CuteDeclarativeLineSeriesCall9>(taken[9]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteDeclarativeLineSeriesCall10 call = reinterpret_cast<CuteDeclarativeLineSeriesCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteDeclarativeLineSeriesCall11 call = reinterpret_cast<CuteDeclarativeLineSeriesCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteDeclarativeLineSeriesCall12 call = reinterpret_cast<CuteDeclarativeLineSeriesCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteDeclarativeLineSeriesCall13 call = reinterpret_cast<CuteDeclarativeLineSeriesCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteDeclarativeLineSeriesCall14 call = reinterpret_cast<CuteDeclarativeLineSeriesCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *DeclarativeLineSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21DeclarativeLineSeries10metaObjectEv(
    const DeclarativeLineSeries *self) {
  return self->metaObject();
}

//  void *DeclarativeLineSeries::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21DeclarativeLineSeries11qt_metacastEPKc(
    DeclarativeLineSeries *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int DeclarativeLineSeries::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21DeclarativeLineSeries11qt_metacallEN11QMetaObject4CallEiPPv(
    DeclarativeLineSeries *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString DeclarativeLineSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21DeclarativeLineSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(DeclarativeLineSeries::tr(s, c, n));
}

//  DeclarativeLineSeries::DeclarativeLineSeries(QObject *parent)
extern "C" Q_DECL_EXPORT
DeclarativeLineSeries *ritual_ZN21DeclarativeLineSeriesC1EP7QObject(
    QObject *parent) {
  return new CuteDeclarativeLineSeries(parent);
}

//  QXYSeries *DeclarativeLineSeries::xySeries()
extern "C" Q_DECL_EXPORT
QXYSeries *ritual_ZN21DeclarativeLineSeries8xySeriesEv(
    DeclarativeLineSeries *self) {
  return self->xySeries();
}

//  QAbstractAxis *DeclarativeLineSeries::axisX()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN21DeclarativeLineSeries5axisXEv(
    DeclarativeLineSeries *self) {
  return self->axisX();
}

//  void DeclarativeLineSeries::setAxisX(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries8setAxisXEP13QAbstractAxis(
    DeclarativeLineSeries *self,
    QAbstractAxis *axis) {
  self->setAxisX(axis);
}

//  QAbstractAxis *DeclarativeLineSeries::axisY()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN21DeclarativeLineSeries5axisYEv(
    DeclarativeLineSeries *self) {
  return self->axisY();
}

//  void DeclarativeLineSeries::setAxisY(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries8setAxisYEP13QAbstractAxis(
    DeclarativeLineSeries *self,
    QAbstractAxis *axis) {
  self->setAxisY(axis);
}

//  QAbstractAxis *DeclarativeLineSeries::axisXTop()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN21DeclarativeLineSeries8axisXTopEv(
    DeclarativeLineSeries *self) {
  return self->axisXTop();
}

//  void DeclarativeLineSeries::setAxisXTop(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries11setAxisXTopEP13QAbstractAxis(
    DeclarativeLineSeries *self,
    QAbstractAxis *axis) {
  self->setAxisXTop(axis);
}

//  QAbstractAxis *DeclarativeLineSeries::axisYRight()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN21DeclarativeLineSeries10axisYRightEv(
    DeclarativeLineSeries *self) {
  return self->axisYRight();
}

//  void DeclarativeLineSeries::setAxisYRight(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries13setAxisYRightEP13QAbstractAxis(
    DeclarativeLineSeries *self,
    QAbstractAxis *axis) {
  self->setAxisYRight(axis);
}

//  QAbstractAxis *DeclarativeLineSeries::axisAngular()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN21DeclarativeLineSeries11axisAngularEv(
    DeclarativeLineSeries *self) {
  return self->axisAngular();
}

//  void DeclarativeLineSeries::setAxisAngular(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries14setAxisAngularEP13QAbstractAxis(
    DeclarativeLineSeries *self,
    QAbstractAxis *axis) {
  self->setAxisAngular(axis);
}

//  QAbstractAxis *DeclarativeLineSeries::axisRadial()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN21DeclarativeLineSeries10axisRadialEv(
    DeclarativeLineSeries *self) {
  return self->axisRadial();
}

//  void DeclarativeLineSeries::setAxisRadial(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries13setAxisRadialEP13QAbstractAxis(
    DeclarativeLineSeries *self,
    QAbstractAxis *axis) {
  self->setAxisRadial(axis);
}

//  qreal DeclarativeLineSeries::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21DeclarativeLineSeries5widthEv(
    const DeclarativeLineSeries *self) {
  return self->width();
}

//  void DeclarativeLineSeries::setWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries8setWidthEd(
    DeclarativeLineSeries *self,
    qreal width) {
  self->setWidth(width);
}

//  Qt::PenStyle DeclarativeLineSeries::style() const
extern "C" Q_DECL_EXPORT
Qt::PenStyle ritual_ZNK21DeclarativeLineSeries5styleEv(
    const DeclarativeLineSeries *self) {
  return self->style();
}

//  void DeclarativeLineSeries::setStyle(Qt::PenStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries8setStyleEN2Qt8PenStyleE(
    DeclarativeLineSeries *self,
    Qt::PenStyle style) {
  self->setStyle(style);
}

//  Qt::PenCapStyle DeclarativeLineSeries::capStyle() const
extern "C" Q_DECL_EXPORT
Qt::PenCapStyle ritual_ZNK21DeclarativeLineSeries8capStyleEv(
    const DeclarativeLineSeries *self) {
  return self->capStyle();
}

//  void DeclarativeLineSeries::setCapStyle(Qt::PenCapStyle capStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries11setCapStyleEN2Qt11PenCapStyleE(
    DeclarativeLineSeries *self,
    Qt::PenCapStyle capStyle) {
  self->setCapStyle(capStyle);
}

//  QQmlListProperty<QObject> DeclarativeLineSeries::declarativeChildren()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN21DeclarativeLineSeries19declarativeChildrenEv(
    DeclarativeLineSeries *self) {
  return new QQmlListProperty<QObject>(self->declarativeChildren());
}

//  void DeclarativeLineSeries::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries10classBeginEv(
    DeclarativeLineSeries *self) {
  self->classBegin();
}

//  void DeclarativeLineSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries17componentCompleteEv(
    DeclarativeLineSeries *self) {
  self->componentComplete();
}

//  void DeclarativeLineSeries::append(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries6appendEdd(
    DeclarativeLineSeries *self,
    qreal x,
    qreal y) {
  self->append(x, y);
}

//  void DeclarativeLineSeries::replace(qreal oldX, qreal oldY, qreal newX,
//      qreal newY)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries7replaceEdddd(
    DeclarativeLineSeries *self,
    qreal oldX,
    qreal oldY,
    qreal newX,
    qreal newY) {
  self->replace(oldX, oldY, newX, newY);
}

//  void DeclarativeLineSeries::replace(int index, qreal newX, qreal newY)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries7replaceEidd(
    DeclarativeLineSeries *self,
    int index,
    qreal newX,
    qreal newY) {
  self->replace(index, newX, newY);
}

//  void DeclarativeLineSeries::remove(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries6removeEdd(
    DeclarativeLineSeries *self,
    qreal x,
    qreal y) {
  self->remove(x, y);
}

//  void DeclarativeLineSeries::remove(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries6removeEi(
    DeclarativeLineSeries *self,
    int index) {
  self->remove(index);
}

//  void DeclarativeLineSeries::removePoints(int index, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries12removePointsEii(
    DeclarativeLineSeries *self,
    int index,
    int count) {
  self->removePoints(index, count);
}

//  void DeclarativeLineSeries::insert(int index, qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries6insertEidd(
    DeclarativeLineSeries *self,
    int index,
    qreal x,
    qreal y) {
  self->insert(index, x, y);
}

//  void DeclarativeLineSeries::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries5clearEv(DeclarativeLineSeries *self) {
  self->clear();
}

//  QPointF DeclarativeLineSeries::at(int index)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN21DeclarativeLineSeries2atEi(
    DeclarativeLineSeries *self,
    int index) {
  return new QPointF(self->at(index));
}

//  void DeclarativeLineSeries::countChanged(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries12countChangedEi(
    DeclarativeLineSeries *self,
    int count) {
  self->countChanged(count);
}

//  void DeclarativeLineSeries::axisXChanged(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries12axisXChangedEP13QAbstractAxis(
    DeclarativeLineSeries *self,
    QAbstractAxis *axis) {
  self->axisXChanged(axis);
}

//  void DeclarativeLineSeries::axisYChanged(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries12axisYChangedEP13QAbstractAxis(
    DeclarativeLineSeries *self,
    QAbstractAxis *axis) {
  self->axisYChanged(axis);
}

//  void DeclarativeLineSeries::axisXTopChanged(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries15axisXTopChangedEP13QAbstractAxis(
    DeclarativeLineSeries *self,
    QAbstractAxis *axis) {
  self->axisXTopChanged(axis);
}

//  void DeclarativeLineSeries::axisYRightChanged(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries17axisYRightChangedEP13QAbstractAxis(
    DeclarativeLineSeries *self,
    QAbstractAxis *axis) {
  self->axisYRightChanged(axis);
}

//  void DeclarativeLineSeries::axisAngularChanged(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries18axisAngularChangedEP13QAbstractAxis(
    DeclarativeLineSeries *self,
    QAbstractAxis *axis) {
  self->axisAngularChanged(axis);
}

//  void DeclarativeLineSeries::axisRadialChanged(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries17axisRadialChangedEP13QAbstractAxis(
    DeclarativeLineSeries *self,
    QAbstractAxis *axis) {
  self->axisRadialChanged(axis);
}

//  void DeclarativeLineSeries::widthChanged(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries12widthChangedEd(
    DeclarativeLineSeries *self,
    qreal width) {
  self->widthChanged(width);
}

//  void DeclarativeLineSeries::styleChanged(Qt::PenStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries12styleChangedEN2Qt8PenStyleE(
    DeclarativeLineSeries *self,
    Qt::PenStyle style) {
  self->styleChanged(style);
}

//  void DeclarativeLineSeries::capStyleChanged(Qt::PenCapStyle capStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries15capStyleChangedEN2Qt11PenCapStyleE(
    DeclarativeLineSeries *self,
    Qt::PenCapStyle capStyle) {
  self->capStyleChanged(capStyle);
}

//  void DeclarativeLineSeries::handleCountChanged(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries18handleCountChangedEi(
    DeclarativeLineSeries *self,
    int index) {
  self->handleCountChanged(index);
}

//  void DeclarativeLineSeries::appendDeclarativeChildren(QQmlListProperty<QO
//      bject> *list, QObject *element)
extern "C" Q_DECL_EXPORT
void ritual_ZN21DeclarativeLineSeries25appendDeclarativeChildrenEP16QQmlListPropertyI7QObjectEPS1_(
    QQmlListProperty<QObject> *list,
    QObject *element) {
  DeclarativeLineSeries::appendDeclarativeChildren(list, element);
}

//  DeclarativeLineSeries as the DeclarativeXySeries it is built on
extern "C" Q_DECL_EXPORT
DeclarativeXySeries *ritual_cast_DeclarativeLineSeries_DeclarativeXySeries(
    DeclarativeLineSeries *self) {
  return static_cast<DeclarativeXySeries *>(self);
}

//  DeclarativeLineSeries as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_DeclarativeLineSeries_QQmlParserStatus(
    DeclarativeLineSeries *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteDeclarativeLineSeries, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_DeclarativeLineSeries(
    DeclarativeLineSeries *self,
    const char *key,
    void *call) {
  return static_cast<CuteDeclarativeLineSeries *>(self)->take(key, call);
}

//  QXYSeries *DeclarativeLineSeries::xySeries()
extern "C" Q_DECL_EXPORT
QXYSeries *ritual_own_ZN21DeclarativeLineSeries8xySeriesEv(
    DeclarativeLineSeries *self) {
  return self->DeclarativeLineSeries::xySeries();
}

//  void DeclarativeLineSeries::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21DeclarativeLineSeries10classBeginEv(
    DeclarativeLineSeries *self) {
  self->DeclarativeLineSeries::classBegin();
}

//  void DeclarativeLineSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21DeclarativeLineSeries17componentCompleteEv(
    DeclarativeLineSeries *self) {
  self->DeclarativeLineSeries::componentComplete();
}

//  a QQmlListProperty<QObject> a ritual of DeclarativeLineSeries gave
extern "C" Q_DECL_EXPORT
void ritual_drop_DeclarativeLineSeries__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}

#endif  // QT_CONFIG(charts_line_chart)
