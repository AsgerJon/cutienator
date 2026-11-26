//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h, Qt 6.12.0. Edited by hand
//  on 2026-11-25: added by hand, instances of templates of the class: 1.
//  Kept as it is when the generator runs again.
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qwidget.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtGui/qpalette.h>
#include <QtGui/qregion.h>
#include <QtGui/qfont.h>
#include <QtCore/qlocale.h>
#include <QtGui/qbrush.h>
#include <QtCore/qobject.h>
#include <QtCore/qsize.h>
#include <QtCore/qstring.h>
#include <QtGui/qcursor.h>
#include <QtCore/qmargins.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <string>

//  A QWidgetPrivate that Python can take functions over in. Every QWidgetPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWidgetPrivateCall0)(const void *, bool, int *);
typedef void (*CuteQWidgetPrivateCall1)(const void *, int, int *);
typedef void (*CuteQWidgetPrivateCall2)(const void *, int *);
typedef void (*CuteQWidgetPrivateCall3)(const void *, int *);
typedef void * (*CuteQWidgetPrivateCall4)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQWidgetPrivateCall5)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQWidgetPrivateCall6)(const void *, int *);
typedef int (*CuteQWidgetPrivateCall7)(const void *, int *);
typedef const QImage * (*CuteQWidgetPrivateCall8)(const void *, int *);
typedef void (*CuteQWidgetPrivateCall9)(const void *, int *);
typedef void (*CuteQWidgetPrivateCall10)(const void *, int *);
typedef void (*CuteQWidgetPrivateCall11)(const void *, int *);
typedef void (*CuteQWidgetPrivateCall12)(const void *, int *);
typedef void (*CuteQWidgetPrivateCall13)(const void *, int *);
typedef void (*CuteQWidgetPrivateCall14)(const void *, int *);
typedef void (*CuteQWidgetPrivateCall15)(const void *, int *);
typedef bool (*CuteQWidgetPrivateCall16)(const void *, int *);
typedef bool (*CuteQWidgetPrivateCall17)(const void *, int *);
class CuteQWidgetPrivate : public QWidgetPrivate {
public:
  using QWidgetPrivate::QWidgetPrivate;
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
      CuteQWidgetPrivateCall0 call = reinterpret_cast<CuteQWidgetPrivateCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWidgetPrivateCall1 call = reinterpret_cast<CuteQWidgetPrivateCall1>(taken[1]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[2]) {
      int handled = 0;
      CuteQWidgetPrivateCall2 call = reinterpret_cast<CuteQWidgetPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[3]) {
      int handled = 0;
      CuteQWidgetPrivateCall3 call = reinterpret_cast<CuteQWidgetPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[4]) {
      int handled = 0;
      CuteQWidgetPrivateCall4 call = reinterpret_cast<CuteQWidgetPrivateCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQWidgetPrivateCall5 call = reinterpret_cast<CuteQWidgetPrivateCall5>(taken[5]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQWidgetPrivateCall6 call = reinterpret_cast<CuteQWidgetPrivateCall6>(taken[6]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[7]) {
      int handled = 0;
      CuteQWidgetPrivateCall7 call = reinterpret_cast<CuteQWidgetPrivateCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[8]) {
      int handled = 0;
      CuteQWidgetPrivateCall8 call = reinterpret_cast<CuteQWidgetPrivateCall8>(taken[8]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[9]) {
      int handled = 0;
      CuteQWidgetPrivateCall9 call = reinterpret_cast<CuteQWidgetPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[10]) {
      int handled = 0;
      CuteQWidgetPrivateCall10 call = reinterpret_cast<CuteQWidgetPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[11]) {
      int handled = 0;
      CuteQWidgetPrivateCall11 call = reinterpret_cast<CuteQWidgetPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[12]) {
      int handled = 0;
      CuteQWidgetPrivateCall12 call = reinterpret_cast<CuteQWidgetPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[13]) {
      int handled = 0;
      CuteQWidgetPrivateCall13 call = reinterpret_cast<CuteQWidgetPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[14]) {
      int handled = 0;
      CuteQWidgetPrivateCall14 call = reinterpret_cast<CuteQWidgetPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[15]) {
      int handled = 0;
      CuteQWidgetPrivateCall15 call = reinterpret_cast<CuteQWidgetPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[16]) {
      int handled = 0;
      CuteQWidgetPrivateCall16 call = reinterpret_cast<CuteQWidgetPrivateCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[17]) {
      int handled = 0;
      CuteQWidgetPrivateCall17 call = reinterpret_cast<CuteQWidgetPrivateCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QWidget *QWidgetPrivate::q_func()
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN14QWidgetPrivate6q_funcEv(QWidgetPrivate *self) {
  return self->q_func();
}

//  const QWidget *QWidgetPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QWidget *ritual_ZNK14QWidgetPrivate6q_funcEv(
    const QWidgetPrivate *self) {
  return self->q_func();
}

//  QWidgetPrivate::QWidgetPrivate(decltype(QObjectPrivateVersion) a0)
extern "C" Q_DECL_EXPORT
QWidgetPrivate *ritual_ZN14QWidgetPrivateC1E16QtPrivate_6_12_0(
    decltype(QObjectPrivateVersion) a0) {
  return new CuteQWidgetPrivate(a0);
}

//  QWidgetPrivate::~QWidgetPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivateD1Ev(QWidgetPrivate *self) {
  delete self;
}

//  QWidgetPrivate *QWidgetPrivate::get(QWidget *w)
extern "C" Q_DECL_EXPORT
QWidgetPrivate *ritual_ZN14QWidgetPrivate3getEP7QWidget(QWidget *w) {
  return QWidgetPrivate::get(w);
}

//  const QWidgetPrivate *QWidgetPrivate::get(const QWidget *w)
extern "C" Q_DECL_EXPORT
const QWidgetPrivate *ritual_ZN14QWidgetPrivate3getEPK7QWidget(
    const QWidget *w) {
  return QWidgetPrivate::get(w);
}

//  void QWidgetPrivate::checkRestoredGeometry(const QRect
//      &availableGeometry, QRect *restoredGeometry, int frameHeight)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate21checkRestoredGeometryERK5QRectPS0_i(
    const QRect *availableGeometry,
    QRect *restoredGeometry,
    int frameHeight) {
  QWidgetPrivate::checkRestoredGeometry(
      *availableGeometry,
      restoredGeometry,
      frameHeight);
}

//  QWExtra *QWidgetPrivate::extraData() const
extern "C" Q_DECL_EXPORT
QWExtra *ritual_ZNK14QWidgetPrivate9extraDataEv(const QWidgetPrivate *self) {
  return self->extraData();
}

//  QTLWExtra *QWidgetPrivate::topData() const
extern "C" Q_DECL_EXPORT
QTLWExtra *ritual_ZNK14QWidgetPrivate7topDataEv(const QWidgetPrivate *self) {
  return self->topData();
}

//  QTLWExtra *QWidgetPrivate::maybeTopData() const
extern "C" Q_DECL_EXPORT
QTLWExtra *ritual_ZNK14QWidgetPrivate12maybeTopDataEv(
    const QWidgetPrivate *self) {
  return self->maybeTopData();
}

//  QPainter *QWidgetPrivate::sharedPainter() const
extern "C" Q_DECL_EXPORT
QPainter *ritual_ZNK14QWidgetPrivate13sharedPainterEv(
    const QWidgetPrivate *self) {
  return self->sharedPainter();
}

//  void QWidgetPrivate::setSharedPainter(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate16setSharedPainterEP8QPainter(
    QWidgetPrivate *self,
    QPainter *painter) {
  self->setSharedPainter(painter);
}

//  QWidgetRepaintManager *QWidgetPrivate::maybeRepaintManager() const
extern "C" Q_DECL_EXPORT
QWidgetRepaintManager *ritual_ZNK14QWidgetPrivate19maybeRepaintManagerEv(
    const QWidgetPrivate *self) {
  return self->maybeRepaintManager();
}

//  QRhi *QWidgetPrivate::rhi() const
extern "C" Q_DECL_EXPORT
QRhi *ritual_ZNK14QWidgetPrivate3rhiEv(const QWidgetPrivate *self) {
  return self->rhi();
}

//  QWindow *QWidgetPrivate::windowHandle(WindowHandleMode mode) const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK14QWidgetPrivate12windowHandleENS_16WindowHandleModeE(
    const QWidgetPrivate *self,
    QWidgetPrivate::WindowHandleMode mode) {
  return self->windowHandle(mode);
}

