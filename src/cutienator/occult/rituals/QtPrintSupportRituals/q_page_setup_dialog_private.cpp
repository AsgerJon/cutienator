//  Written by dev_tooling.RitualGenerator from the records of
//  QtPrintSupport/6.12.0/QtPrintSupport/private/qpagesetupdialog_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtPrintSupport/qtprintsupportglobal.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#if QT_CONFIG(printdialog)
#if QT_CONFIG(printdialog)
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#include <QtPrintSupport/qpagesetupdialog.h>
#include <QtPrintSupport/QtPrintSupport>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qpagesetupdialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPrintSupport/qpagesetupdialog.h>
#include <QtPrintSupport/private/qpagesetupdialog_p.h>
#include <QtPrintSupport/qprinter.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/printsupport/dialogs/qpagesetupdialog.cpp, line 65, as _ZN23QPageSetupDialogPrivateC1EP8QPrinter
inline QPageSetupDialogPrivate::QPageSetupDialogPrivate(QPrinter *prntr) : printer(nullptr), ownsPrinter(false)
{
    setPrinter(prntr);
}

//  from src/printsupport/dialogs/qpagesetupdialog.cpp, line 70, as _ZN23QPageSetupDialogPrivate10setPrinterEP8QPrinter
inline void QPageSetupDialogPrivate::setPrinter(QPrinter *newPrinter)
{
    if (printer && ownsPrinter)
        delete printer;

    if (newPrinter) {
        printer = newPrinter;
        ownsPrinter = false;
    } else {
        printer = new QPrinter;
        ownsPrinter = true;
    }
    if (printer->outputFormat() != QPrinter::NativeFormat)
        qWarning("QPageSetupDialog: Cannot be used on non-native printers");
}
//  -----------------------------------------------------------------------

