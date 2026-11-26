//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qwindow_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qwindow.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qwindow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/qpalette.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <cstring>
#include <QtCore/QSize>

//  A QWindowPrivate that Python can take functions over in. Every QWindowPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQWindowPrivateCall0)(const void *, int *);
typedef const QPalette * (*CuteQWindowPrivateCall1)(const void *, int *);
typedef void (*CuteQWindowPrivateCall2)(const void *, bool, int *);
typedef void (*CuteQWindowPrivateCall3)(const void *, int *);
typedef void (*CuteQWindowPrivateCall4)(const void *, int, int, int *);
typedef const QRectF * (*CuteQWindowPrivateCall5)(const void *, const QRectF *, int *);
typedef bool (*CuteQWindowPrivateCall6)(const void *, int *);
typedef bool (*CuteQWindowPrivateCall7)(const void *, int *);
typedef void (*CuteQWindowPrivateCall8)(const void *, QMouseEvent *, int *);
class CuteQWindowPrivate : public QWindowPrivate {
public:
  using QWindowPrivate::QWindowPrivate;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QWindowPrivate13eventReceiverEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate13windowPaletteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate10setVisibleEb")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate16clearFocusObjectEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate16setFocusToTargetENS_11FocusTargetEN2Qt11FocusReasonE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate25closestAcceptableGeometryERK6QRectF")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate30participatesInLastWindowClosedEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate14treatAsVisibleEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate31maybeSynthesizeContextMenuEventEP11QMouseEvent")) {
      taken[8] = call;
      return true;
    }
    return false;
  }

  //  QWindow *QWindowPrivate::eventReceiver()
  QWindow *eventReceiver() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWindowPrivateCall0 call = reinterpret_cast<CuteQWindowPrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QWindowPrivate::eventReceiver();
  }

  //  QPalette QWindowPrivate::windowPalette() const
  QPalette windowPalette() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQWindowPrivateCall1 call = reinterpret_cast<CuteQWindowPrivateCall1>(taken[1]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindowPrivate::windowPalette();
  }

  //  void QWindowPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWindowPrivateCall2 call = reinterpret_cast<CuteQWindowPrivateCall2>(taken[2]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWindowPrivate::setVisible(visible);
  }

  //  void QWindowPrivate::clearFocusObject()
  void clearFocusObject() override {
    if (taken[3]) {
      int handled = 0;
      CuteQWindowPrivateCall3 call = reinterpret_cast<CuteQWindowPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QWindowPrivate::clearFocusObject();
  }

  //  void QWindowPrivate::setFocusToTarget(FocusTarget a0, Qt::FocusReason
  //      a1)
  void setFocusToTarget(
      QWindowPrivate::FocusTarget a0,
      Qt::FocusReason a1) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWindowPrivateCall4 call = reinterpret_cast<CuteQWindowPrivateCall4>(taken[4]);
      call(this, static_cast<int>(a0), static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QWindowPrivate::setFocusToTarget(a0, a1);
  }

  //  QRectF QWindowPrivate::closestAcceptableGeometry(const QRectF &rect)
  //      const
  QRectF closestAcceptableGeometry(const QRectF &rect) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQWindowPrivateCall5 call = reinterpret_cast<CuteQWindowPrivateCall5>(taken[5]);
      const QRectF * given = call(this, &rect, &handled);
      if (handled && given) return *given;
    }
    return QWindowPrivate::closestAcceptableGeometry(rect);
  }

  //  bool QWindowPrivate::participatesInLastWindowClosed() const
  bool participatesInLastWindowClosed() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQWindowPrivateCall6 call = reinterpret_cast<CuteQWindowPrivateCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWindowPrivate::participatesInLastWindowClosed();
  }

  //  bool QWindowPrivate::treatAsVisible() const
  bool treatAsVisible() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQWindowPrivateCall7 call = reinterpret_cast<CuteQWindowPrivateCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWindowPrivate::treatAsVisible();
  }

  //  void QWindowPrivate::maybeSynthesizeContextMenuEvent(QMouseEvent
  //      *event)
  void maybeSynthesizeContextMenuEvent(QMouseEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQWindowPrivateCall8 call = reinterpret_cast<CuteQWindowPrivateCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWindowPrivate::maybeSynthesizeContextMenuEvent(event);
  }
};

