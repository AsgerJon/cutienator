//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qmdisubwindow_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(mdiarea)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qmdisubwindow.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qmdisubwindow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/qpalette.h>
#include <QtCore/qstring.h>
#include <QtWidgets/qstyleoption.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qmdisubwindow_p.h"
#include <QApplication>
#include <QStylePainter>
#include <QVBoxLayout>
#include <QMouseEvent>
#if QT_CONFIG(whatsthis)
#include <QWhatsThis>
#endif
#if QT_CONFIG(tooltip)
#include <QToolTip>
#endif
#if QT_CONFIG(mainwindow)
#include <QMainWindow>
#endif
#include <QScrollBar>
#include <QDebug>
#include <QMdiArea>
#include <QScopedValueRollback>
#if QT_CONFIG(action)
#  include <qaction.h>
#endif
#if QT_CONFIG(menu)
#include <QMenu>
#endif
#include <QProxyStyle>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qmdisubwindow.cpp, line 889, as _ZN20QMdiSubWindowPrivate23_q_updateStaysOnTopHintEv
inline void QMdiSubWindowPrivate::_q_updateStaysOnTopHint()
{
#if QT_CONFIG(action)
    Q_Q(QMdiSubWindow);
    if (QAction *senderAction = qobject_cast<QAction *>(q->sender())) {
        if (senderAction->isChecked()) {
            q->setWindowFlags(q->windowFlags() | Qt::WindowStaysOnTopHint);
            q->raise();
        } else {
            q->setWindowFlags(q->windowFlags() & ~Qt::WindowStaysOnTopHint);
            q->lower();
        }
    }
#endif // QT_CONFIG(action)
}

//  from src/widgets/widgets/qmdisubwindow.cpp, line 987, as _ZN20QMdiSubWindowPrivate16removeBaseWidgetEv
inline void QMdiSubWindowPrivate::removeBaseWidget()
{
    if (!baseWidget)
        return;

    Q_Q(QMdiSubWindow);
    baseWidget->removeEventFilter(q);
    if (layout)
        layout->removeWidget(baseWidget);
    if (baseWidget->windowTitle() == q->windowTitle()) {
        ignoreWindowTitleChange = true;
        q->setWindowTitle(QString());
        ignoreWindowTitleChange = false;
        q->setWindowModified(false);
    }
    lastChildWindowTitle.clear();
    // QTBUG-47993: parent widget can be reset before this call
    if (baseWidget->parentWidget() == q)
        baseWidget->setParent(nullptr);
    baseWidget = nullptr;
    isWidgetHiddenByUs = false;
}

//  from src/widgets/widgets/qmdisubwindow.cpp, line 1013, as _ZN20QMdiSubWindowPrivate16initOperationMapEv
inline void QMdiSubWindowPrivate::initOperationMap()
{
    operationMap.insert(Move, OperationInfo(HMove | VMove, Qt::ArrowCursor, false));
    operationMap.insert(TopResize, OperationInfo(VMove | VResize | VResizeReverse, Qt::SizeVerCursor));
    operationMap.insert(BottomResize, OperationInfo(VResize, Qt::SizeVerCursor));
    operationMap.insert(LeftResize, OperationInfo(HMove | HResize | HResizeReverse, Qt::SizeHorCursor));
    operationMap.insert(RightResize, OperationInfo(HResize, Qt::SizeHorCursor));
    operationMap.insert(TopLeftResize, OperationInfo(HMove | VMove | HResize | VResize | VResizeReverse
                                                     | HResizeReverse, Qt::SizeFDiagCursor));
    operationMap.insert(TopRightResize, OperationInfo(VMove | HResize | VResize
                                                      | VResizeReverse, Qt::SizeBDiagCursor));
    operationMap.insert(BottomLeftResize, OperationInfo(HMove | HResize | VResize | HResizeReverse,
                                                        Qt::SizeBDiagCursor));
    operationMap.insert(BottomRightResize, OperationInfo(HResize | VResize, Qt::SizeFDiagCursor));
}

