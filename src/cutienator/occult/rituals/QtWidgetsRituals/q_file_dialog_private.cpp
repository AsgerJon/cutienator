//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qfiledialog_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(filedialog)
#if QT_CONFIG(filedialog)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qfiledialog.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qfiledialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qpoint.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtWidgets/private/qwidgetitemdata_p.h>
#include <QtWidgets/qfiledialog.h>
#include <QtWidgets/private/qfiledialog_p.h>
#include <QtWidgets/private/qapplication_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qfontmetrics.h>
#include <QtWidgets/qaction.h>
#include <QtWidgets/qactiongroup.h>
#include <QtWidgets/qheaderview.h>
#if QT_CONFIG(shortcut)
#  include <QtWidgets/qshortcut.h>
#endif
#include <QtWidgets/qgridlayout.h>
#if QT_CONFIG(menu)
#include <QtWidgets/qmenu.h>
#endif
#if QT_CONFIG(messagebox)
#include <QtWidgets/qmessagebox.h>
#endif
#include <stdlib.h>
#if QT_CONFIG(settings)
#include <QtCore/qsettings.h>
#endif
#include <QtCore/qdebug.h>
#if QT_CONFIG(mimetype)
#include <QtCore/qmimedatabase.h>
#endif
#if QT_CONFIG(regularexpression)
#include <QtCore/qregularexpression.h>
#endif
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qstylepainter.h>
#if defined(Q_OS_UNIX)
#include <pwd.h>
#include <unistd.h> // for pathconf() on OS X
#elif defined(Q_OS_WIN)
#  include <QtCore/qt_windows.h>
#endif
#if defined(Q_OS_WASM)
#include <QtGui/private/qwasmlocalfileaccess_p.h>
#endif
#include <algorithm>
#include <QtCore/QMetaEnum>
#if QT_CONFIG(shortcut)
#  include <QtWidgets/qshortcut.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/dialogs/qfiledialog.cpp, line 624, as _ZN18QFileDialogPrivate17updateLookInLabelEv
inline void QFileDialogPrivate::updateLookInLabel()
{
    if (options->isLabelExplicitlySet(QFileDialogOptions::LookIn))
        setLabelTextControl(QFileDialog::LookIn, options->labelText(QFileDialogOptions::LookIn));
}

//  from src/widgets/dialogs/qfiledialog.cpp, line 630, as _ZN18QFileDialogPrivate19updateFileNameLabelEv
inline void QFileDialogPrivate::updateFileNameLabel()
{
    if (options->isLabelExplicitlySet(QFileDialogOptions::FileName)) {
        setLabelTextControl(QFileDialog::FileName, options->labelText(QFileDialogOptions::FileName));
    } else {
        switch (q_func()->fileMode()) {
        case QFileDialog::Directory:
            setLabelTextControl(QFileDialog::FileName, QFileDialog::tr("Directory:"));
            break;
        default:
            setLabelTextControl(QFileDialog::FileName, QFileDialog::tr("File &name:"));
            break;
        }
    }
}

//  from src/widgets/dialogs/qfiledialog.cpp, line 646, as _ZN18QFileDialogPrivate19updateFileTypeLabelEv
inline void QFileDialogPrivate::updateFileTypeLabel()
{
    if (options->isLabelExplicitlySet(QFileDialogOptions::FileType))
        setLabelTextControl(QFileDialog::FileType, options->labelText(QFileDialogOptions::FileType));
}

//  from src/widgets/dialogs/qfiledialog.cpp, line 738, as _ZNK18QFileDialogPrivate12usingWidgetsEv
inline bool QFileDialogPrivate::usingWidgets() const
{
    return !nativeDialogInUse && qFileDialogUi;
}
//  -----------------------------------------------------------------------

