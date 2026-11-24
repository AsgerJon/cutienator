//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qkeysequenceedit_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(keysequenceedit)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qkeysequenceedit.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qkeysequenceedit_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qkeysequenceedit.h"
#include "qkeysequenceedit_p.h"
#include "qboxlayout.h"
#include "qlineedit.h"
#include <private/qkeymapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qkeysequenceedit.cpp, line 19, as _ZN23QKeySequenceEditPrivate4initEv
inline void QKeySequenceEditPrivate::init()
{
    Q_Q(QKeySequenceEdit);

    lineEdit = new QLineEdit(q);
    lineEdit->setObjectName(QStringLiteral("qt_keysequenceedit_lineedit"));
    lineEdit->setClearButtonEnabled(false);
    q->connect(lineEdit, &QLineEdit::textChanged, q, [q](const QString& text) {
        // Clear the shortcut if the user clicked on the clear icon
        if (text.isEmpty())
            q->clear();
    });

    keyNum = 0;
    prevKey = -1;
    finishingKeyCombinations = {Qt::Key_Tab, Qt::Key_Backtab};

    QVBoxLayout *layout = new QVBoxLayout(q);
    layout->setContentsMargins(0, 0, 0, 0);
    layout->addWidget(lineEdit);

    std::fill_n(key, QKeySequencePrivate::MaxKeyCount, QKeyCombination::fromCombined(0));

    lineEdit->setFocusProxy(q);
    lineEdit->installEventFilter(q);
    resetState();

    q->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Fixed);
    q->setFocusPolicy(Qt::StrongFocus);
    q->setAttribute(Qt::WA_MacShowFocusRect, true);
    q->setAttribute(Qt::WA_InputMethodEnabled, false);
}

//  from src/widgets/widgets/qkeysequenceedit.cpp, line 52, as _ZN23QKeySequenceEditPrivate18translateModifiersE6QFlagsIN2Qt16KeyboardModifierEERK7QString
inline int QKeySequenceEditPrivate::translateModifiers(Qt::KeyboardModifiers state, const QString &text)
{
    Q_UNUSED(text);
    int result = 0;
    if (state & Qt::ControlModifier)
        result |= Qt::CTRL;
    if (state & Qt::MetaModifier)
        result |= Qt::META;
    if (state & Qt::AltModifier)
        result |= Qt::ALT;
    return result;
}

//  from src/widgets/widgets/qkeysequenceedit.cpp, line 65, as _ZN23QKeySequenceEditPrivate10resetStateEv
inline void QKeySequenceEditPrivate::resetState()
{
    if (releaseTimer.isActive())
        releaseTimer.stop();
    prevKey = -1;
    lineEdit->setText(keySequence.toString(QKeySequence::NativeText));
    lineEdit->setPlaceholderText(QKeySequenceEdit::tr("Press shortcut"));
}

//  from src/widgets/widgets/qkeysequenceedit.cpp, line 74, as _ZN23QKeySequenceEditPrivate13finishEditingEv
inline void QKeySequenceEditPrivate::finishEditing()
{
    Q_Q(QKeySequenceEdit);

    resetState();
    emit q->keySequenceChanged(keySequence);
    emit q->editingFinished();
}
//  -----------------------------------------------------------------------

