//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qfontdialog_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(fontdialog)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qfontdialog.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qfontdialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qfont.h>
#include <QtCore/qstring.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qwindowdefs.h"
#include "qfontdialog.h"
#include "qfontdialog_p.h"
#include <qapplication.h>
#include <qcheckbox.h>
#include <qcombobox.h>
#include <qevent.h>
#include <qgroupbox.h>
#include <qlabel.h>
#include <qlayout.h>
#include <qlineedit.h>
#include <qpushbutton.h>
#include <qstyle.h>
#include <qdialogbuttonbox.h>
#include <qheaderview.h>
#include <qlistview.h>
#include <qstringlistmodel.h>
#include <qvalidator.h>
#include <private/qfontdatabase_p.h>
#include <private/qdialog_p.h>
#include <private/qfont_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/dialogs/qfontdialog.cpp, line 456, as _ZN18QFontDialogPrivate10initHelperEP21QPlatformDialogHelper
inline void QFontDialogPrivate::initHelper(QPlatformDialogHelper *h)
{
    Q_Q(QFontDialog);
    auto *fontDialogHelper = static_cast<QPlatformFontDialogHelper *>(h);
    fontDialogHelper->setOptions(options);
    fontDialogHelper->setCurrentFont(q->currentFont());
    QObject::connect(fontDialogHelper, &QPlatformFontDialogHelper::currentFontChanged,
                     q, &QFontDialog::currentFontChanged);
    QObject::connect(fontDialogHelper, &QPlatformFontDialogHelper::fontSelected,
                     q, &QFontDialog::fontSelected);
}

//  from src/widgets/dialogs/qfontdialog.cpp, line 468, as _ZN18QFontDialogPrivate17helperPrepareShowEP21QPlatformDialogHelper
inline void QFontDialogPrivate::helperPrepareShow(QPlatformDialogHelper *)
{
    options->setWindowTitle(q_func()->windowTitle());
}

//  from src/widgets/dialogs/qfontdialog.cpp, line 76, as _ZN18QFontDialogPrivateC1Ev
inline QFontDialogPrivate::QFontDialogPrivate()
    : writingSystem(QFontDatabase::Any),
      options(QFontDialogOptions::create())
{
}

//  from src/widgets/dialogs/qfontdialog.cpp, line 82, as _ZN18QFontDialogPrivateD1Ev
inline QFontDialogPrivate::~QFontDialogPrivate()
{
}

//  from src/widgets/dialogs/qfontdialog.cpp, line 392, as _ZN18QFontDialogPrivate7getFontEPbRK5QFontP7QWidgetRK7QString6QFlagsIN11QFontDialog16FontDialogOptionEE
inline QFont QFontDialogPrivate::getFont(bool *ok, const QFont &initial, QWidget *parent,
                                  const QString &title, QFontDialog::FontDialogOptions options)
{
    QAutoPointer<QFontDialog> dlg(new QFontDialog(parent));
    dlg->setOptions(options);
    dlg->setCurrentFont(initial);
    if (!title.isEmpty())
        dlg->setWindowTitle(title);

    int ret = (dlg->exec() || (options & QFontDialog::NoButtons));
    if (ok)
        *ok = !!ret;
    if (ret && bool(dlg)) {
        return dlg->selectedFont();
    } else {
        return initial;
    }
}

//  from src/widgets/dialogs/qfontdialog.cpp, line 673, as _ZN18QFontDialogPrivate16updateSampleFontERK5QFont
inline void QFontDialogPrivate::updateSampleFont(const QFont &newFont)
{
    Q_Q(QFontDialog);
    if (newFont != sampleEdit->font()) {
        sampleEdit->setFont(newFont);
        emit q->currentFontChanged(newFont);
    }
}

