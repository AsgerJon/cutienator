//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdialog_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_container)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdialog_p.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdialog_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qeventpoint.h>
#include <QtCore/qpoint.h>
#include <QtGui/qpalette.h>
#include <cstring>

//  A QQuickDialogPrivate that Python can take functions over in. Every QQuickDialogPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickDialogPrivateCall0)(const void *, int *);
typedef void (*CuteQQuickDialogPrivateCall1)(const void *, int *);
typedef void (*CuteQQuickDialogPrivateCall2)(const void *, QQuickAbstractButton *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickDialogPrivateCall3)(const void *, const QEventPoint *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickDialogPrivateCall4)(const void *, QQuickItem *, const QPointF *, int *);
typedef bool (*CuteQQuickDialogPrivateCall5)(const void *, QQuickItem *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickDialogPrivateCall6)(const void *, QQuickItem *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickDialogPrivateCall7)(const void *, QQuickItem *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickDialogPrivateCall8)(const void *, const QEventPoint *, int *);
typedef void (*CuteQQuickDialogPrivateCall9)(const void *, int *);
typedef int (*CuteQQuickDialogPrivateCall10)(const void *, int *);
typedef void (*CuteQQuickDialogPrivateCall11)(const void *, int *);
typedef void (*CuteQQuickDialogPrivateCall12)(const void *, int *);
typedef void (*CuteQQuickDialogPrivateCall13)(const void *, int *);
typedef bool (*CuteQQuickDialogPrivateCall14)(const void *, int *);
typedef bool (*CuteQQuickDialogPrivateCall15)(const void *, int *);
typedef void (*CuteQQuickDialogPrivateCall16)(const void *, int *);
typedef void (*CuteQQuickDialogPrivateCall17)(const void *, int *);
typedef void (*CuteQQuickDialogPrivateCall18)(const void *, int *);
typedef void * (*CuteQQuickDialogPrivateCall19)(const void *, int *);
typedef void (*CuteQQuickDialogPrivateCall20)(const void *, QQuickItem *, int *);
typedef const QPalette * (*CuteQQuickDialogPrivateCall21)(const void *, int *);
typedef void (*CuteQQuickDialogPrivateCall22)(const void *, const QPalette *, int *);
class CuteQQuickDialogPrivate : public QQuickDialogPrivate {
public:
  using QQuickDialogPrivate::QQuickDialogPrivate;
  void *taken[23] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QQuickDialogPrivate12handleAcceptEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickDialogPrivate12handleRejectEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickDialogPrivate11handleClickEP20QQuickAbstractButton")) {
      taken[2] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate11acceptTouchERK11QEventPoint")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
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
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate24handleReleaseWithoutGrabERK11QEventPoint")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate12handleUngrabEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QQuickPopupPrivate17resolvedPopupTypeEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate10showDimmerEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate10hideDimmerEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate12resizeDimmerEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate22prepareEnterTransitionEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate21prepareExitTransitionEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate23finalizeEnterTransitionEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate22finalizeExitTransitionEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate6openedEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate13getPositionerEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate13itemDestroyedEP10QQuickItem")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QQuickPopupPrivate14defaultPaletteEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickPopupPrivate22updateChildrenPalettesERK8QPalette")) {
      taken[22] = call;
      return true;
    }
    return false;
  }

  //  void QQuickDialogPrivate::handleAccept()
  void handleAccept() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickDialogPrivateCall0 call = reinterpret_cast<CuteQQuickDialogPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickDialogPrivate::handleAccept();
  }

  //  void QQuickDialogPrivate::handleReject()
  void handleReject() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickDialogPrivateCall1 call = reinterpret_cast<CuteQQuickDialogPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickDialogPrivate::handleReject();
  }

  //  void QQuickDialogPrivate::handleClick(QQuickAbstractButton *button)
  void handleClick(QQuickAbstractButton *button) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickDialogPrivateCall2 call = reinterpret_cast<CuteQQuickDialogPrivateCall2>(taken[2]);
      call(this, button, &handled);
      if (handled) return;
    }
    QQuickDialogPrivate::handleClick(button);
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  bool QQuickPopupPrivate::acceptTouch(const QTouchEvent::TouchPoint
  //      &point)
  bool acceptTouch(const QTouchEvent::TouchPoint &point) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickDialogPrivateCall3 call = reinterpret_cast<CuteQQuickDialogPrivateCall3>(taken[3]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::acceptTouch(point);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

  //  bool QQuickPopupPrivate::blockInput(QQuickItem *item, const QPointF
  //      &point) const
  bool blockInput(QQuickItem *item, const QPointF &point) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickDialogPrivateCall4 call = reinterpret_cast<CuteQQuickDialogPrivateCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQQuickDialogPrivateCall5 call = reinterpret_cast<CuteQQuickDialogPrivateCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQQuickDialogPrivateCall6 call = reinterpret_cast<CuteQQuickDialogPrivateCall6>(taken[6]);
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
    if (taken[7]) {
      int handled = 0;
      CuteQQuickDialogPrivateCall7 call = reinterpret_cast<CuteQQuickDialogPrivateCall7>(taken[7]);
      bool given = call(this, item, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::handleRelease(item, point, timestamp);
  }

  //  bool QQuickPopupPrivate::handleReleaseWithoutGrab(const QEventPoint
  //      &a0)
  bool handleReleaseWithoutGrab(const QEventPoint &a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickDialogPrivateCall8 call = reinterpret_cast<CuteQQuickDialogPrivateCall8>(taken[8]);
      bool given = call(this, &a0, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::handleReleaseWithoutGrab(a0);
  }

  //  void QQuickPopupPrivate::handleUngrab()
  void handleUngrab() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickDialogPrivateCall9 call = reinterpret_cast<CuteQQuickDialogPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::handleUngrab();
  }

  //  QQuickPopup::PopupType QQuickPopupPrivate::resolvedPopupType() const
  QQuickPopup::PopupType resolvedPopupType() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickDialogPrivateCall10 call = reinterpret_cast<CuteQQuickDialogPrivateCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickPopup::PopupType>(given);
    }
    return QQuickPopupPrivate::resolvedPopupType();
  }

  //  void QQuickPopupPrivate::showDimmer()
  void showDimmer() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickDialogPrivateCall11 call = reinterpret_cast<CuteQQuickDialogPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::showDimmer();
  }

  //  void QQuickPopupPrivate::hideDimmer()
  void hideDimmer() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickDialogPrivateCall12 call = reinterpret_cast<CuteQQuickDialogPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::hideDimmer();
  }

  //  void QQuickPopupPrivate::resizeDimmer()
  void resizeDimmer() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickDialogPrivateCall13 call = reinterpret_cast<CuteQQuickDialogPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::resizeDimmer();
  }

  //  bool QQuickPopupPrivate::prepareEnterTransition()
  bool prepareEnterTransition() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickDialogPrivateCall14 call = reinterpret_cast<CuteQQuickDialogPrivateCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::prepareEnterTransition();
  }

  //  bool QQuickPopupPrivate::prepareExitTransition()
  bool prepareExitTransition() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickDialogPrivateCall15 call = reinterpret_cast<CuteQQuickDialogPrivateCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::prepareExitTransition();
  }

  //  void QQuickPopupPrivate::finalizeEnterTransition()
  void finalizeEnterTransition() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickDialogPrivateCall16 call = reinterpret_cast<CuteQQuickDialogPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::finalizeEnterTransition();
  }

  //  void QQuickPopupPrivate::finalizeExitTransition()
  void finalizeExitTransition() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickDialogPrivateCall17 call = reinterpret_cast<CuteQQuickDialogPrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::finalizeExitTransition();
  }

  //  void QQuickPopupPrivate::opened()
  void opened() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickDialogPrivateCall18 call = reinterpret_cast<CuteQQuickDialogPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::opened();
  }

  //  QQuickPopupPositioner *QQuickPopupPrivate::getPositioner()
  QQuickPopupPositioner *getPositioner() override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickDialogPrivateCall19 call = reinterpret_cast<CuteQQuickDialogPrivateCall19>(taken[19]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickPopupPositioner *>(given);
    }
    return QQuickPopupPrivate::getPositioner();
  }

  //  void QQuickPopupPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickDialogPrivateCall20 call = reinterpret_cast<CuteQQuickDialogPrivateCall20>(taken[20]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::itemDestroyed(item);
  }

  //  QPalette QQuickPopupPrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickDialogPrivateCall21 call = reinterpret_cast<CuteQQuickDialogPrivateCall21>(taken[21]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickPopupPrivate::defaultPalette();
  }

  //  void QQuickPopupPrivate::updateChildrenPalettes(const QPalette
  //      &parentPalette)
  void updateChildrenPalettes(const QPalette &parentPalette) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickDialogPrivateCall22 call = reinterpret_cast<CuteQQuickDialogPrivateCall22>(taken[22]);
      call(this, &parentPalette, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::updateChildrenPalettes(parentPalette);
  }
};