//  QWindow *QWidgetPrivate::_q_closestWindowHandle() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK14QWidgetPrivate22_q_closestWindowHandleEv(
    const QWidgetPrivate *self) {
  return self->_q_closestWindowHandle();
}

//  QScreen *QWidgetPrivate::associatedScreen() const
extern "C" Q_DECL_EXPORT
QScreen *ritual_ZNK14QWidgetPrivate16associatedScreenEv(
    const QWidgetPrivate *self) {
  return self->associatedScreen();
}

//  void QWidgetPrivate::init(QWidget *desktopWidget, Qt::WindowFlags f)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate4initEP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidgetPrivate *self,
    QWidget *desktopWidget,
    int f) {
  self->init(desktopWidget, QFlags<Qt::WindowType>::fromInt(f));
}

//  void QWidgetPrivate::create()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate6createEv(QWidgetPrivate *self) {
  self->create();
}

//  void QWidgetPrivate::createRecursively()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate17createRecursivelyEv(QWidgetPrivate *self) {
  self->createRecursively();
}

//  void QWidgetPrivate::createWinId()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate11createWinIdEv(QWidgetPrivate *self) {
  self->createWinId();
}

//  bool QWidgetPrivate::setScreenForPoint(const QPoint &pos)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QWidgetPrivate17setScreenForPointERK6QPoint(
    QWidgetPrivate *self,
    const QPoint *pos) {
  return self->setScreenForPoint(*pos);
}

//  bool QWidgetPrivate::setScreen(QScreen *screen)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QWidgetPrivate9setScreenEP7QScreen(
    QWidgetPrivate *self,
    QScreen *screen) {
  return self->setScreen(screen);
}

//  void QWidgetPrivate::createTLExtra()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate13createTLExtraEv(QWidgetPrivate *self) {
  self->createTLExtra();
}

//  void QWidgetPrivate::createExtra()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate11createExtraEv(QWidgetPrivate *self) {
  self->createExtra();
}

//  void QWidgetPrivate::deleteExtra()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate11deleteExtraEv(QWidgetPrivate *self) {
  self->deleteExtra();
}

//  void QWidgetPrivate::createSysExtra()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate14createSysExtraEv(QWidgetPrivate *self) {
  self->createSysExtra();
}

//  void QWidgetPrivate::deleteSysExtra()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate14deleteSysExtraEv(QWidgetPrivate *self) {
  self->deleteSysExtra();
}

//  void QWidgetPrivate::createTLSysExtra()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate16createTLSysExtraEv(QWidgetPrivate *self) {
  self->createTLSysExtra();
}

//  void QWidgetPrivate::deleteTLSysExtra()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate16deleteTLSysExtraEv(QWidgetPrivate *self) {
  self->deleteTLSysExtra();
}

//  void QWidgetPrivate::updateSystemBackground()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate22updateSystemBackgroundEv(
    QWidgetPrivate *self) {
  self->updateSystemBackground();
}

//  void QWidgetPrivate::propagatePaletteChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate22propagatePaletteChangeEv(
    QWidgetPrivate *self) {
  self->propagatePaletteChange();
}

//  void QWidgetPrivate::setPalette_helper(const QPalette &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate17setPalette_helperERK8QPalette(
    QWidgetPrivate *self,
    const QPalette *a0) {
  self->setPalette_helper(*a0);
}

//  void QWidgetPrivate::resolvePalette()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate14resolvePaletteEv(QWidgetPrivate *self) {
  self->resolvePalette();
}

//  QPalette QWidgetPrivate::naturalWidgetPalette(QPalette::ResolveMask
//      inheritedMask) const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK14QWidgetPrivate20naturalWidgetPaletteEy(
    const QWidgetPrivate *self,
    QPalette::ResolveMask inheritedMask) {
  return new QPalette(self->naturalWidgetPalette(inheritedMask));
}

//  void QWidgetPrivate::setMask_sys(const QRegion &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate11setMask_sysERK7QRegion(
    QWidgetPrivate *self,
    const QRegion *a0) {
  self->setMask_sys(*a0);
}

//  void QWidgetPrivate::raise_sys()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate9raise_sysEv(QWidgetPrivate *self) {
  self->raise_sys();
}

//  void QWidgetPrivate::lower_sys()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate9lower_sysEv(QWidgetPrivate *self) {
  self->lower_sys();
}

//  void QWidgetPrivate::stackUnder_sys(QWidget *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate14stackUnder_sysEP7QWidget(
    QWidgetPrivate *self,
    QWidget *a0) {
  self->stackUnder_sys(a0);
}

//  QWidget *QWidgetPrivate::deepestFocusProxy() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK14QWidgetPrivate17deepestFocusProxyEv(
    const QWidgetPrivate *self) {
  return self->deepestFocusProxy();
}

//  void QWidgetPrivate::setFocus_sys()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate12setFocus_sysEv(QWidgetPrivate *self) {
  self->setFocus_sys();
}

//  void QWidgetPrivate::updateFocusChild()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate16updateFocusChildEv(QWidgetPrivate *self) {
  self->updateFocusChild();
}

//  void QWidgetPrivate::updateFont(const QFont &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate10updateFontERK5QFont(
    QWidgetPrivate *self,
    const QFont *a0) {
  self->updateFont(*a0);
}

//  void QWidgetPrivate::setFont_helper(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate14setFont_helperERK5QFont(
    QWidgetPrivate *self,
    const QFont *font) {
  self->setFont_helper(*font);
}

//  QFont QWidgetPrivate::localFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QWidgetPrivate9localFontEv(const QWidgetPrivate *self) {
  return new QFont(self->localFont());
}

//  void QWidgetPrivate::resolveFont()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate11resolveFontEv(QWidgetPrivate *self) {
  self->resolveFont();
}

//  QFont QWidgetPrivate::naturalWidgetFont(uint inheritedMask) const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QWidgetPrivate17naturalWidgetFontEj(
    const QWidgetPrivate *self,
    uint inheritedMask) {
  return new QFont(self->naturalWidgetFont(inheritedMask));
}

//  void QWidgetPrivate::setLayoutDirection_helper(Qt::LayoutDirection a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate25setLayoutDirection_helperEN2Qt15LayoutDirectionE(
    QWidgetPrivate *self,
    Qt::LayoutDirection a0) {
  self->setLayoutDirection_helper(a0);
}

//  void QWidgetPrivate::resolveLayoutDirection()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate22resolveLayoutDirectionEv(
    QWidgetPrivate *self) {
  self->resolveLayoutDirection();
}

//  void QWidgetPrivate::setLocale_helper(const QLocale &l, bool forceUpdate)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate16setLocale_helperERK7QLocaleb(
    QWidgetPrivate *self,
    const QLocale *l,
    bool forceUpdate) {
  self->setLocale_helper(*l, forceUpdate);
}

