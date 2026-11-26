//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickmessagedialogimp
//  l_p_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickmessagedialogimpl_p.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickmessagedialogimpl_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qeventpoint.h>
#include <QtCore/qpoint.h>
#include <QtGui/qpalette.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/private/qquickmessagedialogimpl_p.h>
#include <QtQuickDialogs2QuickImpl/private/qquickmessagedialogimpl_p_p.h>
#include <QtQuickTemplates2/private/qquickdialogbuttonbox_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickmessagedialogimpl.cpp, line 14, as _ZN30QQuickMessageDialogImplPrivate11handleClickEP20QQuickAbstractButton
inline void QQuickMessageDialogImplPrivate::handleClick(QQuickAbstractButton *button)
{
    Q_Q(QQuickMessageDialogImpl);

    if (const QQuickMessageDialogImplAttached *attached = attachedOrWarn()) {
        QPlatformDialogHelper::StandardButton standardButton =
                QQuickDialogButtonBoxPrivate::get(attached->buttonBox())->standardButton(button);
        QPlatformDialogHelper::ButtonRole role = buttonRole(button);

        emit q->buttonClicked(standardButton, role);
    }
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickmessagedialogimpl.cpp, line 12, as _ZN30QQuickMessageDialogImplPrivateC1Ev
inline QQuickMessageDialogImplPrivate::QQuickMessageDialogImplPrivate() { }

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickmessagedialogimpl.cpp, line 27, as _ZN30QQuickMessageDialogImplPrivate14attachedOrWarnEv
inline QQuickMessageDialogImplAttached *QQuickMessageDialogImplPrivate::attachedOrWarn()
{
    Q_Q(QQuickMessageDialogImpl);
    QQuickMessageDialogImplAttached *attached = static_cast<QQuickMessageDialogImplAttached *>(
            qmlAttachedPropertiesObject<QQuickMessageDialogImpl>(q));
    if (!attached)
        qmlWarning(q) << "Expected MessageDialogImpl attached object to be present on" << this;
    return attached;
}
//  -----------------------------------------------------------------------

//  A QQuickMessageDialogImplPrivate that Python can take functions over in. Every QQuickMessageDialogImplPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickMessageDialogImplPrivateCall0)(const void *, QQuickAbstractButton *, int *);
typedef void (*CuteQQuickMessageDialogImplPrivateCall1)(const void *, int *);
typedef void (*CuteQQuickMessageDialogImplPrivateCall2)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickMessageDialogImplPrivateCall3)(const void *, const QEventPoint *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickMessageDialogImplPrivateCall4)(const void *, QQuickItem *, const QPointF *, int *);
typedef bool (*CuteQQuickMessageDialogImplPrivateCall5)(const void *, QQuickItem *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickMessageDialogImplPrivateCall6)(const void *, QQuickItem *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickMessageDialogImplPrivateCall7)(const void *, QQuickItem *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickMessageDialogImplPrivateCall8)(const void *, const QEventPoint *, int *);
typedef void (*CuteQQuickMessageDialogImplPrivateCall9)(const void *, int *);
typedef int (*CuteQQuickMessageDialogImplPrivateCall10)(const void *, int *);
typedef void (*CuteQQuickMessageDialogImplPrivateCall11)(const void *, int *);
typedef void (*CuteQQuickMessageDialogImplPrivateCall12)(const void *, int *);
typedef void (*CuteQQuickMessageDialogImplPrivateCall13)(const void *, int *);
typedef bool (*CuteQQuickMessageDialogImplPrivateCall14)(const void *, int *);
typedef bool (*CuteQQuickMessageDialogImplPrivateCall15)(const void *, int *);
typedef void (*CuteQQuickMessageDialogImplPrivateCall16)(const void *, int *);
typedef void (*CuteQQuickMessageDialogImplPrivateCall17)(const void *, int *);
typedef void (*CuteQQuickMessageDialogImplPrivateCall18)(const void *, int *);
typedef void * (*CuteQQuickMessageDialogImplPrivateCall19)(const void *, int *);
typedef void (*CuteQQuickMessageDialogImplPrivateCall20)(const void *, QQuickItem *, int *);
typedef const QPalette * (*CuteQQuickMessageDialogImplPrivateCall21)(const void *, int *);
typedef void (*CuteQQuickMessageDialogImplPrivateCall22)(const void *, const QPalette *, int *);
class CuteQQuickMessageDialogImplPrivate : public QQuickMessageDialogImplPrivate {
public:
  using QQuickMessageDialogImplPrivate::QQuickMessageDialogImplPrivate;
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

