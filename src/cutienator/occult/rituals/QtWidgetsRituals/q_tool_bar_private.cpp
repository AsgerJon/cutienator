//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtoolbar_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(toolbar)
#if QT_CONFIG(toolbar)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qtoolbar.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qtoolbar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qaction.h>
#include <QtWidgets/qwidgetaction.h>
#include <QtWidgets/qtoolbar.h>
#include <QtWidgets/qstyleoption.h>
#if QT_CONFIG(toolbutton)
#include <QtWidgets/qtoolbutton.h>
#endif
#include <QtWidgets/qmenu.h>
#include <QtCore/qdebug.h>
#include <QtCore/qmath.h>
#ifdef Q_OS_MACOS
#include <QtGui/qpa/qplatformnativeinterface.h>
#endif
#include <QtWidgets/private/qmainwindowlayout_p.h>
#if QT_CONFIG(toolbutton)
#include <QtWidgets/private/qtoolbarextension_p.h>
#endif
#include <QtWidgets/private/qtoolbarlayout_p.h>
#include <QtWidgets/private/qtoolbarseparator_p.h>
#include <QtWidgets/private/qmainwindowlayout_p.h>
#if QT_CONFIG(dockwidget)
#include <QtWidgets/private/qdockarealayout_p.h>
#include <QtWidgets/qdockwidget.h>
#include <QtWidgets/private/qdockwidget_p.h>
#endif
#if QT_CONFIG(toolbar)
#include <QtWidgets/private/qtoolbar_p.h>
#include <QtWidgets/qtoolbar.h>
#include <QtWidgets/private/qtoolbarlayout_p.h>
#endif
#include <QtWidgets/qmainwindow.h>
#if QT_CONFIG(rubberband)
#include <QtWidgets/qrubberband.h>
#endif
#if QT_CONFIG(tabbar)
#include <QtWidgets/private/qtabbar_p.h>
#endif
#include <QtWidgets/qapplication.h>
#if QT_CONFIG(draganddrop)
#include <QtGui/qdrag.h>
#endif
#include <QtCore/qmimedata.h>
#if QT_CONFIG(statusbar)
#include <QtWidgets/qstatusbar.h>
#endif
#include <QtCore/qstring.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstylepainter.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qstack.h>
#include <QtCore/qmap.h>
#include <QtCore/qpointer.h>
#ifndef QT_NO_DEBUG_STREAM
#  include <QtCore/qdebug.h>
#  include <QtCore/qtextstream.h>
#endif
#include <QtWidgets/private/qmenu_p.h>
#include <QtWidgets/private/qapplication_p.h>
#include <QtWidgets/private/qlayoutengine_p.h>
#include <QtWidgets/private/qwidgetresizehandler_p.h>
#include <QtGui/qpa/qplatformwindow_p.h>
#include <QtCore/QScopedValueRollback>
#include <QtCore/private/qoffsetstringarray_p.h>
#include <optional>
#include <QtWidgets/private/qtoolbarextension_p.h>
#include <QtGui/qevent.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstylepainter.h>
#include <QtWidgets/qstyleoption.h>
#include <QtWidgets/qtoolbar.h>
#include <QtWidgets/qapplication.h>
#if QT_CONFIG(draganddrop)
#include <QtGui/qdrag.h>
#endif
#include <QtGui/qevent.h>
#include <QtWidgets/qlayout.h>
#include <QtWidgets/qmainwindow.h>
#include <QtWidgets/qmenu.h>
#include <QtCore/qmimedata.h>
#include <QtWidgets/qstylepainter.h>
#include <QtWidgets/qstyleoption.h>
#include <QtWidgets/qtoolbutton.h>
#include <QtWidgets/qwidgetaction.h>
#include <QtWidgets/private/qwidgetaction_p.h>
#include <QtWidgets/private/qmainwindowlayout_p.h>
#include <QtGui/private/qhighdpiscaling_p.h>
#ifdef Q_OS_MACOS
#include <QtGui/qpa/qplatformnativeinterface.h>
#endif
#include <QtWidgets/private/qtoolbar_p.h>
#include <QtWidgets/private/qtoolbarseparator_p.h>
#include <QtWidgets/private/qtoolbarlayout_p.h>
#include  <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 79, as _ZN14QToolBarLayout22updateMarginAndSpacingEv
inline void QToolBarLayout::updateMarginAndSpacing()
{
    QToolBar *tb = qobject_cast<QToolBar*>(parentWidget());
    if (!tb)
        return;
    QStyle *style = tb->style();
    QStyleOptionToolBar opt;
    tb->initStyleOption(&opt);
    const int margin = style->pixelMetric(QStyle::PM_ToolBarItemMargin, &opt, tb)
            + style->pixelMetric(QStyle::PM_ToolBarFrameWidth, &opt, tb);
    setContentsMargins(margin, margin, margin, margin);
    setSpacing(style->pixelMetric(QStyle::PM_ToolBarItemSpacing, &opt, tb));
}

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 50, as _ZN14QToolBarLayoutC1EP7QWidget
inline QToolBarLayout::QToolBarLayout(QWidget *parent)
    : QLayout(parent), expanded(false), animating(false), dirty(true),
        expanding(false), empty(true), expandFlag(false), popupMenu(nullptr)
{
    QToolBar *tb = qobject_cast<QToolBar*>(parent);
    if (!tb)
        return;

    extension = new QToolBarExtension(tb);
    extension->setFocusPolicy(Qt::NoFocus);
    extension->hide();
    QObject::connect(tb, SIGNAL(orientationChanged(Qt::Orientation)),
                     extension, SLOT(setOrientation(Qt::Orientation)));

    setUsePopupMenu(qobject_cast<QMainWindow*>(tb->parentWidget()) == 0);
}

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 213, as _ZNK14QToolBarLayout7movableEv
inline bool QToolBarLayout::movable() const
{
    QToolBar *tb = qobject_cast<QToolBar*>(parentWidget());
    if (!tb)
        return false;
    QMainWindow *win = qobject_cast<QMainWindow*>(tb->parentWidget());
    return tb->isMovable() && win != nullptr;
}

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 3440, as _ZN17QMainWindowLayout17needsPlatformDragEv
#if QT_CONFIG(draganddrop)
inline bool QMainWindowLayout::needsPlatformDrag()
{
    static const bool wayland =
            QGuiApplication::platformName().startsWith("wayland"_L1, Qt::CaseInsensitive);
    return wayland;
}
#endif  // QT_CONFIG(draganddrop)

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 120, as _ZN14QToolBarLayout17checkUsePopupMenuEv
inline void QToolBarLayout::checkUsePopupMenu()
{
    QToolBar *tb = static_cast<QToolBar *>(parent());
    QMainWindow *mw = qobject_cast<QMainWindow *>(tb->parent());
    Qt::Orientation o = tb->orientation();
    setUsePopupMenu(!mw || tb->isFloating() || perp(o, expandedSize(mw->size())) >= perp(o, mw->size()));
}

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 98, as _ZN14QToolBarLayout15setUsePopupMenuEb
inline void QToolBarLayout::setUsePopupMenu(bool set)
{
    if (!dirty && ((popupMenu == nullptr) == set))
        invalidate();
    if (!set) {
        QObject::connect(extension, SIGNAL(clicked(bool)),
                        this, SLOT(setExpanded(bool)), Qt::UniqueConnection);
        extension->setPopupMode(QToolButton::DelayedPopup);
        extension->setMenu(nullptr);
        delete popupMenu;
        popupMenu = nullptr;
    } else {
        QObject::disconnect(extension, SIGNAL(clicked(bool)),
                            this, SLOT(setExpanded(bool)));
        extension->setPopupMode(QToolButton::InstantPopup);
        if (!popupMenu) {
            popupMenu = new QMenu(extension);
        }
        extension->setMenu(popupMenu);
    }
}

