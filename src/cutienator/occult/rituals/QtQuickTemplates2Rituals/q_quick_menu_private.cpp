//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmenu_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(qml_object_model)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(qml_object_model)
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmenu_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmenu_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtGui/qeventpoint.h>
#include <QtGui/qpalette.h>
#include <cstring>

//  A QQuickMenuPrivate that Python can take functions over in. Every QQuickMenuPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickMenuPrivateCall0)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickMenuPrivateCall1)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickMenuPrivateCall2)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickMenuPrivateCall3)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickMenuPrivateCall4)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void * (*CuteQQuickMenuPrivateCall5)(const void *, int *);
typedef bool (*CuteQQuickMenuPrivateCall6)(const void *, int *);
typedef bool (*CuteQQuickMenuPrivateCall7)(const void *, int *);
typedef bool (*CuteQQuickMenuPrivateCall8)(const void *, QQuickItem *, const QPointF *, int *);
typedef bool (*CuteQQuickMenuPrivateCall9)(const void *, QQuickItem *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickMenuPrivateCall10)(const void *, const QEventPoint *, int *);
typedef const QPalette * (*CuteQQuickMenuPrivateCall11)(const void *, int *);
typedef int (*CuteQQuickMenuPrivateCall12)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickMenuPrivateCall13)(const void *, const QEventPoint *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickMenuPrivateCall14)(const void *, QQuickItem *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickMenuPrivateCall15)(const void *, QQuickItem *, const QPointF *, ulong, int *);
typedef void (*CuteQQuickMenuPrivateCall16)(const void *, int *);
typedef void (*CuteQQuickMenuPrivateCall17)(const void *, int *);
typedef void (*CuteQQuickMenuPrivateCall18)(const void *, int *);
typedef void (*CuteQQuickMenuPrivateCall19)(const void *, int *);
typedef void (*CuteQQuickMenuPrivateCall20)(const void *, int *);
typedef void (*CuteQQuickMenuPrivateCall21)(const void *, int *);
typedef void (*CuteQQuickMenuPrivateCall22)(const void *, int *);
typedef void (*CuteQQuickMenuPrivateCall23)(const void *, const QPalette *, int *);
class CuteQQuickMenuPrivate : public QQuickMenuPrivate {
public:
  using QQuickMenuPrivate::QQuickMenuPrivate;
  void *taken[24] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QQuickMenuPrivate14itemChildAddedEP10QQuickItemS1_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickMenuPrivate23itemSiblingOrderChangedEP10QQuickItem")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickMenuPrivate17itemParentChangedEP10QQuickItemS1_")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate13itemDestroyedEP10QQuickItem")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickMenuPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate13getPositionerEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate22prepareEnterTransitionEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate21prepareExitTransitionEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QQuickPopupPrivate10blockInputEP10QQuickItemRK7QPointF")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate11handlePressEP10QQuickItemRK7QPointFm")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate24handleReleaseWithoutGrabERK11QEventPoint")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QQuickPopupPrivate14defaultPaletteEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QQuickPopupPrivate17resolvedPopupTypeEv")) {
      taken[12] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate11acceptTouchERK11QEventPoint")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate10handleMoveEP10QQuickItemRK7QPointFm")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate13handleReleaseEP10QQuickItemRK7QPointFm")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate12handleUngrabEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate10showDimmerEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate10hideDimmerEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate12resizeDimmerEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate23finalizeEnterTransitionEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate22finalizeExitTransitionEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate6openedEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate22updateChildrenPalettesERK8QPalette")) {
      taken[23] = call;
      return true;
    }
    return false;
  }

  //  void QQuickMenuPrivate::itemChildAdded(QQuickItem *item, QQuickItem
  //      *child)
  void itemChildAdded(QQuickItem *item, QQuickItem *child) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickMenuPrivateCall0 call = reinterpret_cast<CuteQQuickMenuPrivateCall0>(taken[0]);
      call(this, item, child, &handled);
      if (handled) return;
    }
    QQuickMenuPrivate::itemChildAdded(item, child);
  }

  //  void QQuickMenuPrivate::itemSiblingOrderChanged(QQuickItem *item)
  void itemSiblingOrderChanged(QQuickItem *item) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickMenuPrivateCall1 call = reinterpret_cast<CuteQQuickMenuPrivateCall1>(taken[1]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickMenuPrivate::itemSiblingOrderChanged(item);
  }

  //  void QQuickMenuPrivate::itemParentChanged(QQuickItem *item,
  //      QQuickItem *parent)
  void itemParentChanged(QQuickItem *item, QQuickItem *parent) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickMenuPrivateCall2 call = reinterpret_cast<CuteQQuickMenuPrivateCall2>(taken[2]);
      call(this, item, parent, &handled);
      if (handled) return;
    }
    QQuickMenuPrivate::itemParentChanged(item, parent);
  }

  //  void QQuickMenuPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickMenuPrivateCall3 call = reinterpret_cast<CuteQQuickMenuPrivateCall3>(taken[3]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickMenuPrivate::itemDestroyed(item);
  }

  //  void QQuickMenuPrivate::itemGeometryChanged(QQuickItem *a0,
  //      QQuickGeometryChange change, const QRectF &diff)
  void itemGeometryChanged(
      QQuickItem *a0,
      QQuickGeometryChange change,
      const QRectF &diff) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickMenuPrivateCall4 call = reinterpret_cast<CuteQQuickMenuPrivateCall4>(taken[4]);
      call(this, a0, &change, &diff, &handled);
      if (handled) return;
    }
    QQuickMenuPrivate::itemGeometryChanged(a0, change, diff);
  }

  //  QQuickPopupPositioner *QQuickMenuPrivate::getPositioner()
  QQuickPopupPositioner *getPositioner() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickMenuPrivateCall5 call = reinterpret_cast<CuteQQuickMenuPrivateCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickPopupPositioner *>(given);
    }
    return QQuickMenuPrivate::getPositioner();
  }

  //  bool QQuickMenuPrivate::prepareEnterTransition()
  bool prepareEnterTransition() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickMenuPrivateCall6 call = reinterpret_cast<CuteQQuickMenuPrivateCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickMenuPrivate::prepareEnterTransition();
  }

  //  bool QQuickMenuPrivate::prepareExitTransition()
  bool prepareExitTransition() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickMenuPrivateCall7 call = reinterpret_cast<CuteQQuickMenuPrivateCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickMenuPrivate::prepareExitTransition();
  }

  //  bool QQuickMenuPrivate::blockInput(QQuickItem *item, const QPointF
  //      &point) const
  bool blockInput(QQuickItem *item, const QPointF &point) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickMenuPrivateCall8 call = reinterpret_cast<CuteQQuickMenuPrivateCall8>(taken[8]);
      bool given = call(this, item, &point, &handled);
      if (handled) return given;
    }
    return QQuickMenuPrivate::blockInput(item, point);
  }

  //  bool QQuickMenuPrivate::handlePress(QQuickItem *item, const QPointF
  //      &point, ulong timestamp)
  bool handlePress(
      QQuickItem *item,
      const QPointF &point,
      ulong timestamp) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickMenuPrivateCall9 call = reinterpret_cast<CuteQQuickMenuPrivateCall9>(taken[9]);
      bool given = call(this, item, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickMenuPrivate::handlePress(item, point, timestamp);
  }

  //  bool QQuickMenuPrivate::handleReleaseWithoutGrab(const QEventPoint
  //      &eventPoint)
  bool handleReleaseWithoutGrab(const QEventPoint &eventPoint) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickMenuPrivateCall10 call = reinterpret_cast<CuteQQuickMenuPrivateCall10>(taken[10]);
      bool given = call(this, &eventPoint, &handled);
      if (handled) return given;
    }
    return QQuickMenuPrivate::handleReleaseWithoutGrab(eventPoint);
  }

  //  QPalette QQuickMenuPrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickMenuPrivateCall11 call = reinterpret_cast<CuteQQuickMenuPrivateCall11>(taken[11]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickMenuPrivate::defaultPalette();
  }

  //  QQuickPopup::PopupType QQuickMenuPrivate::resolvedPopupType() const
  QQuickPopup::PopupType resolvedPopupType() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickMenuPrivateCall12 call = reinterpret_cast<CuteQQuickMenuPrivateCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickPopup::PopupType>(given);
    }
    return QQuickMenuPrivate::resolvedPopupType();
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  bool QQuickPopupPrivate::acceptTouch(const QTouchEvent::TouchPoint
  //      &point)
  bool acceptTouch(const QTouchEvent::TouchPoint &point) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickMenuPrivateCall13 call = reinterpret_cast<CuteQQuickMenuPrivateCall13>(taken[13]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::acceptTouch(point);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

  //  bool QQuickPopupPrivate::handleMove(QQuickItem *item, const QPointF
  //      &point, ulong timestamp)
  bool handleMove(
      QQuickItem *item,
      const QPointF &point,
      ulong timestamp) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickMenuPrivateCall14 call = reinterpret_cast<CuteQQuickMenuPrivateCall14>(taken[14]);
      bool given = call(this, item, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::handleMove(item, point, timestamp);
  }

  //  bool QQuickPopupPrivate::handleRelease(QQuickItem *item, const
  //      QPointF &point, ulong timestamp)
  bool handleRelease(
      QQuickItem *item,
      const QPointF &point,
      ulong timestamp) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickMenuPrivateCall15 call = reinterpret_cast<CuteQQuickMenuPrivateCall15>(taken[15]);
      bool given = call(this, item, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::handleRelease(item, point, timestamp);
  }

  //  void QQuickPopupPrivate::handleUngrab()
  void handleUngrab() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickMenuPrivateCall16 call = reinterpret_cast<CuteQQuickMenuPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::handleUngrab();
  }

  //  void QQuickPopupPrivate::showDimmer()
  void showDimmer() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickMenuPrivateCall17 call = reinterpret_cast<CuteQQuickMenuPrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::showDimmer();
  }

  //  void QQuickPopupPrivate::hideDimmer()
  void hideDimmer() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickMenuPrivateCall18 call = reinterpret_cast<CuteQQuickMenuPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::hideDimmer();
  }

  //  void QQuickPopupPrivate::resizeDimmer()
  void resizeDimmer() override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickMenuPrivateCall19 call = reinterpret_cast<CuteQQuickMenuPrivateCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::resizeDimmer();
  }

  //  void QQuickPopupPrivate::finalizeEnterTransition()
  void finalizeEnterTransition() override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickMenuPrivateCall20 call = reinterpret_cast<CuteQQuickMenuPrivateCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::finalizeEnterTransition();
  }

  //  void QQuickPopupPrivate::finalizeExitTransition()
  void finalizeExitTransition() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickMenuPrivateCall21 call = reinterpret_cast<CuteQQuickMenuPrivateCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::finalizeExitTransition();
  }

  //  void QQuickPopupPrivate::opened()
  void opened() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickMenuPrivateCall22 call = reinterpret_cast<CuteQQuickMenuPrivateCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::opened();
  }

  //  void QQuickPopupPrivate::updateChildrenPalettes(const QPalette
  //      &parentPalette)
  void updateChildrenPalettes(const QPalette &parentPalette) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickMenuPrivateCall23 call = reinterpret_cast<CuteQQuickMenuPrivateCall23>(taken[23]);
      call(this, &parentPalette, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::updateChildrenPalettes(parentPalette);
  }
};

