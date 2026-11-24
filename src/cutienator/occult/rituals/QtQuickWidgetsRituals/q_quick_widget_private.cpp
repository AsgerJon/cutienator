//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickWidgets/6.12.0/QtQuickWidgets/private/qquickwidget_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickWidgets/qquickwidget.h>
#include <QtQuickWidgets/QtQuickWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickWidgets/6.12.0/QtQuickWidgets/private/qquickwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qsurfaceformat.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qsize.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickWidgets/qquickwidget.h>
#include <QtQuickWidgets/private/qquickwidget_p.h>
#include <QtQuickWidgets/private/qaccessiblequickwidgetfactory_p.h>
#include <QtWidgets/private/qwidgetrepaintmanager_p.h>
#include <QtQuick/private/qquickwindow_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qquickitemchangelistener_p.h>
#include <QtQuick/private/qquickrendercontrol_p.h>
#include <QtQuick/private/qsgrhisupport_p.h>
#include <QtQuick/private/qsgsoftwarerenderer_p.h>
#include <QtQml/private/qqmldebugconnector_p.h>
#include <QtQuick/private/qquickprofiler_p.h>
#include <QtQml/private/qqmldebugserviceinterfaces_p.h>
#include <QtQml/qqmlengine.h>
#include <QtQml/qqmlcomponent.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtCore/qbasictimer.h>
#include <QtGui/QOffscreenSurface>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qpa/qplatformintegration.h>
#include <QtGui/QPainter>
#include <QtQuick/QSGRendererInterface>
#ifdef Q_OS_WIN
#if QT_CONFIG(messagebox)
#  include <QtWidgets/QMessageBox>
#endif
#  include <QtCore/QLibraryInfo>
#  include <QtCore/qt_windows.h>
#endif
#include <QtQuick/qquickgraphicsdevice.h>
#include <QtQuick/qquickrendertarget.h>
#include <QtWidgets/private/qwidget_p.h>
#if QT_CONFIG(graphicsview)
#include <QtWidgets/qgraphicsscene.h>
#include <QtWidgets/qgraphicsview.h>
#endif
#if QT_CONFIG(vulkan)
#include <QtGui/private/qvulkandefaultinstance_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickwidgets/qquickwidget.cpp, line 357, as _ZN19QQuickWidgetPrivate13executeHelperEv
inline void QQuickWidgetPrivate::executeHelper()
{
    ensureEngine();

    if (root) {
        delete root;
        root = nullptr;
    }
    if (component) {
        delete component;
        component = nullptr;
    }
}

//  from ../qtdeclarative/src/quickwidgets/qquickwidget.cpp, line 371, as _ZN19QQuickWidgetPrivate7destroyEv
inline void QQuickWidgetPrivate::destroy()
{
    Q_Q(QQuickWidget);
    invalidateRenderControl();
    q->destroyFramebufferObject();
    delete offscreenWindow;
    delete renderControl;
    offscreenRenderer.reset();
}

//  from ../qtdeclarative/src/quickwidgets/qquickwidget.cpp, line 381, as _ZN19QQuickWidgetPrivate7executeEv
inline void QQuickWidgetPrivate::execute()
{
    Q_Q(QQuickWidget);
    executeHelper();

    if (!source.isEmpty()) {
        component = new QQmlComponent(engine.data(), source, q);
        if (!component->isLoading()) {
            q->continueExecute();
        } else {
            QObject::connect(component, SIGNAL(statusChanged(QQmlComponent::Status)),
                             q, SLOT(continueExecute()));
        }
    }
}

//  from ../qtdeclarative/src/quickwidgets/qquickwidget.cpp, line 397, as _ZN19QQuickWidgetPrivate7executeE14QAnyStringViewS0_
inline void QQuickWidgetPrivate::execute(QAnyStringView uri, QAnyStringView typeName)
{
    Q_Q(QQuickWidget);
    executeHelper();

    component = new QQmlComponent(engine.data(), uri, typeName, q);
    if (!component->isLoading()) {
        q->continueExecute();
    } else {
        QObject::connect(component, SIGNAL(statusChanged(QQmlComponent::Status)),
                         q, SLOT(continueExecute()));
    }
}

