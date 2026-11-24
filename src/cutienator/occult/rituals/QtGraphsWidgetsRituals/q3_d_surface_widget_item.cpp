//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphsWidgets/q3dsurfacewidgetitem.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphsWidgets/qgraphswidgetsglobal.h>
#if QT_CONFIG(graphs_3d_surface3d)
#include <QtGraphsWidgets/q3dsurfacewidgetitem.h>
#include <QtCore/qstring.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qsurface3dseries.h>
#include <QtGraphs/qvalue3daxis.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on Q3DSurfaceWidgetItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQ3DSurfaceWidgetItem : Q3DSurfaceWidgetItem {
  using Q3DSurfaceWidgetItem::event;
};

//  A Q3DSurfaceWidgetItem that Python can take functions over in. Every Q3DSurfaceWidgetItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DSurfaceWidgetItemCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DSurfaceWidgetItemCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DSurfaceWidgetItemCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DSurfaceWidgetItemCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DSurfaceWidgetItemCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DSurfaceWidgetItemCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DSurfaceWidgetItemCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQ3DSurfaceWidgetItem : public Q3DSurfaceWidgetItem {
public:
  using Q3DSurfaceWidgetItem::Q3DSurfaceWidgetItem;
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
  //  bool Q3DSurfaceWidgetItem::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQ3DSurfaceWidgetItemCall0 call = reinterpret_cast<CuteQ3DSurfaceWidgetItemCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return Q3DSurfaceWidgetItem::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool Q3DGraphsWidgetItem::eventFilter(QObject *obj, QEvent *event)
  bool eventFilter(QObject *obj, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQ3DSurfaceWidgetItemCall1 call = reinterpret_cast<CuteQ3DSurfaceWidgetItemCall1>(taken[1]);
      bool given = call(this, obj, event, &handled);
      if (handled) return given;
    }
    return Q3DGraphsWidgetItem::eventFilter(obj, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQ3DSurfaceWidgetItemCall2 call = reinterpret_cast<CuteQ3DSurfaceWidgetItemCall2>(taken[2]);
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
      CuteQ3DSurfaceWidgetItemCall3 call = reinterpret_cast<CuteQ3DSurfaceWidgetItemCall3>(taken[3]);
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
      CuteQ3DSurfaceWidgetItemCall4 call = reinterpret_cast<CuteQ3DSurfaceWidgetItemCall4>(taken[4]);
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
      CuteQ3DSurfaceWidgetItemCall5 call = reinterpret_cast<CuteQ3DSurfaceWidgetItemCall5>(taken[5]);
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
      CuteQ3DSurfaceWidgetItemCall6 call = reinterpret_cast<CuteQ3DSurfaceWidgetItemCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Q3DSurfaceWidgetItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20Q3DSurfaceWidgetItem10metaObjectEv(
    const Q3DSurfaceWidgetItem *self) {
  return self->metaObject();
}

//  QString Q3DSurfaceWidgetItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20Q3DSurfaceWidgetItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Q3DSurfaceWidgetItem::tr(s, c, n));
}

//  Q3DSurfaceWidgetItem::Q3DSurfaceWidgetItem(QObject *parent)
extern "C" Q_DECL_EXPORT
Q3DSurfaceWidgetItem *ritual_ZN20Q3DSurfaceWidgetItemC1EP7QObject(
    QObject *parent) {
  return new CuteQ3DSurfaceWidgetItem(parent);
}

//  Q3DSurfaceWidgetItem::~Q3DSurfaceWidgetItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN20Q3DSurfaceWidgetItemD1Ev(Q3DSurfaceWidgetItem *self) {
  delete self;
}

//  void Q3DSurfaceWidgetItem::addSeries(QSurface3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Q3DSurfaceWidgetItem9addSeriesEP16QSurface3DSeries(
    Q3DSurfaceWidgetItem *self,
    QSurface3DSeries *series) {
  self->addSeries(series);
}

//  void Q3DSurfaceWidgetItem::removeSeries(QSurface3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Q3DSurfaceWidgetItem12removeSeriesEP16QSurface3DSeries(
    Q3DSurfaceWidgetItem *self,
    QSurface3DSeries *series) {
  self->removeSeries(series);
}

//  QList<QSurface3DSeries *> Q3DSurfaceWidgetItem::seriesList() const
extern "C" Q_DECL_EXPORT
QList<QSurface3DSeries *> *ritual_ZNK20Q3DSurfaceWidgetItem10seriesListEv(
    const Q3DSurfaceWidgetItem *self) {
  return new QList<QSurface3DSeries *>(self->seriesList());
}

//  QValue3DAxis *Q3DSurfaceWidgetItem::axisX() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK20Q3DSurfaceWidgetItem5axisXEv(
    const Q3DSurfaceWidgetItem *self) {
  return self->axisX();
}

//  QValue3DAxis *Q3DSurfaceWidgetItem::axisY() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK20Q3DSurfaceWidgetItem5axisYEv(
    const Q3DSurfaceWidgetItem *self) {
  return self->axisY();
}

