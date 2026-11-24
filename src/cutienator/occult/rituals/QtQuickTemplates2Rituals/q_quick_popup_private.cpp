//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpopup_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpopup_p.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpopup_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/qeventpoint.h>
#include <QtCore/qmargins.h>
#include <QtGui/qpalette.h>
#include <cstring>

//  A QQuickPopupPrivate that Python can take functions over in. Every QQuickPopupPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickPopupPrivateCall0)(const void *, const QEventPoint *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickPopupPrivateCall1)(const void *, QQuickItem *, const QPointF *, int *);
typedef bool (*CuteQQuickPopupPrivateCall2)(const void *, QQuickItem *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickPopupPrivateCall3)(const void *, QQuickItem *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickPopupPrivateCall4)(const void *, QQuickItem *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickPopupPrivateCall5)(const void *, const QEventPoint *, int *);
typedef void (*CuteQQuickPopupPrivateCall6)(const void *, int *);
typedef int (*CuteQQuickPopupPrivateCall7)(const void *, int *);
typedef void (*CuteQQuickPopupPrivateCall8)(const void *, int *);
typedef void (*CuteQQuickPopupPrivateCall9)(const void *, int *);
typedef void (*CuteQQuickPopupPrivateCall10)(const void *, int *);
typedef bool (*CuteQQuickPopupPrivateCall11)(const void *, int *);
typedef bool (*CuteQQuickPopupPrivateCall12)(const void *, int *);
typedef void (*CuteQQuickPopupPrivateCall13)(const void *, int *);
typedef void (*CuteQQuickPopupPrivateCall14)(const void *, int *);
typedef void (*CuteQQuickPopupPrivateCall15)(const void *, int *);
typedef void * (*CuteQQuickPopupPrivateCall16)(const void *, int *);
typedef void (*CuteQQuickPopupPrivateCall17)(const void *, QQuickItem *, int *);
typedef const QPalette * (*CuteQQuickPopupPrivateCall18)(const void *, int *);
typedef void (*CuteQQuickPopupPrivateCall19)(const void *, const QPalette *, int *);
class CuteQQuickPopupPrivate : public QQuickPopupPrivate {
public:
  using QQuickPopupPrivate::QQuickPopupPrivate;
  void *taken[20] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate11acceptTouchERK11QEventPoint")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZNK18QQuickPopupPrivate10blockInputEP10QQuickItemRK7QPointF")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate11handlePressEP10QQuickItemRK7QPointFm")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate10handleMoveEP10QQuickItemRK7QPointFm")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate13handleReleaseEP10QQuickItemRK7QPointFm")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate24handleReleaseWithoutGrabERK11QEventPoint")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate12handleUngrabEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QQuickPopupPrivate17resolvedPopupTypeEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate10showDimmerEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate10hideDimmerEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate12resizeDimmerEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate22prepareEnterTransitionEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate21prepareExitTransitionEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate23finalizeEnterTransitionEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate22finalizeExitTransitionEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate6openedEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate13getPositionerEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate13itemDestroyedEP10QQuickItem")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QQuickPopupPrivate14defaultPaletteEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate22updateChildrenPalettesERK8QPalette")) {
      taken[19] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  bool QQuickPopupPrivate::acceptTouch(const QTouchEvent::TouchPoint
  //      &point)
  bool acceptTouch(const QTouchEvent::TouchPoint &point) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickPopupPrivateCall0 call = reinterpret_cast<CuteQQuickPopupPrivateCall0>(taken[0]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::acceptTouch(point);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

  //  bool QQuickPopupPrivate::blockInput(QQuickItem *item, const QPointF
  //      &point) const
  bool blockInput(QQuickItem *item, const QPointF &point) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPopupPrivateCall1 call = reinterpret_cast<CuteQQuickPopupPrivateCall1>(taken[1]);
      bool given = call(this, item, &point, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::blockInput(item, point);
  }

  //  bool QQuickPopupPrivate::handlePress(QQuickItem *item, const QPointF
  //      &point, ulong timestamp)
  bool handlePress(
      QQuickItem *item,
      const QPointF &point,
      ulong timestamp) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickPopupPrivateCall2 call = reinterpret_cast<CuteQQuickPopupPrivateCall2>(taken[2]);
      bool given = call(this, item, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::handlePress(item, point, timestamp);
  }

  //  bool QQuickPopupPrivate::handleMove(QQuickItem *item, const QPointF
  //      &point, ulong timestamp)
  bool handleMove(
      QQuickItem *item,
      const QPointF &point,
      ulong timestamp) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPopupPrivateCall3 call = reinterpret_cast<CuteQQuickPopupPrivateCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQQuickPopupPrivateCall4 call = reinterpret_cast<CuteQQuickPopupPrivateCall4>(taken[4]);
      bool given = call(this, item, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::handleRelease(item, point, timestamp);
  }

  //  bool QQuickPopupPrivate::handleReleaseWithoutGrab(const QEventPoint
  //      &a0)
  bool handleReleaseWithoutGrab(const QEventPoint &a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickPopupPrivateCall5 call = reinterpret_cast<CuteQQuickPopupPrivateCall5>(taken[5]);
      bool given = call(this, &a0, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::handleReleaseWithoutGrab(a0);
  }

  //  void QQuickPopupPrivate::handleUngrab()
  void handleUngrab() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickPopupPrivateCall6 call = reinterpret_cast<CuteQQuickPopupPrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::handleUngrab();
  }

  //  QQuickPopup::PopupType QQuickPopupPrivate::resolvedPopupType() const
  QQuickPopup::PopupType resolvedPopupType() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickPopupPrivateCall7 call = reinterpret_cast<CuteQQuickPopupPrivateCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickPopup::PopupType>(given);
    }
    return QQuickPopupPrivate::resolvedPopupType();
  }

  //  void QQuickPopupPrivate::showDimmer()
  void showDimmer() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickPopupPrivateCall8 call = reinterpret_cast<CuteQQuickPopupPrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::showDimmer();
  }

  //  void QQuickPopupPrivate::hideDimmer()
  void hideDimmer() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickPopupPrivateCall9 call = reinterpret_cast<CuteQQuickPopupPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::hideDimmer();
  }

  //  void QQuickPopupPrivate::resizeDimmer()
  void resizeDimmer() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickPopupPrivateCall10 call = reinterpret_cast<CuteQQuickPopupPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::resizeDimmer();
  }

  //  bool QQuickPopupPrivate::prepareEnterTransition()
  bool prepareEnterTransition() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickPopupPrivateCall11 call = reinterpret_cast<CuteQQuickPopupPrivateCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::prepareEnterTransition();
  }

  //  bool QQuickPopupPrivate::prepareExitTransition()
  bool prepareExitTransition() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickPopupPrivateCall12 call = reinterpret_cast<CuteQQuickPopupPrivateCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::prepareExitTransition();
  }

  //  void QQuickPopupPrivate::finalizeEnterTransition()
  void finalizeEnterTransition() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickPopupPrivateCall13 call = reinterpret_cast<CuteQQuickPopupPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::finalizeEnterTransition();
  }

  //  void QQuickPopupPrivate::finalizeExitTransition()
  void finalizeExitTransition() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickPopupPrivateCall14 call = reinterpret_cast<CuteQQuickPopupPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::finalizeExitTransition();
  }

  //  void QQuickPopupPrivate::opened()
  void opened() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickPopupPrivateCall15 call = reinterpret_cast<CuteQQuickPopupPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::opened();
  }

  //  QQuickPopupPositioner *QQuickPopupPrivate::getPositioner()
  QQuickPopupPositioner *getPositioner() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickPopupPrivateCall16 call = reinterpret_cast<CuteQQuickPopupPrivateCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickPopupPositioner *>(given);
    }
    return QQuickPopupPrivate::getPositioner();
  }

  //  void QQuickPopupPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickPopupPrivateCall17 call = reinterpret_cast<CuteQQuickPopupPrivateCall17>(taken[17]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::itemDestroyed(item);
  }

  //  QPalette QQuickPopupPrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickPopupPrivateCall18 call = reinterpret_cast<CuteQQuickPopupPrivateCall18>(taken[18]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickPopupPrivate::defaultPalette();
  }

  //  void QQuickPopupPrivate::updateChildrenPalettes(const QPalette
  //      &parentPalette)
  void updateChildrenPalettes(const QPalette &parentPalette) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickPopupPrivateCall19 call = reinterpret_cast<CuteQQuickPopupPrivateCall19>(taken[19]);
      call(this, &parentPalette, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::updateChildrenPalettes(parentPalette);
  }
};

