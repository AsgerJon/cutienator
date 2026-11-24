//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdrawer_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdrawer_p.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdrawer_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/qeventpoint.h>
#include <QtGui/qpalette.h>
#include <cstring>

//  A QQuickDrawerPrivate that Python can take functions over in. Every QQuickDrawerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuickDrawerPrivateCall0)(const void *, int *);
typedef void (*CuteQQuickDrawerPrivateCall1)(const void *, int *);
typedef void (*CuteQQuickDrawerPrivateCall2)(const void *, int *);
typedef void (*CuteQQuickDrawerPrivateCall3)(const void *, int *);
typedef bool (*CuteQQuickDrawerPrivateCall4)(const void *, QQuickItem *, const QPointF *, int *);
typedef bool (*CuteQQuickDrawerPrivateCall5)(const void *, QQuickItem *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickDrawerPrivateCall6)(const void *, QQuickItem *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickDrawerPrivateCall7)(const void *, QQuickItem *, const QPointF *, ulong, int *);
typedef void (*CuteQQuickDrawerPrivateCall8)(const void *, int *);
typedef bool (*CuteQQuickDrawerPrivateCall9)(const void *, int *);
typedef bool (*CuteQQuickDrawerPrivateCall10)(const void *, int *);
typedef int (*CuteQQuickDrawerPrivateCall11)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickDrawerPrivateCall12)(const void *, const QEventPoint *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickDrawerPrivateCall13)(const void *, const QEventPoint *, int *);
typedef void (*CuteQQuickDrawerPrivateCall14)(const void *, int *);
typedef void (*CuteQQuickDrawerPrivateCall15)(const void *, int *);
typedef void (*CuteQQuickDrawerPrivateCall16)(const void *, int *);
typedef void (*CuteQQuickDrawerPrivateCall17)(const void *, QQuickItem *, int *);
typedef const QPalette * (*CuteQQuickDrawerPrivateCall18)(const void *, int *);
typedef void (*CuteQQuickDrawerPrivateCall19)(const void *, const QPalette *, int *);
class CuteQQuickDrawerPrivate : public QQuickDrawerPrivate {
public:
  using QQuickDrawerPrivate::QQuickDrawerPrivate;
  void *taken[20] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate13getPositionerEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate10showDimmerEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate10hideDimmerEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate12resizeDimmerEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QQuickPopupPrivate10blockInputEP10QQuickItemRK7QPointF")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate11handlePressEP10QQuickItemRK7QPointFm")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate10handleMoveEP10QQuickItemRK7QPointFm")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate13handleReleaseEP10QQuickItemRK7QPointFm")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate12handleUngrabEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate22prepareEnterTransitionEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate21prepareExitTransitionEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QQuickPopupPrivate17resolvedPopupTypeEv")) {
      taken[11] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate11acceptTouchERK11QEventPoint")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate24handleReleaseWithoutGrabERK11QEventPoint")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate23finalizeEnterTransitionEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate22finalizeExitTransitionEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate6openedEv")) {
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

  //  QQuickPopupPositioner *QQuickDrawerPrivate::getPositioner()
  QQuickPopupPositioner *getPositioner() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickDrawerPrivateCall0 call = reinterpret_cast<CuteQQuickDrawerPrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickPopupPositioner *>(given);
    }
    return QQuickDrawerPrivate::getPositioner();
  }

  //  void QQuickDrawerPrivate::showDimmer()
  void showDimmer() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickDrawerPrivateCall1 call = reinterpret_cast<CuteQQuickDrawerPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickDrawerPrivate::showDimmer();
  }

  //  void QQuickDrawerPrivate::hideDimmer()
  void hideDimmer() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickDrawerPrivateCall2 call = reinterpret_cast<CuteQQuickDrawerPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickDrawerPrivate::hideDimmer();
  }

  //  void QQuickDrawerPrivate::resizeDimmer()
  void resizeDimmer() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickDrawerPrivateCall3 call = reinterpret_cast<CuteQQuickDrawerPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickDrawerPrivate::resizeDimmer();
  }

  //  bool QQuickDrawerPrivate::blockInput(QQuickItem *item, const QPointF
  //      &point) const
  bool blockInput(QQuickItem *item, const QPointF &point) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickDrawerPrivateCall4 call = reinterpret_cast<CuteQQuickDrawerPrivateCall4>(taken[4]);
      bool given = call(this, item, &point, &handled);
      if (handled) return given;
    }
    return QQuickDrawerPrivate::blockInput(item, point);
  }

  //  bool QQuickDrawerPrivate::handlePress(QQuickItem *item, const QPointF
  //      &point, ulong timestamp)
  bool handlePress(
      QQuickItem *item,
      const QPointF &point,
      ulong timestamp) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickDrawerPrivateCall5 call = reinterpret_cast<CuteQQuickDrawerPrivateCall5>(taken[5]);
      bool given = call(this, item, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickDrawerPrivate::handlePress(item, point, timestamp);
  }

  //  bool QQuickDrawerPrivate::handleMove(QQuickItem *item, const QPointF
  //      &point, ulong timestamp)
  bool handleMove(
      QQuickItem *item,
      const QPointF &point,
      ulong timestamp) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickDrawerPrivateCall6 call = reinterpret_cast<CuteQQuickDrawerPrivateCall6>(taken[6]);
      bool given = call(this, item, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickDrawerPrivate::handleMove(item, point, timestamp);
  }

  //  bool QQuickDrawerPrivate::handleRelease(QQuickItem *item, const
  //      QPointF &point, ulong timestamp)
  bool handleRelease(
      QQuickItem *item,
      const QPointF &point,
      ulong timestamp) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickDrawerPrivateCall7 call = reinterpret_cast<CuteQQuickDrawerPrivateCall7>(taken[7]);
      bool given = call(this, item, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickDrawerPrivate::handleRelease(item, point, timestamp);
  }

  //  void QQuickDrawerPrivate::handleUngrab()
  void handleUngrab() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickDrawerPrivateCall8 call = reinterpret_cast<CuteQQuickDrawerPrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickDrawerPrivate::handleUngrab();
  }

  //  bool QQuickDrawerPrivate::prepareEnterTransition()
  bool prepareEnterTransition() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickDrawerPrivateCall9 call = reinterpret_cast<CuteQQuickDrawerPrivateCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickDrawerPrivate::prepareEnterTransition();
  }

  //  bool QQuickDrawerPrivate::prepareExitTransition()
  bool prepareExitTransition() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickDrawerPrivateCall10 call = reinterpret_cast<CuteQQuickDrawerPrivateCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickDrawerPrivate::prepareExitTransition();
  }

  //  QQuickPopup::PopupType QQuickDrawerPrivate::resolvedPopupType() const
  QQuickPopup::PopupType resolvedPopupType() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickDrawerPrivateCall11 call = reinterpret_cast<CuteQQuickDrawerPrivateCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickPopup::PopupType>(given);
    }
    return QQuickDrawerPrivate::resolvedPopupType();
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  bool QQuickPopupPrivate::acceptTouch(const QTouchEvent::TouchPoint
  //      &point)
  bool acceptTouch(const QTouchEvent::TouchPoint &point) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickDrawerPrivateCall12 call = reinterpret_cast<CuteQQuickDrawerPrivateCall12>(taken[12]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::acceptTouch(point);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

  //  bool QQuickPopupPrivate::handleReleaseWithoutGrab(const QEventPoint
  //      &a0)
  bool handleReleaseWithoutGrab(const QEventPoint &a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickDrawerPrivateCall13 call = reinterpret_cast<CuteQQuickDrawerPrivateCall13>(taken[13]);
      bool given = call(this, &a0, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::handleReleaseWithoutGrab(a0);
  }

  //  void QQuickPopupPrivate::finalizeEnterTransition()
  void finalizeEnterTransition() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickDrawerPrivateCall14 call = reinterpret_cast<CuteQQuickDrawerPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::finalizeEnterTransition();
  }

  //  void QQuickPopupPrivate::finalizeExitTransition()
  void finalizeExitTransition() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickDrawerPrivateCall15 call = reinterpret_cast<CuteQQuickDrawerPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::finalizeExitTransition();
  }

  //  void QQuickPopupPrivate::opened()
  void opened() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickDrawerPrivateCall16 call = reinterpret_cast<CuteQQuickDrawerPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::opened();
  }

  //  void QQuickPopupPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickDrawerPrivateCall17 call = reinterpret_cast<CuteQQuickDrawerPrivateCall17>(taken[17]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::itemDestroyed(item);
  }

  //  QPalette QQuickPopupPrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickDrawerPrivateCall18 call = reinterpret_cast<CuteQQuickDrawerPrivateCall18>(taken[18]);
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
      CuteQQuickDrawerPrivateCall19 call = reinterpret_cast<CuteQQuickDrawerPrivateCall19>(taken[19]);
      call(this, &parentPalette, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::updateChildrenPalettes(parentPalette);
  }
};

