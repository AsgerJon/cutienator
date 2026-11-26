//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtextedit_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qtextedit.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qtextedit_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtGui/qtextobject.h>
#include <QtCore/qurl.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
#include <QtWidgets/private/qtextedit_p.h>
#if QT_CONFIG(lineedit)
#include <QtWidgets/qlineedit.h>
#endif
#if QT_CONFIG(textbrowser)
#include <QtWidgets/qtextbrowser.h>
#endif
#include <QtGui/qfont.h>
#include <QtGui/qpainter.h>
#include <QtGui/qevent.h>
#include <QtCore/qdebug.h>
#if QT_CONFIG(draganddrop)
#include <QtGui/qdrag.h>
#endif
#include <QtGui/qclipboard.h>
#if QT_CONFIG(menu)
#include <QtWidgets/qmenu.h>
#endif
#include <QtWidgets/qstyle.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
#include <QtGui/private/qtextdocumentlayout_p.h>
#include <QtGui/qtextdocument.h>
#include <QtGui/private/qtextdocument_p.h>
#include <QtGui/qtextlist.h>
#include <QtWidgets/private/qwidgettextcontrol_p.h>
#include <QtGui/qtextformat.h>
#include <QtCore/qdatetime.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/private/qapplication_p.h>
#include <limits.h>
#include <QtGui/qtextobject.h>
#include <QtGui/qtexttable.h>
#include <QtCore/qvariant.h>
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/widgets/qtextedit.cpp, line 54, as local:qtextedit.cpp:QTextEditControl
class QTextEditControl : public QWidgetTextControl
{
public:
    inline QTextEditControl(QObject *parent) : QWidgetTextControl(parent) {}

    virtual QMimeData *createMimeDataFromSelection() const override {
        QTextEdit *ed = qobject_cast<QTextEdit *>(parent());
        if (!ed)
            return QWidgetTextControl::createMimeDataFromSelection();
        return ed->createMimeDataFromSelection();
    }
    virtual bool canInsertFromMimeData(const QMimeData *source) const override {
        QTextEdit *ed = qobject_cast<QTextEdit *>(parent());
        if (!ed)
            return QWidgetTextControl::canInsertFromMimeData(source);
        return ed->canInsertFromMimeData(source);
    }
    virtual void insertFromMimeData(const QMimeData *source) override {
        QTextEdit *ed = qobject_cast<QTextEdit *>(parent());
        if (!ed)
            QWidgetTextControl::insertFromMimeData(source);
        else
            ed->insertFromMimeData(source);
    }
    QVariant loadResource(int type, const QUrl &name) override {
        auto *ed = qobject_cast<QTextEdit *>(parent());
        if (!ed)
            return QWidgetTextControl::loadResource(type, name);

        QUrl resolvedName = ed->d_func()->resolveUrl(name);
        return ed->loadResource(type, resolvedName);
    }
};

