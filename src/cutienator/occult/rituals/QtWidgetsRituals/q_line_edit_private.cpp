//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qlineedit_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(lineedit)
#if QT_CONFIG(lineedit)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qlineedit.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qlineedit_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qlineedit.h>
#include <QtWidgets/private/qlineedit_p.h>
#include <QtCore/qvariant.h>
#if QT_CONFIG(itemviews)
#include <QtWidgets/qabstractitemview.h>
#endif
#if QT_CONFIG(draganddrop)
#include <QtGui/qdrag.h>
#endif
#if QT_CONFIG(action)
#  include <QtWidgets/qwidgetaction.h>
#endif
#include <QtGui/qclipboard.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
#ifndef QT_NO_IM
#include <QtGui/qinputmethod.h>
#include <QtCore/qlist.h>
#endif
#include <QtGui/qpainter.h>
#if QT_CONFIG(animation)
#include <QtCore/qpropertyanimation.h>
#endif
#include <QtGui/qstylehints.h>
#include <QtGui/qvalidator.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qlineedit_p.cpp, line 380, as _ZN19QLineEditIconButton10setOpacityEd
#if QT_CONFIG(toolbutton)
inline void QLineEditIconButton::setOpacity(qreal value)
{
    if (!qFuzzyCompare(m_opacity, value)) {
        m_opacity = value;
        updateCursor();
        update();
    }
}
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 395, as _ZN19QLineEditIconButton15setHideWithTextEb
#if QT_CONFIG(toolbutton)
#if QT_CONFIG(animation)
inline void QLineEditIconButton::setHideWithText(bool hide)
{
    m_hideWithText = hide;
}
#endif  // QT_CONFIG(animation)
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 334, as _ZN19QLineEditIconButtonC1EP7QWidget
#if QT_CONFIG(toolbutton)
inline QLineEditIconButton::QLineEditIconButton(QWidget *parent)
    : QToolButton(parent)
    , m_opacity(0)
{
    setFocusPolicy(Qt::NoFocus);
}
#endif  // QT_CONFIG(toolbutton)

//  from src/widgets/widgets/qlineedit_p.cpp, line 551, as _ZNK16QLineEditPrivate14findSideWidgetEPK7QAction
#if QT_CONFIG(action)
inline QLineEditPrivate::SideWidgetLocation QLineEditPrivate::findSideWidget(const QAction *a) const
{
    int i = 0;
    for (const auto &e : leadingSideWidgets) {
        if (a == e.action)
            return {QLineEdit::LeadingPosition, i};
        ++i;
    }
    i = 0;
    for (const auto &e : trailingSideWidgets) {
        if (a == e.action)
            return {QLineEdit::TrailingPosition, i};
        ++i;
    }
    return {QLineEdit::LeadingPosition, -1};
}
#endif  // QT_CONFIG(action)