//  from src/widgets/dialogs/qfontdialog.cpp, line 773, as _ZN18QFontDialogPrivate18retranslateStringsEv
inline void QFontDialogPrivate::retranslateStrings()
{
    familyAccel->setText(QFontDialog::tr("&Font"));
    styleAccel->setText(QFontDialog::tr("Font st&yle"));
    sizeAccel->setText(QFontDialog::tr("&Size"));
    effects->setTitle(QFontDialog::tr("Effects"));
    strikeout->setText(QFontDialog::tr("Stri&keout"));
    underline->setText(QFontDialog::tr("&Underline"));
    sample->setTitle(QFontDialog::tr("Sample"));
    writingSystemAccel->setText(QFontDialog::tr("Wr&iting System"));
}

//  from src/widgets/dialogs/qfontdialog.cpp, line 1041, as _ZNK18QFontDialogPrivate17canBeNativeDialogEv
inline bool QFontDialogPrivate::canBeNativeDialog() const
{
    // Don't use Q_Q here! This function is called from ~QDialog,
    // so Q_Q calling q_func() invokes undefined behavior (invalid cast in q_func()).
    const QDialog * const q = static_cast<const QDialog*>(q_ptr);
    if (nativeDialogInUse)
        return true;
    if (QCoreApplication::testAttribute(Qt::AA_DontUseNativeDialogs)
        || q->testAttribute(Qt::WA_DontShowOnScreen)
        || (options->options() & QFontDialog::DontUseNativeDialog)) {
        return false;
    }

    return strcmp(QFontDialog::staticMetaObject.className(), q->metaObject()->className()) == 0;
}

//  from src/widgets/dialogs/qfontdialog.cpp, line 995, as _ZN18QFontDialogPrivate10setVisibleEb
inline void QFontDialogPrivate::setVisible(bool visible)
{
    // Don't use Q_Q here! This function is called from ~QDialog,
    // so Q_Q calling q_func() invokes undefined behavior (invalid cast in q_func()).
    const auto q = static_cast<QDialog *>(q_ptr);

    if (canBeNativeDialog())
        setNativeDialogVisible(visible);
    if (nativeDialogInUse) {
        // Set WA_DontShowOnScreen so that QDialog::setVisible(visible) below
        // updates the state correctly, but skips showing the non-native version:
        q->setAttribute(Qt::WA_DontShowOnScreen, true);
    } else {
        q->setAttribute(Qt::WA_DontShowOnScreen, false);
    }
    QDialogPrivate::setVisible(visible);
}
//  -----------------------------------------------------------------------