//  QQuickMenu *QQuickMenuPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickMenu *ritual_ZN17QQuickMenuPrivate6q_funcEv(QQuickMenuPrivate *self) {
  return self->q_func();
}

//  const QQuickMenu *QQuickMenuPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickMenu *ritual_ZNK17QQuickMenuPrivate6q_funcEv(
    const QQuickMenuPrivate *self) {
  return self->q_func();
}

//  QQuickMenuPrivate::QQuickMenuPrivate()
extern "C" Q_DECL_EXPORT
QQuickMenuPrivate *ritual_ZN17QQuickMenuPrivateC1Ev() {
  return new CuteQQuickMenuPrivate();
}

//  QQuickMenuPrivate *QQuickMenuPrivate::get(QQuickMenu *menu)
extern "C" Q_DECL_EXPORT
QQuickMenuPrivate *ritual_ZN17QQuickMenuPrivate3getEP10QQuickMenu(
    QQuickMenu *menu) {
  return QQuickMenuPrivate::get(menu);
}

//  void QQuickMenuPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate4initEv(QQuickMenuPrivate *self) {
  self->init();
}

//  QPlatformMenu *QQuickMenuPrivate::nativeHandle()
extern "C" Q_DECL_EXPORT
QPlatformMenu *ritual_ZN17QQuickMenuPrivate12nativeHandleEv(
    QQuickMenuPrivate *self) {
  return self->nativeHandle();
}

