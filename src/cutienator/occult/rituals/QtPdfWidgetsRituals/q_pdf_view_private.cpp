//  Written by dev_tooling.RitualGenerator from the records of
//  QtPdfWidgets/6.12.0/QtPdfWidgets/private/qpdfview_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtPdfWidgets/qpdfview.h>
#include <QtPdfWidgets/QtPdfWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPdfWidgets/6.12.0/QtPdfWidgets/private/qpdfview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtGui/qimage.h>
#include <QtCore/qpoint.h>
#include <QtPdf/qpdflink.h>
#include <QtGui/qtransform.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPdfWidgets/qpdfview.h>
#include <QtPdfWidgets/private/qpdfview_p.h>
#include <QtPdf/qpdfpagerenderer.h>
#include <QtPdf/private/qtpdfglobal_p.h>
#include <QtGui/QGuiApplication>
#include <QtCore/QLoggingCategory>
#include <QtGui/QPainter>
#include <QtGui/QPaintEvent>
#include <QtPdf/QPdfDocument>
#include <QtPdf/QPdfPageNavigator>
#include <QtPdf/QPdfSearchModel>
#include <QtGui/QScreen>
#include <QtWidgets/QScrollBar>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwebengine/src/pdfwidgets/qpdfview.cpp, line 29, as _ZN15QPdfViewPrivateC1EP8QPdfView
inline QPdfViewPrivate::QPdfViewPrivate(QPdfView *q)
    : q_ptr(q)
    , m_document(nullptr)
    , m_pageNavigator(nullptr)
    , m_pageRenderer(nullptr)
    , m_pageMode(QPdfView::PageMode::SinglePage)
    , m_zoomMode(QPdfView::ZoomMode::Custom)
    , m_zoomFactor(1.0)
    , m_pageSpacing(3)
    , m_documentMargins(6, 6, 6, 6)
    , m_blockPageScrolling(false)
    , m_pageCacheLimit(20)
    , m_screenResolution(QGuiApplication::primaryScreen()->logicalDotsPerInch() / 72.0)
{
}

//  from ../qtwebengine/src/pdfwidgets/qpdfview.cpp, line 45, as _ZN15QPdfViewPrivate4initEv
inline void QPdfViewPrivate::init()
{
    Q_Q(QPdfView);

    m_pageNavigator = new QPdfPageNavigator(q);
    m_pageRenderer = new QPdfPageRenderer(q);
    m_pageRenderer->setRenderMode(QPdfPageRenderer::RenderMode::MultiThreaded);
}

//  from ../qtwebengine/src/pdfwidgets/qpdfview.cpp, line 54, as _ZN15QPdfViewPrivate21documentStatusChangedEN12QPdfDocument6StatusE
inline void QPdfViewPrivate::documentStatusChanged(QPdfDocument::Status status)
{
    if (status == QPdfDocument::Status::Ready)
        updateDocumentLayout();
    invalidatePageCache();
}

//  from ../qtwebengine/src/pdfwidgets/qpdfview.cpp, line 61, as _ZN15QPdfViewPrivate18currentPageChangedEi
inline void QPdfViewPrivate::currentPageChanged(int currentPage)
{
    Q_Q(QPdfView);

    if (m_blockPageScrolling)
        return;

    q->verticalScrollBar()->setValue(yPositionForPage(currentPage));

    if (m_pageMode == QPdfView::PageMode::SinglePage)
        invalidateDocumentLayout();
}

//  from ../qtwebengine/src/pdfwidgets/qpdfview.cpp, line 74, as _ZN15QPdfViewPrivate18currentZoomChangedEd
inline void QPdfViewPrivate::currentZoomChanged(qreal currentZoom)
{
    Q_Q(QPdfView);
    q->setZoomFactor(currentZoom);
}

//  from ../qtwebengine/src/pdfwidgets/qpdfview.cpp, line 80, as _ZN15QPdfViewPrivate17calculateViewportEv
inline void QPdfViewPrivate::calculateViewport()
{
    Q_Q(QPdfView);

    const int x = q->horizontalScrollBar()->value();
    const int y = q->verticalScrollBar()->value();
    const int width = q->viewport()->width();
    const int height = q->viewport()->height();

    setViewport(QRect(x, y, width, height));
}