  //  void QQuickMessageDialogImplPrivate::handleClick(QQuickAbstractButton
  //      *button)
  void handleClick(QQuickAbstractButton *button) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickMessageDialogImplPrivateCall0 call = reinterpret_cast<CuteQQuickMessageDialogImplPrivateCall0>(taken[0]);
      call(this, button, &handled);
      if (handled) return;
    }
    QQuickMessageDialogImplPrivate::handleClick(button);
  }

  //  void QQuickDialogPrivate::handleAccept()
  void handleAccept() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickMessageDialogImplPrivateCall1 call = reinterpret_cast<CuteQQuickMessageDialogImplPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickDialogPrivate::handleAccept();
  }

  //  void QQuickDialogPrivate::handleReject()
  void handleReject() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickMessageDialogImplPrivateCall2 call = reinterpret_cast<CuteQQuickMessageDialogImplPrivateCall2>(taken[2]);
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
      CuteQQuickMessageDialogImplPrivateCall3 call = reinterpret_cast<CuteQQuickMessageDialogImplPrivateCall3>(taken[3]);
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
      CuteQQuickMessageDialogImplPrivateCall4 call = reinterpret_cast<CuteQQuickMessageDialogImplPrivateCall4>(taken[4]);
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
      CuteQQuickMessageDialogImplPrivateCall5 call = reinterpret_cast<CuteQQuickMessageDialogImplPrivateCall5>(taken[5]);
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
      CuteQQuickMessageDialogImplPrivateCall6 call = reinterpret_cast<CuteQQuickMessageDialogImplPrivateCall6>(taken[6]);
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
      CuteQQuickMessageDialogImplPrivateCall7 call = reinterpret_cast<CuteQQuickMessageDialogImplPrivateCall7>(taken[7]);
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
      CuteQQuickMessageDialogImplPrivateCall8 call = reinterpret_cast<CuteQQuickMessageDialogImplPrivateCall8>(taken[8]);
      bool given = call(this, &a0, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::handleReleaseWithoutGrab(a0);
  }

  //  void QQuickPopupPrivate::handleUngrab()
  void handleUngrab() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickMessageDialogImplPrivateCall9 call = reinterpret_cast<CuteQQuickMessageDialogImplPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::handleUngrab();
  }

  //  QQuickPopup::PopupType QQuickPopupPrivate::resolvedPopupType() const
  QQuickPopup::PopupType resolvedPopupType() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickMessageDialogImplPrivateCall10 call = reinterpret_cast<CuteQQuickMessageDialogImplPrivateCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickPopup::PopupType>(given);
    }
    return QQuickPopupPrivate::resolvedPopupType();
  }

  //  void QQuickPopupPrivate::showDimmer()
  void showDimmer() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickMessageDialogImplPrivateCall11 call = reinterpret_cast<CuteQQuickMessageDialogImplPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::showDimmer();
  }

  //  void QQuickPopupPrivate::hideDimmer()
  void hideDimmer() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickMessageDialogImplPrivateCall12 call = reinterpret_cast<CuteQQuickMessageDialogImplPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::hideDimmer();
  }

  //  void QQuickPopupPrivate::resizeDimmer()
  void resizeDimmer() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickMessageDialogImplPrivateCall13 call = reinterpret_cast<CuteQQuickMessageDialogImplPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::resizeDimmer();
  }

  //  bool QQuickPopupPrivate::prepareEnterTransition()
  bool prepareEnterTransition() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickMessageDialogImplPrivateCall14 call = reinterpret_cast<CuteQQuickMessageDialogImplPrivateCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::prepareEnterTransition();
  }

  //  bool QQuickPopupPrivate::prepareExitTransition()
  bool prepareExitTransition() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickMessageDialogImplPrivateCall15 call = reinterpret_cast<CuteQQuickMessageDialogImplPrivateCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::prepareExitTransition();
  }

  //  void QQuickPopupPrivate::finalizeEnterTransition()
  void finalizeEnterTransition() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickMessageDialogImplPrivateCall16 call = reinterpret_cast<CuteQQuickMessageDialogImplPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::finalizeEnterTransition();
  }

  //  void QQuickPopupPrivate::finalizeExitTransition()
  void finalizeExitTransition() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickMessageDialogImplPrivateCall17 call = reinterpret_cast<CuteQQuickMessageDialogImplPrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::finalizeExitTransition();
  }

  //  void QQuickPopupPrivate::opened()
  void opened() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickMessageDialogImplPrivateCall18 call = reinterpret_cast<CuteQQuickMessageDialogImplPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::opened();
  }

  //  QQuickPopupPositioner *QQuickPopupPrivate::getPositioner()
  QQuickPopupPositioner *getPositioner() override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickMessageDialogImplPrivateCall19 call = reinterpret_cast<CuteQQuickMessageDialogImplPrivateCall19>(taken[19]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickPopupPositioner *>(given);
    }
    return QQuickPopupPrivate::getPositioner();
  }

  //  void QQuickPopupPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickMessageDialogImplPrivateCall20 call = reinterpret_cast<CuteQQuickMessageDialogImplPrivateCall20>(taken[20]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::itemDestroyed(item);
  }

  //  QPalette QQuickPopupPrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickMessageDialogImplPrivateCall21 call = reinterpret_cast<CuteQQuickMessageDialogImplPrivateCall21>(taken[21]);
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
      CuteQQuickMessageDialogImplPrivateCall22 call = reinterpret_cast<CuteQQuickMessageDialogImplPrivateCall22>(taken[22]);
      call(this, &parentPalette, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::updateChildrenPalettes(parentPalette);
  }
};

