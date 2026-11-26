//  Written by dev_tooling.RitualGenerator from the records of
//  QtChartsQml/6.12.0/QtChartsQml/private/declarativebarseries_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtChartsQml/qtchartsqmlexports.h>
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#if QT_CONFIG(charts_bar_chart)
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#include <QtChartsQml/QtChartsQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativebarseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>

//  A DeclarativeHorizontalBarSeries that Python can take functions over in. Every DeclarativeHorizontalBarSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteDeclarativeHorizontalBarSeriesCall0)(const void *, int *);
typedef void (*CuteDeclarativeHorizontalBarSeriesCall1)(const void *, int *);
typedef int (*CuteDeclarativeHorizontalBarSeriesCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteDeclarativeHorizontalBarSeriesCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteDeclarativeHorizontalBarSeriesCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeHorizontalBarSeriesCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeHorizontalBarSeriesCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeHorizontalBarSeriesCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeHorizontalBarSeriesCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeHorizontalBarSeriesCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteDeclarativeHorizontalBarSeries : public DeclarativeHorizontalBarSeries {
public:
  using DeclarativeHorizontalBarSeries::DeclarativeHorizontalBarSeries;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QAbstractSeries4typeEv")) {
      taken[2] = call;
      return true;
    }
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

  //  void DeclarativeHorizontalBarSeries::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteDeclarativeHorizontalBarSeriesCall0 call = reinterpret_cast<CuteDeclarativeHorizontalBarSeriesCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    DeclarativeHorizontalBarSeries::classBegin();
  }

  //  void DeclarativeHorizontalBarSeries::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteDeclarativeHorizontalBarSeriesCall1 call = reinterpret_cast<CuteDeclarativeHorizontalBarSeriesCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    DeclarativeHorizontalBarSeries::componentComplete();
  }

  //  QAbstractSeries::SeriesType QHorizontalBarSeries::type() const
  QAbstractSeries::SeriesType type() const override {
    if (taken[2]) {
      int handled = 0;
      CuteDeclarativeHorizontalBarSeriesCall2 call = reinterpret_cast<CuteDeclarativeHorizontalBarSeriesCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries::SeriesType>(given);
    }
    return QHorizontalBarSeries::type();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteDeclarativeHorizontalBarSeriesCall3 call = reinterpret_cast<CuteDeclarativeHorizontalBarSeriesCall3>(taken[3]);
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
      CuteDeclarativeHorizontalBarSeriesCall4 call = reinterpret_cast<CuteDeclarativeHorizontalBarSeriesCall4>(taken[4]);
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
      CuteDeclarativeHorizontalBarSeriesCall5 call = reinterpret_cast<CuteDeclarativeHorizontalBarSeriesCall5>(taken[5]);
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
      CuteDeclarativeHorizontalBarSeriesCall6 call = reinterpret_cast<CuteDeclarativeHorizontalBarSeriesCall6>(taken[6]);
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
      CuteDeclarativeHorizontalBarSeriesCall7 call = reinterpret_cast<CuteDeclarativeHorizontalBarSeriesCall7>(taken[7]);
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
      CuteDeclarativeHorizontalBarSeriesCall8 call = reinterpret_cast<CuteDeclarativeHorizontalBarSeriesCall8>(taken[8]);
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
      CuteDeclarativeHorizontalBarSeriesCall9 call = reinterpret_cast<CuteDeclarativeHorizontalBarSeriesCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *DeclarativeHorizontalBarSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK30DeclarativeHorizontalBarSeries10metaObjectEv(
    const DeclarativeHorizontalBarSeries *self) {
  return self->metaObject();
}

//  void *DeclarativeHorizontalBarSeries::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN30DeclarativeHorizontalBarSeries11qt_metacastEPKc(
    DeclarativeHorizontalBarSeries *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int DeclarativeHorizontalBarSeries::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN30DeclarativeHorizontalBarSeries11qt_metacallEN11QMetaObject4CallEiPPv(
    DeclarativeHorizontalBarSeries *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString DeclarativeHorizontalBarSeries::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN30DeclarativeHorizontalBarSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(DeclarativeHorizontalBarSeries::tr(s, c, n));
}

//  DeclarativeHorizontalBarSeries::DeclarativeHorizontalBarSeries(QQuickItem
//      *parent)
extern "C" Q_DECL_EXPORT
DeclarativeHorizontalBarSeries *ritual_ZN30DeclarativeHorizontalBarSeriesC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteDeclarativeHorizontalBarSeries(parent);
}