//  from src/widgets/widgets/qmdisubwindow.cpp, line 1599, as _ZNK20QMdiSubWindowPrivate12getOperationERK6QPoint
inline QMdiSubWindowPrivate::Operation QMdiSubWindowPrivate::getOperation(const QPoint &pos) const
{
    OperationInfoMap::const_iterator it;
    for (it = operationMap.constBegin(); it != operationMap.constEnd(); ++it)
        if (it.value().region.contains(pos))
            return it.key();
    return None;
}

//  from src/widgets/widgets/qmdisubwindow.cpp, line 1668, as _ZN20QMdiSubWindowPrivate17ensureWindowStateEN2Qt11WindowStateE
inline void QMdiSubWindowPrivate::ensureWindowState(Qt::WindowState state)
{
    Q_Q(QMdiSubWindow);
    Qt::WindowStates windowStates = q->windowState() | state;
    switch (state) {
    case Qt::WindowMinimized:
        windowStates &= ~Qt::WindowMaximized;
        windowStates &= ~Qt::WindowFullScreen;
        windowStates &= ~Qt::WindowNoState;
        break;
    case Qt::WindowMaximized:
        windowStates &= ~Qt::WindowMinimized;
        windowStates &= ~Qt::WindowFullScreen;
        windowStates &= ~Qt::WindowNoState;
        break;
    case Qt::WindowNoState:
        windowStates &= ~Qt::WindowMinimized;
        windowStates &= ~Qt::WindowMaximized;
        windowStates &= ~Qt::WindowFullScreen;
        break;
    default:
        break;
    }
    if (baseWidget) {
        if (!(baseWidget->windowState() & Qt::WindowActive) && windowStates & Qt::WindowActive)
            baseWidget->overrideWindowState(windowStates & ~Qt::WindowActive);
        else
            baseWidget->overrideWindowState(windowStates);
    }
    q->overrideWindowState(windowStates);
}

//  from src/widgets/widgets/qmdisubwindow.cpp, line 1894, as _ZN20QMdiSubWindowPrivate19leaveRubberBandModeEv
#if QT_CONFIG(rubberband)
inline void QMdiSubWindowPrivate::leaveRubberBandMode()
{
    Q_Q(QMdiSubWindow);
    Q_ASSERT(rubberBand);
    Q_ASSERT(isInRubberBandMode);
    q->releaseMouse();
    isInRubberBandMode = false;
    q->setGeometry(rubberBand->geometry());
    rubberBand->hide();
    currentOperation = None;
}
#endif  // QT_CONFIG(rubberband)

//  from src/widgets/widgets/qmdisubwindow.cpp, line 1908, as _ZNK20QMdiSubWindowPrivate14desktopPaletteEv
inline QPalette QMdiSubWindowPrivate::desktopPalette() const
{
    Q_Q(const QMdiSubWindow);
    QPalette newPalette = q->palette();

    newPalette.setColor(QPalette::Active, QPalette::Highlight,
                        newPalette.color(QPalette::Active, QPalette::Highlight));
    newPalette.setColor(QPalette::Active, QPalette::Base,
                        newPalette.color(QPalette::Active, QPalette::Highlight));
    newPalette.setColor(QPalette::Inactive, QPalette::Highlight,
                        newPalette.color(QPalette::Inactive, QPalette::Dark));
    newPalette.setColor(QPalette::Inactive, QPalette::Base,
                        newPalette.color(QPalette::Inactive, QPalette::Dark));
    newPalette.setColor(QPalette::Inactive, QPalette::HighlightedText,
                        newPalette.color(QPalette::Inactive, QPalette::Window));

    return newPalette;
}