//  A QFileDialogPrivate that Python can take functions over in. Every QFileDialogPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(dialog)
#if QT_CONFIG(filedialog)
typedef bool (*CuteQFileDialogPrivateCall0)(const void *, int *);
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(filedialog)
typedef void (*CuteQFileDialogPrivateCall1)(const void *, bool, int *);
#endif  // QT_CONFIG(filedialog)
#if QT_CONFIG(dialog)
#if QT_CONFIG(filedialog)
typedef void (*CuteQFileDialogPrivateCall2)(const void *, QPlatformDialogHelper *, int *);
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
#if QT_CONFIG(filedialog)
typedef void (*CuteQFileDialogPrivateCall3)(const void *, QPlatformDialogHelper *, int *);
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
#if QT_CONFIG(filedialog)
typedef void (*CuteQFileDialogPrivateCall4)(const void *, int, QPlatformDialogHelper *, int *);
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQFileDialogPrivateCall5)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef int (*CuteQFileDialogPrivateCall6)(const void *, int *);
#endif  // QT_CONFIG(dialog)
typedef void (*CuteQFileDialogPrivateCall7)(const void *, int, int *);
typedef void (*CuteQFileDialogPrivateCall8)(const void *, int *);
typedef void * (*CuteQFileDialogPrivateCall9)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQFileDialogPrivateCall10)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQFileDialogPrivateCall11)(const void *, int *);
typedef int (*CuteQFileDialogPrivateCall12)(const void *, int *);
typedef const QImage * (*CuteQFileDialogPrivateCall13)(const void *, int *);
typedef void (*CuteQFileDialogPrivateCall14)(const void *, int *);
typedef void (*CuteQFileDialogPrivateCall15)(const void *, int *);
typedef void (*CuteQFileDialogPrivateCall16)(const void *, int *);
typedef void (*CuteQFileDialogPrivateCall17)(const void *, int *);
typedef void (*CuteQFileDialogPrivateCall18)(const void *, int *);
typedef void (*CuteQFileDialogPrivateCall19)(const void *, int *);
typedef void (*CuteQFileDialogPrivateCall20)(const void *, int *);
typedef bool (*CuteQFileDialogPrivateCall21)(const void *, int *);
typedef bool (*CuteQFileDialogPrivateCall22)(const void *, int *);
class CuteQFileDialogPrivate : public QFileDialogPrivate {
public:
  using QFileDialogPrivate::QFileDialogPrivate;
  void *taken[23] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(dialog)
#if QT_CONFIG(filedialog)
    if (!std::strcmp(key, "_ZNK14QDialogPrivate17canBeNativeDialogEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(filedialog)
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10setVisibleEb")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(filedialog)
#if QT_CONFIG(dialog)
#if QT_CONFIG(filedialog)
    if (!std::strcmp(key, "_ZN14QDialogPrivate10initHelperEP21QPlatformDialogHelper")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
#if QT_CONFIG(filedialog)
    if (!std::strcmp(key, "_ZN14QDialogPrivate17helperPrepareShowEP21QPlatformDialogHelper")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
#if QT_CONFIG(filedialog)
    if (!std::strcmp(key, "_ZN14QDialogPrivate10helperDoneEN7QDialog10DialogCodeEP21QPlatformDialogHelper")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZN14QWidgetPrivate8recreateEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
    if (!std::strcmp(key, "_ZNK14QDialogPrivate10dialogCodeEv")) {
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
#if QT_CONFIG(filedialog)
  //  bool QFileDialogPrivate::canBeNativeDialog() const
  bool canBeNativeDialog() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQFileDialogPrivateCall0 call = reinterpret_cast<CuteQFileDialogPrivateCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFileDialogPrivate::canBeNativeDialog();
  }
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(filedialog)
  //  void QFileDialogPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[1]) {
      int handled = 0;
      CuteQFileDialogPrivateCall1 call = reinterpret_cast<CuteQFileDialogPrivateCall1>(taken[1]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QFileDialogPrivate::setVisible(visible);
  }
#endif  // QT_CONFIG(filedialog)

#if QT_CONFIG(dialog)
#if QT_CONFIG(filedialog)
  //  void QFileDialogPrivate::initHelper(QPlatformDialogHelper *a0)
  void initHelper(QPlatformDialogHelper *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQFileDialogPrivateCall2 call = reinterpret_cast<CuteQFileDialogPrivateCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFileDialogPrivate::initHelper(a0);
  }
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
#if QT_CONFIG(filedialog)
  //  void QFileDialogPrivate::helperPrepareShow(QPlatformDialogHelper *a0)
  void helperPrepareShow(QPlatformDialogHelper *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQFileDialogPrivateCall3 call = reinterpret_cast<CuteQFileDialogPrivateCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QFileDialogPrivate::helperPrepareShow(a0);
  }
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
#if QT_CONFIG(filedialog)
  //  void QFileDialogPrivate::helperDone(QDialog::DialogCode a0,
  //      QPlatformDialogHelper *a1)
  void helperDone(
      QDialog::DialogCode a0,
      QPlatformDialogHelper *a1) override {
    if (taken[4]) {
      int handled = 0;
      CuteQFileDialogPrivateCall4 call = reinterpret_cast<CuteQFileDialogPrivateCall4>(taken[4]);
      call(this, static_cast<int>(a0), a1, &handled);
      if (handled) return;
    }
    QFileDialogPrivate::helperDone(a0, a1);
  }
#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  void QDialogPrivate::recreate()
  void recreate() override {
    if (taken[5]) {
      int handled = 0;
      CuteQFileDialogPrivateCall5 call = reinterpret_cast<CuteQFileDialogPrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QDialogPrivate::recreate();
  }
#endif  // QT_CONFIG(dialog)

#if QT_CONFIG(dialog)
  //  int QDialogPrivate::dialogCode() const
  int dialogCode() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQFileDialogPrivateCall6 call = reinterpret_cast<CuteQFileDialogPrivateCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QDialogPrivate::dialogCode();
  }
#endif  // QT_CONFIG(dialog)

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[7]) {
      int handled = 0;
      CuteQFileDialogPrivateCall7 call = reinterpret_cast<CuteQFileDialogPrivateCall7>(taken[7]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[8]) {
      int handled = 0;
      CuteQFileDialogPrivateCall8 call = reinterpret_cast<CuteQFileDialogPrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[9]) {
      int handled = 0;
      CuteQFileDialogPrivateCall9 call = reinterpret_cast<CuteQFileDialogPrivateCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQFileDialogPrivateCall10 call = reinterpret_cast<CuteQFileDialogPrivateCall10>(taken[10]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQFileDialogPrivateCall11 call = reinterpret_cast<CuteQFileDialogPrivateCall11>(taken[11]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[12]) {
      int handled = 0;
      CuteQFileDialogPrivateCall12 call = reinterpret_cast<CuteQFileDialogPrivateCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[13]) {
      int handled = 0;
      CuteQFileDialogPrivateCall13 call = reinterpret_cast<CuteQFileDialogPrivateCall13>(taken[13]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[14]) {
      int handled = 0;
      CuteQFileDialogPrivateCall14 call = reinterpret_cast<CuteQFileDialogPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[15]) {
      int handled = 0;
      CuteQFileDialogPrivateCall15 call = reinterpret_cast<CuteQFileDialogPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[16]) {
      int handled = 0;
      CuteQFileDialogPrivateCall16 call = reinterpret_cast<CuteQFileDialogPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[17]) {
      int handled = 0;
      CuteQFileDialogPrivateCall17 call = reinterpret_cast<CuteQFileDialogPrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[18]) {
      int handled = 0;
      CuteQFileDialogPrivateCall18 call = reinterpret_cast<CuteQFileDialogPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[19]) {
      int handled = 0;
      CuteQFileDialogPrivateCall19 call = reinterpret_cast<CuteQFileDialogPrivateCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[20]) {
      int handled = 0;
      CuteQFileDialogPrivateCall20 call = reinterpret_cast<CuteQFileDialogPrivateCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[21]) {
      int handled = 0;
      CuteQFileDialogPrivateCall21 call = reinterpret_cast<CuteQFileDialogPrivateCall21>(taken[21]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[22]) {
      int handled = 0;
      CuteQFileDialogPrivateCall22 call = reinterpret_cast<CuteQFileDialogPrivateCall22>(taken[22]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QFileDialog *QFileDialogPrivate::q_func()
extern "C" Q_DECL_EXPORT
QFileDialog *ritual_ZN18QFileDialogPrivate6q_funcEv(
    QFileDialogPrivate *self) {
  return self->q_func();
}

//  const QFileDialog *QFileDialogPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QFileDialog *ritual_ZNK18QFileDialogPrivate6q_funcEv(
    const QFileDialogPrivate *self) {
  return self->q_func();
}

//  QFileDialogPrivate::QFileDialogPrivate()
extern "C" Q_DECL_EXPORT
QFileDialogPrivate *ritual_ZN18QFileDialogPrivateC1Ev() {
  return new CuteQFileDialogPrivate();
}

//  QPlatformFileDialogHelper *QFileDialogPrivate::platformFileDialogHelper()
//      const
extern "C" Q_DECL_EXPORT
QPlatformFileDialogHelper *ritual_ZNK18QFileDialogPrivate24platformFileDialogHelperEv(
    const QFileDialogPrivate *self) {
  return self->platformFileDialogHelper();
}

//  void QFileDialogPrivate::createToolButtons()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate17createToolButtonsEv(
    QFileDialogPrivate *self) {
  self->createToolButtons();
}

//  void QFileDialogPrivate::createMenuActions()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate17createMenuActionsEv(
    QFileDialogPrivate *self) {
  self->createMenuActions();
}

//  void QFileDialogPrivate::createWidgets()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate13createWidgetsEv(
    QFileDialogPrivate *self) {
  self->createWidgets();
}

//  void QFileDialogPrivate::init(const QFileDialogArgs &args)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate4initERK15QFileDialogArgs(
    QFileDialogPrivate *self,
    const QFileDialogArgs *args) {
  self->init(*args);
}

//  bool QFileDialogPrivate::itemViewKeyboardEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QFileDialogPrivate21itemViewKeyboardEventEP9QKeyEvent(
    QFileDialogPrivate *self,
    QKeyEvent *event) {
  return self->itemViewKeyboardEvent(event);
}

//  QString QFileDialogPrivate::getEnvironmentVariable(const QString &string)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QFileDialogPrivate22getEnvironmentVariableERK7QString(
    QFileDialogPrivate *self,
    const QString *string) {
  return new QString(self->getEnvironmentVariable(*string));
}

//  QStringList QFileDialogPrivate::typedFiles() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QFileDialogPrivate10typedFilesEv(
    const QFileDialogPrivate *self) {
  return new QList<QString>(self->typedFiles());
}

//  QList<QUrl> QFileDialogPrivate::userSelectedFiles() const
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZNK18QFileDialogPrivate17userSelectedFilesEv(
    const QFileDialogPrivate *self) {
  return new QList<QUrl>(self->userSelectedFiles());
}

//  QStringList QFileDialogPrivate::addDefaultSuffixToFiles(const QStringList
//      &filesToFix) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QFileDialogPrivate23addDefaultSuffixToFilesERK5QListI7QStringE(
    const QFileDialogPrivate *self,
    const QList<QString> *filesToFix) {
  return new QList<QString>(self->addDefaultSuffixToFiles(*filesToFix));
}

//  QList<QUrl> QFileDialogPrivate::addDefaultSuffixToUrls(const QList<QUrl>
//      &urlsToFix) const
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZNK18QFileDialogPrivate22addDefaultSuffixToUrlsERK5QListI4QUrlE(
    const QFileDialogPrivate *self,
    const QList<QUrl> *urlsToFix) {
  return new QList<QUrl>(self->addDefaultSuffixToUrls(*urlsToFix));
}

//  bool QFileDialogPrivate::removeDirectory(const QString &path)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QFileDialogPrivate15removeDirectoryERK7QString(
    QFileDialogPrivate *self,
    const QString *path) {
  return self->removeDirectory(*path);
}

//  void QFileDialogPrivate::setLabelTextControl(QFileDialog::DialogLabel
//      label, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate19setLabelTextControlEN11QFileDialog11DialogLabelERK7QString(
    QFileDialogPrivate *self,
    QFileDialog::DialogLabel label,
    const QString *text) {
  self->setLabelTextControl(label, *text);
}

//  void QFileDialogPrivate::updateLookInLabel()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate17updateLookInLabelEv(
    QFileDialogPrivate *self) {
  self->updateLookInLabel();
}