//  from src/widgets/widgets/qtoolbarextension.cpp, line 15, as _ZN17QToolBarExtensionC1EP7QWidget
inline QToolBarExtension::QToolBarExtension(QWidget *parent)
    : QToolButton(parent)
    , m_orientation(Qt::Horizontal)
{
    setObjectName("qt_toolbar_ext_button"_L1);
    setAutoRaise(true);
    setOrientation(m_orientation);
    setSizePolicy(QSizePolicy::Minimum, QSizePolicy::Minimum);
    setCheckable(true);
}

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 542, as _ZNK14QToolBarLayout12expandedSizeERK5QSize
inline QSize QToolBarLayout::expandedSize(const QSize &size) const
{
    if (dirty)
        updateGeomArray();

    QToolBar *tb = qobject_cast<QToolBar*>(parentWidget());
    if (!tb)
        return QSize(0, 0);
    QMainWindow *win = qobject_cast<QMainWindow*>(tb->parentWidget());
    Qt::Orientation o = tb->orientation();
    QStyle *style = tb->style();
    QStyleOptionToolBar opt;
    tb->initStyleOption(&opt);
    const int handleExtent = movable()
            ? style->pixelMetric(QStyle::PM_ToolBarHandleExtent, &opt, tb) : 0;
    const QMargins margins = contentsMargins();
    const int spacing = this->spacing();
    const int extensionExtent = style->pixelMetric(QStyle::PM_ToolBarExtensionExtent, &opt, tb);

    int total_w = 0;
    int count = 0;
    for (int x = 0; x < items.size(); ++x) {
        if (!geomArray[x].empty) {
            total_w += (count == 0 ? 0 : spacing) + geomArray[x].minimumSize;
            ++count;
        }
    }
    if (count == 0)
        return QSize(0, 0);

    int min_w = pick(o, size);
    int rows = (int)qSqrt(qreal(count));
    if (rows == 1)
        ++rows;      // we want to expand to at least two rows
    int space = total_w/rows + spacing + extensionExtent;
    space = qMax(space, min_w - pick(o, margins) - handleExtent);
    if (win != nullptr)
        space = qMin(space, pick(o, win->size()) - pick(o, margins) - handleExtent);

    int w = 0;
    int h = 0;
    int i = 0;
    while (i < items.size()) {
        int count = 0;
        int size = 0;
        int prev = -1;
        int rowHeight = 0;
        for (; i < items.size(); ++i) {
            if (geomArray[i].empty)
                continue;

            int newSize = size + (count == 0 ? 0 : spacing) + geomArray[i].minimumSize;
            rowHeight = qMax(rowHeight, perp(o, items.at(i)->sizeHint()));
            if (prev != -1 && newSize > space) {
                if (count > 1 && size + spacing + extensionExtent > space) {
                    size -= spacing + geomArray[prev].minimumSize;
                    i = prev;
                }
                break;
            }

            size = newSize;
            prev = i;
            ++count;
        }

        w = qMax(size, w);
        h += rowHeight + spacing;
    }

    w += pick(Qt::Horizontal, margins) + handleExtent + spacing + extensionExtent;
    w = qMax(w, min_w);
    if (win != nullptr)
        w = qMin(w, pick(o, win->size()));
    h += pick(Qt::Vertical, margins) - spacing; //there is no spacing before the first row

    QSize result;
    rpick(o, result) = w;
    rperp(o, result) = h;
    return result;
}

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 222, as _ZNK14QToolBarLayout15updateGeomArrayEv
inline void QToolBarLayout::updateGeomArray() const
{
    if (!dirty)
        return;

    QToolBarLayout *that = const_cast<QToolBarLayout*>(this);

    QToolBar *tb = qobject_cast<QToolBar*>(parentWidget());
    if (!tb)
        return;
    QStyle *style = tb->style();
    QStyleOptionToolBar opt;
    tb->initStyleOption(&opt);
    const int handleExtent = movable()
            ? style->pixelMetric(QStyle::PM_ToolBarHandleExtent, &opt, tb) : 0;
    const QMargins margins = contentsMargins();
    const int spacing = this->spacing();
    const int extensionExtent = style->pixelMetric(QStyle::PM_ToolBarExtensionExtent, &opt, tb);
    Qt::Orientation o = tb->orientation();

    that->minSize = QSize(0, 0);
    that->hint = QSize(0, 0);
    rperp(o, that->minSize) = style->pixelMetric(QStyle::PM_ToolBarHandleExtent, &opt, tb);
    rperp(o, that->hint) = style->pixelMetric(QStyle::PM_ToolBarHandleExtent, &opt, tb);

    that->expanding = false;
    that->empty = false;

    QList<QLayoutStruct> a(items.size() + 1); // + 1 for the stretch

    int count = 0;
    for (int i = 0; i < items.size(); ++i) {
        QToolBarItem *item = items.at(i);

        QSize max = item->maximumSize();
        QSize min = item->minimumSize();
        QSize hint = item->sizeHint();
        Qt::Orientations exp = item->expandingDirections();
        bool empty = item->isEmpty();

        that->expanding = expanding || exp & o;


        if (item->widget()) {
            if ((item->widget()->sizePolicy().horizontalPolicy() & QSizePolicy::ExpandFlag)) {
                that->expandFlag = true;
            }
        }

        if (!empty) {
            if (count == 0) // the minimum size only displays one widget
                rpick(o, that->minSize) += pick(o, min);
            int s = perp(o, minSize);
            rperp(o, that->minSize) = qMax(s, perp(o, min));

            //we only add spacing before item (ie never before the first one)
            rpick(o, that->hint) += (count == 0 ? 0 : spacing) + pick(o, hint);
            s = perp(o, that->hint);
            rperp(o, that->hint) = qMax(s, perp(o, hint));
            ++count;
        }

        a[i].sizeHint = pick(o, hint);
        a[i].maximumSize = pick(o, max);
        a[i].minimumSize = pick(o, min);
        a[i].expansive = exp & o;
        if (o == Qt::Horizontal)
            a[i].stretch = item->widget()->sizePolicy().horizontalStretch();
        else
            a[i].stretch = item->widget()->sizePolicy().verticalStretch();
        a[i].empty = empty;
    }

    that->geomArray = a;
    that->empty = count == 0;

    rpick(o, that->minSize) += handleExtent;
    that->minSize += QSize(pick(Qt::Horizontal, margins), pick(Qt::Vertical, margins));
    if (items.size() > 1)
        rpick(o, that->minSize) += spacing + extensionExtent;

    rpick(o, that->hint) += handleExtent;
    that->hint += QSize(pick(Qt::Horizontal, margins), pick(Qt::Vertical, margins));
    that->dirty = false;
}

