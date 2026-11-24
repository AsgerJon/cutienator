//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtabbar_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(tabbar)
#if QT_CONFIG(tabbar)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qtabbar.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qtabbar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <cstring>

//  A QTabBarPrivate that Python can take functions over in. Every QTabBarPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQTabBarPrivateCall0)(const void *, bool, int *);
typedef void (*CuteQTabBarPrivateCall1)(const void *, int, int *);
typedef void (*CuteQTabBarPrivateCall2)(const void *, int *);
typedef void (*CuteQTabBarPrivateCall3)(const void *, int *);
typedef void * (*CuteQTabBarPrivateCall4)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQTabBarPrivateCall5)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQTabBarPrivateCall6)(const void *, int *);
typedef int (*CuteQTabBarPrivateCall7)(const void *, int *);
typedef const QImage * (*CuteQTabBarPrivateCall8)(const void *, int *);
typedef void (*CuteQTabBarPrivateCall9)(const void *, int *);
typedef void (*CuteQTabBarPrivateCall10)(const void *, int *);
typedef void (*CuteQTabBarPrivateCall11)(const void *, int *);
typedef void (*CuteQTabBarPrivateCall12)(const void *, int *);
typedef void (*CuteQTabBarPrivateCall13)(const void *, int *);
typedef void (*CuteQTabBarPrivateCall14)(const void *, int *);
typedef void (*CuteQTabBarPrivateCall15)(const void *, int *);
typedef bool (*CuteQTabBarPrivateCall16)(const void *, int *);
typedef bool (*CuteQTabBarPrivateCall17)(const void *, int *);
class CuteQTabBarPrivate : public QTabBarPrivate {
public:
  using QTabBarPrivate::QTabBarPrivate;
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
      CuteQTabBarPrivateCall0 call = reinterpret_cast<CuteQTabBarPrivateCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTabBarPrivateCall1 call = reinterpret_cast<CuteQTabBarPrivateCall1>(taken[1]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[2]) {
      int handled = 0;
      CuteQTabBarPrivateCall2 call = reinterpret_cast<CuteQTabBarPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[3]) {
      int handled = 0;
      CuteQTabBarPrivateCall3 call = reinterpret_cast<CuteQTabBarPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[4]) {
      int handled = 0;
      CuteQTabBarPrivateCall4 call = reinterpret_cast<CuteQTabBarPrivateCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQTabBarPrivateCall5 call = reinterpret_cast<CuteQTabBarPrivateCall5>(taken[5]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQTabBarPrivateCall6 call = reinterpret_cast<CuteQTabBarPrivateCall6>(taken[6]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[7]) {
      int handled = 0;
      CuteQTabBarPrivateCall7 call = reinterpret_cast<CuteQTabBarPrivateCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[8]) {
      int handled = 0;
      CuteQTabBarPrivateCall8 call = reinterpret_cast<CuteQTabBarPrivateCall8>(taken[8]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[9]) {
      int handled = 0;
      CuteQTabBarPrivateCall9 call = reinterpret_cast<CuteQTabBarPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[10]) {
      int handled = 0;
      CuteQTabBarPrivateCall10 call = reinterpret_cast<CuteQTabBarPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[11]) {
      int handled = 0;
      CuteQTabBarPrivateCall11 call = reinterpret_cast<CuteQTabBarPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[12]) {
      int handled = 0;
      CuteQTabBarPrivateCall12 call = reinterpret_cast<CuteQTabBarPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[13]) {
      int handled = 0;
      CuteQTabBarPrivateCall13 call = reinterpret_cast<CuteQTabBarPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[14]) {
      int handled = 0;
      CuteQTabBarPrivateCall14 call = reinterpret_cast<CuteQTabBarPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[15]) {
      int handled = 0;
      CuteQTabBarPrivateCall15 call = reinterpret_cast<CuteQTabBarPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[16]) {
      int handled = 0;
      CuteQTabBarPrivateCall16 call = reinterpret_cast<CuteQTabBarPrivateCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[17]) {
      int handled = 0;
      CuteQTabBarPrivateCall17 call = reinterpret_cast<CuteQTabBarPrivateCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QTabBar *QTabBarPrivate::q_func()
extern "C" Q_DECL_EXPORT
QTabBar *ritual_ZN14QTabBarPrivate6q_funcEv(QTabBarPrivate *self) {
  return self->q_func();
}

//  const QTabBar *QTabBarPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QTabBar *ritual_ZNK14QTabBarPrivate6q_funcEv(
    const QTabBarPrivate *self) {
  return self->q_func();
}

//  QTabBarPrivate::QTabBarPrivate()
extern "C" Q_DECL_EXPORT
QTabBarPrivate *ritual_ZN14QTabBarPrivateC1Ev() {
  return new CuteQTabBarPrivate();
}

//  QTabBarPrivate::~QTabBarPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTabBarPrivateD1Ev(QTabBarPrivate *self) {
  delete self;
}

//  void QTabBarPrivate::calculateFirstLastVisible(int index, bool visible,
//      bool remove)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTabBarPrivate25calculateFirstLastVisibleEibb(
    QTabBarPrivate *self,
    int index,
    bool visible,
    bool remove) {
  self->calculateFirstLastVisible(index, visible, remove);
}

//  int QTabBarPrivate::selectNewCurrentIndexFrom(int currentIndex)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QTabBarPrivate25selectNewCurrentIndexFromEi(
    QTabBarPrivate *self,
    int currentIndex) {
  return self->selectNewCurrentIndexFrom(currentIndex);
}

//  int QTabBarPrivate::calculateNewPosition(int from, int to, int index)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QTabBarPrivate20calculateNewPositionEiii(
    const QTabBarPrivate *self,
    int from,
    int to,
    int index) {
  return self->calculateNewPosition(from, to, index);
}