//  QQuickDrawer *QQuickDrawerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickDrawer *ritual_ZN19QQuickDrawerPrivate6q_funcEv(
    QQuickDrawerPrivate *self) {
  return self->q_func();
}

//  const QQuickDrawer *QQuickDrawerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickDrawer *ritual_ZNK19QQuickDrawerPrivate6q_funcEv(
    const QQuickDrawerPrivate *self) {
  return self->q_func();
}

//  QQuickDrawerPrivate *QQuickDrawerPrivate::get(QQuickDrawer *drawer)
extern "C" Q_DECL_EXPORT
QQuickDrawerPrivate *ritual_ZN19QQuickDrawerPrivate3getEP12QQuickDrawer(
    QQuickDrawer *drawer) {
  return QQuickDrawerPrivate::get(drawer);
}

//  qreal QQuickDrawerPrivate::offsetAt(const QPointF &point) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQuickDrawerPrivate8offsetAtERK7QPointF(
    const QQuickDrawerPrivate *self,
    const QPointF *point) {
  return self->offsetAt(*point);
}

//  qreal QQuickDrawerPrivate::positionAt(const QPointF &point) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQuickDrawerPrivate10positionAtERK7QPointF(
    const QQuickDrawerPrivate *self,
    const QPointF *point) {
  return self->positionAt(*point);
}