//  void QFileDialogPrivate::updateFileNameLabel()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate19updateFileNameLabelEv(
    QFileDialogPrivate *self) {
  self->updateFileNameLabel();
}

//  void QFileDialogPrivate::updateFileTypeLabel()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate19updateFileTypeLabelEv(
    QFileDialogPrivate *self) {
  self->updateFileTypeLabel();
}

//  void QFileDialogPrivate::updateOkButtonText(bool saveAsOnFolder)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate18updateOkButtonTextEb(
    QFileDialogPrivate *self,
    bool saveAsOnFolder) {
  self->updateOkButtonText(saveAsOnFolder);
}

//  void QFileDialogPrivate::updateCancelButtonText()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate22updateCancelButtonTextEv(
    QFileDialogPrivate *self) {
  self->updateCancelButtonText();
}

//  QModelIndex QFileDialogPrivate::mapToSource(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK18QFileDialogPrivate11mapToSourceERK11QModelIndex(
    const QFileDialogPrivate *self,
    const QModelIndex *index) {
  return new QModelIndex(self->mapToSource(*index));
}

//  QModelIndex QFileDialogPrivate::mapFromSource(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK18QFileDialogPrivate13mapFromSourceERK11QModelIndex(
    const QFileDialogPrivate *self,
    const QModelIndex *index) {
  return new QModelIndex(self->mapFromSource(*index));
}