//  void QTabBarPrivate::slide(int from, int to)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTabBarPrivate5slideEii(
    QTabBarPrivate *self,
    int from,
    int to) {
  self->slide(from, to);
}

//  void QTabBarPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTabBarPrivate4initEv(QTabBarPrivate *self) {
  self->init();
}

//  Tab *QTabBarPrivate::at(int index)
extern "C" Q_DECL_EXPORT
QTabBarPrivate::Tab *ritual_ZN14QTabBarPrivate2atEi(
    QTabBarPrivate *self,
    int index) {
  return self->at(index);
}

//  const Tab *QTabBarPrivate::at(int index) const
extern "C" Q_DECL_EXPORT
const QTabBarPrivate::Tab *ritual_ZNK14QTabBarPrivate2atEi(
    const QTabBarPrivate *self,
    int index) {
  return self->at(index);
}

//  int QTabBarPrivate::indexAtPos(const QPoint &p) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QTabBarPrivate10indexAtPosERK6QPoint(
    const QTabBarPrivate *self,
    const QPoint *p) {
  return self->indexAtPos(*p);
}

//  bool QTabBarPrivate::isAnimated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QTabBarPrivate10isAnimatedEv(const QTabBarPrivate *self) {
  return self->isAnimated();
}

//  bool QTabBarPrivate::validIndex(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QTabBarPrivate10validIndexEi(
    const QTabBarPrivate *self,
    int index) {
  return self->validIndex(index);
}

//  void QTabBarPrivate::setCurrentNextEnabledIndex(int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTabBarPrivate26setCurrentNextEnabledIndexEi(
    QTabBarPrivate *self,
    int offset) {
  self->setCurrentNextEnabledIndex(offset);
}

//  void QTabBarPrivate::scrollTabs()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTabBarPrivate10scrollTabsEv(QTabBarPrivate *self) {
  self->scrollTabs();
}

//  void QTabBarPrivate::closeTab()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTabBarPrivate8closeTabEv(QTabBarPrivate *self) {
  self->closeTab();
}

