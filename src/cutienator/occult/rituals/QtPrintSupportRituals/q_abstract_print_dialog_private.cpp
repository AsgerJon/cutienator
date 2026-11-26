//  Written by dev_tooling.RitualGenerator from the records of
//  QtPrintSupport/6.12.0/QtPrintSupport/private/qabstractprintdialog_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtPrintSupport/qtprintsupportglobal.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#if QT_CONFIG(printdialog)
#if QT_CONFIG(printdialog)
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#if QT_CONFIG(printdialog)
#include <QtPrintSupport/qabstractprintdialog.h>
#endif
#include <QtPrintSupport/QtPrintSupport>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qabstractprintdialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qwidget.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPrintSupport/private/qabstractprintdialog_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtPrintSupport/qprintdialog.h>
#include <QtPrintSupport/qprinter.h>
#include <QtPrintSupport/private/qprinter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/printsupport/dialogs/qabstractprintdialog.cpp, line 245, as _ZN27QAbstractPrintDialogPrivate10setPrinterEP8QPrinter
inline void QAbstractPrintDialogPrivate::setPrinter(QPrinter *newPrinter)
{
    if (newPrinter) {
        printer = newPrinter;
        ownsPrinter = false;
        if (printer->fromPage() || printer->toPage())
            options |= QAbstractPrintDialog::PrintPageRange;
    } else {
        printer = new QPrinter;
        ownsPrinter = true;
    }
    pd = printer->d_func();
}
//  -----------------------------------------------------------------------

