//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qcandlestickseries.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qcandlestickseries.h>
#include <QtCore/qstring.h>
#include <QtCharts/qcandlestickset.h>
#include <QtGui/qcolor.h>
#include <QtGui/qbrush.h>
#include <QtGui/qpen.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QCandlestickSeries that Python can take functions over in. Every QCandlestickSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQCandlestickSeriesCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCandlestickSeriesCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCandlestickSeriesCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickSeriesCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickSeriesCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickSeriesCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickSeriesCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickSeriesCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCandlestickSeries : public QCandlestickSeries {
public:
  using QCandlestickSeries::QCandlestickSeries;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK15QAbstractSeries4typeEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QAbstractSeries::SeriesType QCandlestickSeries::type() const
  QAbstractSeries::SeriesType type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQCandlestickSeriesCall0 call = reinterpret_cast<CuteQCandlestickSeriesCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries::SeriesType>(given);
    }
    return QCandlestickSeries::type();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQCandlestickSeriesCall1 call = reinterpret_cast<CuteQCandlestickSeriesCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQCandlestickSeriesCall2 call = reinterpret_cast<CuteQCandlestickSeriesCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQCandlestickSeriesCall3 call = reinterpret_cast<CuteQCandlestickSeriesCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQCandlestickSeriesCall4 call = reinterpret_cast<CuteQCandlestickSeriesCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQCandlestickSeriesCall5 call = reinterpret_cast<CuteQCandlestickSeriesCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQCandlestickSeriesCall6 call = reinterpret_cast<CuteQCandlestickSeriesCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQCandlestickSeriesCall7 call = reinterpret_cast<CuteQCandlestickSeriesCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCandlestickSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QCandlestickSeries10metaObjectEv(
    const QCandlestickSeries *self) {
  return self->metaObject();
}

//  QString QCandlestickSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QCandlestickSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCandlestickSeries::tr(s, c, n));
}

//  QCandlestickSeries::QCandlestickSeries(QObject *parent)
extern "C" Q_DECL_EXPORT
QCandlestickSeries *ritual_ZN18QCandlestickSeriesC1EP7QObject(
    QObject *parent) {
  return new CuteQCandlestickSeries(parent);
}

//  QCandlestickSeries::~QCandlestickSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCandlestickSeriesD1Ev(QCandlestickSeries *self) {
  delete self;
}

//  bool QCandlestickSeries::append(QCandlestickSet *set)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QCandlestickSeries6appendEP15QCandlestickSet(
    QCandlestickSeries *self,
    QCandlestickSet *set) {
  return self->append(set);
}

//  bool QCandlestickSeries::remove(QCandlestickSet *set)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QCandlestickSeries6removeEP15QCandlestickSet(
    QCandlestickSeries *self,
    QCandlestickSet *set) {
  return self->remove(set);
}

//  bool QCandlestickSeries::append(const QList<QCandlestickSet *> &sets)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QCandlestickSeries6appendERK5QListIP15QCandlestickSetE(
    QCandlestickSeries *self,
    const QList<QCandlestickSet *> *sets) {
  return self->append(*sets);
}

//  bool QCandlestickSeries::remove(const QList<QCandlestickSet *> &sets)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QCandlestickSeries6removeERK5QListIP15QCandlestickSetE(
    QCandlestickSeries *self,
    const QList<QCandlestickSet *> *sets) {
  return self->remove(*sets);
}

//  bool QCandlestickSeries::insert(int index, QCandlestickSet *set)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QCandlestickSeries6insertEiP15QCandlestickSet(
    QCandlestickSeries *self,
    int index,
    QCandlestickSet *set) {
  return self->insert(index, set);
}

//  bool QCandlestickSeries::take(QCandlestickSet *set)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QCandlestickSeries4takeEP15QCandlestickSet(
    QCandlestickSeries *self,
    QCandlestickSet *set) {
  return self->take(set);
}

//  void QCandlestickSeries::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCandlestickSeries5clearEv(QCandlestickSeries *self) {
  self->clear();
}

//  QList<QCandlestickSet *> QCandlestickSeries::sets() const
extern "C" Q_DECL_EXPORT
QList<QCandlestickSet *> *ritual_ZNK18QCandlestickSeries4setsEv(
    const QCandlestickSeries *self) {
  return new QList<QCandlestickSet *>(self->sets());
}

//  int QCandlestickSeries::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QCandlestickSeries5countEv(const QCandlestickSeries *self) {
  return self->count();
}

//  QAbstractSeries::SeriesType QCandlestickSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_ZNK18QCandlestickSeries4typeEv(
    const QCandlestickSeries *self) {
  return self->type();
}

//  void QCandlestickSeries::setMaximumColumnWidth(qreal maximumColumnWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCandlestickSeries21setMaximumColumnWidthEd(
    QCandlestickSeries *self,
    qreal maximumColumnWidth) {
  self->setMaximumColumnWidth(maximumColumnWidth);
}

