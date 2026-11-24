//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qcandlestickset.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qchartglobal.h>
#if QT_CONFIG(charts_candlestick_chart)
#include <QtCharts/qcandlestickset.h>
#include <QtCore/qstring.h>
#include <QtGui/qbrush.h>
#include <QtGui/qpen.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QCandlestickSet that Python can take functions over in. Every QCandlestickSet
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCandlestickSetCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCandlestickSetCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickSetCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickSetCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickSetCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickSetCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCandlestickSetCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCandlestickSet : public QCandlestickSet {
public:
  using QCandlestickSet::QCandlestickSet;
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
      CuteQCandlestickSetCall0 call = reinterpret_cast<CuteQCandlestickSetCall0>(taken[0]);
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
      CuteQCandlestickSetCall1 call = reinterpret_cast<CuteQCandlestickSetCall1>(taken[1]);
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
      CuteQCandlestickSetCall2 call = reinterpret_cast<CuteQCandlestickSetCall2>(taken[2]);
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
      CuteQCandlestickSetCall3 call = reinterpret_cast<CuteQCandlestickSetCall3>(taken[3]);
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
      CuteQCandlestickSetCall4 call = reinterpret_cast<CuteQCandlestickSetCall4>(taken[4]);
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
      CuteQCandlestickSetCall5 call = reinterpret_cast<CuteQCandlestickSetCall5>(taken[5]);
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
      CuteQCandlestickSetCall6 call = reinterpret_cast<CuteQCandlestickSetCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCandlestickSet::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QCandlestickSet10metaObjectEv(
    const QCandlestickSet *self) {
  return self->metaObject();
}

//  QString QCandlestickSet::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QCandlestickSet2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCandlestickSet::tr(s, c, n));
}

//  QCandlestickSet::QCandlestickSet(qreal timestamp, QObject *parent)
extern "C" Q_DECL_EXPORT
QCandlestickSet *ritual_ZN15QCandlestickSetC1EdP7QObject(
    qreal timestamp,
    QObject *parent) {
  return new CuteQCandlestickSet(timestamp, parent);
}

//  QCandlestickSet::QCandlestickSet(qreal open, qreal high, qreal low, qreal
//      close, qreal timestamp, QObject *parent)
extern "C" Q_DECL_EXPORT
QCandlestickSet *ritual_ZN15QCandlestickSetC1EdddddP7QObject(
    qreal open,
    qreal high,
    qreal low,
    qreal close,
    qreal timestamp,
    QObject *parent) {
  return new CuteQCandlestickSet(open, high, low, close, timestamp, parent);
}

//  QCandlestickSet::~QCandlestickSet()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCandlestickSetD1Ev(QCandlestickSet *self) {
  delete self;
}

//  void QCandlestickSet::setTimestamp(qreal timestamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCandlestickSet12setTimestampEd(
    QCandlestickSet *self,
    qreal timestamp) {
  self->setTimestamp(timestamp);
}

//  qreal QCandlestickSet::timestamp() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QCandlestickSet9timestampEv(const QCandlestickSet *self) {
  return self->timestamp();
}

//  void QCandlestickSet::setOpen(qreal open)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCandlestickSet7setOpenEd(
    QCandlestickSet *self,
    qreal open) {
  self->setOpen(open);
}

//  qreal QCandlestickSet::open() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QCandlestickSet4openEv(const QCandlestickSet *self) {
  return self->open();
}

//  void QCandlestickSet::setHigh(qreal high)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCandlestickSet7setHighEd(
    QCandlestickSet *self,
    qreal high) {
  self->setHigh(high);
}

//  qreal QCandlestickSet::high() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QCandlestickSet4highEv(const QCandlestickSet *self) {
  return self->high();
}

//  void QCandlestickSet::setLow(qreal low)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCandlestickSet6setLowEd(QCandlestickSet *self, qreal low) {
  self->setLow(low);
}

//  qreal QCandlestickSet::low() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QCandlestickSet3lowEv(const QCandlestickSet *self) {
  return self->low();
}

//  void QCandlestickSet::setClose(qreal close)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCandlestickSet8setCloseEd(
    QCandlestickSet *self,
    qreal close) {
  self->setClose(close);
}

//  qreal QCandlestickSet::close() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QCandlestickSet5closeEv(const QCandlestickSet *self) {
  return self->close();
}

//  void QCandlestickSet::setBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCandlestickSet8setBrushERK6QBrush(
    QCandlestickSet *self,
    const QBrush *brush) {
  self->setBrush(*brush);
}

//  QBrush QCandlestickSet::brush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK15QCandlestickSet5brushEv(const QCandlestickSet *self) {
  return new QBrush(self->brush());
}

//  void QCandlestickSet::setPen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCandlestickSet6setPenERK4QPen(
    QCandlestickSet *self,
    const QPen *pen) {
  self->setPen(*pen);
}

//  QPen QCandlestickSet::pen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK15QCandlestickSet3penEv(const QCandlestickSet *self) {
  return new QPen(self->pen());
}

//  QCandlestickSetPrivate *QCandlestickSet::d_func()
extern "C" Q_DECL_EXPORT
QCandlestickSetPrivate *ritual_ZN15QCandlestickSet6d_funcEv(
    QCandlestickSet *self) {
  return self->d_func();
}

//  const QCandlestickSetPrivate *QCandlestickSet::d_func() const
extern "C" Q_DECL_EXPORT
const QCandlestickSetPrivate *ritual_ZNK15QCandlestickSet6d_funcEv(
    const QCandlestickSet *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQCandlestickSet, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCandlestickSet(
    QCandlestickSet *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCandlestickSet *>(self)->take(key, call);
}

//  QList<QCandlestickSet *>::QList()
extern "C" Q_DECL_EXPORT
QList<QCandlestickSet *> *ritual_list_make_QCandlestickSet_ptr() {
  return new QList<QCandlestickSet *>();
}

//  void QList<QCandlestickSet *>::append(const QCandlestickSet * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QCandlestickSet_ptr(
    QList<QCandlestickSet *> *self,
    QCandlestickSet *element) {
  self->append(element);
}

//  qsizetype QList<QCandlestickSet *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QCandlestickSet_ptr(
    const QList<QCandlestickSet *> *self) {
  return self->size();
}

//  const QCandlestickSet * &QList<QCandlestickSet *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QCandlestickSet *ritual_list_at_QCandlestickSet_ptr(
    const QList<QCandlestickSet *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QCandlestickSet *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QCandlestickSet_ptr(QList<QCandlestickSet *> *self) {
  delete self;
}

#endif  // QT_CONFIG(charts_candlestick_chart)
