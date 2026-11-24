//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qplaintextedit_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(textedit)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qplaintextedit.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qplaintextedit_p.h>
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
#include "qabstractscrollarea.h"
#if QT_CONFIG(scrollarea)
#include "qscrollbar.h"
#include "qapplication.h"
#include "qstyle.h"
#include "qstyleoption.h"
#include "qevent.h"
#include "qdebug.h"
#include "qboxlayout.h"
#include "qpainter.h"
#include "qmargins.h"
#if QT_CONFIG(itemviews)
#include "qheaderview.h"
#endif
#include <QDebug>
#include "qabstractscrollarea_p.h"
#include "qscrollbar_p.h"
#include <qwidget.h>
#include <private/qguiapplication_p.h>
#include <qpa/qplatformtheme.h>
#include <private/qapplication_p.h>
#ifdef Q_OS_WIN
#  include <qt_windows.h>
#endif
#endif
#include "qplaintextedit_p.h"
#include <qfont.h>
#include <qpainter.h>
#include <qevent.h>
#include <qdebug.h>
#if QT_CONFIG(draganddrop)
#include <qdrag.h>
#endif
#include <qclipboard.h>
#include <qmath.h>
#if QT_CONFIG(menu)
#include <qmenu.h>
#endif
#include <qstyle.h>
#include "private/qapplication_p.h"
#include "private/qtextdocumentlayout_p.h"
#include "private/qabstracttextdocumentlayout_p.h"
#include "qtextdocument.h"
#include "private/qtextdocument_p.h"
#include "qtextlist.h"
#include "qaccessible.h"
#include <qtextformat.h>
#include <qdatetime.h>
#include <qapplication.h>
#include <limits.h>
#include <qtexttable.h>
#include <qvariant.h>
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

//  from src/widgets/widgets/qplaintextedit.cpp, line 414, as _ZN21QPlainTextEditControlC1EP14QPlainTextEdit
inline QPlainTextEditControl::QPlainTextEditControl(QPlainTextEdit *parent)
    : QWidgetTextControl(parent), textEdit(parent),
      topBlock(0)
{
    setAcceptRichText(false);
}

//  from src/widgets/widgets/qplaintextedit.cpp, line 800, as _ZN21QPlainTextEditPrivate27updatePlaceholderVisibilityEv
inline void QPlainTextEditPrivate::updatePlaceholderVisibility()
{
    // We normally only repaint the part of view that contains text in the
    // document that has changed (in repaintContents). But the placeholder
    // text is not a part of the document, but is drawn on separately. So whenever
    // we either show or hide the placeholder text, we issue a full update.
    if (placeholderTextShown != placeHolderTextToBeShown()) {
        viewport->update();
        placeholderTextShown = placeHolderTextToBeShown();
    }
}

//  from src/widgets/widgets/qplaintextedit.cpp, line 1018, as _ZN21QPlainTextEditPrivate22ensureViewportLayoutedEv
inline void QPlainTextEditPrivate::ensureViewportLayouted()
{
}

//  from src/widgets/widgets/qplaintextedit.cpp, line 467, as _ZNK21QPlainTextEditPrivate14verticalOffsetEii
inline qreal QPlainTextEditPrivate::verticalOffset(int topBlock, int topLine) const
{
    qreal offset = 0;
    QTextDocument *doc = control->document();

    if (topLine) {
        QTextBlock currentBlock = doc->findBlockByNumber(topBlock);
        QPlainTextDocumentLayout *documentLayout = qobject_cast<QPlainTextDocumentLayout*>(doc->documentLayout());
        Q_ASSERT(documentLayout);
        QRectF r = documentLayout->blockBoundingRect(currentBlock);
        Q_UNUSED(r);
        QTextLayout *layout = currentBlock.layout();
        if (layout && topLine <= layout->lineCount()) {
            QTextLine line = layout->lineAt(topLine - 1);
            const QRectF lr = line.naturalTextRect();
            offset = lr.bottom();
        }
    }
    if (topBlock == 0 && topLine == 0)
        offset -= doc->documentMargin(); // top margin
    return offset;
}

