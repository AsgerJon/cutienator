//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickwindow_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickwindow.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickwindow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpalette.h>
#include <QtCore/qpoint.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <cstring>

//  A QQuickWindowPrivate that Python can take functions over in. Every QQuickWindowPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickWindowPrivateCall0)(const void *, QQuickPalette *, int *);
typedef void (*CuteQQuickWindowPrivateCall1)(const void *, const QPalette *, int *);
typedef void (*CuteQQuickWindowPrivateCall2)(const void *, int *);
typedef void (*CuteQQuickWindowPrivateCall3)(const void *, int, int, int *);
typedef void (*CuteQQuickWindowPrivateCall4)(const void *, QMouseEvent *, int *);
typedef void * (*CuteQQuickWindowPrivateCall5)(const void *, int *);
typedef const QPalette * (*CuteQQuickWindowPrivateCall6)(const void *, int *);
typedef void (*CuteQQuickWindowPrivateCall7)(const void *, bool, int *);
typedef const QRectF * (*CuteQQuickWindowPrivateCall8)(const void *, const QRectF *, int *);
typedef bool (*CuteQQuickWindowPrivateCall9)(const void *, int *);
typedef bool (*CuteQQuickWindowPrivateCall10)(const void *, int *);
class CuteQQuickWindowPrivate : public QQuickWindowPrivate {
public:
  using QQuickWindowPrivate::QQuickWindowPrivate;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QQuickWindowPrivate10setPaletteEP13QQuickPalette")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickWindowPrivate22updateChildrenPalettesERK8QPalette")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate16clearFocusObjectEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate16setFocusToTargetENS_11FocusTargetEN2Qt11FocusReasonE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate31maybeSynthesizeContextMenuEventEP11QMouseEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate13eventReceiverEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate13windowPaletteEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWindowPrivate10setVisibleEb")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate25closestAcceptableGeometryERK6QRectF")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate30participatesInLastWindowClosedEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWindowPrivate14treatAsVisibleEv")) {
      taken[10] = call;
      return true;
    }
    return false;
  }

  //  void QQuickWindowPrivate::setPalette(QQuickPalette *p)
  void setPalette(QQuickPalette *p) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickWindowPrivateCall0 call = reinterpret_cast<CuteQQuickWindowPrivateCall0>(taken[0]);
      call(this, p, &handled);
      if (handled) return;
    }
    QQuickWindowPrivate::setPalette(p);
  }

  //  void QQuickWindowPrivate::updateChildrenPalettes(const QPalette
  //      &parentPalette)
  void updateChildrenPalettes(const QPalette &parentPalette) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickWindowPrivateCall1 call = reinterpret_cast<CuteQQuickWindowPrivateCall1>(taken[1]);
      call(this, &parentPalette, &handled);
      if (handled) return;
    }
    QQuickWindowPrivate::updateChildrenPalettes(parentPalette);
  }

  //  void QQuickWindowPrivate::clearFocusObject()
  void clearFocusObject() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickWindowPrivateCall2 call = reinterpret_cast<CuteQQuickWindowPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickWindowPrivate::clearFocusObject();
  }

  //  void QQuickWindowPrivate::setFocusToTarget(FocusTarget a0,
  //      Qt::FocusReason a1)
  void setFocusToTarget(
      QWindowPrivate::FocusTarget a0,
      Qt::FocusReason a1) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickWindowPrivateCall3 call = reinterpret_cast<CuteQQuickWindowPrivateCall3>(taken[3]);
      call(this, static_cast<int>(a0), static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QQuickWindowPrivate::setFocusToTarget(a0, a1);
  }

  //  void QQuickWindowPrivate::maybeSynthesizeContextMenuEvent(QMouseEvent
  //      *event)
  void maybeSynthesizeContextMenuEvent(QMouseEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickWindowPrivateCall4 call = reinterpret_cast<CuteQQuickWindowPrivateCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickWindowPrivate::maybeSynthesizeContextMenuEvent(event);
  }

  //  QWindow *QWindowPrivate::eventReceiver()
  QWindow *eventReceiver() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickWindowPrivateCall5 call = reinterpret_cast<CuteQQuickWindowPrivateCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QWindowPrivate::eventReceiver();
  }

  //  QPalette QWindowPrivate::windowPalette() const
  QPalette windowPalette() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickWindowPrivateCall6 call = reinterpret_cast<CuteQQuickWindowPrivateCall6>(taken[6]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindowPrivate::windowPalette();
  }

  //  void QWindowPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickWindowPrivateCall7 call = reinterpret_cast<CuteQQuickWindowPrivateCall7>(taken[7]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWindowPrivate::setVisible(visible);
  }

  //  QRectF QWindowPrivate::closestAcceptableGeometry(const QRectF &rect)
  //      const
  QRectF closestAcceptableGeometry(const QRectF &rect) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickWindowPrivateCall8 call = reinterpret_cast<CuteQQuickWindowPrivateCall8>(taken[8]);
      const QRectF * given = call(this, &rect, &handled);
      if (handled && given) return *given;
    }
    return QWindowPrivate::closestAcceptableGeometry(rect);
  }

  //  bool QWindowPrivate::participatesInLastWindowClosed() const
  bool participatesInLastWindowClosed() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickWindowPrivateCall9 call = reinterpret_cast<CuteQQuickWindowPrivateCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWindowPrivate::participatesInLastWindowClosed();
  }

  //  bool QWindowPrivate::treatAsVisible() const
  bool treatAsVisible() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickWindowPrivateCall10 call = reinterpret_cast<CuteQQuickWindowPrivateCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWindowPrivate::treatAsVisible();
  }
};