//  from src/widgets/widgets/qlineedit_p.cpp, line 235, as _ZN16QLineEditPrivate19initMouseYThresholdEv
inline void QLineEditPrivate::initMouseYThreshold()
{
    mouseYThreshold = QGuiApplication::styleHints()->mouseQuickSelectionThreshold();
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 262, as _ZN16QLineEditPrivate7setTextERK7QString
inline void QLineEditPrivate::setText(const QString& text)
{
    edited = true;
    control->setText(text);
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 54, as _ZNK16QLineEditPrivate16textBeforeCursorEi
inline QString QLineEditPrivate::textBeforeCursor(int curPos) const
{
    const QString &text = control->text();
    return text.mid(0, curPos);
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 60, as _ZNK16QLineEditPrivate15textAfterCursorEi
inline QString QLineEditPrivate::textAfterCursor(int curPos) const
{
    const QString &text = control->text();
    return text.mid(curPos);
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 268, as _ZN16QLineEditPrivate25updatePasswordEchoEditingEb
inline void QLineEditPrivate::updatePasswordEchoEditing(bool editing)
{
    Q_Q(QLineEdit);
    control->updatePasswordEchoEditing(editing);
    q->setAttribute(Qt::WA_InputMethodEnabled, shouldEnableInputMethod());
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 275, as _ZN16QLineEditPrivate16resetInputMethodEv
inline void QLineEditPrivate::resetInputMethod()
{
    Q_Q(QLineEdit);
    if (q->hasFocus() && qApp) {
        QGuiApplication::inputMethod()->reset();
    }
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 117, as _ZN16QLineEditPrivate20handleWindowActivateEv
inline void QLineEditPrivate::handleWindowActivate()
{
    Q_Q(QLineEdit);
    if (!q->hasFocus() && control->hasSelectedText())
        control->deselect();
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 124, as _ZN16QLineEditPrivate10textEditedERK7QString
inline void QLineEditPrivate::textEdited(const QString &text)
{
    Q_Q(QLineEdit);
    edited = true;
    emit q->textEdited(text);
#if QT_CONFIG(completer)
    if (control->completer()
        && control->completer()->completionMode() != QCompleter::InlineCompletion)
        control->complete(-1); // update the popup on cut/paste/del
#endif
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 136, as _ZN16QLineEditPrivate21cursorPositionChangedEii
inline void QLineEditPrivate::cursorPositionChanged(int from, int to)
{
    Q_Q(QLineEdit);
    q->update();
    emit q->cursorPositionChanged(from, to);
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 318, as _ZN16QLineEditPrivate4dragEv
#if QT_CONFIG(draganddrop)
inline void QLineEditPrivate::drag()
{
    Q_Q(QLineEdit);
    dndTimer.stop();
    QMimeData *data = new QMimeData;
    data->setText(control->selectedText());
    QDrag *drag = new QDrag(q);
    drag->setMimeData(data);
    Qt::DropAction action = drag->exec(Qt::CopyAction);
    if (action == Qt::MoveAction && !control->isReadOnly() && drag->target() != q)
        control->removeSelection();
}
#endif  // QT_CONFIG(draganddrop)

//  from src/widgets/widgets/qlineedit_p.cpp, line 471, as _ZN16QLineEditPrivate18clearButtonClickedEv
inline void QLineEditPrivate::clearButtonClicked()
{
    Q_Q(QLineEdit);
    if (!q->text().isEmpty()) {
        q->clear();
        textEdited(QString());
    }
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 480, as _ZN16QLineEditPrivate22controlEditingFinishedEv
inline void QLineEditPrivate::controlEditingFinished()
{
    Q_Q(QLineEdit);
    edited = false;
    emit q->returnPressed();
    emit q->editingFinished();
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 488, as _ZNK16QLineEditPrivate20sideWidgetParametersEv
inline QLineEditPrivate::SideWidgetParameters QLineEditPrivate::sideWidgetParameters() const
{
    Q_Q(const QLineEdit);
    SideWidgetParameters result;
    result.iconSize = q->style()->pixelMetric(QStyle::PM_LineEditIconSize, nullptr, q);
    result.margin = q->style()->pixelMetric(QStyle::PM_LineEditIconMargin, nullptr, q);
    result.widgetWidth = result.iconSize + 6;
    result.widgetHeight = result.iconSize + 2;
    return result;
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 499, as _ZNK16QLineEditPrivate15clearButtonIconEv
inline QIcon QLineEditPrivate::clearButtonIcon() const
{
    Q_Q(const QLineEdit);
    QStyleOptionFrame styleOption;
    q->initStyleOption(&styleOption);
    return q->style()->standardIcon(QStyle::SP_LineEditClearButton, &styleOption, q);
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 507, as _ZN16QLineEditPrivate21setClearButtonEnabledEb
inline void QLineEditPrivate::setClearButtonEnabled(bool enabled)
{
#if QT_CONFIG(action)
    for (const SideWidgetEntry &e : trailingSideWidgets) {
        if (e.flags & SideWidgetClearButton) {
            e.action->setEnabled(enabled);
            break;
        }
    }
#else
    Q_UNUSED(enabled);
#endif
}

//  from src/widgets/widgets/qlineedit_p.cpp, line 521, as _ZN16QLineEditPrivate19positionSideWidgetsEv
inline void QLineEditPrivate::positionSideWidgets()
{
    Q_Q(QLineEdit);
    if (hasSideWidgets()) {
        const QRect contentRect = q->rect();
        const SideWidgetParameters p = sideWidgetParameters();
        const int delta = p.margin + p.widgetWidth;
        QRect widgetGeometry(QPoint(p.margin, (contentRect.height() - p.widgetHeight) / 2),
                             QSize(p.widgetWidth, p.widgetHeight));
        for (const SideWidgetEntry &e : leftSideWidgetList()) {
            e.widget->setGeometry(widgetGeometry);
#if QT_CONFIG(action)
            if (e.action->isVisible())
                widgetGeometry.moveLeft(widgetGeometry.left() + delta);
#else
            Q_UNUSED(delta);
#endif
        }
        widgetGeometry.moveLeft(contentRect.width() - p.widgetWidth - p.margin);
        for (const SideWidgetEntry &e : rightSideWidgetList()) {
            e.widget->setGeometry(widgetGeometry);
#if QT_CONFIG(action)
            if (e.action->isVisible())
                widgetGeometry.moveLeft(widgetGeometry.left() - delta);
#endif
        }
    }
}
//  -----------------------------------------------------------------------

//  A QLineEditPrivate that Python can take functions over in. Every QLineEditPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQLineEditPrivateCall0)(const void *, bool, int *);
typedef void (*CuteQLineEditPrivateCall1)(const void *, int, int *);
typedef void (*CuteQLineEditPrivateCall2)(const void *, int *);
typedef void (*CuteQLineEditPrivateCall3)(const void *, int *);
typedef void * (*CuteQLineEditPrivateCall4)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQLineEditPrivateCall5)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQLineEditPrivateCall6)(const void *, int *);
typedef int (*CuteQLineEditPrivateCall7)(const void *, int *);
typedef const QImage * (*CuteQLineEditPrivateCall8)(const void *, int *);
typedef void (*CuteQLineEditPrivateCall9)(const void *, int *);
typedef void (*CuteQLineEditPrivateCall10)(const void *, int *);
typedef void (*CuteQLineEditPrivateCall11)(const void *, int *);
typedef void (*CuteQLineEditPrivateCall12)(const void *, int *);
typedef void (*CuteQLineEditPrivateCall13)(const void *, int *);
typedef void (*CuteQLineEditPrivateCall14)(const void *, int *);
typedef void (*CuteQLineEditPrivateCall15)(const void *, int *);
typedef bool (*CuteQLineEditPrivateCall16)(const void *, int *);
typedef bool (*CuteQLineEditPrivateCall17)(const void *, int *);
class CuteQLineEditPrivate : public QLineEditPrivate {
public:
  using QLineEditPrivate::QLineEditPrivate;
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
      CuteQLineEditPrivateCall0 call = reinterpret_cast<CuteQLineEditPrivateCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLineEditPrivateCall1 call = reinterpret_cast<CuteQLineEditPrivateCall1>(taken[1]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[2]) {
      int handled = 0;
      CuteQLineEditPrivateCall2 call = reinterpret_cast<CuteQLineEditPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[3]) {
      int handled = 0;
      CuteQLineEditPrivateCall3 call = reinterpret_cast<CuteQLineEditPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[4]) {
      int handled = 0;
      CuteQLineEditPrivateCall4 call = reinterpret_cast<CuteQLineEditPrivateCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQLineEditPrivateCall5 call = reinterpret_cast<CuteQLineEditPrivateCall5>(taken[5]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQLineEditPrivateCall6 call = reinterpret_cast<CuteQLineEditPrivateCall6>(taken[6]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[7]) {
      int handled = 0;
      CuteQLineEditPrivateCall7 call = reinterpret_cast<CuteQLineEditPrivateCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[8]) {
      int handled = 0;
      CuteQLineEditPrivateCall8 call = reinterpret_cast<CuteQLineEditPrivateCall8>(taken[8]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[9]) {
      int handled = 0;
      CuteQLineEditPrivateCall9 call = reinterpret_cast<CuteQLineEditPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[10]) {
      int handled = 0;
      CuteQLineEditPrivateCall10 call = reinterpret_cast<CuteQLineEditPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[11]) {
      int handled = 0;
      CuteQLineEditPrivateCall11 call = reinterpret_cast<CuteQLineEditPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[12]) {
      int handled = 0;
      CuteQLineEditPrivateCall12 call = reinterpret_cast<CuteQLineEditPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[13]) {
      int handled = 0;
      CuteQLineEditPrivateCall13 call = reinterpret_cast<CuteQLineEditPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[14]) {
      int handled = 0;
      CuteQLineEditPrivateCall14 call = reinterpret_cast<CuteQLineEditPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[15]) {
      int handled = 0;
      CuteQLineEditPrivateCall15 call = reinterpret_cast<CuteQLineEditPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[16]) {
      int handled = 0;
      CuteQLineEditPrivateCall16 call = reinterpret_cast<CuteQLineEditPrivateCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[17]) {
      int handled = 0;
      CuteQLineEditPrivateCall17 call = reinterpret_cast<CuteQLineEditPrivateCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QLineEdit *QLineEditPrivate::q_func()
extern "C" Q_DECL_EXPORT
QLineEdit *ritual_ZN16QLineEditPrivate6q_funcEv(QLineEditPrivate *self) {
  return self->q_func();
}

//  const QLineEdit *QLineEditPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QLineEdit *ritual_ZNK16QLineEditPrivate6q_funcEv(
    const QLineEditPrivate *self) {
  return self->q_func();
}

//  QLineEditPrivate::QLineEditPrivate()
extern "C" Q_DECL_EXPORT
QLineEditPrivate *ritual_ZN16QLineEditPrivateC1Ev() {
  return new CuteQLineEditPrivate();
}

//  QLineEditPrivate::~QLineEditPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivateD1Ev(QLineEditPrivate *self) {
  delete self;
}

//  void QLineEditPrivate::initMouseYThreshold()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate19initMouseYThresholdEv(
    QLineEditPrivate *self) {
  self->initMouseYThreshold();
}

//  void QLineEditPrivate::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate7setTextERK7QString(
    QLineEditPrivate *self,
    const QString *text) {
  self->setText(*text);
}

//  QString QLineEditPrivate::textBeforeCursor(int curPos) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QLineEditPrivate16textBeforeCursorEi(
    const QLineEditPrivate *self,
    int curPos) {
  return new QString(self->textBeforeCursor(curPos));
}

//  QString QLineEditPrivate::textAfterCursor(int curPos) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QLineEditPrivate15textAfterCursorEi(
    const QLineEditPrivate *self,
    int curPos) {
  return new QString(self->textAfterCursor(curPos));
}

//  void QLineEditPrivate::updatePasswordEchoEditing(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate25updatePasswordEchoEditingEb(
    QLineEditPrivate *self,
    bool a0) {
  self->updatePasswordEchoEditing(a0);
}

//  void QLineEditPrivate::resetInputMethod()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate16resetInputMethodEv(
    QLineEditPrivate *self) {
  self->resetInputMethod();
}

//  bool QLineEditPrivate::shouldEnableInputMethod() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QLineEditPrivate23shouldEnableInputMethodEv(
    const QLineEditPrivate *self) {
  return self->shouldEnableInputMethod();
}

//  bool QLineEditPrivate::shouldShowPlaceholderText() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QLineEditPrivate25shouldShowPlaceholderTextEv(
    const QLineEditPrivate *self) {
  return self->shouldShowPlaceholderText();
}

//  QLineEditPrivate *QLineEditPrivate::get(QLineEdit *lineEdit)
extern "C" Q_DECL_EXPORT
QLineEditPrivate *ritual_ZN16QLineEditPrivate3getEP9QLineEdit(
    QLineEdit *lineEdit) {
  return QLineEditPrivate::get(lineEdit);
}

//  void QLineEditPrivate::handleWindowActivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate20handleWindowActivateEv(
    QLineEditPrivate *self) {
  self->handleWindowActivate();
}

//  void QLineEditPrivate::textEdited(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate10textEditedERK7QString(
    QLineEditPrivate *self,
    const QString *a0) {
  self->textEdited(*a0);
}

//  void QLineEditPrivate::cursorPositionChanged(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate21cursorPositionChangedEii(
    QLineEditPrivate *self,
    int a0,
    int a1) {
  self->cursorPositionChanged(a0, a1);
}

#if QT_CONFIG(draganddrop)
//  void QLineEditPrivate::drag()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate4dragEv(QLineEditPrivate *self) {
  self->drag();
}
#endif  // QT_CONFIG(draganddrop)

//  void QLineEditPrivate::clearButtonClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate18clearButtonClickedEv(
    QLineEditPrivate *self) {
  self->clearButtonClicked();
}

//  void QLineEditPrivate::controlEditingFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate22controlEditingFinishedEv(
    QLineEditPrivate *self) {
  self->controlEditingFinished();
}