//  QQuickPopup *QQuickPopupPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickPopup *ritual_ZN18QQuickPopupPrivate6q_funcEv(
    QQuickPopupPrivate *self) {
  return self->q_func();
}

//  const QQuickPopup *QQuickPopupPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickPopup *ritual_ZNK18QQuickPopupPrivate6q_funcEv(
    const QQuickPopupPrivate *self) {
  return self->q_func();
}

//  QQuickPopupPrivate::QQuickPopupPrivate()
extern "C" Q_DECL_EXPORT
QQuickPopupPrivate *ritual_ZN18QQuickPopupPrivateC1Ev() {
  return new CuteQQuickPopupPrivate();
}

//  QQuickPopupPrivate *QQuickPopupPrivate::get(QQuickPopup *popup)
extern "C" Q_DECL_EXPORT
QQuickPopupPrivate *ritual_ZN18QQuickPopupPrivate3getEP11QQuickPopup(
    QQuickPopup *popup) {
  return QQuickPopupPrivate::get(popup);
}

//  void QQuickPopupPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupPrivate4initEv(QQuickPopupPrivate *self) {
  self->init();
}

//  void QQuickPopupPrivate::closeOrReject()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupPrivate13closeOrRejectEv(
    QQuickPopupPrivate *self) {
  self->closeOrReject();
}