//  QQuickDialog *QQuickDialogPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickDialog *ritual_ZN19QQuickDialogPrivate6q_funcEv(
    QQuickDialogPrivate *self) {
  return self->q_func();
}

//  const QQuickDialog *QQuickDialogPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickDialog *ritual_ZNK19QQuickDialogPrivate6q_funcEv(
    const QQuickDialogPrivate *self) {
  return self->q_func();
}

//  QQuickDialogPrivate::QQuickDialogPrivate()
extern "C" Q_DECL_EXPORT
QQuickDialogPrivate *ritual_ZN19QQuickDialogPrivateC1Ev() {
  return new CuteQQuickDialogPrivate();
}

//  QQuickDialogPrivate *QQuickDialogPrivate::get(QQuickDialog *dialog)
extern "C" Q_DECL_EXPORT
QQuickDialogPrivate *ritual_ZN19QQuickDialogPrivate3getEP12QQuickDialog(
    QQuickDialog *dialog) {
  return QQuickDialogPrivate::get(dialog);
}

//  QPlatformDialogHelper::ButtonRole
//      QQuickDialogPrivate::buttonRole(QQuickAbstractButton *button)
extern "C" Q_DECL_EXPORT
QPlatformDialogHelper::ButtonRole ritual_ZN19QQuickDialogPrivate10buttonRoleEP20QQuickAbstractButton(
    QQuickAbstractButton *button) {
  return QQuickDialogPrivate::buttonRole(button);
}