//  QQuickWindow *QQuickWindowPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickWindow *ritual_ZN19QQuickWindowPrivate6q_funcEv(
    QQuickWindowPrivate *self) {
  return self->q_func();
}

//  const QQuickWindow *QQuickWindowPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickWindow *ritual_ZNK19QQuickWindowPrivate6q_funcEv(
    const QQuickWindowPrivate *self) {
  return self->q_func();
}

//  QQuickWindowPrivate *QQuickWindowPrivate::get(QQuickWindow *c)
extern "C" Q_DECL_EXPORT
QQuickWindowPrivate *ritual_ZN19QQuickWindowPrivate3getEP12QQuickWindow(
    QQuickWindow *c) {
  return QQuickWindowPrivate::get(c);
}

//  const QQuickWindowPrivate *QQuickWindowPrivate::get(const QQuickWindow
//      *c)
extern "C" Q_DECL_EXPORT
const QQuickWindowPrivate *ritual_ZN19QQuickWindowPrivate3getEPK12QQuickWindow(
    const QQuickWindow *c) {
  return QQuickWindowPrivate::get(c);
}

//  QQuickWindowPrivate::QQuickWindowPrivate()
extern "C" Q_DECL_EXPORT
QQuickWindowPrivate *ritual_ZN19QQuickWindowPrivateC1Ev() {
  return new CuteQQuickWindowPrivate();
}

//  QQuickWindowPrivate::~QQuickWindowPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowPrivateD1Ev(QQuickWindowPrivate *self) {
  delete self;
}

//  void QQuickWindowPrivate::setPalette(QQuickPalette *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowPrivate10setPaletteEP13QQuickPalette(
    QQuickWindowPrivate *self,
    QQuickPalette *p) {
  self->setPalette(p);
}

//  void QQuickWindowPrivate::updateWindowPalette()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowPrivate19updateWindowPaletteEv(
    QQuickWindowPrivate *self) {
  self->updateWindowPalette();
}

//  void QQuickWindowPrivate::updateChildrenPalettes(const QPalette
//      &parentPalette)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowPrivate22updateChildrenPalettesERK8QPalette(
    QQuickWindowPrivate *self,
    const QPalette *parentPalette) {
  self->updateChildrenPalettes(*parentPalette);
}