//  QPlatformMenu *QQuickMenuPrivate::maybeNativeHandle() const
extern "C" Q_DECL_EXPORT
QPlatformMenu *ritual_ZNK17QQuickMenuPrivate17maybeNativeHandleEv(
    const QQuickMenuPrivate *self) {
  return self->maybeNativeHandle();
}

//  QQuickMenu *QQuickMenuPrivate::rootMenu() const
extern "C" Q_DECL_EXPORT
QQuickMenu *ritual_ZNK17QQuickMenuPrivate8rootMenuEv(
    const QQuickMenuPrivate *self) {
  return self->rootMenu();
}

//  bool QQuickMenuPrivate::useNativeMenu() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickMenuPrivate13useNativeMenuEv(
    const QQuickMenuPrivate *self) {
  return self->useNativeMenu();
}

//  bool QQuickMenuPrivate::createNativeMenu()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickMenuPrivate16createNativeMenuEv(
    QQuickMenuPrivate *self) {
  return self->createNativeMenu();
}

//  void QQuickMenuPrivate::removeNativeMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate16removeNativeMenuEv(
    QQuickMenuPrivate *self) {
  self->removeNativeMenu();
}

//  void QQuickMenuPrivate::syncWithNativeMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate18syncWithNativeMenuEv(
    QQuickMenuPrivate *self) {
  self->syncWithNativeMenu();
}