//  void QQuickDialogPrivate::handleAccept()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDialogPrivate12handleAcceptEv(
    QQuickDialogPrivate *self) {
  self->handleAccept();
}

//  void QQuickDialogPrivate::handleReject()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDialogPrivate12handleRejectEv(
    QQuickDialogPrivate *self) {
  self->handleReject();
}

//  void QQuickDialogPrivate::handleClick(QQuickAbstractButton *button)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickDialogPrivate11handleClickEP20QQuickAbstractButton(
    QQuickDialogPrivate *self,
    QQuickAbstractButton *button) {
  self->handleClick(button);
}

//  a Python function taken by a CuteQQuickDialogPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickDialogPrivate(
    QQuickDialogPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickDialogPrivate *>(self)->take(key, call);
}

//  void QQuickDialogPrivate::handleAccept()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickDialogPrivate12handleAcceptEv(
    QQuickDialogPrivate *self) {
  self->QQuickDialogPrivate::handleAccept();
}

//  void QQuickDialogPrivate::handleReject()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickDialogPrivate12handleRejectEv(
    QQuickDialogPrivate *self) {
  self->QQuickDialogPrivate::handleReject();
}

//  void QQuickDialogPrivate::handleClick(QQuickAbstractButton *button)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickDialogPrivate11handleClickEP20QQuickAbstractButton(
    QQuickDialogPrivate *self,
    QQuickAbstractButton *button) {
  self->QQuickDialogPrivate::handleClick(button);
}

#endif  // QT_CONFIG(quicktemplates2_container)