//  void QWidgetPrivate::resolveLocale()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate13resolveLocaleEv(QWidgetPrivate *self) {
  self->resolveLocale();
}

//  void QWidgetPrivate::setStyle_helper(QStyle *newStyle, bool propagate)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate15setStyle_helperEP6QStyleb(
    QWidgetPrivate *self,
    QStyle *newStyle,
    bool propagate) {
  self->setStyle_helper(newStyle, propagate);
}

//  void QWidgetPrivate::inheritStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate12inheritStyleEv(QWidgetPrivate *self) {
  self->inheritStyle();
}

//  void QWidgetPrivate::setUpdatesEnabled_helper(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate24setUpdatesEnabled_helperEb(
    QWidgetPrivate *self,
    bool a0) {
  self->setUpdatesEnabled_helper(a0);
}

//  bool QWidgetPrivate::updateBrushOrigin(QPainter *a0, const QBrush &brush)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QWidgetPrivate17updateBrushOriginEP8QPainterRK6QBrush(
    const QWidgetPrivate *self,
    QPainter *a0,
    const QBrush *brush) {
  return self->updateBrushOrigin(a0, *brush);
}

//  void QWidgetPrivate::paintBackground(QPainter *a0, const QRegion &a1,
//      DrawWidgetFlags flags) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QWidgetPrivate15paintBackgroundEP8QPainterRK7QRegion6QFlagsINS_14DrawWidgetFlagEE(
    const QWidgetPrivate *self,
    QPainter *a0,
    const QRegion *a1,
    int flags) {
  self->paintBackground(
      a0,
      *a1,
      QFlags<QWidgetPrivate::DrawWidgetFlag>::fromInt(flags));
}

//  bool QWidgetPrivate::isAboutToShow() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QWidgetPrivate13isAboutToShowEv(
    const QWidgetPrivate *self) {
  return self->isAboutToShow();
}

//  QRegion QWidgetPrivate::prepareToRender(const QRegion &region,
//      QWidget::RenderFlags renderFlags)
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZN14QWidgetPrivate15prepareToRenderERK7QRegion6QFlagsIN7QWidget10RenderFlagEE(
    QWidgetPrivate *self,
    const QRegion *region,
    int renderFlags) {
  return new QRegion(
      self->prepareToRender(
          *region,
          QFlags<QWidget::RenderFlag>::fromInt(renderFlags)));
}

//  void QWidgetPrivate::render_helper(QPainter *painter, const QPoint
//      &targetOffset, const QRegion &sourceRegion, QWidget::RenderFlags
//      renderFlags)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate13render_helperEP8QPainterRK6QPointRK7QRegion6QFlagsIN7QWidget10RenderFlagEE(
    QWidgetPrivate *self,
    QPainter *painter,
    const QPoint *targetOffset,
    const QRegion *sourceRegion,
    int renderFlags) {
  self->render_helper(
      painter,
      *targetOffset,
      *sourceRegion,
      QFlags<QWidget::RenderFlag>::fromInt(renderFlags));
}

//  void QWidgetPrivate::render(QPaintDevice *target, const QPoint
//      &targetOffset, const QRegion &sourceRegion, QWidget::RenderFlags
//      renderFlags)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate6renderEP12QPaintDeviceRK6QPointRK7QRegion6QFlagsIN7QWidget10RenderFlagEE(
    QWidgetPrivate *self,
    QPaintDevice *target,
    const QPoint *targetOffset,
    const QRegion *sourceRegion,
    int renderFlags) {
  self->render(
      target,
      *targetOffset,
      *sourceRegion,
      QFlags<QWidget::RenderFlag>::fromInt(renderFlags));
}

//  void QWidgetPrivate::drawWidget(QPaintDevice *pdev, const QRegion &rgn,
//      const QPoint &offset, DrawWidgetFlags flags, QPainter *sharedPainter,
//      QWidgetRepaintManager *repaintManager)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate10drawWidgetEP12QPaintDeviceRK7QRegionRK6QPoint6QFlagsINS_14DrawWidgetFlagEEP8QPainterP21QWidgetRepaintManager(
    QWidgetPrivate *self,
    QPaintDevice *pdev,
    const QRegion *rgn,
    const QPoint *offset,
    int flags,
    QPainter *sharedPainter,
    QWidgetRepaintManager *repaintManager) {
  self->drawWidget(
      pdev,
      *rgn,
      *offset,
      QFlags<QWidgetPrivate::DrawWidgetFlag>::fromInt(flags),
      sharedPainter,
      repaintManager);
}

//  void QWidgetPrivate::sendPaintEvent(const QRegion &toBePainted)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate14sendPaintEventERK7QRegion(
    QWidgetPrivate *self,
    const QRegion *toBePainted) {
  self->sendPaintEvent(*toBePainted);
}

//  void QWidgetPrivate::paintSiblingsRecursive(QPaintDevice *pdev, const
//      QObjectList &children, int index, const QRegion &rgn, const QPoint
//      &offset, DrawWidgetFlags flags, QPainter *sharedPainter,
//      QWidgetRepaintManager *repaintManager)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate22paintSiblingsRecursiveEP12QPaintDeviceRK5QListIP7QObjectEiRK7QRegionRK6QPoint6QFlagsINS_14DrawWidgetFlagEEP8QPainterP21QWidgetRepaintManager(
    QWidgetPrivate *self,
    QPaintDevice *pdev,
    const QList<QObject *> *children,
    int index,
    const QRegion *rgn,
    const QPoint *offset,
    int flags,
    QPainter *sharedPainter,
    QWidgetRepaintManager *repaintManager) {
  self->paintSiblingsRecursive(
      pdev,
      *children,
      index,
      *rgn,
      *offset,
      QFlags<QWidgetPrivate::DrawWidgetFlag>::fromInt(flags),
      sharedPainter,
      repaintManager);
}

#if QT_CONFIG(graphicsview)
//  QGraphicsProxyWidget *QWidgetPrivate::nearestGraphicsProxyWidget(const
//      QWidget *origin)
extern "C" Q_DECL_EXPORT
QGraphicsProxyWidget *ritual_ZN14QWidgetPrivate26nearestGraphicsProxyWidgetEPK7QWidget(
    const QWidget *origin) {
  return QWidgetPrivate::nearestGraphicsProxyWidget(origin);
}
#endif  // QT_CONFIG(graphicsview)

//  bool QWidgetPrivate::shouldPaintOnScreen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QWidgetPrivate19shouldPaintOnScreenEv(
    const QWidgetPrivate *self) {
  return self->shouldPaintOnScreen();
}

//  void QWidgetPrivate::paintOnScreen(const QRegion &rgn)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate13paintOnScreenERK7QRegion(
    QWidgetPrivate *self,
    const QRegion *rgn) {
  self->paintOnScreen(*rgn);
}

//  QRect QWidgetPrivate::clipRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK14QWidgetPrivate8clipRectEv(const QWidgetPrivate *self) {
  return new QRect(self->clipRect());
}

//  QRegion QWidgetPrivate::clipRegion() const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK14QWidgetPrivate10clipRegionEv(
    const QWidgetPrivate *self) {
  return new QRegion(self->clipRegion());
}

//  void QWidgetPrivate::setSystemClip(QPaintEngine *paintEngine, qreal
//      devicePixelRatio, const QRegion &region)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate13setSystemClipEP12QPaintEnginedRK7QRegion(
    QWidgetPrivate *self,
    QPaintEngine *paintEngine,
    qreal devicePixelRatio,
    const QRegion *region) {
  self->setSystemClip(paintEngine, devicePixelRatio, *region);
}