//  from src/widgets/widgets/qtoolbar.cpp, line 68, as _ZN15QToolBarPrivate13_q_toggleViewEb
inline void QToolBarPrivate::_q_toggleView(bool b)
{
    Q_Q(QToolBar);
    if (b == q->isHidden()) {
        if (b)
            q->show();
        else
            q->close();
    }
}

//  from src/widgets/widgets/qtoolbar.cpp, line 79, as _ZN15QToolBarPrivate17_q_updateIconSizeERK5QSize
inline void QToolBarPrivate::_q_updateIconSize(const QSize &sz)
{
    Q_Q(QToolBar);
    if (!explicitIconSize) {
        // iconSize not explicitly set
        q->setIconSize(sz);
        explicitIconSize = false;
    }
}

//  from src/widgets/widgets/qtoolbar.cpp, line 89, as _ZN15QToolBarPrivate24_q_updateToolButtonStyleEN2Qt15ToolButtonStyleE
inline void QToolBarPrivate::_q_updateToolButtonStyle(Qt::ToolButtonStyle style)
{
    Q_Q(QToolBar);
    if (!explicitToolButtonStyle) {
        q->setToolButtonStyle(style);
        explicitToolButtonStyle = false;
    }
}

//  from src/widgets/widgets/qtoolbar.cpp, line 98, as _ZN15QToolBarPrivate17updateWindowFlagsEbb
inline void QToolBarPrivate::updateWindowFlags(bool floating, bool unplug)
{
    Q_Q(QToolBar);
    Qt::WindowFlags flags = floating ? Qt::Tool : Qt::Widget;

    flags |= Qt::FramelessWindowHint;

#if QT_CONFIG(draganddrop)
    // If we are performing a platform drag the flag is not needed and we want to avoid recreating
    // the platform window when it would be removed later
    if (unplug && !QMainWindowLayout::needsPlatformDrag())
        flags |= Qt::X11BypassWindowManagerHint;
#else
    Q_UNUSED(unplug);
#endif

    q->setWindowFlags(flags);
}