//  A QPageSetupDialogPrivate that Python can take functions over in. Every QPageSetupDialogPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(dialog)
typedef void (*CuteQPageSetupDialogPrivateCall0)(const void *, bool, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef bool (*CuteQPageSetupDialogPrivateCall1)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQPageSetupDialogPrivateCall2)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef int (*CuteQPageSetupDialogPrivateCall3)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQPageSetupDialogPrivateCall4)(const void *, QPlatformDialogHelper *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQPageSetupDialogPrivateCall5)(const void *, QPlatformDialogHelper *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQPageSetupDialogPrivateCall6)(const void *, int, QPlatformDialogHelper *, int *);
#endif  // QT_CONFIG(dialog)
typedef void (*CuteQPageSetupDialogPrivateCall7)(const void *, int, int *);
typedef void (*CuteQPageSetupDialogPrivateCall8)(const void *, int *);
typedef void * (*CuteQPageSetupDialogPrivateCall9)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQPageSetupDialogPrivateCall10)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQPageSetupDialogPrivateCall11)(const void *, int *);
typedef int (*CuteQPageSetupDialogPrivateCall12)(const void *, int *);
typedef const QImage * (*CuteQPageSetupDialogPrivateCall13)(const void *, int *);
typedef void (*CuteQPageSetupDialogPrivateCall14)(const void *, int *);
typedef void (*CuteQPageSetupDialogPrivateCall15)(const void *, int *);
typedef void (*CuteQPageSetupDialogPrivateCall16)(const void *, int *);
typedef void (*CuteQPageSetupDialogPrivateCall17)(const void *, int *);
typedef void (*CuteQPageSetupDialogPrivateCall18)(const void *, int *);
typedef void (*CuteQPageSetupDialogPrivateCall19)(const void *, int *);
typedef void (*CuteQPageSetupDialogPrivateCall20)(const void *, int *);
typedef bool (*CuteQPageSetupDialogPrivateCall21)(const void *, int *);
typedef bool (*CuteQPageSetupDialogPrivateCall22)(const void *, int *);
class CuteQPageSetupDialogPrivate : public QPageSetupDialogPrivate {
public:
  using QPageSetupDialogPrivate::QPageSetupDialogPrivate;
  void *taken[23] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10setVisibleEb")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZNK14QDialogPrivate17canBeNativeDialogEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN14QWidgetPrivate8recreateEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZNK14QDialogPrivate10dialogCodeEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN14QDialogPrivate10initHelperEP21QPlatformDialogHelper")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN14QDialogPrivate17helperPrepareShowEP21QPlatformDialogHelper")) {
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
  //  void QDialogPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPageSetupDialogPrivateCall0 call = reinterpret_cast<CuteQPageSetupDialogPrivateCall0>(taken[0]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QDialogPrivate::setVisible(visible);
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  bool QDialogPrivate::canBeNativeDialog() const
  bool canBeNativeDialog() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPageSetupDialogPrivateCall1 call = reinterpret_cast<CuteQPageSetupDialogPrivateCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QDialogPrivate::canBeNativeDialog();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialogPrivate::recreate()
  void recreate() override {
    if (taken[2]) {
      int handled = 0;
      CuteQPageSetupDialogPrivateCall2 call = reinterpret_cast<CuteQPageSetupDialogPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QDialogPrivate::recreate();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  int QDialogPrivate::dialogCode() const
  int dialogCode() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQPageSetupDialogPrivateCall3 call = reinterpret_cast<CuteQPageSetupDialogPrivateCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QDialogPrivate::dialogCode();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialogPrivate::initHelper(QPlatformDialogHelper *a0)
  void initHelper(QPlatformDialogHelper *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPageSetupDialogPrivateCall4 call = reinterpret_cast<CuteQPageSetupDialogPrivateCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialogPrivate::initHelper(a0);
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialogPrivate::helperPrepareShow(QPlatformDialogHelper *a0)
  void helperPrepareShow(QPlatformDialogHelper *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPageSetupDialogPrivateCall5 call = reinterpret_cast<CuteQPageSetupDialogPrivateCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QDialogPrivate::helperPrepareShow(a0);
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
      CuteQPageSetupDialogPrivateCall6 call = reinterpret_cast<CuteQPageSetupDialogPrivateCall6>(taken[6]);
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
      CuteQPageSetupDialogPrivateCall7 call = reinterpret_cast<CuteQPageSetupDialogPrivateCall7>(taken[7]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[8]) {
      int handled = 0;
      CuteQPageSetupDialogPrivateCall8 call = reinterpret_cast<CuteQPageSetupDialogPrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[9]) {
      int handled = 0;
      CuteQPageSetupDialogPrivateCall9 call = reinterpret_cast<CuteQPageSetupDialogPrivateCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQPageSetupDialogPrivateCall10 call = reinterpret_cast<CuteQPageSetupDialogPrivateCall10>(taken[10]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQPageSetupDialogPrivateCall11 call = reinterpret_cast<CuteQPageSetupDialogPrivateCall11>(taken[11]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[12]) {
      int handled = 0;
      CuteQPageSetupDialogPrivateCall12 call = reinterpret_cast<CuteQPageSetupDialogPrivateCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[13]) {
      int handled = 0;
      CuteQPageSetupDialogPrivateCall13 call = reinterpret_cast<CuteQPageSetupDialogPrivateCall13>(taken[13]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[14]) {
      int handled = 0;
      CuteQPageSetupDialogPrivateCall14 call = reinterpret_cast<CuteQPageSetupDialogPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[15]) {
      int handled = 0;
      CuteQPageSetupDialogPrivateCall15 call = reinterpret_cast<CuteQPageSetupDialogPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[16]) {
      int handled = 0;
      CuteQPageSetupDialogPrivateCall16 call = reinterpret_cast<CuteQPageSetupDialogPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[17]) {
      int handled = 0;
      CuteQPageSetupDialogPrivateCall17 call = reinterpret_cast<CuteQPageSetupDialogPrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[18]) {
      int handled = 0;
      CuteQPageSetupDialogPrivateCall18 call = reinterpret_cast<CuteQPageSetupDialogPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[19]) {
      int handled = 0;
      CuteQPageSetupDialogPrivateCall19 call = reinterpret_cast<CuteQPageSetupDialogPrivateCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[20]) {
      int handled = 0;
      CuteQPageSetupDialogPrivateCall20 call = reinterpret_cast<CuteQPageSetupDialogPrivateCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[21]) {
      int handled = 0;
      CuteQPageSetupDialogPrivateCall21 call = reinterpret_cast<CuteQPageSetupDialogPrivateCall21>(taken[21]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[22]) {
      int handled = 0;
      CuteQPageSetupDialogPrivateCall22 call = reinterpret_cast<CuteQPageSetupDialogPrivateCall22>(taken[22]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QPageSetupDialog *QPageSetupDialogPrivate::q_func()
extern "C" Q_DECL_EXPORT
QPageSetupDialog *ritual_ZN23QPageSetupDialogPrivate6q_funcEv(
    QPageSetupDialogPrivate *self) {
  return self->q_func();
}

//  const QPageSetupDialog *QPageSetupDialogPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QPageSetupDialog *ritual_ZNK23QPageSetupDialogPrivate6q_funcEv(
    const QPageSetupDialogPrivate *self) {
  return self->q_func();
}

//  QPageSetupDialogPrivate::QPageSetupDialogPrivate(QPrinter *printer)
extern "C" Q_DECL_EXPORT
QPageSetupDialogPrivate *ritual_ZN23QPageSetupDialogPrivateC1EP8QPrinter(
    QPrinter *printer) {
  return new CuteQPageSetupDialogPrivate(printer);
}

//  void QPageSetupDialogPrivate::setPrinter(QPrinter *newPrinter)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPageSetupDialogPrivate10setPrinterEP8QPrinter(
    QPageSetupDialogPrivate *self,
    QPrinter *newPrinter) {
  self->setPrinter(newPrinter);
}

//  a Python function taken by a CuteQPageSetupDialogPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPageSetupDialogPrivate(
    QPageSetupDialogPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPageSetupDialogPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(printdialog)
#endif  // QT_CONFIG(printdialog)