//  void QQuickMenuPrivate::syncWithUseNativeMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate21syncWithUseNativeMenuEv(
    QQuickMenuPrivate *self) {
  self->syncWithUseNativeMenu();
}

//  void QQuickMenuPrivate::setNativeMenuVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate20setNativeMenuVisibleEb(
    QQuickMenuPrivate *self,
    bool visible) {
  self->setNativeMenuVisible(visible);
}

//  void QQuickMenuPrivate::makeEditMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate12makeEditMenuEv(QQuickMenuPrivate *self) {
  self->makeEditMenu();
}

//  QQuickItem *QQuickMenuPrivate::itemAt(int index) const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK17QQuickMenuPrivate6itemAtEi(
    const QQuickMenuPrivate *self,
    int index) {
  return self->itemAt(index);
}

//  void QQuickMenuPrivate::insertItem(int index, QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate10insertItemEiP10QQuickItem(
    QQuickMenuPrivate *self,
    int index,
    QQuickItem *item) {
  self->insertItem(index, item);
}

//  void QQuickMenuPrivate::maybeCreateAndInsertNativeItem(int index,
//      QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate30maybeCreateAndInsertNativeItemEiP10QQuickItem(
    QQuickMenuPrivate *self,
    int index,
    QQuickItem *item) {
  self->maybeCreateAndInsertNativeItem(index, item);
}

//  void QQuickMenuPrivate::moveItem(int from, int to)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate8moveItemEii(
    QQuickMenuPrivate *self,
    int from,
    int to) {
  self->moveItem(from, to);
}

