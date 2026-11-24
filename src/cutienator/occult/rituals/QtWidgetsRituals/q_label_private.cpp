//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qlabel_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qlabel.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qlabel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qstring.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qframe.h"
#include "qbitmap.h"
#include "qdrawutil.h"
#include "qevent.h"
#include "qpainter.h"
#include "qstyle.h"
#include "qstyleoption.h"
#include "qstylepainter.h"
#include "qapplication.h"
#include "qframe_p.h"
#include "qpainter.h"
#include "qevent.h"
#include "qpixmapcache.h"
#include "qstyle.h"
#include "qstyleoption.h"
#include "qlabel_p.h"
#include "private/qhexstring_p.h"
#include <qmath.h>
#if QT_CONFIG(style_stylesheet)
#include "private/qstylesheetstyle_p.h"
#endif
#if QT_CONFIG(abstractbutton)
#include "qabstractbutton.h"
#endif
#if QT_CONFIG(accessibility)
#include <qaccessible.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from src/widgets/widgets/qlabel.cpp, line 44, as _ZN13QLabelPrivateD1Ev
inline QLabelPrivate::~QLabelPrivate()
{
}

//  from src/widgets/widgets/qlabel.cpp, line 202, as _ZN13QLabelPrivate4initEv
inline void QLabelPrivate::init()
{
    Q_Q(QLabel);

    q->setSizePolicy(QSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred,
                                 QSizePolicy::Label));
    setLayoutItemMargins(QStyle::SE_LabelLayoutItem);
}

//  from src/widgets/widgets/qlabel.cpp, line 1299, as _ZN13QLabelPrivate13clearContentsEv
inline void QLabelPrivate::clearContents()
{
    delete control;
    control = nullptr;
    isTextLabel = false;
    hasShortcut = false;

#ifndef QT_NO_PICTURE
    picture.reset();
#endif
    icon.reset();
    pixmapSize = QSize();

    text.clear();
    Q_Q(QLabel);
#ifndef QT_NO_SHORTCUT
    if (shortcutId)
        q->releaseShortcut(shortcutId);
    shortcutId = 0;
#endif
#if QT_CONFIG(movie)
    for (auto &conn : movieConnections)
        QObject::disconnect(conn);
    movie = nullptr;
#endif
#ifndef QT_NO_CURSOR
    if (onAnchor) {
        if (validCursor)
            q->setCursor(cursor);
        else
            q->unsetCursor();
    }
    validCursor = false;
    onAnchor = false;
#endif
}

//  from src/widgets/widgets/qlabel.cpp, line 1117, as _ZN13QLabelPrivate11updateLabelEv
inline void QLabelPrivate::updateLabel()
{
    Q_Q(QLabel);
    valid_hints = false;

    if (isTextLabel) {
        QSizePolicy policy = q->sizePolicy();
        const bool wrap = align & Qt::TextWordWrap;
        policy.setHeightForWidth(wrap);
        if (policy != q->sizePolicy())  // ### should be replaced by WA_WState_OwnSizePolicy idiom
            q->setSizePolicy(policy);
        textLayoutDirty = true;
    }
    q->updateGeometry();
    q->update(q->contentsRect());
}

//  from src/widgets/widgets/qlabel.cpp, line 1230, as _ZN13QLabelPrivate12movieUpdatedERK5QRect
#if QT_CONFIG(movie)
inline void QLabelPrivate::movieUpdated(const QRect &rect)
{
    Q_Q(QLabel);
    if (movie && movie->isValid()) {
        QRect r;
        if (scaledcontents) {
            QRect cr = q->contentsRect();
            QRect pixmapRect(cr.topLeft(), movie->currentPixmap().size());
            if (pixmapRect.isEmpty())
                return;
            r.setRect(cr.left(), cr.top(),
                      (rect.width() * cr.width()) / pixmapRect.width(),
                      (rect.height() * cr.height()) / pixmapRect.height());
        } else {
            r = q->style()->itemPixmapRect(q->contentsRect(), align, movie->currentPixmap());
            r.translate(rect.x(), rect.y());
            r.setWidth(qMin(r.width(), rect.width()));
            r.setHeight(qMin(r.height(), rect.height()));
        }
        q->update(r);
    }
}
#endif  // QT_CONFIG(movie)

