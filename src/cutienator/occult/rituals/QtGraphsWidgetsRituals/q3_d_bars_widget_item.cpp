//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphsWidgets/q3dbarswidgetitem.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphsWidgets/qgraphswidgetsglobal.h>
#if QT_CONFIG(graphs_3d_bars3d)
#include <QtGraphsWidgets/q3dbarswidgetitem.h>
#include <QtCore/qstring.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_bars3d))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qbar3dseries.h>
#endif
#include <QtCore/qsize.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d)))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qabstract3daxis.h>
#endif
#include <QtGui/qimage.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on Q3DBarsWidgetItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQ3DBarsWidgetItem : Q3DBarsWidgetItem {
  using Q3DBarsWidgetItem::event;
};

//  A Q3DBarsWidgetItem that Python can take functions over in. Every Q3DBarsWidgetItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DBarsWidgetItemCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DBarsWidgetItemCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DBarsWidgetItemCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DBarsWidgetItemCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DBarsWidgetItemCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DBarsWidgetItemCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DBarsWidgetItemCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQ3DBarsWidgetItem : public Q3DBarsWidgetItem {
public:
  using Q3DBarsWidgetItem::Q3DBarsWidgetItem;
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
  //  bool Q3DBarsWidgetItem::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQ3DBarsWidgetItemCall0 call = reinterpret_cast<CuteQ3DBarsWidgetItemCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return Q3DBarsWidgetItem::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool Q3DGraphsWidgetItem::eventFilter(QObject *obj, QEvent *event)
  bool eventFilter(QObject *obj, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQ3DBarsWidgetItemCall1 call = reinterpret_cast<CuteQ3DBarsWidgetItemCall1>(taken[1]);
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
      CuteQ3DBarsWidgetItemCall2 call = reinterpret_cast<CuteQ3DBarsWidgetItemCall2>(taken[2]);
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
      CuteQ3DBarsWidgetItemCall3 call = reinterpret_cast<CuteQ3DBarsWidgetItemCall3>(taken[3]);
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
      CuteQ3DBarsWidgetItemCall4 call = reinterpret_cast<CuteQ3DBarsWidgetItemCall4>(taken[4]);
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
      CuteQ3DBarsWidgetItemCall5 call = reinterpret_cast<CuteQ3DBarsWidgetItemCall5>(taken[5]);
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
      CuteQ3DBarsWidgetItemCall6 call = reinterpret_cast<CuteQ3DBarsWidgetItemCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Q3DBarsWidgetItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17Q3DBarsWidgetItem10metaObjectEv(
    const Q3DBarsWidgetItem *self) {
  return self->metaObject();
}

//  void *Q3DBarsWidgetItem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17Q3DBarsWidgetItem11qt_metacastEPKc(
    Q3DBarsWidgetItem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Q3DBarsWidgetItem::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17Q3DBarsWidgetItem11qt_metacallEN11QMetaObject4CallEiPPv(
    Q3DBarsWidgetItem *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Q3DBarsWidgetItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17Q3DBarsWidgetItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Q3DBarsWidgetItem::tr(s, c, n));
}

//  Q3DBarsWidgetItem::Q3DBarsWidgetItem(QObject *parent)
extern "C" Q_DECL_EXPORT
Q3DBarsWidgetItem *ritual_ZN17Q3DBarsWidgetItemC1EP7QObject(
    QObject *parent) {
  return new CuteQ3DBarsWidgetItem(parent);
}

//  Q3DBarsWidgetItem::~Q3DBarsWidgetItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItemD1Ev(Q3DBarsWidgetItem *self) {
  delete self;
}

//  QBar3DSeries *Q3DBarsWidgetItem::primarySeries() const
extern "C" Q_DECL_EXPORT
QBar3DSeries *ritual_ZNK17Q3DBarsWidgetItem13primarySeriesEv(
    const Q3DBarsWidgetItem *self) {
  return self->primarySeries();
}

//  void Q3DBarsWidgetItem::addSeries(QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItem9addSeriesEP12QBar3DSeries(
    Q3DBarsWidgetItem *self,
    QBar3DSeries *series) {
  self->addSeries(series);
}

