//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphsWidgets/q3dgraphswidgetitem.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGraphsWidgets/q3dgraphswidgetitem.h>
#include <QtCore/qstring.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qgraphstheme.h>
#include <QtCore/qlocale.h>
#include <QtGui/qvectornd.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d)))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qcustom3ditem.h>
#endif
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtGui/qcolor.h>
#include <QtGui/qeventpoint.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QSharedPointer>
#include <QtQuick/QQuickItemGrabResult>
#include <QtCore/QSize>

//  Only a class built on Q3DGraphsWidgetItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQ3DGraphsWidgetItem : Q3DGraphsWidgetItem {
  using Q3DGraphsWidgetItem::event;
  using Q3DGraphsWidgetItem::eventFilter;
};

//  A Q3DGraphsWidgetItem that Python can take functions over in. Every Q3DGraphsWidgetItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DGraphsWidgetItemCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DGraphsWidgetItemCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DGraphsWidgetItemCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DGraphsWidgetItemCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DGraphsWidgetItemCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DGraphsWidgetItemCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DGraphsWidgetItemCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQ3DGraphsWidgetItem : public Q3DGraphsWidgetItem {
public:
  using Q3DGraphsWidgetItem::Q3DGraphsWidgetItem;
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
  //  bool Q3DGraphsWidgetItem::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQ3DGraphsWidgetItemCall0 call = reinterpret_cast<CuteQ3DGraphsWidgetItemCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return Q3DGraphsWidgetItem::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool Q3DGraphsWidgetItem::eventFilter(QObject *obj, QEvent *event)
  bool eventFilter(QObject *obj, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQ3DGraphsWidgetItemCall1 call = reinterpret_cast<CuteQ3DGraphsWidgetItemCall1>(taken[1]);
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
      CuteQ3DGraphsWidgetItemCall2 call = reinterpret_cast<CuteQ3DGraphsWidgetItemCall2>(taken[2]);
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
      CuteQ3DGraphsWidgetItemCall3 call = reinterpret_cast<CuteQ3DGraphsWidgetItemCall3>(taken[3]);
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
      CuteQ3DGraphsWidgetItemCall4 call = reinterpret_cast<CuteQ3DGraphsWidgetItemCall4>(taken[4]);
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
      CuteQ3DGraphsWidgetItemCall5 call = reinterpret_cast<CuteQ3DGraphsWidgetItemCall5>(taken[5]);
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
      CuteQ3DGraphsWidgetItemCall6 call = reinterpret_cast<CuteQ3DGraphsWidgetItemCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Q3DGraphsWidgetItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19Q3DGraphsWidgetItem10metaObjectEv(
    const Q3DGraphsWidgetItem *self) {
  return self->metaObject();
}

//  void *Q3DGraphsWidgetItem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19Q3DGraphsWidgetItem11qt_metacastEPKc(
    Q3DGraphsWidgetItem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Q3DGraphsWidgetItem::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19Q3DGraphsWidgetItem11qt_metacallEN11QMetaObject4CallEiPPv(
    Q3DGraphsWidgetItem *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Q3DGraphsWidgetItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19Q3DGraphsWidgetItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Q3DGraphsWidgetItem::tr(s, c, n));
}

//  void Q3DGraphsWidgetItem::addTheme(QGraphsTheme *theme)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem8addThemeEP12QGraphsTheme(
    Q3DGraphsWidgetItem *self,
    QGraphsTheme *theme) {
  self->addTheme(theme);
}

//  void Q3DGraphsWidgetItem::releaseTheme(QGraphsTheme *theme)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem12releaseThemeEP12QGraphsTheme(
    Q3DGraphsWidgetItem *self,
    QGraphsTheme *theme) {
  self->releaseTheme(theme);
}

//  QGraphsTheme *Q3DGraphsWidgetItem::activeTheme() const
extern "C" Q_DECL_EXPORT
QGraphsTheme *ritual_ZNK19Q3DGraphsWidgetItem11activeThemeEv(
    const Q3DGraphsWidgetItem *self) {
  return self->activeTheme();
}

//  QList<QGraphsTheme *> Q3DGraphsWidgetItem::themes() const
extern "C" Q_DECL_EXPORT
QList<QGraphsTheme *> *ritual_ZNK19Q3DGraphsWidgetItem6themesEv(
    const Q3DGraphsWidgetItem *self) {
  return new QList<QGraphsTheme *>(self->themes());
}

//  QtGraphs3D::TransparencyTechnique
//      Q3DGraphsWidgetItem::transparencyTechnique() const
extern "C" Q_DECL_EXPORT
QtGraphs3D::TransparencyTechnique ritual_ZNK19Q3DGraphsWidgetItem21transparencyTechniqueEv(
    const Q3DGraphsWidgetItem *self) {
  return self->transparencyTechnique();
}

//  QtGraphs3D::ShadowQuality Q3DGraphsWidgetItem::shadowQuality() const
extern "C" Q_DECL_EXPORT
QtGraphs3D::ShadowQuality ritual_ZNK19Q3DGraphsWidgetItem13shadowQualityEv(
    const Q3DGraphsWidgetItem *self) {
  return self->shadowQuality();
}

//  QtGraphs3D::SelectionFlags Q3DGraphsWidgetItem::selectionMode() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19Q3DGraphsWidgetItem13selectionModeEv(
    const Q3DGraphsWidgetItem *self) {
  return static_cast<int>(self->selectionMode().toInt());
}

//  Q3DScene *Q3DGraphsWidgetItem::scene() const
extern "C" Q_DECL_EXPORT
Q3DScene *ritual_ZNK19Q3DGraphsWidgetItem5sceneEv(
    const Q3DGraphsWidgetItem *self) {
  return self->scene();
}

//  bool Q3DGraphsWidgetItem::measureFps() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19Q3DGraphsWidgetItem10measureFpsEv(
    const Q3DGraphsWidgetItem *self) {
  return self->measureFps();
}

//  int Q3DGraphsWidgetItem::currentFps() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19Q3DGraphsWidgetItem10currentFpsEv(
    const Q3DGraphsWidgetItem *self) {
  return self->currentFps();
}