//  from src/widgets/widgets/qlabel.cpp, line 1253, as _ZN13QLabelPrivate12movieResizedERK5QSize
#if QT_CONFIG(movie)
inline void QLabelPrivate::movieResized(const QSize &size)
{
    Q_Q(QLabel);
    q->update(); //we need to refresh the whole background in case the new size is smaller
    valid_hints = false;
    movieUpdated(QRect(QPoint(0,0), size));
    q->updateGeometry();
}
#endif  // QT_CONFIG(movie)

//  from src/widgets/widgets/qlabel.cpp, line 1204, as _ZN13QLabelPrivate14updateShortcutEv
#if !defined(QT_NO_SHORTCUT)
inline void QLabelPrivate::updateShortcut()
{
    Q_Q(QLabel);
    Q_ASSERT(shortcutId == 0);
    // Introduce an extra boolean to indicate the presence of a shortcut in the
    // text. We cannot use the shortcutId itself because on the mac mnemonics are
    // off by default, so QKeySequence::mnemonic always returns an empty sequence.
    // But then we do want to hide the ampersands, so we can't use shortcutId.
    hasShortcut = false;

    if (!text.contains(u'&'))
        return;
    hasShortcut = true;
    shortcutId = q->grabShortcut(QKeySequence::mnemonic(text));
}
#endif  // !defined(QT_NO_SHORTCUT)

//  from src/widgets/widgets/qlabel.cpp, line 1221, as _ZN13QLabelPrivate12buddyDeletedEv
#if !defined(QT_NO_SHORTCUT)
inline void QLabelPrivate::buddyDeleted()
{
    Q_Q(QLabel);
    q->setBuddy(nullptr);
}
#endif  // !defined(QT_NO_SHORTCUT)

//  from src/widgets/widgets/qlabel.cpp, line 1562, as _ZNK13QLabelPrivate17ensureTextControlEv
inline void QLabelPrivate::ensureTextControl() const
{
    Q_Q(const QLabel);
    if (!isTextLabel)
        return;
    if (!control) {
        control = new QWidgetTextControl(const_cast<QLabel *>(q));
        control->document()->setUndoRedoEnabled(false);
        control->document()->setDefaultFont(q->font());
        if (resourceProvider != nullptr)
            control->document()->setResourceProvider(resourceProvider);
        control->setTextInteractionFlags(textInteractionFlags);
        control->setOpenExternalLinks(openExternalLinks);
        control->setPalette(q->palette());
        control->setFocus(q->hasFocus());
        QObject::connect(control, &QWidgetTextControl::updateRequest,
                         q, qOverload<>(&QLabel::update));
        QObject::connect(control, &QWidgetTextControl::linkActivated,
                         q, &QLabel::linkActivated);
        QObjectPrivate::connect(control, &QWidgetTextControl::linkHovered,
                                this, &QLabelPrivate::linkHovered);
        textLayoutDirty = true;
        textDirty = true;
    }
}

//  from src/widgets/widgets/qlabel.cpp, line 1598, as _ZN13QLabelPrivate11linkHoveredERK7QString
inline void QLabelPrivate::linkHovered(const QString &anchor)
{
    Q_Q(QLabel);
#ifndef QT_NO_CURSOR
    if (anchor.isEmpty()) { // restore cursor
        if (validCursor)
            q->setCursor(cursor);
        else
            q->unsetCursor();
        onAnchor = false;
    } else if (!onAnchor) {
        validCursor = q->testAttribute(Qt::WA_SetCursor);
        if (validCursor) {
            cursor = q->cursor();
        }
        q->setCursor(Qt::PointingHandCursor);
        onAnchor = true;
    }
#endif
    emit q->linkHovered(anchor);
}

