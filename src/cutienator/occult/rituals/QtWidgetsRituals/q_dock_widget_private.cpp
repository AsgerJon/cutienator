//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qdockwidget_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(dockwidget)
#if QT_CONFIG(dockwidget)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qdockwidget.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qdockwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
#include <QtWidgets/private/qwidgetresizehandler_p.h>
#include <QtWidgets/qframe.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/private/qwidget_p.h>
#include <QtGui/qcursor.h>
#if QT_CONFIG(sizegrip)
#include <QtWidgets/qsizegrip.h>
#endif
#include <QtGui/qevent.h>
#include <QtCore/qdebug.h>
#include <QtWidgets/private/qlayoutengine_p.h>
#include <QtWidgets/qdockwidget.h>
#include <QtWidgets/qaction.h>
#include <QtWidgets/qapplication.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
#include <QtWidgets/qdrawutil.h>
#include <QtGui/qevent.h>
#include <QtGui/qfontmetrics.h>
#include <QtWidgets/qproxystyle.h>
#include <QtGui/qwindow.h>
#include <QtGui/qscreen.h>
#include <QtWidgets/qmainwindow.h>
#include <QtWidgets/qstylepainter.h>
#include <QtWidgets/qtoolbutton.h>
#include <QtCore/qdebug.h>
#include <QtWidgets/private/qwidgetresizehandler_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtGui/private/qhighdpiscaling_p.h>
#include <QtWidgets/private/qdockwidget_p.h>
#include <QtWidgets/private/qmainwindowlayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/widgets/qdockwidget.cpp, line 39, as local:qdockwidget.cpp:mainwindow_from_dock
static const QMainWindow *mainwindow_from_dock(const QDockWidget *dock)
{
    for (const QWidget *p = dock->parentWidget(); p; p = p->parentWidget()) {
        if (const QMainWindow *window = qobject_cast<const QMainWindow*>(p))
            return window;
    }
    return nullptr;
}

//  from src/widgets/widgets/qdockwidget.cpp, line 54, as local:qdockwidget.cpp:hasFeature
static inline bool hasFeature(const QDockWidgetPrivate *priv, QDockWidget::DockWidgetFeature feature)
{ return (priv->features & feature) == feature; }

//  from src/widgets/widgets/qdockwidget.cpp, line 91, as local:qdockwidget.cpp:QDockWidgetTitleButton
class QDockWidgetTitleButton : public QAbstractButton
{
    Q_OBJECT

public:
    QDockWidgetTitleButton(QDockWidget *dockWidget);

    QSize sizeHint() const override;
    QSize minimumSizeHint() const override
    { return sizeHint(); }

    void enterEvent(QEnterEvent *event) override;
    void leaveEvent(QEvent *event) override;
    void paintEvent(QPaintEvent *event) override;

protected:
    bool event(QEvent *event) override;

private:
    QSize dockButtonIconSize() const;

    mutable int m_iconSize = -1;
};

//  from src/widgets/widgets/qdockwidget.cpp, line 115, as local:qdockwidget.cpp:QDockWidgetTitleButton::QDockWidgetTitleButton
inline QDockWidgetTitleButton::QDockWidgetTitleButton(QDockWidget *dockWidget)
    : QAbstractButton(dockWidget)
{
    setFocusPolicy(Qt::NoFocus);
}

//  from src/widgets/widgets/qdockwidget.cpp, line 121, as local:qdockwidget.cpp:QDockWidgetTitleButton::event
inline bool QDockWidgetTitleButton::event(QEvent *event)
{
    switch (event->type()) {
    case QEvent::StyleChange:
    case QEvent::DevicePixelRatioChange:
        m_iconSize = -1;
        break;
    default:
        break;
    }
    return QAbstractButton::event(event);
}

//  from src/widgets/widgets/qdockwidget.cpp, line 134, as local:qdockwidget.cpp:QDockWidgetTitleButton::dockButtonIconSize
inline QSize QDockWidgetTitleButton::dockButtonIconSize() const
{
    if (m_iconSize < 0) {
        m_iconSize = style()->pixelMetric(QStyle::PM_SmallIconSize, nullptr, this);
        if (style()->styleHint(QStyle::SH_DockWidget_ButtonsHaveFrame, nullptr, this))
            m_iconSize = (m_iconSize * 5) / 8;  // 16 -> 10
    }
    return QSize(m_iconSize, m_iconSize);
}