//  A QFontDialogPrivate that Python can take functions over in. Every QFontDialogPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(dialog)
#if QT_CONFIG(fontdialog)
typedef bool (*CuteQFontDialogPrivateCall0)(const void *, int *);
#endif  // QT_CONFIG(fontdialog)
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(fontdialog)
typedef void (*CuteQFontDialogPrivateCall1)(const void *, bool, int *);
#endif  // QT_CONFIG(fontdialog)
#if QT_CONFIG(dialog)
#if QT_CONFIG(fontdialog)
typedef void (*CuteQFontDialogPrivateCall2)(const void *, QPlatformDialogHelper *, int *);
#endif  // QT_CONFIG(fontdialog)
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
#if QT_CONFIG(fontdialog)
typedef void (*CuteQFontDialogPrivateCall3)(const void *, QPlatformDialogHelper *, int *);
#endif  // QT_CONFIG(fontdialog)
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQFontDialogPrivateCall4)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef int (*CuteQFontDialogPrivateCall5)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQFontDialogPrivateCall6)(const void *, int, QPlatformDialogHelper *, int *);
#endif  // QT_CONFIG(dialog)
typedef void (*CuteQFontDialogPrivateCall7)(const void *, int, int *);
typedef void (*CuteQFontDialogPrivateCall8)(const void *, int *);
typedef void * (*CuteQFontDialogPrivateCall9)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQFontDialogPrivateCall10)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQFontDialogPrivateCall11)(const void *, int *);
typedef int (*CuteQFontDialogPrivateCall12)(const void *, int *);
typedef const QImage * (*CuteQFontDialogPrivateCall13)(const void *, int *);
typedef void (*CuteQFontDialogPrivateCall14)(const void *, int *);
typedef void (*CuteQFontDialogPrivateCall15)(const void *, int *);
typedef void (*CuteQFontDialogPrivateCall16)(const void *, int *);
typedef void (*CuteQFontDialogPrivateCall17)(const void *, int *);
typedef void (*CuteQFontDialogPrivateCall18)(const void *, int *);
typedef void (*CuteQFontDialogPrivateCall19)(const void *, int *);
typedef void (*CuteQFontDialogPrivateCall20)(const void *, int *);
typedef bool (*CuteQFontDialogPrivateCall21)(const void *, int *);
typedef bool (*CuteQFontDialogPrivateCall22)(const void *, int *);
class CuteQFontDialogPrivate : public QFontDialogPrivate {
public:
  using QFontDialogPrivate::QFontDialogPrivate;
  void *taken[23] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(dialog)
#if QT_CONFIG(fontdialog)
    if (!std::strcmp(key, "_ZNK14QDialogPrivate17canBeNativeDialogEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(fontdialog)
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(fontdialog)
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10setVisibleEb")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(fontdialog)
#if QT_CONFIG(dialog)
#if QT_CONFIG(fontdialog)
    if (!std::strcmp(key, "_ZN14QDialogPrivate10initHelperEP21QPlatformDialogHelper")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(fontdialog)
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
#if QT_CONFIG(fontdialog)
    if (!std::strcmp(key, "_ZN14QDialogPrivate17helperPrepareShowEP21QPlatformDialogHelper")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(fontdialog)
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN14QWidgetPrivate8recreateEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZNK14QDialogPrivate10dialogCodeEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN14QDialogPrivate10helperDoneEN7QDialog10DialogCodeEP21QPlatformDialogHelper")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14aboutToDestroyEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate11focusObjectEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate9rhiConfigEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate7textureEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate16textureListFlagsEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15grabFramebufferEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25beginBackingStorePaintingEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate23endBackingStorePaintingEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate12beginComposeEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10endComposeEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate29initializeViewportFramebufferEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25resizeViewportFramebufferEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14resolveSamplesEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15isStereoEnabledEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate24toggleStereoTargetBufferEv")) {
      taken[22] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(dialog)
#if QT_CONFIG(fontdialog)
  //  bool QFontDialogPrivate::canBeNativeDialog() const
  bool canBeNativeDialog() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQFontDialogPrivateCall0 call = reinterpret_cast<CuteQFontDialogPrivateCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFontDialogPrivate::canBeNativeDialog();
  }
#endif  // QT_CONFIG(fontdialog)
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(fontdialog)
  //  void QFontDialogPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[1]) {
      int handled = 0;
      CuteQFontDialogPrivateCall1 call = reinterpret_cast<CuteQFontDialogPrivateCall1>(taken[1]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QFontDialogPrivate::setVisible(visible);
  }
#endif  // QT_CONFIG(fontdialog)

#if QT_CONFIG(dialog)
#if QT_CONFIG(fontdialog)
  //  void QFontDialogPrivate::initHelper(QPlatformDialogHelper *a0)
  void initHelper(QPlatformDialogHelper *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQFontDialogPrivateCall2 call = reinterpret_cast<CuteQFontDialogPrivateCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFontDialogPrivate::initHelper(a0);
  }
#endif  // QT_CONFIG(fontdialog)
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
#if QT_CONFIG(fontdialog)
  //  void QFontDialogPrivate::helperPrepareShow(QPlatformDialogHelper *a0)
  void helperPrepareShow(QPlatformDialogHelper *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQFontDialogPrivateCall3 call = reinterpret_cast<CuteQFontDialogPrivateCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFontDialogPrivate::helperPrepareShow(a0);
  }
#endif  // QT_CONFIG(fontdialog)
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialogPrivate::recreate()
  void recreate() override {
    if (taken[4]) {
      int handled = 0;
      CuteQFontDialogPrivateCall4 call = reinterpret_cast<CuteQFontDialogPrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QDialogPrivate::recreate();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  int QDialogPrivate::dialogCode() const
  int dialogCode() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQFontDialogPrivateCall5 call = reinterpret_cast<CuteQFontDialogPrivateCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QDialogPrivate::dialogCode();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialogPrivate::helperDone(QDialog::DialogCode a0,
  //      QPlatformDialogHelper *a1)
  void helperDone(
      QDialog::DialogCode a0,
      QPlatformDialogHelper *a1) override {
    if (taken[6]) {
      int handled = 0;
      CuteQFontDialogPrivateCall6 call = reinterpret_cast<CuteQFontDialogPrivateCall6>(taken[6]);
      call(this, static_cast<int>(a0), a1, &handled);
      if (handled) return;
    }
    QDialogPrivate::helperDone(a0, a1);
  }
#endif  // QT_CONFIG(dialog)

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[7]) {
      int handled = 0;
      CuteQFontDialogPrivateCall7 call = reinterpret_cast<CuteQFontDialogPrivateCall7>(taken[7]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[8]) {
      int handled = 0;
      CuteQFontDialogPrivateCall8 call = reinterpret_cast<CuteQFontDialogPrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[9]) {
      int handled = 0;
      CuteQFontDialogPrivateCall9 call = reinterpret_cast<CuteQFontDialogPrivateCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQFontDialogPrivateCall10 call = reinterpret_cast<CuteQFontDialogPrivateCall10>(taken[10]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQFontDialogPrivateCall11 call = reinterpret_cast<CuteQFontDialogPrivateCall11>(taken[11]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[12]) {
      int handled = 0;
      CuteQFontDialogPrivateCall12 call = reinterpret_cast<CuteQFontDialogPrivateCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[13]) {
      int handled = 0;
      CuteQFontDialogPrivateCall13 call = reinterpret_cast<CuteQFontDialogPrivateCall13>(taken[13]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[14]) {
      int handled = 0;
      CuteQFontDialogPrivateCall14 call = reinterpret_cast<CuteQFontDialogPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[15]) {
      int handled = 0;
      CuteQFontDialogPrivateCall15 call = reinterpret_cast<CuteQFontDialogPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[16]) {
      int handled = 0;
      CuteQFontDialogPrivateCall16 call = reinterpret_cast<CuteQFontDialogPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[17]) {
      int handled = 0;
      CuteQFontDialogPrivateCall17 call = reinterpret_cast<CuteQFontDialogPrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[18]) {
      int handled = 0;
      CuteQFontDialogPrivateCall18 call = reinterpret_cast<CuteQFontDialogPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[19]) {
      int handled = 0;
      CuteQFontDialogPrivateCall19 call = reinterpret_cast<CuteQFontDialogPrivateCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[20]) {
      int handled = 0;
      CuteQFontDialogPrivateCall20 call = reinterpret_cast<CuteQFontDialogPrivateCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[21]) {
      int handled = 0;
      CuteQFontDialogPrivateCall21 call = reinterpret_cast<CuteQFontDialogPrivateCall21>(taken[21]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[22]) {
      int handled = 0;
      CuteQFontDialogPrivateCall22 call = reinterpret_cast<CuteQFontDialogPrivateCall22>(taken[22]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QFontDialog *QFontDialogPrivate::q_func()
extern "C" Q_DECL_EXPORT
QFontDialog *ritual_ZN18QFontDialogPrivate6q_funcEv(
    QFontDialogPrivate *self) {
  return self->q_func();
}

//  const QFontDialog *QFontDialogPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QFontDialog *ritual_ZNK18QFontDialogPrivate6q_funcEv(
    const QFontDialogPrivate *self) {
  return self->q_func();
}

//  QFontDialogPrivate::QFontDialogPrivate()
extern "C" Q_DECL_EXPORT
QFontDialogPrivate *ritual_ZN18QFontDialogPrivateC1Ev() {
  return new CuteQFontDialogPrivate();
}

//  QFontDialogPrivate::~QFontDialogPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFontDialogPrivateD1Ev(QFontDialogPrivate *self) {
  delete self;
}

//  QPlatformFontDialogHelper *QFontDialogPrivate::platformFontDialogHelper()
//      const
extern "C" Q_DECL_EXPORT
QPlatformFontDialogHelper *ritual_ZNK18QFontDialogPrivate24platformFontDialogHelperEv(
    const QFontDialogPrivate *self) {
  return self->platformFontDialogHelper();
}

//  QFont QFontDialogPrivate::getFont(bool *ok, const QFont &initial, QWidget
//      *parent, const QString &title, QFontDialog::FontDialogOptions
//      options)
extern "C" Q_DECL_EXPORT
QFont *ritual_ZN18QFontDialogPrivate7getFontEPbRK5QFontP7QWidgetRK7QString6QFlagsIN11QFontDialog16FontDialogOptionEE(
    bool *ok,
    const QFont *initial,
    QWidget *parent,
    const QString *title,
    int options) {
  return new QFont(
      QFontDialogPrivate::getFont(
          ok,
          *initial,
          parent,
          *title,
          QFlags<QFontDialog::FontDialogOption>::fromInt(options)));
}

//  void QFontDialogPrivate::updateSampleFont(const QFont &newFont)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFontDialogPrivate16updateSampleFontERK5QFont(
    QFontDialogPrivate *self,
    const QFont *newFont) {
  self->updateSampleFont(*newFont);
}

//  void QFontDialogPrivate::retranslateStrings()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFontDialogPrivate18retranslateStringsEv(
    QFontDialogPrivate *self) {
  self->retranslateStrings();
}

//  bool QFontDialogPrivate::canBeNativeDialog() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QFontDialogPrivate17canBeNativeDialogEv(
    const QFontDialogPrivate *self) {
  return self->canBeNativeDialog();
}

//  void QFontDialogPrivate::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFontDialogPrivate10setVisibleEb(
    QFontDialogPrivate *self,
    bool visible) {
  self->setVisible(visible);
}

//  void QFontDialogPrivate::initHelper(QPlatformDialogHelper *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFontDialogPrivate10initHelperEP21QPlatformDialogHelper(
    QFontDialogPrivate *self,
    QPlatformDialogHelper *a0) {
  self->initHelper(a0);
}

//  void QFontDialogPrivate::helperPrepareShow(QPlatformDialogHelper *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFontDialogPrivate17helperPrepareShowEP21QPlatformDialogHelper(
    QFontDialogPrivate *self,
    QPlatformDialogHelper *a0) {
  self->helperPrepareShow(a0);
}

//  a Python function taken by a CuteQFontDialogPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFontDialogPrivate(
    QFontDialogPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFontDialogPrivate *>(self)->take(key, call);
}

//  bool QFontDialogPrivate::canBeNativeDialog() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QFontDialogPrivate17canBeNativeDialogEv(
    const QFontDialogPrivate *self) {
  return self->QFontDialogPrivate::canBeNativeDialog();
}

//  void QFontDialogPrivate::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QFontDialogPrivate10setVisibleEb(
    QFontDialogPrivate *self,
    bool visible) {
  self->QFontDialogPrivate::setVisible(visible);
}

//  void QFontDialogPrivate::initHelper(QPlatformDialogHelper *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QFontDialogPrivate10initHelperEP21QPlatformDialogHelper(
    QFontDialogPrivate *self,
    QPlatformDialogHelper *a0) {
  self->QFontDialogPrivate::initHelper(a0);
}

//  void QFontDialogPrivate::helperPrepareShow(QPlatformDialogHelper *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QFontDialogPrivate17helperPrepareShowEP21QPlatformDialogHelper(
    QFontDialogPrivate *self,
    QPlatformDialogHelper *a0) {
  self->QFontDialogPrivate::helperPrepareShow(a0);
}

#endif  // QT_CONFIG(fontdialog)