//  from src/widgets/widgets/qlabel.cpp, line 1468, as _ZNK13QLabelPrivate12documentRectEv
inline QRect QLabelPrivate::documentRect() const
{
    Q_Q(const QLabel);
    Q_ASSERT_X(isTextLabel, "documentRect", "document rect called for label that is not a text label!");
    QRect cr = q->contentsRect();
    cr.adjust(margin, margin, -margin, -margin);
    const int align = QStyle::visualAlignment(isTextLabel ? textDirection()
                                                          : q->layoutDirection(), QFlag(this->align));
    int m = indent;
    if (m < 0 && q->frameWidth()) // no indent, but we do have a frame
        m = q->fontMetrics().horizontalAdvance(u'x') / 2 - margin;
    if (m > 0) {
        if (align & Qt::AlignLeft)
            cr.setLeft(cr.left() + m);
        if (align & Qt::AlignRight)
            cr.setRight(cr.right() - m);
        if (align & Qt::AlignTop)
            cr.setTop(cr.top() + m);
        if (align & Qt::AlignBottom)
            cr.setBottom(cr.bottom() - m);
    }
    return cr;
}

//  from src/widgets/widgets/qlabel.cpp, line 1456, as _ZNK13QLabelPrivate13textDirectionEv
inline Qt::LayoutDirection QLabelPrivate::textDirection() const
{
    if (control) {
        QTextOption opt = control->document()->defaultTextOption();
        return opt.textDirection();
    }

    return text.isRightToLeft() ? Qt::RightToLeft : Qt::LeftToRight;
}
//  -----------------------------------------------------------------------

//  A QLabelPrivate that Python can take functions over in. Every QLabelPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQLabelPrivateCall0)(const void *, bool, int *);
typedef void (*CuteQLabelPrivateCall1)(const void *, int, int *);
typedef void (*CuteQLabelPrivateCall2)(const void *, int *);
typedef void (*CuteQLabelPrivateCall3)(const void *, int *);
typedef void * (*CuteQLabelPrivateCall4)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQLabelPrivateCall5)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQLabelPrivateCall6)(const void *, int *);
typedef int (*CuteQLabelPrivateCall7)(const void *, int *);
typedef const QImage * (*CuteQLabelPrivateCall8)(const void *, int *);
typedef void (*CuteQLabelPrivateCall9)(const void *, int *);
typedef void (*CuteQLabelPrivateCall10)(const void *, int *);
typedef void (*CuteQLabelPrivateCall11)(const void *, int *);
typedef void (*CuteQLabelPrivateCall12)(const void *, int *);
typedef void (*CuteQLabelPrivateCall13)(const void *, int *);
typedef void (*CuteQLabelPrivateCall14)(const void *, int *);
typedef void (*CuteQLabelPrivateCall15)(const void *, int *);
typedef bool (*CuteQLabelPrivateCall16)(const void *, int *);
typedef bool (*CuteQLabelPrivateCall17)(const void *, int *);
class CuteQLabelPrivate : public QLabelPrivate {
public:
  using QLabelPrivate::QLabelPrivate;
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
      CuteQLabelPrivateCall0 call = reinterpret_cast<CuteQLabelPrivateCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLabelPrivateCall1 call = reinterpret_cast<CuteQLabelPrivateCall1>(taken[1]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[2]) {
      int handled = 0;
      CuteQLabelPrivateCall2 call = reinterpret_cast<CuteQLabelPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[3]) {
      int handled = 0;
      CuteQLabelPrivateCall3 call = reinterpret_cast<CuteQLabelPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[4]) {
      int handled = 0;
      CuteQLabelPrivateCall4 call = reinterpret_cast<CuteQLabelPrivateCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQLabelPrivateCall5 call = reinterpret_cast<CuteQLabelPrivateCall5>(taken[5]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQLabelPrivateCall6 call = reinterpret_cast<CuteQLabelPrivateCall6>(taken[6]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[7]) {
      int handled = 0;
      CuteQLabelPrivateCall7 call = reinterpret_cast<CuteQLabelPrivateCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[8]) {
      int handled = 0;
      CuteQLabelPrivateCall8 call = reinterpret_cast<CuteQLabelPrivateCall8>(taken[8]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[9]) {
      int handled = 0;
      CuteQLabelPrivateCall9 call = reinterpret_cast<CuteQLabelPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[10]) {
      int handled = 0;
      CuteQLabelPrivateCall10 call = reinterpret_cast<CuteQLabelPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[11]) {
      int handled = 0;
      CuteQLabelPrivateCall11 call = reinterpret_cast<CuteQLabelPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[12]) {
      int handled = 0;
      CuteQLabelPrivateCall12 call = reinterpret_cast<CuteQLabelPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[13]) {
      int handled = 0;
      CuteQLabelPrivateCall13 call = reinterpret_cast<CuteQLabelPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[14]) {
      int handled = 0;
      CuteQLabelPrivateCall14 call = reinterpret_cast<CuteQLabelPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[15]) {
      int handled = 0;
      CuteQLabelPrivateCall15 call = reinterpret_cast<CuteQLabelPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[16]) {
      int handled = 0;
      CuteQLabelPrivateCall16 call = reinterpret_cast<CuteQLabelPrivateCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[17]) {
      int handled = 0;
      CuteQLabelPrivateCall17 call = reinterpret_cast<CuteQLabelPrivateCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QLabel *QLabelPrivate::q_func()
extern "C" Q_DECL_EXPORT
QLabel *ritual_ZN13QLabelPrivate6q_funcEv(QLabelPrivate *self) {
  return self->q_func();
}

//  const QLabel *QLabelPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QLabel *ritual_ZNK13QLabelPrivate6q_funcEv(const QLabelPrivate *self) {
  return self->q_func();
}

//  QLabelPrivate::~QLabelPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLabelPrivateD1Ev(QLabelPrivate *self) {
  delete self;
}

//  void QLabelPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLabelPrivate4initEv(QLabelPrivate *self) {
  self->init();
}

//  void QLabelPrivate::clearContents()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLabelPrivate13clearContentsEv(QLabelPrivate *self) {
  self->clearContents();
}

//  void QLabelPrivate::updateLabel()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLabelPrivate11updateLabelEv(QLabelPrivate *self) {
  self->updateLabel();
}

