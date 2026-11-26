//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfontdialogimpl_p
//  _p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickDialogs2QuickImpl/qtquickdialogs2quickimplexports.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfontdialogimpl_p.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfontdialogimpl_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qeventpoint.h>
#include <QtCore/qpoint.h>
#include <QtGui/qpalette.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/private/qquickfontdialogimpl_p.h>
#include <QtQuickDialogs2QuickImpl/private/qquickfontdialogimpl_p_p.h>
#include <QtQuickTemplates2/private/qquickdialogbuttonbox_p_p.h>
#include <QtGui/private/qfontdatabase_p.h>
#include <QtCore/QRegularExpression>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfontdialogimpl.cpp, line 35, as _ZN27QQuickFontDialogImplPrivate11handleClickEP20QQuickAbstractButton
inline void QQuickFontDialogImplPrivate::handleClick(QQuickAbstractButton *button)
{
    Q_Q(QQuickFontDialogImpl);
    if (buttonRole(button) == QPlatformDialogHelper::AcceptRole) {
        q->accept();
        QQuickDialogPrivate::handleClick(button);
    }
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfontdialogimpl.cpp, line 33, as _ZN27QQuickFontDialogImplPrivate12handleAcceptEv
inline void QQuickFontDialogImplPrivate::handleAccept() { }

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfontdialogimpl.cpp, line 17, as _ZN27QQuickFontDialogImplPrivateC1Ev
inline QQuickFontDialogImplPrivate::QQuickFontDialogImplPrivate()
{
}
//  -----------------------------------------------------------------------

//  A QQuickFontDialogImplPrivate that Python can take functions over in. Every QQuickFontDialogImplPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickFontDialogImplPrivateCall0)(const void *, int *);
typedef void (*CuteQQuickFontDialogImplPrivateCall1)(const void *, QQuickAbstractButton *, int *);
typedef void (*CuteQQuickFontDialogImplPrivateCall2)(const void *, int *);
#if QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickFontDialogImplPrivateCall3)(const void *, const QEventPoint *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickFontDialogImplPrivateCall4)(const void *, QQuickItem *, const QPointF *, int *);
typedef bool (*CuteQQuickFontDialogImplPrivateCall5)(const void *, QQuickItem *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickFontDialogImplPrivateCall6)(const void *, QQuickItem *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickFontDialogImplPrivateCall7)(const void *, QQuickItem *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickFontDialogImplPrivateCall8)(const void *, const QEventPoint *, int *);
typedef void (*CuteQQuickFontDialogImplPrivateCall9)(const void *, int *);
typedef int (*CuteQQuickFontDialogImplPrivateCall10)(const void *, int *);
typedef void (*CuteQQuickFontDialogImplPrivateCall11)(const void *, int *);
typedef void (*CuteQQuickFontDialogImplPrivateCall12)(const void *, int *);
typedef void (*CuteQQuickFontDialogImplPrivateCall13)(const void *, int *);
typedef bool (*CuteQQuickFontDialogImplPrivateCall14)(const void *, int *);
typedef bool (*CuteQQuickFontDialogImplPrivateCall15)(const void *, int *);
typedef void (*CuteQQuickFontDialogImplPrivateCall16)(const void *, int *);
typedef void (*CuteQQuickFontDialogImplPrivateCall17)(const void *, int *);
typedef void (*CuteQQuickFontDialogImplPrivateCall18)(const void *, int *);
typedef void * (*CuteQQuickFontDialogImplPrivateCall19)(const void *, int *);
typedef void (*CuteQQuickFontDialogImplPrivateCall20)(const void *, QQuickItem *, int *);
typedef const QPalette * (*CuteQQuickFontDialogImplPrivateCall21)(const void *, int *);
typedef void (*CuteQQuickFontDialogImplPrivateCall22)(const void *, const QPalette *, int *);
class CuteQQuickFontDialogImplPrivate : public QQuickFontDialogImplPrivate {
public:
  using QQuickFontDialogImplPrivate::QQuickFontDialogImplPrivate;
  void *taken[23] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QQuickDialogPrivate12handleAcceptEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickDialogPrivate11handleClickEP20QQuickAbstractButton")) {
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

  //  void QQuickFontDialogImplPrivate::handleAccept()
  void handleAccept() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickFontDialogImplPrivateCall0 call = reinterpret_cast<CuteQQuickFontDialogImplPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickFontDialogImplPrivate::handleAccept();
  }

  //  void QQuickFontDialogImplPrivate::handleClick(QQuickAbstractButton
  //      *button)
  void handleClick(QQuickAbstractButton *button) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickFontDialogImplPrivateCall1 call = reinterpret_cast<CuteQQuickFontDialogImplPrivateCall1>(taken[1]);
      call(this, button, &handled);
      if (handled) return;
    }
    QQuickFontDialogImplPrivate::handleClick(button);
  }

  //  void QQuickDialogPrivate::handleReject()
  void handleReject() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickFontDialogImplPrivateCall2 call = reinterpret_cast<CuteQQuickFontDialogImplPrivateCall2>(taken[2]);
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
      CuteQQuickFontDialogImplPrivateCall3 call = reinterpret_cast<CuteQQuickFontDialogImplPrivateCall3>(taken[3]);
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
      CuteQQuickFontDialogImplPrivateCall4 call = reinterpret_cast<CuteQQuickFontDialogImplPrivateCall4>(taken[4]);
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
      CuteQQuickFontDialogImplPrivateCall5 call = reinterpret_cast<CuteQQuickFontDialogImplPrivateCall5>(taken[5]);
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
      CuteQQuickFontDialogImplPrivateCall6 call = reinterpret_cast<CuteQQuickFontDialogImplPrivateCall6>(taken[6]);
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
      CuteQQuickFontDialogImplPrivateCall7 call = reinterpret_cast<CuteQQuickFontDialogImplPrivateCall7>(taken[7]);
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
      CuteQQuickFontDialogImplPrivateCall8 call = reinterpret_cast<CuteQQuickFontDialogImplPrivateCall8>(taken[8]);
      bool given = call(this, &a0, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::handleReleaseWithoutGrab(a0);
  }

  //  void QQuickPopupPrivate::handleUngrab()
  void handleUngrab() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickFontDialogImplPrivateCall9 call = reinterpret_cast<CuteQQuickFontDialogImplPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::handleUngrab();
  }

  //  QQuickPopup::PopupType QQuickPopupPrivate::resolvedPopupType() const
  QQuickPopup::PopupType resolvedPopupType() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickFontDialogImplPrivateCall10 call = reinterpret_cast<CuteQQuickFontDialogImplPrivateCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return static_cast<QQuickPopup::PopupType>(given);
    }
    return QQuickPopupPrivate::resolvedPopupType();
  }

  //  void QQuickPopupPrivate::showDimmer()
  void showDimmer() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickFontDialogImplPrivateCall11 call = reinterpret_cast<CuteQQuickFontDialogImplPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::showDimmer();
  }

  //  void QQuickPopupPrivate::hideDimmer()
  void hideDimmer() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickFontDialogImplPrivateCall12 call = reinterpret_cast<CuteQQuickFontDialogImplPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::hideDimmer();
  }

  //  void QQuickPopupPrivate::resizeDimmer()
  void resizeDimmer() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickFontDialogImplPrivateCall13 call = reinterpret_cast<CuteQQuickFontDialogImplPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::resizeDimmer();
  }

  //  bool QQuickPopupPrivate::prepareEnterTransition()
  bool prepareEnterTransition() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickFontDialogImplPrivateCall14 call = reinterpret_cast<CuteQQuickFontDialogImplPrivateCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::prepareEnterTransition();
  }

  //  bool QQuickPopupPrivate::prepareExitTransition()
  bool prepareExitTransition() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickFontDialogImplPrivateCall15 call = reinterpret_cast<CuteQQuickFontDialogImplPrivateCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickPopupPrivate::prepareExitTransition();
  }

  //  void QQuickPopupPrivate::finalizeEnterTransition()
  void finalizeEnterTransition() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickFontDialogImplPrivateCall16 call = reinterpret_cast<CuteQQuickFontDialogImplPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::finalizeEnterTransition();
  }

  //  void QQuickPopupPrivate::finalizeExitTransition()
  void finalizeExitTransition() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickFontDialogImplPrivateCall17 call = reinterpret_cast<CuteQQuickFontDialogImplPrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::finalizeExitTransition();
  }

  //  void QQuickPopupPrivate::opened()
  void opened() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickFontDialogImplPrivateCall18 call = reinterpret_cast<CuteQQuickFontDialogImplPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::opened();
  }

  //  QQuickPopupPositioner *QQuickPopupPrivate::getPositioner()
  QQuickPopupPositioner *getPositioner() override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickFontDialogImplPrivateCall19 call = reinterpret_cast<CuteQQuickFontDialogImplPrivateCall19>(taken[19]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickPopupPositioner *>(given);
    }
    return QQuickPopupPrivate::getPositioner();
  }

  //  void QQuickPopupPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickFontDialogImplPrivateCall20 call = reinterpret_cast<CuteQQuickFontDialogImplPrivateCall20>(taken[20]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::itemDestroyed(item);
  }

  //  QPalette QQuickPopupPrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickFontDialogImplPrivateCall21 call = reinterpret_cast<CuteQQuickFontDialogImplPrivateCall21>(taken[21]);
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
      CuteQQuickFontDialogImplPrivateCall22 call = reinterpret_cast<CuteQQuickFontDialogImplPrivateCall22>(taken[22]);
      call(this, &parentPalette, &handled);
      if (handled) return;
    }
    QQuickPopupPrivate::updateChildrenPalettes(parentPalette);
  }
};