//  from src/widgets/widgets/qmdisubwindow.cpp, line 1965, as _ZN20QMdiSubWindowPrivate14setFocusWidgetEv
inline void QMdiSubWindowPrivate::setFocusWidget()
{
    Q_Q(QMdiSubWindow);
    if (!baseWidget) {
        q->setFocus();
        return;
    }

    // This will give focus to the next child if possible, otherwise
    // do nothing, hence it's not possible to tab between windows with
    // just hitting tab (unless Qt::TabFocus is removed from the focus policy).
    if (focusInReason == Qt::TabFocusReason) {
        q->focusNextChild();
        return;
    }

    // Same as above, but gives focus to the previous child.
    if (focusInReason == Qt::BacktabFocusReason) {
        q->focusPreviousChild();
        return;
    }

    if (!(q->windowState() & Qt::WindowMinimized) && restoreFocus())
        return;

    if (QWidget *focusWidget = baseWidget->focusWidget()) {
        if (!focusWidget->hasFocus() && q->isAncestorOf(focusWidget)
                && focusWidget->isVisible() && !q->isMinimized()
                && focusWidget->focusPolicy() != Qt::NoFocus) {
            focusWidget->setFocus();
        } else {
            q->setFocus();
        }
        return;
    }

    QWidget *focusWidget = q->nextInFocusChain();
    while (focusWidget && focusWidget != q && focusWidget->focusPolicy() == Qt::NoFocus)
        focusWidget = focusWidget->nextInFocusChain();
    if (focusWidget && q->isAncestorOf(focusWidget))
        focusWidget->setFocus();
    else if (baseWidget->focusPolicy() != Qt::NoFocus)
        baseWidget->setFocus();
    else if (!q->hasFocus())
        q->setFocus();
}

//  from src/widgets/widgets/qmdisubwindow.cpp, line 2012, as _ZN20QMdiSubWindowPrivate12restoreFocusEv
inline bool QMdiSubWindowPrivate::restoreFocus()
{
    if (restoreFocusWidget.isNull())
        return false;
    QWidget *candidate = restoreFocusWidget;
    restoreFocusWidget.clear();
    if (!candidate->hasFocus() && q_func()->isAncestorOf(candidate)
        && candidate->isVisible()
        && candidate->focusPolicy() != Qt::NoFocus) {
        candidate->setFocus();
        return true;
    }
    return candidate->hasFocus();
}

//  from src/widgets/widgets/qmdisubwindow.cpp, line 1317, as _ZN20QMdiSubWindowPrivate16storeFocusWidgetEv
inline void QMdiSubWindowPrivate::storeFocusWidget()
{
    if (QWidget *focus = QApplication::focusWidget()) {
        if (!restoreFocusWidget && q_func()->isAncestorOf(focus))
            restoreFocusWidget = focus;
    }
}

//  from src/widgets/widgets/qmdisubwindow.cpp, line 2098, as _ZN20QMdiSubWindowPrivate10setEnabledENS_17WindowStateActionEb
#if !defined(QT_NO_ACTION)
inline void QMdiSubWindowPrivate::setEnabled(WindowStateAction action, bool enable)
{
    if (actions[action])
        actions[action]->setEnabled(enable);
}
#endif  // !defined(QT_NO_ACTION)

//  from src/widgets/widgets/qmdisubwindow.cpp, line 2105, as _ZN20QMdiSubWindowPrivate15addToSystemMenuENS_17WindowStateActionERK7QStringPKc
#if !defined(QT_NO_ACTION)
#if QT_CONFIG(menu)
inline void QMdiSubWindowPrivate::addToSystemMenu(WindowStateAction action, const QString &text,
                                           const char *slot)
{
    if (!systemMenu)
        return;
    actions[action] = systemMenu->addAction(text, q_func(), slot);
}
#endif  // QT_CONFIG(menu)
#endif  // !defined(QT_NO_ACTION)

//  from src/widgets/widgets/qmdisubwindow.cpp, line 2160, as _ZNK20QMdiSubWindowPrivate18setSizeGripVisibleEb
#if QT_CONFIG(sizegrip)
inline void QMdiSubWindowPrivate::setSizeGripVisible(bool visible) const
{
    // See if we can find any size grips
    const QList<QSizeGrip *> sizeGrips = q_func()->findChildren<QSizeGrip *>();
    for (QSizeGrip *grip : sizeGrips)
        grip->setVisible(visible);
}
#endif  // QT_CONFIG(sizegrip)