//  SideWidgetParameters QLineEditPrivate::sideWidgetParameters() const
extern "C" Q_DECL_EXPORT
QLineEditPrivate::SideWidgetParameters *ritual_ZNK16QLineEditPrivate20sideWidgetParametersEv(
    const QLineEditPrivate *self) {
  return new QLineEditPrivate::SideWidgetParameters(
      self->sideWidgetParameters());
}

//  QIcon QLineEditPrivate::clearButtonIcon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK16QLineEditPrivate15clearButtonIconEv(
    const QLineEditPrivate *self) {
  return new QIcon(self->clearButtonIcon());
}

//  void QLineEditPrivate::setClearButtonEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate21setClearButtonEnabledEb(
    QLineEditPrivate *self,
    bool enabled) {
  self->setClearButtonEnabled(enabled);
}

//  void QLineEditPrivate::positionSideWidgets()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLineEditPrivate19positionSideWidgetsEv(
    QLineEditPrivate *self) {
  self->positionSideWidgets();
}

//  bool QLineEditPrivate::hasSideWidgets() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QLineEditPrivate14hasSideWidgetsEv(
    const QLineEditPrivate *self) {
  return self->hasSideWidgets();
}

//  a Python function taken by a CuteQLineEditPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLineEditPrivate(
    QLineEditPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLineEditPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(lineedit)