//  QQuickFontDialogImpl *QQuickFontDialogImplPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickFontDialogImpl *ritual_ZN27QQuickFontDialogImplPrivate6q_funcEv(
    QQuickFontDialogImplPrivate *self) {
  return self->q_func();
}

//  const QQuickFontDialogImpl *QQuickFontDialogImplPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickFontDialogImpl *ritual_ZNK27QQuickFontDialogImplPrivate6q_funcEv(
    const QQuickFontDialogImplPrivate *self) {
  return self->q_func();
}

//  QQuickFontDialogImplPrivate::QQuickFontDialogImplPrivate()
extern "C" Q_DECL_EXPORT
QQuickFontDialogImplPrivate *ritual_ZN27QQuickFontDialogImplPrivateC1Ev() {
  return new CuteQQuickFontDialogImplPrivate();
}

//  QQuickFontDialogImplPrivate
//      *QQuickFontDialogImplPrivate::get(QQuickFontDialogImpl *dialog)
extern "C" Q_DECL_EXPORT
QQuickFontDialogImplPrivate *ritual_ZN27QQuickFontDialogImplPrivate3getEP20QQuickFontDialogImpl(
    QQuickFontDialogImpl *dialog) {
  return QQuickFontDialogImplPrivate::get(dialog);
}