//  from src/widgets/widgets/qtextedit.cpp, line 262, as local:qtextedit.cpp:documentSize
#if QT_CONFIG(scrollbar)
static QSize documentSize(QWidgetTextControl *control)
{
    QTextDocument *doc = control->document();
    QAbstractTextDocumentLayout *layout = doc->documentLayout();

    QSize docSize;

    if (QTextDocumentLayout *tlayout = qobject_cast<QTextDocumentLayout *>(layout)) {
        docSize = tlayout->dynamicDocumentSize().toSize();
        int percentageDone = tlayout->layoutStatus();
        // extrapolate height
        if (percentageDone > 0)
            docSize.setHeight(docSize.height() * 100 / percentageDone);
    } else {
        docSize = layout->documentSize().toSize();
    }

    return docSize;
}
#endif  // QT_CONFIG(scrollbar)

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 133, as _ZN26QAbstractScrollAreaPrivateC2Ev
#if QT_CONFIG(scrollarea)
inline QAbstractScrollAreaPrivate::QAbstractScrollAreaPrivate()
    :hbar(nullptr), vbar(nullptr), vbarpolicy(Qt::ScrollBarAsNeeded), hbarpolicy(Qt::ScrollBarAsNeeded),
     shownOnce(false), inResize(false), sizeAdjustPolicy(QAbstractScrollArea::AdjustIgnored),
     viewport(nullptr), cornerWidget(nullptr), left(0), top(0), right(0), bottom(0),
     xoffset(0), yoffset(0), viewportFilter(nullptr)
{
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 141, as _ZN26QAbstractScrollAreaPrivateD2Ev
#if QT_CONFIG(scrollarea)
inline QAbstractScrollAreaPrivate::~QAbstractScrollAreaPrivate()
{
}
#endif  // QT_CONFIG(scrollarea)

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

//  from src/widgets/widgets/qtextedit.cpp, line 282, as _ZN16QTextEditPrivate16adjustScrollbarsEv
#if QT_CONFIG(scrollbar)
inline void QTextEditPrivate::adjustScrollbars()
{
    if (ignoreAutomaticScrollbarAdjustment)
        return;
    ignoreAutomaticScrollbarAdjustment = true; // avoid recursion, #106108

    QSize viewportSize = viewport->size();
    QSize docSize = documentSize(control);

    // due to the recursion guard we have to repeat this step a few times,
    // as adding/removing a scroll bar will cause the document or viewport
    // size to change
    // ideally we should loop until the viewport size and doc size stabilize,
    // but in corner cases they might fluctuate, so we need to limit the
    // number of iterations
    for (int i = 0; i < 4; ++i) {
        hbar->setRange(0, docSize.width() - viewportSize.width());
        hbar->setPageStep(viewportSize.width());

        vbar->setRange(0, docSize.height() - viewportSize.height());
        vbar->setPageStep(viewportSize.height());

        // if we are in left-to-right mode widening the document due to
        // lazy layouting does not require a repaint. If in right-to-left
        // the scroll bar has the value zero and it visually has the maximum
        // value (it is visually at the right), then widening the document
        // keeps it at value zero but visually adjusts it to the new maximum
        // on the right, hence we need an update.
        if (q_func()->isRightToLeft())
            viewport->update();

        _q_showOrHideScrollBars();

        const QSize oldViewportSize = viewportSize;
        const QSize oldDocSize = docSize;

        // make sure the document is layouted if the viewport width changes
        viewportSize = viewport->size();
        if (viewportSize.width() != oldViewportSize.width())
            relayoutDocument();

        docSize = documentSize(control);
        if (viewportSize == oldViewportSize && docSize == oldDocSize)
            break;
    }
    ignoreAutomaticScrollbarAdjustment = false;
}
#endif  // QT_CONFIG(scrollbar)

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

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 1363, as _ZN26QAbstractScrollAreaPrivate23_q_showOrHideScrollBarsEv
#if QT_CONFIG(scrollarea)
inline void QAbstractScrollAreaPrivate::_q_showOrHideScrollBars()
{
    layoutChildren();
}
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

//  from src/widgets/widgets/qtextedit.cpp, line 88, as _ZN16QTextEditPrivateC1Ev
inline QTextEditPrivate::QTextEditPrivate()
    : control(nullptr),
      autoFormatting(QTextEdit::AutoNone), tabChangesFocus(false),
      lineWrap(QTextEdit::WidgetWidth), lineWrapColumnOrWidth(0),
      wordWrap(QTextOption::WrapAtWordBoundaryOrAnywhere), clickCausedFocus(0)
{
    ignoreAutomaticScrollbarAdjustment = false;
    preferRichText = false;
    showCursorOnInitialShow = true;
    inDrag = false;
}

//  from src/widgets/widgets/qtextedit.cpp, line 100, as _ZN16QTextEditPrivateD1Ev
inline QTextEditPrivate::~QTextEditPrivate()
{
    for (QMetaObject::Connection &connection : connections)
        QObject::disconnect(connection);
}

//  from src/widgets/widgets/qtextedit.cpp, line 1485, as _ZN16QTextEditPrivate5paintEP8QPainterP11QPaintEvent
inline void QTextEditPrivate::paint(QPainter *p, QPaintEvent *e)
{
    const int xOffset = horizontalOffset();
    const int yOffset = verticalOffset();

    QRect r = e->rect();
    p->translate(-xOffset, -yOffset);
    r.translate(xOffset, yOffset);

    QTextDocument *doc = control->document();
    QTextDocumentLayout *layout = qobject_cast<QTextDocumentLayout *>(doc->documentLayout());

    // the layout might need to expand the root frame to
    // the viewport if NoWrap is set
    if (layout)
        layout->setViewport(viewport->rect());

    control->drawContents(p, r, q_func());

    if (layout)
        layout->setViewport(QRect());

    if (!placeholderText.isEmpty() && doc->isEmpty() && !control->isPreediting()) {
        const QColor col = control->palette().placeholderText().color();
        p->setPen(col);
        const int margin = int(doc->documentMargin());
        QRectF boundingRect = layout ? layout->frameBoundingRect(doc->rootFrame()) : viewport->rect();
        p->drawText(boundingRect.adjusted(margin, margin, -margin, -margin),
                    Qt::AlignTop | Qt::TextWordWrap,
                    placeholderText);
    }
}

//  from src/widgets/widgets/qtextedit.cpp, line 190, as _ZN16QTextEditPrivate15repaintContentsERK6QRectF
inline void QTextEditPrivate::repaintContents(const QRectF &contentsRect)
{
    if (!contentsRect.isValid()) {
        viewport->update();
        return;
    }
    const int xOffset = horizontalOffset();
    const int yOffset = verticalOffset();
    const QRectF visibleRect(xOffset, yOffset, viewport->width(), viewport->height());

    QRect r = contentsRect.intersected(visibleRect).toAlignedRect();
    if (r.isEmpty())
        return;

    r.translate(-xOffset, -yOffset);
    viewport->update(r);
}

//  from src/widgets/widgets/qtextedit.cpp, line 332, as _ZN16QTextEditPrivate13ensureVisibleERK6QRectF
inline void QTextEditPrivate::ensureVisible(const QRectF &_rect)
{
    const QRect rect = _rect.toRect();
    if ((vbar->isVisible() && vbar->maximum() < rect.bottom())
        || (hbar->isVisible() && hbar->maximum() < rect.right()))
        adjustScrollbars();
    const int visibleWidth = viewport->width();
    const int visibleHeight = viewport->height();
    const bool rtl = q_func()->isRightToLeft();

    if (rect.x() < horizontalOffset()) {
        if (rtl)
            hbar->setValue(hbar->maximum() - rect.x());
        else
            hbar->setValue(rect.x());
    } else if (rect.x() + rect.width() > horizontalOffset() + visibleWidth) {
        if (rtl)
            hbar->setValue(hbar->maximum() - (rect.x() + rect.width() - visibleWidth));
        else
            hbar->setValue(rect.x() + rect.width() - visibleWidth);
    }

    if (rect.y() < verticalOffset())
        vbar->setValue(rect.y());
    else if (rect.y() + rect.height() > verticalOffset() + visibleHeight)
        vbar->setValue(rect.y() + rect.height() - visibleHeight);
}

//  from src/widgets/widgets/qtextedit.cpp, line 1411, as _ZN16QTextEditPrivate16relayoutDocumentEv
inline void QTextEditPrivate::relayoutDocument()
{
    QTextDocument *doc = control->document();
    QAbstractTextDocumentLayout *layout = doc->documentLayout();

    if (QTextDocumentLayout *tlayout = qobject_cast<QTextDocumentLayout *>(layout)) {
        if (lineWrap == QTextEdit::FixedColumnWidth)
            tlayout->setFixedColumnWidth(lineWrapColumnOrWidth);
        else
            tlayout->setFixedColumnWidth(-1);
    }

    QTextDocumentLayout *tlayout = qobject_cast<QTextDocumentLayout *>(layout);
    QSize lastUsedSize;
    if (tlayout)
        lastUsedSize = tlayout->dynamicDocumentSize().toSize();
    else
        lastUsedSize = layout->documentSize().toSize();

    // ignore calls to adjustScrollbars caused by an emission of the
    // usedSizeChanged() signal in the layout, as we're calling it
    // later on our own anyway (or deliberately not) .
    const bool oldIgnoreScrollbarAdjustment = ignoreAutomaticScrollbarAdjustment;
    ignoreAutomaticScrollbarAdjustment = true;

    int width = viewport->width();
    if (lineWrap == QTextEdit::FixedPixelWidth)
        width = lineWrapColumnOrWidth;
    else if (lineWrap == QTextEdit::NoWrap) {
        QVariant alignmentProperty = doc->documentLayout()->property("contentHasAlignment");
        if (alignmentProperty.userType() == QMetaType::Bool && !alignmentProperty.toBool()) {

            width = 0;
        }
    }

    doc->setPageSize(QSize(width, -1));
    if (tlayout)
        tlayout->ensureLayouted(verticalOffset() + viewport->height());

    ignoreAutomaticScrollbarAdjustment = oldIgnoreScrollbarAdjustment;

    QSize usedSize;
    if (tlayout)
        usedSize = tlayout->dynamicDocumentSize().toSize();
    else
        usedSize = layout->documentSize().toSize();

    // this is an obscure situation in the layout that can happen:
    // if a character at the end of a line is the tallest one and therefore
    // influencing the total height of the line and the line right below it
    // is always taller though, then it can happen that if due to line breaking
    // that tall character wraps into the lower line the document not only shrinks
    // horizontally (causing the character to wrap in the first place) but also
    // vertically, because the original line is now smaller and the one below kept
    // its size. So a layout with less width _can_ take up less vertical space, too.
    // If the wider case causes a vertical scroll bar to appear and the narrower one
    // (narrower because the vertical scroll bar takes up horizontal space)) to disappear
    // again then we have an endless loop, as adjustScrollbars sets new ranges on the
    // scroll bars, the QAbstractScrollArea will find out about it and try to show/hide
    // the scroll bars again. That's why we try to detect this case here and break out.
    //
    // (if you change this please also check the layoutingLoop() testcase in
    // QTextEdit's autotests)
    if (lastUsedSize.isValid()
        && !vbar->isHidden()
        && viewport->width() < lastUsedSize.width()
        && usedSize.height() < lastUsedSize.height()
        && usedSize.height() <= viewport->height())
        return;

    adjustScrollbars();
}

//  from src/widgets/widgets/qtextedit.cpp, line 106, as _ZN16QTextEditPrivate20createAutoBulletListEv
inline void QTextEditPrivate::createAutoBulletList()
{
    QTextCursor cursor = control->textCursor();
    cursor.beginEditBlock();

    QTextBlockFormat blockFmt = cursor.blockFormat();

    QTextListFormat listFmt;
    listFmt.setStyle(QTextListFormat::ListDisc);
    listFmt.setIndent(blockFmt.indent() + 1);

    blockFmt.setIndent(0);
    cursor.setBlockFormat(blockFmt);

    cursor.createList(listFmt);

    cursor.endEditBlock();
    control->setTextCursor(cursor);
}

//  from src/widgets/widgets/qtextedit.cpp, line 235, as _ZN16QTextEditPrivate10pageUpDownEN11QTextCursor13MoveOperationENS0_8MoveModeE
inline void QTextEditPrivate::pageUpDown(QTextCursor::MoveOperation op, QTextCursor::MoveMode moveMode)
{
    QTextCursor cursor = control->textCursor();
    bool moved = false;
    qreal lastY = control->cursorRect(cursor).top();
    qreal distance = 0;
    // move using movePosition to keep the cursor's x
    do {
        qreal y = control->cursorRect(cursor).top();
        distance += qAbs(y - lastY);
        lastY = y;
        moved = cursor.movePosition(op, moveMode);
    } while (moved && distance < viewport->height());

    if (moved) {
        if (op == QTextCursor::Up) {
            cursor.movePosition(QTextCursor::Down, moveMode);
            vbar->triggerAction(QAbstractSlider::SliderPageStepSub);
        } else {
            cursor.movePosition(QTextCursor::Up, moveMode);
            vbar->triggerAction(QAbstractSlider::SliderPageStepAdd);
        }
    }
    control->setTextCursor(cursor, moveMode == QTextCursor::KeepAnchor);
}

//  from src/widgets/widgets/qtextedit.cpp, line 208, as _ZN16QTextEditPrivate21cursorPositionChangedEv
inline void QTextEditPrivate::cursorPositionChanged()
{
    Q_Q(QTextEdit);
    emit q->cursorPositionChanged();
#if QT_CONFIG(accessibility)
    QAccessibleTextCursorEvent event(q, q->textCursor().position());
    QAccessible::updateAccessibility(&event);
#endif
}

//  from src/widgets/widgets/qtextedit.cpp, line 218, as _ZN16QTextEditPrivate29hoveredBlockWithMarkerChangedERK10QTextBlock
inline void QTextEditPrivate::hoveredBlockWithMarkerChanged(const QTextBlock &block)
{
#if QT_CONFIG(cursor)
    Q_Q(QTextEdit);
    Qt::CursorShape cursor = cursorToRestoreAfterHover;
    if (block.isValid() && !q->isReadOnly()) {
        QTextBlockFormat::MarkerType marker = block.blockFormat().marker();
        if (marker != QTextBlockFormat::MarkerType::NoMarker) {
            if (viewport->cursor().shape() != Qt::PointingHandCursor)
                cursorToRestoreAfterHover = viewport->cursor().shape();
            cursor = Qt::PointingHandCursor;
        }
    }
    viewport->setCursor(cursor);
#endif
}

//  from src/widgets/widgets/qtextedit.cpp, line 1535, as _ZN16QTextEditPrivate23updateDefaultTextOptionEv
inline void QTextEditPrivate::updateDefaultTextOption()
{
    QTextDocument *doc = control->document();

    QTextOption opt = doc->defaultTextOption();
    QTextOption::WrapMode oldWrapMode = opt.wrapMode();

    if (lineWrap == QTextEdit::NoWrap)
        opt.setWrapMode(QTextOption::NoWrap);
    else
        opt.setWrapMode(wordWrap);

    if (opt.wrapMode() != oldWrapMode)
        doc->setDefaultTextOption(opt);
}
//  -----------------------------------------------------------------------

//  A QTextEditPrivate that Python can take functions over in. Every QTextEditPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(textedit)
typedef const QUrl * (*CuteQTextEditPrivateCall0)(const void *, const QUrl *, int *);
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQTextEditPrivateCall1)(const void *, int, int, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef bool (*CuteQTextEditPrivateCall2)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef const QPoint * (*CuteQTextEditPrivateCall3)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
typedef void (*CuteQTextEditPrivateCall4)(const void *, bool, int *);
typedef void (*CuteQTextEditPrivateCall5)(const void *, int, int *);
typedef void (*CuteQTextEditPrivateCall6)(const void *, int *);
typedef void (*CuteQTextEditPrivateCall7)(const void *, int *);
typedef void * (*CuteQTextEditPrivateCall8)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQTextEditPrivateCall9)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQTextEditPrivateCall10)(const void *, int *);
typedef int (*CuteQTextEditPrivateCall11)(const void *, int *);
typedef const QImage * (*CuteQTextEditPrivateCall12)(const void *, int *);
typedef void (*CuteQTextEditPrivateCall13)(const void *, int *);
typedef void (*CuteQTextEditPrivateCall14)(const void *, int *);
typedef void (*CuteQTextEditPrivateCall15)(const void *, int *);
typedef void (*CuteQTextEditPrivateCall16)(const void *, int *);
typedef void (*CuteQTextEditPrivateCall17)(const void *, int *);
typedef void (*CuteQTextEditPrivateCall18)(const void *, int *);
typedef void (*CuteQTextEditPrivateCall19)(const void *, int *);
typedef bool (*CuteQTextEditPrivateCall20)(const void *, int *);
typedef bool (*CuteQTextEditPrivateCall21)(const void *, int *);
class CuteQTextEditPrivate : public QTextEditPrivate {
public:
  using QTextEditPrivate::QTextEditPrivate;
  void *taken[22] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK16QTextEditPrivate10resolveUrlERK4QUrl")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN26QAbstractScrollAreaPrivate22scrollBarPolicyChangedEN2Qt11OrientationENS0_15ScrollBarPolicyE")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK26QAbstractScrollAreaPrivate19canStartScrollingAtERK6QPoint")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK26QAbstractScrollAreaPrivate14contentsOffsetEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10setVisibleEb")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14aboutToDestroyEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate8recreateEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate11focusObjectEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate9rhiConfigEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate7textureEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate16textureListFlagsEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15grabFramebufferEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25beginBackingStorePaintingEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate23endBackingStorePaintingEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate12beginComposeEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10endComposeEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate29initializeViewportFramebufferEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25resizeViewportFramebufferEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14resolveSamplesEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15isStereoEnabledEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate24toggleStereoTargetBufferEv")) {
      taken[21] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(textedit)
  //  QUrl QTextEditPrivate::resolveUrl(const QUrl &url) const
  QUrl resolveUrl(const QUrl &url) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQTextEditPrivateCall0 call = reinterpret_cast<CuteQTextEditPrivateCall0>(taken[0]);
      const QUrl * given = call(this, &url, &handled);
      if (handled && given) return *given;
    }
    return QTextEditPrivate::resolveUrl(url);
  }
