//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qdialog_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qdialog.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qdialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <cstring>

//  Only a class built on QDialogPrivate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDialogPrivate : QDialogPrivate {
  using QDialogPrivate::dialogCode;
};

//  A QDialogPrivate that Python can take functions over in. Every QDialogPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(dialog)
typedef void (*CuteQDialogPrivateCall0)(const void *, bool, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef bool (*CuteQDialogPrivateCall1)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQDialogPrivateCall2)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef int (*CuteQDialogPrivateCall3)(const void *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQDialogPrivateCall4)(const void *, QPlatformDialogHelper *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQDialogPrivateCall5)(const void *, QPlatformDialogHelper *, int *);
#endif  // QT_CONFIG(dialog)
#if QT_CONFIG(dialog)
typedef void (*CuteQDialogPrivateCall6)(const void *, int, QPlatformDialogHelper *, int *);
#endif  // QT_CONFIG(dialog)
typedef void (*CuteQDialogPrivateCall7)(const void *, int, int *);
typedef void (*CuteQDialogPrivateCall8)(const void *, int *);
typedef void * (*CuteQDialogPrivateCall9)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQDialogPrivateCall10)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQDialogPrivateCall11)(const void *, int *);
typedef int (*CuteQDialogPrivateCall12)(const void *, int *);
typedef const QImage * (*CuteQDialogPrivateCall13)(const void *, int *);
typedef void (*CuteQDialogPrivateCall14)(const void *, int *);
typedef void (*CuteQDialogPrivateCall15)(const void *, int *);
typedef void (*CuteQDialogPrivateCall16)(const void *, int *);
typedef void (*CuteQDialogPrivateCall17)(const void *, int *);
typedef void (*CuteQDialogPrivateCall18)(const void *, int *);
typedef void (*CuteQDialogPrivateCall19)(const void *, int *);
typedef void (*CuteQDialogPrivateCall20)(const void *, int *);
typedef bool (*CuteQDialogPrivateCall21)(const void *, int *);
typedef bool (*CuteQDialogPrivateCall22)(const void *, int *);
class CuteQDialogPrivate : public QDialogPrivate {
public:
  using QDialogPrivate::QDialogPrivate;
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
      CuteQDialogPrivateCall0 call = reinterpret_cast<CuteQDialogPrivateCall0>(taken[0]);
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
      CuteQDialogPrivateCall1 call = reinterpret_cast<CuteQDialogPrivateCall1>(taken[1]);
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
      CuteQDialogPrivateCall2 call = reinterpret_cast<CuteQDialogPrivateCall2>(taken[2]);
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
      CuteQDialogPrivateCall3 call = reinterpret_cast<CuteQDialogPrivateCall3>(taken[3]);
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
      CuteQDialogPrivateCall4 call = reinterpret_cast<CuteQDialogPrivateCall4>(taken[4]);
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
      CuteQDialogPrivateCall5 call = reinterpret_cast<CuteQDialogPrivateCall5>(taken[5]);
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
      CuteQDialogPrivateCall6 call = reinterpret_cast<CuteQDialogPrivateCall6>(taken[6]);
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
      CuteQDialogPrivateCall7 call = reinterpret_cast<CuteQDialogPrivateCall7>(taken[7]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[8]) {
      int handled = 0;
      CuteQDialogPrivateCall8 call = reinterpret_cast<CuteQDialogPrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[9]) {
      int handled = 0;
      CuteQDialogPrivateCall9 call = reinterpret_cast<CuteQDialogPrivateCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQDialogPrivateCall10 call = reinterpret_cast<CuteQDialogPrivateCall10>(taken[10]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQDialogPrivateCall11 call = reinterpret_cast<CuteQDialogPrivateCall11>(taken[11]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[12]) {
      int handled = 0;
      CuteQDialogPrivateCall12 call = reinterpret_cast<CuteQDialogPrivateCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[13]) {
      int handled = 0;
      CuteQDialogPrivateCall13 call = reinterpret_cast<CuteQDialogPrivateCall13>(taken[13]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[14]) {
      int handled = 0;
      CuteQDialogPrivateCall14 call = reinterpret_cast<CuteQDialogPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[15]) {
      int handled = 0;
      CuteQDialogPrivateCall15 call = reinterpret_cast<CuteQDialogPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[16]) {
      int handled = 0;
      CuteQDialogPrivateCall16 call = reinterpret_cast<CuteQDialogPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[17]) {
      int handled = 0;
      CuteQDialogPrivateCall17 call = reinterpret_cast<CuteQDialogPrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[18]) {
      int handled = 0;
      CuteQDialogPrivateCall18 call = reinterpret_cast<CuteQDialogPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[19]) {
      int handled = 0;
      CuteQDialogPrivateCall19 call = reinterpret_cast<CuteQDialogPrivateCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[20]) {
      int handled = 0;
      CuteQDialogPrivateCall20 call = reinterpret_cast<CuteQDialogPrivateCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[21]) {
      int handled = 0;
      CuteQDialogPrivateCall21 call = reinterpret_cast<CuteQDialogPrivateCall21>(taken[21]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[22]) {
      int handled = 0;
      CuteQDialogPrivateCall22 call = reinterpret_cast<CuteQDialogPrivateCall22>(taken[22]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QDialog *QDialogPrivate::q_func()
extern "C" Q_DECL_EXPORT
QDialog *ritual_ZN14QDialogPrivate6q_funcEv(QDialogPrivate *self) {
  return self->q_func();
}

//  const QDialog *QDialogPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QDialog *ritual_ZNK14QDialogPrivate6q_funcEv(
    const QDialogPrivate *self) {
  return self->q_func();
}

//  QDialogPrivate::QDialogPrivate()
extern "C" Q_DECL_EXPORT
QDialogPrivate *ritual_ZN14QDialogPrivateC1Ev() {
  return new CuteQDialogPrivate();
}

//  QDialogPrivate::~QDialogPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDialogPrivateD1Ev(QDialogPrivate *self) {
  delete self;
}

//  void QDialogPrivate::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDialogPrivate10setVisibleEb(
    QDialogPrivate *self,
    bool visible) {
  self->setVisible(visible);
}

//  QWindow *QDialogPrivate::transientParentWindow() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK14QDialogPrivate21transientParentWindowEv(
    const QDialogPrivate *self) {
  return self->transientParentWindow();
}

//  bool QDialogPrivate::setNativeDialogVisible(bool visible)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QDialogPrivate22setNativeDialogVisibleEb(
    QDialogPrivate *self,
    bool visible) {
  return self->setNativeDialogVisible(visible);
}

//  QVariant QDialogPrivate::styleHint(QPlatformDialogHelper::StyleHint hint)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QDialogPrivate9styleHintEN21QPlatformDialogHelper9StyleHintE(
    const QDialogPrivate *self,
    QPlatformDialogHelper::StyleHint hint) {
  return new QVariant(self->styleHint(hint));
}

#if QT_CONFIG(pushbutton)
//  void QDialogPrivate::setDefault(QPushButton *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDialogPrivate10setDefaultEP11QPushButton(
    QDialogPrivate *self,
    QPushButton *a0) {
  self->setDefault(a0);
}
#endif  // QT_CONFIG(pushbutton)