//  from ../qtwebengine/src/pdfwidgets/qpdfview.cpp, line 92, as _ZN15QPdfViewPrivate11setViewportE5QRect
inline void QPdfViewPrivate::setViewport(QRect viewport)
{
    if (m_viewport == viewport)
        return;

    const QSize oldSize = m_viewport.size();

    m_viewport = viewport;

    if (oldSize != m_viewport.size()) {
        updateDocumentLayout();

        if (m_zoomMode != QPdfView::ZoomMode::Custom) {
            invalidatePageCache();
        }
    }

    if (m_pageMode == QPdfView::PageMode::MultiPage) {
        // An imaginary, 2px height line at the upper half of the viewport, which is used to
        // determine which page is currently located there -> we propagate that as 'current' page
        // to the QPdfPageNavigator object
        const QRect currentPageLine(m_viewport.x(), m_viewport.y() + m_viewport.height() * 0.4, m_viewport.width(), 2);

        int currentPage = 0;
        for (auto it = m_documentLayout.pageGeometryAndScale.cbegin();
             it != m_documentLayout.pageGeometryAndScale.cend(); ++it) {
            const QRect pageGeometry = it.value().first;
            if (pageGeometry.intersects(currentPageLine)) {
                currentPage = it.key();
                break;
            }
        }

        if (currentPage != m_pageNavigator->currentPage()) {
            m_blockPageScrolling = true;
            // ΤODO give location on the page
            m_pageNavigator->jump(currentPage, {}, m_zoomFactor);
            m_blockPageScrolling = false;
        }
    }
}

//  from ../qtwebengine/src/pdfwidgets/qpdfview.cpp, line 134, as _ZN15QPdfViewPrivate16updateScrollBarsEv
inline void QPdfViewPrivate::updateScrollBars()
{
    Q_Q(QPdfView);

    const QSize p = q->viewport()->size();
    const QSize v = m_documentLayout.documentSize;

    q->horizontalScrollBar()->setRange(0, v.width() - p.width());
    q->horizontalScrollBar()->setPageStep(p.width());
    q->verticalScrollBar()->setRange(0, v.height() - p.height());
    q->verticalScrollBar()->setPageStep(p.height());
}

//  from ../qtwebengine/src/pdfwidgets/qpdfview.cpp, line 199, as _ZN15QPdfViewPrivate12pageRenderedEi5QSizeRK6QImagey
inline void QPdfViewPrivate::pageRendered(int pageNumber, QSize imageSize, const QImage &image, quint64 requestId)
{
    Q_Q(QPdfView);

    Q_UNUSED(imageSize);
    Q_UNUSED(requestId);

    if (!m_cachedPagesLRU.contains(pageNumber)) {
        if (m_cachedPagesLRU.size() > m_pageCacheLimit)
            m_pageCache.remove(m_cachedPagesLRU.takeFirst());

        m_cachedPagesLRU.append(pageNumber);
    }

    m_pageCache.insert(pageNumber, image);

    q->viewport()->update();
}

//  from ../qtwebengine/src/pdfwidgets/qpdfview.cpp, line 218, as _ZN15QPdfViewPrivate24invalidateDocumentLayoutEv
inline void QPdfViewPrivate::invalidateDocumentLayout()
{
    updateDocumentLayout();
    invalidatePageCache();
}

//  from ../qtwebengine/src/pdfwidgets/qpdfview.cpp, line 224, as _ZN15QPdfViewPrivate19invalidatePageCacheEv
inline void QPdfViewPrivate::invalidatePageCache()
{
    Q_Q(QPdfView);

    m_pageCache.clear();
    q->viewport()->update();
}

//  from ../qtwebengine/src/pdfwidgets/qpdfview.cpp, line 307, as _ZNK15QPdfViewPrivate16yPositionForPageEi
inline qreal QPdfViewPrivate::yPositionForPage(int pageNumber) const
{
    const auto it = m_documentLayout.pageGeometryAndScale.constFind(pageNumber);
    if (it == m_documentLayout.pageGeometryAndScale.cend())
        return 0.0;

    return (*it).first.y();
}

//  from ../qtwebengine/src/pdfwidgets/qpdfview.cpp, line 316, as _ZN15QPdfViewPrivate12pagePositionERK7QPointF
inline QPdfLink QPdfViewPrivate::pagePosition(const QPointF &viewPosition)
{
    for (auto it = m_documentLayout.pageGeometryAndScale.cbegin();
         it != m_documentLayout.pageGeometryAndScale.cend(); ++it) {
        const int page = it.key();
        const QTransform screenInvTransform = screenScaleTransform(page).inverted();
        const QRect pageGeometry = it.value().first;
        if (pageGeometry.contains(viewPosition.toPoint())) {
            QPointF posInPoints = screenInvTransform.map(viewPosition - pageGeometry.topLeft()
                                                         + m_viewport.topLeft());
            return QPdfLink(page, posInPoints, 1);
        }
    }
    return {}; // invalid: not found
}