//  from src/widgets/widgets/qdockwidget.cpp, line 144, as local:qdockwidget.cpp:QDockWidgetTitleButton::sizeHint
inline QSize QDockWidgetTitleButton::sizeHint() const
{
    ensurePolished();

    int size = 2*style()->pixelMetric(QStyle::PM_DockWidgetTitleBarButtonMargin, nullptr, this);
    if (!icon().isNull()) {
        const QSize sz = icon().actualSize(dockButtonIconSize());
        size += qMax(sz.width(), sz.height());
    }

    return QSize(size, size);
}

//  from src/widgets/widgets/qdockwidget.cpp, line 157, as local:qdockwidget.cpp:QDockWidgetTitleButton::enterEvent
inline void QDockWidgetTitleButton::enterEvent(QEnterEvent *event)
{
    if (isEnabled()) update();
    QAbstractButton::enterEvent(event);
}

//  from src/widgets/widgets/qdockwidget.cpp, line 163, as local:qdockwidget.cpp:QDockWidgetTitleButton::leaveEvent
inline void QDockWidgetTitleButton::leaveEvent(QEvent *event)
{
    if (isEnabled()) update();
    QAbstractButton::leaveEvent(event);
}

//  from src/widgets/widgets/qdockwidget.cpp, line 169, as local:qdockwidget.cpp:QDockWidgetTitleButton::paintEvent
inline void QDockWidgetTitleButton::paintEvent(QPaintEvent *)
{
    QStylePainter p(this);

    QStyleOptionToolButton opt;
    opt.initFrom(this);
    opt.state |= QStyle::State_AutoRaise;

    if (style()->styleHint(QStyle::SH_DockWidget_ButtonsHaveFrame, nullptr, this)) {
        if (isEnabled() && underMouse() && !isChecked() && !isDown())
            opt.state |= QStyle::State_Raised;
        if (isChecked())
            opt.state |= QStyle::State_On;
        if (isDown())
            opt.state |= QStyle::State_Sunken;
        p.drawPrimitive(QStyle::PE_PanelButtonTool, opt);
    } else if (isDown() || isChecked()) {
        // no frame, but the icon might have explicit pixmaps for QIcon::On
        opt.state |= QStyle::State_On | QStyle::State_Sunken;
    }

    opt.icon = icon();
    opt.subControls = { };
    opt.activeSubControls = { };
    opt.features = QStyleOptionToolButton::None;
    opt.arrowType = Qt::NoArrow;
    opt.iconSize = dockButtonIconSize();
    p.drawComplexControl(QStyle::CC_ToolButton, opt);
}

//  from src/widgets/widgets/qwidgetresizehandler.cpp, line 22, as local:qwidgetresizehandler.cpp:RANGE
#define RANGE 4

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 3440, as _ZN17QMainWindowLayout17needsPlatformDragEv
#if QT_CONFIG(draganddrop)
inline bool QMainWindowLayout::needsPlatformDrag()
{
    static const bool wayland =
            QGuiApplication::platformName().startsWith("wayland"_L1, Qt::CaseInsensitive);
    return wayland;
}
#endif  // QT_CONFIG(draganddrop)

//  from src/widgets/widgets/qwidgetresizehandler.cpp, line 40, as _ZN20QWidgetResizeHandler10setEnabledEb
inline void QWidgetResizeHandler::setEnabled(bool b)
{
    if (b == enabled)
        return;

    enabled = b;
    if (!enabled)
        setMouseCursor(Nowhere);
}