#if QT_CONFIG(pushbutton)
//  void QDialogPrivate::setMainDefault(QPushButton *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDialogPrivate14setMainDefaultEP11QPushButton(
    QDialogPrivate *self,
    QPushButton *a0) {
  self->setMainDefault(a0);
}
#endif  // QT_CONFIG(pushbutton)

#if QT_CONFIG(pushbutton)
//  void QDialogPrivate::hideDefault()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDialogPrivate11hideDefaultEv(QDialogPrivate *self) {
  self->hideDefault();
}
#endif  // QT_CONFIG(pushbutton)

//  void QDialogPrivate::resetModalitySetByOpen()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDialogPrivate22resetModalitySetByOpenEv(
    QDialogPrivate *self) {
  self->resetModalitySetByOpen();
}

//  QPlatformDialogHelper *QDialogPrivate::platformHelper() const
extern "C" Q_DECL_EXPORT
QPlatformDialogHelper *ritual_ZNK14QDialogPrivate14platformHelperEv(
    const QDialogPrivate *self) {
  return self->platformHelper();
}

//  bool QDialogPrivate::canBeNativeDialog() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QDialogPrivate17canBeNativeDialogEv(
    const QDialogPrivate *self) {
  return self->canBeNativeDialog();
}

//  void QDialogPrivate::close(int resultCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDialogPrivate5closeEi(
    QDialogPrivate *self,
    int resultCode) {
  self->close(resultCode);
}