//  bool Q3DGraphsWidgetItem::isOrthoProjection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19Q3DGraphsWidgetItem17isOrthoProjectionEv(
    const Q3DGraphsWidgetItem *self) {
  return self->isOrthoProjection();
}

//  QtGraphs3D::ElementType Q3DGraphsWidgetItem::selectedElement() const
extern "C" Q_DECL_EXPORT
QtGraphs3D::ElementType ritual_ZNK19Q3DGraphsWidgetItem15selectedElementEv(
    const Q3DGraphsWidgetItem *self) {
  return self->selectedElement();
}

//  qreal Q3DGraphsWidgetItem::aspectRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19Q3DGraphsWidgetItem11aspectRatioEv(
    const Q3DGraphsWidgetItem *self) {
  return self->aspectRatio();
}

//  QtGraphs3D::OptimizationHint Q3DGraphsWidgetItem::optimizationHint()
//      const
extern "C" Q_DECL_EXPORT
QtGraphs3D::OptimizationHint ritual_ZNK19Q3DGraphsWidgetItem16optimizationHintEv(
    const Q3DGraphsWidgetItem *self) {
  return self->optimizationHint();
}

//  bool Q3DGraphsWidgetItem::isPolar() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19Q3DGraphsWidgetItem7isPolarEv(
    const Q3DGraphsWidgetItem *self) {
  return self->isPolar();
}

//  float Q3DGraphsWidgetItem::labelMargin() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19Q3DGraphsWidgetItem11labelMarginEv(
    const Q3DGraphsWidgetItem *self) {
  return self->labelMargin();
}

//  float Q3DGraphsWidgetItem::radialLabelOffset() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19Q3DGraphsWidgetItem17radialLabelOffsetEv(
    const Q3DGraphsWidgetItem *self) {
  return self->radialLabelOffset();
}

//  qreal Q3DGraphsWidgetItem::horizontalAspectRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19Q3DGraphsWidgetItem21horizontalAspectRatioEv(
    const Q3DGraphsWidgetItem *self) {
  return self->horizontalAspectRatio();
}

//  QLocale Q3DGraphsWidgetItem::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK19Q3DGraphsWidgetItem6localeEv(
    const Q3DGraphsWidgetItem *self) {
  return new QLocale(self->locale());
}

//  QVector3D Q3DGraphsWidgetItem::queriedGraphPosition() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK19Q3DGraphsWidgetItem20queriedGraphPositionEv(
    const Q3DGraphsWidgetItem *self) {
  return new QVector3D(self->queriedGraphPosition());
}

//  qreal Q3DGraphsWidgetItem::margin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19Q3DGraphsWidgetItem6marginEv(
    const Q3DGraphsWidgetItem *self) {
  return self->margin();
}

//  qreal Q3DGraphsWidgetItem::cutoffMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19Q3DGraphsWidgetItem12cutoffMarginEv(
    const Q3DGraphsWidgetItem *self) {
  return self->cutoffMargin();
}

//  void Q3DGraphsWidgetItem::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem14clearSelectionEv(
    Q3DGraphsWidgetItem *self) {
  self->clearSelection();
}

//  bool Q3DGraphsWidgetItem::hasSeries(QAbstract3DSeries *series) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19Q3DGraphsWidgetItem9hasSeriesEP17QAbstract3DSeries(
    const Q3DGraphsWidgetItem *self,
    QAbstract3DSeries *series) {
  return self->hasSeries(series);
}

//  qsizetype Q3DGraphsWidgetItem::addCustomItem(QCustom3DItem *item)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN19Q3DGraphsWidgetItem13addCustomItemEP13QCustom3DItem(
    Q3DGraphsWidgetItem *self,
    QCustom3DItem *item) {
  return self->addCustomItem(item);
}

//  void Q3DGraphsWidgetItem::removeCustomItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem17removeCustomItemsEv(
    Q3DGraphsWidgetItem *self) {
  self->removeCustomItems();
}

//  void Q3DGraphsWidgetItem::removeCustomItem(QCustom3DItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem16removeCustomItemEP13QCustom3DItem(
    Q3DGraphsWidgetItem *self,
    QCustom3DItem *item) {
  self->removeCustomItem(item);
}

//  void Q3DGraphsWidgetItem::removeCustomItemAt(QVector3D position)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem18removeCustomItemAtE9QVector3D(
    Q3DGraphsWidgetItem *self,
    const QVector3D *position) {
  self->removeCustomItemAt(*position);
}

//  void Q3DGraphsWidgetItem::releaseCustomItem(QCustom3DItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem17releaseCustomItemEP13QCustom3DItem(
    Q3DGraphsWidgetItem *self,
    QCustom3DItem *item) {
  self->releaseCustomItem(item);
}

//  QList<QCustom3DItem *> Q3DGraphsWidgetItem::customItems() const
extern "C" Q_DECL_EXPORT
QList<QCustom3DItem *> *ritual_ZNK19Q3DGraphsWidgetItem11customItemsEv(
    const Q3DGraphsWidgetItem *self) {
  return new QList<QCustom3DItem *>(self->customItems());
}

//  int Q3DGraphsWidgetItem::selectedLabelIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19Q3DGraphsWidgetItem18selectedLabelIndexEv(
    const Q3DGraphsWidgetItem *self) {
  return self->selectedLabelIndex();
}

//  QAbstract3DAxis *Q3DGraphsWidgetItem::selectedAxis() const
extern "C" Q_DECL_EXPORT
QAbstract3DAxis *ritual_ZNK19Q3DGraphsWidgetItem12selectedAxisEv(
    const Q3DGraphsWidgetItem *self) {
  return self->selectedAxis();
}

//  qsizetype Q3DGraphsWidgetItem::selectedCustomItemIndex() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK19Q3DGraphsWidgetItem23selectedCustomItemIndexEv(
    const Q3DGraphsWidgetItem *self) {
  return self->selectedCustomItemIndex();
}

//  QCustom3DItem *Q3DGraphsWidgetItem::selectedCustomItem() const
extern "C" Q_DECL_EXPORT
QCustom3DItem *ritual_ZNK19Q3DGraphsWidgetItem18selectedCustomItemEv(
    const Q3DGraphsWidgetItem *self) {
  return self->selectedCustomItem();
}