//  void QQuickWindowPrivate::init(QQuickWindow *a0, QQuickRenderControl
//      *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowPrivate4initEP12QQuickWindowP19QQuickRenderControl(
    QQuickWindowPrivate *self,
    QQuickWindow *a0,
    QQuickRenderControl *control) {
  self->init(a0, control);
}

//  QQuickDeliveryAgentPrivate *QQuickWindowPrivate::deliveryAgentPrivate()
//      const
extern "C" Q_DECL_EXPORT
QQuickDeliveryAgentPrivate *ritual_ZNK19QQuickWindowPrivate20deliveryAgentPrivateEv(
    const QQuickWindowPrivate *self) {
  return self->deliveryAgentPrivate();
}

#if QT_CONFIG(cursor)
//  void QQuickWindowPrivate::updateCursor(const QPointF &scenePos,
//      QQuickItem *rootItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowPrivate12updateCursorERK7QPointFP10QQuickItem(
    QQuickWindowPrivate *self,
    const QPointF *scenePos,
    QQuickItem *rootItem) {
  self->updateCursor(*scenePos, rootItem);
}
#endif  // QT_CONFIG(cursor)

//  void QQuickWindowPrivate::clearFocusObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowPrivate16clearFocusObjectEv(
    QQuickWindowPrivate *self) {
  self->clearFocusObject();
}

//  void QQuickWindowPrivate::setFocusToTarget(FocusTarget a0,
//      Qt::FocusReason a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowPrivate16setFocusToTargetEN14QWindowPrivate11FocusTargetEN2Qt11FocusReasonE(
    QQuickWindowPrivate *self,
    QWindowPrivate::FocusTarget a0,
    Qt::FocusReason a1) {
  self->setFocusToTarget(a0, a1);
}

//  void QQuickWindowPrivate::maybeSynthesizeContextMenuEvent(QMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowPrivate31maybeSynthesizeContextMenuEventEP11QMouseEvent(
    QQuickWindowPrivate *self,
    QMouseEvent *event) {
  self->maybeSynthesizeContextMenuEvent(event);
}

//  void QQuickWindowPrivate::dirtyItem(QQuickItem *item, bool maySkipUpdate)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowPrivate9dirtyItemEP10QQuickItemb(
    QQuickWindowPrivate *self,
    QQuickItem *item,
    bool maySkipUpdate) {
  self->dirtyItem(item, maySkipUpdate);
}

//  void QQuickWindowPrivate::cleanup(QSGNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowPrivate7cleanupEP7QSGNode(
    QQuickWindowPrivate *self,
    QSGNode *a0) {
  self->cleanup(a0);
}

//  void QQuickWindowPrivate::ensureCustomRenderTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowPrivate24ensureCustomRenderTargetEv(
    QQuickWindowPrivate *self) {
  self->ensureCustomRenderTarget();
}

//  void QQuickWindowPrivate::setCustomCommandBuffer(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowPrivate22setCustomCommandBufferEP17QRhiCommandBuffer(
    QQuickWindowPrivate *self,
    QRhiCommandBuffer *cb) {
  self->setCustomCommandBuffer(cb);
}

//  void QQuickWindowPrivate::polishItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowPrivate11polishItemsEv(
    QQuickWindowPrivate *self) {
  self->polishItems();
}

//  void QQuickWindowPrivate::forcePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowPrivate11forcePolishEv(
    QQuickWindowPrivate *self) {
  self->forcePolish();
}

//  void QQuickWindowPrivate::invalidateFontData(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowPrivate18invalidateFontDataEP10QQuickItem(
    QQuickWindowPrivate *self,
    QQuickItem *item) {
  self->invalidateFontData(item);
}

//  void QQuickWindowPrivate::syncSceneGraph()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowPrivate14syncSceneGraphEv(
    QQuickWindowPrivate *self) {
  self->syncSceneGraph();
}