//  from src/widgets/widgets/qtoolbar.cpp, line 117, as _ZN15QToolBarPrivate14setWindowStateEbbRK5QRect
inline void QToolBarPrivate::setWindowState(bool floating, bool unplug, const QRect &rect)
{
    Q_Q(QToolBar);
    bool visible = !q->isHidden();
    bool wasFloating = q->isFloating(); // ...is also currently using popup menus

    updateWindowFlags(floating, unplug);

    if (floating != wasFloating)
        layout->checkUsePopupMenu();

    if (!rect.isNull())
        q->setGeometry(rect);

    if (visible)
        q->show();

    if (floating != wasFloating)
        emit q->topLevelChanged(floating);
}

//  from src/widgets/widgets/qtoolbar.cpp, line 374, as _ZN15QToolBarPrivate4plugERK5QRect
inline void QToolBarPrivate::plug(const QRect &r)
{
    setWindowState(false, false, r);
}
//  -----------------------------------------------------------------------

//  A QToolBarPrivate that Python can take functions over in. Every QToolBarPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQToolBarPrivateCall0)(const void *, bool, int *);
typedef void (*CuteQToolBarPrivateCall1)(const void *, int, int *);
typedef void (*CuteQToolBarPrivateCall2)(const void *, int *);
typedef void (*CuteQToolBarPrivateCall3)(const void *, int *);
typedef void * (*CuteQToolBarPrivateCall4)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQToolBarPrivateCall5)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQToolBarPrivateCall6)(const void *, int *);
typedef int (*CuteQToolBarPrivateCall7)(const void *, int *);
typedef const QImage * (*CuteQToolBarPrivateCall8)(const void *, int *);
typedef void (*CuteQToolBarPrivateCall9)(const void *, int *);
typedef void (*CuteQToolBarPrivateCall10)(const void *, int *);
typedef void (*CuteQToolBarPrivateCall11)(const void *, int *);
typedef void (*CuteQToolBarPrivateCall12)(const void *, int *);
typedef void (*CuteQToolBarPrivateCall13)(const void *, int *);
typedef void (*CuteQToolBarPrivateCall14)(const void *, int *);
typedef void (*CuteQToolBarPrivateCall15)(const void *, int *);
typedef bool (*CuteQToolBarPrivateCall16)(const void *, int *);
typedef bool (*CuteQToolBarPrivateCall17)(const void *, int *);
class CuteQToolBarPrivate : public QToolBarPrivate {
public:
  using QToolBarPrivate::QToolBarPrivate;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10setVisibleEb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE")) {
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

