//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qsortpolicy.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qsortpolicy.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>
#include <Qt3DRender/Qt3DRender>

//  A Qt3DRender::QSortPolicy that Python can take functions over in. Every Qt3DRender::QSortPolicy
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QSortPolicyCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QSortPolicyCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QSortPolicyCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QSortPolicyCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QSortPolicyCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QSortPolicyCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QSortPolicyCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QSortPolicy : public Qt3DRender::QSortPolicy {
public:
  using Qt3DRender::QSortPolicy::QSortPolicy;
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
      CuteQt3DRender_QSortPolicyCall0 call = reinterpret_cast<CuteQt3DRender_QSortPolicyCall0>(taken[0]);
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
      CuteQt3DRender_QSortPolicyCall1 call = reinterpret_cast<CuteQt3DRender_QSortPolicyCall1>(taken[1]);
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
      CuteQt3DRender_QSortPolicyCall2 call = reinterpret_cast<CuteQt3DRender_QSortPolicyCall2>(taken[2]);
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
      CuteQt3DRender_QSortPolicyCall3 call = reinterpret_cast<CuteQt3DRender_QSortPolicyCall3>(taken[3]);
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
      CuteQt3DRender_QSortPolicyCall4 call = reinterpret_cast<CuteQt3DRender_QSortPolicyCall4>(taken[4]);
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
      CuteQt3DRender_QSortPolicyCall5 call = reinterpret_cast<CuteQt3DRender_QSortPolicyCall5>(taken[5]);
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
      CuteQt3DRender_QSortPolicyCall6 call = reinterpret_cast<CuteQt3DRender_QSortPolicyCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QSortPolicy::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender11QSortPolicy10metaObjectEv(
    const Qt3DRender::QSortPolicy *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QSortPolicy::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender11QSortPolicy11qt_metacastEPKc(
    Qt3DRender::QSortPolicy *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QSortPolicy::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender11QSortPolicy11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QSortPolicy *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QSortPolicy::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender11QSortPolicy2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QSortPolicy::tr(s, c, n));
}

//  Qt3DRender::QSortPolicy::QSortPolicy(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QSortPolicy *ritual_ZN10Qt3DRender11QSortPolicyC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QSortPolicy(parent);
}

//  Qt3DRender::QSortPolicy::~QSortPolicy()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QSortPolicyD1Ev(Qt3DRender::QSortPolicy *self) {
  delete self;
}

//  QList<SortType> Qt3DRender::QSortPolicy::sortTypes() const
extern "C" Q_DECL_EXPORT
QList<Qt3DRender::QSortPolicy::SortType> *ritual_ZNK10Qt3DRender11QSortPolicy9sortTypesEv(
    const Qt3DRender::QSortPolicy *self) {
  return new QList<Qt3DRender::QSortPolicy::SortType>(self->sortTypes());
}

//  QList<int> Qt3DRender::QSortPolicy::sortTypesInt() const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK10Qt3DRender11QSortPolicy12sortTypesIntEv(
    const Qt3DRender::QSortPolicy *self) {
  return new QList<int>(self->sortTypesInt());
}

//  void Qt3DRender::QSortPolicy::setSortTypes(const QList<SortType>
//      &sortTypes)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QSortPolicy12setSortTypesERK5QListINS0_8SortTypeEE(
    Qt3DRender::QSortPolicy *self,
    const QList<Qt3DRender::QSortPolicy::SortType> *sortTypes) {
  self->setSortTypes(*sortTypes);
}

//  void Qt3DRender::QSortPolicy::setSortTypes(const QList<int>
//      &sortTypesInt)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QSortPolicy12setSortTypesERK5QListIiE(
    Qt3DRender::QSortPolicy *self,
    const QList<int> *sortTypesInt) {
  self->setSortTypes(*sortTypesInt);
}

//  void Qt3DRender::QSortPolicy::sortTypesChanged(const QList<SortType>
//      &sortTypes)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QSortPolicy16sortTypesChangedERK5QListINS0_8SortTypeEE(
    Qt3DRender::QSortPolicy *self,
    const QList<Qt3DRender::QSortPolicy::SortType> *sortTypes) {
  self->sortTypesChanged(*sortTypes);
}

//  void Qt3DRender::QSortPolicy::sortTypesChanged(const QList<int>
//      &sortTypes)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11QSortPolicy16sortTypesChangedERK5QListIiE(
    Qt3DRender::QSortPolicy *self,
    const QList<int> *sortTypes) {
  self->sortTypesChanged(*sortTypes);
}

//  Qt3DRender::QSortPolicy::QSortPolicy(QSortPolicyPrivate &dd,
//      Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QSortPolicy *ritual_ZN10Qt3DRender11QSortPolicyC1ERNS_18QSortPolicyPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QSortPolicyPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QSortPolicy(*dd, parent);
}

//  QSortPolicyPrivate *Qt3DRender::QSortPolicy::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QSortPolicyPrivate *ritual_ZN10Qt3DRender11QSortPolicy6d_funcEv(
    Qt3DRender::QSortPolicy *self) {
  return self->d_func();
}

//  const QSortPolicyPrivate *Qt3DRender::QSortPolicy::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QSortPolicyPrivate *ritual_ZNK10Qt3DRender11QSortPolicy6d_funcEv(
    const Qt3DRender::QSortPolicy *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QSortPolicy, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QSortPolicy(
    Qt3DRender::QSortPolicy *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QSortPolicy *>(self)->take(key, call);
}

//  a QList<Qt3DRender::QSortPolicy::SortType> a ritual of
//      Qt3DRender::QSortPolicy gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QSortPolicy__QList_Qt3DRender_QSortPolicy_SortType(
    QList<Qt3DRender::QSortPolicy::SortType> *self) {
  delete self;
}

//  a QList<int> a ritual of Qt3DRender::QSortPolicy gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QSortPolicy__QList_int(QList<int> *self) {
  delete self;
}