//  void QTabBarPrivate::moveTab(int index, int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTabBarPrivate7moveTabEii(
    QTabBarPrivate *self,
    int index,
    int offset) {
  self->moveTab(index, offset);
}

//  void QTabBarPrivate::moveTabFinished(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTabBarPrivate15moveTabFinishedEi(
    QTabBarPrivate *self,
    int index) {
  self->moveTabFinished(index);
}

//  void QTabBarPrivate::refresh()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTabBarPrivate7refreshEv(QTabBarPrivate *self) {
  self->refresh();
}

//  void QTabBarPrivate::layoutTabs()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTabBarPrivate10layoutTabsEv(QTabBarPrivate *self) {
  self->layoutTabs();
}

//  void QTabBarPrivate::layoutWidgets(int start)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTabBarPrivate13layoutWidgetsEi(
    QTabBarPrivate *self,
    int start) {
  self->layoutWidgets(start);
}

//  void QTabBarPrivate::layoutTab(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTabBarPrivate9layoutTabEi(QTabBarPrivate *self, int index) {
  self->layoutTab(index);
}

//  void QTabBarPrivate::updateMacBorderMetrics()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTabBarPrivate22updateMacBorderMetricsEv(
    QTabBarPrivate *self) {
  self->updateMacBorderMetrics();
}

//  void QTabBarPrivate::setupMovableTab()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTabBarPrivate15setupMovableTabEv(QTabBarPrivate *self) {
  self->setupMovableTab();
}

//  void QTabBarPrivate::autoHideTabs()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTabBarPrivate12autoHideTabsEv(QTabBarPrivate *self) {
  self->autoHideTabs();
}

//  QRect QTabBarPrivate::scrollRect(int index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK14QTabBarPrivate10scrollRectEi(
    const QTabBarPrivate *self,
    int index) {
  return new QRect(self->scrollRect(index));
}

//  QRect QTabBarPrivate::normalizedScrollRect(int index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK14QTabBarPrivate20normalizedScrollRectEi(
    const QTabBarPrivate *self,
    int index) {
  return new QRect(self->normalizedScrollRect(index));
}

//  int QTabBarPrivate::hoveredTabIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QTabBarPrivate15hoveredTabIndexEv(
    const QTabBarPrivate *self) {
  return self->hoveredTabIndex();
}

//  void QTabBarPrivate::initBasicStyleOption(QStyleOptionTab *option, int
//      tabIndex) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QTabBarPrivate20initBasicStyleOptionEP15QStyleOptionTabi(
    const QTabBarPrivate *self,
    QStyleOptionTab *option,
    int tabIndex) {
  self->initBasicStyleOption(option, tabIndex);
}

//  void QTabBarPrivate::makeVisible(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTabBarPrivate11makeVisibleEi(
    QTabBarPrivate *self,
    int index) {
  self->makeVisible(index);
}

//  const Tab *QTabBarPrivate::lastVisibleTab() const
extern "C" Q_DECL_EXPORT
const QTabBarPrivate::Tab *ritual_ZNK14QTabBarPrivate14lastVisibleTabEv(
    const QTabBarPrivate *self) {
  return self->lastVisibleTab();
}

//  void QTabBarPrivate::initStyleBaseOption(QStyleOptionTabBarBase
//      *optTabBase, QTabBar *tabbar, QSize size)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTabBarPrivate19initStyleBaseOptionEP22QStyleOptionTabBarBaseP7QTabBar5QSize(
    QStyleOptionTabBarBase *optTabBase,
    QTabBar *tabbar,
    const QSize *size) {
  QTabBarPrivate::initStyleBaseOption(optTabBase, tabbar, *size);
}

//  void QTabBarPrivate::killSwitchTabTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTabBarPrivate18killSwitchTabTimerEv(QTabBarPrivate *self) {
  self->killSwitchTabTimer();
}

//  a Python function taken by a CuteQTabBarPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTabBarPrivate(
    QTabBarPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTabBarPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(tabbar)