//  from ../qtwebengine/src/pdfwidgets/qpdfview.cpp, line 332, as _ZNK15QPdfViewPrivate20screenScaleTransformEi
inline QTransform QPdfViewPrivate::screenScaleTransform(int page) const
{
    qreal scale = m_screenResolution * m_zoomFactor;
    switch (m_zoomMode) {
    case QPdfView::ZoomMode::FitToWidth:
    case QPdfView::ZoomMode::FitInView:
        scale = m_screenResolution * m_documentLayout.pageGeometryAndScale[page].second;
        break;
    default:
        break;
    }

    return QTransform::fromScale(scale, scale);
}

//  from ../qtwebengine/src/pdfwidgets/qpdfview.cpp, line 232, as _ZNK15QPdfViewPrivate23calculateDocumentLayoutEv
inline QPdfViewPrivate::DocumentLayout QPdfViewPrivate::calculateDocumentLayout() const
{
    // The DocumentLayout describes a virtual layout where all pages are positioned inside
    //    - For SinglePage mode, this is just an area as large as the current page surrounded
    //      by the m_documentMargins.
    //    - For MultiPage mode, this is the area that is covered by all pages which are placed
    //      below each other, with m_pageSpacing inbetween and surrounded by m_documentMargins

    DocumentLayout documentLayout;

    if (!m_document || m_document->status() != QPdfDocument::Status::Ready)
        return documentLayout;

    QHash<int, QPair<QRect, qreal>> pageGeometryAndScale;

    const int pageCount = m_document->pageCount();

    int totalWidth = 0;

    const int startPage = (m_pageMode == QPdfView::PageMode::SinglePage ? m_pageNavigator->currentPage() : 0);
    const int endPage = (m_pageMode == QPdfView::PageMode::SinglePage ? m_pageNavigator->currentPage() + 1 : pageCount);

    // calculate page sizes
    for (int page = startPage; page < endPage; ++page) {
        QSize pageSize;
        qreal pageScale = m_zoomFactor;
        if (m_zoomMode == QPdfView::ZoomMode::Custom) {
            pageSize = QSizeF(m_document->pagePointSize(page) * m_screenResolution * m_zoomFactor).toSize();
        } else if (m_zoomMode == QPdfView::ZoomMode::FitToWidth) {
            pageSize = QSizeF(m_document->pagePointSize(page) * m_screenResolution).toSize();
            pageScale = (qreal(m_viewport.width() - m_documentMargins.left() - m_documentMargins.right()) /
                         qreal(pageSize.width()));
            pageSize *= pageScale;
        } else if (m_zoomMode == QPdfView::ZoomMode::FitInView) {
            const QSize viewportSize(m_viewport.size() +
                                     QSize(-m_documentMargins.left() - m_documentMargins.right(), -m_pageSpacing));

            pageSize = QSizeF(m_document->pagePointSize(page) * m_screenResolution).toSize();
            QSize scaledSize = pageSize.scaled(viewportSize, Qt::KeepAspectRatio);
            // because of KeepAspectRatio, the ratio of widths should be the same as the ratio of heights
            pageScale = qreal(scaledSize.width()) / qreal(pageSize.width());
            pageSize = scaledSize;
        }

        totalWidth = qMax(totalWidth, pageSize.width());

        pageGeometryAndScale[page] = {QRect(QPoint(0, 0), pageSize), pageScale};
    }

    totalWidth += m_documentMargins.left() + m_documentMargins.right();

    int pageY = m_documentMargins.top();

    // calculate page positions
    for (int page = startPage; page < endPage; ++page) {
        const QSize pageSize = pageGeometryAndScale[page].first.size();

        // center horizontal inside the viewport
        const int pageX = (qMax(totalWidth, m_viewport.width()) - pageSize.width()) / 2;

        pageGeometryAndScale[page].first.moveTopLeft(QPoint(pageX, pageY));

        pageY += pageSize.height() + m_pageSpacing;
    }

    pageY += m_documentMargins.bottom();

    documentLayout.pageGeometryAndScale = pageGeometryAndScale;

    // calculate overall document size
    documentLayout.documentSize = QSize(totalWidth, pageY);

    return documentLayout;
}

//  from ../qtwebengine/src/pdfwidgets/qpdfview.cpp, line 347, as _ZN15QPdfViewPrivate20updateDocumentLayoutEv
inline void QPdfViewPrivate::updateDocumentLayout()
{
    m_documentLayout = calculateDocumentLayout();

    updateScrollBars();
}
//  -----------------------------------------------------------------------