//  QString QFileDialogPrivate::rootPath() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QFileDialogPrivate8rootPathEv(
    const QFileDialogPrivate *self) {
  return new QString(self->rootPath());
}

//  QLineEdit *QFileDialogPrivate::lineEdit() const
extern "C" Q_DECL_EXPORT
QLineEdit *ritual_ZNK18QFileDialogPrivate8lineEditEv(
    const QFileDialogPrivate *self) {
  return self->lineEdit();
}

//  long QFileDialogPrivate::maxNameLength(const QString &path)
extern "C" Q_DECL_EXPORT
long ritual_ZN18QFileDialogPrivate13maxNameLengthERK7QString(
    const QString *path) {
  return QFileDialogPrivate::maxNameLength(*path);
}

//  QString QFileDialogPrivate::basename(const QString &path) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QFileDialogPrivate8basenameERK7QString(
    const QFileDialogPrivate *self,
    const QString *path) {
  return new QString(self->basename(*path));
}

//  QDir::Filters QFileDialogPrivate::filterForMode(QDir::Filters filters)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QFileDialogPrivate13filterForModeE6QFlagsIN4QDir6FilterEE(
    const QFileDialogPrivate *self,
    int filters) {
  return static_cast<int>(
      self->filterForMode(
          QFlags<QDir::Filter>::fromInt(filters)).toInt());
}