//  void QQuickFontDialogImplPrivate::handleAccept()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickFontDialogImplPrivate12handleAcceptEv(
    QQuickFontDialogImplPrivate *self) {
  self->handleAccept();
}

//  void QQuickFontDialogImplPrivate::handleClick(QQuickAbstractButton
//      *button)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickFontDialogImplPrivate11handleClickEP20QQuickAbstractButton(
    QQuickFontDialogImplPrivate *self,
    QQuickAbstractButton *button) {
  self->handleClick(button);
}

//  a Python function taken by a CuteQQuickFontDialogImplPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickFontDialogImplPrivate(
    QQuickFontDialogImplPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickFontDialogImplPrivate *>(self)->take(key, call);
}

//  void QQuickFontDialogImplPrivate::handleAccept()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickFontDialogImplPrivate12handleAcceptEv(
    QQuickFontDialogImplPrivate *self) {
  self->QQuickFontDialogImplPrivate::handleAccept();
}

//  void QQuickFontDialogImplPrivate::handleClick(QQuickAbstractButton
//      *button)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickFontDialogImplPrivate11handleClickEP20QQuickAbstractButton(
    QQuickFontDialogImplPrivate *self,
    QQuickAbstractButton *button) {
  self->QQuickFontDialogImplPrivate::handleClick(button);
}

#endif  // QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