//  void Q3DBarsWidgetItem::removeSeries(QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItem12removeSeriesEP12QBar3DSeries(
    Q3DBarsWidgetItem *self,
    QBar3DSeries *series) {
  self->removeSeries(series);
}

//  void Q3DBarsWidgetItem::insertSeries(int index, QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItem12insertSeriesEiP12QBar3DSeries(
    Q3DBarsWidgetItem *self,
    int index,
    QBar3DSeries *series) {
  self->insertSeries(index, series);
}

//  QList<QBar3DSeries *> Q3DBarsWidgetItem::seriesList() const
extern "C" Q_DECL_EXPORT
QList<QBar3DSeries *> *ritual_ZNK17Q3DBarsWidgetItem10seriesListEv(
    const Q3DBarsWidgetItem *self) {
  return new QList<QBar3DSeries *>(self->seriesList());
}

//  bool Q3DBarsWidgetItem::isMultiSeriesUniform() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17Q3DBarsWidgetItem20isMultiSeriesUniformEv(
    const Q3DBarsWidgetItem *self) {
  return self->isMultiSeriesUniform();
}

//  float Q3DBarsWidgetItem::barThickness() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK17Q3DBarsWidgetItem12barThicknessEv(
    const Q3DBarsWidgetItem *self) {
  return self->barThickness();
}

//  QSizeF Q3DBarsWidgetItem::barSpacing() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK17Q3DBarsWidgetItem10barSpacingEv(
    const Q3DBarsWidgetItem *self) {
  return new QSizeF(self->barSpacing());
}

//  bool Q3DBarsWidgetItem::isBarSpacingRelative() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17Q3DBarsWidgetItem20isBarSpacingRelativeEv(
    const Q3DBarsWidgetItem *self) {
  return self->isBarSpacingRelative();
}

//  QSizeF Q3DBarsWidgetItem::barSeriesMargin() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK17Q3DBarsWidgetItem15barSeriesMarginEv(
    const Q3DBarsWidgetItem *self) {
  return new QSizeF(self->barSeriesMargin());
}

//  QCategory3DAxis *Q3DBarsWidgetItem::rowAxis() const
extern "C" Q_DECL_EXPORT
QCategory3DAxis *ritual_ZNK17Q3DBarsWidgetItem7rowAxisEv(
    const Q3DBarsWidgetItem *self) {
  return self->rowAxis();
}

//  QCategory3DAxis *Q3DBarsWidgetItem::columnAxis() const
extern "C" Q_DECL_EXPORT
QCategory3DAxis *ritual_ZNK17Q3DBarsWidgetItem10columnAxisEv(
    const Q3DBarsWidgetItem *self) {
  return self->columnAxis();
}

//  QValue3DAxis *Q3DBarsWidgetItem::valueAxis() const
extern "C" Q_DECL_EXPORT
QValue3DAxis *ritual_ZNK17Q3DBarsWidgetItem9valueAxisEv(
    const Q3DBarsWidgetItem *self) {
  return self->valueAxis();
}

//  void Q3DBarsWidgetItem::addAxis(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItem7addAxisEP15QAbstract3DAxis(
    Q3DBarsWidgetItem *self,
    QAbstract3DAxis *axis) {
  self->addAxis(axis);
}

//  void Q3DBarsWidgetItem::releaseAxis(QAbstract3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItem11releaseAxisEP15QAbstract3DAxis(
    Q3DBarsWidgetItem *self,
    QAbstract3DAxis *axis) {
  self->releaseAxis(axis);
}

//  QList<QAbstract3DAxis *> Q3DBarsWidgetItem::axes() const
extern "C" Q_DECL_EXPORT
QList<QAbstract3DAxis *> *ritual_ZNK17Q3DBarsWidgetItem4axesEv(
    const Q3DBarsWidgetItem *self) {
  return new QList<QAbstract3DAxis *>(self->axes());
}

//  QBar3DSeries *Q3DBarsWidgetItem::selectedSeries() const
extern "C" Q_DECL_EXPORT
QBar3DSeries *ritual_ZNK17Q3DBarsWidgetItem14selectedSeriesEv(
    const Q3DBarsWidgetItem *self) {
  return self->selectedSeries();
}