//  from src/widgets/widgets/qmdisubwindow.cpp, line 235, as _ZNK20QMdiSubWindowPrivate25originalWindowTitleHelperEv
inline QString QMdiSubWindowPrivate::originalWindowTitleHelper() const
{
    Q_Q(const QMdiSubWindow);
    // QTBUG-92240: When DontMaximizeSubWindowOnActivation is set and
    // there is another subwindow maximized, use its original title.
    if (auto *mdiArea = q->mdiArea()) {
        const auto &subWindows = mdiArea->subWindowList();
        for (auto *subWindow : subWindows) {
            if (subWindow != q && subWindow->isMaximized()) {
                auto *subWindowD = static_cast<QMdiSubWindowPrivate *>(qt_widget_private(subWindow));
                if (!subWindowD->originalTitle.isNull())
                    return subWindowD->originalTitle;
            }
        }
    }
    return q->window()->windowTitle();
}
//  -----------------------------------------------------------------------

//  A QMdiSubWindowPrivate that Python can take functions over in. Every QMdiSubWindowPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(mdiarea)
typedef void (*CuteQMdiSubWindowPrivateCall0)(const void *, int, int *);
#endif  // QT_CONFIG(mdiarea)
typedef void (*CuteQMdiSubWindowPrivateCall1)(const void *, bool, int *);
typedef void (*CuteQMdiSubWindowPrivateCall2)(const void *, int *);
typedef void (*CuteQMdiSubWindowPrivateCall3)(const void *, int *);
typedef void * (*CuteQMdiSubWindowPrivateCall4)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQMdiSubWindowPrivateCall5)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQMdiSubWindowPrivateCall6)(const void *, int *);
typedef int (*CuteQMdiSubWindowPrivateCall7)(const void *, int *);
typedef const QImage * (*CuteQMdiSubWindowPrivateCall8)(const void *, int *);
typedef void (*CuteQMdiSubWindowPrivateCall9)(const void *, int *);
typedef void (*CuteQMdiSubWindowPrivateCall10)(const void *, int *);
typedef void (*CuteQMdiSubWindowPrivateCall11)(const void *, int *);
typedef void (*CuteQMdiSubWindowPrivateCall12)(const void *, int *);
typedef void (*CuteQMdiSubWindowPrivateCall13)(const void *, int *);
typedef void (*CuteQMdiSubWindowPrivateCall14)(const void *, int *);
typedef void (*CuteQMdiSubWindowPrivateCall15)(const void *, int *);
typedef bool (*CuteQMdiSubWindowPrivateCall16)(const void *, int *);
typedef bool (*CuteQMdiSubWindowPrivateCall17)(const void *, int *);
class CuteQMdiSubWindowPrivate : public QMdiSubWindowPrivate {
public:
  using QMdiSubWindowPrivate::QMdiSubWindowPrivate;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(mdiarea)
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(mdiarea)
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10setVisibleEb")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14aboutToDestroyEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate8recreateEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate11focusObjectEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate9rhiConfigEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate7textureEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate16textureListFlagsEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15grabFramebufferEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25beginBackingStorePaintingEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate23endBackingStorePaintingEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate12beginComposeEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10endComposeEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate29initializeViewportFramebufferEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25resizeViewportFramebufferEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14resolveSamplesEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15isStereoEnabledEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate24toggleStereoTargetBufferEv")) {
      taken[17] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(mdiarea)
  //  void QMdiSubWindowPrivate::setWindowFlags(Qt::WindowFlags
  //      windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[0]) {
      int handled = 0;
      CuteQMdiSubWindowPrivateCall0 call = reinterpret_cast<CuteQMdiSubWindowPrivateCall0>(taken[0]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QMdiSubWindowPrivate::setWindowFlags(windowFlags);
  }
#endif  // QT_CONFIG(mdiarea)

  //  void QWidgetPrivate::setVisible(bool a0)
  void setVisible(bool a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQMdiSubWindowPrivateCall1 call = reinterpret_cast<CuteQMdiSubWindowPrivateCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[2]) {
      int handled = 0;
      CuteQMdiSubWindowPrivateCall2 call = reinterpret_cast<CuteQMdiSubWindowPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[3]) {
      int handled = 0;
      CuteQMdiSubWindowPrivateCall3 call = reinterpret_cast<CuteQMdiSubWindowPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[4]) {
      int handled = 0;
      CuteQMdiSubWindowPrivateCall4 call = reinterpret_cast<CuteQMdiSubWindowPrivateCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQMdiSubWindowPrivateCall5 call = reinterpret_cast<CuteQMdiSubWindowPrivateCall5>(taken[5]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQMdiSubWindowPrivateCall6 call = reinterpret_cast<CuteQMdiSubWindowPrivateCall6>(taken[6]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[7]) {
      int handled = 0;
      CuteQMdiSubWindowPrivateCall7 call = reinterpret_cast<CuteQMdiSubWindowPrivateCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[8]) {
      int handled = 0;
      CuteQMdiSubWindowPrivateCall8 call = reinterpret_cast<CuteQMdiSubWindowPrivateCall8>(taken[8]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[9]) {
      int handled = 0;
      CuteQMdiSubWindowPrivateCall9 call = reinterpret_cast<CuteQMdiSubWindowPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[10]) {
      int handled = 0;
      CuteQMdiSubWindowPrivateCall10 call = reinterpret_cast<CuteQMdiSubWindowPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[11]) {
      int handled = 0;
      CuteQMdiSubWindowPrivateCall11 call = reinterpret_cast<CuteQMdiSubWindowPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[12]) {
      int handled = 0;
      CuteQMdiSubWindowPrivateCall12 call = reinterpret_cast<CuteQMdiSubWindowPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[13]) {
      int handled = 0;
      CuteQMdiSubWindowPrivateCall13 call = reinterpret_cast<CuteQMdiSubWindowPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[14]) {
      int handled = 0;
      CuteQMdiSubWindowPrivateCall14 call = reinterpret_cast<CuteQMdiSubWindowPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[15]) {
      int handled = 0;
      CuteQMdiSubWindowPrivateCall15 call = reinterpret_cast<CuteQMdiSubWindowPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[16]) {
      int handled = 0;
      CuteQMdiSubWindowPrivateCall16 call = reinterpret_cast<CuteQMdiSubWindowPrivateCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[17]) {
      int handled = 0;
      CuteQMdiSubWindowPrivateCall17 call = reinterpret_cast<CuteQMdiSubWindowPrivateCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QMdiSubWindow *QMdiSubWindowPrivate::q_func()
extern "C" Q_DECL_EXPORT
QMdiSubWindow *ritual_ZN20QMdiSubWindowPrivate6q_funcEv(
    QMdiSubWindowPrivate *self) {
  return self->q_func();
}

//  const QMdiSubWindow *QMdiSubWindowPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QMdiSubWindow *ritual_ZNK20QMdiSubWindowPrivate6q_funcEv(
    const QMdiSubWindowPrivate *self) {
  return self->q_func();
}

//  void QMdiSubWindowPrivate::_q_updateStaysOnTopHint()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMdiSubWindowPrivate23_q_updateStaysOnTopHintEv(
    QMdiSubWindowPrivate *self) {
  self->_q_updateStaysOnTopHint();
}

//  void QMdiSubWindowPrivate::removeBaseWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMdiSubWindowPrivate16removeBaseWidgetEv(
    QMdiSubWindowPrivate *self) {
  self->removeBaseWidget();
}

//  void QMdiSubWindowPrivate::initOperationMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMdiSubWindowPrivate16initOperationMapEv(
    QMdiSubWindowPrivate *self) {
  self->initOperationMap();
}

//  Operation QMdiSubWindowPrivate::getOperation(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
QMdiSubWindowPrivate::Operation ritual_ZNK20QMdiSubWindowPrivate12getOperationERK6QPoint(
    const QMdiSubWindowPrivate *self,
    const QPoint *pos) {
  return self->getOperation(*pos);
}

//  void QMdiSubWindowPrivate::ensureWindowState(Qt::WindowState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMdiSubWindowPrivate17ensureWindowStateEN2Qt11WindowStateE(
    QMdiSubWindowPrivate *self,
    Qt::WindowState state) {
  self->ensureWindowState(state);
}