//  QWindow *QWindowPrivate::q_func()
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZN14QWindowPrivate6q_funcEv(QWindowPrivate *self) {
  return self->q_func();
}

//  const QWindow *QWindowPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QWindow *ritual_ZNK14QWindowPrivate6q_funcEv(
    const QWindowPrivate *self) {
  return self->q_func();
}

//  QWindowPrivate::QWindowPrivate(decltype(QObjectPrivateVersion) version)
extern "C" Q_DECL_EXPORT
QWindowPrivate *ritual_ZN14QWindowPrivateC1E16QtPrivate_6_12_0(
    decltype(QObjectPrivateVersion) version) {
  return new CuteQWindowPrivate(version);
}

//  QWindowPrivate::~QWindowPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowPrivateD1Ev(QWindowPrivate *self) {
  delete self;
}

//  void QWindowPrivate::init(QWindow *parent, QScreen *targetScreen)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowPrivate4initEP7QWindowP7QScreen(
    QWindowPrivate *self,
    QWindow *parent,
    QScreen *targetScreen) {
  self->init(parent, targetScreen);
}

#if !defined(QT_NO_CURSOR)
//  void QWindowPrivate::setCursor(const QCursor *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowPrivate9setCursorEPK7QCursor(
    QWindowPrivate *self,
    const QCursor *c) {
  self->setCursor(c);
}
#endif  // !defined(QT_NO_CURSOR)

#if !defined(QT_NO_CURSOR)
//  bool QWindowPrivate::applyCursor()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QWindowPrivate11applyCursorEv(QWindowPrivate *self) {
  return self->applyCursor();
}
#endif  // !defined(QT_NO_CURSOR)

//  QPoint QWindowPrivate::globalPosition() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK14QWindowPrivate14globalPositionEv(
    const QWindowPrivate *self) {
  return new QPoint(self->globalPosition());
}

//  QWindow *QWindowPrivate::topLevelWindow(QWindow::AncestorMode mode) const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK14QWindowPrivate14topLevelWindowEN7QWindow12AncestorModeE(
    const QWindowPrivate *self,
    QWindow::AncestorMode mode) {
  return self->topLevelWindow(mode);
}

//  QWindow *QWindowPrivate::eventReceiver()
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZN14QWindowPrivate13eventReceiverEv(QWindowPrivate *self) {
  return self->eventReceiver();
}

//  QPalette QWindowPrivate::windowPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK14QWindowPrivate13windowPaletteEv(
    const QWindowPrivate *self) {
  return new QPalette(self->windowPalette());
}

//  void QWindowPrivate::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowPrivate10setVisibleEb(
    QWindowPrivate *self,
    bool visible) {
  self->setVisible(visible);
}

//  void QWindowPrivate::updateVisibility()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowPrivate16updateVisibilityEv(QWindowPrivate *self) {
  self->updateVisibility();
}

//  void QWindowPrivate::_q_clearAlert()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowPrivate13_q_clearAlertEv(QWindowPrivate *self) {
  self->_q_clearAlert();
}

//  void QWindowPrivate::updateSiblingPosition(SiblingPosition a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowPrivate21updateSiblingPositionENS_15SiblingPositionE(
    QWindowPrivate *self,
    QWindowPrivate::SiblingPosition a0) {
  self->updateSiblingPosition(a0);
}

//  bool QWindowPrivate::windowRecreationRequired(QScreen *newScreen) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QWindowPrivate24windowRecreationRequiredEP7QScreen(
    const QWindowPrivate *self,
    QScreen *newScreen) {
  return self->windowRecreationRequired(newScreen);
}

//  void QWindowPrivate::create(bool recursive)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowPrivate6createEb(
    QWindowPrivate *self,
    bool recursive) {
  self->create(recursive);
}

//  void QWindowPrivate::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowPrivate7destroyEv(QWindowPrivate *self) {
  self->destroy();
}