//  void QQuickWindowPrivate::renderSceneGraph()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowPrivate16renderSceneGraphEv(
    QQuickWindowPrivate *self) {
  self->renderSceneGraph();
}

//  bool QQuickWindowPrivate::isRenderable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQuickWindowPrivate12isRenderableEv(
    const QQuickWindowPrivate *self) {
  return self->isRenderable();
}

//  bool QQuickWindowPrivate::emitError(QQuickWindow::SceneGraphError error,
//      const QString &msg)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickWindowPrivate9emitErrorEN12QQuickWindow15SceneGraphErrorERK7QString(
    QQuickWindowPrivate *self,
    QQuickWindow::SceneGraphError error,
    const QString *msg) {
  return self->emitError(error, *msg);
}

//  QSGTexture *QQuickWindowPrivate::createTextureFromNativeTexture(quint64
//      nativeObjectHandle, int nativeLayoutOrState, uint nativeFormat, const
//      QSize &size, QQuickWindow::CreateTextureOptions options,
//      TextureFromNativeTextureFlags flags) const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK19QQuickWindowPrivate30createTextureFromNativeTextureEyijRK5QSize6QFlagsIN12QQuickWindow19CreateTextureOptionEES3_INS_28TextureFromNativeTextureFlagEE(
    const QQuickWindowPrivate *self,
    quint64 nativeObjectHandle,
    int nativeLayoutOrState,
    uint nativeFormat,
    const QSize *size,
    int options,
    int flags) {
  return self->createTextureFromNativeTexture(
      nativeObjectHandle,
      nativeLayoutOrState,
      nativeFormat,
      *size,
      QFlags<QQuickWindow::CreateTextureOption>::fromInt(options),
      QFlags<QQuickWindowPrivate::TextureFromNativeTextureFlag>::fromInt(flags));
}

//  QSGTexture *QQuickWindowPrivate::createTextureFromNativeTexture(quint64
//      nativeObjectHandle, int nativeLayoutOrState, const QSize &size,
//      QQuickWindow::CreateTextureOptions options,
//      TextureFromNativeTextureFlags flags) const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK19QQuickWindowPrivate30createTextureFromNativeTextureEyiRK5QSize6QFlagsIN12QQuickWindow19CreateTextureOptionEES3_INS_28TextureFromNativeTextureFlagEE(
    const QQuickWindowPrivate *self,
    quint64 nativeObjectHandle,
    int nativeLayoutOrState,
    const QSize *size,
    int options,
    int flags) {
  return self->createTextureFromNativeTexture(
      nativeObjectHandle,
      nativeLayoutOrState,
      *size,
      QFlags<QQuickWindow::CreateTextureOption>::fromInt(options),
      QFlags<QQuickWindowPrivate::TextureFromNativeTextureFlag>::fromInt(flags));
}

//  void QQuickWindowPrivate::updateDirtyNodes()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowPrivate16updateDirtyNodesEv(
    QQuickWindowPrivate *self) {
  self->updateDirtyNodes();
}

//  void QQuickWindowPrivate::cleanupNodes()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowPrivate12cleanupNodesEv(
    QQuickWindowPrivate *self) {
  self->cleanupNodes();
}

//  void QQuickWindowPrivate::cleanupNodesOnShutdown()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowPrivate22cleanupNodesOnShutdownEv(
    QQuickWindowPrivate *self) {
  self->cleanupNodesOnShutdown();
}

//  void QQuickWindowPrivate::updateDirtyNode(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowPrivate15updateDirtyNodeEP10QQuickItem(
    QQuickWindowPrivate *self,
    QQuickItem *a0) {
  self->updateDirtyNode(a0);
}

//  void QQuickWindowPrivate::fireFrameSwapped()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowPrivate16fireFrameSwappedEv(
    QQuickWindowPrivate *self) {
  self->fireFrameSwapped();
}

