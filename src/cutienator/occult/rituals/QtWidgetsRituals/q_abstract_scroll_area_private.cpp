//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qabstractscrollarea_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: added are 1 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(scrollarea)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qabstractscrollarea.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qabstractscrollarea_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qframe.h>
#include <QtGui/qbitmap.h>
#include <QtWidgets/qdrawutil.h>
#include <QtGui/qevent.h>
#include <QtGui/qpainter.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#include <QtWidgets/qstylepainter.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/private/qframe_p.h>
#include <QtWidgets/qabstractscrollarea.h>
#if QT_CONFIG(scrollarea)
#include <QtWidgets/qscrollbar.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#include <QtGui/qevent.h>
#include <QtCore/qdebug.h>
#include <QtWidgets/qboxlayout.h>
#include <QtGui/qpainter.h>
#include <QtCore/qmargins.h>
#if QT_CONFIG(itemviews)
#include <QtWidgets/qheaderview.h>
#endif
#include <QtCore/QDebug>
#include <QtWidgets/private/qabstractscrollarea_p.h>
#include <QtWidgets/private/qscrollbar_p.h>
#include <QtWidgets/qwidget.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtWidgets/private/qapplication_p.h>
#ifdef Q_OS_WIN
#  include <QtCore/qt_windows.h>
#endif
#endif
#include <QtWidgets/qapplication.h>
#include <QtGui/qcursor.h>
#include <QtGui/qevent.h>
#include <QtGui/qpainter.h>
#include <QtWidgets/qscrollbar.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#include <QtWidgets/qstylepainter.h>
#include <QtCore/qelapsedtimer.h>
#include <QtCore/qpointer.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
#if QT_CONFIG(menu)
#include <QtWidgets/qmenu.h>
#include <QtWidgets/private/qmenu_p.h>
#endif
#include <limits.h>
#include <QtWidgets/private/qscrollbar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/widgets/qframe.cpp, line 19, as _ZN13QFramePrivateC2Ev
inline QFramePrivate::QFramePrivate()
    : frect(0, 0, 0, 0),
      frameStyle(QFrame::NoFrame | QFrame::Plain),
      lineWidth(1),
      midLineWidth(0),
      frameWidth(0),
      leftFrameWidth(0), rightFrameWidth(0),
      topFrameWidth(0), bottomFrameWidth(0)
{
}

