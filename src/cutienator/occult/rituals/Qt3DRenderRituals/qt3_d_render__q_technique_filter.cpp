//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qtechniquefilter.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qtechniquefilter.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>
#include <Qt3DRender/Qt3DRender>

//  A Qt3DRender::QTechniqueFilter that Python can take functions over in. Every Qt3DRender::QTechniqueFilter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QTechniqueFilterCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QTechniqueFilterCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QTechniqueFilterCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QTechniqueFilterCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QTechniqueFilterCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QTechniqueFilterCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QTechniqueFilterCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QTechniqueFilter : public Qt3DRender::QTechniqueFilter {
public:
  using Qt3DRender::QTechniqueFilter::QTechniqueFilter;
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
      CuteQt3DRender_QTechniqueFilterCall0 call = reinterpret_cast<CuteQt3DRender_QTechniqueFilterCall0>(taken[0]);
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
      CuteQt3DRender_QTechniqueFilterCall1 call = reinterpret_cast<CuteQt3DRender_QTechniqueFilterCall1>(taken[1]);
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
      CuteQt3DRender_QTechniqueFilterCall2 call = reinterpret_cast<CuteQt3DRender_QTechniqueFilterCall2>(taken[2]);
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
      CuteQt3DRender_QTechniqueFilterCall3 call = reinterpret_cast<CuteQt3DRender_QTechniqueFilterCall3>(taken[3]);
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
      CuteQt3DRender_QTechniqueFilterCall4 call = reinterpret_cast<CuteQt3DRender_QTechniqueFilterCall4>(taken[4]);
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
      CuteQt3DRender_QTechniqueFilterCall5 call = reinterpret_cast<CuteQt3DRender_QTechniqueFilterCall5>(taken[5]);
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
      CuteQt3DRender_QTechniqueFilterCall6 call = reinterpret_cast<CuteQt3DRender_QTechniqueFilterCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QTechniqueFilter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender16QTechniqueFilter10metaObjectEv(
    const Qt3DRender::QTechniqueFilter *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QTechniqueFilter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender16QTechniqueFilter11qt_metacastEPKc(
    Qt3DRender::QTechniqueFilter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QTechniqueFilter::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender16QTechniqueFilter11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QTechniqueFilter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QTechniqueFilter::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender16QTechniqueFilter2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QTechniqueFilter::tr(s, c, n));
}

//  Qt3DRender::QTechniqueFilter::QTechniqueFilter(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QTechniqueFilter *ritual_ZN10Qt3DRender16QTechniqueFilterC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QTechniqueFilter(parent);
}

//  Qt3DRender::QTechniqueFilter::~QTechniqueFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QTechniqueFilterD1Ev(
    Qt3DRender::QTechniqueFilter *self) {
  delete self;
}

//  QList<QFilterKey *> Qt3DRender::QTechniqueFilter::matchAll() const
extern "C" Q_DECL_EXPORT
QList<Qt3DRender::QFilterKey *> *ritual_ZNK10Qt3DRender16QTechniqueFilter8matchAllEv(
    const Qt3DRender::QTechniqueFilter *self) {
  return new QList<Qt3DRender::QFilterKey *>(self->matchAll());
}

//  void Qt3DRender::QTechniqueFilter::addMatch(QFilterKey *filterKey)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QTechniqueFilter8addMatchEPNS_10QFilterKeyE(
    Qt3DRender::QTechniqueFilter *self,
    Qt3DRender::QFilterKey *filterKey) {
  self->addMatch(filterKey);
}

//  void Qt3DRender::QTechniqueFilter::removeMatch(QFilterKey *filterKey)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QTechniqueFilter11removeMatchEPNS_10QFilterKeyE(
    Qt3DRender::QTechniqueFilter *self,
    Qt3DRender::QFilterKey *filterKey) {
  self->removeMatch(filterKey);
}

//  void Qt3DRender::QTechniqueFilter::addParameter(QParameter *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QTechniqueFilter12addParameterEPNS_10QParameterE(
    Qt3DRender::QTechniqueFilter *self,
    Qt3DRender::QParameter *p) {
  self->addParameter(p);
}

//  void Qt3DRender::QTechniqueFilter::removeParameter(QParameter *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QTechniqueFilter15removeParameterEPNS_10QParameterE(
    Qt3DRender::QTechniqueFilter *self,
    Qt3DRender::QParameter *p) {
  self->removeParameter(p);
}

//  QList<QParameter *> Qt3DRender::QTechniqueFilter::parameters() const
extern "C" Q_DECL_EXPORT
QList<Qt3DRender::QParameter *> *ritual_ZNK10Qt3DRender16QTechniqueFilter10parametersEv(
    const Qt3DRender::QTechniqueFilter *self) {
  return new QList<Qt3DRender::QParameter *>(self->parameters());
}

//  Qt3DRender::QTechniqueFilter::QTechniqueFilter(QTechniqueFilterPrivate
//      &dd, Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QTechniqueFilter *ritual_ZN10Qt3DRender16QTechniqueFilterC1ERNS_23QTechniqueFilterPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QTechniqueFilterPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QTechniqueFilter(*dd, parent);
}

//  QTechniqueFilterPrivate *Qt3DRender::QTechniqueFilter::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QTechniqueFilterPrivate *ritual_ZN10Qt3DRender16QTechniqueFilter6d_funcEv(
    Qt3DRender::QTechniqueFilter *self) {
  return self->d_func();
}

//  const QTechniqueFilterPrivate *Qt3DRender::QTechniqueFilter::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QTechniqueFilterPrivate *ritual_ZNK10Qt3DRender16QTechniqueFilter6d_funcEv(
    const Qt3DRender::QTechniqueFilter *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QTechniqueFilter, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QTechniqueFilter(
    Qt3DRender::QTechniqueFilter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QTechniqueFilter *>(self)->take(key, call);
}

//  a QList<Qt3DRender::QFilterKey *> a ritual of
//      Qt3DRender::QTechniqueFilter gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QTechniqueFilter__QList_Qt3DRender_QFilterKey(
    QList<Qt3DRender::QFilterKey *> *self) {
  delete self;
}

//  a QList<Qt3DRender::QParameter *> a ritual of
//      Qt3DRender::QTechniqueFilter gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QTechniqueFilter__QList_Qt3DRender_QParameter(
    QList<Qt3DRender::QParameter *> *self) {
  delete self;
}