//  QQuickPopupPositioner *QQuickDrawerPrivate::getPositioner()
extern "C" Q_DECL_EXPORT
QQuickPopupPositioner *ritual_ZN19QQuickDrawerPrivate13getPositionerEv(
    QQuickDrawerPrivate *self) {
  return self->getPositioner();
}

//  void QQuickDrawerPrivate::showDimmer()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDrawerPrivate10showDimmerEv(
    QQuickDrawerPrivate *self) {
  self->showDimmer();
}

//  void QQuickDrawerPrivate::hideDimmer()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDrawerPrivate10hideDimmerEv(
    QQuickDrawerPrivate *self) {
  self->hideDimmer();
}

//  void QQuickDrawerPrivate::resizeDimmer()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDrawerPrivate12resizeDimmerEv(
    QQuickDrawerPrivate *self) {
  self->resizeDimmer();
}

//  bool QQuickDrawerPrivate::startDrag(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickDrawerPrivate9startDragEP6QEvent(
    QQuickDrawerPrivate *self,
    QEvent *event) {
  return self->startDrag(event);
}

//  bool QQuickDrawerPrivate::grabMouse(QQuickItem *item, QMouseEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickDrawerPrivate9grabMouseEP10QQuickItemP11QMouseEvent(
    QQuickDrawerPrivate *self,
    QQuickItem *item,
    QMouseEvent *event) {
  return self->grabMouse(item, event);
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  bool QQuickDrawerPrivate::grabTouch(QQuickItem *item, QTouchEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickDrawerPrivate9grabTouchEP10QQuickItemP11QTouchEvent(
    QQuickDrawerPrivate *self,
    QQuickItem *item,
    QTouchEvent *event) {
  return self->grabTouch(item, event);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

//  bool QQuickDrawerPrivate::blockInput(QQuickItem *item, const QPointF
//      &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickDrawerPrivate10blockInputEP10QQuickItemRK7QPointF(
    const QQuickDrawerPrivate *self,
    QQuickItem *item,
    const QPointF *point) {
  return self->blockInput(item, *point);
}

//  bool QQuickDrawerPrivate::handlePress(QQuickItem *item, const QPointF
//      &point, ulong timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickDrawerPrivate11handlePressEP10QQuickItemRK7QPointFm(
    QQuickDrawerPrivate *self,
    QQuickItem *item,
    const QPointF *point,
    ulong timestamp) {
  return self->handlePress(item, *point, timestamp);
}

//  bool QQuickDrawerPrivate::handleMove(QQuickItem *item, const QPointF
//      &point, ulong timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickDrawerPrivate10handleMoveEP10QQuickItemRK7QPointFm(
    QQuickDrawerPrivate *self,
    QQuickItem *item,
    const QPointF *point,
    ulong timestamp) {
  return self->handleMove(item, *point, timestamp);
}