//  from src/widgets/widgets/qframe.cpp, line 30, as _ZN13QFramePrivateD2Ev
inline QFramePrivate::~QFramePrivate()
{
}

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 1368, as _ZNK26QAbstractScrollAreaPrivate14contentsOffsetEv
#if QT_CONFIG(scrollarea)
inline QPoint QAbstractScrollAreaPrivate::contentsOffset() const
{
    Q_Q(const QAbstractScrollArea);
    QPoint offset;
    if (vbar->isVisible())
        offset.setY(vbar->value());
    if (hbar->isVisible()) {
        if (q->isRightToLeft())
            offset.setX(hbar->maximum() - hbar->value());
        else
            offset.setX(hbar->value());
    }
    return offset;
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 1315, as _ZNK26QAbstractScrollAreaPrivate19canStartScrollingAtERK6QPoint
#if QT_CONFIG(scrollarea)
inline bool QAbstractScrollAreaPrivate::canStartScrollingAt(const QPoint &startPos) const
{
    Q_Q(const QAbstractScrollArea);

    // don't start scrolling on a QAbstractSlider
    if (qobject_cast<QAbstractSlider *>(q->viewport()->childAt(startPos)))
        return false;

    return true;
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 145, as _ZN37QAbstractScrollAreaScrollBarContainerC1EN2Qt11OrientationEP7QWidget
#if QT_CONFIG(scrollarea)
inline QAbstractScrollAreaScrollBarContainer::QAbstractScrollAreaScrollBarContainer(Qt::Orientation orientation, QWidget *parent)
    :QWidget(parent), scrollBar(new QScrollBar(orientation, this)),
     layout(new QBoxLayout(orientation == Qt::Horizontal ? QBoxLayout::LeftToRight : QBoxLayout::TopToBottom)),
     orientation(orientation)
{
    setLayout(layout);
    layout->setContentsMargins(QMargins());
    layout->setSpacing(0);
    layout->addWidget(scrollBar);
    layout->setSizeConstraint(QLayout::SetMaximumSize);
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/widgets/qscrollbar.cpp, line 200, as _ZN17QScrollBarPrivate12setTransientEb
inline void QScrollBarPrivate::setTransient(bool value)
{
    Q_Q(QScrollBar);
    if (transient != value) {
        transient = value;
        if (q->isVisible()) {
            QStyleOptionSlider opt;
            q->initStyleOption(&opt);
            if (q->style()->styleHint(QStyle::SH_ScrollBar_Transient, &opt, q))
                q->update();
        } else if (!transient) {
            q->show();
        }
    }
}

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 133, as _ZN26QAbstractScrollAreaPrivateC1Ev
#if QT_CONFIG(scrollarea)
inline QAbstractScrollAreaPrivate::QAbstractScrollAreaPrivate()
    :hbar(nullptr), vbar(nullptr), vbarpolicy(Qt::ScrollBarAsNeeded), hbarpolicy(Qt::ScrollBarAsNeeded),
     shownOnce(false), inResize(false), sizeAdjustPolicy(QAbstractScrollArea::AdjustIgnored),
     viewport(nullptr), cornerWidget(nullptr), left(0), top(0), right(0), bottom(0),
     xoffset(0), yoffset(0), viewportFilter(nullptr)
{
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 141, as _ZN26QAbstractScrollAreaPrivateD1Ev
#if QT_CONFIG(scrollarea)
inline QAbstractScrollAreaPrivate::~QAbstractScrollAreaPrivate()
{
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 213, as _ZN26QAbstractScrollAreaPrivate16replaceScrollBarEP10QScrollBarN2Qt11OrientationE
#if QT_CONFIG(scrollarea)
inline void QAbstractScrollAreaPrivate::replaceScrollBar(QScrollBar *scrollBar,
                                                  Qt::Orientation orientation)
{
    Q_Q(QAbstractScrollArea);

    QAbstractScrollAreaScrollBarContainer *container = scrollBarContainers[orientation];
    bool horizontal = (orientation == Qt::Horizontal);
    QScrollBar *oldBar = horizontal ? hbar : vbar;
    if (horizontal)
        hbar = scrollBar;
    else
        vbar = scrollBar;
    scrollBar->setParent(container);
    container->scrollBar = scrollBar;
    container->layout->removeWidget(oldBar);
    container->layout->insertWidget(0, scrollBar);
    scrollBar->setVisible(oldBar->isVisibleTo(container));
    scrollBar->setInvertedAppearance(oldBar->invertedAppearance());
    scrollBar->setInvertedControls(oldBar->invertedControls());
    scrollBar->setRange(oldBar->minimum(), oldBar->maximum());
    scrollBar->setOrientation(oldBar->orientation());
    scrollBar->setPageStep(oldBar->pageStep());
    scrollBar->setSingleStep(oldBar->singleStep());
    scrollBar->d_func()->viewMayChangeSingleStep = oldBar->d_func()->viewMayChangeSingleStep;
    scrollBar->setSliderDown(oldBar->isSliderDown());
    scrollBar->setSliderPosition(oldBar->sliderPosition());
    scrollBar->setTracking(oldBar->hasTracking());
    scrollBar->setValue(oldBar->value());
    scrollBar->installEventFilter(q);
    oldBar->removeEventFilter(q);
    delete oldBar;

    QObject::connect(scrollBar, SIGNAL(valueChanged(int)),
                     q, horizontal ? SLOT(_q_hslide(int)) : SLOT(_q_vslide(int)));
    QObject::connect(scrollBar, SIGNAL(rangeChanged(int,int)),
                     q, SLOT(_q_showOrHideScrollBars()), Qt::QueuedConnection);
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 251, as _ZN26QAbstractScrollAreaPrivate4initEv
#if QT_CONFIG(scrollarea)
#if defined(Q_OS_LINUX)
inline void QAbstractScrollAreaPrivate::init()
{
    Q_Q(QAbstractScrollArea);
    viewport = new QWidget(q);
    viewport->setObjectName("qt_scrollarea_viewport"_L1);
    viewport->setBackgroundRole(QPalette::Base);
    viewport->setAutoFillBackground(true);
    scrollBarContainers[Qt::Horizontal] = new QAbstractScrollAreaScrollBarContainer(Qt::Horizontal, q);
    scrollBarContainers[Qt::Horizontal]->setObjectName("qt_scrollarea_hcontainer"_L1);
    hbar = scrollBarContainers[Qt::Horizontal]->scrollBar;
    hbar->setRange(0,0);
    scrollBarContainers[Qt::Horizontal]->setVisible(false);
    hbar->installEventFilter(q);
    QObject::connect(hbar, SIGNAL(valueChanged(int)), q, SLOT(_q_hslide(int)));
    QObject::connect(hbar, SIGNAL(rangeChanged(int,int)), q, SLOT(_q_showOrHideScrollBars()), Qt::QueuedConnection);
    scrollBarContainers[Qt::Vertical] = new QAbstractScrollAreaScrollBarContainer(Qt::Vertical, q);
    scrollBarContainers[Qt::Vertical]->setObjectName("qt_scrollarea_vcontainer"_L1);
    vbar = scrollBarContainers[Qt::Vertical]->scrollBar;
    vbar->setRange(0,0);
    scrollBarContainers[Qt::Vertical]->setVisible(false);
    vbar->installEventFilter(q);
    QObject::connect(vbar, SIGNAL(valueChanged(int)), q, SLOT(_q_vslide(int)));
    QObject::connect(vbar, SIGNAL(rangeChanged(int,int)), q, SLOT(_q_showOrHideScrollBars()), Qt::QueuedConnection);
    viewportFilter.reset(new QAbstractScrollAreaFilter(this));
    viewport->installEventFilter(viewportFilter.data());
    viewport->setFocusProxy(q);
    q->setFocusPolicy(Qt::StrongFocus);
    q->setFrameStyle(QFrame::StyledPanel | QFrame::Sunken);
    q->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
    layoutChildren();
#ifndef Q_OS_MACOS
#  ifndef QT_NO_GESTURES
    viewport->grabGesture(Qt::PanGesture);
#  endif
#endif
}
#endif  // defined(Q_OS_LINUX)
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 288, as _ZN26QAbstractScrollAreaPrivate14layoutChildrenEv
#if QT_CONFIG(scrollarea)
inline void QAbstractScrollAreaPrivate::layoutChildren()
{
    bool needH = false;
    bool needV = false;
    layoutChildren_helper(&needH, &needV);
    // Call a second time if one scrollbar was needed and not the other to
    // check if it needs to readjust accordingly
    if (needH != needV)
        layoutChildren_helper(&needH, &needV);
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 299, as _ZN26QAbstractScrollAreaPrivate21layoutChildren_helperEPbS0_
#if QT_CONFIG(scrollarea)
inline void QAbstractScrollAreaPrivate::layoutChildren_helper(bool *needHorizontalScrollbar, bool *needVerticalScrollbar)
{
    Q_Q(QAbstractScrollArea);
    QStyleOptionSlider barOpt;

    hbar->initStyleOption(&barOpt);
    bool htransient = hbar->style()->styleHint(QStyle::SH_ScrollBar_Transient, &barOpt, hbar);
    bool needh = *needHorizontalScrollbar || ((hbarpolicy != Qt::ScrollBarAlwaysOff) && ((hbarpolicy == Qt::ScrollBarAlwaysOn && !htransient)
                            || ((hbarpolicy == Qt::ScrollBarAsNeeded || htransient)
                            && hbar->minimum() < hbar->maximum() && !hbar->sizeHint().isEmpty())));
    const int hscrollOverlap = hbar->style()->pixelMetric(QStyle::PM_ScrollView_ScrollBarOverlap, &barOpt, hbar);

    vbar->initStyleOption(&barOpt);
    bool vtransient = vbar->style()->styleHint(QStyle::SH_ScrollBar_Transient, &barOpt, vbar);
    bool needv = *needVerticalScrollbar || ((vbarpolicy != Qt::ScrollBarAlwaysOff) && ((vbarpolicy == Qt::ScrollBarAlwaysOn && !vtransient)
                            || ((vbarpolicy == Qt::ScrollBarAsNeeded || vtransient)
                            && vbar->minimum() < vbar->maximum() && !vbar->sizeHint().isEmpty())));
    const int vscrollOverlap = vbar->style()->pixelMetric(QStyle::PM_ScrollView_ScrollBarOverlap, &barOpt, vbar);

    QStyleOption opt(0);
    opt.initFrom(q);

    const int hsbExt = hbar->sizeHint().height();
    const int vsbExt = vbar->sizeHint().width();
    const QPoint extPoint(vsbExt, hsbExt);
    const QSize extSize(vsbExt, hsbExt);

    const QRect widgetRect = q->rect();

    const bool hasCornerWidget = (cornerWidget != nullptr);

    QPoint cornerOffset((needv && vscrollOverlap == 0) ? vsbExt : 0, (needh && hscrollOverlap == 0) ? hsbExt : 0);
    QRect controlsRect;
    QRect viewportRect;

    // In FrameOnlyAroundContents mode the frame is drawn between the controls and
    // the viewport, else the frame rect is equal to the widget rect.
    if ((frameStyle != QFrame::NoFrame) &&
        q->style()->styleHint(QStyle::SH_ScrollView_FrameOnlyAroundContents, &opt, q)) {
        controlsRect = widgetRect;
        const int spacing = q->style()->pixelMetric(QStyle::PM_ScrollView_ScrollBarSpacing, &opt, q);
        const QPoint cornerExtra(needv ? spacing + vscrollOverlap : 0, needh ? spacing + hscrollOverlap : 0);
        QRect frameRect = widgetRect;
        frameRect.adjust(0, 0, -cornerOffset.x() - cornerExtra.x(), -cornerOffset.y() - cornerExtra.y());
        q->setFrameRect(QStyle::visualRect(opt.direction, opt.rect, frameRect));
        // The frame rect needs to be in logical coords, however we need to flip
        // the contentsRect back before passing it on to the viewportRect
        // since the viewportRect has its logical coords calculated later.
        viewportRect = QStyle::visualRect(opt.direction, opt.rect, q->contentsRect());
    } else {
        q->setFrameRect(QStyle::visualRect(opt.direction, opt.rect, widgetRect));
        controlsRect = q->contentsRect();
        viewportRect = QRect(controlsRect.topLeft(), controlsRect.bottomRight() - cornerOffset);
    }

    cornerOffset = QPoint(needv ? vsbExt : 0, needh ? hsbExt : 0);

    // If we have a corner widget and are only showing one scroll bar, we need to move it
    // to make room for the corner widget.
    if (hasCornerWidget && ((needv && vscrollOverlap == 0) || (needh && hscrollOverlap == 0)))
        cornerOffset =  extPoint;

    // The corner point is where the scroll bar rects, the corner widget rect and the
    // viewport rect meets.
    const QPoint cornerPoint(controlsRect.bottomRight() + QPoint(1, 1) - cornerOffset);

    // Some styles paints the corner if both scorllbars are showing and there is
    // no corner widget.
    if (needv && needh && !hasCornerWidget && hscrollOverlap == 0 && vscrollOverlap == 0)
        cornerPaintingRect = QStyle::visualRect(opt.direction, opt.rect, QRect(cornerPoint, extSize));
    else
        cornerPaintingRect = QRect();

    // move the scrollbars away from top/left headers
    int vHeaderRight = 0;
    int hHeaderBottom = 0;
#if QT_CONFIG(itemviews)
    if ((vscrollOverlap > 0 && needv) || (hscrollOverlap > 0 && needh)) {
        const QList<QHeaderView *> headers = q->findChildren<QHeaderView*>();
        if (headers.size() <= 2) {
            for (const QHeaderView *header : headers) {
                const QRect geo = header->geometry();
                if (header->orientation() == Qt::Vertical && header->isVisible() && QStyle::visualRect(opt.direction, opt.rect, geo).left() <= opt.rect.width() / 2)
                    vHeaderRight = QStyle::visualRect(opt.direction, opt.rect, geo).right();
                else if (header->orientation() == Qt::Horizontal && header->isVisible() && geo.top() <= q->frameWidth())
                    hHeaderBottom = geo.bottom();
             }
         }
    }
#endif // QT_CONFIG(itemviews)
    if (needh) {
        QRect horizontalScrollBarRect(QPoint(controlsRect.left() + vHeaderRight, cornerPoint.y()), QPoint(cornerPoint.x() - 1, controlsRect.bottom()));

        if (!hasCornerWidget && htransient)
            horizontalScrollBarRect.adjust(0, 0, cornerOffset.x(), 0);
        scrollBarContainers[Qt::Horizontal]->setGeometry(QStyle::visualRect(opt.direction, opt.rect, horizontalScrollBarRect));
        scrollBarContainers[Qt::Horizontal]->raise();
    }

    if (needv) {
        QRect verticalScrollBarRect  (QPoint(cornerPoint.x(), controlsRect.top() + hHeaderBottom),  QPoint(controlsRect.right(), cornerPoint.y() - 1));
        if (!hasCornerWidget && vtransient)
            verticalScrollBarRect.adjust(0, 0, 0, cornerOffset.y());
        scrollBarContainers[Qt::Vertical]->setGeometry(QStyle::visualRect(opt.direction, opt.rect, verticalScrollBarRect));
        scrollBarContainers[Qt::Vertical]->raise();
    }

    if (cornerWidget) {
        const QRect cornerWidgetRect(cornerPoint, controlsRect.bottomRight());
        cornerWidget->setGeometry(QStyle::visualRect(opt.direction, opt.rect, cornerWidgetRect));
    }

    scrollBarContainers[Qt::Horizontal]->setVisible(needh);
    scrollBarContainers[Qt::Vertical]->setVisible(needv);

    if (q->isRightToLeft())
        viewportRect.adjust(right, top, -left, -bottom);
    else
        viewportRect.adjust(left, top, -right, -bottom);
    viewportRect = QStyle::visualRect(opt.direction, opt.rect, viewportRect);
    viewportRect.translate(-overshoot);
    viewport->setGeometry(viewportRect); // resize the viewport last

    *needHorizontalScrollbar = needh;
    *needVerticalScrollbar = needv;
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 1340, as _ZN26QAbstractScrollAreaPrivate21setScrollBarTransientEP10QScrollBarb
#if QT_CONFIG(scrollarea)
inline void QAbstractScrollAreaPrivate::setScrollBarTransient(QScrollBar *scrollBar, bool transient)
{
    scrollBar->d_func()->setTransient(transient);
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 1363, as _ZN26QAbstractScrollAreaPrivate23_q_showOrHideScrollBarsEv
#if QT_CONFIG(scrollarea)
inline void QAbstractScrollAreaPrivate::_q_showOrHideScrollBars()
{
    layoutChildren();
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 1485, as _ZNK26QAbstractScrollAreaPrivate17defaultSingleStepEv
#if QT_CONFIG(scrollarea)
inline int QAbstractScrollAreaPrivate::defaultSingleStep() const
{
    auto *platformTheme = QGuiApplicationPrivate::platformTheme();
    return platformTheme->themeHint(QPlatformTheme::ScrollSingleStepDistance).value<int>();
}
#endif  // QT_CONFIG(scrollarea)
//  -----------------------------------------------------------------------

//  A QAbstractScrollAreaPrivate that Python can take functions over in. Every QAbstractScrollAreaPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(scrollarea)
typedef void (*CuteQAbstractScrollAreaPrivateCall0)(const void *, int, int, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef bool (*CuteQAbstractScrollAreaPrivateCall1)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef const QPoint * (*CuteQAbstractScrollAreaPrivateCall2)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
typedef void (*CuteQAbstractScrollAreaPrivateCall3)(const void *, bool, int *);
typedef void (*CuteQAbstractScrollAreaPrivateCall4)(const void *, int, int *);
typedef void (*CuteQAbstractScrollAreaPrivateCall5)(const void *, int *);
typedef void (*CuteQAbstractScrollAreaPrivateCall6)(const void *, int *);
typedef void * (*CuteQAbstractScrollAreaPrivateCall7)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQAbstractScrollAreaPrivateCall8)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQAbstractScrollAreaPrivateCall9)(const void *, int *);
typedef int (*CuteQAbstractScrollAreaPrivateCall10)(const void *, int *);
typedef const QImage * (*CuteQAbstractScrollAreaPrivateCall11)(const void *, int *);
typedef void (*CuteQAbstractScrollAreaPrivateCall12)(const void *, int *);
typedef void (*CuteQAbstractScrollAreaPrivateCall13)(const void *, int *);
typedef void (*CuteQAbstractScrollAreaPrivateCall14)(const void *, int *);
typedef void (*CuteQAbstractScrollAreaPrivateCall15)(const void *, int *);
typedef void (*CuteQAbstractScrollAreaPrivateCall16)(const void *, int *);
typedef void (*CuteQAbstractScrollAreaPrivateCall17)(const void *, int *);
typedef void (*CuteQAbstractScrollAreaPrivateCall18)(const void *, int *);
typedef bool (*CuteQAbstractScrollAreaPrivateCall19)(const void *, int *);
typedef bool (*CuteQAbstractScrollAreaPrivateCall20)(const void *, int *);
class CuteQAbstractScrollAreaPrivate : public QAbstractScrollAreaPrivate {
public:
  using QAbstractScrollAreaPrivate::QAbstractScrollAreaPrivate;
  void *taken[21] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN26QAbstractScrollAreaPrivate22scrollBarPolicyChangedEN2Qt11OrientationENS0_15ScrollBarPolicyE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK26QAbstractScrollAreaPrivate19canStartScrollingAtERK6QPoint")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK26QAbstractScrollAreaPrivate14contentsOffsetEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10setVisibleEb")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14aboutToDestroyEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate8recreateEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate11focusObjectEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate9rhiConfigEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate7textureEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate16textureListFlagsEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15grabFramebufferEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25beginBackingStorePaintingEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate23endBackingStorePaintingEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate12beginComposeEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10endComposeEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate29initializeViewportFramebufferEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25resizeViewportFramebufferEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14resolveSamplesEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15isStereoEnabledEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate24toggleStereoTargetBufferEv")) {
      taken[20] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(scrollarea)
  //  void
  //      QAbstractScrollAreaPrivate::scrollBarPolicyChanged(Qt::Orientatio
  //      n a0, Qt::ScrollBarPolicy a1)
  void scrollBarPolicyChanged(
      Qt::Orientation a0,
      Qt::ScrollBarPolicy a1) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractScrollAreaPrivateCall0 call = reinterpret_cast<CuteQAbstractScrollAreaPrivateCall0>(taken[0]);
      call(this, static_cast<int>(a0), static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QAbstractScrollAreaPrivate::scrollBarPolicyChanged(a0, a1);
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  bool QAbstractScrollAreaPrivate::canStartScrollingAt(const QPoint
  //      &startPos) const
  bool canStartScrollingAt(const QPoint &startPos) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractScrollAreaPrivateCall1 call = reinterpret_cast<CuteQAbstractScrollAreaPrivateCall1>(taken[1]);
      bool given = call(this, &startPos, &handled);
      if (handled) return given;
    }
    return QAbstractScrollAreaPrivate::canStartScrollingAt(startPos);
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  QPoint QAbstractScrollAreaPrivate::contentsOffset() const
  QPoint contentsOffset() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractScrollAreaPrivateCall2 call = reinterpret_cast<CuteQAbstractScrollAreaPrivateCall2>(taken[2]);
      const QPoint * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollAreaPrivate::contentsOffset();
  }
#endif  // QT_CONFIG(scrollarea)

  //  void QWidgetPrivate::setVisible(bool a0)
  void setVisible(bool a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractScrollAreaPrivateCall3 call = reinterpret_cast<CuteQAbstractScrollAreaPrivateCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractScrollAreaPrivateCall4 call = reinterpret_cast<CuteQAbstractScrollAreaPrivateCall4>(taken[4]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractScrollAreaPrivateCall5 call = reinterpret_cast<CuteQAbstractScrollAreaPrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractScrollAreaPrivateCall6 call = reinterpret_cast<CuteQAbstractScrollAreaPrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractScrollAreaPrivateCall7 call = reinterpret_cast<CuteQAbstractScrollAreaPrivateCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractScrollAreaPrivateCall8 call = reinterpret_cast<CuteQAbstractScrollAreaPrivateCall8>(taken[8]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractScrollAreaPrivateCall9 call = reinterpret_cast<CuteQAbstractScrollAreaPrivateCall9>(taken[9]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstractScrollAreaPrivateCall10 call = reinterpret_cast<CuteQAbstractScrollAreaPrivateCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[11]) {
      int handled = 0;
      CuteQAbstractScrollAreaPrivateCall11 call = reinterpret_cast<CuteQAbstractScrollAreaPrivateCall11>(taken[11]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[12]) {
      int handled = 0;
      CuteQAbstractScrollAreaPrivateCall12 call = reinterpret_cast<CuteQAbstractScrollAreaPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[13]) {
      int handled = 0;
      CuteQAbstractScrollAreaPrivateCall13 call = reinterpret_cast<CuteQAbstractScrollAreaPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[14]) {
      int handled = 0;
      CuteQAbstractScrollAreaPrivateCall14 call = reinterpret_cast<CuteQAbstractScrollAreaPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[15]) {
      int handled = 0;
      CuteQAbstractScrollAreaPrivateCall15 call = reinterpret_cast<CuteQAbstractScrollAreaPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[16]) {
      int handled = 0;
      CuteQAbstractScrollAreaPrivateCall16 call = reinterpret_cast<CuteQAbstractScrollAreaPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[17]) {
      int handled = 0;
      CuteQAbstractScrollAreaPrivateCall17 call = reinterpret_cast<CuteQAbstractScrollAreaPrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[18]) {
      int handled = 0;
      CuteQAbstractScrollAreaPrivateCall18 call = reinterpret_cast<CuteQAbstractScrollAreaPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[19]) {
      int handled = 0;
      CuteQAbstractScrollAreaPrivateCall19 call = reinterpret_cast<CuteQAbstractScrollAreaPrivateCall19>(taken[19]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[20]) {
      int handled = 0;
      CuteQAbstractScrollAreaPrivateCall20 call = reinterpret_cast<CuteQAbstractScrollAreaPrivateCall20>(taken[20]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QAbstractScrollArea *QAbstractScrollAreaPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAbstractScrollArea *ritual_ZN26QAbstractScrollAreaPrivate6q_funcEv(
    QAbstractScrollAreaPrivate *self) {
  return self->q_func();
}

//  const QAbstractScrollArea *QAbstractScrollAreaPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAbstractScrollArea *ritual_ZNK26QAbstractScrollAreaPrivate6q_funcEv(
    const QAbstractScrollAreaPrivate *self) {
  return self->q_func();
}

#if QT_CONFIG(scrollarea)
//  QAbstractScrollAreaPrivate::QAbstractScrollAreaPrivate()
extern "C" Q_DECL_EXPORT
QAbstractScrollAreaPrivate *ritual_ZN26QAbstractScrollAreaPrivateC1Ev() {
  return new CuteQAbstractScrollAreaPrivate();
}
#endif  // QT_CONFIG(scrollarea)

//  QAbstractScrollAreaPrivate::~QAbstractScrollAreaPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractScrollAreaPrivateD1Ev(
    QAbstractScrollAreaPrivate *self) {
  delete self;
}

#if QT_CONFIG(scrollarea)
//  void QAbstractScrollAreaPrivate::replaceScrollBar(QScrollBar *scrollBar,
//      Qt::Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractScrollAreaPrivate16replaceScrollBarEP10QScrollBarN2Qt11OrientationE(
    QAbstractScrollAreaPrivate *self,
    QScrollBar *scrollBar,
    Qt::Orientation orientation) {
  self->replaceScrollBar(scrollBar, orientation);
}
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
#if defined(Q_OS_LINUX)
//  void QAbstractScrollAreaPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractScrollAreaPrivate4initEv(
    QAbstractScrollAreaPrivate *self) {
  self->init();
}
#endif  // defined(Q_OS_LINUX)
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
//  void QAbstractScrollAreaPrivate::layoutChildren()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractScrollAreaPrivate14layoutChildrenEv(
    QAbstractScrollAreaPrivate *self) {
  self->layoutChildren();
}
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
//  void QAbstractScrollAreaPrivate::layoutChildren_helper(bool
//      *needHorizontalScrollbar, bool *needVerticalScrollbar)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractScrollAreaPrivate21layoutChildren_helperEPbS0_(
    QAbstractScrollAreaPrivate *self,
    bool *needHorizontalScrollbar,
    bool *needVerticalScrollbar) {
  self->layoutChildren_helper(
      needHorizontalScrollbar,
      needVerticalScrollbar);
}
#endif  // QT_CONFIG(scrollarea)

//  void QAbstractScrollAreaPrivate::scrollBarPolicyChanged(Qt::Orientation
//      a0, Qt::ScrollBarPolicy a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractScrollAreaPrivate22scrollBarPolicyChangedEN2Qt11OrientationENS0_15ScrollBarPolicyE(
    QAbstractScrollAreaPrivate *self,
    Qt::Orientation a0,
    Qt::ScrollBarPolicy a1) {
  self->scrollBarPolicyChanged(a0, a1);
}

//  bool QAbstractScrollAreaPrivate::canStartScrollingAt(const QPoint
//      &startPos) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QAbstractScrollAreaPrivate19canStartScrollingAtERK6QPoint(
    const QAbstractScrollAreaPrivate *self,
    const QPoint *startPos) {
  return self->canStartScrollingAt(*startPos);
}

#if QT_CONFIG(scrollarea)
//  void QAbstractScrollAreaPrivate::setScrollBarTransient(QScrollBar
//      *scrollBar, bool transient)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractScrollAreaPrivate21setScrollBarTransientEP10QScrollBarb(
    QAbstractScrollAreaPrivate *self,
    QScrollBar *scrollBar,
    bool transient) {
  self->setScrollBarTransient(scrollBar, transient);
}
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
//  void QAbstractScrollAreaPrivate::_q_showOrHideScrollBars()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractScrollAreaPrivate23_q_showOrHideScrollBarsEv(
    QAbstractScrollAreaPrivate *self) {
  self->_q_showOrHideScrollBars();
}
#endif  // QT_CONFIG(scrollarea)

//  QPoint QAbstractScrollAreaPrivate::contentsOffset() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK26QAbstractScrollAreaPrivate14contentsOffsetEv(
    const QAbstractScrollAreaPrivate *self) {
  return new QPoint(self->contentsOffset());
}

//  bool QAbstractScrollAreaPrivate::viewportEvent(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QAbstractScrollAreaPrivate13viewportEventEP6QEvent(
    QAbstractScrollAreaPrivate *self,
    QEvent *event) {
  return self->viewportEvent(event);
}

#if QT_CONFIG(scrollarea)
//  int QAbstractScrollAreaPrivate::defaultSingleStep() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QAbstractScrollAreaPrivate17defaultSingleStepEv(
    const QAbstractScrollAreaPrivate *self) {
  return self->defaultSingleStep();
}
#endif  // QT_CONFIG(scrollarea)

//  a Python function taken by a CuteQAbstractScrollAreaPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractScrollAreaPrivate(
    QAbstractScrollAreaPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractScrollAreaPrivate *>(self)->take(key, call);
}

//  void QAbstractScrollAreaPrivate::scrollBarPolicyChanged(Qt::Orientation
//      a0, Qt::ScrollBarPolicy a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QAbstractScrollAreaPrivate22scrollBarPolicyChangedEN2Qt11OrientationENS0_15ScrollBarPolicyE(
    QAbstractScrollAreaPrivate *self,
    Qt::Orientation a0,
    Qt::ScrollBarPolicy a1) {
  self->QAbstractScrollAreaPrivate::scrollBarPolicyChanged(a0, a1);
}

#if QT_CONFIG(scrollarea)
//  bool QAbstractScrollAreaPrivate::canStartScrollingAt(const QPoint
//      &startPos) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK26QAbstractScrollAreaPrivate19canStartScrollingAtERK6QPoint(
    const QAbstractScrollAreaPrivate *self,
    const QPoint *startPos) {
  return self->QAbstractScrollAreaPrivate::canStartScrollingAt(*startPos);
}
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
//  QPoint QAbstractScrollAreaPrivate::contentsOffset() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_own_ZNK26QAbstractScrollAreaPrivate14contentsOffsetEv(
    const QAbstractScrollAreaPrivate *self) {
  return new QPoint(self->QAbstractScrollAreaPrivate::contentsOffset());
}
#endif  // QT_CONFIG(scrollarea)

#endif  // QT_CONFIG(scrollarea)