#if QT_CONFIG(rubberband)
//  void QMdiSubWindowPrivate::leaveRubberBandMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMdiSubWindowPrivate19leaveRubberBandModeEv(
    QMdiSubWindowPrivate *self) {
  self->leaveRubberBandMode();
}
#endif  // QT_CONFIG(rubberband)

//  QPalette QMdiSubWindowPrivate::desktopPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK20QMdiSubWindowPrivate14desktopPaletteEv(
    const QMdiSubWindowPrivate *self) {
  return new QPalette(self->desktopPalette());
}

//  void QMdiSubWindowPrivate::setFocusWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMdiSubWindowPrivate14setFocusWidgetEv(
    QMdiSubWindowPrivate *self) {
  self->setFocusWidget();
}

//  bool QMdiSubWindowPrivate::restoreFocus()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QMdiSubWindowPrivate12restoreFocusEv(
    QMdiSubWindowPrivate *self) {
  return self->restoreFocus();
}

//  void QMdiSubWindowPrivate::storeFocusWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMdiSubWindowPrivate16storeFocusWidgetEv(
    QMdiSubWindowPrivate *self) {
  self->storeFocusWidget();
}

#if !defined(QT_NO_ACTION)
//  void QMdiSubWindowPrivate::setEnabled(WindowStateAction a0, bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMdiSubWindowPrivate10setEnabledENS_17WindowStateActionEb(
    QMdiSubWindowPrivate *self,
    QMdiSubWindowPrivate::WindowStateAction a0,
    bool enable) {
  self->setEnabled(a0, enable);
}
#endif  // !defined(QT_NO_ACTION)