//  QSharedPointer<QQuickItemGrabResult>
//      Q3DGraphsWidgetItem::renderToImage(QSize imageSize) const
extern "C" Q_DECL_EXPORT
QSharedPointer<QQuickItemGrabResult> *ritual_ZNK19Q3DGraphsWidgetItem13renderToImageE5QSize(
    const Q3DGraphsWidgetItem *self,
    const QSize *imageSize) {
  return new QSharedPointer<QQuickItemGrabResult>(
      self->renderToImage(
          *imageSize));
}

//  QtGraphs3D::CameraPreset Q3DGraphsWidgetItem::cameraPreset() const
extern "C" Q_DECL_EXPORT
QtGraphs3D::CameraPreset ritual_ZNK19Q3DGraphsWidgetItem12cameraPresetEv(
    const Q3DGraphsWidgetItem *self) {
  return self->cameraPreset();
}

//  float Q3DGraphsWidgetItem::cameraXRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19Q3DGraphsWidgetItem15cameraXRotationEv(
    const Q3DGraphsWidgetItem *self) {
  return self->cameraXRotation();
}

//  float Q3DGraphsWidgetItem::cameraYRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19Q3DGraphsWidgetItem15cameraYRotationEv(
    const Q3DGraphsWidgetItem *self) {
  return self->cameraYRotation();
}

//  float Q3DGraphsWidgetItem::minCameraXRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19Q3DGraphsWidgetItem18minCameraXRotationEv(
    const Q3DGraphsWidgetItem *self) {
  return self->minCameraXRotation();
}

//  float Q3DGraphsWidgetItem::maxCameraXRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19Q3DGraphsWidgetItem18maxCameraXRotationEv(
    const Q3DGraphsWidgetItem *self) {
  return self->maxCameraXRotation();
}

//  float Q3DGraphsWidgetItem::minCameraYRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19Q3DGraphsWidgetItem18minCameraYRotationEv(
    const Q3DGraphsWidgetItem *self) {
  return self->minCameraYRotation();
}

//  float Q3DGraphsWidgetItem::maxCameraYRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19Q3DGraphsWidgetItem18maxCameraYRotationEv(
    const Q3DGraphsWidgetItem *self) {
  return self->maxCameraYRotation();
}

//  bool Q3DGraphsWidgetItem::isZoomAtTargetEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19Q3DGraphsWidgetItem21isZoomAtTargetEnabledEv(
    const Q3DGraphsWidgetItem *self) {
  return self->isZoomAtTargetEnabled();
}

//  bool Q3DGraphsWidgetItem::isZoomEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19Q3DGraphsWidgetItem13isZoomEnabledEv(
    const Q3DGraphsWidgetItem *self) {
  return self->isZoomEnabled();
}

//  bool Q3DGraphsWidgetItem::isSelectionEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19Q3DGraphsWidgetItem18isSelectionEnabledEv(
    const Q3DGraphsWidgetItem *self) {
  return self->isSelectionEnabled();
}

//  bool Q3DGraphsWidgetItem::isRotationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19Q3DGraphsWidgetItem17isRotationEnabledEv(
    const Q3DGraphsWidgetItem *self) {
  return self->isRotationEnabled();
}

//  bool Q3DGraphsWidgetItem::isPanEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19Q3DGraphsWidgetItem12isPanEnabledEv(
    const Q3DGraphsWidgetItem *self) {
  return self->isPanEnabled();
}

//  QtGraphs3D::DragMode Q3DGraphsWidgetItem::dragMode() const
extern "C" Q_DECL_EXPORT
QtGraphs3D::DragMode ritual_ZNK19Q3DGraphsWidgetItem8dragModeEv(
    const Q3DGraphsWidgetItem *self) {
  return self->dragMode();
}

//  float Q3DGraphsWidgetItem::cameraZoomLevel() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19Q3DGraphsWidgetItem15cameraZoomLevelEv(
    const Q3DGraphsWidgetItem *self) {
  return self->cameraZoomLevel();
}

//  float Q3DGraphsWidgetItem::minCameraZoomLevel() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19Q3DGraphsWidgetItem18minCameraZoomLevelEv(
    const Q3DGraphsWidgetItem *self) {
  return self->minCameraZoomLevel();
}

//  float Q3DGraphsWidgetItem::maxCameraZoomLevel() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19Q3DGraphsWidgetItem18maxCameraZoomLevelEv(
    const Q3DGraphsWidgetItem *self) {
  return self->maxCameraZoomLevel();
}

//  QVector3D Q3DGraphsWidgetItem::cameraTargetPosition() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK19Q3DGraphsWidgetItem20cameraTargetPositionEv(
    const Q3DGraphsWidgetItem *self) {
  return new QVector3D(self->cameraTargetPosition());
}

//  bool Q3DGraphsWidgetItem::wrapCameraXRotation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19Q3DGraphsWidgetItem19wrapCameraXRotationEv(
    const Q3DGraphsWidgetItem *self) {
  return self->wrapCameraXRotation();
}

//  bool Q3DGraphsWidgetItem::wrapCameraYRotation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19Q3DGraphsWidgetItem19wrapCameraYRotationEv(
    const Q3DGraphsWidgetItem *self) {
  return self->wrapCameraYRotation();
}

//  int Q3DGraphsWidgetItem::msaaSamples() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19Q3DGraphsWidgetItem11msaaSamplesEv(
    const Q3DGraphsWidgetItem *self) {
  return self->msaaSamples();
}

//  void Q3DGraphsWidgetItem::doPicking(QPoint point)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem9doPickingE6QPoint(
    Q3DGraphsWidgetItem *self,
    const QPoint *point) {
  self->doPicking(*point);
}

//  void Q3DGraphsWidgetItem::doRayPicking(QVector3D origin, QVector3D
//      direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem12doRayPickingE9QVector3DS0_(
    Q3DGraphsWidgetItem *self,
    const QVector3D *origin,
    const QVector3D *direction) {
  self->doRayPicking(*origin, *direction);
}