//  void QQuickMenuPrivate::removeItem(int index, QQuickItem *item,
//      DestructionPolicy destructionPolicy)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate10removeItemEiP10QQuickItemNS_17DestructionPolicyE(
    QQuickMenuPrivate *self,
    int index,
    QQuickItem *item,
    QQuickMenuPrivate::DestructionPolicy destructionPolicy) {
  self->removeItem(index, item, destructionPolicy);
}

//  void QQuickMenuPrivate::removeNativeItem(int index, SyncPolicy
//      syncPolicy)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate16removeNativeItemEiNS_10SyncPolicyE(
    QQuickMenuPrivate *self,
    int index,
    QQuickMenuPrivate::SyncPolicy syncPolicy) {
  self->removeNativeItem(index, syncPolicy);
}

//  void QQuickMenuPrivate::resetNativeData()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate15resetNativeDataEv(
    QQuickMenuPrivate *self) {
  self->resetNativeData();
}

//  void QQuickMenuPrivate::recursivelyCreateNativeMenuItems(QQuickMenu
//      *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate32recursivelyCreateNativeMenuItemsEP10QQuickMenu(
    QQuickMenu *menu) {
  QQuickMenuPrivate::recursivelyCreateNativeMenuItems(menu);
}

//  void QQuickMenuPrivate::printContentModelItems() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QQuickMenuPrivate22printContentModelItemsEv(
    const QQuickMenuPrivate *self) {
  self->printContentModelItems();
}

//  QQuickItem *QQuickMenuPrivate::beginCreateItem()
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN17QQuickMenuPrivate15beginCreateItemEv(
    QQuickMenuPrivate *self) {
  return self->beginCreateItem();
}

//  void QQuickMenuPrivate::completeCreateItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate18completeCreateItemEv(
    QQuickMenuPrivate *self) {
  self->completeCreateItem();
}

//  QQuickItem *QQuickMenuPrivate::createItem(QQuickMenu *menu)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN17QQuickMenuPrivate10createItemEP10QQuickMenu(
    QQuickMenuPrivate *self,
    QQuickMenu *menu) {
  return self->createItem(menu);
}

//  QQuickItem *QQuickMenuPrivate::createItem(QQuickAction *action)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN17QQuickMenuPrivate10createItemEP12QQuickAction(
    QQuickMenuPrivate *self,
    QQuickAction *action) {
  return self->createItem(action);
}

//  void QQuickMenuPrivate::resizeItem(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate10resizeItemEP10QQuickItem(
    QQuickMenuPrivate *self,
    QQuickItem *item) {
  self->resizeItem(item);
}

//  void QQuickMenuPrivate::resizeItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate11resizeItemsEv(QQuickMenuPrivate *self) {
  self->resizeItems();
}

//  void QQuickMenuPrivate::itemChildAdded(QQuickItem *item, QQuickItem
//      *child)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate14itemChildAddedEP10QQuickItemS1_(
    QQuickMenuPrivate *self,
    QQuickItem *item,
    QQuickItem *child) {
  self->itemChildAdded(item, child);
}

//  void QQuickMenuPrivate::itemSiblingOrderChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate23itemSiblingOrderChangedEP10QQuickItem(
    QQuickMenuPrivate *self,
    QQuickItem *item) {
  self->itemSiblingOrderChanged(item);
}

//  void QQuickMenuPrivate::itemParentChanged(QQuickItem *item, QQuickItem
//      *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate17itemParentChangedEP10QQuickItemS1_(
    QQuickMenuPrivate *self,
    QQuickItem *item,
    QQuickItem *parent) {
  self->itemParentChanged(item, parent);
}

//  void QQuickMenuPrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate13itemDestroyedEP10QQuickItem(
    QQuickMenuPrivate *self,
    QQuickItem *item) {
  self->itemDestroyed(item);
}

//  void QQuickMenuPrivate::itemGeometryChanged(QQuickItem *a0,
//      QQuickGeometryChange change, const QRectF &diff)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickMenuPrivate *self,
    QQuickItem *a0,
    const QQuickGeometryChange *change,
    const QRectF *diff) {
  self->itemGeometryChanged(a0, *change, *diff);
}