//  void QWidgetPrivate::subtractOpaqueChildren(QRegion &rgn, const QRect
//      &clipRect) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QWidgetPrivate22subtractOpaqueChildrenER7QRegionRK5QRect(
    const QWidgetPrivate *self,
    QRegion *rgn,
    const QRect *clipRect) {
  self->subtractOpaqueChildren(*rgn, *clipRect);
}

//  void QWidgetPrivate::subtractOpaqueSiblings(QRegion &source, bool
//      *hasDirtySiblingsAbove, bool alsoNonOpaque) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QWidgetPrivate22subtractOpaqueSiblingsER7QRegionPbb(
    const QWidgetPrivate *self,
    QRegion *source,
    bool *hasDirtySiblingsAbove,
    bool alsoNonOpaque) {
  self->subtractOpaqueSiblings(
      *source,
      hasDirtySiblingsAbove,
      alsoNonOpaque);
}

//  void QWidgetPrivate::clipToEffectiveMask(QRegion &region) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QWidgetPrivate19clipToEffectiveMaskER7QRegion(
    const QWidgetPrivate *self,
    QRegion *region) {
  self->clipToEffectiveMask(*region);
}

//  void QWidgetPrivate::updateIsOpaque()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate14updateIsOpaqueEv(QWidgetPrivate *self) {
  self->updateIsOpaque();
}

//  void QWidgetPrivate::setOpaque(bool opaque)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate9setOpaqueEb(
    QWidgetPrivate *self,
    bool opaque) {
  self->setOpaque(opaque);
}

//  void QWidgetPrivate::updateIsTranslucent()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate19updateIsTranslucentEv(QWidgetPrivate *self) {
  self->updateIsTranslucent();
}

#if QT_CONFIG(graphicseffect)
//  void QWidgetPrivate::invalidateGraphicsEffectsRecursively()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate36invalidateGraphicsEffectsRecursivelyEv(
    QWidgetPrivate *self) {
  self->invalidateGraphicsEffectsRecursively();
}
#endif  // QT_CONFIG(graphicseffect)

//  const QRegion &QWidgetPrivate::getOpaqueChildren() const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK14QWidgetPrivate17getOpaqueChildrenEv(
    const QWidgetPrivate *self) {
  return new QRegion(self->getOpaqueChildren());
}

//  void QWidgetPrivate::setDirtyOpaqueRegion()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate20setDirtyOpaqueRegionEv(
    QWidgetPrivate *self) {
  self->setDirtyOpaqueRegion();
}

//  bool QWidgetPrivate::close()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QWidgetPrivate5closeEv(QWidgetPrivate *self) {
  return self->close();
}

//  bool QWidgetPrivate::handleClose(CloseMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QWidgetPrivate11handleCloseENS_9CloseModeE(
    QWidgetPrivate *self,
    QWidgetPrivate::CloseMode mode) {
  return self->handleClose(mode);
}

//  void QWidgetPrivate::setWindowIcon_helper()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate20setWindowIcon_helperEv(
    QWidgetPrivate *self) {
  self->setWindowIcon_helper();
}

//  void QWidgetPrivate::setWindowIcon_sys()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate17setWindowIcon_sysEv(QWidgetPrivate *self) {
  self->setWindowIcon_sys();
}

//  void QWidgetPrivate::setWindowOpacity_sys(qreal opacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate20setWindowOpacity_sysEd(
    QWidgetPrivate *self,
    qreal opacity) {
  self->setWindowOpacity_sys(opacity);
}

//  void QWidgetPrivate::adjustQuitOnCloseAttribute()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate26adjustQuitOnCloseAttributeEv(
    QWidgetPrivate *self) {
  self->adjustQuitOnCloseAttribute();
}

//  void QWidgetPrivate::scrollChildren(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate14scrollChildrenEii(
    QWidgetPrivate *self,
    int dx,
    int dy) {
  self->scrollChildren(dx, dy);
}

//  void QWidgetPrivate::moveRect(const QRect &a0, int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate8moveRectERK5QRectii(
    QWidgetPrivate *self,
    const QRect *a0,
    int dx,
    int dy) {
  self->moveRect(*a0, dx, dy);
}

//  void QWidgetPrivate::scrollRect(const QRect &a0, int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate10scrollRectERK5QRectii(
    QWidgetPrivate *self,
    const QRect *a0,
    int dx,
    int dy) {
  self->scrollRect(*a0, dx, dy);
}

//  void QWidgetPrivate::invalidateBackingStore_resizeHelper(const QPoint
//      &oldPos, const QSize &oldSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate35invalidateBackingStore_resizeHelperERK6QPointRK5QSize(
    QWidgetPrivate *self,
    const QPoint *oldPos,
    const QSize *oldSize) {
  self->invalidateBackingStore_resizeHelper(*oldPos, *oldSize);
}

//  QRegion QWidgetPrivate::overlappedRegion(const QRect &rect, bool
//      breakAfterFirst) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK14QWidgetPrivate16overlappedRegionERK5QRectb(
    const QWidgetPrivate *self,
    const QRect *rect,
    bool breakAfterFirst) {
  return new QRegion(self->overlappedRegion(*rect, breakAfterFirst));
}

//  bool QWidgetPrivate::isOverlapped(const QRect &rect) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QWidgetPrivate12isOverlappedERK5QRect(
    const QWidgetPrivate *self,
    const QRect *rect) {
  return self->isOverlapped(*rect);
}

//  void QWidgetPrivate::syncBackingStore()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate16syncBackingStoreEv(QWidgetPrivate *self) {
  self->syncBackingStore();
}

//  void QWidgetPrivate::syncBackingStore(const QRegion &region)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate16syncBackingStoreERK7QRegion(
    QWidgetPrivate *self,
    const QRegion *region) {
  self->syncBackingStore(*region);
}

//  bool QWidgetPrivate::shouldDiscardSyncRequest() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QWidgetPrivate24shouldDiscardSyncRequestEv(
    const QWidgetPrivate *self) {
  return self->shouldDiscardSyncRequest();
}

//  void QWidgetPrivate::updateWidgetTransform(QEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate21updateWidgetTransformEP6QEvent(
    QWidgetPrivate *self,
    QEvent *event) {
  self->updateWidgetTransform(event);
}

//  void QWidgetPrivate::reparentFocusWidgets(QWidget *oldtlw)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate20reparentFocusWidgetsEP7QWidget(
    QWidgetPrivate *self,
    QWidget *oldtlw) {
  self->reparentFocusWidgets(oldtlw);
}

//  void QWidgetPrivate::setWinId(WId a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate8setWinIdEy(QWidgetPrivate *self, WId a0) {
  self->setWinId(a0);
}

//  void QWidgetPrivate::showChildren(bool spontaneous)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate12showChildrenEb(
    QWidgetPrivate *self,
    bool spontaneous) {
  self->showChildren(spontaneous);
}

//  void QWidgetPrivate::hideChildren(bool spontaneous)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate12hideChildrenEb(
    QWidgetPrivate *self,
    bool spontaneous) {
  self->hideChildren(spontaneous);
}

//  void QWidgetPrivate::setParent_sys(QWidget *parent, Qt::WindowFlags a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate13setParent_sysEP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidgetPrivate *self,
    QWidget *parent,
    int a1) {
  self->setParent_sys(parent, QFlags<Qt::WindowType>::fromInt(a1));
}

//  void QWidgetPrivate::reparentWidgetWindows(QWidget *parentWithWindow,
//      Qt::WindowFlags windowFlags)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate21reparentWidgetWindowsEP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidgetPrivate *self,
    QWidget *parentWithWindow,
    int windowFlags) {
  self->reparentWidgetWindows(
      parentWithWindow,
      QFlags<Qt::WindowType>::fromInt(windowFlags));
}