//  float Q3DGraphsWidgetItem::ambientLightStrength() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19Q3DGraphsWidgetItem20ambientLightStrengthEv(
    const Q3DGraphsWidgetItem *self) {
  return self->ambientLightStrength();
}

//  float Q3DGraphsWidgetItem::lightStrength() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19Q3DGraphsWidgetItem13lightStrengthEv(
    const Q3DGraphsWidgetItem *self) {
  return self->lightStrength();
}

//  float Q3DGraphsWidgetItem::shadowStrength() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19Q3DGraphsWidgetItem14shadowStrengthEv(
    const Q3DGraphsWidgetItem *self) {
  return self->shadowStrength();
}

//  QColor Q3DGraphsWidgetItem::lightColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19Q3DGraphsWidgetItem10lightColorEv(
    const Q3DGraphsWidgetItem *self) {
  return new QColor(self->lightColor());
}

//  QtGraphs3D::GridLineType Q3DGraphsWidgetItem::gridLineType() const
extern "C" Q_DECL_EXPORT
QtGraphs3D::GridLineType ritual_ZNK19Q3DGraphsWidgetItem12gridLineTypeEv(
    const Q3DGraphsWidgetItem *self) {
  return self->gridLineType();
}

//  QQuickWidget *Q3DGraphsWidgetItem::widget() const
extern "C" Q_DECL_EXPORT
QQuickWidget *ritual_ZNK19Q3DGraphsWidgetItem6widgetEv(
    const Q3DGraphsWidgetItem *self) {
  return self->widget();
}

//  Q3DGraphsWidgetItem::~Q3DGraphsWidgetItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItemD1Ev(Q3DGraphsWidgetItem *self) {
  delete self;
}

//  void Q3DGraphsWidgetItem::setActiveTheme(QGraphsTheme *activeTheme)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem14setActiveThemeEP12QGraphsTheme(
    Q3DGraphsWidgetItem *self,
    QGraphsTheme *activeTheme) {
  self->setActiveTheme(activeTheme);
}

//  void Q3DGraphsWidgetItem::setTransparencyTechnique(QtGraphs3D::Transparen
//      cyTechnique technique)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem24setTransparencyTechniqueEN10QtGraphs3D21TransparencyTechniqueE(
    Q3DGraphsWidgetItem *self,
    QtGraphs3D::TransparencyTechnique technique) {
  self->setTransparencyTechnique(technique);
}

//  void Q3DGraphsWidgetItem::setShadowQuality(const
//      QtGraphs3D::ShadowQuality &shadowQuality)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem16setShadowQualityERKN10QtGraphs3D13ShadowQualityE(
    Q3DGraphsWidgetItem *self,
    const QtGraphs3D::ShadowQuality *shadowQuality) {
  self->setShadowQuality(*shadowQuality);
}

//  void Q3DGraphsWidgetItem::setSelectionMode(const
//      QtGraphs3D::SelectionFlags &selectionMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem16setSelectionModeERK6QFlagsIN10QtGraphs3D13SelectionFlagEE(
    Q3DGraphsWidgetItem *self,
    const QtGraphs3D::SelectionFlags *selectionMode) {
  self->setSelectionMode(*selectionMode);
}

//  void Q3DGraphsWidgetItem::setMeasureFps(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem13setMeasureFpsEb(
    Q3DGraphsWidgetItem *self,
    bool enable) {
  self->setMeasureFps(enable);
}

//  void Q3DGraphsWidgetItem::setOrthoProjection(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem18setOrthoProjectionEb(
    Q3DGraphsWidgetItem *self,
    bool enable) {
  self->setOrthoProjection(enable);
}

//  void Q3DGraphsWidgetItem::setAspectRatio(qreal ratio)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem14setAspectRatioEd(
    Q3DGraphsWidgetItem *self,
    qreal ratio) {
  self->setAspectRatio(ratio);
}

//  void
//      Q3DGraphsWidgetItem::setOptimizationHint(QtGraphs3D::OptimizationHint
//      hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem19setOptimizationHintEN10QtGraphs3D16OptimizationHintE(
    Q3DGraphsWidgetItem *self,
    QtGraphs3D::OptimizationHint hint) {
  self->setOptimizationHint(hint);
}

//  void Q3DGraphsWidgetItem::setPolar(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem8setPolarEb(
    Q3DGraphsWidgetItem *self,
    bool enable) {
  self->setPolar(enable);
}

//  void Q3DGraphsWidgetItem::setLabelMargin(float margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem14setLabelMarginEf(
    Q3DGraphsWidgetItem *self,
    float margin) {
  self->setLabelMargin(margin);
}

//  void Q3DGraphsWidgetItem::setRadialLabelOffset(float offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem20setRadialLabelOffsetEf(
    Q3DGraphsWidgetItem *self,
    float offset) {
  self->setRadialLabelOffset(offset);
}

//  void Q3DGraphsWidgetItem::setHorizontalAspectRatio(qreal ratio)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem24setHorizontalAspectRatioEd(
    Q3DGraphsWidgetItem *self,
    qreal ratio) {
  self->setHorizontalAspectRatio(ratio);
}

//  void Q3DGraphsWidgetItem::setLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem9setLocaleERK7QLocale(
    Q3DGraphsWidgetItem *self,
    const QLocale *locale) {
  self->setLocale(*locale);
}

//  void Q3DGraphsWidgetItem::setMargin(qreal margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem9setMarginEd(
    Q3DGraphsWidgetItem *self,
    qreal margin) {
  self->setMargin(margin);
}

//  void Q3DGraphsWidgetItem::setCutoffMargin(qreal margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem15setCutoffMarginEd(
    Q3DGraphsWidgetItem *self,
    qreal margin) {
  self->setCutoffMargin(margin);
}

//  void Q3DGraphsWidgetItem::setCameraPreset(QtGraphs3D::CameraPreset
//      preset)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem15setCameraPresetEN10QtGraphs3D12CameraPresetE(
    Q3DGraphsWidgetItem *self,
    QtGraphs3D::CameraPreset preset) {
  self->setCameraPreset(preset);
}