//  from src/widgets/widgets/qplaintextedit.cpp, line 1903, as _ZN21QPlainTextEditPrivate23updateDefaultTextOptionEv
inline void QPlainTextEditPrivate::updateDefaultTextOption()
{
    QTextDocument *doc = control->document();

    QTextOption opt = doc->defaultTextOption();
    QTextOption::WrapMode oldWrapMode = opt.wrapMode();

    if (lineWrap == QPlainTextEdit::NoWrap)
        opt.setWrapMode(QTextOption::NoWrap);
    else
        opt.setWrapMode(wordWrap);

    if (opt.wrapMode() != oldWrapMode)
        doc->setDefaultTextOption(opt);
}

//  from src/widgets/widgets/qplaintextedit.cpp, line 720, as _ZN21QPlainTextEditPrivate14updateViewportEv
inline void QPlainTextEditPrivate::updateViewport()
{
    Q_Q(QPlainTextEdit);
    viewport->update();
    emit q->updateRequest(viewport->rect(), 0);
}

//  from src/widgets/widgets/qplaintextedit.cpp, line 421, as _ZN21QPlainTextEditPrivate21cursorPositionChangedEv
inline void QPlainTextEditPrivate::cursorPositionChanged()
{
    pageUpDownLastCursorYIsValid = false;
    Q_Q(QPlainTextEdit);
#if QT_CONFIG(accessibility)
    QAccessibleTextCursorEvent ev(q, q->textCursor().position());
    QAccessible::updateAccessibility(&ev);
#endif
    emit q->cursorPositionChanged();
}
//  -----------------------------------------------------------------------