//  bool QQuickDrawerPrivate::handleRelease(QQuickItem *item, const QPointF
//      &point, ulong timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickDrawerPrivate13handleReleaseEP10QQuickItemRK7QPointFm(
    QQuickDrawerPrivate *self,
    QQuickItem *item,
    const QPointF *point,
    ulong timestamp) {
  return self->handleRelease(item, *point, timestamp);
}

//  void QQuickDrawerPrivate::handleUngrab()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDrawerPrivate12handleUngrabEv(
    QQuickDrawerPrivate *self) {
  self->handleUngrab();
}

//  bool QQuickDrawerPrivate::prepareEnterTransition()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickDrawerPrivate22prepareEnterTransitionEv(
    QQuickDrawerPrivate *self) {
  return self->prepareEnterTransition();
}

//  bool QQuickDrawerPrivate::prepareExitTransition()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickDrawerPrivate21prepareExitTransitionEv(
    QQuickDrawerPrivate *self) {
  return self->prepareExitTransition();
}

//  QQuickPopup::PopupType QQuickDrawerPrivate::resolvedPopupType() const
extern "C" Q_DECL_EXPORT
QQuickPopup::PopupType ritual_ZNK19QQuickDrawerPrivate17resolvedPopupTypeEv(
    const QQuickDrawerPrivate *self) {
  return self->resolvedPopupType();
}

//  bool QQuickDrawerPrivate::setEdge(Qt::Edge edge)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickDrawerPrivate7setEdgeEN2Qt4EdgeE(
    QQuickDrawerPrivate *self,
    Qt::Edge edge) {
  return self->setEdge(edge);
}

//  Qt::Edge QQuickDrawerPrivate::effectiveEdge() const
extern "C" Q_DECL_EXPORT
Qt::Edge ritual_ZNK19QQuickDrawerPrivate13effectiveEdgeEv(
    const QQuickDrawerPrivate *self) {
  return self->effectiveEdge();
}

//  bool QQuickDrawerPrivate::isWithinDragMargin(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickDrawerPrivate18isWithinDragMarginERK7QPointF(
    const QQuickDrawerPrivate *self,
    const QPointF *point) {
  return self->isWithinDragMargin(*point);
}