//  void Q3DGraphsWidgetItem::setCameraXRotation(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem18setCameraXRotationEf(
    Q3DGraphsWidgetItem *self,
    float rotation) {
  self->setCameraXRotation(rotation);
}

//  void Q3DGraphsWidgetItem::setCameraYRotation(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem18setCameraYRotationEf(
    Q3DGraphsWidgetItem *self,
    float rotation) {
  self->setCameraYRotation(rotation);
}

//  void Q3DGraphsWidgetItem::setMinCameraXRotation(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem21setMinCameraXRotationEf(
    Q3DGraphsWidgetItem *self,
    float rotation) {
  self->setMinCameraXRotation(rotation);
}

//  void Q3DGraphsWidgetItem::setMaxCameraXRotation(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem21setMaxCameraXRotationEf(
    Q3DGraphsWidgetItem *self,
    float rotation) {
  self->setMaxCameraXRotation(rotation);
}

//  void Q3DGraphsWidgetItem::setMinCameraYRotation(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem21setMinCameraYRotationEf(
    Q3DGraphsWidgetItem *self,
    float rotation) {
  self->setMinCameraYRotation(rotation);
}

//  void Q3DGraphsWidgetItem::setMaxCameraYRotation(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem21setMaxCameraYRotationEf(
    Q3DGraphsWidgetItem *self,
    float rotation) {
  self->setMaxCameraYRotation(rotation);
}

//  void Q3DGraphsWidgetItem::setZoomAtTargetEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem22setZoomAtTargetEnabledEb(
    Q3DGraphsWidgetItem *self,
    bool enable) {
  self->setZoomAtTargetEnabled(enable);
}

//  void Q3DGraphsWidgetItem::setZoomEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem14setZoomEnabledEb(
    Q3DGraphsWidgetItem *self,
    bool enable) {
  self->setZoomEnabled(enable);
}

//  void Q3DGraphsWidgetItem::setSelectionEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem19setSelectionEnabledEb(
    Q3DGraphsWidgetItem *self,
    bool enable) {
  self->setSelectionEnabled(enable);
}

//  void Q3DGraphsWidgetItem::setRotationEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem18setRotationEnabledEb(
    Q3DGraphsWidgetItem *self,
    bool enable) {
  self->setRotationEnabled(enable);
}

//  void Q3DGraphsWidgetItem::setPanEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem13setPanEnabledEb(
    Q3DGraphsWidgetItem *self,
    bool enable) {
  self->setPanEnabled(enable);
}

//  void Q3DGraphsWidgetItem::setDragMode(QtGraphs3D::DragMode newDragMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem11setDragModeEN10QtGraphs3D8DragModeE(
    Q3DGraphsWidgetItem *self,
    QtGraphs3D::DragMode newDragMode) {
  self->setDragMode(newDragMode);
}

//  void Q3DGraphsWidgetItem::setDefaultInputHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem22setDefaultInputHandlerEv(
    Q3DGraphsWidgetItem *self) {
  self->setDefaultInputHandler();
}

//  void Q3DGraphsWidgetItem::unsetDefaultInputHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem24unsetDefaultInputHandlerEv(
    Q3DGraphsWidgetItem *self) {
  self->unsetDefaultInputHandler();
}

//  void Q3DGraphsWidgetItem::unsetDefaultTapHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem22unsetDefaultTapHandlerEv(
    Q3DGraphsWidgetItem *self) {
  self->unsetDefaultTapHandler();
}

//  void Q3DGraphsWidgetItem::unsetDefaultDragHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem23unsetDefaultDragHandlerEv(
    Q3DGraphsWidgetItem *self) {
  self->unsetDefaultDragHandler();
}

//  void Q3DGraphsWidgetItem::unsetDefaultWheelHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem24unsetDefaultWheelHandlerEv(
    Q3DGraphsWidgetItem *self) {
  self->unsetDefaultWheelHandler();
}

//  void Q3DGraphsWidgetItem::unsetDefaultPinchHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem24unsetDefaultPinchHandlerEv(
    Q3DGraphsWidgetItem *self) {
  self->unsetDefaultPinchHandler();
}

//  void Q3DGraphsWidgetItem::setDragButton(Qt::MouseButtons button)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem13setDragButtonE6QFlagsIN2Qt11MouseButtonEE(
    Q3DGraphsWidgetItem *self,
    int button) {
  self->setDragButton(QFlags<Qt::MouseButton>::fromInt(button));
}

//  void Q3DGraphsWidgetItem::setPanButton(Qt::MouseButtons button)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem12setPanButtonE6QFlagsIN2Qt11MouseButtonEE(
    Q3DGraphsWidgetItem *self,
    int button) {
  self->setPanButton(QFlags<Qt::MouseButton>::fromInt(button));
}

//  void Q3DGraphsWidgetItem::setCameraZoomLevel(float level)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem18setCameraZoomLevelEf(
    Q3DGraphsWidgetItem *self,
    float level) {
  self->setCameraZoomLevel(level);
}

//  void Q3DGraphsWidgetItem::setMinCameraZoomLevel(float level)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem21setMinCameraZoomLevelEf(
    Q3DGraphsWidgetItem *self,
    float level) {
  self->setMinCameraZoomLevel(level);
}

//  void Q3DGraphsWidgetItem::setMaxCameraZoomLevel(float level)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem21setMaxCameraZoomLevelEf(
    Q3DGraphsWidgetItem *self,
    float level) {
  self->setMaxCameraZoomLevel(level);
}

//  void Q3DGraphsWidgetItem::setCameraTargetPosition(QVector3D target)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem23setCameraTargetPositionE9QVector3D(
    Q3DGraphsWidgetItem *self,
    const QVector3D *target) {
  self->setCameraTargetPosition(*target);
}

//  void Q3DGraphsWidgetItem::setWrapCameraXRotation(bool wrap)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem22setWrapCameraXRotationEb(
    Q3DGraphsWidgetItem *self,
    bool wrap) {
  self->setWrapCameraXRotation(wrap);
}

//  void Q3DGraphsWidgetItem::setWrapCameraYRotation(bool wrap)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem22setWrapCameraYRotationEb(
    Q3DGraphsWidgetItem *self,
    bool wrap) {
  self->setWrapCameraYRotation(wrap);
}