//  from src/widgets/widgets/qwidgetresizehandler.cpp, line 257, as _ZN20QWidgetResizeHandler14setMouseCursorENS_13MousePositionE
inline void QWidgetResizeHandler::setMouseCursor(MousePosition m)
{
#ifdef QT_NO_CURSOR
    Q_UNUSED(m);
#else
    QObjectList children = widget->children();
    for (int i = 0; i < children.size(); ++i) {
        if (QWidget *w = qobject_cast<QWidget*>(children.at(i))) {
            if (!w->testAttribute(Qt::WA_SetCursor)) {
                w->setCursor(Qt::ArrowCursor);
            }
        }
    }

    switch (m) {
    case TopLeft:
    case BottomRight:
        widget->setCursor(Qt::SizeFDiagCursor);
        break;
    case BottomLeft:
    case TopRight:
        widget->setCursor(Qt::SizeBDiagCursor);
        break;
    case Top:
    case Bottom:
        widget->setCursor(Qt::SizeVerCursor);
        break;
    case Left:
    case Right:
        widget->setCursor(Qt::SizeHorCursor);
        break;
    default:
        widget->setCursor(Qt::ArrowCursor);
        break;
    }
#endif // QT_NO_CURSOR
}

//  from src/widgets/widgets/qdockwidget.cpp, line 667, as _ZN18QDockWidgetPrivate10toggleViewEb
inline void QDockWidgetPrivate::toggleView(bool b)
{
    Q_Q(QDockWidget);
    if (b == q->isHidden()) {
        if (b)
            q->show();
        else
            q->close();
    }
}

//  from src/widgets/widgets/qdockwidget.cpp, line 715, as _ZN18QDockWidgetPrivate14toggleTopLevelEv
inline void QDockWidgetPrivate::toggleTopLevel()
{
    Q_Q(QDockWidget);
    q->setFloating(!q->isFloating());
}

//  from src/widgets/widgets/qdockwidget.cpp, line 875, as _ZN18QDockWidgetPrivate16toDockWidgetAreaEN9QInternal12DockPositionE
inline Qt::DockWidgetArea QDockWidgetPrivate::toDockWidgetArea(QInternal::DockPosition pos)
{
    switch (pos) {
    case QInternal::LeftDock:   return Qt::LeftDockWidgetArea;
    case QInternal::RightDock:  return Qt::RightDockWidgetArea;
    case QInternal::TopDock:    return Qt::TopDockWidgetArea;
    case QInternal::BottomDock: return Qt::BottomDockWidgetArea;
    default: break;
    }
    return Qt::NoDockWidgetArea;
}

//  from src/widgets/widgets/qdockwidget.cpp, line 1139, as _ZN18QDockWidgetPrivate19recalculatePressPosEP12QResizeEvent
inline void QDockWidgetPrivate::recalculatePressPos(QResizeEvent *event)
{
    qreal ratio = event->oldSize().width() / (1.0 * event->size().width());
    state->pressPos.setX(state->pressPos.x() / ratio);
}
//  -----------------------------------------------------------------------

//  QDockWidget *QDockWidgetPrivate::q_func()
extern "C" Q_DECL_EXPORT
QDockWidget *ritual_ZN18QDockWidgetPrivate6q_funcEv(
    QDockWidgetPrivate *self) {
  return self->q_func();
}

//  const QDockWidget *QDockWidgetPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QDockWidget *ritual_ZNK18QDockWidgetPrivate6q_funcEv(
    const QDockWidgetPrivate *self) {
  return self->q_func();
}

//  void QDockWidgetPrivate::toggleView(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDockWidgetPrivate10toggleViewEb(
    QDockWidgetPrivate *self,
    bool a0) {
  self->toggleView(a0);
}

//  void QDockWidgetPrivate::toggleTopLevel()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDockWidgetPrivate14toggleTopLevelEv(
    QDockWidgetPrivate *self) {
  self->toggleTopLevel();
}

//  Qt::DockWidgetArea
//      QDockWidgetPrivate::toDockWidgetArea(QInternal::DockPosition pos)
extern "C" Q_DECL_EXPORT
Qt::DockWidgetArea ritual_ZN18QDockWidgetPrivate16toDockWidgetAreaEN9QInternal12DockPositionE(
    QInternal::DockPosition pos) {
  return QDockWidgetPrivate::toDockWidgetArea(pos);
}

//  void QDockWidgetPrivate::recalculatePressPos(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QDockWidgetPrivate19recalculatePressPosEP12QResizeEvent(
    QDockWidgetPrivate *self,
    QResizeEvent *event) {
  self->recalculatePressPos(event);
}

#endif  // QT_CONFIG(dockwidget)
#endif  // QT_CONFIG(dockwidget)