//  A QPlainTextEditPrivate that Python can take functions over in. Every QPlainTextEditPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(scrollarea)
typedef void (*CuteQPlainTextEditPrivateCall0)(const void *, int, int, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef bool (*CuteQPlainTextEditPrivateCall1)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef const QPoint * (*CuteQPlainTextEditPrivateCall2)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
typedef void (*CuteQPlainTextEditPrivateCall3)(const void *, bool, int *);
typedef void (*CuteQPlainTextEditPrivateCall4)(const void *, int, int *);
typedef void (*CuteQPlainTextEditPrivateCall5)(const void *, int *);
typedef void (*CuteQPlainTextEditPrivateCall6)(const void *, int *);
typedef void * (*CuteQPlainTextEditPrivateCall7)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQPlainTextEditPrivateCall8)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQPlainTextEditPrivateCall9)(const void *, int *);
typedef int (*CuteQPlainTextEditPrivateCall10)(const void *, int *);
typedef const QImage * (*CuteQPlainTextEditPrivateCall11)(const void *, int *);
typedef void (*CuteQPlainTextEditPrivateCall12)(const void *, int *);
typedef void (*CuteQPlainTextEditPrivateCall13)(const void *, int *);
typedef void (*CuteQPlainTextEditPrivateCall14)(const void *, int *);
typedef void (*CuteQPlainTextEditPrivateCall15)(const void *, int *);
typedef void (*CuteQPlainTextEditPrivateCall16)(const void *, int *);
typedef void (*CuteQPlainTextEditPrivateCall17)(const void *, int *);
typedef void (*CuteQPlainTextEditPrivateCall18)(const void *, int *);
typedef bool (*CuteQPlainTextEditPrivateCall19)(const void *, int *);
typedef bool (*CuteQPlainTextEditPrivateCall20)(const void *, int *);
class CuteQPlainTextEditPrivate : public QPlainTextEditPrivate {
public:
  using QPlainTextEditPrivate::QPlainTextEditPrivate;
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
      CuteQPlainTextEditPrivateCall0 call = reinterpret_cast<CuteQPlainTextEditPrivateCall0>(taken[0]);
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
      CuteQPlainTextEditPrivateCall1 call = reinterpret_cast<CuteQPlainTextEditPrivateCall1>(taken[1]);
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
      CuteQPlainTextEditPrivateCall2 call = reinterpret_cast<CuteQPlainTextEditPrivateCall2>(taken[2]);
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
      CuteQPlainTextEditPrivateCall3 call = reinterpret_cast<CuteQPlainTextEditPrivateCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall4 call = reinterpret_cast<CuteQPlainTextEditPrivateCall4>(taken[4]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall5 call = reinterpret_cast<CuteQPlainTextEditPrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall6 call = reinterpret_cast<CuteQPlainTextEditPrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall7 call = reinterpret_cast<CuteQPlainTextEditPrivateCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall8 call = reinterpret_cast<CuteQPlainTextEditPrivateCall8>(taken[8]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall9 call = reinterpret_cast<CuteQPlainTextEditPrivateCall9>(taken[9]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall10 call = reinterpret_cast<CuteQPlainTextEditPrivateCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[11]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall11 call = reinterpret_cast<CuteQPlainTextEditPrivateCall11>(taken[11]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[12]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall12 call = reinterpret_cast<CuteQPlainTextEditPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[13]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall13 call = reinterpret_cast<CuteQPlainTextEditPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[14]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall14 call = reinterpret_cast<CuteQPlainTextEditPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[15]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall15 call = reinterpret_cast<CuteQPlainTextEditPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[16]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall16 call = reinterpret_cast<CuteQPlainTextEditPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[17]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall17 call = reinterpret_cast<CuteQPlainTextEditPrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[18]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall18 call = reinterpret_cast<CuteQPlainTextEditPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[19]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall19 call = reinterpret_cast<CuteQPlainTextEditPrivateCall19>(taken[19]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[20]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall20 call = reinterpret_cast<CuteQPlainTextEditPrivateCall20>(taken[20]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QPlainTextEdit *QPlainTextEditPrivate::q_func()
extern "C" Q_DECL_EXPORT
QPlainTextEdit *ritual_ZN21QPlainTextEditPrivate6q_funcEv(
    QPlainTextEditPrivate *self) {
  return self->q_func();
}

//  const QPlainTextEdit *QPlainTextEditPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QPlainTextEdit *ritual_ZNK21QPlainTextEditPrivate6q_funcEv(
    const QPlainTextEditPrivate *self) {
  return self->q_func();
}

//  void QPlainTextEditPrivate::updatePlaceholderVisibility()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlainTextEditPrivate27updatePlaceholderVisibilityEv(
    QPlainTextEditPrivate *self) {
  self->updatePlaceholderVisibility();
}

//  void QPlainTextEditPrivate::ensureViewportLayouted()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlainTextEditPrivate22ensureViewportLayoutedEv(
    QPlainTextEditPrivate *self) {
  self->ensureViewportLayouted();
}

//  int QPlainTextEditPrivate::horizontalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QPlainTextEditPrivate16horizontalOffsetEv(
    const QPlainTextEditPrivate *self) {
  return self->horizontalOffset();
}

//  qreal QPlainTextEditPrivate::verticalOffset(int topBlock, int topLine)
//      const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QPlainTextEditPrivate14verticalOffsetEii(
    const QPlainTextEditPrivate *self,
    int topBlock,
    int topLine) {
  return self->verticalOffset(topBlock, topLine);
}

//  void QPlainTextEditPrivate::updateDefaultTextOption()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlainTextEditPrivate23updateDefaultTextOptionEv(
    QPlainTextEditPrivate *self) {
  self->updateDefaultTextOption();
}

//  void QPlainTextEditPrivate::updateViewport()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlainTextEditPrivate14updateViewportEv(
    QPlainTextEditPrivate *self) {
  self->updateViewport();
}

//  void QPlainTextEditPrivate::cursorPositionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlainTextEditPrivate21cursorPositionChangedEv(
    QPlainTextEditPrivate *self) {
  self->cursorPositionChanged();
}

//  bool QPlainTextEditPrivate::placeHolderTextToBeShown() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QPlainTextEditPrivate24placeHolderTextToBeShownEv(
    const QPlainTextEditPrivate *self) {
  return self->placeHolderTextToBeShown();
}

//  a Python function taken by a CuteQPlainTextEditPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlainTextEditPrivate(
    QPlainTextEditPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlainTextEditPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(textedit)