//  void Q3DGraphsWidgetItem::setCameraPosition(float horizontal, float
//      vertical, float zoom)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem17setCameraPositionEfff(
    Q3DGraphsWidgetItem *self,
    float horizontal,
    float vertical,
    float zoom) {
  self->setCameraPosition(horizontal, vertical, zoom);
}

//  void Q3DGraphsWidgetItem::setMsaaSamples(int samples)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem14setMsaaSamplesEi(
    Q3DGraphsWidgetItem *self,
    int samples) {
  self->setMsaaSamples(samples);
}

//  void Q3DGraphsWidgetItem::setAmbientLightStrength(float
//      newAmbientLightStrength)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem23setAmbientLightStrengthEf(
    Q3DGraphsWidgetItem *self,
    float newAmbientLightStrength) {
  self->setAmbientLightStrength(newAmbientLightStrength);
}

//  void Q3DGraphsWidgetItem::setLightStrength(float newLightStrength)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem16setLightStrengthEf(
    Q3DGraphsWidgetItem *self,
    float newLightStrength) {
  self->setLightStrength(newLightStrength);
}

//  void Q3DGraphsWidgetItem::setShadowStrength(float newShadowStrength)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem17setShadowStrengthEf(
    Q3DGraphsWidgetItem *self,
    float newShadowStrength) {
  self->setShadowStrength(newShadowStrength);
}

//  void Q3DGraphsWidgetItem::setLightColor(QColor newLightColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem13setLightColorE6QColor(
    Q3DGraphsWidgetItem *self,
    const QColor *newLightColor) {
  self->setLightColor(*newLightColor);
}

//  void Q3DGraphsWidgetItem::setGridLineType(const QtGraphs3D::GridLineType
//      &gridLineType)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem15setGridLineTypeERKN10QtGraphs3D12GridLineTypeE(
    Q3DGraphsWidgetItem *self,
    const QtGraphs3D::GridLineType *gridLineType) {
  self->setGridLineType(*gridLineType);
}

//  void Q3DGraphsWidgetItem::setWidget(QQuickWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem9setWidgetEP12QQuickWidget(
    Q3DGraphsWidgetItem *self,
    QQuickWidget *widget) {
  self->setWidget(widget);
}

//  Q3DGraphsWidgetItem::Q3DGraphsWidgetItem(Q3DGraphsWidgetItemPrivate &dd,
//      QObject *parent, const QString &graph)
extern "C" Q_DECL_EXPORT
Q3DGraphsWidgetItem *ritual_ZN19Q3DGraphsWidgetItemC1ER26Q3DGraphsWidgetItemPrivateP7QObjectRK7QString(
    Q3DGraphsWidgetItemPrivate *dd,
    QObject *parent,
    const QString *graph) {
  return new CuteQ3DGraphsWidgetItem(*dd, parent, *graph);
}

//  bool Q3DGraphsWidgetItem::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19Q3DGraphsWidgetItem5eventEP6QEvent(
    Q3DGraphsWidgetItem *self,
    QEvent *event) {
  return self->event(event);
}

//  bool Q3DGraphsWidgetItem::eventFilter(QObject *obj, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19Q3DGraphsWidgetItem11eventFilterEP7QObjectP6QEvent(
    Q3DGraphsWidgetItem *self,
    QObject *obj,
    QEvent *event) {
  return self->eventFilter(obj, event);
}

//  void Q3DGraphsWidgetItem::activeThemeChanged(QGraphsTheme *activeTheme)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem18activeThemeChangedEP12QGraphsTheme(
    Q3DGraphsWidgetItem *self,
    QGraphsTheme *activeTheme) {
  self->activeThemeChanged(activeTheme);
}

//  void Q3DGraphsWidgetItem::shadowQualityChanged(QtGraphs3D::ShadowQuality
//      quality)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem20shadowQualityChangedEN10QtGraphs3D13ShadowQualityE(
    Q3DGraphsWidgetItem *self,
    QtGraphs3D::ShadowQuality quality) {
  self->shadowQualityChanged(quality);
}

//  void Q3DGraphsWidgetItem::transparencyTechniqueChanged(QtGraphs3D::Transp
//      arencyTechnique technique)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem28transparencyTechniqueChangedEN10QtGraphs3D21TransparencyTechniqueE(
    Q3DGraphsWidgetItem *self,
    QtGraphs3D::TransparencyTechnique technique) {
  self->transparencyTechniqueChanged(technique);
}

//  void Q3DGraphsWidgetItem::selectionModeChanged(const
//      QtGraphs3D::SelectionFlags selectionMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem20selectionModeChangedE6QFlagsIN10QtGraphs3D13SelectionFlagEE(
    Q3DGraphsWidgetItem *self,
    int selectionMode) {
  self->selectionModeChanged(
      QFlags<QtGraphs3D::SelectionFlag>::fromInt(selectionMode));
}

//  void Q3DGraphsWidgetItem::selectedElementChanged(QtGraphs3D::ElementType
//      type)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem22selectedElementChangedEN10QtGraphs3D11ElementTypeE(
    Q3DGraphsWidgetItem *self,
    QtGraphs3D::ElementType type) {
  self->selectedElementChanged(type);
}

//  void Q3DGraphsWidgetItem::measureFpsChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem17measureFpsChangedEb(
    Q3DGraphsWidgetItem *self,
    bool enabled) {
  self->measureFpsChanged(enabled);
}

//  void Q3DGraphsWidgetItem::currentFpsChanged(int fps)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem17currentFpsChangedEi(
    Q3DGraphsWidgetItem *self,
    int fps) {
  self->currentFpsChanged(fps);
}

//  void Q3DGraphsWidgetItem::orthoProjectionChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem22orthoProjectionChangedEb(
    Q3DGraphsWidgetItem *self,
    bool enabled) {
  self->orthoProjectionChanged(enabled);
}

//  void Q3DGraphsWidgetItem::aspectRatioChanged(qreal ratio)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem18aspectRatioChangedEd(
    Q3DGraphsWidgetItem *self,
    qreal ratio) {
  self->aspectRatioChanged(ratio);
}