//  from ../qtdeclarative/src/quickwidgets/qquickwidget.cpp, line 411, as _ZN19QQuickWidgetPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF
inline void QQuickWidgetPrivate::itemGeometryChanged(QQuickItem *resizeItem, QQuickGeometryChange change,
                                              const QRectF &oldGeometry)
{
    Q_Q(QQuickWidget);
    if (resizeItem == root && resizeMode == QQuickWidget::SizeViewToRootObject) {
        // wait for both width and height to be changed
        resizetimer.start(0,q);
    }
    QQuickItemChangeListener::itemGeometryChanged(resizeItem, change, oldGeometry);
}

//  from ../qtdeclarative/src/quickwidgets/qquickwidget.cpp, line 1006, as _ZN19QQuickWidgetPrivate10initResizeEv
inline void QQuickWidgetPrivate::initResize()
{
    if (root) {
        if (resizeMode == QQuickWidget::SizeViewToRootObject) {
            QQuickItemPrivate *p = QQuickItemPrivate::get(root);
            p->addItemChangeListener(this, QQuickItemPrivate::Geometry);
        }
    }
    updateSize();
}

//  from ../qtdeclarative/src/quickwidgets/qquickwidget.cpp, line 1017, as _ZN19QQuickWidgetPrivate10updateSizeEv
inline void QQuickWidgetPrivate::updateSize()
{
    Q_Q(QQuickWidget);
    if (!root)
        return;

    if (resizeMode == QQuickWidget::SizeViewToRootObject) {
        QSize newSize = QSize(root->width(), root->height());
        if (newSize.isValid()) {
            if (newSize != q->size()) {
                q->resize(newSize);
                q->updateGeometry();
            } else if (offscreenWindow->size().isEmpty()) {
                // QQuickDeliveryAgentPrivate::deliverHoverEvent() ignores events that
                // occur outside of QQuickRootItem's geometry, so we need it to match root's size.
                offscreenWindow->resize(newSize);
                offscreenWindow->contentItem()->setSize(newSize);
            }
        }
    } else if (resizeMode == QQuickWidget::SizeRootObjectToView) {
        const bool needToUpdateWidth = !qFuzzyCompare(q->width(), root->width());
        const bool needToUpdateHeight = !qFuzzyCompare(q->height(), root->height());

        if (needToUpdateWidth && needToUpdateHeight) {
            // Make sure that we have realistic sizing behavior by following
            // what on-screen windows would do and resize everything, not just
            // the root item. We do this because other types may be relying on
            // us to behave correctly.
            const QSizeF newSize(q->width(), q->height());
            offscreenWindow->resize(newSize.toSize());
            offscreenWindow->contentItem()->setSize(newSize);
            root->setSize(newSize);
        } else if (needToUpdateWidth) {
            const int newWidth = q->width();
            offscreenWindow->setWidth(newWidth);
            offscreenWindow->contentItem()->setWidth(newWidth);
            root->setWidth(newWidth);
        } else if (needToUpdateHeight) {
            const int newHeight = q->height();
            offscreenWindow->setHeight(newHeight);
            offscreenWindow->contentItem()->setHeight(newHeight);
            root->setHeight(newHeight);
        }
    }
}

//  from ../qtdeclarative/src/quickwidgets/qquickwidget.cpp, line 1068, as _ZN19QQuickWidgetPrivate14updatePositionEv
inline void QQuickWidgetPrivate::updatePosition()
{
    Q_Q(QQuickWidget);
    if (offscreenWindow == nullptr)
        return;

    const QPoint &pos = q->mapToGlobal(QPoint(0, 0));
    if (offscreenWindow->position() != pos)
        offscreenWindow->setPosition(pos);
}

//  from ../qtdeclarative/src/quickwidgets/qquickwidget.cpp, line 1402, as _ZN19QQuickWidgetPrivate13setRootObjectEP7QObject
inline bool QQuickWidgetPrivate::setRootObject(QObject *obj)
{
    Q_Q(QQuickWidget);
    if (root == obj)
        return true;

    if (QQuickItem *sgItem = qobject_cast<QQuickItem *>(obj)) {
        root = sgItem;
        sgItem->setParentItem(offscreenWindow->contentItem());
    } else if (qobject_cast<QWindow *>(obj)) {
        qWarning() << "QQuickWidget does not support using windows as a root item." << Qt::endl
                   << Qt::endl
                   << "If you wish to create your root window from QML, consider using QQmlApplicationEngine instead." << Qt::endl;
    } else {
        qWarning() << "QQuickWidget only supports loading of root objects that derive from QQuickItem." << Qt::endl
                   << Qt::endl
                   << "Ensure your QML code is written for QtQuick 2, and uses a root that is or" << Qt::endl
                   << "inherits from QtQuick's Item (not a Timer, QtObject, etc)." << Qt::endl;
        delete obj;
        root = nullptr;
    }
    if (root) {
        initialSize = rootObjectSize();
        bool resized = q->testAttribute(Qt::WA_Resized);
        if ((resizeMode == QQuickWidget::SizeViewToRootObject || !resized) &&
            initialSize != q->size()) {
            q->resize(initialSize);
        }
        initResize();
        return true;
    }

    return false;
}