//  QAbstractItemView *QFileDialogPrivate::currentView() const
extern "C" Q_DECL_EXPORT
QAbstractItemView *ritual_ZNK18QFileDialogPrivate11currentViewEv(
    const QFileDialogPrivate *self) {
  return self->currentView();
}

//  QString QFileDialogPrivate::toInternal(const QString &path)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QFileDialogPrivate10toInternalERK7QString(
    const QString *path) {
  return new QString(QFileDialogPrivate::toInternal(*path));
}

#if QT_CONFIG(settings)
//  void QFileDialogPrivate::saveSettings()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate12saveSettingsEv(
    QFileDialogPrivate *self) {
  self->saveSettings();
}
#endif  // QT_CONFIG(settings)

#if QT_CONFIG(settings)
//  bool QFileDialogPrivate::restoreFromSettings()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QFileDialogPrivate19restoreFromSettingsEv(
    QFileDialogPrivate *self) {
  return self->restoreFromSettings();
}
#endif  // QT_CONFIG(settings)

//  bool QFileDialogPrivate::restoreWidgetState(QStringList &history, int
//      splitterPosition)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QFileDialogPrivate18restoreWidgetStateER5QListI7QStringEi(
    QFileDialogPrivate *self,
    QStringList *history,
    int splitterPosition) {
  return self->restoreWidgetState(*history, splitterPosition);
}

//  void QFileDialogPrivate::setLastVisitedDirectory(const QUrl &dir)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate23setLastVisitedDirectoryERK4QUrl(
    const QUrl *dir) {
  QFileDialogPrivate::setLastVisitedDirectory(*dir);
}