//  bool QQuickPopupPrivate::tryClose(const QPointF &pos,
//      QQuickPopup::ClosePolicy flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickPopupPrivate8tryCloseERK7QPointF6QFlagsIN11QQuickPopup15ClosePolicyFlagEE(
    QQuickPopupPrivate *self,
    const QPointF *pos,
    int flags) {
  return self->tryClose(
      *pos,
      QFlags<QQuickPopup::ClosePolicyFlag>::fromInt(flags));
}

//  bool QQuickPopupPrivate::contains(const QPointF &scenePos) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickPopupPrivate8containsERK7QPointF(
    const QQuickPopupPrivate *self,
    const QPointF *scenePos) {
  return self->contains(*scenePos);
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  bool QQuickPopupPrivate::acceptTouch(const QTouchEvent::TouchPoint
//      &point)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickPopupPrivate11acceptTouchERK11QEventPoint(
    QQuickPopupPrivate *self,
    const QEventPoint *point) {
  return self->acceptTouch(*point);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

//  bool QQuickPopupPrivate::blockInput(QQuickItem *item, const QPointF
//      &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickPopupPrivate10blockInputEP10QQuickItemRK7QPointF(
    const QQuickPopupPrivate *self,
    QQuickItem *item,
    const QPointF *point) {
  return self->blockInput(item, *point);
}

//  bool QQuickPopupPrivate::handlePress(QQuickItem *item, const QPointF
//      &point, ulong timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickPopupPrivate11handlePressEP10QQuickItemRK7QPointFm(
    QQuickPopupPrivate *self,
    QQuickItem *item,
    const QPointF *point,
    ulong timestamp) {
  return self->handlePress(item, *point, timestamp);
}