//  QQuickPopupPositioner *QQuickMenuPrivate::getPositioner()
extern "C" Q_DECL_EXPORT
QQuickPopupPositioner *ritual_ZN17QQuickMenuPrivate13getPositionerEv(
    QQuickMenuPrivate *self) {
  return self->getPositioner();
}

//  bool QQuickMenuPrivate::prepareEnterTransition()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickMenuPrivate22prepareEnterTransitionEv(
    QQuickMenuPrivate *self) {
  return self->prepareEnterTransition();
}

//  bool QQuickMenuPrivate::prepareExitTransition()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickMenuPrivate21prepareExitTransitionEv(
    QQuickMenuPrivate *self) {
  return self->prepareExitTransition();
}

//  bool QQuickMenuPrivate::blockInput(QQuickItem *item, const QPointF
//      &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickMenuPrivate10blockInputEP10QQuickItemRK7QPointF(
    const QQuickMenuPrivate *self,
    QQuickItem *item,
    const QPointF *point) {
  return self->blockInput(item, *point);
}

//  bool QQuickMenuPrivate::handlePress(QQuickItem *item, const QPointF
//      &point, ulong timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickMenuPrivate11handlePressEP10QQuickItemRK7QPointFm(
    QQuickMenuPrivate *self,
    QQuickItem *item,
    const QPointF *point,
    ulong timestamp) {
  return self->handlePress(item, *point, timestamp);
}

//  bool QQuickMenuPrivate::handleReleaseWithoutGrab(const QEventPoint
//      &eventPoint)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickMenuPrivate24handleReleaseWithoutGrabERK11QEventPoint(
    QQuickMenuPrivate *self,
    const QEventPoint *eventPoint) {
  return self->handleReleaseWithoutGrab(*eventPoint);
}

//  void QQuickMenuPrivate::onItemHovered()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate13onItemHoveredEv(QQuickMenuPrivate *self) {
  self->onItemHovered();
}

//  void QQuickMenuPrivate::onItemTriggered()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate15onItemTriggeredEv(
    QQuickMenuPrivate *self) {
  self->onItemTriggered();
}

//  void QQuickMenuPrivate::onItemActiveFocusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate24onItemActiveFocusChangedEv(
    QQuickMenuPrivate *self) {
  self->onItemActiveFocusChanged();
}

//  void QQuickMenuPrivate::onItemVisibleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate20onItemVisibleChangedEv(
    QQuickMenuPrivate *self) {
  self->onItemVisibleChanged();
}

//  void QQuickMenuPrivate::updateTextPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate17updateTextPaddingEv(
    QQuickMenuPrivate *self) {
  self->updateTextPadding();
}

//  void QQuickMenuPrivate::updateCollapsedSeparators()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate25updateCollapsedSeparatorsEv(
    QQuickMenuPrivate *self) {
  self->updateCollapsedSeparators();
}

//  QQuickMenu *QQuickMenuPrivate::currentSubMenu() const
extern "C" Q_DECL_EXPORT
QQuickMenu *ritual_ZNK17QQuickMenuPrivate14currentSubMenuEv(
    const QQuickMenuPrivate *self) {
  return self->currentSubMenu();
}

//  void QQuickMenuPrivate::setParentMenu(QQuickMenu *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate13setParentMenuEP10QQuickMenu(
    QQuickMenuPrivate *self,
    QQuickMenu *parent) {
  self->setParentMenu(parent);
}

//  void QQuickMenuPrivate::resolveParentItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate17resolveParentItemEv(
    QQuickMenuPrivate *self) {
  self->resolveParentItem();
}

//  void QQuickMenuPrivate::popup(QQuickItem *menuItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate5popupEP10QQuickItem(
    QQuickMenuPrivate *self,
    QQuickItem *menuItem) {
  self->popup(menuItem);
}

//  void QQuickMenuPrivate::propagateKeyEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate17propagateKeyEventEP9QKeyEvent(
    QQuickMenuPrivate *self,
    QKeyEvent *event) {
  self->propagateKeyEvent(event);
}