#if !defined(QT_NO_ACTION)
#if QT_CONFIG(menu)
//  void QMdiSubWindowPrivate::addToSystemMenu(WindowStateAction a0, const
//      QString &text, const char *slot)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMdiSubWindowPrivate15addToSystemMenuENS_17WindowStateActionERK7QStringPKc(
    QMdiSubWindowPrivate *self,
    QMdiSubWindowPrivate::WindowStateAction a0,
    const QString *text,
    const char *slot) {
  self->addToSystemMenu(a0, *text, slot);
}
#endif  // QT_CONFIG(menu)
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(sizegrip)
//  void QMdiSubWindowPrivate::setSizeGripVisible(bool visible) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QMdiSubWindowPrivate18setSizeGripVisibleEb(
    const QMdiSubWindowPrivate *self,
    bool visible) {
  self->setSizeGripVisible(visible);
}
#endif  // QT_CONFIG(sizegrip)

//  QString QMdiSubWindowPrivate::originalWindowTitleHelper() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QMdiSubWindowPrivate25originalWindowTitleHelperEv(
    const QMdiSubWindowPrivate *self) {
  return new QString(self->originalWindowTitleHelper());
}

//  void QMdiSubWindowPrivate::setNewGeometry(QRect *geometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMdiSubWindowPrivate14setNewGeometryEP5QRect(
    QMdiSubWindowPrivate *self,
    QRect *geometry) {
  self->setNewGeometry(geometry);
}

//  bool QMdiSubWindowPrivate::hasBorder(const QStyleOptionTitleBar &options)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QMdiSubWindowPrivate9hasBorderERK20QStyleOptionTitleBar(
    const QMdiSubWindowPrivate *self,
    const QStyleOptionTitleBar *options) {
  return self->hasBorder(*options);
}

//  bool QMdiSubWindowPrivate::autoRaise() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QMdiSubWindowPrivate9autoRaiseEv(
    const QMdiSubWindowPrivate *self) {
  return self->autoRaise();
}

//  bool QMdiSubWindowPrivate::isResizeOperation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QMdiSubWindowPrivate17isResizeOperationEv(
    const QMdiSubWindowPrivate *self) {
  return self->isResizeOperation();
}

//  bool QMdiSubWindowPrivate::isMoveOperation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QMdiSubWindowPrivate15isMoveOperationEv(
    const QMdiSubWindowPrivate *self) {
  return self->isMoveOperation();
}

//  a Python function taken by a CuteQMdiSubWindowPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMdiSubWindowPrivate(
    QMdiSubWindowPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMdiSubWindowPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(mdiarea)