#endif  // QT_CONFIG(textedit)

#if QT_CONFIG(scrollarea)
  //  void
  //      QAbstractScrollAreaPrivate::scrollBarPolicyChanged(Qt::Orientatio
  //      n a0, Qt::ScrollBarPolicy a1)
  void scrollBarPolicyChanged(
      Qt::Orientation a0,
      Qt::ScrollBarPolicy a1) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTextEditPrivateCall1 call = reinterpret_cast<CuteQTextEditPrivateCall1>(taken[1]);
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
    if (taken[2]) {
      int handled = 0;
      CuteQTextEditPrivateCall2 call = reinterpret_cast<CuteQTextEditPrivateCall2>(taken[2]);
      bool given = call(this, &startPos, &handled);
      if (handled) return given;
    }
    return QAbstractScrollAreaPrivate::canStartScrollingAt(startPos);
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  QPoint QAbstractScrollAreaPrivate::contentsOffset() const
  QPoint contentsOffset() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQTextEditPrivateCall3 call = reinterpret_cast<CuteQTextEditPrivateCall3>(taken[3]);
      const QPoint * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollAreaPrivate::contentsOffset();
  }
#endif  // QT_CONFIG(scrollarea)

  //  void QWidgetPrivate::setVisible(bool a0)
  void setVisible(bool a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTextEditPrivateCall4 call = reinterpret_cast<CuteQTextEditPrivateCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[5]) {
      int handled = 0;
      CuteQTextEditPrivateCall5 call = reinterpret_cast<CuteQTextEditPrivateCall5>(taken[5]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[6]) {
      int handled = 0;
      CuteQTextEditPrivateCall6 call = reinterpret_cast<CuteQTextEditPrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[7]) {
      int handled = 0;
      CuteQTextEditPrivateCall7 call = reinterpret_cast<CuteQTextEditPrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[8]) {
      int handled = 0;
      CuteQTextEditPrivateCall8 call = reinterpret_cast<CuteQTextEditPrivateCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQTextEditPrivateCall9 call = reinterpret_cast<CuteQTextEditPrivateCall9>(taken[9]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQTextEditPrivateCall10 call = reinterpret_cast<CuteQTextEditPrivateCall10>(taken[10]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[11]) {
      int handled = 0;
      CuteQTextEditPrivateCall11 call = reinterpret_cast<CuteQTextEditPrivateCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[12]) {
      int handled = 0;
      CuteQTextEditPrivateCall12 call = reinterpret_cast<CuteQTextEditPrivateCall12>(taken[12]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[13]) {
      int handled = 0;
      CuteQTextEditPrivateCall13 call = reinterpret_cast<CuteQTextEditPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[14]) {
      int handled = 0;
      CuteQTextEditPrivateCall14 call = reinterpret_cast<CuteQTextEditPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[15]) {
      int handled = 0;
      CuteQTextEditPrivateCall15 call = reinterpret_cast<CuteQTextEditPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[16]) {
      int handled = 0;
      CuteQTextEditPrivateCall16 call = reinterpret_cast<CuteQTextEditPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[17]) {
      int handled = 0;
      CuteQTextEditPrivateCall17 call = reinterpret_cast<CuteQTextEditPrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[18]) {
      int handled = 0;
      CuteQTextEditPrivateCall18 call = reinterpret_cast<CuteQTextEditPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[19]) {
      int handled = 0;
      CuteQTextEditPrivateCall19 call = reinterpret_cast<CuteQTextEditPrivateCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[20]) {
      int handled = 0;
      CuteQTextEditPrivateCall20 call = reinterpret_cast<CuteQTextEditPrivateCall20>(taken[20]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[21]) {
      int handled = 0;
      CuteQTextEditPrivateCall21 call = reinterpret_cast<CuteQTextEditPrivateCall21>(taken[21]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QTextEdit *QTextEditPrivate::q_func()
extern "C" Q_DECL_EXPORT
QTextEdit *ritual_ZN16QTextEditPrivate6q_funcEv(QTextEditPrivate *self) {
  return self->q_func();
}

//  const QTextEdit *QTextEditPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QTextEdit *ritual_ZNK16QTextEditPrivate6q_funcEv(
    const QTextEditPrivate *self) {
  return self->q_func();
}

#if QT_CONFIG(scrollarea)
//  QTextEditPrivate::QTextEditPrivate()
extern "C" Q_DECL_EXPORT
QTextEditPrivate *ritual_ZN16QTextEditPrivateC1Ev() {
  return new CuteQTextEditPrivate();
}
#endif  // QT_CONFIG(scrollarea)

//  QTextEditPrivate::~QTextEditPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextEditPrivateD1Ev(QTextEditPrivate *self) {
  delete self;
}

//  void QTextEditPrivate::paint(QPainter *p, QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextEditPrivate5paintEP8QPainterP11QPaintEvent(
    QTextEditPrivate *self,
    QPainter *p,
    QPaintEvent *e) {
  self->paint(p, e);
}

//  void QTextEditPrivate::repaintContents(const QRectF &contentsRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextEditPrivate15repaintContentsERK6QRectF(
    QTextEditPrivate *self,
    const QRectF *contentsRect) {
  self->repaintContents(*contentsRect);
}

//  QPoint QTextEditPrivate::mapToContents(const QPoint &point) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK16QTextEditPrivate13mapToContentsERK6QPoint(
    const QTextEditPrivate *self,
    const QPoint *point) {
  return new QPoint(self->mapToContents(*point));
}

#if QT_CONFIG(scrollbar)
#if QT_CONFIG(scrollarea)
//  void QTextEditPrivate::ensureVisible(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextEditPrivate13ensureVisibleERK6QRectF(
    QTextEditPrivate *self,
    const QRectF *rect) {
  self->ensureVisible(*rect);
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(scrollbar)

#if QT_CONFIG(scrollbar)
#if QT_CONFIG(scrollarea)
//  void QTextEditPrivate::relayoutDocument()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextEditPrivate16relayoutDocumentEv(
    QTextEditPrivate *self) {
  self->relayoutDocument();
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(scrollbar)

//  void QTextEditPrivate::createAutoBulletList()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextEditPrivate20createAutoBulletListEv(
    QTextEditPrivate *self) {
  self->createAutoBulletList();
}

//  void QTextEditPrivate::pageUpDown(QTextCursor::MoveOperation op,
//      QTextCursor::MoveMode moveMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextEditPrivate10pageUpDownEN11QTextCursor13MoveOperationENS0_8MoveModeE(
    QTextEditPrivate *self,
    QTextCursor::MoveOperation op,
    QTextCursor::MoveMode moveMode) {
  self->pageUpDown(op, moveMode);
}