//  void QWidgetPrivate::reparentWidgetWindowChildren(QWidget
//      *parentWithWindow)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate28reparentWidgetWindowChildrenEP7QWidget(
    QWidgetPrivate *self,
    QWidget *parentWithWindow) {
  self->reparentWidgetWindowChildren(parentWithWindow);
}

//  void QWidgetPrivate::scroll_sys(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate10scroll_sysEii(
    QWidgetPrivate *self,
    int dx,
    int dy) {
  self->scroll_sys(dx, dy);
}

//  void QWidgetPrivate::scroll_sys(int dx, int dy, const QRect &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate10scroll_sysEiiRK5QRect(
    QWidgetPrivate *self,
    int dx,
    int dy,
    const QRect *r) {
  self->scroll_sys(dx, dy, *r);
}

//  void QWidgetPrivate::deactivateWidgetCleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate23deactivateWidgetCleanupEv(
    QWidgetPrivate *self) {
  self->deactivateWidgetCleanup();
}

//  void QWidgetPrivate::setGeometry_sys(int a0, int a1, int a2, int a3, bool
//      a4)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate15setGeometry_sysEiiiib(
    QWidgetPrivate *self,
    int a0,
    int a1,
    int a2,
    int a3,
    bool a4) {
  self->setGeometry_sys(a0, a1, a2, a3, a4);
}

//  void QWidgetPrivate::fixPosIncludesFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate19fixPosIncludesFrameEv(QWidgetPrivate *self) {
  self->fixPosIncludesFrame();
}

//  void QWidgetPrivate::sendPendingMoveAndResizeEvents(bool recursive, bool
//      disableUpdates)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate30sendPendingMoveAndResizeEventsEbb(
    QWidgetPrivate *self,
    bool recursive,
    bool disableUpdates) {
  self->sendPendingMoveAndResizeEvents(recursive, disableUpdates);
}

//  void QWidgetPrivate::activateChildLayoutsRecursively()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate31activateChildLayoutsRecursivelyEv(
    QWidgetPrivate *self) {
  self->activateChildLayoutsRecursively();
}

//  void QWidgetPrivate::show_recursive()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate14show_recursiveEv(QWidgetPrivate *self) {
  self->show_recursive();
}

//  void QWidgetPrivate::show_helper()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate11show_helperEv(QWidgetPrivate *self) {
  self->show_helper();
}

//  void QWidgetPrivate::show_sys()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate8show_sysEv(QWidgetPrivate *self) {
  self->show_sys();
}

//  void QWidgetPrivate::hide_sys()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate8hide_sysEv(QWidgetPrivate *self) {
  self->hide_sys();
}

//  void QWidgetPrivate::hide_helper()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate11hide_helperEv(QWidgetPrivate *self) {
  self->hide_helper();
}

//  bool QWidgetPrivate::isExplicitlyHidden() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QWidgetPrivate18isExplicitlyHiddenEv(
    const QWidgetPrivate *self) {
  return self->isExplicitlyHidden();
}

//  void QWidgetPrivate::_q_showIfNotHidden()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate18_q_showIfNotHiddenEv(QWidgetPrivate *self) {
  self->_q_showIfNotHidden();
}

//  void QWidgetPrivate::setVisible(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate10setVisibleEb(QWidgetPrivate *self, bool a0) {
  self->setVisible(a0);
}

//  void QWidgetPrivate::setEnabled_helper(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate17setEnabled_helperEb(
    QWidgetPrivate *self,
    bool a0) {
  self->setEnabled_helper(a0);
}

//  void QWidgetPrivate::adjustFlags(Qt::WindowFlags &flags, QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate11adjustFlagsER6QFlagsIN2Qt10WindowTypeEEP7QWidget(
    Qt::WindowFlags *flags,
    QWidget *w) {
  QWidgetPrivate::adjustFlags(*flags, w);
}

//  void QWidgetPrivate::updateFrameStrut()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate16updateFrameStrutEv(QWidgetPrivate *self) {
  self->updateFrameStrut();
}

//  QRect QWidgetPrivate::frameStrut() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK14QWidgetPrivate10frameStrutEv(const QWidgetPrivate *self) {
  return new QRect(self->frameStrut());
}

//  void QWidgetPrivate::setWindowIconText_sys(const QString &cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate21setWindowIconText_sysERK7QString(
    QWidgetPrivate *self,
    const QString *cap) {
  self->setWindowIconText_sys(*cap);
}

//  void QWidgetPrivate::setWindowIconText_helper(const QString &cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate24setWindowIconText_helperERK7QString(
    QWidgetPrivate *self,
    const QString *cap) {
  self->setWindowIconText_helper(*cap);
}

//  void QWidgetPrivate::setWindowTitle_sys(const QString &cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate18setWindowTitle_sysERK7QString(
    QWidgetPrivate *self,
    const QString *cap) {
  self->setWindowTitle_sys(*cap);
}

//  void QWidgetPrivate::setWindowFilePath_sys(const QString &filePath)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate21setWindowFilePath_sysERK7QString(
    QWidgetPrivate *self,
    const QString *filePath) {
  self->setWindowFilePath_sys(*filePath);
}

#if !defined(QT_NO_CURSOR)
//  void QWidgetPrivate::setCursor_sys(const QCursor &cursor)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate13setCursor_sysERK7QCursor(
    QWidgetPrivate *self,
    const QCursor *cursor) {
  self->setCursor_sys(*cursor);
}
#endif  // !defined(QT_NO_CURSOR)

#if !defined(QT_NO_CURSOR)
//  void QWidgetPrivate::unsetCursor_sys()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate15unsetCursor_sysEv(QWidgetPrivate *self) {
  self->unsetCursor_sys();
}
#endif  // !defined(QT_NO_CURSOR)

//  void QWidgetPrivate::setWindowTitle_helper(const QString &cap)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate21setWindowTitle_helperERK7QString(
    QWidgetPrivate *self,
    const QString *cap) {
  self->setWindowTitle_helper(*cap);
}

//  void QWidgetPrivate::setWindowFilePath_helper(const QString &filePath)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate24setWindowFilePath_helperERK7QString(
    QWidgetPrivate *self,
    const QString *filePath) {
  self->setWindowFilePath_helper(*filePath);
}

//  void QWidgetPrivate::setWindowModified_helper()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate24setWindowModified_helperEv(
    QWidgetPrivate *self) {
  self->setWindowModified_helper();
}

//  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE(
    QWidgetPrivate *self,
    int windowFlags) {
  self->setWindowFlags(QFlags<Qt::WindowType>::fromInt(windowFlags));
}

//  bool QWidgetPrivate::setMinimumSize_helper(int &minw, int &minh)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QWidgetPrivate21setMinimumSize_helperERiS0_(
    QWidgetPrivate *self,
    int *minw,
    int *minh) {
  return self->setMinimumSize_helper(*minw, *minh);
}

//  bool QWidgetPrivate::setMaximumSize_helper(int &maxw, int &maxh)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QWidgetPrivate21setMaximumSize_helperERiS0_(
    QWidgetPrivate *self,
    int *maxw,
    int *maxh) {
  return self->setMaximumSize_helper(*maxw, *maxh);
}

//  void QWidgetPrivate::setConstraints_sys()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate18setConstraints_sysEv(QWidgetPrivate *self) {
  self->setConstraints_sys();
}

//  bool QWidgetPrivate::pointInsideRectAndMask(const QPointF &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QWidgetPrivate22pointInsideRectAndMaskERK7QPointF(
    const QWidgetPrivate *self,
    const QPointF *a0) {
  return self->pointInsideRectAndMask(*a0);
}