#if QT_CONFIG(movie)
//  void QLabelPrivate::movieUpdated(const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLabelPrivate12movieUpdatedERK5QRect(
    QLabelPrivate *self,
    const QRect *rect) {
  self->movieUpdated(*rect);
}
#endif  // QT_CONFIG(movie)

#if QT_CONFIG(movie)
//  void QLabelPrivate::movieResized(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLabelPrivate12movieResizedERK5QSize(
    QLabelPrivate *self,
    const QSize *size) {
  self->movieResized(*size);
}
#endif  // QT_CONFIG(movie)

#if !defined(QT_NO_SHORTCUT)
//  void QLabelPrivate::updateShortcut()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLabelPrivate14updateShortcutEv(QLabelPrivate *self) {
  self->updateShortcut();
}
#endif  // !defined(QT_NO_SHORTCUT)

#if !defined(QT_NO_SHORTCUT)
//  void QLabelPrivate::buddyDeleted()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLabelPrivate12buddyDeletedEv(QLabelPrivate *self) {
  self->buddyDeleted();
}
#endif  // !defined(QT_NO_SHORTCUT)

//  bool QLabelPrivate::needTextControl() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QLabelPrivate15needTextControlEv(
    const QLabelPrivate *self) {
  return self->needTextControl();
}

//  void QLabelPrivate::ensureTextControl() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QLabelPrivate17ensureTextControlEv(
    const QLabelPrivate *self) {
  self->ensureTextControl();
}

//  void QLabelPrivate::linkHovered(const QString &link)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QLabelPrivate11linkHoveredERK7QString(
    QLabelPrivate *self,
    const QString *link) {
  self->linkHovered(*link);
}

//  QRect QLabelPrivate::documentRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK13QLabelPrivate12documentRectEv(const QLabelPrivate *self) {
  return new QRect(self->documentRect());
}

//  Qt::LayoutDirection QLabelPrivate::textDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK13QLabelPrivate13textDirectionEv(
    const QLabelPrivate *self) {
  return self->textDirection();
}

//  a Python function taken by a CuteQLabelPrivate, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLabelPrivate(
    QLabelPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLabelPrivate *>(self)->take(key, call);
}