//  QAbstractAxis *DeclarativeHorizontalBarSeries::axisX()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN30DeclarativeHorizontalBarSeries5axisXEv(
    DeclarativeHorizontalBarSeries *self) {
  return self->axisX();
}

//  void DeclarativeHorizontalBarSeries::setAxisX(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN30DeclarativeHorizontalBarSeries8setAxisXEP13QAbstractAxis(
    DeclarativeHorizontalBarSeries *self,
    QAbstractAxis *axis) {
  self->setAxisX(axis);
}

//  QAbstractAxis *DeclarativeHorizontalBarSeries::axisY()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN30DeclarativeHorizontalBarSeries5axisYEv(
    DeclarativeHorizontalBarSeries *self) {
  return self->axisY();
}

//  void DeclarativeHorizontalBarSeries::setAxisY(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN30DeclarativeHorizontalBarSeries8setAxisYEP13QAbstractAxis(
    DeclarativeHorizontalBarSeries *self,
    QAbstractAxis *axis) {
  self->setAxisY(axis);
}

//  QAbstractAxis *DeclarativeHorizontalBarSeries::axisXTop()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN30DeclarativeHorizontalBarSeries8axisXTopEv(
    DeclarativeHorizontalBarSeries *self) {
  return self->axisXTop();
}

//  void DeclarativeHorizontalBarSeries::setAxisXTop(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN30DeclarativeHorizontalBarSeries11setAxisXTopEP13QAbstractAxis(
    DeclarativeHorizontalBarSeries *self,
    QAbstractAxis *axis) {
  self->setAxisXTop(axis);
}

//  QAbstractAxis *DeclarativeHorizontalBarSeries::axisYRight()
extern "C" Q_DECL_EXPORT
QAbstractAxis *ritual_ZN30DeclarativeHorizontalBarSeries10axisYRightEv(
    DeclarativeHorizontalBarSeries *self) {
  return self->axisYRight();
}

//  void DeclarativeHorizontalBarSeries::setAxisYRight(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN30DeclarativeHorizontalBarSeries13setAxisYRightEP13QAbstractAxis(
    DeclarativeHorizontalBarSeries *self,
    QAbstractAxis *axis) {
  self->setAxisYRight(axis);
}

//  QQmlListProperty<QObject>
//      DeclarativeHorizontalBarSeries::seriesChildren()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN30DeclarativeHorizontalBarSeries14seriesChildrenEv(
    DeclarativeHorizontalBarSeries *self) {
  return new QQmlListProperty<QObject>(self->seriesChildren());
}

//  DeclarativeBarSet *DeclarativeHorizontalBarSeries::at(int index)
extern "C" Q_DECL_EXPORT
DeclarativeBarSet *ritual_ZN30DeclarativeHorizontalBarSeries2atEi(
    DeclarativeHorizontalBarSeries *self,
    int index) {
  return self->at(index);
}

//  DeclarativeBarSet *DeclarativeHorizontalBarSeries::append(QString label,
//      QVariantList values)
extern "C" Q_DECL_EXPORT
DeclarativeBarSet *ritual_ZN30DeclarativeHorizontalBarSeries6appendE7QString5QListI8QVariantE(
    DeclarativeHorizontalBarSeries *self,
    const QString *label,
    const QList<QVariant> *values) {
  return self->append(*label, *values);
}

//  DeclarativeBarSet *DeclarativeHorizontalBarSeries::insert(int index,
//      QString label, QVariantList values)
extern "C" Q_DECL_EXPORT
DeclarativeBarSet *ritual_ZN30DeclarativeHorizontalBarSeries6insertEi7QString5QListI8QVariantE(
    DeclarativeHorizontalBarSeries *self,
    int index,
    const QString *label,
    const QList<QVariant> *values) {
  return self->insert(index, *label, *values);
}

