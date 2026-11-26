//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qcategoryaxis.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qcategoryaxis.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QCategoryAxis that Python can take functions over in. Every QCategoryAxis
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQCategoryAxisCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCategoryAxisCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCategoryAxisCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCategoryAxisCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCategoryAxisCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCategoryAxisCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCategoryAxisCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCategoryAxisCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCategoryAxis : public QCategoryAxis {
public:
  using QCategoryAxis::QCategoryAxis;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK13QAbstractAxis4typeEv")) {
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

  //  AxisType QCategoryAxis::type() const
  QAbstractAxis::AxisType type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQCategoryAxisCall0 call = reinterpret_cast<CuteQCategoryAxisCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractAxis::AxisType>(given);
    }
    return QCategoryAxis::type();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQCategoryAxisCall1 call = reinterpret_cast<CuteQCategoryAxisCall1>(taken[1]);
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
      CuteQCategoryAxisCall2 call = reinterpret_cast<CuteQCategoryAxisCall2>(taken[2]);
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
      CuteQCategoryAxisCall3 call = reinterpret_cast<CuteQCategoryAxisCall3>(taken[3]);
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
      CuteQCategoryAxisCall4 call = reinterpret_cast<CuteQCategoryAxisCall4>(taken[4]);
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
      CuteQCategoryAxisCall5 call = reinterpret_cast<CuteQCategoryAxisCall5>(taken[5]);
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
      CuteQCategoryAxisCall6 call = reinterpret_cast<CuteQCategoryAxisCall6>(taken[6]);
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
      CuteQCategoryAxisCall7 call = reinterpret_cast<CuteQCategoryAxisCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCategoryAxis::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QCategoryAxis10metaObjectEv(
    const QCategoryAxis *self) {
  return self->metaObject();
}

//  void *QCategoryAxis::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QCategoryAxis11qt_metacastEPKc(
    QCategoryAxis *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QCategoryAxis::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QCategoryAxis11qt_metacallEN11QMetaObject4CallEiPPv(
    QCategoryAxis *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QCategoryAxis::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QCategoryAxis2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCategoryAxis::tr(s, c, n));
}

//  QCategoryAxis::QCategoryAxis(QObject *parent)
extern "C" Q_DECL_EXPORT
QCategoryAxis *ritual_ZN13QCategoryAxisC1EP7QObject(QObject *parent) {
  return new CuteQCategoryAxis(parent);
}

//  QCategoryAxis::~QCategoryAxis()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCategoryAxisD1Ev(QCategoryAxis *self) {
  delete self;
}

//  QCategoryAxis::QCategoryAxis(QCategoryAxisPrivate &d, QObject *parent)
extern "C" Q_DECL_EXPORT
QCategoryAxis *ritual_ZN13QCategoryAxisC1ER20QCategoryAxisPrivateP7QObject(
    QCategoryAxisPrivate *d,
    QObject *parent) {
  return new CuteQCategoryAxis(*d, parent);
}

//  AxisType QCategoryAxis::type() const
extern "C" Q_DECL_EXPORT
QAbstractAxis::AxisType ritual_ZNK13QCategoryAxis4typeEv(
    const QCategoryAxis *self) {
  return self->type();
}

//  void QCategoryAxis::append(const QString &label, qreal categoryEndValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCategoryAxis6appendERK7QStringd(
    QCategoryAxis *self,
    const QString *label,
    qreal categoryEndValue) {
  self->append(*label, categoryEndValue);
}

//  void QCategoryAxis::remove(const QString &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCategoryAxis6removeERK7QString(
    QCategoryAxis *self,
    const QString *label) {
  self->remove(*label);
}

//  void QCategoryAxis::replaceLabel(const QString &oldLabel, const QString
//      &newLabel)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCategoryAxis12replaceLabelERK7QStringS2_(
    QCategoryAxis *self,
    const QString *oldLabel,
    const QString *newLabel) {
  self->replaceLabel(*oldLabel, *newLabel);
}

//  qreal QCategoryAxis::startValue(const QString &categoryLabel) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QCategoryAxis10startValueERK7QString(
    const QCategoryAxis *self,
    const QString *categoryLabel) {
  return self->startValue(*categoryLabel);
}

//  void QCategoryAxis::setStartValue(qreal min)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCategoryAxis13setStartValueEd(
    QCategoryAxis *self,
    qreal min) {
  self->setStartValue(min);
}

//  qreal QCategoryAxis::endValue(const QString &categoryLabel) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QCategoryAxis8endValueERK7QString(
    const QCategoryAxis *self,
    const QString *categoryLabel) {
  return self->endValue(*categoryLabel);
}

//  QStringList QCategoryAxis::categoriesLabels()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN13QCategoryAxis16categoriesLabelsEv(
    QCategoryAxis *self) {
  return new QList<QString>(self->categoriesLabels());
}

//  int QCategoryAxis::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QCategoryAxis5countEv(const QCategoryAxis *self) {
  return self->count();
}

//  QCategoryAxis::AxisLabelsPosition QCategoryAxis::labelsPosition() const
extern "C" Q_DECL_EXPORT
QCategoryAxis::AxisLabelsPosition ritual_ZNK13QCategoryAxis14labelsPositionEv(
    const QCategoryAxis *self) {
  return self->labelsPosition();
}

//  void QCategoryAxis::setLabelsPosition(QCategoryAxis::AxisLabelsPosition
//      position)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCategoryAxis17setLabelsPositionENS_18AxisLabelsPositionE(
    QCategoryAxis *self,
    QCategoryAxis::AxisLabelsPosition position) {
  self->setLabelsPosition(position);
}

//  void QCategoryAxis::categoriesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCategoryAxis17categoriesChangedEv(QCategoryAxis *self) {
  self->categoriesChanged();
}

//  void
//      QCategoryAxis::labelsPositionChanged(QCategoryAxis::AxisLabelsPositio
//      n position)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCategoryAxis21labelsPositionChangedENS_18AxisLabelsPositionE(
    QCategoryAxis *self,
    QCategoryAxis::AxisLabelsPosition position) {
  self->labelsPositionChanged(position);
}

//  QCategoryAxisPrivate *QCategoryAxis::d_func()
extern "C" Q_DECL_EXPORT
QCategoryAxisPrivate *ritual_ZN13QCategoryAxis6d_funcEv(
    QCategoryAxis *self) {
  return self->d_func();
}

//  const QCategoryAxisPrivate *QCategoryAxis::d_func() const
extern "C" Q_DECL_EXPORT
const QCategoryAxisPrivate *ritual_ZNK13QCategoryAxis6d_funcEv(
    const QCategoryAxis *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQCategoryAxis, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCategoryAxis(
    QCategoryAxis *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCategoryAxis *>(self)->take(key, call);
}

//  AxisType QCategoryAxis::type() const
extern "C" Q_DECL_EXPORT
QAbstractAxis::AxisType ritual_own_ZNK13QCategoryAxis4typeEv(
    const QCategoryAxis *self) {
  return self->QCategoryAxis::type();
}