//  QPdfView *QPdfViewPrivate::q_func()
extern "C" Q_DECL_EXPORT
QPdfView *ritual_ZN15QPdfViewPrivate6q_funcEv(QPdfViewPrivate *self) {
  return self->q_func();
}

//  const QPdfView *QPdfViewPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QPdfView *ritual_ZNK15QPdfViewPrivate6q_funcEv(
    const QPdfViewPrivate *self) {
  return self->q_func();
}

//  QPdfViewPrivate::QPdfViewPrivate(QPdfView *q)
extern "C" Q_DECL_EXPORT
QPdfViewPrivate *ritual_ZN15QPdfViewPrivateC1EP8QPdfView(QPdfView *q) {
  return new QPdfViewPrivate(q);
}

//  void QPdfViewPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPdfViewPrivate4initEv(QPdfViewPrivate *self) {
  self->init();
}

//  void QPdfViewPrivate::documentStatusChanged(QPdfDocument::Status status)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPdfViewPrivate21documentStatusChangedEN12QPdfDocument6StatusE(
    QPdfViewPrivate *self,
    QPdfDocument::Status status) {
  self->documentStatusChanged(status);
}

//  void QPdfViewPrivate::currentPageChanged(int currentPage)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPdfViewPrivate18currentPageChangedEi(
    QPdfViewPrivate *self,
    int currentPage) {
  self->currentPageChanged(currentPage);
}

//  void QPdfViewPrivate::currentZoomChanged(qreal currentZoom)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPdfViewPrivate18currentZoomChangedEd(
    QPdfViewPrivate *self,
    qreal currentZoom) {
  self->currentZoomChanged(currentZoom);
}

//  void QPdfViewPrivate::calculateViewport()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPdfViewPrivate17calculateViewportEv(QPdfViewPrivate *self) {
  self->calculateViewport();
}

//  void QPdfViewPrivate::setViewport(QRect viewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPdfViewPrivate11setViewportE5QRect(
    QPdfViewPrivate *self,
    const QRect *viewport) {
  self->setViewport(*viewport);
}

//  void QPdfViewPrivate::updateScrollBars()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPdfViewPrivate16updateScrollBarsEv(QPdfViewPrivate *self) {
  self->updateScrollBars();
}

//  void QPdfViewPrivate::pageRendered(int pageNumber, QSize imageSize, const
//      QImage &image, quint64 requestId)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPdfViewPrivate12pageRenderedEi5QSizeRK6QImagey(
    QPdfViewPrivate *self,
    int pageNumber,
    const QSize *imageSize,
    const QImage *image,
    quint64 requestId) {
  self->pageRendered(pageNumber, *imageSize, *image, requestId);
}

//  void QPdfViewPrivate::invalidateDocumentLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPdfViewPrivate24invalidateDocumentLayoutEv(
    QPdfViewPrivate *self) {
  self->invalidateDocumentLayout();
}

//  void QPdfViewPrivate::invalidatePageCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPdfViewPrivate19invalidatePageCacheEv(
    QPdfViewPrivate *self) {
  self->invalidatePageCache();
}

//  qreal QPdfViewPrivate::yPositionForPage(int page) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QPdfViewPrivate16yPositionForPageEi(
    const QPdfViewPrivate *self,
    int page) {
  return self->yPositionForPage(page);
}

//  QPdfLink QPdfViewPrivate::pagePosition(const QPointF &viewPosition)
extern "C" Q_DECL_EXPORT
QPdfLink *ritual_ZN15QPdfViewPrivate12pagePositionERK7QPointF(
    QPdfViewPrivate *self,
    const QPointF *viewPosition) {
  return new QPdfLink(self->pagePosition(*viewPosition));
}

//  QTransform QPdfViewPrivate::screenScaleTransform(int page) const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK15QPdfViewPrivate20screenScaleTransformEi(
    const QPdfViewPrivate *self,
    int page) {
  return new QTransform(self->screenScaleTransform(page));
}

//  DocumentLayout QPdfViewPrivate::calculateDocumentLayout() const
extern "C" Q_DECL_EXPORT
QPdfViewPrivate::DocumentLayout *ritual_ZNK15QPdfViewPrivate23calculateDocumentLayoutEv(
    const QPdfViewPrivate *self) {
  return new QPdfViewPrivate::DocumentLayout(
      self->calculateDocumentLayout());
}

//  void QPdfViewPrivate::updateDocumentLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPdfViewPrivate20updateDocumentLayoutEv(
    QPdfViewPrivate *self) {
  self->updateDocumentLayout();
}