//  float Q3DBarsWidgetItem::floorLevel() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK17Q3DBarsWidgetItem10floorLevelEv(
    const Q3DBarsWidgetItem *self) {
  return self->floorLevel();
}

//  void Q3DBarsWidgetItem::renderSliceToImage(int requestedIndex,
//      QtGraphs3D::SliceCaptureType sliceType)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItem18renderSliceToImageEiN10QtGraphs3D16SliceCaptureTypeE(
    Q3DBarsWidgetItem *self,
    int requestedIndex,
    QtGraphs3D::SliceCaptureType sliceType) {
  self->renderSliceToImage(requestedIndex, sliceType);
}

//  void Q3DBarsWidgetItem::setPrimarySeries(QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItem16setPrimarySeriesEP12QBar3DSeries(
    Q3DBarsWidgetItem *self,
    QBar3DSeries *series) {
  self->setPrimarySeries(series);
}

//  void Q3DBarsWidgetItem::setMultiSeriesUniform(bool uniform)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItem21setMultiSeriesUniformEb(
    Q3DBarsWidgetItem *self,
    bool uniform) {
  self->setMultiSeriesUniform(uniform);
}

//  void Q3DBarsWidgetItem::setBarThickness(float thicknessRatio)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItem15setBarThicknessEf(
    Q3DBarsWidgetItem *self,
    float thicknessRatio) {
  self->setBarThickness(thicknessRatio);
}

//  void Q3DBarsWidgetItem::setBarSpacing(QSizeF spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItem13setBarSpacingE6QSizeF(
    Q3DBarsWidgetItem *self,
    const QSizeF *spacing) {
  self->setBarSpacing(*spacing);
}

//  void Q3DBarsWidgetItem::setBarSpacingRelative(bool relative)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItem21setBarSpacingRelativeEb(
    Q3DBarsWidgetItem *self,
    bool relative) {
  self->setBarSpacingRelative(relative);
}

//  void Q3DBarsWidgetItem::setBarSeriesMargin(QSizeF margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItem18setBarSeriesMarginE6QSizeF(
    Q3DBarsWidgetItem *self,
    const QSizeF *margin) {
  self->setBarSeriesMargin(*margin);
}

//  void Q3DBarsWidgetItem::setRowAxis(QCategory3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItem10setRowAxisEP15QCategory3DAxis(
    Q3DBarsWidgetItem *self,
    QCategory3DAxis *axis) {
  self->setRowAxis(axis);
}

//  void Q3DBarsWidgetItem::setColumnAxis(QCategory3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItem13setColumnAxisEP15QCategory3DAxis(
    Q3DBarsWidgetItem *self,
    QCategory3DAxis *axis) {
  self->setColumnAxis(axis);
}

//  void Q3DBarsWidgetItem::setValueAxis(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItem12setValueAxisEP12QValue3DAxis(
    Q3DBarsWidgetItem *self,
    QValue3DAxis *axis) {
  self->setValueAxis(axis);
}

//  void Q3DBarsWidgetItem::setFloorLevel(float level)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItem13setFloorLevelEf(
    Q3DBarsWidgetItem *self,
    float level) {
  self->setFloorLevel(level);
}

//  bool Q3DBarsWidgetItem::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17Q3DBarsWidgetItem5eventEP6QEvent(
    Q3DBarsWidgetItem *self,
    QEvent *event) {
  return self->event(event);
}

//  void Q3DBarsWidgetItem::multiSeriesUniformChanged(bool uniform)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItem25multiSeriesUniformChangedEb(
    Q3DBarsWidgetItem *self,
    bool uniform) {
  self->multiSeriesUniformChanged(uniform);
}

//  void Q3DBarsWidgetItem::barThicknessChanged(float thicknessRatio)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItem19barThicknessChangedEf(
    Q3DBarsWidgetItem *self,
    float thicknessRatio) {
  self->barThicknessChanged(thicknessRatio);
}

//  void Q3DBarsWidgetItem::barSpacingChanged(QSizeF spacing)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItem17barSpacingChangedE6QSizeF(
    Q3DBarsWidgetItem *self,
    const QSizeF *spacing) {
  self->barSpacingChanged(*spacing);
}