//  void QWindowPrivate::setTopLevelScreen(QScreen *newScreen, bool recreate)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowPrivate17setTopLevelScreenEP7QScreenb(
    QWindowPrivate *self,
    QScreen *newScreen,
    bool recreate) {
  self->setTopLevelScreen(newScreen, recreate);
}

//  void QWindowPrivate::connectToScreen(QScreen *topLevelScreen)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowPrivate15connectToScreenEP7QScreen(
    QWindowPrivate *self,
    QScreen *topLevelScreen) {
  self->connectToScreen(topLevelScreen);
}

//  void QWindowPrivate::disconnectFromScreen()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowPrivate20disconnectFromScreenEv(
    QWindowPrivate *self) {
  self->disconnectFromScreen();
}

//  void QWindowPrivate::emitScreenChangedRecursion(QScreen *newScreen)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowPrivate26emitScreenChangedRecursionEP7QScreen(
    QWindowPrivate *self,
    QScreen *newScreen) {
  self->emitScreenChangedRecursion(newScreen);
}

//  QScreen *QWindowPrivate::screenForGeometry(const QRect &rect) const
extern "C" Q_DECL_EXPORT
QScreen *ritual_ZNK14QWindowPrivate17screenForGeometryERK5QRect(
    const QWindowPrivate *self,
    const QRect *rect) {
  return self->screenForGeometry(*rect);
}

//  void QWindowPrivate::setTransientParent(QWindow *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowPrivate18setTransientParentEP7QWindow(
    QWindowPrivate *self,
    QWindow *parent) {
  self->setTransientParent(parent);
}

//  void QWindowPrivate::clearFocusObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowPrivate16clearFocusObjectEv(QWindowPrivate *self) {
  self->clearFocusObject();
}

//  void QWindowPrivate::setFocusToTarget(FocusTarget a0, Qt::FocusReason a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowPrivate16setFocusToTargetENS_11FocusTargetEN2Qt11FocusReasonE(
    QWindowPrivate *self,
    QWindowPrivate::FocusTarget a0,
    Qt::FocusReason a1) {
  self->setFocusToTarget(a0, a1);
}

//  QRectF QWindowPrivate::closestAcceptableGeometry(const QRectF &rect)
//      const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK14QWindowPrivate25closestAcceptableGeometryERK6QRectF(
    const QWindowPrivate *self,
    const QRectF *rect) {
  return new QRectF(self->closestAcceptableGeometry(*rect));
}

//  void QWindowPrivate::setMinOrMaxSize(QSize *oldSizeMember, const QSize
//      &size, qxp::function_ref<void ()> funcWidthChanged,
//      qxp::function_ref<void ()> funcHeightChanged)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowPrivate15setMinOrMaxSizeEP5QSizeRKS0_N3qxp12function_refIJFvvEEEES7_(
    QWindowPrivate *self,
    QSize *oldSizeMember,
    const QSize *size,
    const qxp::function_ref<void ()> *funcWidthChanged,
    const qxp::function_ref<void ()> *funcHeightChanged) {
  self->setMinOrMaxSize(
      oldSizeMember,
      *size,
      *funcWidthChanged,
      *funcHeightChanged);
}

//  bool QWindowPrivate::participatesInLastWindowClosed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QWindowPrivate30participatesInLastWindowClosedEv(
    const QWindowPrivate *self) {
  return self->participatesInLastWindowClosed();
}

//  bool QWindowPrivate::treatAsVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QWindowPrivate14treatAsVisibleEv(
    const QWindowPrivate *self) {
  return self->treatAsVisible();
}

//  void QWindowPrivate::maybeSynthesizeContextMenuEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowPrivate31maybeSynthesizeContextMenuEventEP11QMouseEvent(
    QWindowPrivate *self,
    QMouseEvent *event) {
  self->maybeSynthesizeContextMenuEvent(event);
}

//  const QWindow *QWindowPrivate::forwardToPopup(QEvent *event, const
//      QWindow *activePopupOnPress)
extern "C" Q_DECL_EXPORT
const QWindow *ritual_ZN14QWindowPrivate14forwardToPopupEP6QEventPK7QWindow(
    QWindowPrivate *self,
    QEvent *event,
    const QWindow *activePopupOnPress) {
  return self->forwardToPopup(event, activePopupOnPress);
}