//  from ../qtdeclarative/src/quickwidgets/qquickwidget.cpp, line 1097, as _ZN19QQuickWidgetPrivate28handleContextCreationFailureERK14QSurfaceFormat
#if defined(Q_OS_LINUX)
inline void QQuickWidgetPrivate::handleContextCreationFailure(const QSurfaceFormat &)
{
    Q_Q(QQuickWidget);

    QString translatedMessage;
    QString untranslatedMessage;
    QQuickWindowPrivate::rhiCreationFailureMessage(QLatin1String("QRhi"), &translatedMessage, &untranslatedMessage);

    static const QMetaMethod errorSignal = QMetaMethod::fromSignal(&QQuickWidget::sceneGraphError);
    const bool signalConnected = q->isSignalConnected(errorSignal);
    if (signalConnected)
        emit q->sceneGraphError(QQuickWindow::ContextNotAvailable, translatedMessage);

#if defined(Q_OS_WIN) && QT_CONFIG(messagebox)
    if (!signalConnected && !QLibraryInfo::isDebugBuild() && !GetConsoleWindow())
        QMessageBox::critical(q, QCoreApplication::applicationName(), translatedMessage);
#endif // Q_OS_WIN
    if (!signalConnected)
        qFatal("%s", qPrintable(untranslatedMessage));
}
#endif  // defined(Q_OS_LINUX)

//  from ../qtdeclarative/src/quickwidgets/qquickwidget.cpp, line 1457, as _ZNK19QQuickWidgetPrivate7textureEv
inline QWidgetPrivate::TextureData QQuickWidgetPrivate::texture() const
{
    return { outputTexture, nullptr };
}

//  from ../qtdeclarative/src/quickwidgets/qquickwidget.cpp, line 1462, as _ZN19QQuickWidgetPrivate16textureListFlagsEv
inline QPlatformTextureList::Flags QQuickWidgetPrivate::textureListFlags()
{
    QPlatformTextureList::Flags flags = QWidgetPrivate::textureListFlags();
    flags |= QPlatformTextureList::NeedsPremultipliedAlphaBlending;
    return flags;
}

//  from ../qtdeclarative/src/quickwidgets/qquickwidget.cpp, line 510, as _ZN19QQuickWidgetPrivate15grabFramebufferEv
inline QImage QQuickWidgetPrivate::grabFramebuffer()
{
    if (!useSoftwareRenderer && !rhi)
        return QImage();

    // grabWindow() does not work for the rhi case, we are in control of the
    // render target, and so it is up to us to read it back. When the software
    // renderer is in use, just call grabWindow().

    if (outputTexture) {
        render(true);
        QRhiCommandBuffer *cb = nullptr;
        rhi->beginOffscreenFrame(&cb);
        QRhiResourceUpdateBatch *resUpd = rhi->nextResourceUpdateBatch();
        QRhiReadbackResult readResult;
        resUpd->readBackTexture(QRhiReadbackDescription(outputTexture), &readResult);
        cb->resourceUpdate(resUpd);
        rhi->endOffscreenFrame();
        if (!readResult.data.isEmpty()) {
            QImage wrapperImage(reinterpret_cast<const uchar *>(readResult.data.constData()),
                                readResult.pixelSize.width(), readResult.pixelSize.height(),
                                QImage::Format_RGBA8888_Premultiplied);
            if (rhi->isYUpInFramebuffer())
                return wrapperImage.flipped();
            else
                return wrapperImage.copy();
        }
        return QImage();
    }

    return offscreenWindow->grabWindow();
}

//  from ../qtdeclarative/src/quickwidgets/qquickwidget.cpp, line 269, as _ZNK19QQuickWidgetPrivate12ensureEngineEv
inline void QQuickWidgetPrivate::ensureEngine() const
{
    Q_Q(const QQuickWidget);
    if (!engine.isNull())
        return;

    engine = new QQmlEngine(const_cast<QQuickWidget*>(q));
    engine.data()->setIncubationController(offscreenWindow->incubationController());
}