//  void QDialogPrivate::recreate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDialogPrivate8recreateEv(QDialogPrivate *self) {
  self->recreate();
}

//  int QDialogPrivate::dialogCode() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QDialogPrivate10dialogCodeEv(const QDialogPrivate *self) {
  return self->dialogCode();
}

//  void QDialogPrivate::initHelper(QPlatformDialogHelper *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDialogPrivate10initHelperEP21QPlatformDialogHelper(
    QDialogPrivate *self,
    QPlatformDialogHelper *a0) {
  self->initHelper(a0);
}

//  void QDialogPrivate::helperPrepareShow(QPlatformDialogHelper *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDialogPrivate17helperPrepareShowEP21QPlatformDialogHelper(
    QDialogPrivate *self,
    QPlatformDialogHelper *a0) {
  self->helperPrepareShow(a0);
}

//  void QDialogPrivate::helperDone(QDialog::DialogCode a0,
//      QPlatformDialogHelper *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDialogPrivate10helperDoneEN7QDialog10DialogCodeEP21QPlatformDialogHelper(
    QDialogPrivate *self,
    QDialog::DialogCode a0,
    QPlatformDialogHelper *a1) {
  self->helperDone(a0, a1);
}

//  a Python function taken by a CuteQDialogPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDialogPrivate(
    QDialogPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDialogPrivate *>(self)->take(key, call);
}

//  void QDialogPrivate::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QDialogPrivate10setVisibleEb(
    QDialogPrivate *self,
    bool visible) {
  self->QDialogPrivate::setVisible(visible);
}

//  bool QDialogPrivate::canBeNativeDialog() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QDialogPrivate17canBeNativeDialogEv(
    const QDialogPrivate *self) {
  return self->QDialogPrivate::canBeNativeDialog();
}

//  void QDialogPrivate::recreate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QDialogPrivate8recreateEv(QDialogPrivate *self) {
  self->QDialogPrivate::recreate();
}

//  int QDialogPrivate::dialogCode() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK14QDialogPrivate10dialogCodeEv(
    const QDialogPrivate *self) {
  return static_cast<const OwnQDialogPrivate *>(self)->OwnQDialogPrivate::dialogCode();
}

//  void QDialogPrivate::initHelper(QPlatformDialogHelper *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QDialogPrivate10initHelperEP21QPlatformDialogHelper(
    QDialogPrivate *self,
    QPlatformDialogHelper *a0) {
  self->QDialogPrivate::initHelper(a0);
}

//  void QDialogPrivate::helperPrepareShow(QPlatformDialogHelper *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QDialogPrivate17helperPrepareShowEP21QPlatformDialogHelper(
    QDialogPrivate *self,
    QPlatformDialogHelper *a0) {
  self->QDialogPrivate::helperPrepareShow(a0);
}

//  void QDialogPrivate::helperDone(QDialog::DialogCode a0,
//      QPlatformDialogHelper *a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QDialogPrivate10helperDoneEN7QDialog10DialogCodeEP21QPlatformDialogHelper(
    QDialogPrivate *self,
    QDialog::DialogCode a0,
    QPlatformDialogHelper *a1) {
  self->QDialogPrivate::helperDone(a0, a1);
}

#endif  // QT_CONFIG(dialog)
#endif  // QT_CONFIG(dialog)