//  void QFileDialogPrivate::retranslateWindowTitle()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate22retranslateWindowTitleEv(
    QFileDialogPrivate *self) {
  self->retranslateWindowTitle();
}

//  void QFileDialogPrivate::retranslateStrings()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate18retranslateStringsEv(
    QFileDialogPrivate *self) {
  self->retranslateStrings();
}

//  void QFileDialogPrivate::emitFilesSelected(const QStringList &files)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate17emitFilesSelectedERK5QListI7QStringE(
    QFileDialogPrivate *self,
    const QList<QString> *files) {
  self->emitFilesSelected(*files);
}

//  void QFileDialogPrivate::saveHistorySelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate20saveHistorySelectionEv(
    QFileDialogPrivate *self) {
  self->saveHistorySelection();
}

//  void QFileDialogPrivate::goHome()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate6goHomeEv(QFileDialogPrivate *self) {
  self->goHome();
}

//  void QFileDialogPrivate::pathChanged(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate11pathChangedERK7QString(
    QFileDialogPrivate *self,
    const QString *a0) {
  self->pathChanged(*a0);
}

//  void QFileDialogPrivate::navigate(HistoryItem &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate8navigateERNS_11HistoryItemE(
    QFileDialogPrivate *self,
    QFileDialogPrivate::HistoryItem *a0) {
  self->navigate(*a0);
}

//  void QFileDialogPrivate::navigateBackward()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate16navigateBackwardEv(
    QFileDialogPrivate *self) {
  self->navigateBackward();
}

//  void QFileDialogPrivate::navigateForward()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate15navigateForwardEv(
    QFileDialogPrivate *self) {
  self->navigateForward();
}

//  void QFileDialogPrivate::navigateToParent()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate16navigateToParentEv(
    QFileDialogPrivate *self) {
  self->navigateToParent();
}

//  void QFileDialogPrivate::createDirectory()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate15createDirectoryEv(
    QFileDialogPrivate *self) {
  self->createDirectory();
}

//  void QFileDialogPrivate::showListView()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate12showListViewEv(
    QFileDialogPrivate *self) {
  self->showListView();
}

//  void QFileDialogPrivate::showDetailsView()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate15showDetailsViewEv(
    QFileDialogPrivate *self) {
  self->showDetailsView();
}

//  void QFileDialogPrivate::showContextMenu(const QPoint &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate15showContextMenuERK6QPoint(
    QFileDialogPrivate *self,
    const QPoint *position) {
  self->showContextMenu(*position);
}

//  void QFileDialogPrivate::renameCurrent()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate13renameCurrentEv(
    QFileDialogPrivate *self) {
  self->renameCurrent();
}

//  void QFileDialogPrivate::deleteCurrent()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate13deleteCurrentEv(
    QFileDialogPrivate *self) {
  self->deleteCurrent();
}

//  void QFileDialogPrivate::showHidden()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate10showHiddenEv(QFileDialogPrivate *self) {
  self->showHidden();
}

//  void QFileDialogPrivate::showHeader(QAction *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate10showHeaderEP7QAction(
    QFileDialogPrivate *self,
    QAction *a0) {
  self->showHeader(a0);
}

//  void QFileDialogPrivate::updateOkButton()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate14updateOkButtonEv(
    QFileDialogPrivate *self) {
  self->updateOkButton();
}

//  void QFileDialogPrivate::currentChanged(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate14currentChangedERK11QModelIndex(
    QFileDialogPrivate *self,
    const QModelIndex *index) {
  self->currentChanged(*index);
}

//  void QFileDialogPrivate::enterDirectory(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate14enterDirectoryERK11QModelIndex(
    QFileDialogPrivate *self,
    const QModelIndex *index) {
  self->enterDirectory(*index);
}

//  void QFileDialogPrivate::emitUrlSelected(const QUrl &file)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate15emitUrlSelectedERK4QUrl(
    QFileDialogPrivate *self,
    const QUrl *file) {
  self->emitUrlSelected(*file);
}

//  void QFileDialogPrivate::emitUrlsSelected(const QList<QUrl> &files)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate16emitUrlsSelectedERK5QListI4QUrlE(
    QFileDialogPrivate *self,
    const QList<QUrl> *files) {
  self->emitUrlsSelected(*files);
}

