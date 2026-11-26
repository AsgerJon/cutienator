//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qlayerfilter.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qlayerfilter.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>
#include <Qt3DRender/Qt3DRender>

//  A Qt3DRender::QLayerFilter that Python can take functions over in. Every Qt3DRender::QLayerFilter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QLayerFilterCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QLayerFilterCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QLayerFilterCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QLayerFilterCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QLayerFilterCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QLayerFilterCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QLayerFilterCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QLayerFilter : public Qt3DRender::QLayerFilter {
public:
  using Qt3DRender::QLayerFilter::QLayerFilter;
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
      CuteQt3DRender_QLayerFilterCall0 call = reinterpret_cast<CuteQt3DRender_QLayerFilterCall0>(taken[0]);
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
      CuteQt3DRender_QLayerFilterCall1 call = reinterpret_cast<CuteQt3DRender_QLayerFilterCall1>(taken[1]);
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
      CuteQt3DRender_QLayerFilterCall2 call = reinterpret_cast<CuteQt3DRender_QLayerFilterCall2>(taken[2]);
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
      CuteQt3DRender_QLayerFilterCall3 call = reinterpret_cast<CuteQt3DRender_QLayerFilterCall3>(taken[3]);
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
      CuteQt3DRender_QLayerFilterCall4 call = reinterpret_cast<CuteQt3DRender_QLayerFilterCall4>(taken[4]);
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
      CuteQt3DRender_QLayerFilterCall5 call = reinterpret_cast<CuteQt3DRender_QLayerFilterCall5>(taken[5]);
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
      CuteQt3DRender_QLayerFilterCall6 call = reinterpret_cast<CuteQt3DRender_QLayerFilterCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QLayerFilter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender12QLayerFilter10metaObjectEv(
    const Qt3DRender::QLayerFilter *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QLayerFilter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender12QLayerFilter11qt_metacastEPKc(
    Qt3DRender::QLayerFilter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QLayerFilter::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender12QLayerFilter11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QLayerFilter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QLayerFilter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender12QLayerFilter2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QLayerFilter::tr(s, c, n));
}

//  Qt3DRender::QLayerFilter::QLayerFilter(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QLayerFilter *ritual_ZN10Qt3DRender12QLayerFilterC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QLayerFilter(parent);
}

//  Qt3DRender::QLayerFilter::~QLayerFilter()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QLayerFilterD1Ev(
    Qt3DRender::QLayerFilter *self) {
  delete self;
}

//  void Qt3DRender::QLayerFilter::addLayer(QLayer *layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QLayerFilter8addLayerEPNS_6QLayerE(
    Qt3DRender::QLayerFilter *self,
    Qt3DRender::QLayer *layer) {
  self->addLayer(layer);
}

//  void Qt3DRender::QLayerFilter::removeLayer(QLayer *layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QLayerFilter11removeLayerEPNS_6QLayerE(
    Qt3DRender::QLayerFilter *self,
    Qt3DRender::QLayer *layer) {
  self->removeLayer(layer);
}

//  QList<QLayer *> Qt3DRender::QLayerFilter::layers() const
extern "C" Q_DECL_EXPORT
QList<Qt3DRender::QLayer *> *ritual_ZNK10Qt3DRender12QLayerFilter6layersEv(
    const Qt3DRender::QLayerFilter *self) {
  return new QList<Qt3DRender::QLayer *>(self->layers());
}

//  FilterMode Qt3DRender::QLayerFilter::filterMode() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QLayerFilter::FilterMode ritual_ZNK10Qt3DRender12QLayerFilter10filterModeEv(
    const Qt3DRender::QLayerFilter *self) {
  return self->filterMode();
}

//  void Qt3DRender::QLayerFilter::setFilterMode(FilterMode filterMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QLayerFilter13setFilterModeENS0_10FilterModeE(
    Qt3DRender::QLayerFilter *self,
    Qt3DRender::QLayerFilter::FilterMode filterMode) {
  self->setFilterMode(filterMode);
}

//  void Qt3DRender::QLayerFilter::filterModeChanged(FilterMode filterMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QLayerFilter17filterModeChangedENS0_10FilterModeE(
    Qt3DRender::QLayerFilter *self,
    Qt3DRender::QLayerFilter::FilterMode filterMode) {
  self->filterModeChanged(filterMode);
}

//  Qt3DRender::QLayerFilter::QLayerFilter(QLayerFilterPrivate &dd,
//      Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QLayerFilter *ritual_ZN10Qt3DRender12QLayerFilterC1ERNS_19QLayerFilterPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QLayerFilterPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QLayerFilter(*dd, parent);
}

//  QLayerFilterPrivate *Qt3DRender::QLayerFilter::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QLayerFilterPrivate *ritual_ZN10Qt3DRender12QLayerFilter6d_funcEv(
    Qt3DRender::QLayerFilter *self) {
  return self->d_func();
}

//  const QLayerFilterPrivate *Qt3DRender::QLayerFilter::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QLayerFilterPrivate *ritual_ZNK10Qt3DRender12QLayerFilter6d_funcEv(
    const Qt3DRender::QLayerFilter *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QLayerFilter, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QLayerFilter(
    Qt3DRender::QLayerFilter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QLayerFilter *>(self)->take(key, call);
}

//  a QList<Qt3DRender::QLayer *> a ritual of Qt3DRender::QLayerFilter gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QLayerFilter__QList_Qt3DRender_QLayer(
    QList<Qt3DRender::QLayer *> *self) {
  delete self;
}