//  QWidget *QWidgetPrivate::childAt_helper(const QPointF &a0, bool a1) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK14QWidgetPrivate14childAt_helperERK7QPointFb(
    const QWidgetPrivate *self,
    const QPointF *a0,
    bool a1) {
  return self->childAt_helper(*a0, a1);
}

//  QWidget *QWidgetPrivate::childAtRecursiveHelper(const QPointF &p, bool
//      a1) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK14QWidgetPrivate22childAtRecursiveHelperERK7QPointFb(
    const QWidgetPrivate *self,
    const QPointF *p,
    bool a1) {
  return self->childAtRecursiveHelper(*p, a1);
}

//  void QWidgetPrivate::updateGeometry_helper(bool forceUpdate)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate21updateGeometry_helperEb(
    QWidgetPrivate *self,
    bool forceUpdate) {
  self->updateGeometry_helper(forceUpdate);
}

//  void QWidgetPrivate::getLayoutItemMargins(int *left, int *top, int
//      *right, int *bottom) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QWidgetPrivate20getLayoutItemMarginsEPiS0_S0_S0_(
    const QWidgetPrivate *self,
    int *left,
    int *top,
    int *right,
    int *bottom) {
  self->getLayoutItemMargins(left, top, right, bottom);
}

//  void QWidgetPrivate::setLayoutItemMargins(int left, int top, int right,
//      int bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate20setLayoutItemMarginsEiiii(
    QWidgetPrivate *self,
    int left,
    int top,
    int right,
    int bottom) {
  self->setLayoutItemMargins(left, top, right, bottom);
}

//  void QWidgetPrivate::setLayoutItemMargins(QStyle::SubElement element,
//      const QStyleOption *opt)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate20setLayoutItemMarginsEN6QStyle10SubElementEPK12QStyleOption(
    QWidgetPrivate *self,
    QStyle::SubElement element,
    const QStyleOption *opt) {
  self->setLayoutItemMargins(element, opt);
}

//  void QWidgetPrivate::updateContentsRect()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate18updateContentsRectEv(QWidgetPrivate *self) {
  self->updateContentsRect();
}

//  QMargins QWidgetPrivate::safeAreaMargins() const
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZNK14QWidgetPrivate15safeAreaMarginsEv(
    const QWidgetPrivate *self) {
  return new QMargins(self->safeAreaMargins());
}

//  void QWidgetPrivate::aboutToDestroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate14aboutToDestroyEv(QWidgetPrivate *self) {
  self->aboutToDestroy();
}

//  void QWidgetPrivate::recreate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate8recreateEv(QWidgetPrivate *self) {
  self->recreate();
}

//  QWidget *QWidgetPrivate::effectiveFocusWidget()
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN14QWidgetPrivate20effectiveFocusWidgetEv(
    QWidgetPrivate *self) {
  return self->effectiveFocusWidget();
}

//  void QWidgetPrivate::setModal_sys()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate12setModal_sysEv(QWidgetPrivate *self) {
  self->setModal_sys();
}

//  QWidget *QWidgetPrivate::parentGraphicsView(const QWidget *widget)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN14QWidgetPrivate18parentGraphicsViewEPK7QWidget(
    const QWidget *widget) {
  return QWidgetPrivate::parentGraphicsView(widget);
}

//  QRect QWidgetPrivate::screenGeometry(const QWidget *widget)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN14QWidgetPrivate14screenGeometryEPK7QWidget(
    const QWidget *widget) {
  return new QRect(QWidgetPrivate::screenGeometry(widget));
}

//  QRect QWidgetPrivate::availableScreenGeometry(const QWidget *widget)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN14QWidgetPrivate23availableScreenGeometryEPK7QWidget(
    const QWidget *widget) {
  return new QRect(QWidgetPrivate::availableScreenGeometry(widget));
}

//  QScreen *QWidgetPrivate::screen(const QWidget *widget, const QPoint
//      &globalPosition, bool hasPosition)
extern "C" Q_DECL_EXPORT
QScreen *ritual_ZN14QWidgetPrivate6screenEPK7QWidgetRK6QPointb(
    const QWidget *widget,
    const QPoint *globalPosition,
    bool hasPosition) {
  return QWidgetPrivate::screen(widget, *globalPosition, hasPosition);
}

//  QRect QWidgetPrivate::screenGeometry(const QWidget *widget, const QPoint
//      &globalPosition, bool hasPosition)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN14QWidgetPrivate14screenGeometryEPK7QWidgetRK6QPointb(
    const QWidget *widget,
    const QPoint *globalPosition,
    bool hasPosition) {
  return new QRect(
      QWidgetPrivate::screenGeometry(
          widget,
          *globalPosition,
          hasPosition));
}

//  QRect QWidgetPrivate::availableScreenGeometry(const QWidget *widget,
//      const QPoint &globalPosition, bool hasPosition)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN14QWidgetPrivate23availableScreenGeometryEPK7QWidgetRK6QPointb(
    const QWidget *widget,
    const QPoint *globalPosition,
    bool hasPosition) {
  return new QRect(
      QWidgetPrivate::availableScreenGeometry(
          widget,
          *globalPosition,
          hasPosition));
}

//  void QWidgetPrivate::setRedirected(QPaintDevice *replacement, const
//      QPoint &offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate13setRedirectedEP12QPaintDeviceRK6QPoint(
    QWidgetPrivate *self,
    QPaintDevice *replacement,
    const QPoint *offset) {
  self->setRedirected(replacement, *offset);
}

//  QPaintDevice *QWidgetPrivate::redirected(QPoint *offset) const
extern "C" Q_DECL_EXPORT
QPaintDevice *ritual_ZNK14QWidgetPrivate10redirectedEP6QPoint(
    const QWidgetPrivate *self,
    QPoint *offset) {
  return self->redirected(offset);
}

//  void QWidgetPrivate::restoreRedirected()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate17restoreRedirectedEv(QWidgetPrivate *self) {
  self->restoreRedirected();
}

//  void QWidgetPrivate::enforceNativeChildren()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate21enforceNativeChildrenEv(
    QWidgetPrivate *self) {
  self->enforceNativeChildren();
}

//  bool QWidgetPrivate::nativeChildrenForced() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QWidgetPrivate20nativeChildrenForcedEv(
    const QWidgetPrivate *self) {
  return self->nativeChildrenForced();
}

//  QRect QWidgetPrivate::effectiveRectFor(const QRegion &region) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK14QWidgetPrivate16effectiveRectForERK7QRegion(
    const QWidgetPrivate *self,
    const QRegion *region) {
  return new QRect(self->effectiveRectFor(*region));
}

//  QRect QWidgetPrivate::effectiveRectFor(const QRect &rect) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK14QWidgetPrivate16effectiveRectForERK5QRect(
    const QWidgetPrivate *self,
    const QRect *rect) {
  return new QRect(self->effectiveRectFor(*rect));
}

//  QSize QWidgetPrivate::adjustedSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK14QWidgetPrivate12adjustedSizeEv(
    const QWidgetPrivate *self) {
  return new QSize(self->adjustedSize());
}

//  void QWidgetPrivate::handleSoftwareInputPanel(Qt::MouseButton button,
//      bool clickCausedFocus)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate24handleSoftwareInputPanelEN2Qt11MouseButtonEb(
    QWidgetPrivate *self,
    Qt::MouseButton button,
    bool clickCausedFocus) {
  self->handleSoftwareInputPanel(button, clickCausedFocus);
}

//  void QWidgetPrivate::handleSoftwareInputPanel(bool clickCausedFocus)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate24handleSoftwareInputPanelEb(
    QWidgetPrivate *self,
    bool clickCausedFocus) {
  self->handleSoftwareInputPanel(clickCausedFocus);
}