//  QQuickMessageDialogImpl *QQuickMessageDialogImplPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickMessageDialogImpl *ritual_ZN30QQuickMessageDialogImplPrivate6q_funcEv(
    QQuickMessageDialogImplPrivate *self) {
  return self->q_func();
}

//  const QQuickMessageDialogImpl *QQuickMessageDialogImplPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickMessageDialogImpl *ritual_ZNK30QQuickMessageDialogImplPrivate6q_funcEv(
    const QQuickMessageDialogImplPrivate *self) {
  return self->q_func();
}

//  QQuickMessageDialogImplPrivate::QQuickMessageDialogImplPrivate()
extern "C" Q_DECL_EXPORT
QQuickMessageDialogImplPrivate *ritual_ZN30QQuickMessageDialogImplPrivateC1Ev() {
  return new CuteQQuickMessageDialogImplPrivate();
}

//  QQuickMessageDialogImplPrivate
//      *QQuickMessageDialogImplPrivate::get(QQuickMessageDialogImpl *dialog)
extern "C" Q_DECL_EXPORT
QQuickMessageDialogImplPrivate *ritual_ZN30QQuickMessageDialogImplPrivate3getEP23QQuickMessageDialogImpl(
    QQuickMessageDialogImpl *dialog) {
  return QQuickMessageDialogImplPrivate::get(dialog);
}

//  QQuickMessageDialogImplAttached
//      *QQuickMessageDialogImplPrivate::attachedOrWarn()
extern "C" Q_DECL_EXPORT
QQuickMessageDialogImplAttached *ritual_ZN30QQuickMessageDialogImplPrivate14attachedOrWarnEv(
    QQuickMessageDialogImplPrivate *self) {
  return self->attachedOrWarn();
}

//  void QQuickMessageDialogImplPrivate::handleClick(QQuickAbstractButton
//      *button)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickMessageDialogImplPrivate11handleClickEP20QQuickAbstractButton(
    QQuickMessageDialogImplPrivate *self,
    QQuickAbstractButton *button) {
  self->handleClick(button);
}

//  a Python function taken by a CuteQQuickMessageDialogImplPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickMessageDialogImplPrivate(
    QQuickMessageDialogImplPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickMessageDialogImplPrivate *>(self)->take(key, call);
}

//  void QQuickMessageDialogImplPrivate::handleClick(QQuickAbstractButton
//      *button)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuickMessageDialogImplPrivate11handleClickEP20QQuickAbstractButton(
    QQuickMessageDialogImplPrivate *self,
    QQuickAbstractButton *button) {
  self->QQuickMessageDialogImplPrivate::handleClick(button);
}