//  a Python function taken by a CuteQQuickDrawerPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickDrawerPrivate(
    QQuickDrawerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickDrawerPrivate *>(self)->take(key, call);
}

//  QQuickPopupPositioner *QQuickDrawerPrivate::getPositioner()
extern "C" Q_DECL_EXPORT
QQuickPopupPositioner *ritual_own_ZN19QQuickDrawerPrivate13getPositionerEv(
    QQuickDrawerPrivate *self) {
  return self->QQuickDrawerPrivate::getPositioner();
}

//  void QQuickDrawerPrivate::showDimmer()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickDrawerPrivate10showDimmerEv(
    QQuickDrawerPrivate *self) {
  self->QQuickDrawerPrivate::showDimmer();
}

//  void QQuickDrawerPrivate::hideDimmer()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickDrawerPrivate10hideDimmerEv(
    QQuickDrawerPrivate *self) {
  self->QQuickDrawerPrivate::hideDimmer();
}

//  void QQuickDrawerPrivate::resizeDimmer()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickDrawerPrivate12resizeDimmerEv(
    QQuickDrawerPrivate *self) {
  self->QQuickDrawerPrivate::resizeDimmer();
}

//  bool QQuickDrawerPrivate::blockInput(QQuickItem *item, const QPointF
//      &point) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QQuickDrawerPrivate10blockInputEP10QQuickItemRK7QPointF(
    const QQuickDrawerPrivate *self,
    QQuickItem *item,
    const QPointF *point) {
  return self->QQuickDrawerPrivate::blockInput(item, *point);
}

//  bool QQuickDrawerPrivate::handlePress(QQuickItem *item, const QPointF
//      &point, ulong timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQuickDrawerPrivate11handlePressEP10QQuickItemRK7QPointFm(
    QQuickDrawerPrivate *self,
    QQuickItem *item,
    const QPointF *point,
    ulong timestamp) {
  return self->QQuickDrawerPrivate::handlePress(item, *point, timestamp);
}

//  bool QQuickDrawerPrivate::handleMove(QQuickItem *item, const QPointF
//      &point, ulong timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQuickDrawerPrivate10handleMoveEP10QQuickItemRK7QPointFm(
    QQuickDrawerPrivate *self,
    QQuickItem *item,
    const QPointF *point,
    ulong timestamp) {
  return self->QQuickDrawerPrivate::handleMove(item, *point, timestamp);
}

//  bool QQuickDrawerPrivate::handleRelease(QQuickItem *item, const QPointF
//      &point, ulong timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQuickDrawerPrivate13handleReleaseEP10QQuickItemRK7QPointFm(
    QQuickDrawerPrivate *self,
    QQuickItem *item,
    const QPointF *point,
    ulong timestamp) {
  return self->QQuickDrawerPrivate::handleRelease(item, *point, timestamp);
}

//  void QQuickDrawerPrivate::handleUngrab()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickDrawerPrivate12handleUngrabEv(
    QQuickDrawerPrivate *self) {
  self->QQuickDrawerPrivate::handleUngrab();
}

//  bool QQuickDrawerPrivate::prepareEnterTransition()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQuickDrawerPrivate22prepareEnterTransitionEv(
    QQuickDrawerPrivate *self) {
  return self->QQuickDrawerPrivate::prepareEnterTransition();
}

//  bool QQuickDrawerPrivate::prepareExitTransition()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QQuickDrawerPrivate21prepareExitTransitionEv(
    QQuickDrawerPrivate *self) {
  return self->QQuickDrawerPrivate::prepareExitTransition();
}

//  QQuickPopup::PopupType QQuickDrawerPrivate::resolvedPopupType() const
extern "C" Q_DECL_EXPORT
QQuickPopup::PopupType ritual_own_ZNK19QQuickDrawerPrivate17resolvedPopupTypeEv(
    const QQuickDrawerPrivate *self) {
  return self->QQuickDrawerPrivate::resolvedPopupType();
}