//  from ../qtdeclarative/src/quickwidgets/qquickwidget.cpp, line 289, as _ZN19QQuickWidgetPrivate25handleWindowAboutToChangeEv
inline void QQuickWidgetPrivate::handleWindowAboutToChange()
{
    Q_Q(QQuickWidget);
    if (rhi)
        rhi->removeCleanupCallback(q);

    invalidateRenderControl();
    deviceLost = true;
    rhi = nullptr;
}

//  from ../qtdeclarative/src/quickwidgets/qquickwidget.cpp, line 279, as _ZN19QQuickWidgetPrivate23invalidateRenderControlEv
inline void QQuickWidgetPrivate::invalidateRenderControl()
{
    if (!useSoftwareRenderer && rhi) {
        // For the user's own OpenGL code connected to some QQuickWindow signals.
        rhi->makeThreadLocalNativeContextCurrent();
    }

    renderControl->invalidate();
}

//  from ../qtdeclarative/src/quickwidgets/qquickwidget.cpp, line 1079, as _ZNK19QQuickWidgetPrivate14rootObjectSizeEv
inline QSize QQuickWidgetPrivate::rootObjectSize() const
{
    QSize rootObjectSize(0,0);
    int widthCandidate = -1;
    int heightCandidate = -1;
    if (root) {
        widthCandidate = root->width();
        heightCandidate = root->height();
    }
    if (widthCandidate > 0) {
        rootObjectSize.setWidth(widthCandidate);
    }
    if (heightCandidate > 0) {
        rootObjectSize.setHeight(heightCandidate);
    }
    return rootObjectSize;
}
//  -----------------------------------------------------------------------

