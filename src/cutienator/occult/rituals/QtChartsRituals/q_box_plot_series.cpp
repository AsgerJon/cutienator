//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qboxplotseries.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qboxplotseries.h>
#include <QtCore/qstring.h>
#include <QtCharts/qboxset.h>
#include <QtGui/qbrush.h>
#include <QtGui/qpen.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QBoxPlotSeries that Python can take functions over in. Every QBoxPlotSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQBoxPlotSeriesCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBoxPlotSeriesCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBoxPlotSeriesCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxPlotSeriesCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxPlotSeriesCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxPlotSeriesCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxPlotSeriesCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBoxPlotSeriesCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQBoxPlotSeries : public QBoxPlotSeries {
public:
  using QBoxPlotSeries::QBoxPlotSeries;
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

  //  QAbstractSeries::SeriesType QBoxPlotSeries::type() const
  QAbstractSeries::SeriesType type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQBoxPlotSeriesCall0 call = reinterpret_cast<CuteQBoxPlotSeriesCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractSeries::SeriesType>(given);
    }
    return QBoxPlotSeries::type();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQBoxPlotSeriesCall1 call = reinterpret_cast<CuteQBoxPlotSeriesCall1>(taken[1]);
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
      CuteQBoxPlotSeriesCall2 call = reinterpret_cast<CuteQBoxPlotSeriesCall2>(taken[2]);
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
      CuteQBoxPlotSeriesCall3 call = reinterpret_cast<CuteQBoxPlotSeriesCall3>(taken[3]);
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
      CuteQBoxPlotSeriesCall4 call = reinterpret_cast<CuteQBoxPlotSeriesCall4>(taken[4]);
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
      CuteQBoxPlotSeriesCall5 call = reinterpret_cast<CuteQBoxPlotSeriesCall5>(taken[5]);
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
      CuteQBoxPlotSeriesCall6 call = reinterpret_cast<CuteQBoxPlotSeriesCall6>(taken[6]);
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
      CuteQBoxPlotSeriesCall7 call = reinterpret_cast<CuteQBoxPlotSeriesCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QBoxPlotSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QBoxPlotSeries10metaObjectEv(
    const QBoxPlotSeries *self) {
  return self->metaObject();
}

//  QString QBoxPlotSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QBoxPlotSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBoxPlotSeries::tr(s, c, n));
}

//  QBoxPlotSeries::QBoxPlotSeries(QObject *parent)
extern "C" Q_DECL_EXPORT
QBoxPlotSeries *ritual_ZN14QBoxPlotSeriesC1EP7QObject(QObject *parent) {
  return new CuteQBoxPlotSeries(parent);
}

//  QBoxPlotSeries::~QBoxPlotSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBoxPlotSeriesD1Ev(QBoxPlotSeries *self) {
  delete self;
}

//  bool QBoxPlotSeries::append(QBoxSet *box)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QBoxPlotSeries6appendEP7QBoxSet(
    QBoxPlotSeries *self,
    QBoxSet *box) {
  return self->append(box);
}

//  bool QBoxPlotSeries::remove(QBoxSet *box)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QBoxPlotSeries6removeEP7QBoxSet(
    QBoxPlotSeries *self,
    QBoxSet *box) {
  return self->remove(box);
}

//  bool QBoxPlotSeries::take(QBoxSet *box)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QBoxPlotSeries4takeEP7QBoxSet(
    QBoxPlotSeries *self,
    QBoxSet *box) {
  return self->take(box);
}

//  bool QBoxPlotSeries::append(const QList<QBoxSet *> &boxes)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QBoxPlotSeries6appendERK5QListIP7QBoxSetE(
    QBoxPlotSeries *self,
    const QList<QBoxSet *> *boxes) {
  return self->append(*boxes);
}

//  bool QBoxPlotSeries::insert(int index, QBoxSet *box)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QBoxPlotSeries6insertEiP7QBoxSet(
    QBoxPlotSeries *self,
    int index,
    QBoxSet *box) {
  return self->insert(index, box);
}

//  int QBoxPlotSeries::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QBoxPlotSeries5countEv(const QBoxPlotSeries *self) {
  return self->count();
}

//  QList<QBoxSet *> QBoxPlotSeries::boxSets() const
extern "C" Q_DECL_EXPORT
QList<QBoxSet *> *ritual_ZNK14QBoxPlotSeries7boxSetsEv(
    const QBoxPlotSeries *self) {
  return new QList<QBoxSet *>(self->boxSets());
}

//  void QBoxPlotSeries::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBoxPlotSeries5clearEv(QBoxPlotSeries *self) {
  self->clear();
}

//  QAbstractSeries::SeriesType QBoxPlotSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_ZNK14QBoxPlotSeries4typeEv(
    const QBoxPlotSeries *self) {
  return self->type();
}

//  void QBoxPlotSeries::setBoxOutlineVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBoxPlotSeries20setBoxOutlineVisibleEb(
    QBoxPlotSeries *self,
    bool visible) {
  self->setBoxOutlineVisible(visible);
}

//  bool QBoxPlotSeries::boxOutlineVisible()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QBoxPlotSeries17boxOutlineVisibleEv(QBoxPlotSeries *self) {
  return self->boxOutlineVisible();
}

//  void QBoxPlotSeries::setBoxWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBoxPlotSeries11setBoxWidthEd(
    QBoxPlotSeries *self,
    qreal width) {
  self->setBoxWidth(width);
}

//  qreal QBoxPlotSeries::boxWidth()
extern "C" Q_DECL_EXPORT
qreal ritual_ZN14QBoxPlotSeries8boxWidthEv(QBoxPlotSeries *self) {
  return self->boxWidth();
}

//  void QBoxPlotSeries::setBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBoxPlotSeries8setBrushERK6QBrush(
    QBoxPlotSeries *self,
    const QBrush *brush) {
  self->setBrush(*brush);
}

//  QBrush QBoxPlotSeries::brush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK14QBoxPlotSeries5brushEv(const QBoxPlotSeries *self) {
  return new QBrush(self->brush());
}

//  void QBoxPlotSeries::setPen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QBoxPlotSeries6setPenERK4QPen(
    QBoxPlotSeries *self,
    const QPen *pen) {
  self->setPen(*pen);
}

//  QPen QBoxPlotSeries::pen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK14QBoxPlotSeries3penEv(const QBoxPlotSeries *self) {
  return new QPen(self->pen());
}

//  QBoxPlotSeriesPrivate *QBoxPlotSeries::d_func()
extern "C" Q_DECL_EXPORT
QBoxPlotSeriesPrivate *ritual_ZN14QBoxPlotSeries6d_funcEv(
    QBoxPlotSeries *self) {
  return self->d_func();
}

//  const QBoxPlotSeriesPrivate *QBoxPlotSeries::d_func() const
extern "C" Q_DECL_EXPORT
const QBoxPlotSeriesPrivate *ritual_ZNK14QBoxPlotSeries6d_funcEv(
    const QBoxPlotSeries *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQBoxPlotSeries, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBoxPlotSeries(
    QBoxPlotSeries *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBoxPlotSeries *>(self)->take(key, call);
}

//  QAbstractSeries::SeriesType QBoxPlotSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstractSeries::SeriesType ritual_own_ZNK14QBoxPlotSeries4typeEv(
    const QBoxPlotSeries *self) {
  return self->QBoxPlotSeries::type();
}