//  bool DeclarativeHorizontalBarSeries::remove(QBarSet *barset)
extern "C" Q_DECL_EXPORT
bool ritual_ZN30DeclarativeHorizontalBarSeries6removeEP7QBarSet(
    DeclarativeHorizontalBarSeries *self,
    QBarSet *barset) {
  return self->remove(barset);
}

//  void DeclarativeHorizontalBarSeries::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN30DeclarativeHorizontalBarSeries5clearEv(
    DeclarativeHorizontalBarSeries *self) {
  self->clear();
}

//  void DeclarativeHorizontalBarSeries::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN30DeclarativeHorizontalBarSeries10classBeginEv(
    DeclarativeHorizontalBarSeries *self) {
  self->classBegin();
}

//  void DeclarativeHorizontalBarSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN30DeclarativeHorizontalBarSeries17componentCompleteEv(
    DeclarativeHorizontalBarSeries *self) {
  self->componentComplete();
}

//  void DeclarativeHorizontalBarSeries::axisXChanged(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN30DeclarativeHorizontalBarSeries12axisXChangedEP13QAbstractAxis(
    DeclarativeHorizontalBarSeries *self,
    QAbstractAxis *axis) {
  self->axisXChanged(axis);
}

//  void DeclarativeHorizontalBarSeries::axisYChanged(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN30DeclarativeHorizontalBarSeries12axisYChangedEP13QAbstractAxis(
    DeclarativeHorizontalBarSeries *self,
    QAbstractAxis *axis) {
  self->axisYChanged(axis);
}

//  void DeclarativeHorizontalBarSeries::axisXTopChanged(QAbstractAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN30DeclarativeHorizontalBarSeries15axisXTopChangedEP13QAbstractAxis(
    DeclarativeHorizontalBarSeries *self,
    QAbstractAxis *axis) {
  self->axisXTopChanged(axis);
}

//  void DeclarativeHorizontalBarSeries::axisYRightChanged(QAbstractAxis
//      *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN30DeclarativeHorizontalBarSeries17axisYRightChangedEP13QAbstractAxis(
    DeclarativeHorizontalBarSeries *self,
    QAbstractAxis *axis) {
  self->axisYRightChanged(axis);
}

//  void DeclarativeHorizontalBarSeries::appendSeriesChildren(QQmlListPropert
//      y<QObject> *list, QObject *element)
extern "C" Q_DECL_EXPORT
void ritual_ZN30DeclarativeHorizontalBarSeries20appendSeriesChildrenEP16QQmlListPropertyI7QObjectEPS1_(
    QQmlListProperty<QObject> *list,
    QObject *element) {
  DeclarativeHorizontalBarSeries::appendSeriesChildren(list, element);
}

//  DeclarativeHorizontalBarSeries as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_DeclarativeHorizontalBarSeries_QQmlParserStatus(
    DeclarativeHorizontalBarSeries *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteDeclarativeHorizontalBarSeries, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_DeclarativeHorizontalBarSeries(
    DeclarativeHorizontalBarSeries *self,
    const char *key,
    void *call) {
  return static_cast<CuteDeclarativeHorizontalBarSeries *>(self)->take(key, call);
}

//  void DeclarativeHorizontalBarSeries::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30DeclarativeHorizontalBarSeries10classBeginEv(
    DeclarativeHorizontalBarSeries *self) {
  self->DeclarativeHorizontalBarSeries::classBegin();
}

//  void DeclarativeHorizontalBarSeries::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30DeclarativeHorizontalBarSeries17componentCompleteEv(
    DeclarativeHorizontalBarSeries *self) {
  self->DeclarativeHorizontalBarSeries::componentComplete();
}

//  a QQmlListProperty<QObject> a ritual of DeclarativeHorizontalBarSeries
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_DeclarativeHorizontalBarSeries__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}

#endif  // QT_CONFIG(charts_bar_chart)