//  bool QWindowPrivate::isPopup() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QWindowPrivate7isPopupEv(const QWindowPrivate *self) {
  return self->isPopup();
}

//  void QWindowPrivate::setAutomaticPositionAndResizeEnabled(bool a)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWindowPrivate36setAutomaticPositionAndResizeEnabledEb(
    QWindowPrivate *self,
    bool a) {
  self->setAutomaticPositionAndResizeEnabled(a);
}

//  bool QWindowPrivate::updateDevicePixelRatio()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QWindowPrivate22updateDevicePixelRatioEv(
    QWindowPrivate *self) {
  return self->updateDevicePixelRatio();
}

//  QWindowPrivate *QWindowPrivate::get(QWindow *window)
extern "C" Q_DECL_EXPORT
QWindowPrivate *ritual_ZN14QWindowPrivate3getEP7QWindow(QWindow *window) {
  return QWindowPrivate::get(window);
}

//  Qt::WindowState QWindowPrivate::effectiveState(Qt::WindowStates a0)
extern "C" Q_DECL_EXPORT
Qt::WindowState ritual_ZN14QWindowPrivate14effectiveStateE6QFlagsIN2Qt11WindowStateEE(
    int a0) {
  return QWindowPrivate::effectiveState(
      QFlags<Qt::WindowState>::fromInt(a0));
}

//  a Python function taken by a CuteQWindowPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWindowPrivate(
    QWindowPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWindowPrivate *>(self)->take(key, call);
}

//  QWindow *QWindowPrivate::eventReceiver()
extern "C" Q_DECL_EXPORT
QWindow *ritual_own_ZN14QWindowPrivate13eventReceiverEv(
    QWindowPrivate *self) {
  return self->QWindowPrivate::eventReceiver();
}

//  QPalette QWindowPrivate::windowPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_own_ZNK14QWindowPrivate13windowPaletteEv(
    const QWindowPrivate *self) {
  return new QPalette(self->QWindowPrivate::windowPalette());
}

//  void QWindowPrivate::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QWindowPrivate10setVisibleEb(
    QWindowPrivate *self,
    bool visible) {
  self->QWindowPrivate::setVisible(visible);
}

//  void QWindowPrivate::clearFocusObject()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QWindowPrivate16clearFocusObjectEv(
    QWindowPrivate *self) {
  self->QWindowPrivate::clearFocusObject();
}

//  void QWindowPrivate::setFocusToTarget(FocusTarget a0, Qt::FocusReason a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QWindowPrivate16setFocusToTargetENS_11FocusTargetEN2Qt11FocusReasonE(
    QWindowPrivate *self,
    QWindowPrivate::FocusTarget a0,
    Qt::FocusReason a1) {
  self->QWindowPrivate::setFocusToTarget(a0, a1);
}

//  QRectF QWindowPrivate::closestAcceptableGeometry(const QRectF &rect)
//      const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK14QWindowPrivate25closestAcceptableGeometryERK6QRectF(
    const QWindowPrivate *self,
    const QRectF *rect) {
  return new QRectF(self->QWindowPrivate::closestAcceptableGeometry(*rect));
}

//  bool QWindowPrivate::participatesInLastWindowClosed() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QWindowPrivate30participatesInLastWindowClosedEv(
    const QWindowPrivate *self) {
  return self->QWindowPrivate::participatesInLastWindowClosed();
}

//  bool QWindowPrivate::treatAsVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QWindowPrivate14treatAsVisibleEv(
    const QWindowPrivate *self) {
  return self->QWindowPrivate::treatAsVisible();
}

//  void QWindowPrivate::maybeSynthesizeContextMenuEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QWindowPrivate31maybeSynthesizeContextMenuEventEP11QMouseEvent(
    QWindowPrivate *self,
    QMouseEvent *event) {
  self->QWindowPrivate::maybeSynthesizeContextMenuEvent(event);
}