//  int QTextEditPrivate::horizontalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTextEditPrivate16horizontalOffsetEv(
    const QTextEditPrivate *self) {
  return self->horizontalOffset();
}

//  int QTextEditPrivate::verticalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTextEditPrivate14verticalOffsetEv(
    const QTextEditPrivate *self) {
  return self->verticalOffset();
}

//  void QTextEditPrivate::sendControlEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextEditPrivate16sendControlEventEP6QEvent(
    QTextEditPrivate *self,
    QEvent *e) {
  self->sendControlEvent(e);
}

//  void QTextEditPrivate::cursorPositionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextEditPrivate21cursorPositionChangedEv(
    QTextEditPrivate *self) {
  self->cursorPositionChanged();
}

//  void QTextEditPrivate::hoveredBlockWithMarkerChanged(const QTextBlock
//      &block)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextEditPrivate29hoveredBlockWithMarkerChangedERK10QTextBlock(
    QTextEditPrivate *self,
    const QTextBlock *block) {
  self->hoveredBlockWithMarkerChanged(*block);
}

//  void QTextEditPrivate::updateDefaultTextOption()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTextEditPrivate23updateDefaultTextOptionEv(
    QTextEditPrivate *self) {
  self->updateDefaultTextOption();
}

//  QUrl QTextEditPrivate::resolveUrl(const QUrl &url) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK16QTextEditPrivate10resolveUrlERK4QUrl(
    const QTextEditPrivate *self,
    const QUrl *url) {
  return new QUrl(self->resolveUrl(*url));
}

//  a Python function taken by a CuteQTextEditPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTextEditPrivate(
    QTextEditPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTextEditPrivate *>(self)->take(key, call);
}

//  QUrl QTextEditPrivate::resolveUrl(const QUrl &url) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_own_ZNK16QTextEditPrivate10resolveUrlERK4QUrl(
    const QTextEditPrivate *self,
    const QUrl *url) {
  return new QUrl(self->QTextEditPrivate::resolveUrl(*url));
}

#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(textedit)