//  void QWidgetPrivate::setWSGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate13setWSGeometryEv(QWidgetPrivate *self) {
  self->setWSGeometry();
}

//  QPoint QWidgetPrivate::mapToWS(const QPoint &p) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK14QWidgetPrivate7mapToWSERK6QPoint(
    const QWidgetPrivate *self,
    const QPoint *p) {
  return new QPoint(self->mapToWS(*p));
}

//  QPoint QWidgetPrivate::mapFromWS(const QPoint &p) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK14QWidgetPrivate9mapFromWSERK6QPoint(
    const QWidgetPrivate *self,
    const QPoint *p) {
  return new QPoint(self->mapFromWS(*p));
}

//  QRect QWidgetPrivate::mapToWS(const QRect &r) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK14QWidgetPrivate7mapToWSERK5QRect(
    const QWidgetPrivate *self,
    const QRect *r) {
  return new QRect(self->mapToWS(*r));
}

//  QRect QWidgetPrivate::mapFromWS(const QRect &r) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK14QWidgetPrivate9mapFromWSERK5QRect(
    const QWidgetPrivate *self,
    const QRect *r) {
  return new QRect(self->mapFromWS(*r));
}

//  QObject *QWidgetPrivate::focusObject()
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN14QWidgetPrivate11focusObjectEv(QWidgetPrivate *self) {
  return self->focusObject();
}

//  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
extern "C" Q_DECL_EXPORT
QPlatformBackingStoreRhiConfig *ritual_ZNK14QWidgetPrivate9rhiConfigEv(
    const QWidgetPrivate *self) {
  return new QPlatformBackingStoreRhiConfig(self->rhiConfig());
}

//  TextureData QWidgetPrivate::texture() const
extern "C" Q_DECL_EXPORT
QWidgetPrivate::TextureData *ritual_ZNK14QWidgetPrivate7textureEv(
    const QWidgetPrivate *self) {
  return new QWidgetPrivate::TextureData(self->texture());
}

//  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
extern "C" Q_DECL_EXPORT
int ritual_ZN14QWidgetPrivate16textureListFlagsEv(QWidgetPrivate *self) {
  return static_cast<int>(self->textureListFlags().toInt());
}

//  QImage QWidgetPrivate::grabFramebuffer()
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN14QWidgetPrivate15grabFramebufferEv(QWidgetPrivate *self) {
  return new QImage(self->grabFramebuffer());
}

//  void QWidgetPrivate::beginBackingStorePainting()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate25beginBackingStorePaintingEv(
    QWidgetPrivate *self) {
  self->beginBackingStorePainting();
}

//  void QWidgetPrivate::endBackingStorePainting()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate23endBackingStorePaintingEv(
    QWidgetPrivate *self) {
  self->endBackingStorePainting();
}

//  void QWidgetPrivate::beginCompose()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate12beginComposeEv(QWidgetPrivate *self) {
  self->beginCompose();
}

//  void QWidgetPrivate::endCompose()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate10endComposeEv(QWidgetPrivate *self) {
  self->endCompose();
}

//  void QWidgetPrivate::setRenderToTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate18setRenderToTextureEv(QWidgetPrivate *self) {
  self->setRenderToTexture();
}

//  void QWidgetPrivate::setTextureChildSeen()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate19setTextureChildSeenEv(QWidgetPrivate *self) {
  self->setTextureChildSeen();
}

//  void QWidgetPrivate::sendComposeStatus(QWidget *w, bool end)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate17sendComposeStatusEP7QWidgetb(
    QWidget *w,
    bool end) {
  QWidgetPrivate::sendComposeStatus(w, end);
}

//  void QWidgetPrivate::initializeViewportFramebuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate29initializeViewportFramebufferEv(
    QWidgetPrivate *self) {
  self->initializeViewportFramebuffer();
}

//  void QWidgetPrivate::resizeViewportFramebuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate25resizeViewportFramebufferEv(
    QWidgetPrivate *self) {
  self->resizeViewportFramebuffer();
}

//  void QWidgetPrivate::resolveSamples()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate14resolveSamplesEv(QWidgetPrivate *self) {
  self->resolveSamples();
}

//  bool QWidgetPrivate::isStereoEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QWidgetPrivate15isStereoEnabledEv(QWidgetPrivate *self) {
  return self->isStereoEnabled();
}

//  bool QWidgetPrivate::toggleStereoTargetBuffer()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QWidgetPrivate24toggleStereoTargetBufferEv(
    QWidgetPrivate *self) {
  return self->toggleStereoTargetBuffer();
}

//  void QWidgetPrivate::setWidgetParentHelper(QObject *widgetAsObject,
//      QObject *newParent)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate21setWidgetParentHelperEP7QObjectS1_(
    QObject *widgetAsObject,
    QObject *newParent) {
  QWidgetPrivate::setWidgetParentHelper(widgetAsObject, newParent);
}

//  std::string QWidgetPrivate::flagsForDumping() const
extern "C" Q_DECL_EXPORT
std::string *ritual_ZNK14QWidgetPrivate15flagsForDumpingB5cxx11Ev(
    const QWidgetPrivate *self) {
  return new std::string(self->flagsForDumping());
}

//  QWidget *QWidgetPrivate::closestParentWidgetWithWindowHandle() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK14QWidgetPrivate35closestParentWidgetWithWindowHandleEv(
    const QWidgetPrivate *self) {
  return self->closestParentWidgetWithWindowHandle();
}

//  QWidget *QWidgetPrivate::nextPrevElementInFocusChain(FocusDirection
//      direction) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK14QWidgetPrivate27nextPrevElementInFocusChainENS_14FocusDirectionE(
    const QWidgetPrivate *self,
    QWidgetPrivate::FocusDirection direction) {
  return self->nextPrevElementInFocusChain(direction);
}

//  bool QWidgetPrivate::removeFromFocusChain(FocusChainRemovalRules rules,
//      FocusDirection direction)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QWidgetPrivate20removeFromFocusChainE6QFlagsINS_21FocusChainRemovalRuleEENS_14FocusDirectionE(
    QWidgetPrivate *self,
    int rules,
    QWidgetPrivate::FocusDirection direction) {
  return self->removeFromFocusChain(
      QFlags<QWidgetPrivate::FocusChainRemovalRule>::fromInt(rules),
      direction);
}

//  bool QWidgetPrivate::insertIntoFocusChain(FocusDirection direction,
//      QWidget *position)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QWidgetPrivate20insertIntoFocusChainENS_14FocusDirectionEP7QWidget(
    QWidgetPrivate *self,
    QWidgetPrivate::FocusDirection direction,
    QWidget *position) {
  return self->insertIntoFocusChain(direction, position);
}

//  bool QWidgetPrivate::insertIntoFocusChain(const QWidgetList
//      &toBeInserted, FocusDirection direction, QWidget *position)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QWidgetPrivate20insertIntoFocusChainERK5QListIP7QWidgetENS_14FocusDirectionES2_(
    const QList<QWidget *> *toBeInserted,
    QWidgetPrivate::FocusDirection direction,
    QWidget *position) {
  return QWidgetPrivate::insertIntoFocusChain(
      *toBeInserted,
      direction,
      position);
}

//  bool QWidgetPrivate::insertIntoFocusChainBefore(QWidget *position)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QWidgetPrivate26insertIntoFocusChainBeforeEP7QWidget(
    QWidgetPrivate *self,
    QWidget *position) {
  return self->insertIntoFocusChainBefore(position);
}

//  bool QWidgetPrivate::insertIntoFocusChainAfter(QWidget *position)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QWidgetPrivate25insertIntoFocusChainAfterEP7QWidget(
    QWidgetPrivate *self,
    QWidget *position) {
  return self->insertIntoFocusChainAfter(position);
}