//  bool QQuickPopupPrivate::handleMove(QQuickItem *item, const QPointF
//      &point, ulong timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickPopupPrivate10handleMoveEP10QQuickItemRK7QPointFm(
    QQuickPopupPrivate *self,
    QQuickItem *item,
    const QPointF *point,
    ulong timestamp) {
  return self->handleMove(item, *point, timestamp);
}

//  bool QQuickPopupPrivate::handleRelease(QQuickItem *item, const QPointF
//      &point, ulong timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickPopupPrivate13handleReleaseEP10QQuickItemRK7QPointFm(
    QQuickPopupPrivate *self,
    QQuickItem *item,
    const QPointF *point,
    ulong timestamp) {
  return self->handleRelease(item, *point, timestamp);
}

//  bool QQuickPopupPrivate::handleReleaseWithoutGrab(const QEventPoint &a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickPopupPrivate24handleReleaseWithoutGrabERK11QEventPoint(
    QQuickPopupPrivate *self,
    const QEventPoint *a0) {
  return self->handleReleaseWithoutGrab(*a0);
}

//  void QQuickPopupPrivate::handleUngrab()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupPrivate12handleUngrabEv(
    QQuickPopupPrivate *self) {
  self->handleUngrab();
}

//  bool QQuickPopupPrivate::handleMouseEvent(QQuickItem *item, QMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickPopupPrivate16handleMouseEventEP10QQuickItemP11QMouseEvent(
    QQuickPopupPrivate *self,
    QQuickItem *item,
    QMouseEvent *event) {
  return self->handleMouseEvent(item, event);
}

//  bool QQuickPopupPrivate::handleHoverEvent(QQuickItem *item, QHoverEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickPopupPrivate16handleHoverEventEP10QQuickItemP11QHoverEvent(
    QQuickPopupPrivate *self,
    QQuickItem *item,
    QHoverEvent *event) {
  return self->handleHoverEvent(item, event);
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  bool QQuickPopupPrivate::handleTouchEvent(QQuickItem *item, QTouchEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickPopupPrivate16handleTouchEventEP10QQuickItemP11QTouchEvent(
    QQuickPopupPrivate *self,
    QQuickItem *item,
    QTouchEvent *event) {
  return self->handleTouchEvent(item, event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

//  QMarginsF QQuickPopupPrivate::windowInsets() const
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZNK18QQuickPopupPrivate12windowInsetsEv(
    const QQuickPopupPrivate *self) {
  return new QMarginsF(self->windowInsets());
}

//  QPointF QQuickPopupPrivate::windowInsetsTopLeft() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK18QQuickPopupPrivate19windowInsetsTopLeftEv(
    const QQuickPopupPrivate *self) {
  return new QPointF(self->windowInsetsTopLeft());
}

//  void QQuickPopupPrivate::setEffectivePosFromWindowPos(const QPointF
//      &windowPos)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupPrivate28setEffectivePosFromWindowPosERK7QPointF(
    QQuickPopupPrivate *self,
    const QPointF *windowPos) {
  self->setEffectivePosFromWindowPos(*windowPos);
}

//  void QQuickPopupPrivate::reposition()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupPrivate10repositionEv(QQuickPopupPrivate *self) {
  self->reposition();
}

//  bool QQuickPopupPrivate::usePopupWindow() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQuickPopupPrivate14usePopupWindowEv(
    const QQuickPopupPrivate *self) {
  return self->usePopupWindow();
}

//  void QQuickPopupPrivate::adjustPopupItemParentAndWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupPrivate30adjustPopupItemParentAndWindowEv(
    QQuickPopupPrivate *self) {
  self->adjustPopupItemParentAndWindow();
}

//  void QQuickPopupPrivate::createOverlay()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupPrivate13createOverlayEv(
    QQuickPopupPrivate *self) {
  self->createOverlay();
}

//  QQuickItem *QQuickPopupPrivate::createDimmer(QQmlComponent *component,
//      QQuickPopup *popup, QQuickItem *parent) const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK18QQuickPopupPrivate12createDimmerEP13QQmlComponentP11QQuickPopupP10QQuickItem(
    const QQuickPopupPrivate *self,
    QQmlComponent *component,
    QQuickPopup *popup,
    QQuickItem *parent) {
  return self->createDimmer(component, popup, parent);
}