//  void
//      Q3DGraphsWidgetItem::optimizationHintChanged(QtGraphs3D::Optimization
//      Hint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem23optimizationHintChangedEN10QtGraphs3D16OptimizationHintE(
    Q3DGraphsWidgetItem *self,
    QtGraphs3D::OptimizationHint hint) {
  self->optimizationHintChanged(hint);
}

//  void Q3DGraphsWidgetItem::polarChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem12polarChangedEb(
    Q3DGraphsWidgetItem *self,
    bool enabled) {
  self->polarChanged(enabled);
}

//  void Q3DGraphsWidgetItem::labelMarginChanged(float margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem18labelMarginChangedEf(
    Q3DGraphsWidgetItem *self,
    float margin) {
  self->labelMarginChanged(margin);
}

//  void Q3DGraphsWidgetItem::radialLabelOffsetChanged(float offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem24radialLabelOffsetChangedEf(
    Q3DGraphsWidgetItem *self,
    float offset) {
  self->radialLabelOffsetChanged(offset);
}

//  void Q3DGraphsWidgetItem::horizontalAspectRatioChanged(qreal ratio)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem28horizontalAspectRatioChangedEd(
    Q3DGraphsWidgetItem *self,
    qreal ratio) {
  self->horizontalAspectRatioChanged(ratio);
}

//  void Q3DGraphsWidgetItem::localeChanged(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem13localeChangedERK7QLocale(
    Q3DGraphsWidgetItem *self,
    const QLocale *locale) {
  self->localeChanged(*locale);
}

//  void Q3DGraphsWidgetItem::queriedGraphPositionChanged(QVector3D data)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem27queriedGraphPositionChangedE9QVector3D(
    Q3DGraphsWidgetItem *self,
    const QVector3D *data) {
  self->queriedGraphPositionChanged(*data);
}

//  void Q3DGraphsWidgetItem::marginChanged(qreal margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem13marginChangedEd(
    Q3DGraphsWidgetItem *self,
    qreal margin) {
  self->marginChanged(margin);
}

//  void Q3DGraphsWidgetItem::cutoffMarginChanged(qreal newMargin)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem19cutoffMarginChangedEd(
    Q3DGraphsWidgetItem *self,
    qreal newMargin) {
  self->cutoffMarginChanged(newMargin);
}

//  void Q3DGraphsWidgetItem::cameraPresetChanged(QtGraphs3D::CameraPreset
//      preset)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem19cameraPresetChangedEN10QtGraphs3D12CameraPresetE(
    Q3DGraphsWidgetItem *self,
    QtGraphs3D::CameraPreset preset) {
  self->cameraPresetChanged(preset);
}

//  void Q3DGraphsWidgetItem::cameraXRotationChanged(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem22cameraXRotationChangedEf(
    Q3DGraphsWidgetItem *self,
    float rotation) {
  self->cameraXRotationChanged(rotation);
}

//  void Q3DGraphsWidgetItem::cameraYRotationChanged(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem22cameraYRotationChangedEf(
    Q3DGraphsWidgetItem *self,
    float rotation) {
  self->cameraYRotationChanged(rotation);
}

//  void Q3DGraphsWidgetItem::cameraZoomLevelChanged(float zoomLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem22cameraZoomLevelChangedEf(
    Q3DGraphsWidgetItem *self,
    float zoomLevel) {
  self->cameraZoomLevelChanged(zoomLevel);
}

//  void Q3DGraphsWidgetItem::cameraTargetPositionChanged(QVector3D target)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem27cameraTargetPositionChangedE9QVector3D(
    Q3DGraphsWidgetItem *self,
    const QVector3D *target) {
  self->cameraTargetPositionChanged(*target);
}

//  void Q3DGraphsWidgetItem::minCameraZoomLevelChanged(float zoomLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem25minCameraZoomLevelChangedEf(
    Q3DGraphsWidgetItem *self,
    float zoomLevel) {
  self->minCameraZoomLevelChanged(zoomLevel);
}

//  void Q3DGraphsWidgetItem::maxCameraZoomLevelChanged(float zoomLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem25maxCameraZoomLevelChangedEf(
    Q3DGraphsWidgetItem *self,
    float zoomLevel) {
  self->maxCameraZoomLevelChanged(zoomLevel);
}

//  void Q3DGraphsWidgetItem::minCameraXRotationChanged(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem25minCameraXRotationChangedEf(
    Q3DGraphsWidgetItem *self,
    float rotation) {
  self->minCameraXRotationChanged(rotation);
}

//  void Q3DGraphsWidgetItem::minCameraYRotationChanged(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem25minCameraYRotationChangedEf(
    Q3DGraphsWidgetItem *self,
    float rotation) {
  self->minCameraYRotationChanged(rotation);
}

//  void Q3DGraphsWidgetItem::maxCameraXRotationChanged(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem25maxCameraXRotationChangedEf(
    Q3DGraphsWidgetItem *self,
    float rotation) {
  self->maxCameraXRotationChanged(rotation);
}

//  void Q3DGraphsWidgetItem::maxCameraYRotationChanged(float rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem25maxCameraYRotationChangedEf(
    Q3DGraphsWidgetItem *self,
    float rotation) {
  self->maxCameraYRotationChanged(rotation);
}

//  void Q3DGraphsWidgetItem::wrapCameraXRotationChanged(bool wrap)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem26wrapCameraXRotationChangedEb(
    Q3DGraphsWidgetItem *self,
    bool wrap) {
  self->wrapCameraXRotationChanged(wrap);
}

//  void Q3DGraphsWidgetItem::wrapCameraYRotationChanged(bool wrap)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem26wrapCameraYRotationChangedEb(
    Q3DGraphsWidgetItem *self,
    bool wrap) {
  self->wrapCameraYRotationChanged(wrap);
}

//  void Q3DGraphsWidgetItem::msaaSamplesChanged(int samples)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem18msaaSamplesChangedEi(
    Q3DGraphsWidgetItem *self,
    int samples) {
  self->msaaSamplesChanged(samples);
}

