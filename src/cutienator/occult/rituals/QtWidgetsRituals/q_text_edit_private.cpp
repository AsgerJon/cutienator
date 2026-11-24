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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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