//  void QQuickPopupPrivate::destroyDimmer()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupPrivate13destroyDimmerEv(
    QQuickPopupPrivate *self) {
  self->destroyDimmer();
}

//  void QQuickPopupPrivate::toggleOverlay()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupPrivate13toggleOverlayEv(
    QQuickPopupPrivate *self) {
  self->toggleOverlay();
}

//  void QQuickPopupPrivate::updateContentPalettes(const QPalette
//      &parentPalette)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupPrivate21updateContentPalettesERK8QPalette(
    QQuickPopupPrivate *self,
    const QPalette *parentPalette) {
  self->updateContentPalettes(*parentPalette);
}

//  QQuickPopup::PopupType QQuickPopupPrivate::resolvedPopupType() const
extern "C" Q_DECL_EXPORT
QQuickPopup::PopupType ritual_ZNK18QQuickPopupPrivate17resolvedPopupTypeEv(
    const QQuickPopupPrivate *self) {
  return self->resolvedPopupType();
}

//  void QQuickPopupPrivate::showDimmer()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupPrivate10showDimmerEv(QQuickPopupPrivate *self) {
  self->showDimmer();
}

//  void QQuickPopupPrivate::hideDimmer()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupPrivate10hideDimmerEv(QQuickPopupPrivate *self) {
  self->hideDimmer();
}

//  void QQuickPopupPrivate::resizeDimmer()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupPrivate12resizeDimmerEv(
    QQuickPopupPrivate *self) {
  self->resizeDimmer();
}

//  bool QQuickPopupPrivate::prepareEnterTransition()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickPopupPrivate22prepareEnterTransitionEv(
    QQuickPopupPrivate *self) {
  return self->prepareEnterTransition();
}

//  bool QQuickPopupPrivate::prepareExitTransition()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickPopupPrivate21prepareExitTransitionEv(
    QQuickPopupPrivate *self) {
  return self->prepareExitTransition();
}

//  void QQuickPopupPrivate::finalizeEnterTransition()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupPrivate23finalizeEnterTransitionEv(
    QQuickPopupPrivate *self) {
  self->finalizeEnterTransition();
}

//  void QQuickPopupPrivate::finalizeExitTransition()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupPrivate22finalizeExitTransitionEv(
    QQuickPopupPrivate *self) {
  self->finalizeExitTransition();
}

//  void QQuickPopupPrivate::opened()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupPrivate6openedEv(QQuickPopupPrivate *self) {
  self->opened();
}

//  Qt::WindowFlags QQuickPopupPrivate::popupWindowFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QQuickPopupPrivate16popupWindowFlagsEv(
    const QQuickPopupPrivate *self) {
  return static_cast<int>(self->popupWindowFlags().toInt());
}

//  void QQuickPopupPrivate::setPopupWindowFlags(Qt::WindowFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupPrivate19setPopupWindowFlagsE6QFlagsIN2Qt10WindowTypeEE(
    QQuickPopupPrivate *self,
    int flags) {
  self->setPopupWindowFlags(QFlags<Qt::WindowType>::fromInt(flags));
}

//  QMarginsF QQuickPopupPrivate::getMargins() const
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZNK18QQuickPopupPrivate10getMarginsEv(
    const QQuickPopupPrivate *self) {
  return new QMarginsF(self->getMargins());
}

//  void QQuickPopupPrivate::setTopMargin(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupPrivate12setTopMarginEdb(
    QQuickPopupPrivate *self,
    qreal value,
    bool reset) {
  self->setTopMargin(value, reset);
}

//  void QQuickPopupPrivate::setLeftMargin(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupPrivate13setLeftMarginEdb(
    QQuickPopupPrivate *self,
    qreal value,
    bool reset) {
  self->setLeftMargin(value, reset);
}