//  void Q3DBarsWidgetItem::barSpacingRelativeChanged(bool relative)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItem25barSpacingRelativeChangedEb(
    Q3DBarsWidgetItem *self,
    bool relative) {
  self->barSpacingRelativeChanged(relative);
}

//  void Q3DBarsWidgetItem::barSeriesMarginChanged(QSizeF margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItem22barSeriesMarginChangedE6QSizeF(
    Q3DBarsWidgetItem *self,
    const QSizeF *margin) {
  self->barSeriesMarginChanged(*margin);
}

//  void Q3DBarsWidgetItem::rowAxisChanged(QCategory3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItem14rowAxisChangedEP15QCategory3DAxis(
    Q3DBarsWidgetItem *self,
    QCategory3DAxis *axis) {
  self->rowAxisChanged(axis);
}

//  void Q3DBarsWidgetItem::columnAxisChanged(QCategory3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItem17columnAxisChangedEP15QCategory3DAxis(
    Q3DBarsWidgetItem *self,
    QCategory3DAxis *axis) {
  self->columnAxisChanged(axis);
}

//  void Q3DBarsWidgetItem::valueAxisChanged(QValue3DAxis *axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItem16valueAxisChangedEP12QValue3DAxis(
    Q3DBarsWidgetItem *self,
    QValue3DAxis *axis) {
  self->valueAxisChanged(axis);
}

//  void Q3DBarsWidgetItem::primarySeriesChanged(QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItem20primarySeriesChangedEP12QBar3DSeries(
    Q3DBarsWidgetItem *self,
    QBar3DSeries *series) {
  self->primarySeriesChanged(series);
}

//  void Q3DBarsWidgetItem::selectedSeriesChanged(QBar3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItem21selectedSeriesChangedEP12QBar3DSeries(
    Q3DBarsWidgetItem *self,
    QBar3DSeries *series) {
  self->selectedSeriesChanged(series);
}

//  void Q3DBarsWidgetItem::floorLevelChanged(float level)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItem17floorLevelChangedEf(
    Q3DBarsWidgetItem *self,
    float level) {
  self->floorLevelChanged(level);
}

//  void Q3DBarsWidgetItem::sliceImageChanged(const QImage &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN17Q3DBarsWidgetItem17sliceImageChangedERK6QImage(
    Q3DBarsWidgetItem *self,
    const QImage *image) {
  self->sliceImageChanged(*image);
}

//  Q3DBarsWidgetItemPrivate *Q3DBarsWidgetItem::d_func()
extern "C" Q_DECL_EXPORT
Q3DBarsWidgetItemPrivate *ritual_ZN17Q3DBarsWidgetItem6d_funcEv(
    Q3DBarsWidgetItem *self) {
  return self->d_func();
}

//  const Q3DBarsWidgetItemPrivate *Q3DBarsWidgetItem::d_func() const
extern "C" Q_DECL_EXPORT
const Q3DBarsWidgetItemPrivate *ritual_ZNK17Q3DBarsWidgetItem6d_funcEv(
    const Q3DBarsWidgetItem *self) {
  return self->d_func();
}

//  QQuickGraphsBars *Q3DBarsWidgetItem::graphBars()
extern "C" Q_DECL_EXPORT
QQuickGraphsBars *ritual_ZN17Q3DBarsWidgetItem9graphBarsEv(
    Q3DBarsWidgetItem *self) {
  return self->graphBars();
}

//  const QQuickGraphsBars *Q3DBarsWidgetItem::graphBars() const
extern "C" Q_DECL_EXPORT
const QQuickGraphsBars *ritual_ZNK17Q3DBarsWidgetItem9graphBarsEv(
    const Q3DBarsWidgetItem *self) {
  return self->graphBars();
}

//  a Python function taken by a CuteQ3DBarsWidgetItem, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Q3DBarsWidgetItem(
    Q3DBarsWidgetItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQ3DBarsWidgetItem *>(self)->take(key, call);
}

//  bool Q3DBarsWidgetItem::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17Q3DBarsWidgetItem5eventEP6QEvent(
    Q3DBarsWidgetItem *self,
    QEvent *event) {
  return static_cast<OwnQ3DBarsWidgetItem *>(self)->OwnQ3DBarsWidgetItem::event(
      event);
}

#endif  // QT_CONFIG(graphs_3d_bars3d)
