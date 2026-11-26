//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgsoftwarepixmaprenderer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgsoftwarepixmaprenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgsoftwarepixmaprenderer_p.h>
#include <QtQuick/private/qsgsoftwarecontext_p.h>
#include <QtQuick/QSGSimpleRectNode>
#include <QtCore/QElapsedTimer>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepixmaprenderer.cpp, line 22, as _ZN25QSGSoftwarePixmapRendererD2Ev
inline QSGSoftwarePixmapRenderer::~QSGSoftwarePixmapRenderer()
{

}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepixmaprenderer.cpp, line 16, as _ZN25QSGSoftwarePixmapRendererC1EP16QSGRenderContext
inline QSGSoftwarePixmapRenderer::QSGSoftwarePixmapRenderer(QSGRenderContext *context)
    : QSGAbstractSoftwareRenderer(context)
{

}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepixmaprenderer.cpp, line 27, as _ZN25QSGSoftwarePixmapRenderer11renderSceneEv
inline void QSGSoftwarePixmapRenderer::renderScene()
{
    QSGRenderer::renderScene();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepixmaprenderer.cpp, line 32, as _ZN25QSGSoftwarePixmapRenderer6renderEv
inline void QSGSoftwarePixmapRenderer::render()
{

}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepixmaprenderer.cpp, line 77, as _ZN25QSGSoftwarePixmapRenderer17setProjectionRectERK5QRect
inline void QSGSoftwarePixmapRenderer::setProjectionRect(const QRect &projectionRect)
{
    m_projectionRect = projectionRect;
}
//  -----------------------------------------------------------------------

//  A QSGSoftwarePixmapRenderer that Python can take functions over in. Every QSGSoftwarePixmapRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGSoftwarePixmapRendererCall0)(const void *, QSGNode *, int, int *);
typedef void (*CuteQSGSoftwarePixmapRendererCall1)(const void *, int *);
typedef void (*CuteQSGSoftwarePixmapRendererCall2)(const void *, int *);
typedef void (*CuteQSGSoftwarePixmapRendererCall3)(const void *, const QByteArray *, int *);
typedef bool (*CuteQSGSoftwarePixmapRendererCall4)(const void *, int *);
typedef void (*CuteQSGSoftwarePixmapRendererCall5)(const void *, int *);
typedef void (*CuteQSGSoftwarePixmapRendererCall6)(const void *, int *);
typedef void (*CuteQSGSoftwarePixmapRendererCall7)(const void *, int *);
typedef void (*CuteQSGSoftwarePixmapRendererCall8)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGSoftwarePixmapRendererCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSGSoftwarePixmapRendererCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwarePixmapRendererCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwarePixmapRendererCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwarePixmapRendererCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwarePixmapRendererCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSGSoftwarePixmapRendererCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSGSoftwarePixmapRenderer : public QSGSoftwarePixmapRenderer {
public:
  using QSGSoftwarePixmapRenderer::QSGSoftwarePixmapRenderer;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QSGAbstractRenderer11nodeChangedEP7QSGNode6QFlagsINS0_13DirtyStateBitEE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QSGAbstractRenderer18prepareSceneInlineEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QSGAbstractRenderer17renderSceneInlineEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGRenderer20setVisualizationModeERK10QByteArray")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGRenderer40hasVisualizationModeWithContinuousUpdateEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGRenderer22releaseCachedResourcesEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGRenderer13prepareInlineEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGRenderer12renderInlineEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGRenderer10preprocessEv")) {
      taken[8] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QSGAbstractSoftwareRenderer::nodeChanged(QSGNode *node,
  //      QSGNode::DirtyState state)
  void nodeChanged(QSGNode *node, QSGNode::DirtyState state) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGSoftwarePixmapRendererCall0 call = reinterpret_cast<CuteQSGSoftwarePixmapRendererCall0>(taken[0]);
      call(this, node, static_cast<int>(state.toInt()), &handled);
      if (handled) return;
    }
    QSGAbstractSoftwareRenderer::nodeChanged(node, state);
  }

  //  void QSGRenderer::prepareSceneInline()
  void prepareSceneInline() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGSoftwarePixmapRendererCall1 call = reinterpret_cast<CuteQSGSoftwarePixmapRendererCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderer::prepareSceneInline();
  }

  //  void QSGRenderer::renderSceneInline()
  void renderSceneInline() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGSoftwarePixmapRendererCall2 call = reinterpret_cast<CuteQSGSoftwarePixmapRendererCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderer::renderSceneInline();
  }

  //  void QSGRenderer::setVisualizationMode(const QByteArray &a0)
  void setVisualizationMode(const QByteArray &a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGSoftwarePixmapRendererCall3 call = reinterpret_cast<CuteQSGSoftwarePixmapRendererCall3>(taken[3]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QSGRenderer::setVisualizationMode(a0);
  }

  //  bool QSGRenderer::hasVisualizationModeWithContinuousUpdate() const
  bool hasVisualizationModeWithContinuousUpdate() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGSoftwarePixmapRendererCall4 call = reinterpret_cast<CuteQSGSoftwarePixmapRendererCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGRenderer::hasVisualizationModeWithContinuousUpdate();
  }

  //  void QSGRenderer::releaseCachedResources()
  void releaseCachedResources() override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGSoftwarePixmapRendererCall5 call = reinterpret_cast<CuteQSGSoftwarePixmapRendererCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderer::releaseCachedResources();
  }

  //  void QSGRenderer::prepareInline()
  void prepareInline() override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGSoftwarePixmapRendererCall6 call = reinterpret_cast<CuteQSGSoftwarePixmapRendererCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderer::prepareInline();
  }

  //  void QSGRenderer::renderInline()
  void renderInline() override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGSoftwarePixmapRendererCall7 call = reinterpret_cast<CuteQSGSoftwarePixmapRendererCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderer::renderInline();
  }

  //  void QSGRenderer::preprocess()
  void preprocess() override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGSoftwarePixmapRendererCall8 call = reinterpret_cast<CuteQSGSoftwarePixmapRendererCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QSGRenderer::preprocess();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGSoftwarePixmapRendererCall9 call = reinterpret_cast<CuteQSGSoftwarePixmapRendererCall9>(taken[9]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGSoftwarePixmapRendererCall10 call = reinterpret_cast<CuteQSGSoftwarePixmapRendererCall10>(taken[10]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGSoftwarePixmapRendererCall11 call = reinterpret_cast<CuteQSGSoftwarePixmapRendererCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGSoftwarePixmapRendererCall12 call = reinterpret_cast<CuteQSGSoftwarePixmapRendererCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGSoftwarePixmapRendererCall13 call = reinterpret_cast<CuteQSGSoftwarePixmapRendererCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGSoftwarePixmapRendererCall14 call = reinterpret_cast<CuteQSGSoftwarePixmapRendererCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGSoftwarePixmapRendererCall15 call = reinterpret_cast<CuteQSGSoftwarePixmapRendererCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QSGSoftwarePixmapRenderer::QSGSoftwarePixmapRenderer(QSGRenderContext
//      *context)
extern "C" Q_DECL_EXPORT
QSGSoftwarePixmapRenderer *ritual_ZN25QSGSoftwarePixmapRendererC1EP16QSGRenderContext(
    QSGRenderContext *context) {
  return new CuteQSGSoftwarePixmapRenderer(context);
}

//  QSGSoftwarePixmapRenderer::~QSGSoftwarePixmapRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGSoftwarePixmapRendererD1Ev(
    QSGSoftwarePixmapRenderer *self) {
  delete self;
}

//  void QSGSoftwarePixmapRenderer::renderScene()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGSoftwarePixmapRenderer11renderSceneEv(
    QSGSoftwarePixmapRenderer *self) {
  self->renderScene();
}

//  void QSGSoftwarePixmapRenderer::render()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGSoftwarePixmapRenderer6renderEv(
    QSGSoftwarePixmapRenderer *self) {
  self->render();
}

//  void QSGSoftwarePixmapRenderer::setProjectionRect(const QRect
//      &projectionRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSGSoftwarePixmapRenderer17setProjectionRectERK5QRect(
    QSGSoftwarePixmapRenderer *self,
    const QRect *projectionRect) {
  self->setProjectionRect(*projectionRect);
}

//  a Python function taken by a CuteQSGSoftwarePixmapRenderer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGSoftwarePixmapRenderer(
    QSGSoftwarePixmapRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGSoftwarePixmapRenderer *>(self)->take(key, call);
}
