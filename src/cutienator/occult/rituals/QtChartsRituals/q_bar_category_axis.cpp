//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/qbarcategoryaxis.h, Qt 6.12.0. Changes made here are lost.
#include <QtCharts/qbarcategoryaxis.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QBarCategoryAxis that Python can take functions over in. Every QBarCategoryAxis
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQBarCategoryAxisCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBarCategoryAxisCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBarCategoryAxisCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarCategoryAxisCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarCategoryAxisCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarCategoryAxisCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarCategoryAxisCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBarCategoryAxisCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQBarCategoryAxis : public QBarCategoryAxis {
public:
  using QBarCategoryAxis::QBarCategoryAxis;
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

  //  AxisType QBarCategoryAxis::type() const
  QAbstractAxis::AxisType type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQBarCategoryAxisCall0 call = reinterpret_cast<CuteQBarCategoryAxisCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractAxis::AxisType>(given);
    }
    return QBarCategoryAxis::type();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQBarCategoryAxisCall1 call = reinterpret_cast<CuteQBarCategoryAxisCall1>(taken[1]);
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
      CuteQBarCategoryAxisCall2 call = reinterpret_cast<CuteQBarCategoryAxisCall2>(taken[2]);
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
      CuteQBarCategoryAxisCall3 call = reinterpret_cast<CuteQBarCategoryAxisCall3>(taken[3]);
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
      CuteQBarCategoryAxisCall4 call = reinterpret_cast<CuteQBarCategoryAxisCall4>(taken[4]);
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
      CuteQBarCategoryAxisCall5 call = reinterpret_cast<CuteQBarCategoryAxisCall5>(taken[5]);
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
      CuteQBarCategoryAxisCall6 call = reinterpret_cast<CuteQBarCategoryAxisCall6>(taken[6]);
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
      CuteQBarCategoryAxisCall7 call = reinterpret_cast<CuteQBarCategoryAxisCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QBarCategoryAxis::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QBarCategoryAxis10metaObjectEv(
    const QBarCategoryAxis *self) {
  return self->metaObject();
}

//  void *QBarCategoryAxis::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QBarCategoryAxis11qt_metacastEPKc(
    QBarCategoryAxis *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QBarCategoryAxis::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QBarCategoryAxis11qt_metacallEN11QMetaObject4CallEiPPv(
    QBarCategoryAxis *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QBarCategoryAxis::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QBarCategoryAxis2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBarCategoryAxis::tr(s, c, n));
}

//  QBarCategoryAxis::QBarCategoryAxis(QObject *parent)
extern "C" Q_DECL_EXPORT
QBarCategoryAxis *ritual_ZN16QBarCategoryAxisC1EP7QObject(QObject *parent) {
  return new CuteQBarCategoryAxis(parent);
}

//  QBarCategoryAxis::~QBarCategoryAxis()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBarCategoryAxisD1Ev(QBarCategoryAxis *self) {
  delete self;
}

//  QBarCategoryAxis::QBarCategoryAxis(QBarCategoryAxisPrivate &d, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QBarCategoryAxis *ritual_ZN16QBarCategoryAxisC1ER23QBarCategoryAxisPrivateP7QObject(
    QBarCategoryAxisPrivate *d,
    QObject *parent) {
  return new CuteQBarCategoryAxis(*d, parent);
}

//  AxisType QBarCategoryAxis::type() const
extern "C" Q_DECL_EXPORT
QAbstractAxis::AxisType ritual_ZNK16QBarCategoryAxis4typeEv(
    const QBarCategoryAxis *self) {
  return self->type();
}

//  void QBarCategoryAxis::append(const QStringList &categories)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBarCategoryAxis6appendERK5QListI7QStringE(
    QBarCategoryAxis *self,
    const QList<QString> *categories) {
  self->append(*categories);
}

//  void QBarCategoryAxis::append(const QString &category)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBarCategoryAxis6appendERK7QString(
    QBarCategoryAxis *self,
    const QString *category) {
  self->append(*category);
}

//  void QBarCategoryAxis::remove(const QString &category)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBarCategoryAxis6removeERK7QString(
    QBarCategoryAxis *self,
    const QString *category) {
  self->remove(*category);
}

//  void QBarCategoryAxis::insert(int index, const QString &category)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBarCategoryAxis6insertEiRK7QString(
    QBarCategoryAxis *self,
    int index,
    const QString *category) {
  self->insert(index, *category);
}