//  A QKeySequenceEditPrivate that Python can take functions over in. Every QKeySequenceEditPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQKeySequenceEditPrivateCall0)(const void *, bool, int *);
typedef void (*CuteQKeySequenceEditPrivateCall1)(const void *, int, int *);
typedef void (*CuteQKeySequenceEditPrivateCall2)(const void *, int *);
typedef void (*CuteQKeySequenceEditPrivateCall3)(const void *, int *);
typedef void * (*CuteQKeySequenceEditPrivateCall4)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQKeySequenceEditPrivateCall5)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQKeySequenceEditPrivateCall6)(const void *, int *);
typedef int (*CuteQKeySequenceEditPrivateCall7)(const void *, int *);
typedef const QImage * (*CuteQKeySequenceEditPrivateCall8)(const void *, int *);
typedef void (*CuteQKeySequenceEditPrivateCall9)(const void *, int *);
typedef void (*CuteQKeySequenceEditPrivateCall10)(const void *, int *);
typedef void (*CuteQKeySequenceEditPrivateCall11)(const void *, int *);
typedef void (*CuteQKeySequenceEditPrivateCall12)(const void *, int *);
typedef void (*CuteQKeySequenceEditPrivateCall13)(const void *, int *);
typedef void (*CuteQKeySequenceEditPrivateCall14)(const void *, int *);
typedef void (*CuteQKeySequenceEditPrivateCall15)(const void *, int *);
typedef bool (*CuteQKeySequenceEditPrivateCall16)(const void *, int *);
typedef bool (*CuteQKeySequenceEditPrivateCall17)(const void *, int *);
class CuteQKeySequenceEditPrivate : public QKeySequenceEditPrivate {
public:
  using QKeySequenceEditPrivate::QKeySequenceEditPrivate;
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
      CuteQKeySequenceEditPrivateCall0 call = reinterpret_cast<CuteQKeySequenceEditPrivateCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[1]) {
      int handled = 0;
      CuteQKeySequenceEditPrivateCall1 call = reinterpret_cast<CuteQKeySequenceEditPrivateCall1>(taken[1]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[2]) {
      int handled = 0;
      CuteQKeySequenceEditPrivateCall2 call = reinterpret_cast<CuteQKeySequenceEditPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[3]) {
      int handled = 0;
      CuteQKeySequenceEditPrivateCall3 call = reinterpret_cast<CuteQKeySequenceEditPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[4]) {
      int handled = 0;
      CuteQKeySequenceEditPrivateCall4 call = reinterpret_cast<CuteQKeySequenceEditPrivateCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQKeySequenceEditPrivateCall5 call = reinterpret_cast<CuteQKeySequenceEditPrivateCall5>(taken[5]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQKeySequenceEditPrivateCall6 call = reinterpret_cast<CuteQKeySequenceEditPrivateCall6>(taken[6]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[7]) {
      int handled = 0;
      CuteQKeySequenceEditPrivateCall7 call = reinterpret_cast<CuteQKeySequenceEditPrivateCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[8]) {
      int handled = 0;
      CuteQKeySequenceEditPrivateCall8 call = reinterpret_cast<CuteQKeySequenceEditPrivateCall8>(taken[8]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[9]) {
      int handled = 0;
      CuteQKeySequenceEditPrivateCall9 call = reinterpret_cast<CuteQKeySequenceEditPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[10]) {
      int handled = 0;
      CuteQKeySequenceEditPrivateCall10 call = reinterpret_cast<CuteQKeySequenceEditPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[11]) {
      int handled = 0;
      CuteQKeySequenceEditPrivateCall11 call = reinterpret_cast<CuteQKeySequenceEditPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[12]) {
      int handled = 0;
      CuteQKeySequenceEditPrivateCall12 call = reinterpret_cast<CuteQKeySequenceEditPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[13]) {
      int handled = 0;
      CuteQKeySequenceEditPrivateCall13 call = reinterpret_cast<CuteQKeySequenceEditPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[14]) {
      int handled = 0;
      CuteQKeySequenceEditPrivateCall14 call = reinterpret_cast<CuteQKeySequenceEditPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[15]) {
      int handled = 0;
      CuteQKeySequenceEditPrivateCall15 call = reinterpret_cast<CuteQKeySequenceEditPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[16]) {
      int handled = 0;
      CuteQKeySequenceEditPrivateCall16 call = reinterpret_cast<CuteQKeySequenceEditPrivateCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[17]) {
      int handled = 0;
      CuteQKeySequenceEditPrivateCall17 call = reinterpret_cast<CuteQKeySequenceEditPrivateCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QKeySequenceEdit *QKeySequenceEditPrivate::q_func()
extern "C" Q_DECL_EXPORT
QKeySequenceEdit *ritual_ZN23QKeySequenceEditPrivate6q_funcEv(
    QKeySequenceEditPrivate *self) {
  return self->q_func();
}

//  const QKeySequenceEdit *QKeySequenceEditPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QKeySequenceEdit *ritual_ZNK23QKeySequenceEditPrivate6q_funcEv(
    const QKeySequenceEditPrivate *self) {
  return self->q_func();
}

//  void QKeySequenceEditPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QKeySequenceEditPrivate4initEv(
    QKeySequenceEditPrivate *self) {
  self->init();
}

//  int QKeySequenceEditPrivate::translateModifiers(Qt::KeyboardModifiers
//      state, const QString &text)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QKeySequenceEditPrivate18translateModifiersE6QFlagsIN2Qt16KeyboardModifierEERK7QString(
    QKeySequenceEditPrivate *self,
    int state,
    const QString *text) {
  return self->translateModifiers(
      QFlags<Qt::KeyboardModifier>::fromInt(state),
      *text);
}

//  void QKeySequenceEditPrivate::resetState()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QKeySequenceEditPrivate10resetStateEv(
    QKeySequenceEditPrivate *self) {
  self->resetState();
}

//  void QKeySequenceEditPrivate::finishEditing()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QKeySequenceEditPrivate13finishEditingEv(
    QKeySequenceEditPrivate *self) {
  self->finishEditing();
}

//  void QKeySequenceEditPrivate::rebuildKeySequence()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QKeySequenceEditPrivate18rebuildKeySequenceEv(
    QKeySequenceEditPrivate *self) {
  self->rebuildKeySequence();
}

//  a Python function taken by a CuteQKeySequenceEditPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QKeySequenceEditPrivate(
    QKeySequenceEditPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQKeySequenceEditPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(keysequenceedit)