//  void QFileDialogPrivate::nativeCurrentChanged(const QUrl &file)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate20nativeCurrentChangedERK4QUrl(
    QFileDialogPrivate *self,
    const QUrl *file) {
  self->nativeCurrentChanged(*file);
}

//  void QFileDialogPrivate::nativeEnterDirectory(const QUrl &directory)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate20nativeEnterDirectoryERK4QUrl(
    QFileDialogPrivate *self,
    const QUrl *directory) {
  self->nativeEnterDirectory(*directory);
}

//  void QFileDialogPrivate::goToDirectory(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate13goToDirectoryERK7QString(
    QFileDialogPrivate *self,
    const QString *a0) {
  self->goToDirectory(*a0);
}

//  void QFileDialogPrivate::useNameFilter(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate13useNameFilterEi(
    QFileDialogPrivate *self,
    int index) {
  self->useNameFilter(index);
}

//  void QFileDialogPrivate::selectionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate16selectionChangedEv(
    QFileDialogPrivate *self) {
  self->selectionChanged();
}

//  void QFileDialogPrivate::goToUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate7goToUrlERK4QUrl(
    QFileDialogPrivate *self,
    const QUrl *url) {
  self->goToUrl(*url);
}

//  void QFileDialogPrivate::autoCompleteFileName(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate20autoCompleteFileNameERK7QString(
    QFileDialogPrivate *self,
    const QString *a0) {
  self->autoCompleteFileName(*a0);
}

//  void QFileDialogPrivate::rowsInserted(const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate12rowsInsertedERK11QModelIndex(
    QFileDialogPrivate *self,
    const QModelIndex *parent) {
  self->rowsInserted(*parent);
}

//  void QFileDialogPrivate::fileRenamed(const QString &path, const QString
//      &oldName, const QString &newName)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate11fileRenamedERK7QStringS2_S2_(
    QFileDialogPrivate *self,
    const QString *path,
    const QString *oldName,
    const QString *newName) {
  self->fileRenamed(*path, *oldName, *newName);
}

//  bool QFileDialogPrivate::canBeNativeDialog() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QFileDialogPrivate17canBeNativeDialogEv(
    const QFileDialogPrivate *self) {
  return self->canBeNativeDialog();
}

//  void QFileDialogPrivate::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate10setVisibleEb(
    QFileDialogPrivate *self,
    bool visible) {
  self->setVisible(visible);
}

//  bool QFileDialogPrivate::usingWidgets() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QFileDialogPrivate12usingWidgetsEv(
    const QFileDialogPrivate *self) {
  return self->usingWidgets();
}

//  void QFileDialogPrivate::setDirectory_sys(const QUrl &directory)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate16setDirectory_sysERK4QUrl(
    QFileDialogPrivate *self,
    const QUrl *directory) {
  self->setDirectory_sys(*directory);
}

//  QUrl QFileDialogPrivate::directory_sys() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK18QFileDialogPrivate13directory_sysEv(
    const QFileDialogPrivate *self) {
  return new QUrl(self->directory_sys());
}

//  void QFileDialogPrivate::selectFile_sys(const QUrl &filename)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate14selectFile_sysERK4QUrl(
    QFileDialogPrivate *self,
    const QUrl *filename) {
  self->selectFile_sys(*filename);
}

//  QList<QUrl> QFileDialogPrivate::selectedFiles_sys() const
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZNK18QFileDialogPrivate17selectedFiles_sysEv(
    const QFileDialogPrivate *self) {
  return new QList<QUrl>(self->selectedFiles_sys());
}

//  void QFileDialogPrivate::setFilter_sys()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate13setFilter_sysEv(
    QFileDialogPrivate *self) {
  self->setFilter_sys();
}

//  void QFileDialogPrivate::selectMimeTypeFilter_sys(const QString &filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate24selectMimeTypeFilter_sysERK7QString(
    QFileDialogPrivate *self,
    const QString *filter) {
  self->selectMimeTypeFilter_sys(*filter);
}