//  QWidgetList QWidgetPrivate::takeFromFocusChain(QWidget *from, QWidget
//      *to, FocusDirection direction)
extern "C" Q_DECL_EXPORT
QList<QWidget *> *ritual_ZN14QWidgetPrivate18takeFromFocusChainEP7QWidgetS1_NS_14FocusDirectionE(
    QWidget *from,
    QWidget *to,
    QWidgetPrivate::FocusDirection direction) {
  return new QList<QWidget *>(
      QWidgetPrivate::takeFromFocusChain(
          from,
          to,
          direction));
}

//  void QWidgetPrivate::reparentFocusChildren(FocusDirection direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate21reparentFocusChildrenENS_14FocusDirectionE(
    QWidgetPrivate *self,
    QWidgetPrivate::FocusDirection direction) {
  self->reparentFocusChildren(direction);
}

//  QWidget *QWidgetPrivate::determineLastFocusChild(QWidget *noFurtherThan)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN14QWidgetPrivate23determineLastFocusChildEP7QWidget(
    QWidgetPrivate *self,
    QWidget *noFurtherThan) {
  return self->determineLastFocusChild(noFurtherThan);
}

//  void QWidgetPrivate::initFocusChain()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate14initFocusChainEv(QWidgetPrivate *self) {
  self->initFocusChain();
}

//  bool QWidgetPrivate::isInFocusChain() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QWidgetPrivate14isInFocusChainEv(
    const QWidgetPrivate *self) {
  return self->isInFocusChain();
}

//  bool QWidgetPrivate::isFocusChainConsistent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QWidgetPrivate22isFocusChainConsistentEv(
    const QWidgetPrivate *self) {
  return self->isFocusChainConsistent();
}

//  void QWidgetPrivate::setNetWmWindowTypes(bool skipIfMissing)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate19setNetWmWindowTypesEb(
    QWidgetPrivate *self,
    bool skipIfMissing) {
  self->setNetWmWindowTypes(skipIfMissing);
}

//  bool QWidgetPrivate::stealKeyboardGrab(bool grab)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QWidgetPrivate17stealKeyboardGrabEb(
    QWidgetPrivate *self,
    bool grab) {
  return self->stealKeyboardGrab(grab);
}

//  bool QWidgetPrivate::stealMouseGrab(bool grab)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QWidgetPrivate14stealMouseGrabEb(
    QWidgetPrivate *self,
    bool grab) {
  return self->stealMouseGrab(grab);
}

//  bool QWidgetPrivate::hasChildWithFocusPolicy(Qt::FocusPolicy policy,
//      const QWidget *excludeChildrenOf) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QWidgetPrivate23hasChildWithFocusPolicyEN2Qt11FocusPolicyEPK7QWidget(
    const QWidgetPrivate *self,
    Qt::FocusPolicy policy,
    const QWidget *excludeChildrenOf) {
  return self->hasChildWithFocusPolicy(policy, excludeChildrenOf);
}

//  a Python function taken by a CuteQWidgetPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWidgetPrivate(
    QWidgetPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWidgetPrivate *>(self)->take(key, call);
}

//  void QWidgetPrivate::setVisible(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QWidgetPrivate10setVisibleEb(
    QWidgetPrivate *self,
    bool a0) {
  self->QWidgetPrivate::setVisible(a0);
}

//  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QWidgetPrivate14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE(
    QWidgetPrivate *self,
    int windowFlags) {
  self->QWidgetPrivate::setWindowFlags(
      QFlags<Qt::WindowType>::fromInt(windowFlags));
}

//  void QWidgetPrivate::aboutToDestroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QWidgetPrivate14aboutToDestroyEv(QWidgetPrivate *self) {
  self->QWidgetPrivate::aboutToDestroy();
}

//  void QWidgetPrivate::recreate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QWidgetPrivate8recreateEv(QWidgetPrivate *self) {
  self->QWidgetPrivate::recreate();
}

//  QObject *QWidgetPrivate::focusObject()
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZN14QWidgetPrivate11focusObjectEv(QWidgetPrivate *self) {
  return self->QWidgetPrivate::focusObject();
}

//  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
extern "C" Q_DECL_EXPORT
QPlatformBackingStoreRhiConfig *ritual_own_ZNK14QWidgetPrivate9rhiConfigEv(
    const QWidgetPrivate *self) {
  return new QPlatformBackingStoreRhiConfig(
      self->QWidgetPrivate::rhiConfig());
}

//  TextureData QWidgetPrivate::texture() const
extern "C" Q_DECL_EXPORT
QWidgetPrivate::TextureData *ritual_own_ZNK14QWidgetPrivate7textureEv(
    const QWidgetPrivate *self) {
  return new QWidgetPrivate::TextureData(self->QWidgetPrivate::texture());
}

//  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
extern "C" Q_DECL_EXPORT
int ritual_own_ZN14QWidgetPrivate16textureListFlagsEv(QWidgetPrivate *self) {
  return static_cast<int>(self->QWidgetPrivate::textureListFlags().toInt());
}

//  QImage QWidgetPrivate::grabFramebuffer()
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZN14QWidgetPrivate15grabFramebufferEv(
    QWidgetPrivate *self) {
  return new QImage(self->QWidgetPrivate::grabFramebuffer());
}

//  void QWidgetPrivate::beginBackingStorePainting()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QWidgetPrivate25beginBackingStorePaintingEv(
    QWidgetPrivate *self) {
  self->QWidgetPrivate::beginBackingStorePainting();
}

//  void QWidgetPrivate::endBackingStorePainting()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QWidgetPrivate23endBackingStorePaintingEv(
    QWidgetPrivate *self) {
  self->QWidgetPrivate::endBackingStorePainting();
}

//  void QWidgetPrivate::beginCompose()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QWidgetPrivate12beginComposeEv(QWidgetPrivate *self) {
  self->QWidgetPrivate::beginCompose();
}

//  void QWidgetPrivate::endCompose()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QWidgetPrivate10endComposeEv(QWidgetPrivate *self) {
  self->QWidgetPrivate::endCompose();
}

//  void QWidgetPrivate::initializeViewportFramebuffer()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QWidgetPrivate29initializeViewportFramebufferEv(
    QWidgetPrivate *self) {
  self->QWidgetPrivate::initializeViewportFramebuffer();
}

//  void QWidgetPrivate::resizeViewportFramebuffer()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QWidgetPrivate25resizeViewportFramebufferEv(
    QWidgetPrivate *self) {
  self->QWidgetPrivate::resizeViewportFramebuffer();
}

//  void QWidgetPrivate::resolveSamples()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QWidgetPrivate14resolveSamplesEv(QWidgetPrivate *self) {
  self->QWidgetPrivate::resolveSamples();
}

//  bool QWidgetPrivate::isStereoEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QWidgetPrivate15isStereoEnabledEv(QWidgetPrivate *self) {
  return self->QWidgetPrivate::isStereoEnabled();
}

//  bool QWidgetPrivate::toggleStereoTargetBuffer()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QWidgetPrivate24toggleStereoTargetBufferEv(
    QWidgetPrivate *self) {
  return self->QWidgetPrivate::toggleStereoTargetBuffer();
}

//  a std::string a ritual of QWidgetPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QWidgetPrivate__std_string(std::string *self) {
  delete self;
}

//  void QWidgetPrivate::invalidateBackingStore<QRect>(const QRect &)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWidgetPrivate22invalidateBackingStoreI5QRectEEvRKT_(
    QWidgetPrivate *self,
    const QRect *t) {
  self->invalidateBackingStore<QRect>(*t);
}