//  void Q3DGraphsWidgetItem::tapped(QEventPoint eventPoint, Qt::MouseButton
//      button)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem6tappedE11QEventPointN2Qt11MouseButtonE(
    Q3DGraphsWidgetItem *self,
    const QEventPoint *eventPoint,
    Qt::MouseButton button) {
  self->tapped(*eventPoint, button);
}

//  void Q3DGraphsWidgetItem::doubleTapped(QEventPoint eventPoint,
//      Qt::MouseButton button)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem12doubleTappedE11QEventPointN2Qt11MouseButtonE(
    Q3DGraphsWidgetItem *self,
    const QEventPoint *eventPoint,
    Qt::MouseButton button) {
  self->doubleTapped(*eventPoint, button);
}

//  void Q3DGraphsWidgetItem::longPressed()
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem11longPressedEv(
    Q3DGraphsWidgetItem *self) {
  self->longPressed();
}

//  void Q3DGraphsWidgetItem::dragged(QVector2D delta)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem7draggedE9QVector2D(
    Q3DGraphsWidgetItem *self,
    const QVector2D *delta) {
  self->dragged(*delta);
}

//  void Q3DGraphsWidgetItem::wheel(QWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem5wheelEP11QWheelEvent(
    Q3DGraphsWidgetItem *self,
    QWheelEvent *event) {
  self->wheel(event);
}

//  void Q3DGraphsWidgetItem::pinch(qreal delta)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem5pinchEd(
    Q3DGraphsWidgetItem *self,
    qreal delta) {
  self->pinch(delta);
}

//  void Q3DGraphsWidgetItem::mouseMove(QPoint mousePos)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem9mouseMoveE6QPoint(
    Q3DGraphsWidgetItem *self,
    const QPoint *mousePos) {
  self->mouseMove(*mousePos);
}

//  void Q3DGraphsWidgetItem::zoomEnabledChanged(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem18zoomEnabledChangedEb(
    Q3DGraphsWidgetItem *self,
    bool enable) {
  self->zoomEnabledChanged(enable);
}

//  void Q3DGraphsWidgetItem::zoomAtTargetEnabledChanged(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem26zoomAtTargetEnabledChangedEb(
    Q3DGraphsWidgetItem *self,
    bool enable) {
  self->zoomAtTargetEnabledChanged(enable);
}

//  void Q3DGraphsWidgetItem::rotationEnabledChanged(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem22rotationEnabledChangedEb(
    Q3DGraphsWidgetItem *self,
    bool enable) {
  self->rotationEnabledChanged(enable);
}

//  void Q3DGraphsWidgetItem::panEnabledChanged(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem17panEnabledChangedEb(
    Q3DGraphsWidgetItem *self,
    bool enable) {
  self->panEnabledChanged(enable);
}

//  void Q3DGraphsWidgetItem::dragModeChanged(QtGraphs3D::DragMode dragMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem15dragModeChangedEN10QtGraphs3D8DragModeE(
    Q3DGraphsWidgetItem *self,
    QtGraphs3D::DragMode dragMode) {
  self->dragModeChanged(dragMode);
}

//  void Q3DGraphsWidgetItem::selectionEnabledChanged(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem23selectionEnabledChangedEb(
    Q3DGraphsWidgetItem *self,
    bool enable) {
  self->selectionEnabledChanged(enable);
}

//  void Q3DGraphsWidgetItem::ambientLightStrengthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem27ambientLightStrengthChangedEv(
    Q3DGraphsWidgetItem *self) {
  self->ambientLightStrengthChanged();
}

//  void Q3DGraphsWidgetItem::lightStrengthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem20lightStrengthChangedEv(
    Q3DGraphsWidgetItem *self) {
  self->lightStrengthChanged();
}

//  void Q3DGraphsWidgetItem::shadowStrengthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem21shadowStrengthChangedEv(
    Q3DGraphsWidgetItem *self) {
  self->shadowStrengthChanged();
}

//  void Q3DGraphsWidgetItem::lightColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem17lightColorChangedEv(
    Q3DGraphsWidgetItem *self) {
  self->lightColorChanged();
}

//  void Q3DGraphsWidgetItem::gridLineTypeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19Q3DGraphsWidgetItem19gridLineTypeChangedEv(
    Q3DGraphsWidgetItem *self) {
  self->gridLineTypeChanged();
}

//  Q3DGraphsWidgetItemPrivate *Q3DGraphsWidgetItem::d_func()
extern "C" Q_DECL_EXPORT
Q3DGraphsWidgetItemPrivate *ritual_ZN19Q3DGraphsWidgetItem6d_funcEv(
    Q3DGraphsWidgetItem *self) {
  return self->d_func();
}

//  const Q3DGraphsWidgetItemPrivate *Q3DGraphsWidgetItem::d_func() const
extern "C" Q_DECL_EXPORT
const Q3DGraphsWidgetItemPrivate *ritual_ZNK19Q3DGraphsWidgetItem6d_funcEv(
    const Q3DGraphsWidgetItem *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQ3DGraphsWidgetItem, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Q3DGraphsWidgetItem(
    Q3DGraphsWidgetItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQ3DGraphsWidgetItem *>(self)->take(key, call);
}

//  bool Q3DGraphsWidgetItem::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19Q3DGraphsWidgetItem5eventEP6QEvent(
    Q3DGraphsWidgetItem *self,
    QEvent *event) {
  return static_cast<OwnQ3DGraphsWidgetItem *>(self)->OwnQ3DGraphsWidgetItem::event(
      event);
}

//  bool Q3DGraphsWidgetItem::eventFilter(QObject *obj, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19Q3DGraphsWidgetItem11eventFilterEP7QObjectP6QEvent(
    Q3DGraphsWidgetItem *self,
    QObject *obj,
    QEvent *event) {
  return static_cast<OwnQ3DGraphsWidgetItem *>(self)->OwnQ3DGraphsWidgetItem::eventFilter(
      obj,
      event);
}

//  a QSharedPointer<QQuickItemGrabResult> a ritual of Q3DGraphsWidgetItem
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Q3DGraphsWidgetItem__QSharedPointer_QQuickItemGrabResult(
    QSharedPointer<QQuickItemGrabResult> *self) {
  delete self;
}