//  void QQuickWindowPrivate::fireAboutToStop()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowPrivate15fireAboutToStopEv(
    QQuickWindowPrivate *self) {
  self->fireAboutToStop();
}

//  void QQuickWindowPrivate::updateChildWindowStackingOrder(QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowPrivate30updateChildWindowStackingOrderEP10QQuickItem(
    QQuickWindowPrivate *self,
    QQuickItem *item) {
  self->updateChildWindowStackingOrder(item);
}

//  int QQuickWindowPrivate::multiViewCount()
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuickWindowPrivate14multiViewCountEv(
    QQuickWindowPrivate *self) {
  return self->multiViewCount();
}

//  QRhiRenderTarget *QQuickWindowPrivate::activeCustomRhiRenderTarget()
extern "C" Q_DECL_EXPORT
QRhiRenderTarget *ritual_ZN19QQuickWindowPrivate27activeCustomRhiRenderTargetEv(
    QQuickWindowPrivate *self) {
  return self->activeCustomRhiRenderTarget();
}

//  void QQuickWindowPrivate::rhiCreationFailureMessage(const QString
//      &backendName, QString *translatedMessage, QString
//      *untranslatedMessage)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowPrivate25rhiCreationFailureMessageERK7QStringPS0_S3_(
    const QString *backendName,
    QString *translatedMessage,
    QString *untranslatedMessage) {
  QQuickWindowPrivate::rhiCreationFailureMessage(
      *backendName,
      translatedMessage,
      untranslatedMessage);
}

//  QOpenGLContext *QQuickWindowPrivate::openglContext()
extern "C" Q_DECL_EXPORT
QOpenGLContext *ritual_ZN19QQuickWindowPrivate13openglContextEv(
    QQuickWindowPrivate *self) {
  return self->openglContext();
}

//  void QQuickWindowPrivate::cleanupNodesOnShutdown(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWindowPrivate22cleanupNodesOnShutdownEP10QQuickItem(
    QQuickItem *a0) {
  QQuickWindowPrivate::cleanupNodesOnShutdown(a0);
}

//  a Python function taken by a CuteQQuickWindowPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWindowPrivate(
    QQuickWindowPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWindowPrivate *>(self)->take(key, call);
}

//  void QQuickWindowPrivate::setPalette(QQuickPalette *p)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickWindowPrivate10setPaletteEP13QQuickPalette(
    QQuickWindowPrivate *self,
    QQuickPalette *p) {
  self->QQuickWindowPrivate::setPalette(p);
}

//  void QQuickWindowPrivate::updateChildrenPalettes(const QPalette
//      &parentPalette)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickWindowPrivate22updateChildrenPalettesERK8QPalette(
    QQuickWindowPrivate *self,
    const QPalette *parentPalette) {
  self->QQuickWindowPrivate::updateChildrenPalettes(*parentPalette);
}

//  void QQuickWindowPrivate::clearFocusObject()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickWindowPrivate16clearFocusObjectEv(
    QQuickWindowPrivate *self) {
  self->QQuickWindowPrivate::clearFocusObject();
}

//  void QQuickWindowPrivate::setFocusToTarget(FocusTarget a0,
//      Qt::FocusReason a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickWindowPrivate16setFocusToTargetEN14QWindowPrivate11FocusTargetEN2Qt11FocusReasonE(
    QQuickWindowPrivate *self,
    QWindowPrivate::FocusTarget a0,
    Qt::FocusReason a1) {
  self->QQuickWindowPrivate::setFocusToTarget(a0, a1);
}

//  void QQuickWindowPrivate::maybeSynthesizeContextMenuEvent(QMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickWindowPrivate31maybeSynthesizeContextMenuEventEP11QMouseEvent(
    QQuickWindowPrivate *self,
    QMouseEvent *event) {
  self->QQuickWindowPrivate::maybeSynthesizeContextMenuEvent(event);
}
