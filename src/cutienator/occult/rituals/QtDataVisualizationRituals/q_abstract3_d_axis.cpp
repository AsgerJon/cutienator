//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/qabstract3daxis.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtDataVisualization/qabstract3daxis.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QAbstract3DAxis that Python can take functions over in. Every QAbstract3DAxis
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstract3DAxisCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstract3DAxisCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DAxisCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DAxisCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DAxisCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DAxisCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DAxisCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstract3DAxis : public QAbstract3DAxis {
public:
  using QAbstract3DAxis::QAbstract3DAxis;
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
      CuteQAbstract3DAxisCall0 call = reinterpret_cast<CuteQAbstract3DAxisCall0>(taken[0]);
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
      CuteQAbstract3DAxisCall1 call = reinterpret_cast<CuteQAbstract3DAxisCall1>(taken[1]);
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
      CuteQAbstract3DAxisCall2 call = reinterpret_cast<CuteQAbstract3DAxisCall2>(taken[2]);
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
      CuteQAbstract3DAxisCall3 call = reinterpret_cast<CuteQAbstract3DAxisCall3>(taken[3]);
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
      CuteQAbstract3DAxisCall4 call = reinterpret_cast<CuteQAbstract3DAxisCall4>(taken[4]);
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
      CuteQAbstract3DAxisCall5 call = reinterpret_cast<CuteQAbstract3DAxisCall5>(taken[5]);
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
      CuteQAbstract3DAxisCall6 call = reinterpret_cast<CuteQAbstract3DAxisCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstract3DAxis::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QAbstract3DAxis10metaObjectEv(
    const QAbstract3DAxis *self) {
  return self->metaObject();
}

//  QString QAbstract3DAxis::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QAbstract3DAxis2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstract3DAxis::tr(s, c, n));
}

//  QAbstract3DAxis::QAbstract3DAxis(QAbstract3DAxisPrivate *d, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_ZN15QAbstract3DAxisC1EP22QAbstract3DAxisPrivateP7QObject(
    QAbstract3DAxisPrivate *d,
    QObject *parent) {
  return new CuteQAbstract3DAxis(d, parent);
}

//  QAbstract3DAxis::~QAbstract3DAxis()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstract3DAxisD1Ev(QAbstract3DAxis *self) {
  delete self;
}

//  void QAbstract3DAxis::setTitle(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstract3DAxis8setTitleERK7QString(
    QAbstract3DAxis *self,
    const QString *title) {
  self->setTitle(*title);
}

//  QString QAbstract3DAxis::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QAbstract3DAxis5titleEv(const QAbstract3DAxis *self) {
  return new QString(self->title());
}

//  void QAbstract3DAxis::setLabels(const QStringList &labels)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstract3DAxis9setLabelsERK5QListI7QStringE(
    QAbstract3DAxis *self,
    const QList<QString> *labels) {
  self->setLabels(*labels);
}

//  QStringList QAbstract3DAxis::labels() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK15QAbstract3DAxis6labelsEv(
    const QAbstract3DAxis *self) {
  return new QList<QString>(self->labels());
}

//  AxisOrientation QAbstract3DAxis::orientation() const
extern "C" Q_DECL_EXPORT
QAbstract3DAxis::AxisOrientation ritual_ZNK15QAbstract3DAxis11orientationEv(
    const QAbstract3DAxis *self) {
  return self->orientation();
}

//  AxisType QAbstract3DAxis::type() const
extern "C" Q_DECL_EXPORT
QAbstract3DAxis::AxisType ritual_ZNK15QAbstract3DAxis4typeEv(
    const QAbstract3DAxis *self) {
  return self->type();
}

//  void QAbstract3DAxis::setMin(float min)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstract3DAxis6setMinEf(QAbstract3DAxis *self, float min) {
  self->setMin(min);
}

//  float QAbstract3DAxis::min() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK15QAbstract3DAxis3minEv(const QAbstract3DAxis *self) {
  return self->min();
}

//  void QAbstract3DAxis::setMax(float max)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstract3DAxis6setMaxEf(QAbstract3DAxis *self, float max) {
  self->setMax(max);
}

//  float QAbstract3DAxis::max() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK15QAbstract3DAxis3maxEv(const QAbstract3DAxis *self) {
  return self->max();
}

//  void QAbstract3DAxis::setAutoAdjustRange(bool autoAdjust)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstract3DAxis18setAutoAdjustRangeEb(
    QAbstract3DAxis *self,
    bool autoAdjust) {
  self->setAutoAdjustRange(autoAdjust);
}

//  bool QAbstract3DAxis::isAutoAdjustRange() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstract3DAxis17isAutoAdjustRangeEv(
    const QAbstract3DAxis *self) {
  return self->isAutoAdjustRange();
}

//  void QAbstract3DAxis::setRange(float min, float max)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstract3DAxis8setRangeEff(
    QAbstract3DAxis *self,
    float min,
    float max) {
  self->setRange(min, max);
}

//  void QAbstract3DAxis::setLabelAutoRotation(float angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstract3DAxis20setLabelAutoRotationEf(
    QAbstract3DAxis *self,
    float angle) {
  self->setLabelAutoRotation(angle);
}

//  float QAbstract3DAxis::labelAutoRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK15QAbstract3DAxis17labelAutoRotationEv(
    const QAbstract3DAxis *self) {
  return self->labelAutoRotation();
}

//  void QAbstract3DAxis::setTitleVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstract3DAxis15setTitleVisibleEb(
    QAbstract3DAxis *self,
    bool visible) {
  self->setTitleVisible(visible);
}

//  bool QAbstract3DAxis::isTitleVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstract3DAxis14isTitleVisibleEv(
    const QAbstract3DAxis *self) {
  return self->isTitleVisible();
}

//  void QAbstract3DAxis::setTitleFixed(bool fixed)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstract3DAxis13setTitleFixedEb(
    QAbstract3DAxis *self,
    bool fixed) {
  self->setTitleFixed(fixed);
}

//  bool QAbstract3DAxis::isTitleFixed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstract3DAxis12isTitleFixedEv(
    const QAbstract3DAxis *self) {
  return self->isTitleFixed();
}

//  a Python function taken by a CuteQAbstract3DAxis, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstract3DAxis(
    QAbstract3DAxis *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstract3DAxis *>(self)->take(key, call);
}

//  QList<QAbstract3DAxis *>::QList()
extern "C" Q_DECL_EXPORT
QList<QAbstract3DAxis *> *ritual_list_make_QAbstract3DAxis_ptr() {
  return new QList<QAbstract3DAxis *>();
}

//  void QList<QAbstract3DAxis *>::append(const QAbstract3DAxis * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QAbstract3DAxis_ptr(
    QList<QAbstract3DAxis *> *self,
    QAbstract3DAxis *element) {
  self->append(element);
}

//  qsizetype QList<QAbstract3DAxis *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QAbstract3DAxis_ptr(
    const QList<QAbstract3DAxis *> *self) {
  return self->size();
}

//  const QAbstract3DAxis * &QList<QAbstract3DAxis *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_list_at_QAbstract3DAxis_ptr(
    const QList<QAbstract3DAxis *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QAbstract3DAxis *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QAbstract3DAxis_ptr(QList<QAbstract3DAxis *> *self) {
  delete self;
}