//  A QAbstractPrintDialogPrivate that Python can take functions over in. Every QAbstractPrintDialogPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(dialog)
typedef void (*CuteQAbstractPrintDialogPrivateCall0)(const void *, bool, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef bool (*CuteQAbstractPrintDialogPrivateCall1)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQAbstractPrintDialogPrivateCall2)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef int (*CuteQAbstractPrintDialogPrivateCall3)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQAbstractPrintDialogPrivateCall4)(const void *, QPlatformDialogHelper *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQAbstractPrintDialogPrivateCall5)(const void *, QPlatformDialogHelper *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQAbstractPrintDialogPrivateCall6)(const void *, int, QPlatformDialogHelper *, int *);
#endif  // QT_CONFIG(dialog)
typedef void (*CuteQAbstractPrintDialogPrivateCall7)(const void *, int, int *);
typedef void (*CuteQAbstractPrintDialogPrivateCall8)(const void *, int *);
typedef void * (*CuteQAbstractPrintDialogPrivateCall9)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQAbstractPrintDialogPrivateCall10)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQAbstractPrintDialogPrivateCall11)(const void *, int *);
typedef int (*CuteQAbstractPrintDialogPrivateCall12)(const void *, int *);
typedef const QImage * (*CuteQAbstractPrintDialogPrivateCall13)(const void *, int *);
typedef void (*CuteQAbstractPrintDialogPrivateCall14)(const void *, int *);
typedef void (*CuteQAbstractPrintDialogPrivateCall15)(const void *, int *);
typedef void (*CuteQAbstractPrintDialogPrivateCall16)(const void *, int *);
typedef void (*CuteQAbstractPrintDialogPrivateCall17)(const void *, int *);
typedef void (*CuteQAbstractPrintDialogPrivateCall18)(const void *, int *);
typedef void (*CuteQAbstractPrintDialogPrivateCall19)(const void *, int *);
typedef void (*CuteQAbstractPrintDialogPrivateCall20)(const void *, int *);
typedef bool (*CuteQAbstractPrintDialogPrivateCall21)(const void *, int *);
typedef bool (*CuteQAbstractPrintDialogPrivateCall22)(const void *, int *);
class CuteQAbstractPrintDialogPrivate : public QAbstractPrintDialogPrivate {
public:
  using QAbstractPrintDialogPrivate::QAbstractPrintDialogPrivate;
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
      CuteQAbstractPrintDialogPrivateCall0 call = reinterpret_cast<CuteQAbstractPrintDialogPrivateCall0>(taken[0]);
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
      CuteQAbstractPrintDialogPrivateCall1 call = reinterpret_cast<CuteQAbstractPrintDialogPrivateCall1>(taken[1]);
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
      CuteQAbstractPrintDialogPrivateCall2 call = reinterpret_cast<CuteQAbstractPrintDialogPrivateCall2>(taken[2]);
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
      CuteQAbstractPrintDialogPrivateCall3 call = reinterpret_cast<CuteQAbstractPrintDialogPrivateCall3>(taken[3]);
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
      CuteQAbstractPrintDialogPrivateCall4 call = reinterpret_cast<CuteQAbstractPrintDialogPrivateCall4>(taken[4]);
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
      CuteQAbstractPrintDialogPrivateCall5 call = reinterpret_cast<CuteQAbstractPrintDialogPrivateCall5>(taken[5]);
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
      CuteQAbstractPrintDialogPrivateCall6 call = reinterpret_cast<CuteQAbstractPrintDialogPrivateCall6>(taken[6]);
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
      CuteQAbstractPrintDialogPrivateCall7 call = reinterpret_cast<CuteQAbstractPrintDialogPrivateCall7>(taken[7]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractPrintDialogPrivateCall8 call = reinterpret_cast<CuteQAbstractPrintDialogPrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractPrintDialogPrivateCall9 call = reinterpret_cast<CuteQAbstractPrintDialogPrivateCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstractPrintDialogPrivateCall10 call = reinterpret_cast<CuteQAbstractPrintDialogPrivateCall10>(taken[10]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQAbstractPrintDialogPrivateCall11 call = reinterpret_cast<CuteQAbstractPrintDialogPrivateCall11>(taken[11]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[12]) {
      int handled = 0;
      CuteQAbstractPrintDialogPrivateCall12 call = reinterpret_cast<CuteQAbstractPrintDialogPrivateCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[13]) {
      int handled = 0;
      CuteQAbstractPrintDialogPrivateCall13 call = reinterpret_cast<CuteQAbstractPrintDialogPrivateCall13>(taken[13]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[14]) {
      int handled = 0;
      CuteQAbstractPrintDialogPrivateCall14 call = reinterpret_cast<CuteQAbstractPrintDialogPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[15]) {
      int handled = 0;
      CuteQAbstractPrintDialogPrivateCall15 call = reinterpret_cast<CuteQAbstractPrintDialogPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[16]) {
      int handled = 0;
      CuteQAbstractPrintDialogPrivateCall16 call = reinterpret_cast<CuteQAbstractPrintDialogPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[17]) {
      int handled = 0;
      CuteQAbstractPrintDialogPrivateCall17 call = reinterpret_cast<CuteQAbstractPrintDialogPrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[18]) {
      int handled = 0;
      CuteQAbstractPrintDialogPrivateCall18 call = reinterpret_cast<CuteQAbstractPrintDialogPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[19]) {
      int handled = 0;
      CuteQAbstractPrintDialogPrivateCall19 call = reinterpret_cast<CuteQAbstractPrintDialogPrivateCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[20]) {
      int handled = 0;
      CuteQAbstractPrintDialogPrivateCall20 call = reinterpret_cast<CuteQAbstractPrintDialogPrivateCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[21]) {
      int handled = 0;
      CuteQAbstractPrintDialogPrivateCall21 call = reinterpret_cast<CuteQAbstractPrintDialogPrivateCall21>(taken[21]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[22]) {
      int handled = 0;
      CuteQAbstractPrintDialogPrivateCall22 call = reinterpret_cast<CuteQAbstractPrintDialogPrivateCall22>(taken[22]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QAbstractPrintDialog *QAbstractPrintDialogPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAbstractPrintDialog *ritual_ZN27QAbstractPrintDialogPrivate6q_funcEv(
    QAbstractPrintDialogPrivate *self) {
  return self->q_func();
}

//  const QAbstractPrintDialog *QAbstractPrintDialogPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAbstractPrintDialog *ritual_ZNK27QAbstractPrintDialogPrivate6q_funcEv(
    const QAbstractPrintDialogPrivate *self) {
  return self->q_func();
}

//  QAbstractPrintDialogPrivate::QAbstractPrintDialogPrivate()
extern "C" Q_DECL_EXPORT
QAbstractPrintDialogPrivate *ritual_ZN27QAbstractPrintDialogPrivateC1Ev() {
  return new CuteQAbstractPrintDialogPrivate();
}

//  void QAbstractPrintDialogPrivate::setTabs(const QList<QWidget *> &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAbstractPrintDialogPrivate7setTabsERK5QListIP7QWidgetE(
    QAbstractPrintDialogPrivate *self,
    const QList<QWidget *> *a0) {
  self->setTabs(*a0);
}

//  void QAbstractPrintDialogPrivate::setPrinter(QPrinter *newPrinter)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAbstractPrintDialogPrivate10setPrinterEP8QPrinter(
    QAbstractPrintDialogPrivate *self,
    QPrinter *newPrinter) {
  self->setPrinter(newPrinter);
}

//  a Python function taken by a CuteQAbstractPrintDialogPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractPrintDialogPrivate(
    QAbstractPrintDialogPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractPrintDialogPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(printdialog)
#endif  // QT_CONFIG(printdialog)