//  void QQuickMenuPrivate::startHoverTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate15startHoverTimerEv(
    QQuickMenuPrivate *self) {
  self->startHoverTimer();
}

//  void QQuickMenuPrivate::stopHoverTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate14stopHoverTimerEv(
    QQuickMenuPrivate *self) {
  self->stopHoverTimer();
}

//  void QQuickMenuPrivate::setCurrentIndex(int index, Qt::FocusReason
//      reason)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate15setCurrentIndexEiN2Qt11FocusReasonE(
    QQuickMenuPrivate *self,
    int index,
    Qt::FocusReason reason) {
  self->setCurrentIndex(index, reason);
}

//  bool QQuickMenuPrivate::activateNextItem()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickMenuPrivate16activateNextItemEv(
    QQuickMenuPrivate *self) {
  return self->activateNextItem();
}

//  bool QQuickMenuPrivate::activatePreviousItem()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickMenuPrivate20activatePreviousItemEv(
    QQuickMenuPrivate *self) {
  return self->activatePreviousItem();
}

//  QQuickMenuItem *QQuickMenuPrivate::firstEnabledMenuItem() const
extern "C" Q_DECL_EXPORT
QQuickMenuItem *ritual_ZNK17QQuickMenuPrivate20firstEnabledMenuItemEv(
    const QQuickMenuPrivate *self) {
  return self->firstEnabledMenuItem();
}

//  void QQuickMenuPrivate::contentData_append(QQmlListProperty<QObject>
//      *prop, QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate18contentData_appendEP16QQmlListPropertyI7QObjectEPS1_(
    QQmlListProperty<QObject> *prop,
    QObject *obj) {
  QQuickMenuPrivate::contentData_append(prop, obj);
}

//  qsizetype QQuickMenuPrivate::contentData_count(QQmlListProperty<QObject>
//      *prop)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN17QQuickMenuPrivate17contentData_countEP16QQmlListPropertyI7QObjectE(
    QQmlListProperty<QObject> *prop) {
  return QQuickMenuPrivate::contentData_count(prop);
}

//  QObject *QQuickMenuPrivate::contentData_at(QQmlListProperty<QObject>
//      *prop, qsizetype index)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN17QQuickMenuPrivate14contentData_atEP16QQmlListPropertyI7QObjectEx(
    QQmlListProperty<QObject> *prop,
    qsizetype index) {
  return QQuickMenuPrivate::contentData_at(prop, index);
}

//  void QQuickMenuPrivate::contentData_clear(QQmlListProperty<QObject>
//      *prop)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate17contentData_clearEP16QQmlListPropertyI7QObjectE(
    QQmlListProperty<QObject> *prop) {
  QQuickMenuPrivate::contentData_clear(prop);
}

//  QPalette QQuickMenuPrivate::defaultPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK17QQuickMenuPrivate14defaultPaletteEv(
    const QQuickMenuPrivate *self) {
  return new QPalette(self->defaultPalette());
}

//  QQuickPopup::PopupType QQuickMenuPrivate::resolvedPopupType() const
extern "C" Q_DECL_EXPORT
QQuickPopup::PopupType ritual_ZNK17QQuickMenuPrivate17resolvedPopupTypeEv(
    const QQuickMenuPrivate *self) {
  return self->resolvedPopupType();
}

//  void QQuickMenuPrivate::resetContentItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickMenuPrivate16resetContentItemEv(
    QQuickMenuPrivate *self) {
  self->resetContentItem();
}

//  a Python function taken by a CuteQQuickMenuPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickMenuPrivate(
    QQuickMenuPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickMenuPrivate *>(self)->take(key, call);
}

//  void QQuickMenuPrivate::itemChildAdded(QQuickItem *item, QQuickItem
//      *child)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickMenuPrivate14itemChildAddedEP10QQuickItemS1_(
    QQuickMenuPrivate *self,
    QQuickItem *item,
    QQuickItem *child) {
  self->QQuickMenuPrivate::itemChildAdded(item, child);
}