  //  void QWidgetPrivate::setVisible(bool a0)
  void setVisible(bool a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQToolBarPrivateCall0 call = reinterpret_cast<CuteQToolBarPrivateCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[1]) {
      int handled = 0;
      CuteQToolBarPrivateCall1 call = reinterpret_cast<CuteQToolBarPrivateCall1>(taken[1]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[2]) {
      int handled = 0;
      CuteQToolBarPrivateCall2 call = reinterpret_cast<CuteQToolBarPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[3]) {
      int handled = 0;
      CuteQToolBarPrivateCall3 call = reinterpret_cast<CuteQToolBarPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[4]) {
      int handled = 0;
      CuteQToolBarPrivateCall4 call = reinterpret_cast<CuteQToolBarPrivateCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQToolBarPrivateCall5 call = reinterpret_cast<CuteQToolBarPrivateCall5>(taken[5]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQToolBarPrivateCall6 call = reinterpret_cast<CuteQToolBarPrivateCall6>(taken[6]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[7]) {
      int handled = 0;
      CuteQToolBarPrivateCall7 call = reinterpret_cast<CuteQToolBarPrivateCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[8]) {
      int handled = 0;
      CuteQToolBarPrivateCall8 call = reinterpret_cast<CuteQToolBarPrivateCall8>(taken[8]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[9]) {
      int handled = 0;
      CuteQToolBarPrivateCall9 call = reinterpret_cast<CuteQToolBarPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[10]) {
      int handled = 0;
      CuteQToolBarPrivateCall10 call = reinterpret_cast<CuteQToolBarPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[11]) {
      int handled = 0;
      CuteQToolBarPrivateCall11 call = reinterpret_cast<CuteQToolBarPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[12]) {
      int handled = 0;
      CuteQToolBarPrivateCall12 call = reinterpret_cast<CuteQToolBarPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[13]) {
      int handled = 0;
      CuteQToolBarPrivateCall13 call = reinterpret_cast<CuteQToolBarPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[14]) {
      int handled = 0;
      CuteQToolBarPrivateCall14 call = reinterpret_cast<CuteQToolBarPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[15]) {
      int handled = 0;
      CuteQToolBarPrivateCall15 call = reinterpret_cast<CuteQToolBarPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[16]) {
      int handled = 0;
      CuteQToolBarPrivateCall16 call = reinterpret_cast<CuteQToolBarPrivateCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[17]) {
      int handled = 0;
      CuteQToolBarPrivateCall17 call = reinterpret_cast<CuteQToolBarPrivateCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QToolBar *QToolBarPrivate::q_func()
extern "C" Q_DECL_EXPORT
QToolBar *ritual_ZN15QToolBarPrivate6q_funcEv(QToolBarPrivate *self) {
  return self->q_func();
}

//  const QToolBar *QToolBarPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QToolBar *ritual_ZNK15QToolBarPrivate6q_funcEv(
    const QToolBarPrivate *self) {
  return self->q_func();
}

//  QToolBarPrivate::QToolBarPrivate()
extern "C" Q_DECL_EXPORT
QToolBarPrivate *ritual_ZN15QToolBarPrivateC1Ev() {
  return new CuteQToolBarPrivate();
}

//  void QToolBarPrivate::_q_toggleView(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QToolBarPrivate13_q_toggleViewEb(
    QToolBarPrivate *self,
    bool b) {
  self->_q_toggleView(b);
}

//  void QToolBarPrivate::_q_updateIconSize(const QSize &sz)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QToolBarPrivate17_q_updateIconSizeERK5QSize(
    QToolBarPrivate *self,
    const QSize *sz) {
  self->_q_updateIconSize(*sz);
}

//  void QToolBarPrivate::_q_updateToolButtonStyle(Qt::ToolButtonStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QToolBarPrivate24_q_updateToolButtonStyleEN2Qt15ToolButtonStyleE(
    QToolBarPrivate *self,
    Qt::ToolButtonStyle style) {
  self->_q_updateToolButtonStyle(style);
}

#if QT_CONFIG(draganddrop)
//  void QToolBarPrivate::updateWindowFlags(bool floating, bool unplug)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QToolBarPrivate17updateWindowFlagsEbb(
    QToolBarPrivate *self,
    bool floating,
    bool unplug) {
  self->updateWindowFlags(floating, unplug);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QToolBarPrivate::setWindowState(bool floating, bool unplug, const
//      QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QToolBarPrivate14setWindowStateEbbRK5QRect(
    QToolBarPrivate *self,
    bool floating,
    bool unplug,
    const QRect *rect) {
  self->setWindowState(floating, unplug, *rect);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QToolBarPrivate::plug(const QRect &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QToolBarPrivate4plugERK5QRect(
    QToolBarPrivate *self,
    const QRect *r) {
  self->plug(*r);
}
#endif  // QT_CONFIG(draganddrop)

//  a Python function taken by a CuteQToolBarPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QToolBarPrivate(
    QToolBarPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQToolBarPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(toolbar)
#endif  // QT_CONFIG(toolbar)