//  qreal QCandlestickSeries::maximumColumnWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QCandlestickSeries18maximumColumnWidthEv(
    const QCandlestickSeries *self) {
  return self->maximumColumnWidth();
}

//  void QCandlestickSeries::setMinimumColumnWidth(qreal minimumColumnWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCandlestickSeries21setMinimumColumnWidthEd(
    QCandlestickSeries *self,
    qreal minimumColumnWidth) {
  self->setMinimumColumnWidth(minimumColumnWidth);
}

//  qreal QCandlestickSeries::minimumColumnWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QCandlestickSeries18minimumColumnWidthEv(
    const QCandlestickSeries *self) {
  return self->minimumColumnWidth();
}

//  void QCandlestickSeries::setBodyWidth(qreal bodyWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCandlestickSeries12setBodyWidthEd(
    QCandlestickSeries *self,
    qreal bodyWidth) {
  self->setBodyWidth(bodyWidth);
}

//  qreal QCandlestickSeries::bodyWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QCandlestickSeries9bodyWidthEv(
    const QCandlestickSeries *self) {
  return self->bodyWidth();
}

//  void QCandlestickSeries::setBodyOutlineVisible(bool bodyOutlineVisible)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCandlestickSeries21setBodyOutlineVisibleEb(
    QCandlestickSeries *self,
    bool bodyOutlineVisible) {
  self->setBodyOutlineVisible(bodyOutlineVisible);
}

//  bool QCandlestickSeries::bodyOutlineVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QCandlestickSeries18bodyOutlineVisibleEv(
    const QCandlestickSeries *self) {
  return self->bodyOutlineVisible();
}

//  void QCandlestickSeries::setCapsWidth(qreal capsWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCandlestickSeries12setCapsWidthEd(
    QCandlestickSeries *self,
    qreal capsWidth) {
  self->setCapsWidth(capsWidth);
}

//  qreal QCandlestickSeries::capsWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QCandlestickSeries9capsWidthEv(
    const QCandlestickSeries *self) {
  return self->capsWidth();
}

//  void QCandlestickSeries::setCapsVisible(bool capsVisible)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCandlestickSeries14setCapsVisibleEb(
    QCandlestickSeries *self,
    bool capsVisible) {
  self->setCapsVisible(capsVisible);
}

//  bool QCandlestickSeries::capsVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QCandlestickSeries11capsVisibleEv(
    const QCandlestickSeries *self) {
  return self->capsVisible();
}

//  void QCandlestickSeries::setIncreasingColor(const QColor
//      &increasingColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCandlestickSeries18setIncreasingColorERK6QColor(
    QCandlestickSeries *self,
    const QColor *increasingColor) {
  self->setIncreasingColor(*increasingColor);
}

//  QColor QCandlestickSeries::increasingColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK18QCandlestickSeries15increasingColorEv(
    const QCandlestickSeries *self) {
  return new QColor(self->increasingColor());
}

//  void QCandlestickSeries::setDecreasingColor(const QColor
//      &decreasingColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCandlestickSeries18setDecreasingColorERK6QColor(
    QCandlestickSeries *self,
    const QColor *decreasingColor) {
  self->setDecreasingColor(*decreasingColor);
}

//  QColor QCandlestickSeries::decreasingColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK18QCandlestickSeries15decreasingColorEv(
    const QCandlestickSeries *self) {
  return new QColor(self->decreasingColor());
}

//  void QCandlestickSeries::setBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCandlestickSeries8setBrushERK6QBrush(
    QCandlestickSeries *self,
    const QBrush *brush) {
  self->setBrush(*brush);
}

//  QBrush QCandlestickSeries::brush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK18QCandlestickSeries5brushEv(
    const QCandlestickSeries *self) {
  return new QBrush(self->brush());
}

//  void QCandlestickSeries::setPen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCandlestickSeries6setPenERK4QPen(
    QCandlestickSeries *self,
    const QPen *pen) {
  self->setPen(*pen);
}

//  QPen QCandlestickSeries::pen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK18QCandlestickSeries3penEv(const QCandlestickSeries *self) {
  return new QPen(self->pen());
}

//  QCandlestickSeriesPrivate *QCandlestickSeries::d_func()
extern "C" Q_DECL_EXPORT
QCandlestickSeriesPrivate *ritual_ZN18QCandlestickSeries6d_funcEv(
    QCandlestickSeries *self) {
  return self->d_func();
}

//  const QCandlestickSeriesPrivate *QCandlestickSeries::d_func() const
extern "C" Q_DECL_EXPORT
const QCandlestickSeriesPrivate *ritual_ZNK18QCandlestickSeries6d_funcEv(
    const QCandlestickSeries *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQCandlestickSeries, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCandlestickSeries(
    QCandlestickSeries *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCandlestickSeries *>(self)->take(key, call);
}

//  QAbstractSeries::SeriesType QCandlestickSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_own_ZNK18QCandlestickSeries4typeEv(
    const QCandlestickSeries *self) {
  return self->QCandlestickSeries::type();
}