//  void QQuickMenuPrivate::itemSiblingOrderChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickMenuPrivate23itemSiblingOrderChangedEP10QQuickItem(
    QQuickMenuPrivate *self,
    QQuickItem *item) {
  self->QQuickMenuPrivate::itemSiblingOrderChanged(item);
}

//  void QQuickMenuPrivate::itemParentChanged(QQuickItem *item, QQuickItem
//      *parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickMenuPrivate17itemParentChangedEP10QQuickItemS1_(
    QQuickMenuPrivate *self,
    QQuickItem *item,
    QQuickItem *parent) {
  self->QQuickMenuPrivate::itemParentChanged(item, parent);
}

//  void QQuickMenuPrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickMenuPrivate13itemDestroyedEP10QQuickItem(
    QQuickMenuPrivate *self,
    QQuickItem *item) {
  self->QQuickMenuPrivate::itemDestroyed(item);
}

//  void QQuickMenuPrivate::itemGeometryChanged(QQuickItem *a0,
//      QQuickGeometryChange change, const QRectF &diff)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickMenuPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickMenuPrivate *self,
    QQuickItem *a0,
    const QQuickGeometryChange *change,
    const QRectF *diff) {
  self->QQuickMenuPrivate::itemGeometryChanged(a0, *change, *diff);
}

//  QQuickPopupPositioner *QQuickMenuPrivate::getPositioner()
extern "C" Q_DECL_EXPORT
QQuickPopupPositioner *ritual_own_ZN17QQuickMenuPrivate13getPositionerEv(
    QQuickMenuPrivate *self) {
  return self->QQuickMenuPrivate::getPositioner();
}

//  bool QQuickMenuPrivate::prepareEnterTransition()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QQuickMenuPrivate22prepareEnterTransitionEv(
    QQuickMenuPrivate *self) {
  return self->QQuickMenuPrivate::prepareEnterTransition();
}

//  bool QQuickMenuPrivate::prepareExitTransition()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QQuickMenuPrivate21prepareExitTransitionEv(
    QQuickMenuPrivate *self) {
  return self->QQuickMenuPrivate::prepareExitTransition();
}

//  bool QQuickMenuPrivate::blockInput(QQuickItem *item, const QPointF
//      &point) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QQuickMenuPrivate10blockInputEP10QQuickItemRK7QPointF(
    const QQuickMenuPrivate *self,
    QQuickItem *item,
    const QPointF *point) {
  return self->QQuickMenuPrivate::blockInput(item, *point);
}

//  bool QQuickMenuPrivate::handlePress(QQuickItem *item, const QPointF
//      &point, ulong timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QQuickMenuPrivate11handlePressEP10QQuickItemRK7QPointFm(
    QQuickMenuPrivate *self,
    QQuickItem *item,
    const QPointF *point,
    ulong timestamp) {
  return self->QQuickMenuPrivate::handlePress(item, *point, timestamp);
}

//  bool QQuickMenuPrivate::handleReleaseWithoutGrab(const QEventPoint
//      &eventPoint)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QQuickMenuPrivate24handleReleaseWithoutGrabERK11QEventPoint(
    QQuickMenuPrivate *self,
    const QEventPoint *eventPoint) {
  return self->QQuickMenuPrivate::handleReleaseWithoutGrab(*eventPoint);
}

//  QPalette QQuickMenuPrivate::defaultPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_own_ZNK17QQuickMenuPrivate14defaultPaletteEv(
    const QQuickMenuPrivate *self) {
  return new QPalette(self->QQuickMenuPrivate::defaultPalette());
}

//  QQuickPopup::PopupType QQuickMenuPrivate::resolvedPopupType() const
extern "C" Q_DECL_EXPORT
QQuickPopup::PopupType ritual_own_ZNK17QQuickMenuPrivate17resolvedPopupTypeEv(
    const QQuickMenuPrivate *self) {
  return self->QQuickMenuPrivate::resolvedPopupType();
}

#endif  // QT_CONFIG(qml_object_model)
