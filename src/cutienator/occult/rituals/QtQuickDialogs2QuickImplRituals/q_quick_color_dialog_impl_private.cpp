//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickcolordialogimpl_
//  p_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickcolordialogimpl_p.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickcolordialogimpl_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qeventpoint.h>
#include <QtCore/qpoint.h>
#include <QtGui/qpalette.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/private/qquickcolordialogimpl_p.h>
#include <QtQuickDialogs2QuickImpl/private/qquickcolordialogimpl_p_p.h>
#include <QtQuickDialogs2QuickImpl/private/qquickcolordialogutils_p.h>
#include <QtQuickTemplates2/private/qquickslider_p.h>
#include <QtGui/qpa/qplatformintegration.h>
#include <QtGui/qpa/qplatformservices.h>
#include <QtGui/private/qguiapplication_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickcolordialogimpl.cpp, line 67, as _ZN28QQuickColorDialogImplPrivateD1Ev
inline QQuickColorDialogImplPrivate::~QQuickColorDialogImplPrivate()
{
    if (m_eyeDropperMode)
        eyeDropperLeave(QCursor::pos(), QQuickEyeDropperEventFilter::LeaveReason::Default);
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickcolordialogimpl.cpp, line 84, as _ZN28QQuickColorDialogImplPrivate14attachedOrWarnEv
inline QQuickColorDialogImplAttached *QQuickColorDialogImplPrivate::attachedOrWarn()
{
    Q_Q(QQuickColorDialogImpl);
    QQuickColorDialogImplAttached *attached = static_cast<QQuickColorDialogImplAttached *>(
            qmlAttachedPropertiesObject<QQuickColorDialogImpl>(q, false));
    if (!attached)
        qmlWarning(q) << "Expected ColorDialogImpl attached object to be present on" << this;
    return attached;
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickcolordialogimpl.cpp, line 73, as _ZN28QQuickColorDialogImplPrivate11handleClickEP20QQuickAbstractButton
inline void QQuickColorDialogImplPrivate::handleClick(QQuickAbstractButton *button)
{
    Q_Q(QQuickColorDialogImpl);
    const auto c = q->color();
    if (buttonRole(button) == QPlatformDialogHelper::AcceptRole && c.isValid()) {
        q->setColor(c);
        q->accept();
    }
    QQuickDialogPrivate::handleClick(button);
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickcolordialogimpl.cpp, line 174, as _ZN28QQuickColorDialogImplPrivate16alphaSliderMovedEv
inline void QQuickColorDialogImplPrivate::alphaSliderMoved()
{
    Q_Q(QQuickColorDialogImpl);
    if (auto attached = attachedOrWarn())
        q->setAlpha(attached->alphaSlider()->value());
}
//  -----------------------------------------------------------------------

//  A QQuickColorDialogImplPrivate that Python can take functions over in. Every QQuickColorDialogImplPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickColorDialogImplPrivateCall0)(const void *, QQuickAbstractButton *, int *);
typedef void (*CuteQQuickColorDialogImplPrivateCall1)(const void *, int *);
typedef void (*CuteQQuickColorDialogImplPrivateCall2)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickColorDialogImplPrivateCall3)(const void *, const QEventPoint *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickColorDialogImplPrivateCall4)(const void *, QQuickItem *, const QPointF *, int *);
typedef bool (*CuteQQuickColorDialogImplPrivateCall5)(const void *, QQuickItem *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickColorDialogImplPrivateCall6)(const void *, QQuickItem *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickColorDialogImplPrivateCall7)(const void *, QQuickItem *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickColorDialogImplPrivateCall8)(const void *, const QEventPoint *, int *);
typedef void (*CuteQQuickColorDialogImplPrivateCall9)(const void *, int *);
typedef int (*CuteQQuickColorDialogImplPrivateCall10)(const void *, int *);
typedef void (*CuteQQuickColorDialogImplPrivateCall11)(const void *, int *);
typedef void (*CuteQQuickColorDialogImplPrivateCall12)(const void *, int *);
typedef void (*CuteQQuickColorDialogImplPrivateCall13)(const void *, int *);
typedef bool (*CuteQQuickColorDialogImplPrivateCall14)(const void *, int *);
typedef bool (*CuteQQuickColorDialogImplPrivateCall15)(const void *, int *);
typedef void (*CuteQQuickColorDialogImplPrivateCall16)(const void *, int *);
typedef void (*CuteQQuickColorDialogImplPrivateCall17)(const void *, int *);
typedef void (*CuteQQuickColorDialogImplPrivateCall18)(const void *, int *);
typedef void * (*CuteQQuickColorDialogImplPrivateCall19)(const void *, int *);
typedef void (*CuteQQuickColorDialogImplPrivateCall20)(const void *, QQuickItem *, int *);
typedef const QPalette * (*CuteQQuickColorDialogImplPrivateCall21)(const void *, int *);
typedef void (*CuteQQuickColorDialogImplPrivateCall22)(const void *, const QPalette *, int *);
class CuteQQuickColorDialogImplPrivate : public QQuickColorDialogImplPrivate {
public:
  using QQuickColorDialogImplPrivate::QQuickColorDialogImplPrivate;
  void *taken[23] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QQuickDialogPrivate11handleClickEP20QQuickAbstractButton")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickDialogPrivate12handleAcceptEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickDialogPrivate12handleRejectEv")) {
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

  //  void QQuickColorDialogImplPrivate::handleClick(QQuickAbstractButton
  //      *button)
  void handleClick(QQuickAbstractButton *button) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickColorDialogImplPrivateCall0 call = reinterpret_cast<CuteQQuickColorDialogImplPrivateCall0>(taken[0]);
      call(this, button, &handled);
      if (handled) return;
    }
    QQuickColorDialogImplPrivate::handleClick(button);
  }

  //  void QQuickDialogPrivate::handleAccept()
  void handleAccept() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickColorDialogImplPrivateCall1 call = reinterpret_cast<CuteQQuickColorDialogImplPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickDialogPrivate::handleAccept();
  }

  //  void QQuickDialogPrivate::handleReject()
  void handleReject() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickColorDialogImplPrivateCall2 call = reinterpret_cast<CuteQQuickColorDialogImplPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickDialogPrivate::handleReject();
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  bool QQuickPopupPrivate::acceptTouch(const QTouchEvent::TouchPoint
  //      &point)
  bool acceptTouch(const QTouchEvent::TouchPoint &point) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickColorDialogImplPrivateCall3 call = reinterpret_cast<CuteQQuickColorDialogImplPrivateCall3>(taken[3]);
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
      CuteQQuickColorDialogImplPrivateCall4 call = reinterpret_cast<CuteQQuickColorDialogImplPrivateCall4>(taken[4]);
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
      CuteQQuickColorDialogImplPrivateCall5 call = reinterpret_cast<CuteQQuickColorDialogImplPrivateCall5>(taken[5]);
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
      CuteQQuickColorDialogImplPrivateCall6 call = reinterpret_cast<CuteQQuickColorDialogImplPrivateCall6>(taken[6]);
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
      CuteQQuickColorDialogImplPrivateCall7 call = reinterpret_cast<CuteQQuickColorDialogImplPrivateCall7>(taken[7]);
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
      CuteQQuickColorDialogImplPrivateCall8 call = reinterpret_cast<CuteQQuickColorDialogImplPrivateCall8>(taken[8]);
      bool given = call(this, &a0, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::handleReleaseWithoutGrab(a0);
  }

  //  void QQuickPopupPrivate::handleUngrab()
  void handleUngrab() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickColorDialogImplPrivateCall9 call = reinterpret_cast<CuteQQuickColorDialogImplPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::handleUngrab();
  }

  //  QQuickPopup::PopupType QQuickPopupPrivate::resolvedPopupType() const
  QQuickPopup::PopupType resolvedPopupType() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickColorDialogImplPrivateCall10 call = reinterpret_cast<CuteQQuickColorDialogImplPrivateCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickPopup::PopupType>(given);
    }
    return QQuickPopupPrivate::resolvedPopupType();
  }

  //  void QQuickPopupPrivate::showDimmer()
  void showDimmer() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickColorDialogImplPrivateCall11 call = reinterpret_cast<CuteQQuickColorDialogImplPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::showDimmer();
  }

  //  void QQuickPopupPrivate::hideDimmer()
  void hideDimmer() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickColorDialogImplPrivateCall12 call = reinterpret_cast<CuteQQuickColorDialogImplPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::hideDimmer();
  }

  //  void QQuickPopupPrivate::resizeDimmer()
  void resizeDimmer() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickColorDialogImplPrivateCall13 call = reinterpret_cast<CuteQQuickColorDialogImplPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::resizeDimmer();
  }

  //  bool QQuickPopupPrivate::prepareEnterTransition()
  bool prepareEnterTransition() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickColorDialogImplPrivateCall14 call = reinterpret_cast<CuteQQuickColorDialogImplPrivateCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::prepareEnterTransition();
  }

  //  bool QQuickPopupPrivate::prepareExitTransition()
  bool prepareExitTransition() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickColorDialogImplPrivateCall15 call = reinterpret_cast<CuteQQuickColorDialogImplPrivateCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::prepareExitTransition();
  }

  //  void QQuickPopupPrivate::finalizeEnterTransition()
  void finalizeEnterTransition() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickColorDialogImplPrivateCall16 call = reinterpret_cast<CuteQQuickColorDialogImplPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::finalizeEnterTransition();
  }

  //  void QQuickPopupPrivate::finalizeExitTransition()
  void finalizeExitTransition() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickColorDialogImplPrivateCall17 call = reinterpret_cast<CuteQQuickColorDialogImplPrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::finalizeExitTransition();
  }

  //  void QQuickPopupPrivate::opened()
  void opened() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickColorDialogImplPrivateCall18 call = reinterpret_cast<CuteQQuickColorDialogImplPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::opened();
  }

  //  QQuickPopupPositioner *QQuickPopupPrivate::getPositioner()
  QQuickPopupPositioner *getPositioner() override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickColorDialogImplPrivateCall19 call = reinterpret_cast<CuteQQuickColorDialogImplPrivateCall19>(taken[19]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickPopupPositioner *>(given);
    }
    return QQuickPopupPrivate::getPositioner();
  }

  //  void QQuickPopupPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickColorDialogImplPrivateCall20 call = reinterpret_cast<CuteQQuickColorDialogImplPrivateCall20>(taken[20]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::itemDestroyed(item);
  }

  //  QPalette QQuickPopupPrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickColorDialogImplPrivateCall21 call = reinterpret_cast<CuteQQuickColorDialogImplPrivateCall21>(taken[21]);
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
      CuteQQuickColorDialogImplPrivateCall22 call = reinterpret_cast<CuteQQuickColorDialogImplPrivateCall22>(taken[22]);
      call(this, &parentPalette, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::updateChildrenPalettes(parentPalette);
  }
};