//  QValue3DAxis *Q3DSurfaceWidgetItem::axisZ() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK20Q3DSurfaceWidgetItem5axisZEv(
    const Q3DSurfaceWidgetItem *self) {
  return self->axisZ();
}

//  void Q3DSurfaceWidgetItem::addAxis(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Q3DSurfaceWidgetItem7addAxisEP12QValue3DAxis(
    Q3DSurfaceWidgetItem *self,
    QValue3DAxis *axis) {
  self->addAxis(axis);
}

//  void Q3DSurfaceWidgetItem::releaseAxis(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Q3DSurfaceWidgetItem11releaseAxisEP12QValue3DAxis(
    Q3DSurfaceWidgetItem *self,
    QValue3DAxis *axis) {
  self->releaseAxis(axis);
}

//  QList<QValue3DAxis *> Q3DSurfaceWidgetItem::axes() const
extern "C" Q_DECL_EXPORT
QList<QValue3DAxis *> *ritual_ZNK20Q3DSurfaceWidgetItem4axesEv(
    const Q3DSurfaceWidgetItem *self) {
  return new QList<QValue3DAxis *>(self->axes());
}

//  QSurface3DSeries *Q3DSurfaceWidgetItem::selectedSeries() const
extern "C" Q_DECL_EXPORT
QSurface3DSeries *ritual_ZNK20Q3DSurfaceWidgetItem14selectedSeriesEv(
    const Q3DSurfaceWidgetItem *self) {
  return self->selectedSeries();
}

//  bool Q3DSurfaceWidgetItem::flipHorizontalGrid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20Q3DSurfaceWidgetItem18flipHorizontalGridEv(
    const Q3DSurfaceWidgetItem *self) {
  return self->flipHorizontalGrid();
}

//  void Q3DSurfaceWidgetItem::renderSliceToImage(int index, int
//      requestedIndex, QtGraphs3D::SliceCaptureType sliceType)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Q3DSurfaceWidgetItem18renderSliceToImageEiiN10QtGraphs3D16SliceCaptureTypeE(
    Q3DSurfaceWidgetItem *self,
    int index,
    int requestedIndex,
    QtGraphs3D::SliceCaptureType sliceType) {
  self->renderSliceToImage(index, requestedIndex, sliceType);
}

//  void Q3DSurfaceWidgetItem::setAxisX(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Q3DSurfaceWidgetItem8setAxisXEP12QValue3DAxis(
    Q3DSurfaceWidgetItem *self,
    QValue3DAxis *axis) {
  self->setAxisX(axis);
}

//  void Q3DSurfaceWidgetItem::setAxisY(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Q3DSurfaceWidgetItem8setAxisYEP12QValue3DAxis(
    Q3DSurfaceWidgetItem *self,
    QValue3DAxis *axis) {
  self->setAxisY(axis);
}

//  void Q3DSurfaceWidgetItem::setAxisZ(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Q3DSurfaceWidgetItem8setAxisZEP12QValue3DAxis(
    Q3DSurfaceWidgetItem *self,
    QValue3DAxis *axis) {
  self->setAxisZ(axis);
}

//  void Q3DSurfaceWidgetItem::setFlipHorizontalGrid(bool flip)
extern "C" Q_DECL_EXPORT
void ritual_ZN20Q3DSurfaceWidgetItem21setFlipHorizontalGridEb(
    Q3DSurfaceWidgetItem *self,
    bool flip) {
  self->setFlipHorizontalGrid(flip);
}

//  bool Q3DSurfaceWidgetItem::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20Q3DSurfaceWidgetItem5eventEP6QEvent(
    Q3DSurfaceWidgetItem *self,
    QEvent *event) {
  return self->event(event);
}

//  Q3DSurfaceWidgetItemPrivate *Q3DSurfaceWidgetItem::d_func()
extern "C" Q_DECL_EXPORT
Q3DSurfaceWidgetItemPrivate *ritual_ZN20Q3DSurfaceWidgetItem6d_funcEv(
    Q3DSurfaceWidgetItem *self) {
  return self->d_func();
}

//  const Q3DSurfaceWidgetItemPrivate *Q3DSurfaceWidgetItem::d_func() const
extern "C" Q_DECL_EXPORT
const Q3DSurfaceWidgetItemPrivate *ritual_ZNK20Q3DSurfaceWidgetItem6d_funcEv(
    const Q3DSurfaceWidgetItem *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQ3DSurfaceWidgetItem, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Q3DSurfaceWidgetItem(
    Q3DSurfaceWidgetItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQ3DSurfaceWidgetItem *>(self)->take(key, call);
}

//  bool Q3DSurfaceWidgetItem::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20Q3DSurfaceWidgetItem5eventEP6QEvent(
    Q3DSurfaceWidgetItem *self,
    QEvent *event) {
  return static_cast<OwnQ3DSurfaceWidgetItem *>(self)->OwnQ3DSurfaceWidgetItem::event(
      event);
}

#endif  // QT_CONFIG(graphs_3d_surface3d)