//  void QQuickPopupPrivate::setRightMargin(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupPrivate14setRightMarginEdb(
    QQuickPopupPrivate *self,
    qreal value,
    bool reset) {
  self->setRightMargin(value, reset);
}

//  void QQuickPopupPrivate::setBottomMargin(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupPrivate15setBottomMarginEdb(
    QQuickPopupPrivate *self,
    qreal value,
    bool reset) {
  self->setBottomMargin(value, reset);
}

//  QQuickPopupAnchors *QQuickPopupPrivate::getAnchors()
extern "C" Q_DECL_EXPORT
QQuickPopupAnchors *ritual_ZN18QQuickPopupPrivate10getAnchorsEv(
    QQuickPopupPrivate *self) {
  return self->getAnchors();
}

//  QQuickPopupPositioner *QQuickPopupPrivate::getPositioner()
extern "C" Q_DECL_EXPORT
QQuickPopupPositioner *ritual_ZN18QQuickPopupPrivate13getPositionerEv(
    QQuickPopupPrivate *self) {
  return self->getPositioner();
}

//  void QQuickPopupPrivate::setWindow(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupPrivate9setWindowEP12QQuickWindow(
    QQuickPopupPrivate *self,
    QQuickWindow *window) {
  self->setWindow(window);
}

//  void QQuickPopupPrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupPrivate13itemDestroyedEP10QQuickItem(
    QQuickPopupPrivate *self,
    QQuickItem *item) {
  self->itemDestroyed(item);
}

//  QPalette QQuickPopupPrivate::defaultPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK18QQuickPopupPrivate14defaultPaletteEv(
    const QQuickPopupPrivate *self) {
  return new QPalette(self->defaultPalette());
}

//  void QQuickPopupPrivate::updateChildrenPalettes(const QPalette
//      &parentPalette)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupPrivate22updateChildrenPalettesERK8QPalette(
    QQuickPopupPrivate *self,
    const QPalette *parentPalette) {
  self->updateChildrenPalettes(*parentPalette);
}

//  a Python function taken by a CuteQQuickPopupPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPopupPrivate(
    QQuickPopupPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPopupPrivate *>(self)->take(key, call);
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  bool QQuickPopupPrivate::acceptTouch(const QTouchEvent::TouchPoint
//      &point)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QQuickPopupPrivate11acceptTouchERK11QEventPoint(
    QQuickPopupPrivate *self,
    const QEventPoint *point) {
  return self->QQuickPopupPrivate::acceptTouch(*point);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

//  bool QQuickPopupPrivate::blockInput(QQuickItem *item, const QPointF
//      &point) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QQuickPopupPrivate10blockInputEP10QQuickItemRK7QPointF(
    const QQuickPopupPrivate *self,
    QQuickItem *item,
    const QPointF *point) {
  return self->QQuickPopupPrivate::blockInput(item, *point);
}

//  bool QQuickPopupPrivate::handlePress(QQuickItem *item, const QPointF
//      &point, ulong timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QQuickPopupPrivate11handlePressEP10QQuickItemRK7QPointFm(
    QQuickPopupPrivate *self,
    QQuickItem *item,
    const QPointF *point,
    ulong timestamp) {
  return self->QQuickPopupPrivate::handlePress(item, *point, timestamp);
}

//  bool QQuickPopupPrivate::handleMove(QQuickItem *item, const QPointF
//      &point, ulong timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QQuickPopupPrivate10handleMoveEP10QQuickItemRK7QPointFm(
    QQuickPopupPrivate *self,
    QQuickItem *item,
    const QPointF *point,
    ulong timestamp) {
  return self->QQuickPopupPrivate::handleMove(item, *point, timestamp);
}

//  bool QQuickPopupPrivate::handleRelease(QQuickItem *item, const QPointF
//      &point, ulong timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QQuickPopupPrivate13handleReleaseEP10QQuickItemRK7QPointFm(
    QQuickPopupPrivate *self,
    QQuickItem *item,
    const QPointF *point,
    ulong timestamp) {
  return self->QQuickPopupPrivate::handleRelease(item, *point, timestamp);
}