//  A QQuickWidgetPrivate that Python can take functions over in. Every QQuickWidgetPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickWidgetPrivateCall0)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQQuickWidgetPrivateCall1)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQQuickWidgetPrivateCall2)(const void *, int *);
typedef int (*CuteQQuickWidgetPrivateCall3)(const void *, int *);
typedef const QImage * (*CuteQQuickWidgetPrivateCall4)(const void *, int *);
typedef void (*CuteQQuickWidgetPrivateCall5)(const void *, bool, int *);
typedef void (*CuteQQuickWidgetPrivateCall6)(const void *, int, int *);
typedef void (*CuteQQuickWidgetPrivateCall7)(const void *, int *);
typedef void (*CuteQQuickWidgetPrivateCall8)(const void *, int *);
typedef void * (*CuteQQuickWidgetPrivateCall9)(const void *, int *);
typedef void (*CuteQQuickWidgetPrivateCall10)(const void *, int *);
typedef void (*CuteQQuickWidgetPrivateCall11)(const void *, int *);
typedef void (*CuteQQuickWidgetPrivateCall12)(const void *, int *);
typedef void (*CuteQQuickWidgetPrivateCall13)(const void *, int *);
typedef void (*CuteQQuickWidgetPrivateCall14)(const void *, int *);
typedef void (*CuteQQuickWidgetPrivateCall15)(const void *, int *);
typedef void (*CuteQQuickWidgetPrivateCall16)(const void *, int *);
typedef bool (*CuteQQuickWidgetPrivateCall17)(const void *, int *);
typedef bool (*CuteQQuickWidgetPrivateCall18)(const void *, int *);
class CuteQQuickWidgetPrivate : public QQuickWidgetPrivate {
public:
  using QQuickWidgetPrivate::QQuickWidgetPrivate;
  void *taken[19] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QQuickWidgetPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate9rhiConfigEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate7textureEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate16textureListFlagsEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15grabFramebufferEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10setVisibleEb")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14aboutToDestroyEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate8recreateEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate11focusObjectEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25beginBackingStorePaintingEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate23endBackingStorePaintingEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate12beginComposeEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10endComposeEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate29initializeViewportFramebufferEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25resizeViewportFramebufferEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14resolveSamplesEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15isStereoEnabledEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate24toggleStereoTargetBufferEv")) {
      taken[18] = call;
      return true;
    }
    return false;
  }

  //  void QQuickWidgetPrivate::itemGeometryChanged(QQuickItem *item,
  //      QQuickGeometryChange change, const QRectF &oldGeometry)
  void itemGeometryChanged(
      QQuickItem *item,
      QQuickGeometryChange change,
      const QRectF &oldGeometry) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickWidgetPrivateCall0 call = reinterpret_cast<CuteQQuickWidgetPrivateCall0>(taken[0]);
      call(this, item, &change, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickWidgetPrivate::itemGeometryChanged(item, change, oldGeometry);
  }

  //  QPlatformBackingStoreRhiConfig QQuickWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickWidgetPrivateCall1 call = reinterpret_cast<CuteQQuickWidgetPrivateCall1>(taken[1]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickWidgetPrivate::rhiConfig();
  }

  //  TextureData QQuickWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickWidgetPrivateCall2 call = reinterpret_cast<CuteQQuickWidgetPrivateCall2>(taken[2]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QQuickWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickWidgetPrivateCall3 call = reinterpret_cast<CuteQQuickWidgetPrivateCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QQuickWidgetPrivate::textureListFlags();
  }

  //  QImage QQuickWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickWidgetPrivateCall4 call = reinterpret_cast<CuteQQuickWidgetPrivateCall4>(taken[4]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::setVisible(bool a0)
  void setVisible(bool a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickWidgetPrivateCall5 call = reinterpret_cast<CuteQQuickWidgetPrivateCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickWidgetPrivateCall6 call = reinterpret_cast<CuteQQuickWidgetPrivateCall6>(taken[6]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickWidgetPrivateCall7 call = reinterpret_cast<CuteQQuickWidgetPrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickWidgetPrivateCall8 call = reinterpret_cast<CuteQQuickWidgetPrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickWidgetPrivateCall9 call = reinterpret_cast<CuteQQuickWidgetPrivateCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickWidgetPrivateCall10 call = reinterpret_cast<CuteQQuickWidgetPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickWidgetPrivateCall11 call = reinterpret_cast<CuteQQuickWidgetPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickWidgetPrivateCall12 call = reinterpret_cast<CuteQQuickWidgetPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickWidgetPrivateCall13 call = reinterpret_cast<CuteQQuickWidgetPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickWidgetPrivateCall14 call = reinterpret_cast<CuteQQuickWidgetPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickWidgetPrivateCall15 call = reinterpret_cast<CuteQQuickWidgetPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickWidgetPrivateCall16 call = reinterpret_cast<CuteQQuickWidgetPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickWidgetPrivateCall17 call = reinterpret_cast<CuteQQuickWidgetPrivateCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickWidgetPrivateCall18 call = reinterpret_cast<CuteQQuickWidgetPrivateCall18>(taken[18]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QQuickWidget *QQuickWidgetPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickWidget *ritual_ZN19QQuickWidgetPrivate6q_funcEv(
    QQuickWidgetPrivate *self) {
  return self->q_func();
}

//  const QQuickWidget *QQuickWidgetPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickWidget *ritual_ZNK19QQuickWidgetPrivate6q_funcEv(
    const QQuickWidgetPrivate *self) {
  return self->q_func();
}

//  QQuickWidgetPrivate *QQuickWidgetPrivate::get(QQuickWidget *view)
extern "C" Q_DECL_EXPORT
QQuickWidgetPrivate *ritual_ZN19QQuickWidgetPrivate3getEP12QQuickWidget(
    QQuickWidget *view) {
  return QQuickWidgetPrivate::get(view);
}

//  const QQuickWidgetPrivate *QQuickWidgetPrivate::get(const QQuickWidget
//      *view)
extern "C" Q_DECL_EXPORT
const QQuickWidgetPrivate *ritual_ZN19QQuickWidgetPrivate3getEPK12QQuickWidget(
    const QQuickWidget *view) {
  return QQuickWidgetPrivate::get(view);
}

//  void QQuickWidgetPrivate::executeHelper()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWidgetPrivate13executeHelperEv(
    QQuickWidgetPrivate *self) {
  self->executeHelper();
}

//  void QQuickWidgetPrivate::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWidgetPrivate7destroyEv(QQuickWidgetPrivate *self) {
  self->destroy();
}

//  void QQuickWidgetPrivate::execute()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWidgetPrivate7executeEv(QQuickWidgetPrivate *self) {
  self->execute();
}