//  QString QFileDialogPrivate::selectedMimeTypeFilter_sys() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QFileDialogPrivate26selectedMimeTypeFilter_sysEv(
    const QFileDialogPrivate *self) {
  return new QString(self->selectedMimeTypeFilter_sys());
}

//  void QFileDialogPrivate::selectNameFilter_sys(const QString &filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate20selectNameFilter_sysERK7QString(
    QFileDialogPrivate *self,
    const QString *filter) {
  self->selectNameFilter_sys(*filter);
}

//  QString QFileDialogPrivate::selectedNameFilter_sys() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QFileDialogPrivate22selectedNameFilter_sysEv(
    const QFileDialogPrivate *self) {
  return new QString(self->selectedNameFilter_sys());
}

//  QFileDialogPrivate::~QFileDialogPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivateD1Ev(QFileDialogPrivate *self) {
  delete self;
}

//  void QFileDialogPrivate::initHelper(QPlatformDialogHelper *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate10initHelperEP21QPlatformDialogHelper(
    QFileDialogPrivate *self,
    QPlatformDialogHelper *a0) {
  self->initHelper(a0);
}

//  void QFileDialogPrivate::helperPrepareShow(QPlatformDialogHelper *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate17helperPrepareShowEP21QPlatformDialogHelper(
    QFileDialogPrivate *self,
    QPlatformDialogHelper *a0) {
  self->helperPrepareShow(a0);
}

//  void QFileDialogPrivate::helperDone(QDialog::DialogCode a0,
//      QPlatformDialogHelper *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate10helperDoneEN7QDialog10DialogCodeEP21QPlatformDialogHelper(
    QFileDialogPrivate *self,
    QDialog::DialogCode a0,
    QPlatformDialogHelper *a1) {
  self->helperDone(a0, a1);
}

//  void QFileDialogPrivate::itemNotFound(const QString &fileName,
//      QFileDialog::FileMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFileDialogPrivate12itemNotFoundERK7QStringN11QFileDialog8FileModeE(
    QFileDialogPrivate *self,
    const QString *fileName,
    QFileDialog::FileMode mode) {
  self->itemNotFound(*fileName, mode);
}

//  bool QFileDialogPrivate::itemAlreadyExists(const QString &fileName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QFileDialogPrivate17itemAlreadyExistsERK7QString(
    QFileDialogPrivate *self,
    const QString *fileName) {
  return self->itemAlreadyExists(*fileName);
}

//  a Python function taken by a CuteQFileDialogPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFileDialogPrivate(
    QFileDialogPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFileDialogPrivate *>(self)->take(key, call);
}

//  bool QFileDialogPrivate::canBeNativeDialog() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK18QFileDialogPrivate17canBeNativeDialogEv(
    const QFileDialogPrivate *self) {
  return self->QFileDialogPrivate::canBeNativeDialog();
}

//  void QFileDialogPrivate::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QFileDialogPrivate10setVisibleEb(
    QFileDialogPrivate *self,
    bool visible) {
  self->QFileDialogPrivate::setVisible(visible);
}

//  void QFileDialogPrivate::initHelper(QPlatformDialogHelper *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QFileDialogPrivate10initHelperEP21QPlatformDialogHelper(
    QFileDialogPrivate *self,
    QPlatformDialogHelper *a0) {
  self->QFileDialogPrivate::initHelper(a0);
}

//  void QFileDialogPrivate::helperPrepareShow(QPlatformDialogHelper *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QFileDialogPrivate17helperPrepareShowEP21QPlatformDialogHelper(
    QFileDialogPrivate *self,
    QPlatformDialogHelper *a0) {
  self->QFileDialogPrivate::helperPrepareShow(a0);
}

//  void QFileDialogPrivate::helperDone(QDialog::DialogCode a0,
//      QPlatformDialogHelper *a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QFileDialogPrivate10helperDoneEN7QDialog10DialogCodeEP21QPlatformDialogHelper(
    QFileDialogPrivate *self,
    QDialog::DialogCode a0,
    QPlatformDialogHelper *a1) {
  self->QFileDialogPrivate::helperDone(a0, a1);
}

#endif  // QT_CONFIG(filedialog)
#endif  // QT_CONFIG(filedialog)