//  bool QQuickPopupPrivate::handleReleaseWithoutGrab(const QEventPoint &a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QQuickPopupPrivate24handleReleaseWithoutGrabERK11QEventPoint(
    QQuickPopupPrivate *self,
    const QEventPoint *a0) {
  return self->QQuickPopupPrivate::handleReleaseWithoutGrab(*a0);
}

//  void QQuickPopupPrivate::handleUngrab()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickPopupPrivate12handleUngrabEv(
    QQuickPopupPrivate *self) {
  self->QQuickPopupPrivate::handleUngrab();
}

//  QQuickPopup::PopupType QQuickPopupPrivate::resolvedPopupType() const
extern "C" Q_DECL_EXPORT
QQuickPopup::PopupType ritual_own_ZNK18QQuickPopupPrivate17resolvedPopupTypeEv(
    const QQuickPopupPrivate *self) {
  return self->QQuickPopupPrivate::resolvedPopupType();
}

//  void QQuickPopupPrivate::showDimmer()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickPopupPrivate10showDimmerEv(
    QQuickPopupPrivate *self) {
  self->QQuickPopupPrivate::showDimmer();
}

//  void QQuickPopupPrivate::hideDimmer()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickPopupPrivate10hideDimmerEv(
    QQuickPopupPrivate *self) {
  self->QQuickPopupPrivate::hideDimmer();
}

//  void QQuickPopupPrivate::resizeDimmer()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickPopupPrivate12resizeDimmerEv(
    QQuickPopupPrivate *self) {
  self->QQuickPopupPrivate::resizeDimmer();
}

//  bool QQuickPopupPrivate::prepareEnterTransition()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QQuickPopupPrivate22prepareEnterTransitionEv(
    QQuickPopupPrivate *self) {
  return self->QQuickPopupPrivate::prepareEnterTransition();
}

//  bool QQuickPopupPrivate::prepareExitTransition()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QQuickPopupPrivate21prepareExitTransitionEv(
    QQuickPopupPrivate *self) {
  return self->QQuickPopupPrivate::prepareExitTransition();
}

//  void QQuickPopupPrivate::finalizeEnterTransition()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickPopupPrivate23finalizeEnterTransitionEv(
    QQuickPopupPrivate *self) {
  self->QQuickPopupPrivate::finalizeEnterTransition();
}

//  void QQuickPopupPrivate::finalizeExitTransition()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickPopupPrivate22finalizeExitTransitionEv(
    QQuickPopupPrivate *self) {
  self->QQuickPopupPrivate::finalizeExitTransition();
}

//  void QQuickPopupPrivate::opened()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickPopupPrivate6openedEv(QQuickPopupPrivate *self) {
  self->QQuickPopupPrivate::opened();
}

//  QQuickPopupPositioner *QQuickPopupPrivate::getPositioner()
extern "C" Q_DECL_EXPORT
QQuickPopupPositioner *ritual_own_ZN18QQuickPopupPrivate13getPositionerEv(
    QQuickPopupPrivate *self) {
  return self->QQuickPopupPrivate::getPositioner();
}

//  void QQuickPopupPrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickPopupPrivate13itemDestroyedEP10QQuickItem(
    QQuickPopupPrivate *self,
    QQuickItem *item) {
  self->QQuickPopupPrivate::itemDestroyed(item);
}

//  QPalette QQuickPopupPrivate::defaultPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_own_ZNK18QQuickPopupPrivate14defaultPaletteEv(
    const QQuickPopupPrivate *self) {
  return new QPalette(self->QQuickPopupPrivate::defaultPalette());
}

//  void QQuickPopupPrivate::updateChildrenPalettes(const QPalette
//      &parentPalette)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickPopupPrivate22updateChildrenPalettesERK8QPalette(
    QQuickPopupPrivate *self,
    const QPalette *parentPalette) {
  self->QQuickPopupPrivate::updateChildrenPalettes(*parentPalette);
}