//  void QBarCategoryAxis::replace(const QString &oldCategory, const QString
//      &newCategory)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBarCategoryAxis7replaceERK7QStringS2_(
    QBarCategoryAxis *self,
    const QString *oldCategory,
    const QString *newCategory) {
  self->replace(*oldCategory, *newCategory);
}

//  void QBarCategoryAxis::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBarCategoryAxis5clearEv(QBarCategoryAxis *self) {
  self->clear();
}

//  void QBarCategoryAxis::setCategories(const QStringList &categories)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBarCategoryAxis13setCategoriesERK5QListI7QStringE(
    QBarCategoryAxis *self,
    const QList<QString> *categories) {
  self->setCategories(*categories);
}

//  QStringList QBarCategoryAxis::categories()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN16QBarCategoryAxis10categoriesEv(
    QBarCategoryAxis *self) {
  return new QList<QString>(self->categories());
}

//  int QBarCategoryAxis::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QBarCategoryAxis5countEv(const QBarCategoryAxis *self) {
  return self->count();
}

//  QString QBarCategoryAxis::at(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QBarCategoryAxis2atEi(
    const QBarCategoryAxis *self,
    int index) {
  return new QString(self->at(index));
}

//  void QBarCategoryAxis::setMin(const QString &minCategory)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBarCategoryAxis6setMinERK7QString(
    QBarCategoryAxis *self,
    const QString *minCategory) {
  self->setMin(*minCategory);
}

//  QString QBarCategoryAxis::min() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QBarCategoryAxis3minEv(const QBarCategoryAxis *self) {
  return new QString(self->min());
}

//  void QBarCategoryAxis::setMax(const QString &maxCategory)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBarCategoryAxis6setMaxERK7QString(
    QBarCategoryAxis *self,
    const QString *maxCategory) {
  self->setMax(*maxCategory);
}

//  QString QBarCategoryAxis::max() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QBarCategoryAxis3maxEv(const QBarCategoryAxis *self) {
  return new QString(self->max());
}

//  void QBarCategoryAxis::setRange(const QString &minCategory, const QString
//      &maxCategory)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBarCategoryAxis8setRangeERK7QStringS2_(
    QBarCategoryAxis *self,
    const QString *minCategory,
    const QString *maxCategory) {
  self->setRange(*minCategory, *maxCategory);
}

//  void QBarCategoryAxis::categoriesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBarCategoryAxis17categoriesChangedEv(
    QBarCategoryAxis *self) {
  self->categoriesChanged();
}

//  void QBarCategoryAxis::minChanged(const QString &min)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBarCategoryAxis10minChangedERK7QString(
    QBarCategoryAxis *self,
    const QString *min) {
  self->minChanged(*min);
}

//  void QBarCategoryAxis::maxChanged(const QString &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBarCategoryAxis10maxChangedERK7QString(
    QBarCategoryAxis *self,
    const QString *max) {
  self->maxChanged(*max);
}

//  void QBarCategoryAxis::rangeChanged(const QString &min, const QString
//      &max)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBarCategoryAxis12rangeChangedERK7QStringS2_(
    QBarCategoryAxis *self,
    const QString *min,
    const QString *max) {
  self->rangeChanged(*min, *max);
}

//  void QBarCategoryAxis::countChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBarCategoryAxis12countChangedEv(QBarCategoryAxis *self) {
  self->countChanged();
}

//  QBarCategoryAxisPrivate *QBarCategoryAxis::d_func()
extern "C" Q_DECL_EXPORT
QBarCategoryAxisPrivate *ritual_ZN16QBarCategoryAxis6d_funcEv(
    QBarCategoryAxis *self) {
  return self->d_func();
}

//  const QBarCategoryAxisPrivate *QBarCategoryAxis::d_func() const
extern "C" Q_DECL_EXPORT
const QBarCategoryAxisPrivate *ritual_ZNK16QBarCategoryAxis6d_funcEv(
    const QBarCategoryAxis *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQBarCategoryAxis, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBarCategoryAxis(
    QBarCategoryAxis *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBarCategoryAxis *>(self)->take(key, call);
}

//  AxisType QBarCategoryAxis::type() const
extern "C" Q_DECL_EXPORT
QAbstractAxis::AxisType ritual_own_ZNK16QBarCategoryAxis4typeEv(
    const QBarCategoryAxis *self) {
  return self->QBarCategoryAxis::type();
}