//  QQuickColorDialogImpl *QQuickColorDialogImplPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickColorDialogImpl *ritual_ZN28QQuickColorDialogImplPrivate6q_funcEv(
    QQuickColorDialogImplPrivate *self) {
  return self->q_func();
}

//  const QQuickColorDialogImpl *QQuickColorDialogImplPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickColorDialogImpl *ritual_ZNK28QQuickColorDialogImplPrivate6q_funcEv(
    const QQuickColorDialogImplPrivate *self) {
  return self->q_func();
}

//  QQuickColorDialogImplPrivate::~QQuickColorDialogImplPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickColorDialogImplPrivateD1Ev(
    QQuickColorDialogImplPrivate *self) {
  delete self;
}

//  QQuickColorDialogImplPrivate
//      *QQuickColorDialogImplPrivate::get(QQuickColorDialogImpl *dialog)
extern "C" Q_DECL_EXPORT
QQuickColorDialogImplPrivate *ritual_ZN28QQuickColorDialogImplPrivate3getEP21QQuickColorDialogImpl(
    QQuickColorDialogImpl *dialog) {
  return QQuickColorDialogImplPrivate::get(dialog);
}

//  QQuickColorDialogImplAttached
//      *QQuickColorDialogImplPrivate::attachedOrWarn()
extern "C" Q_DECL_EXPORT
QQuickColorDialogImplAttached *ritual_ZN28QQuickColorDialogImplPrivate14attachedOrWarnEv(
    QQuickColorDialogImplPrivate *self) {
  return self->attachedOrWarn();
}

//  void QQuickColorDialogImplPrivate::handleClick(QQuickAbstractButton
//      *button)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickColorDialogImplPrivate11handleClickEP20QQuickAbstractButton(
    QQuickColorDialogImplPrivate *self,
    QQuickAbstractButton *button) {
  self->handleClick(button);
}

//  void QQuickColorDialogImplPrivate::alphaSliderMoved()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickColorDialogImplPrivate16alphaSliderMovedEv(
    QQuickColorDialogImplPrivate *self) {
  self->alphaSliderMoved();
}

//  a Python function taken by a CuteQQuickColorDialogImplPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickColorDialogImplPrivate(
    QQuickColorDialogImplPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickColorDialogImplPrivate *>(self)->take(key, call);
}

//  void QQuickColorDialogImplPrivate::handleClick(QQuickAbstractButton
//      *button)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuickColorDialogImplPrivate11handleClickEP20QQuickAbstractButton(
    QQuickColorDialogImplPrivate *self,
    QQuickAbstractButton *button) {
  self->QQuickColorDialogImplPrivate::handleClick(button);
}