//  void QQuickWidgetPrivate::execute(QAnyStringView uri, QAnyStringView
//      typeName)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWidgetPrivate7executeE14QAnyStringViewS0_(
    QQuickWidgetPrivate *self,
    const QString *uri,
    const QString *typeName) {
  self->execute(QAnyStringView(*uri), QAnyStringView(*typeName));
}

//  void QQuickWidgetPrivate::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWidgetPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickWidgetPrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *oldGeometry) {
  self->itemGeometryChanged(item, *change, *oldGeometry);
}

//  void QQuickWidgetPrivate::initResize()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWidgetPrivate10initResizeEv(
    QQuickWidgetPrivate *self) {
  self->initResize();
}

//  void QQuickWidgetPrivate::updateSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWidgetPrivate10updateSizeEv(
    QQuickWidgetPrivate *self) {
  self->updateSize();
}

//  void QQuickWidgetPrivate::updatePosition()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWidgetPrivate14updatePositionEv(
    QQuickWidgetPrivate *self) {
  self->updatePosition();
}

//  bool QQuickWidgetPrivate::setRootObject(QObject *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQuickWidgetPrivate13setRootObjectEP7QObject(
    QQuickWidgetPrivate *self,
    QObject *a0) {
  return self->setRootObject(a0);
}

#if defined(Q_OS_LINUX)
//  void QQuickWidgetPrivate::handleContextCreationFailure(const
//      QSurfaceFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWidgetPrivate28handleContextCreationFailureERK14QSurfaceFormat(
    QQuickWidgetPrivate *self,
    const QSurfaceFormat *format) {
  self->handleContextCreationFailure(*format);
}
#endif  // defined(Q_OS_LINUX)

//  TextureData QQuickWidgetPrivate::texture() const
extern "C" Q_DECL_EXPORT
QWidgetPrivate::TextureData *ritual_ZNK19QQuickWidgetPrivate7textureEv(
    const QQuickWidgetPrivate *self) {
  return new QWidgetPrivate::TextureData(self->texture());
}

//  QPlatformTextureList::Flags QQuickWidgetPrivate::textureListFlags()
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQuickWidgetPrivate16textureListFlagsEv(
    QQuickWidgetPrivate *self) {
  return static_cast<int>(self->textureListFlags().toInt());
}

//  QImage QQuickWidgetPrivate::grabFramebuffer()
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN19QQuickWidgetPrivate15grabFramebufferEv(
    QQuickWidgetPrivate *self) {
  return new QImage(self->grabFramebuffer());
}

//  void QQuickWidgetPrivate::ensureEngine() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QQuickWidgetPrivate12ensureEngineEv(
    const QQuickWidgetPrivate *self) {
  self->ensureEngine();
}

//  void QQuickWidgetPrivate::handleWindowAboutToChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWidgetPrivate25handleWindowAboutToChangeEv(
    QQuickWidgetPrivate *self) {
  self->handleWindowAboutToChange();
}

//  void QQuickWidgetPrivate::invalidateRenderControl()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickWidgetPrivate23invalidateRenderControlEv(
    QQuickWidgetPrivate *self) {
  self->invalidateRenderControl();
}

//  QSize QQuickWidgetPrivate::rootObjectSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QQuickWidgetPrivate14rootObjectSizeEv(
    const QQuickWidgetPrivate *self) {
  return new QSize(self->rootObjectSize());
}

//  a Python function taken by a CuteQQuickWidgetPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWidgetPrivate(
    QQuickWidgetPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWidgetPrivate *>(self)->take(key, call);
}

//  void QQuickWidgetPrivate::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickWidgetPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickWidgetPrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *oldGeometry) {
  self->QQuickWidgetPrivate::itemGeometryChanged(
      item,
      *change,
      *oldGeometry);
}

//  TextureData QQuickWidgetPrivate::texture() const
extern "C" Q_DECL_EXPORT
QWidgetPrivate::TextureData *ritual_own_ZNK19QQuickWidgetPrivate7textureEv(
    const QQuickWidgetPrivate *self) {
  return new QWidgetPrivate::TextureData(
      self->QQuickWidgetPrivate::texture());
}

//  QPlatformTextureList::Flags QQuickWidgetPrivate::textureListFlags()
extern "C" Q_DECL_EXPORT
int ritual_own_ZN19QQuickWidgetPrivate16textureListFlagsEv(
    QQuickWidgetPrivate *self) {
  return static_cast<int>(
      self->QQuickWidgetPrivate::textureListFlags().toInt());
}
